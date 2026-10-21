#!/usr/bin/env python3
"""Run deterministic pytest shards and calculate combined statement coverage.

Can be executed in stages in constrained environments:
  python scripts/run_coverage_shards.py --shards 8 --shard-range 1-4 --keep-coverage-data
  python scripts/run_coverage_shards.py --shards 8 --shard-range 5-8 --append-coverage
The runner tracks completed shards and collection fingerprint so it refuses to report
combined coverage until every shard from the same test inventory has succeeded.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BACKEND=ROOT/"backend"
LINE_RE=re.compile(r"tests/(test_[^:]+\.py)::")


def run(cmd:list[str], *, cwd:Path, env:dict[str,str]|None=None)->subprocess.CompletedProcess[str]:
    return subprocess.run(cmd,cwd=cwd,env=env,text=True,stdout=None,stderr=None)


def collect(py:str, env:dict[str,str])->dict[str,int]:
    proc=subprocess.run([py,"-m","pytest","--collect-only","-q","-o","addopts=","tests"],cwd=BACKEND,env=env,text=True,capture_output=True)
    if proc.returncode:
        sys.stdout.write(proc.stdout); sys.stderr.write(proc.stderr)
        raise RuntimeError("pytest collection failed")
    counts:dict[str,int]={}
    for line in (proc.stdout+"\n"+proc.stderr).splitlines():
        match=LINE_RE.match(line.strip())
        if match:
            name="tests/"+match.group(1); counts[name]=counts.get(name,0)+1
    if not counts: raise RuntimeError("could not parse pytest's collected test ids")
    return counts


def make_bins(counts:dict[str,int], shards:int)->list[list[str]]:
    if not isinstance(shards, int) or isinstance(shards, bool) or not 1 <= shards <= 20:
        raise ValueError("shards must be an integer from 1 to 20")
    if not counts or any(not isinstance(name, str) or not name for name in counts):
        raise ValueError("counts must contain at least one non-empty module name")
    if any(not isinstance(count, int) or isinstance(count, bool) or count < 1 for count in counts.values()):
        raise ValueError("each module count must be a positive integer")
    bins=[[] for _ in range(min(shards,len(counts)))]
    weights=[0 for _ in bins]
    for name,count in sorted(counts.items(),key=lambda item:(-item[1],item[0])):
        idx=min(range(len(bins)),key=lambda i:weights[i])
        bins[idx].append(name); weights[idx]+=count
    return bins


def parse_shard_range(value: str, shard_count: int) -> list[int]:
    """Parse a 1-based inclusive range, or an empty value meaning all shards."""
    if not isinstance(shard_count, int) or shard_count < 1:
        raise ValueError("shard_count must be positive")
    if not value:
        return list(range(1, shard_count + 1))
    if not isinstance(value, str) or any(ch.isspace() for ch in value):
        raise ValueError(f"range must be a 1-based inclusive range within 1-{shard_count}")
    try:
        start_s, end_s = value.split("-", 1)
        start, end = int(start_s), int(end_s)
        if not 1 <= start <= end <= shard_count:
            raise ValueError
    except (ValueError, AttributeError) as exc:
        raise ValueError(f"range must be a 1-based inclusive range within 1-{shard_count}") from exc
    return list(range(start, end + 1))


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shards",type=int,default=8)
    parser.add_argument("--min-coverage",type=float,default=80.0)
    parser.add_argument("--coverage-json",default="",help="Optional path for a JSON coverage summary")
    parser.add_argument("--shard-range",default="",help="1-based inclusive range, e.g. 1-4; default runs every shard")
    parser.add_argument("--append-coverage",action="store_true",help="Append to a previously staged coverage run")
    parser.add_argument("--keep-coverage-data",action="store_true",help="Keep data/state after this stage without reporting final coverage")
    parser.add_argument("--coverage-file",default=str(BACKEND/".coverage"),help="Coverage data path")
    args=parser.parse_args()
    if args.shards<1 or args.shards>20: parser.error("--shards must be between 1 and 20")
    if not (0 <= args.min_coverage <= 100): parser.error("--min-coverage must be between 0 and 100")
    py=sys.executable
    env=os.environ.copy(); env["PYTHONPATH"]="."; coverage_file=Path(args.coverage_file).resolve(); coverage_file.parent.mkdir(parents=True,exist_ok=True)
    env["COVERAGE_FILE"]=str(coverage_file)
    state_path=coverage_file.with_name(coverage_file.name.lstrip(".")+"-shard-state.json")
    try: counts=collect(py,env)
    except RuntimeError as exc: print(f"ERROR: {exc}",file=sys.stderr); return 2
    bins=make_bins(counts,args.shards)
    shard_count=len(bins)
    weights=[sum(counts[name] for name in group) for group in bins]
    try:
        selected=parse_shard_range(args.shard_range, shard_count)
    except ValueError as exc:
        parser.error(str(exc))
    fingerprint=hashlib.sha256(json.dumps({"counts":counts,"shards":shard_count},sort_keys=True).encode()).hexdigest()
    if args.append_coverage:
        if not state_path.is_file() or not coverage_file.is_file():
            print("ERROR: --append-coverage requires existing staged data and shard state",file=sys.stderr); return 2
        try: state=json.loads(state_path.read_text(encoding="utf-8"))
        except Exception: print("ERROR: prior coverage shard state is invalid",file=sys.stderr); return 2
        if state.get("fingerprint") != fingerprint or state.get("shard_count") != shard_count:
            print("ERROR: test collection changed since the previous coverage stage; restart without --append-coverage",file=sys.stderr); return 2
        completed=set(int(i) for i in state.get("completed_shards",[]))
    else:
        if not args.shard_range and args.keep_coverage_data:
            parser.error("--keep-coverage-data is meant for a staged --shard-range run")
        subprocess.run([py,"-m","coverage","erase"],cwd=BACKEND,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        state={"fingerprint":fingerprint,"shard_count":shard_count,"test_module_count":len(counts),"test_cases_collected":sum(counts.values()),"completed_shards":[]}
        completed=set()
        state_path.unlink(missing_ok=True)
    duplicate=completed.intersection(selected)
    if duplicate:
        print(f"ERROR: shards already recorded as complete: {sorted(duplicate)}; restart or choose remaining shards",file=sys.stderr); return 2
    failures=[]
    with tempfile.TemporaryDirectory(prefix="firewatch-v9-coverage-") as td:
        for idx in selected:
            files=bins[idx-1]
            junit=Path(td)/f"junit-{idx}.xml"
            print(f"\n=== Coverage shard {idx}/{shard_count}: {weights[idx-1]} collected cases across {len(files)} modules ===",flush=True)
            cmd=[py,"-m","pytest",*files,"-q","--cov=app","--cov-append","--cov-report=", "--junitxml",str(junit)]
            result=run(cmd,cwd=BACKEND,env=env)
            shard_failed=result.returncode != 0
            if junit.exists():
                import xml.etree.ElementTree as ET
                try:
                    doc=ET.parse(junit).getroot(); suites=[doc] if doc.tag=="testsuite" else list(doc.iter("testsuite"))
                    shard_failed = shard_failed or any(int(x.attrib.get("failures","0")) or int(x.attrib.get("errors","0")) for x in suites)
                    for suite in suites:
                        if int(suite.attrib.get("skipped","0")):
                            print(f"NOTE: shard {idx} reported {suite.attrib.get('skipped')} skipped tests",flush=True)
                except Exception:
                    shard_failed=True; print(f"Could not parse JUnit summary for shard {idx}",file=sys.stderr)
            if shard_failed: failures.append(idx)
            else:
                completed.add(idx); state["completed_shards"]=sorted(completed)
                state_path.write_text(json.dumps(state,indent=2)+"\n",encoding="utf-8")
        if failures:
            print(f"FAIL: coverage shard(s) failed: {sorted(set(failures))}",file=sys.stderr)
            return 1
        if args.keep_coverage_data:
            print(f"STAGED: completed shards {sorted(completed)} of {shard_count}. Run remaining shards with --append-coverage.",flush=True)
            return 0
        if len(completed) != shard_count:
            print(f"ERROR: cannot report combined coverage; completed shards are {sorted(completed)} of 1..{shard_count}",file=sys.stderr)
            return 2
        temp_json=Path(td)/"coverage.json"
        report=subprocess.run([py,"-m","coverage","json","-o",str(temp_json)],cwd=BACKEND,env=env,text=True,capture_output=True)
        if report.returncode:
            print(report.stdout); print(report.stderr,file=sys.stderr); return report.returncode
        coverage=json.loads(temp_json.read_text(encoding="utf-8")); percent=float(coverage.get("totals",{}).get("percent_covered",0.0))
        display=run([py,"-m","coverage","report","--fail-under",str(args.min_coverage)],cwd=BACKEND,env=env)
        if display.returncode: return display.returncode
        summary={"test_cases_collected":sum(counts.values()),"test_module_count":len(counts),"shards":shard_count,"coverage_percent":percent,"minimum_percent":args.min_coverage,"failures":0,"skipped":0,"completed_shards":sorted(completed),"collection_fingerprint":fingerprint}
        if args.coverage_json: Path(args.coverage_json).write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
        print(f"RESULT: {sum(counts.values())} collected cases across {len(counts)} modules; {shard_count} coverage shards; statement coverage {percent:.2f}%; failures: 0",flush=True)
    subprocess.run([py,"-m","coverage","erase"],cwd=BACKEND,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    state_path.unlink(missing_ok=True)
    return 0

if __name__=="__main__": raise SystemExit(main())
