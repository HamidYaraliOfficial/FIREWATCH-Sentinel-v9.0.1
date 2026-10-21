PYTHON ?= python

.PHONY: run test lint verify demo
run:
	PYTHONPATH=backend $(PYTHON) -m uvicorn app.main:app --host 127.0.0.1 --port 8000

test:
	$(PYTHON) -m pip install -r backend/requirements-dev.txt
	cd backend && PYTHONPATH=. $(PYTHON) -m pytest tests -q -rA --cov=app --cov-report=term-missing --cov-fail-under=78

lint:
	$(PYTHON) -m compileall -q backend/app backend/tests demo_target
	node --check frontend/static/app.js
	bash -n scripts/publish_to_github.sh
	$(PYTHON) scripts/repo_hygiene.py

verify:
	$(PYTHON) scripts/verify_release.py

# Local-only intentionally vulnerable target. Use only in an isolated lab.
demo:
	PYTHONPATH=. $(PYTHON) -m uvicorn demo_target.main:app --host 127.0.0.1 --port 8765
