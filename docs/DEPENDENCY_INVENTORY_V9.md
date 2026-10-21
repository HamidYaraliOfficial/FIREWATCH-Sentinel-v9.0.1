# FIREWATCH v9.0.1 — Declared Dependency Inventory

Declared entries: **17**

> This inventory is not a resolved SBOM and is not a vulnerability audit.

| Package | Extras | Declared constraint | Marker | Requirement files |
|---|---|---|---|---|
| `bandit` | — | `==1.9.4` | `—` | `backend/requirements-dev.txt` |
| `beautifulsoup4` | — | `==4.14.3` | `—` | `backend/requirements.txt` |
| `cryptography` | — | `>=44,<47` | `—` | `backend/requirements.txt` |
| `fastapi` | — | `==0.141.1` | `—` | `backend/requirements.txt` |
| `httpcore` | — | `==1.0.9` | `—` | `backend/requirements.txt` |
| `httpx` | — | `==0.28.1` | `—` | `backend/requirements.txt` |
| `Jinja2` | — | `==3.1.6` | `—` | `backend/requirements.txt` |
| `pip-audit` | — | `==2.10.1` | `—` | `backend/requirements-dev.txt` |
| `playwright` | — | `==1.63.0` | `—` | `backend/requirements.txt` |
| `psycopg` | binary | `>=3.2,<4` | `—` | `backend/requirements.txt` |
| `pytest` | — | `==9.0.2` | `—` | `backend/requirements-dev.txt` |
| `pytest-asyncio` | — | `>=1.0,<2` | `—` | `backend/requirements-dev.txt` |
| `pytest-cov` | — | `==7.0.0` | `—` | `backend/requirements-dev.txt` |
| `python-multipart` | — | `>=0.0.20,<1` | `—` | `backend/requirements.txt` |
| `PyYAML` | — | `==6.0.3` | `—` | `backend/requirements.txt` |
| `SQLAlchemy` | — | `==2.0.54` | `—` | `backend/requirements.txt` |
| `uvicorn` | standard | `==0.48.0` | `—` | `backend/requirements.txt` |

## Limitations

- This is a declared-requirements inventory, not a resolved SBOM.
- Constraint ranges are not resolved to installed artifact versions.
- Transitive dependency closure and vulnerability status are not implied.
- Run pip-audit in a trusted environment with package index access before release/deployment.
