<div align="center">
    <a href="https://pypi.python.org/pypi/ChatDraw">
        <img src="https://img.shields.io/pypi/v/ChatDraw.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatDraw/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatDraw/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatDraw/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

English | [简体中文](README.md)
</div>

# ChatDraw

`ChatDraw` is the ChatArch Python CLI package shell for drawing-oriented work. The public CLI has removed the template `hello` command and now exposes only truthful root-level package information entries. Future drawing capabilities must update the Python API, CLI tree, docs, and tests together.

## Quick Start

```bash
pip install ChatDraw
chatdraw --version
chatdraw --tree
```

Development environment:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

```text
chatdraw  # ChatDraw drawing assistant package shell
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

`chatdraw hello` was a scaffold leftover and has been removed from the public CLI.

## Documentation

- Documentation home: https://arch.gh.wzhecnu.cn/ChatDraw/
- CLI tree: https://arch.gh.wzhecnu.cn/ChatDraw/cli-tree/
- English docs: https://arch.gh.wzhecnu.cn/ChatDraw/en/

## Development Notes

Read `DEVELOP.md` and `AGENTS.md` before expanding commands, and keep `--tree`, README, MkDocs, tests, and changelog synchronized.
