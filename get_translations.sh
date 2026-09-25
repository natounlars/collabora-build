#!/bin/bash
# 把 translations 仓库克隆到 engine/translations
set -euo pipefail

COLLABORA_DIR="${1:-${PWD}}"
BRANCH="${TRANSLATIONS_BRANCH:-main}"
REPO="${TRANSLATIONS_REPO:-https://gerrit.collaboraoffice.com/translations}"
TARGET="${COLLABORA_DIR}/engine/translations"

echo "==> Cloning translations (branch: ${BRANCH})"
rm -rf "${TARGET}"
git clone --depth 1 --branch "${BRANCH}" "${REPO}" "${TARGET}"
echo "==> translations commit: $(git -C "${TARGET}" rev-parse HEAD)"
