from pathlib import Path


def test_mkdocs_uses_chatarch_public_domain_material_i18n_and_renderer():
    mkdocs = Path("mkdocs.yml").read_text(encoding="utf-8")

    assert "site_url: https://arch.gh.wzhecnu.cn/ChatDraw/" in mkdocs
    assert "repo_url: https://github.com/ChatArch/ChatDraw" in mkdocs
    assert "name: material" in mkdocs
    assert "mkdocs-static-i18n" in Path("pyproject.toml").read_text(encoding="utf-8")
    assert "- i18n:" in mkdocs
    assert "docs_structure: suffix" in mkdocs
    assert "pymdownx.emoji" in mkdocs
    assert "material.extensions.emoji.twemoji" in mkdocs
    assert "material.extensions.emoji.to_svg" in mkdocs


def test_bilingual_cli_tree_docs_exist():
    assert Path("docs/cli-tree.md").exists()
    assert Path("docs/cli-tree.en.md").exists()
    assert "chatdraw --tree" in Path("docs/cli-tree.md").read_text(encoding="utf-8")
    assert "chatdraw --tree" in Path("docs/cli-tree.en.md").read_text(encoding="utf-8")
