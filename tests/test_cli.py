import click
from click.testing import CliRunner

from chatdraw import __version__
from chatdraw.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatdraw, version {__version__}" in result.output


def test_top_level_help_exposes_tree_options_and_not_scaffold_hello():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "Print the registered CLI tree and exit." in result.output
    assert "--tree-brief" in result.output
    assert "without parameter signatures" in result.output
    assert "hello" not in result.output.lower()


def test_tree_option_renders_truthful_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chatdraw"
    assert "├── --help  # Show this message and exit." in result.output
    assert "├── --version  # Show the version and exit." in result.output
    assert "├── --tree  # Print the registered CLI tree and exit." in result.output
    assert (
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit."
        in result.output
    )
    assert "hello" not in result.output.lower()


def test_tree_defaults_to_signatures_and_brief_omits_them():
    @click.command(name="render", help="Render one drawing.")
    @click.argument("source")
    @click.option("--format", "output_format")
    def render(source: str, output_format: str | None) -> None:
        del source, output_format

    main.add_command(render)
    try:
        full = CliRunner().invoke(main, ["--tree"])
        brief = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("render", None)

    assert full.exit_code == 0, full.output
    assert brief.exit_code == 0, brief.output
    assert "render <SOURCE> [--format OUTPUT-FORMAT]  # Render one drawing." in full.output
    assert "render  # Render one drawing." in brief.output
    assert "<SOURCE>" not in brief.output
    assert "[--format OUTPUT-FORMAT]" not in brief.output


def test_scaffold_hello_command_is_removed():
    help_result = CliRunner().invoke(main, ["--help"])
    tree_result = CliRunner().invoke(main, ["--tree"])
    brief_result = CliRunner().invoke(main, ["--tree-brief"])
    missing_result = CliRunner().invoke(main, ["hello", "ChatArch"])

    assert help_result.exit_code == 0, help_result.output
    assert tree_result.exit_code == 0, tree_result.output
    assert brief_result.exit_code == 0, brief_result.output
    assert "hello" not in help_result.output.lower()
    assert "hello" not in tree_result.output.lower()
    assert "hello" not in brief_result.output.lower()
    assert missing_result.exit_code != 0
    assert "No such command" in missing_result.output


def test_tree_root_uses_public_console_command_in_module_mode():
    result = CliRunner().invoke(main, ["--tree"], prog_name="python -m chatdraw.cli")

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chatdraw"
    assert "python -m chatdraw.cli" not in result.output
