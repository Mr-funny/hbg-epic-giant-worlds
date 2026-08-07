#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dist_dir="${repo_dir}/dist"
archive="${dist_dir}/hbg-epic-giant-worlds-v1.2.0.tar.gz"

mkdir -p "${dist_dir}"
tar -czf "${archive}" \
  --exclude='.git' \
  --exclude='dist' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  -C "$(dirname "${repo_dir}")" \
  "$(basename "${repo_dir}")"
printf '%s\n' "${archive}"
