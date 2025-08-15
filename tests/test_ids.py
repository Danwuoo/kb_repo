from src.build_kb.ids import decide_dataset_id, uuid5_from_title_repo


def test_decide_with_doi() -> None:
    got = decide_dataset_id("10.1/a", None, "t", "https://x.org/r", "https://ns")
    assert got == "doi:10.1/a"


def test_decide_with_accession_plain() -> None:
    got = decide_dataset_id(None, "GSE123", "t", "https://x.org/r", "https://ns")
    assert got == "acc:GSE123"


def test_decide_with_accession_scheme() -> None:
    got = decide_dataset_id(None, "gse:GSE123", "t", "https://x.org/r", "https://ns")
    assert got == "gse:GSE123"


def test_uuid5_stability() -> None:
    u1 = uuid5_from_title_repo("Title A", "repo.org", "https://ns")
    u2 = uuid5_from_title_repo("Title A", "repo.org", "https://ns")
    assert u1 == u2


def test_uuid5_changes_on_title() -> None:
    u1 = uuid5_from_title_repo("Title A", "repo.org", "https://ns")
    u2 = uuid5_from_title_repo("Title B", "repo.org", "https://ns")
    assert u1 != u2


def test_uuid5_changes_on_repo() -> None:
    u1 = uuid5_from_title_repo("Title A", "repo1.org", "https://ns")
    u2 = uuid5_from_title_repo("Title A", "repo2.org", "https://ns")
    assert u1 != u2

