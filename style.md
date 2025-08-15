# Code Style & Docs

## 1. Python 程式風格（PEP 8）
- 縮排 4 空格；行寬 100；檔尾保留換行。
- 命名：變數/函式/模組 `snake_case`；類別 `CamelCase`。
- 匯入順序：標準庫 → 第三方 → 專案（空行分組）。

### Lint 與 Format
- **Ruff** 作為主要 Linter，與 **Black** 格式檢查並行。  
  建議在 `pyproject.toml` 設定：
    ```toml
    [tool.ruff]
    line-length = 100
    target-version = "py311"
    select = ["E","F","I","D","UP","B"]
    ignore = ["D203","D213"]
    ```

## 2. Docstring（Google / Napoleon）
- 使用 **Google style docstrings**，並以 type hints 為主：
  ```python
  def build_index(vectors: np.ndarray, m: int = 32) -> Index:
      """Build an ANN index.

      Args:
          vectors: 形狀為 [N, D] 的向量。
          m: HNSW `M` 參數。

      Returns:
          已訓練完成的索引物件。
      """
  ```

## 3. 型別檢查（mypy）
- 預設 `strict = False`，針對核心模組逐步拉高嚴格度；CI 執行 `mypy .`。
- 可選：使用 mypy GitHub Action 取得 PR inline 註解。

## 4. 提交與版本
- Commit：**Conventional Commits**（破壞性變更以 `!` 標記）。
- 版本：**SemVer**；Changelog：**Keep a Changelog**。
