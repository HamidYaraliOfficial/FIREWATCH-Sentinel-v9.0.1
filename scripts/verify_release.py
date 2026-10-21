#!/usr/bin/env python3
"""Run the local FIREWATCH release gate and distinguish PASS/SKIP/FAIL."""
from __future__ import annotations
import argparse, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(label: str, command: list[str], *, cwd: Path = ROOT, env: dict[str, str] | None = None) -> str:
    print(f"\n=== {label} ===", flush=True)
    try:
        proc = subprocess.run(command, cwd=cwd, env=env, text=True)
    except FileNotFoundError:
        print(f"[SKIP] {label}: executable not installed", flush=True)
        return "skipped"
    status = "passed" if proc.returncode == 0 else "failed"
    print(f"[{status.upper()}] {label} (exit {proc.returncode})", flush=True)
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict-optional-tools", action="store_true", help="Treat missing Bandit, pip-audit, Node, Bash or Docker as failure")
    parser.add_argument("--coverage-shards", type=int, default=8)
    parser.add_argument("--coverage-shard-range", default="", help="Run a 1-based inclusive shard range, e.g. 1-4")
    parser.add_argument("--append-coverage", action="store_true", help="Append a staged coverage shard run")
    parser.add_argument("--keep-coverage-data", action="store_true", help="Keep staged coverage data for a subsequent shard range")
    args = parser.parse_args()
    statuses: list[tuple[str, str]] = []
    def record(label: str, status: str):
        statuses.append((label, status))
        return status
    def checked(label: str, command: list[str], **kwargs):
        return record(label, run(label, command, **kwargs))
    py = sys.executable

    checked("Python compilation: app, tests, demo and release scripts", [py, "-m", "compileall", "-q", "backend/app", "backend/tests", "demo_target", "scripts"])
    if shutil.which("node"):
        checked("Dashboard JavaScript syntax", ["node", "--check", "frontend/static/app.js"])
    else:
        record("Dashboard JavaScript syntax", "failed" if args.strict_optional_tools else "skipped")
        print("[SKIP] Node.js not installed; browser JavaScript syntax was not checked locally.")
    if shutil.which("bash"):
        checked("Publisher shell syntax", ["bash", "-n", "scripts/publish_to_github.sh"])
    else:
        record("Publisher shell syntax", "failed" if args.strict_optional_tools else "skipped")
        print("[SKIP] Bash not installed; shell publisher syntax was not checked locally.")

    checked("Docker Compose YAML parse", [py, "-c", "import yaml; yaml.safe_load(open('docker-compose.yml', encoding='utf-8')); print('Compose YAML OK')"])
    checked("Repository hygiene", [py, "scripts/repo_hygiene.py"])
    checked("Assessment plan export", [py, "scripts/export_assessment_plan.py"])
    checked("Test manifest generation", [py, "scripts/build_test_manifest.py"])
    checked("Declared dependency inventory generation", [py, "scripts/export_dependency_inventory.py"])

    coverage_summary = Path(tempfile.gettempdir()) / "firewatch-v9-coverage-summary.json"
    command = [py, "scripts/run_coverage_shards.py", "--shards", str(args.coverage_shards), "--min-coverage", "80", "--coverage-json", str(coverage_summary)]
    if args.coverage_shard_range:
        command += ["--shard-range", args.coverage_shard_range]
    if args.append_coverage:
        command.append("--append-coverage")
    if args.keep_coverage_data:
        command.append("--keep-coverage-data")
    coverage_status = checked("Full regression suite / combined coverage gate", command, env=os.environ.copy())
    if coverage_summary.exists():
        try:
            import json
            summary = json.loads(coverage_summary.read_text(encoding="utf-8"))
            print(f"Test report: tests={summary['test_cases_collected']} modules={summary['test_module_count']} coverage={summary['coverage_percent']:.2f}% failures={summary['failures']}")
        except Exception as exc:
            print(f"Coverage summary parsing skipped: {type(exc).__name__}")
        finally:
            coverage_summary.unlink(missing_ok=True)

    optional = [("Bandit", ["bandit", "-q", "-r", "backend/app", "-lll", "-iii"]),
                ("pip-audit", ["pip-audit", "-r", "backend/requirements.txt"])]
    for label, command in optional:
        if shutil.which(command[0]):
            checked(label, command)
        else:
            status = "failed" if args.strict_optional_tools else "skipped"
            record(label, status)
            print(f"[{status.upper()}] {label}: executable not installed; result is unverified locally.")
    if shutil.which("docker"):
        checked("Docker Compose configuration", ["docker", "compose", "config", "-q"])
    else:
        status = "failed" if args.strict_optional_tools else "skipped"
        record("Docker Compose configuration", status)
        print(f"[{status.upper()}] Docker CLI not installed; Docker image build/deployment is not verified locally.")

    passed = sum(status == "passed" for _, status in statuses)
    skipped = sum(status == "skipped" for _, status in statuses)
    failed = sum(status == "failed" for _, status in statuses)
    print(f"\nRelease verification totals: {passed} PASS, {skipped} SKIP/UNVERIFIED, {failed} FAIL.")
    for label, status in statuses:
        print(f" - {status.upper():10} {label}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
