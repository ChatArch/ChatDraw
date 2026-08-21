# CLI Tree

The top-level Click group uses `chatstyle.add_tree_option()` to generate full and brief views from the real registered command surface. `ChatDraw` currently exposes only root-level package information entries and no business subcommands; the template `hello` command has been removed and must not be kept as a public compatibility surface.

## Full command tree

```text
chatdraw
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatdraw --tree` keeps command parameter signatures by default. There are currently no business commands, so the output contains only root pseudo-options without parameters.

## Brief command tree

```text
chatdraw
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatdraw --tree-brief` keeps the same nodes and purpose comments while omitting parameter signatures, so its current output matches the full tree.

## Status contract

- `chatdraw --help` must expose `--tree` and `--tree-brief`.
- `chatdraw --tree` and `chatdraw --tree-brief` must exit 0 and list only real registered commands/options.
- `chatdraw hello` must fail; `hello` was a template/scaffold leftover, not a business command.
- Future drawing capabilities must add reusable Python APIs first, then CLI commands, and then update this page.
