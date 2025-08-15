# kb_repo

本專案旨在建構資料知識庫 (KB)，以支援分析與檢索需求。資料來源涵蓋公開論文、資料集與程式碼庫。

## 處理流程

資料處理流程遵循資料湖設計，分為三個層級：

1. **Bronze**：將原始資料轉換為統一的 Parquet 格式並落盤。
2. **Silver**：跨來源正規化與連結，形成 `publications`、`dataset_candidates` 與 `edges_pub_to_ds`。
3. **Gold**：組裝最終的 `kb.parquet`，並產出嵌入與索引供下游系統使用。

本專案遵循 *MDC RULES v1.1* 規範。

> 後續將會產出 Kaggle 版本的 `README.txt`。

