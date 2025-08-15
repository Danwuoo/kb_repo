import numpy as np

from src.embed.indexer import FlatIndex


def test_flat_ip_top1_self() -> None:
    v = np.eye(4, dtype=np.float32)
    idx = FlatIndex(v)
    s, I = idx.search(v, k=1)
    assert np.all(I.flatten() == np.arange(4))


def test_flat_ip_shape() -> None:
    v = np.random.RandomState(0).randn(10, 8).astype("float32")
    idx = FlatIndex(v)
    q = v[:3]
    s, I = idx.search(q, k=5)
    assert s.shape == (3, 5) and I.shape == (3, 5)


def test_flat_ip_rank_order() -> None:
    v = np.array([[1, 0], [0.9, 0], [0, 1]], dtype=np.float32)
    idx = FlatIndex(v)
    q = np.array([[1, 0]], dtype=np.float32)
    s, I = idx.search(q, k=2)
    assert I[0, 0] == 0 and I[0, 1] == 1

