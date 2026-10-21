#!/usr/bin/env bash
# Interactive, non-force-pushing publisher for the official FIREWATCH repository.
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="${FIREWATCH_GITHUB_REPO:-HamidYaraliOfficial/FIREWATCH-WebSec-Agent}"
DESCRIPTION="Scope-controlled, evidence-driven web application security assessment platform with safe discovery, API inventory, and multi-format reporting."
cd "$ROOT"

fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
need() { command -v "$1" >/dev/null 2>&1 || fail "Required command not found: $1"; }

need git
need gh
need python
need node

printf '\nFIREWATCH GitHub publishing preflight\nRepository: %s\n\n' "$REPO"
gh auth status >/dev/null || fail "GitHub CLI is not authenticated. Run: gh auth login"
python scripts/verify_release.py || fail "Release verification failed. Resolve the checks above before publishing."

if [[ -d .git ]]; then
  git diff --cached --quiet || fail "There are already staged changes. Review/commit them before using this publisher."
else
  git init
fi
git branch -M main

git add -A
printf '\nFiles staged for publishing (review this list):\n'
git status --short
printf '\nThis script will publish code to GitHub. It will never force-push.\n'
read -r -p "Type PUSH to continue: " CONFIRM
if [[ "$CONFIRM" != "PUSH" ]]; then
  git reset -q
  printf 'Cancelled. Files were left unchanged; newly staged changes were unstaged.\n'
  exit 0
fi

if ! git diff --cached --quiet; then
  git commit -m "feat: release FIREWATCH Sentinel v9.0.1"
fi

if gh repo view "$REPO" --json name >/dev/null 2>&1; then
  printf 'GitHub repository already exists: %s\n' "$REPO"
else
  printf '\nChoose repository visibility. Public repositories can be cloned by anyone.\n'
  while true; do
    read -r -p "Visibility [private/public] (default private): " VISIBILITY
    VISIBILITY="${VISIBILITY:-private}"
    case "$VISIBILITY" in
      private|public) break ;;
      *) printf 'Enter private or public.\n' ;;
    esac
  done
  gh repo create "$REPO" "--$VISIBILITY" --description "$DESCRIPTION" || fail "GitHub repository creation failed. Check permissions and whether the repository already exists."
fi

EXPECTED_HTTPS="https://github.com/${REPO}.git"
if git remote get-url origin >/dev/null 2>&1; then
  ORIGIN="$(git remote get-url origin)"
  case "$ORIGIN" in
    "https://github.com/${REPO}"|"https://github.com/${REPO}.git"|"git@github.com:${REPO}"|"git@github.com:${REPO}.git") ;;
    *) fail "Existing origin is '$ORIGIN', not '$REPO'. Review it manually; publisher will not overwrite it." ;;
  esac
else
  git remote add origin "$EXPECTED_HTTPS"
fi

git push -u origin main
printf '\nPublished successfully: https://github.com/%s\n' "$REPO"
printf 'Next: review Actions/CodeQL, then create a release tag only after CI passes.\n'
