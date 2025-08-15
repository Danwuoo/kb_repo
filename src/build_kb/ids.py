"""資料集識別碼決策工具。"""
from __future__ import annotations

import uuid
from urllib.parse import urlparse

from src.normalize.text import normalize_text


def uuid5_from_title_repo(title: str, repo_domain: str, namespace_url: str) -> str:
    """以標題與庫域名產生穩定的 UUIDv5。"""

    norm = f"{normalize_text(title)}|{repo_domain.lower()}"
    ns = uuid.uuid5(uuid.NAMESPACE_URL, namespace_url)
    return str(uuid.uuid5(ns, norm))


def decide_dataset_id(
    doi: str | None,
    accession: str | None,
    title: str,
    repo_url: str,
    namespace_url: str,
) -> str:
    """識別碼決策流程：``doi`` ➜ ``<scheme>:<id>`` ➜ ``uuid5(...)``。"""

    if doi:
        return f"doi:{doi}"
    if accession:
        if ":" in accession:
            return accession
        return f"acc:{accession}"
    repo_domain = urlparse(repo_url).netloc or "unknown"
    return uuid5_from_title_repo(title, repo_domain, namespace_url)

