"""Deterministic declared dependency inventory parser tests."""
import importlib.util
import json
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("firewatch_dependency_inventory", ROOT / "scripts/export_dependency_inventory.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def test_v9_real_inventory_is_deterministic_and_explicitly_not_an_sbom():
    first = module.generate_inventory(ROOT)
    second = module.generate_inventory(ROOT)
    assert first == second
    assert first["application_version"] == "9.0.1"
    assert first["component_count"] == len(first["components"]) > 0
    assert "not a resolved SBOM" in " ".join(first["limitations"])
    assert all(item["resolution_status"] == "declared_constraint_not_resolved" for item in first["components"])


def test_v9_inventory_tracks_dev_and_runtime_sources():
    inventory = module.generate_inventory(ROOT)
    assert {source for item in inventory["components"] for source in item["source_files"]} >= {
        "backend/requirements.txt", "backend/requirements-dev.txt"
    }


@pytest.mark.parametrize("package", ["Foo_Bar", "foo.bar", "FOO-BAR", "foo---bar", "foo__bar"])
def test_v9_package_name_canonicalization(package):
    assert module.normalize_name(package) == "foo-bar"


@pytest.mark.parametrize("line", [
    "", "# comment", "-e .", "git+https://example.test/repo.git", "https://example.test/package.whl",
    "--index-url https://example.test/simple", "package==1.0\\nnot-a-requirement",
])
def test_v9_unsupported_requirement_lines_fail_closed(tmp_path, line):
    root = tmp_path
    req = root / "requirements.txt"
    req.write_text(line + "\n", encoding="utf-8")
    try:
        got = module.parse_requirements([req], root=root)
        assert not got
    except ValueError:
        # Direct URL/editable/options are explicitly not accepted by this inventory parser.
        assert line.startswith(("-e", "git+", "https://", "--", "package=="))


def test_v9_requirements_parser_handles_extras_constraints_and_markers(tmp_path):
    root = tmp_path
    req = root / "requirements.txt"
    req.write_text("Example_Pkg[crypto,cli]>=1.2,<3; python_version >= '3.11' # note\n", encoding="utf-8")
    parsed = module.parse_requirements([req], root=root)
    assert parsed == [{
        "name": "Example_Pkg", "normalized_name": "example-pkg", "extras": ["cli", "crypto"],
        "version_constraint": ">=1.2,<3", "environment_marker": "python_version >= '3.11'",
        "source_files": ["requirements.txt"], "resolution_status": "declared_constraint_not_resolved",
    }]


def test_v9_requirements_parser_detects_include_cycles(tmp_path):
    root = tmp_path
    a = root / "a.txt"; b = root / "b.txt"
    a.write_text("-r b.txt\n", encoding="utf-8")
    b.write_text("-r a.txt\n", encoding="utf-8")
    with pytest.raises(ValueError, match="cycle"):
        module.parse_requirements([a], root=root)


def test_v9_requirements_parser_rejects_include_outside_root(tmp_path):
    root = tmp_path / "root"; root.mkdir()
    outside = tmp_path / "outside.txt"; outside.write_text("testpkg==1.0\n", encoding="utf-8")
    req = root / "requirements.txt"; req.write_text(f"-r {outside}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="inside the repository"):
        module.parse_requirements([req], root=root)
