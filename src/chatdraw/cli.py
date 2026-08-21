"""CLI entrypoint for ChatDraw."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatdraw import __version__


@click.group(
    name="chatdraw",
    invoke_without_command=True,
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(version=__version__, prog_name="chatdraw")
@add_tree_option(renderer_options={"root_name": "chatdraw"})
def main() -> None:
    """ChatDraw drawing assistant package shell."""


if __name__ == "__main__":
    main()
