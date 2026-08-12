from pathlib import Path


def test_publish_workflow_uses_oidc_with_release_guards():
    workflow = Path(".github/workflows/publish.yml").read_text(encoding="utf-8")

    assert "id-token: write" in workflow
    assert "pypa/gh-action-pypi-publish@release/v1" in workflow
    assert "Check tag matches package version" in workflow
    assert "Check release commit is on default branch" in workflow
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in workflow
    assert "git merge-base --is-ancestor \"${GITHUB_SHA}\" refs/remotes/origin/main" in workflow
    assert "Check PyPI version" in workflow
    legacy_environment_marker = "environment" + ": pypi"
    assert legacy_environment_marker not in workflow


def test_preview_workflow_uses_public_docs_domain_from_mkdocs():
    workflow = Path(".github/workflows/preview.yaml").read_text(encoding="utf-8")

    assert "site_url" in workflow
    assert "CHATARCH_PREVIEW_URL" in workflow
    assert "${site_url}/dev/" in workflow
    assert "github.io/${repo}/dev" not in workflow
    assert "Preview available at:" in workflow


def test_deploy_workflow_exists_for_main_docs():
    workflow = Path(".github/workflows/deploy.yaml").read_text(encoding="utf-8")

    assert "mkdocs gh-deploy --force" in workflow
    assert "branches:" in workflow
    assert "main" in workflow
