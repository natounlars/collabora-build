#!/bin/bash
# 在构建目录里克隆 Collabora Office monorepo（main 分支）
# 类似 chromium 的 get_chromium_from_git.sh
set -euo pipefail

BUILD_DIR="${1:-${PWD}}"
BRANCH="${COLLABORA_BRANCH:-main}"
REPO="${COLLABORA_REPO:-https://gerrit.collaboraoffice.com/online}"
TARGET="${BUILD_DIR}/collabora-office"

echo "==> Cloning ${REPO} (branch: ${BRANCH})"
rm -rf "${TARGET}"
# --depth=1 是必须的：LibreOffice 完整历史 > 1 GB，COPR 会超时
git clone --depth 1 --branch "${BRANCH}" "${REPO}" "${TARGET}"

cd "${TARGET}"
COMMIT="$(git rev-parse HEAD)"
echo "==> collabora commit: ${COMMIT}"
echo "${COMMIT}" > "${BUILD_DIR}/.collabora_commit"

# 记录到 spec 用的基础版本
if [ -f "${BUILD_DIR}/version.txt" ]; then
    echo "==> base version: $(cat "${BUILD_DIR}/version.txt")"
fi
