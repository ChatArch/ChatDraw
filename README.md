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

[英文版](README.en.md) | 简体中文
</div>

# ChatDraw

`ChatDraw` 是 ChatArch 绘图方向的 Python CLI 包壳。当前公开 CLI 已清理模板 `hello` 命令，只保留真实 root-only 包信息入口；后续新增绘图能力时，必须同步 Python API、CLI 树、文档和测试。

## 快速开始

```bash
pip install ChatDraw
chatdraw --version
chatdraw --tree
```

开发环境：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

```text
chatdraw # ChatDraw — drawing assistant package shell.
├── --help # Show this message and exit.
├── --version # Show the version and exit.
└── --tree # Print the registered command tree.
```

`chatdraw hello` 是脚手架残留，已从公开 CLI 删除。

## 文档

- 文档首页：https://arch.gh.wzhecnu.cn/ChatDraw/
- CLI 树：https://arch.gh.wzhecnu.cn/ChatDraw/cli-tree/
- 英文文档：https://arch.gh.wzhecnu.cn/ChatDraw/en/

## 开发说明

扩展命令前先阅读 `DEVELOP.md` 和 `AGENTS.md`，并保持 `--tree`、README、MkDocs、测试与 changelog 同步。
