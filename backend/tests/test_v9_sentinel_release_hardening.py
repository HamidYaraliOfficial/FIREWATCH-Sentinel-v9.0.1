"""Release-hardening regression tests for FIREWATCH Sentinel v9."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from app.main import _resolve_scan_report_path, MAX_REPORT_FILE_BYTES, MAX_REPORT_BUNDLE_BYTES

SCAN_ID = "123e4567-e89b-12d3-a456-426614174000"


def test_report_path_accepts_only_files_beneath_the_scan_directory(tmp_path, monkeypatch):
    import app.main as main_module

    report_root = tmp_path / "reports"
    scan_root = report_root / SCAN_ID
    scan_root.mkdir(parents=True)
    accepted = scan_root / "report.json"
    accepted.write_text('{"ok":true}', encoding="utf-8")
    monkeypatch.setattr(main_module, "settings", SimpleNamespace(report_dir=str(report_root)))

    assert _resolve_scan_report_path(SCAN_ID, str(accepted)) == accepted.resolve()


def test_report_path_rejects_database_path_outside_scan_directory(tmp_path, monkeypatch):
    import app.main as main_module

    report_root = tmp_path / "reports"
    scan_root = report_root / SCAN_ID
    scan_root.mkdir(parents=True)
    external = tmp_path / "private.json"
    external.write_text('{"secret":"never serve"}', encoding="utf-8")
    monkeypatch.setattr(main_module, "settings", SimpleNamespace(report_dir=str(report_root)))

    assert _resolve_scan_report_path(SCAN_ID, str(external)) is None


@pytest.mark.parametrize("scan_id", ["../private", "nested/../private", "", "."])
def test_report_path_rejects_unsafe_scan_id(tmp_path, monkeypatch, scan_id):
    import app.main as main_module

    report_root = tmp_path / "reports"
    report_root.mkdir()
    monkeypatch.setattr(main_module, "settings", SimpleNamespace(report_dir=str(report_root)))
    assert _resolve_scan_report_path(scan_id, str(tmp_path / "report.json")) is None


def test_report_path_rejects_symlink_escape(tmp_path, monkeypatch):
    import app.main as main_module

    report_root = tmp_path / "reports"
    scan_root = report_root / SCAN_ID
    scan_root.mkdir(parents=True)
    external = tmp_path / "external.txt"
    external.write_text("external", encoding="utf-8")
    link = scan_root / "report.json"
    try:
        link.symlink_to(external)
    except (OSError, NotImplementedError):
        pytest.skip("Symlink creation unavailable on this platform")
    monkeypatch.setattr(main_module, "settings", SimpleNamespace(report_dir=str(report_root)))
    assert _resolve_scan_report_path(SCAN_ID, str(link)) is None


def test_report_download_limits_are_bounded_and_sane():
    assert 0 < MAX_REPORT_FILE_BYTES <= MAX_REPORT_BUNDLE_BYTES
    assert MAX_REPORT_FILE_BYTES == 32 * 1024 * 1024
    assert MAX_REPORT_BUNDLE_BYTES == 64 * 1024 * 1024


def test_api_docs_are_disabled_in_production_and_enabled_in_development():
    from app.main import api_docs_options

    assert api_docs_options("production") == {"docs_url": None, "redoc_url": None, "openapi_url": None}
    assert api_docs_options("prod") == {"docs_url": None, "redoc_url": None, "openapi_url": None}
    assert api_docs_options("development") == {"docs_url": "/docs", "redoc_url": "/redoc", "openapi_url": "/openapi.json"}
