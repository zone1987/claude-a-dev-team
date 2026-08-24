---
name: sw-sync
description: Checks the upstream shopware/shopware repository for new versions and trunk drift (GitHub releases and tags API) and updates the sw-* skill library. --check reports only, --apply updates the skills.
argument-hint: [--check|--apply]
allowed-tools: Read, Grep, Glob, Bash, Edit, Write, WebFetch, Task
model: sonnet
---

# /sw-sync

Bring the skill library up to the current Shopware release. Delegate to the `shopware-librarian`
agent (skill `sw-release`).

## Steps
1. Read the state file (`plugins/shopware-quality/.sync-state.json`).
2. **Versions**: `https://api.github.com/repos/shopware/shopware/tags` and `/releases` — the newest
   against the recorded version.
3. **Trunk drift**: a local trunk pull or a GitHub compare since `lastCommit`; `changelog/`, and any
   new `adr/`.
4. Map the skills affected (the rules live in `sw-release`).
5. Mode:
   - `--check` (the default): report the recorded against the newest version, the drift, the skills
     affected and what to do — changing nothing.
   - `--apply`: update, extend or remove the skills, maintain `marketplace.json`, the plugin version
     and the changelog, update `.sync-state.json`, then validate.

Where something is unclear, or a large BC break is involved, stop and report instead. Never invent —
check against the source.
