# Development Guide

## CLI Rules

- Keep the public root command explicit as `chatdraw`.
- Use `chatstyle>=0.2.0,<0.3.0` and `add_tree_option()` for the registered `--tree` / `--tree-brief` runtime; do not add a package-local tree renderer.
- If ChatDraw introduces env/profile/config behavior, register a typed ChatEnv config and use `chatenv>=0.2.10,<0.3.0` plus ChatEnv storage paths.
- Prefer `CommandSchema`, `CommandField`, `add_interactive_option()`, and `resolve_command_inputs()` for new commands.
- Missing required args should auto-enter interactive mode when recoverable.
- `-i` forces interactive mode; `-I` disables prompting and must fail fast.
- Prompt defaults must match actual execution defaults.
- Sensitive values must stay masked in prompts and summaries.
- Prefer lazy imports in CLI wiring and keep implementation imports local when possible.

## Docs and Tests

- Use doc-first CLI testing.
- Put real CLI coverage under `tests/cli-tests/`.
- Put mock/fake CLI coverage under `tests/mock-cli-tests/`.
- Keep `--help`, `--tree`, `--tree-brief`, `README.md`, `docs/`, and `CHANGELOG.md` in sync with the actual Click registry.
- Put drawing behavior in reusable importable Python functions before exposing it through a thin CLI adapter.

## Automation

- Keep automation small and reviewable.
- Prefer commands that can run in CI without interactive prompts.
- Ensure generated defaults are safe for local development.
