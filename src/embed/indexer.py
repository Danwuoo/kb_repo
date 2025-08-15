"""簡易向量索引器實作。"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np


Metric = Literal["ip", "l2"]


@dataclass
class IndexMeta:
    type: str
    metric: Metric
    params: dict
    version: str


class FlatIndex:
    """僅支援內積的極簡 Flat 索引器，供 CI 與測試使用。"""

    def __init__(self, vectors: np.ndarray, metric: Metric = "ip") -> None:
        self.v = vectors.astype("float32", copy=False)
        self.metric = metric

    def search(self, q: np.ndarray, k: int = 10) -> tuple[np.ndarray, np.ndarray]:
        q = q.astype("float32", copy=False)
        if self.metric == "ip":
            scores = q @ self.v.T
            idx = np.argsort(-scores, axis=1)[:, :k]
            top = np.take_along_axis(scores, idx, axis=1)
            return top, idx
        raise NotImplementedError("l2 not implemented in smoke index")

