# CLI 树

顶层 Click group 使用 `chatstyle.add_tree_option()` 从真实注册的 command surface 生成 full/brief 两种视图。当前 `ChatDraw` 只有根级包信息入口，没有业务子命令；模板 `hello` 命令已删除，不能作为公开兼容接口保留。

## 完整命令树

```text
chatdraw
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatdraw --tree` 默认保留命令参数签名。当前没有业务命令，因此只有无参数的 root pseudo-options。

## 简洁命令树

```text
chatdraw
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatdraw --tree-brief` 保留相同节点和用途说明，但省略参数签名；因此当前输出与完整树相同。

## 状态契约

- `chatdraw --help` 必须暴露 `--tree` 和 `--tree-brief`。
- `chatdraw --tree` 和 `chatdraw --tree-brief` 必须 exit 0，并只列出真实注册的命令/选项。
- `chatdraw hello` 必须失败；`hello` 是 template/scaffold 残留，不是业务命令。
- 新增真实绘图能力时，先增加可复用 Python API，再新增 CLI command，并同步本页。
