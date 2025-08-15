#!/usr/bin/env bash
set -euo pipefail
pytest -q
ruff check .
black --check .
isort --check-only .
mypy .

