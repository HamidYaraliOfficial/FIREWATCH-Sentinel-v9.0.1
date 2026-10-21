# FIREWATCH Dashboard v5

The dependency-free HTML/CSS/JavaScript dashboard is served by FastAPI and requires no Node build. It supports scan profiles, passive-only mode, bounded safe parameter probes, progress, findings/assets, cancellation, baseline diff and HTML/JSON/CSV/Markdown/SARIF downloads. If `FIREWATCH_API_KEY` is configured, provide it in the dashboard; it is stored in browser sessionStorage for this session only. Do not use the dashboard over an untrusted network without HTTPS and access controls.
