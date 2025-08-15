# Versioning Policy

本專案遵循 **Semantic Versioning 2.0.0** 與 **Keep a Changelog**。

## 1. 版本號
- `MAJOR.MINOR.PATCH` 格式：
  - **MAJOR**：破壞相容（schema 或規則變更）。
  - **MINOR**：向後相容新增。
  - **PATCH**：修正（不改界面）。

## 2. Changelog
- 以 **Keep a Changelog 1.1.0** 維護 `CHANGELOG.md`，區塊：
  - `## [Unreleased]`
  - `### Added | Changed | Fixed | Removed`

## 3. 提交與發版
- 採用 **Conventional Commits**；`!` 表破壞性變更。
- 標籤：`vX.Y.Z` 並建立對應 GitHub Release。

## 4. CI 與守門
- CI 驗證：`ruff`、`black --check`、`mypy`、`pytest` 全綠才可合併。
- 使用 `actions/setup-python` 內建 pip cache 加速。
