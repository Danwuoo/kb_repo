# kb_repo

本專案旨在建構資料知識庫 (KB)，以支援分析與檢索需求。資料來源涵蓋公開論文、資料集與程式碼庫。

## 處理流程

資料處理流程遵循資料湖設計，分為三個層級：

1. **Bronze**：將原始資料轉換為統一的 Parquet 格式並落盤。
2. **Silver**：跨來源正規化與連結，形成 `publications`、`dataset_candidates` 與 `edges_pub_to_ds`。
3. **Gold**：組裝最終的 `kb.parquet`，並產出嵌入與索引供下游系統使用。

本專案遵循 *MDC RULES v1.1* 規範。

> 後續將會產出 Kaggle 版本的 `README.txt`。

## 安裝

```bash
# A) Poetry
pip install poetry
poetry install

# B) uv（選用。若已使用 Poetry，略過）
# pipx install uv
# uv pip install -r requirements.txt

# 安裝 pre-commit 並啟用
pip install pre-commit
pre-commit install
```

## 依賴風險與對策

* **固定 Python 版本**：`pyproject.toml` 內鎖定 `python = "^3.11"`，CI 亦使用 3.11。
* **鎖檔**：建議使用 Poetry 產生 `poetry.lock`（或 `uv` 生成 `requirements.lock`）。
* **環境快照**：`src/utils/env_probe.py` 每次提交自動寫入 `kb_local/logs/env.txt`。
* **可重現性**：後續的 `kb_meta.json` 可加入 `schema_hash`、`source_fingerprint`、`index.params` 與 `version` 等欄位。

