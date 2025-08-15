"""將環境快照寫入 ``logs/env.txt``。

此腳本由 pre-commit 於每次提交時執行，僅依賴最小套件。
"""
from __future__ import annotations

import os
import platform
import sys
from datetime import datetime, timezone


def main() -> None:
    logs_dir = os.path.join("kb_local", "logs")
    os.makedirs(logs_dir, exist_ok=True)
    path = os.path.join(logs_dir, "env.txt")
    now = datetime.now(timezone.utc).isoformat()
    lines = [
        f"captured_at_utc={now}\n",
        f"python={sys.version.split()[0]}\n",
        f"platform={platform.platform()}\n",
    ]
    try:
        import numpy as np  # type: ignore

        lines.append(f"numpy={np.__version__}\n")
    except Exception:
        lines.append("numpy=NA\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()

