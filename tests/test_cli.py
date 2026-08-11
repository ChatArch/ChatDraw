from click.testing import CliRunner

from chatdraw.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert "0.1.1" in result.output


def test_top_level_help_exposes_tree_and_not_scaffold_hello():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "hello" not in result.output.lower()


def test_tree_option_renders_truthful_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert "chatdraw" in result.output
    assert "--help" in result.output
    assert "--version" in result.output
    assert "--tree" in result.output
    assert "hello" not in result.output.lower()


def test_scaffold_hello_command_is_removed():
    result = CliRunner().invoke(main, ["hello", "ChatArch"])

    assert result.exit_code != 0
    assert "No such command" in result.output
