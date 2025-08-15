"""文字正規化工具。"""
from __future__ import annotations

import html
import re
import unicodedata as ud


_GREEK = {
    "α": "alpha",
    "β": "beta",
    "γ": "gamma",
    "Δ": "Delta",
}


def normalize_text(s: str) -> str:
    """依 MDC 規範 v1.1（節錄）正規化文字。

    步驟：NFKC ➜ 轉小寫 ➜ 去除首尾空白與標點 ➜ 壓縮空白 ➜
    破折號與引號正規化 ➜ 希臘字母映射 ➜ HTML 解碼。

    參數：
        s: 原始字串。

    回傳：
        正規化後的字串。
    """

    t = ud.normalize("NFKC", s).casefold()
    t = "".join(ch for ch in ud.normalize("NFKD", t) if not ud.combining(ch))
    t = t.strip(" \t\n\r\f\v-—–'\"")
    t = re.sub(r"\s+", " ", t)
    t = t.replace("—", "-").replace("–", "-")
    t = "".join(_GREEK.get(ch, ch) for ch in t)
    t = html.unescape(t)
    return t


def normalize_doi(doi: str) -> str:
    """回傳移除 ``https://doi.org/`` 前綴且小寫的 DOI。"""

    d = doi.strip()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d, flags=re.I)
    return d.lower()

