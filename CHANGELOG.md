# Changelog

## 0.1.3 - 2026-08-21

### Changed

- 使用 `chatstyle>=0.2.0,<0.3.0` 的 `add_tree_option()` 替换包内 Click tree renderer，并固定公开根命令名为 `chatdraw`。
- 新增 `chatdraw --tree-brief`，默认 `--tree` 保留参数签名，brief 输出省略参数签名。
- 同步版本、CLI 测试、中英文文档、开发约定与 CI 的已安装 console-script/build/check 验收。

## 0.1.2 - 2026-08-12

### Changed

- 将 `chatdraw --tree` 从静态字符串改为由 Click command surface 渲染，避免 CLI 和文档树漂移。
- 同步版本测试与发布 workflow guard，准备 `0.1.2` patch release。

## 0.1.1 - 2026-08-12

### Changed

- 删除公开 CLI 中的 template/scaffold `hello` 命令；当前 `ChatDraw` 的真实 command surface 为 root-only。
- 新增 `chatdraw --version` 和 `chatdraw --tree`，并用测试锁住 `hello` 不再公开。
- 对齐 README、MkDocs 首页和 CLI 树文档到 ChatArch 公共文档域名。
- 启用 MkDocs Material bilingual/i18n 配置与 `pymdownx.emoji` Material renderer。
- 加强 Preview Docs、CI 和 Trusted Publishing/OIDC 发布 workflow guard。

## 0.1.0 - 2026-06-23

### Changed

- 准备 `0.1.0` 发版，用于验证 PyPI Trusted Publishing 免 token 发布流程。
- 发布 workflow 使用显式 `v*` tag 与当时的手动触发入口，使用 PyPI Trusted Publishing（`id-token: write` 加 GitHub 环境名 `pypi`），不依赖仓库级 PyPI token secret。
