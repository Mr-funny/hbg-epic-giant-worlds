#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
codex_root="${CODEX_HOME:-${HOME}/.codex}"
target_dir="${1:-${codex_root}/skills}"
timestamp="$(date +%Y%m%d-%H%M%S)"

mkdir -p "${target_dir}"

for skill_dir in "${repo_dir}"/skills/hbg-*; do
  skill_name="$(basename "${skill_dir}")"
  destination="${target_dir}/${skill_name}"
  if [[ -e "${destination}" ]]; then
    mv "${destination}" "${destination}.backup-${timestamp}"
  fi
  cp -R "${skill_dir}" "${destination}"
  printf 'Installed %s -> %s\n' "${skill_name}" "${destination}"
done

printf 'Done. Restart or reload your Agent, then invoke $hbg-keyword-giant-world, $hbg-oriental-giant-world, or $hbg-oriental-giant-roam.\n'

