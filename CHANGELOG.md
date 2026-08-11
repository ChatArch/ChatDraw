# Changelog

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
- 发布 workflow 使用显式 `v*` tag / `workflow_dispatch` 触发，使用 PyPI Trusted Publishing（`id-token: write` + `environment: pypi`），不依赖仓库级 PyPI token secret。
