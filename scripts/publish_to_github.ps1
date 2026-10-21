# Interactive, non-force-pushing publisher for the official FIREWATCH repository.
$ErrorActionPreference = 'Stop'
$Repo = if ($env:FIREWATCH_GITHUB_REPO) { $env:FIREWATCH_GITHUB_REPO } else { 'HamidYaraliOfficial/FIREWATCH-WebSec-Agent' }
$Description = 'Scope-controlled, evidence-driven web application security assessment platform with safe discovery, API inventory, and multi-format reporting.'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Push-Location $Root
try {
    foreach ($Command in @('git', 'gh', 'python', 'node')) {
        if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
            throw "Required command not found: $Command"
        }
    }

    Write-Host "`nFIREWATCH GitHub publishing preflight`nRepository: $Repo`n"
    gh auth status | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI is not authenticated. Run: gh auth login' }

    python scripts/verify_release.py
    if ($LASTEXITCODE -ne 0) { throw 'Release verification failed. Resolve the checks above before publishing.' }

    if (-not (Test-Path '.git')) { git init; if ($LASTEXITCODE -ne 0) { throw 'git init failed.' } }
    git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) { throw 'There are already staged changes. Review/commit them before using this publisher.' }
    git branch -M main
    if ($LASTEXITCODE -ne 0) { throw 'Unable to set the branch to main.' }

    git add -A
    if ($LASTEXITCODE -ne 0) { throw 'git add failed.' }
    Write-Host "`nFiles staged for publishing (review this list):"
    git status --short
    Write-Host "`nThis script will publish code to GitHub. It will never force-push."
    $Confirm = Read-Host 'Type PUSH to continue'
    if ($Confirm -cne 'PUSH') {
        git reset -q
        Write-Host 'Cancelled. Files were left unchanged; newly staged changes were unstaged.'
        return
    }

    git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) {
        git commit -m 'feat: release FIREWATCH Sentinel v9.0.1'
        if ($LASTEXITCODE -ne 0) { throw 'git commit failed. Set git user.name and user.email, then retry.' }
    }

    gh repo view $Repo --json name | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`nPublic repositories can be cloned by anyone."
        do { $Visibility = Read-Host 'Visibility [private/public] (default private)'; if (-not $Visibility) { $Visibility = 'private' } } until ($Visibility -in @('private', 'public'))
        gh repo create $Repo "--$Visibility" --description $Description
        if ($LASTEXITCODE -ne 0) { throw 'GitHub repository creation failed. Check permissions and whether it already exists.' }
    }
    else {
        Write-Host "GitHub repository already exists: $Repo"
    }

    $Expected = "https://github.com/$Repo.git"
    $Origin = git remote get-url origin 2>$null
    if ($LASTEXITCODE -eq 0 -and $Origin) {
        $NormalizedOrigin = $Origin.TrimEnd('/') -replace '\.git$', ''
        $NormalizedExpected = $Expected -replace '\.git$', ''
        if ($NormalizedOrigin -ne $NormalizedExpected -and $Origin -ne "git@github.com:$Repo.git" -and $Origin -ne "git@github.com:$Repo") {
            throw "Existing origin is '$Origin', not '$Repo'. Review it manually; publisher will not overwrite it."
        }
    }
    else {
        git remote add origin $Expected
        if ($LASTEXITCODE -ne 0) { throw 'Unable to configure origin remote.' }
    }

    git push -u origin main
    if ($LASTEXITCODE -ne 0) { throw 'Push failed. No force-push was attempted. Review remote history/permissions and retry.' }
    Write-Host "`nPublished successfully: https://github.com/$Repo"
    Write-Host 'Next: review Actions/CodeQL, then create a release tag only after CI passes.'
}
finally {
    Pop-Location
}
