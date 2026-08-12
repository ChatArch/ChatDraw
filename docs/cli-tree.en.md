# CLI Tree

`chatdraw --tree` is generated from the real registered Click command surface. `ChatDraw` currently exposes only root-level package information entries and no business subcommands; the template `hello` command has been removed and must not be kept as a public compatibility surface.

## Top-level command

```text
chatdraw  # ChatDraw drawing assistant package shell
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Status contract

- `chatdraw --help` must expose `--tree`.
- `chatdraw --tree` must exit 0 and list only real registered commands/options.
- `chatdraw hello` must fail; `hello` was a template/scaffold leftover, not a business command.
- Future drawing capabilities must add reusable Python APIs first, then CLI commands, and then update this page.
