# Contributing Guide

歡迎貢獻！提出 PR 前請先閱讀本指南。

## 開發流程
1. 從 `main` 切出功能分支：`feature/*`、`fix/*`、`chore/*`。
2. 撰寫/更新測試，確保 `pytest` 全綠。
3. 本地執行 `ruff check . && black --check . && mypy .`。
4. 以 **Conventional Commits** 撰寫提交訊息（見下）。開 PR 對 `develop` 或受保護分支。

## 提交訊息（Conventional Commits）
基本格式：
```

<type>\[optional scope]: <description>

\[optional body]

\[optional footer(s)]

```
常用 `type`：`feat|fix|docs|refactor|perf|test|build|ci|chore|revert`。  
**破壞性變更**請在 `type` 後加 `!`，並在 footer 加 `BREAKING CHANGE: ...`。

## 版本與發佈
- 採 **SemVer 2.0.0**：`MAJOR.MINOR.PATCH`。
  - MAJOR：破壞相容。
  - MINOR：向後相容新增。
  - PATCH：修正。
- 變更記錄遵循 **Keep a Changelog 1.1.0**，維護 `CHANGELOG.md`。

## 程式風格與 Docstring
- 遵循 **PEP 8**，行寬 100。導入順序：標準庫 → 第三方 → 專案。
- Docstring 使用 **Google style**，並全面使用型別註記。

## 測試
- 測試放在 `tests/`，命名 `test_*.py`。
- 單元測試覆蓋核心模組；整合測試涵蓋主要小管線。

## CI
- PR 需通過 CI（ruff/black/mypy/pytest）。`setup-python` 啟用 pip 快取加速。
