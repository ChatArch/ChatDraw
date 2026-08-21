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
    for path in (Path("docs/cli-tree.md"), Path("docs/cli-tree.en.md")):
        assert path.exists()
        text = path.read_text(encoding="utf-8")
        assert "chatstyle.add_tree_option()" in text
        assert "chatdraw --tree" in text
        assert "chatdraw --tree-brief" in text
        assert "└── --tree-brief" in text
