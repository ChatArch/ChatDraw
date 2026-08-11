"""CLI entrypoint for ChatDraw."""

from __future__ import annotations

import click

from chatdraw import __version__


_TREE = """chatdraw # ChatDraw — drawing assistant package shell.
├── --help # Show this message and exit.
├── --version # Show the version and exit.
└── --tree # Print the registered command tree.
"""


def _print_tree(ctx: click.Context, _param: click.Parameter, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo(_TREE.rstrip())
    ctx.exit(0)


@click.group(name="chatdraw", invoke_without_command=False)
@click.version_option(version=__version__, prog_name="chatdraw")
@click.option(
    "--tree",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=_print_tree,
    help="Print the registered command tree.",
)
def main() -> None:
    """ChatDraw drawing assistant package shell."""


if __name__ == "__main__":
    main()
