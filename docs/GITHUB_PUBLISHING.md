# Publish FIREWATCH v9 to GitHub

This folder is prepared as a clean source release. It does not contain a `.git` directory or an authenticated session, so publishing remains an explicit action by the repository owner.

## 0. Preferred: interactive publisher script

The release includes a helper for both Bash and Windows PowerShell. It runs repository hygiene, Python compilation, dashboard JavaScript syntax validation, and the full pytest suite; stages files for review; requires typing `PUSH`; asks you to choose public/private visibility if the repository does not yet exist; checks the `origin` remote; and uses a normal push (never force-pushes). It does not store a GitHub token in the repository.

**Linux / macOS / Git Bash** (from the project root):

```bash
python -m pip install -r backend/requirements-dev.txt
bash scripts/publish_to_github.sh
```

**Windows PowerShell** (from the project root):

```powershell
py -m pip install -r backend/requirements-dev.txt
.\scripts\publish_to_github.ps1
```

Install Git, Node.js, Python, and the [GitHub CLI](https://cli.github.com/), then authenticate with `gh auth login`. Carefully review the staged file list before typing `PUSH`. The default repository is `HamidYaraliOfficial/FIREWATCH-WebSec-Agent`; override it with `FIREWATCH_GITHUB_REPO` only if you intentionally want another repository.

## 1. Create an empty GitHub repository

Open <https://github.com/new> while signed in as `HamidYaraliOfficial`.

Recommended settings:

- **Repository name:** `FIREWATCH-WebSec-Agent`
- **Description:** `Scope-controlled, evidence-driven web application security assessment platform with safe discovery, API inventory, and multi-format reporting.`
- **Visibility:** Public if you intend open-source distribution; otherwise choose Private first.
- Do **not** initialize it with a README, `.gitignore`, or license. Those files are already in this release.

## 2. Extract the ZIP and open a terminal

Extract `FIREWATCH-Sentinel-v9.0.1.zip`. Enter the extracted folder that contains `README.md`, `backend/`, and `frontend/`.

Run the local checks first:

```bash
python scripts/repo_hygiene.py
python -m compileall -q backend/app
node --check frontend/static/app.js
python -m pip install -r backend/requirements-dev.txt
cd backend
PYTHONPATH=. python -m pytest tests -q -rA
cd ..
```

## 2A. Windows PowerShell checks

From the extracted project root in PowerShell:

```powershell
py -m pip install -r backend/requirements-dev.txt
python scripts/repo_hygiene.py
python -m compileall -q backend/app
node --check frontend/static/app.js
Push-Location backend
$env:PYTHONPATH = "."
python -m pytest -q -rA
Pop-Location
```

Install Git and the GitHub CLI (`gh`) first if they are not present. Authenticate with `gh auth login`, then verify with `gh auth status`.

## 3. Manual initialize and push (alternative)

```bash
git init
git add .
git status --short
git commit -m "feat: release FIREWATCH Sentinel v9.0.1"
git branch -M main
git remote add origin https://github.com/HamidYaraliOfficial/FIREWATCH-WebSec-Agent.git
git push -u origin main
```

Review `git status --short` before commit. Do not add `.env`, local databases, `.firewatch/`, `secret.key`, real scan reports, customer URLs, authentication tokens, or production evidence. The project `.gitignore` covers common runtime files; it cannot know every secret in your environment.

If `git remote add origin` says `origin` already exists, check `git remote -v` before changing it. If Git asks for credentials, use the GitHub credential manager or GitHub CLI; do not paste a personal access token into source files or commit history. Check availability when creating the repository; a local package cannot reserve a GitHub repository name.

## Alternative: GitHub CLI

After installing and authenticating `gh`, from the project root:

```bash
gh auth status
gh repo create HamidYaraliOfficial/FIREWATCH-WebSec-Agent --public --source=. --remote=origin --push
```

Use `--private` instead of `--public` if you want a private repository. Do not create the repository twice; use either the web UI sequence or the CLI sequence.

## 4. Verify the release on GitHub

After pushing:

1. Open `https://github.com/HamidYaraliOfficial/FIREWATCH-WebSec-Agent`.
2. Confirm the root README renders and `frontend/index.html` is present.
3. Open **Actions** and confirm the CI workflow passes.
4. Confirm the CodeQL workflow starts (initial scans can take longer than unit CI).
5. Add repository topics such as `web-security`, `application-security`, `owasp`, `fastapi`, `playwright`, `api-security`, `security-testing`, and `devsecops`.
6. Set the repository description and website/social preview in **Settings → General** if desired.
7. Create a release tag only after CI passes:

```bash
git tag -a v9.0.1 -m "FIREWATCH Sentinel v9.0.1"
git push origin v9.0.1
```

## 5. Suggested GitHub repository settings

- Enable Issues and Discussions only if you plan to maintain them.
- Use **Settings → Rules → Rulesets** to protect `main` and require CI checks for pull requests.
- Keep private vulnerability reports out of public Issues; follow `SECURITY.md`.
- Enable Dependabot alerts and secret scanning when available for the repository/plan.
- Never commit generated reports from real targets unless you have reviewed and sanitized every field and are authorized to publish them.
