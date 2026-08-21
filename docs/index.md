# ChatDraw 文档

`ChatDraw` 当前是 ChatArch 绘图方向的 Python CLI 包壳。当前公开 CLI 已清理模板 `hello` 命令，只保留真实可执行的根级包信息入口；未来新增绘图能力时，必须先补可复用 Python API，再把真实 command surface 反映到 `chatdraw --tree` 和 `chatdraw --tree-brief`。

## 当前入口

| 入口 | 用途 |
|------|------|
| `chatdraw --help` | 查看当前公开 CLI 选项。 |
| `chatdraw --version` | 回读已安装包版本。 |
| `chatdraw --tree` | 打印带参数签名的真实注册 CLI 树。 |
| `chatdraw --tree-brief` | 打印省略参数签名的同一 CLI 树。 |

## 文档导航

<div class="grid cards" markdown>

-   :material-console-line: **CLI 树**

    ---

    由 ChatStyle 从真实 Click command surface 生成 full/brief 两种视图，确认当前没有残留模板命令。

    [查看 CLI 树](cli-tree.md)

-   :material-package-variant: **包发布契约**

    ---

    通过 Trusted Publishing/OIDC 发布，文档入口统一使用 ChatArch 公共域名。

    [PyPI 项目](https://pypi.org/project/ChatDraw/)

</div>

## 当前边界

- `hello` 是模板残留，已从公开 CLI 删除。
- 当前没有业务子命令；这不是隐藏能力，而是 root-only 的真实状态。
- 新增绘图命令时，需要同步测试、README、CLI 树、MkDocs 页面和发布说明。

英文版通过页面右上角语言切换进入。
