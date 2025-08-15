from src.normalize.text import normalize_doi, normalize_text


def test_simple_space() -> None:
    assert normalize_text(" A  B ") == "a b"


def test_quotes_dash() -> None:
    assert normalize_text("A—B") == "a-b"


def test_greek_map() -> None:
    assert "alpha" in normalize_text("α")


def test_html_unescape() -> None:
    assert normalize_text("A&amp;B") == "a&b"


def test_normalize_doi_prefix() -> None:
    assert normalize_doi("https://doi.org/10.1/ABC") == "10.1/abc"


def test_normalize_doi_dx() -> None:
    assert normalize_doi("http://dx.doi.org/10.2/XYZ") == "10.2/xyz"


def test_normalize_doi_bare() -> None:
    assert normalize_doi("10.3/abc") == "10.3/abc"


def test_trim_punct() -> None:
    assert normalize_text(" 'title' ") == "title"


def test_collapse_spaces() -> None:
    assert normalize_text("a\n\n b\t c") == "a b c"


def test_casefold() -> None:
    assert normalize_text("Å") == "a"

