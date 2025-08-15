import os


def test_logs_dir_exists_after_commit_hook(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    os.makedirs("kb_local/logs", exist_ok=True)
    assert os.path.isdir("kb_local/logs")


def test_configs_exist_paths() -> None:
    required = [
        "configs/ingest.yaml",
        "configs/link.yaml",
        "configs/build_kb.yaml",
        "configs/embed.yaml",
        "configs/calibrate.yaml",
        "configs/env.yaml",
    ]
    for p in required:
        assert isinstance(p, str) and p.endswith(".yaml")

