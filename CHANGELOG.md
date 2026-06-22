# Changelog

## YYYY-MM-DD

### Added

### Changed

- 发布 workflow 改为显式 `v*` tag / `workflow_dispatch` 触发，使用 PyPI Trusted Publishing（`id-token: write` + `environment: pypi`），不再依赖仓库级 PyPI token secret。

### Fixed
