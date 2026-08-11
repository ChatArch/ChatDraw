# CLI 树

`chatdraw --tree` 从真实注册的 Click command surface 生成。当前 `ChatDraw` 只有根级包信息入口，没有业务子命令；模板 `hello` 命令已删除，不能作为公开兼容接口保留。

## 顶层命令

```text
chatdraw # ChatDraw — drawing assistant package shell.
├── --help # Show this message and exit.
├── --version # Show the version and exit.
└── --tree # Print the registered command tree.
```

## 状态契约

- `chatdraw --help` 必须暴露 `--tree`。
- `chatdraw --tree` 必须 exit 0，并只列出真实注册的命令/选项。
- `chatdraw hello` 必须失败；`hello` 是 template/scaffold 残留，不是业务命令。
- 新增真实绘图能力时，先增加可复用 Python API，再新增 CLI command，并同步本页。
