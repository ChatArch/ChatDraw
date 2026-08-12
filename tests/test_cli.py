from click.testing import CliRunner

from chatdraw.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert "0.1.2" in result.output


def test_top_level_help_exposes_tree_and_not_scaffold_hello():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "hello" not in result.output.lower()


def test_tree_option_renders_truthful_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert "chatdraw  # ChatDraw drawing assistant package shell" in result.output
    assert "├── --help  # show command help" in result.output
    assert "├── --version  # show the installed package version" in result.output
    assert "└── --tree  # show this CLI tree" in result.output
    assert "hello" not in result.output.lower()


def test_scaffold_hello_command_is_removed():
    result = CliRunner().invoke(main, ["hello", "ChatArch"])

    assert result.exit_code != 0
    assert "No such command" in result.output
