# Shopware library — knowledge sync (self-update)

Keeps the `sw-*` skills current against `shopware/shopware`. Run it through the `shopware-librarian` agent (`/sw-sync`).

## Sources
- **Releases/tags** (new versions): `https://api.github.com/repos/shopware/shopware/releases`
  and `https://api.github.com/repos/shopware/shopware/tags` → latest version vs. the stored state.
- **Trunk drift**: GitHub compare API or a local trunk pull; additionally `changelog/`, `CHANGELOG.md`,
  `UPGRADE-*`, `RELEASE_INFO-*`, new/changed `adr/`.

## State file (`plugins/shopware-quality/.sync-state.json`)
```json
{ "lastCommit": "<sha>", "lastRelease": "v6.7.x.x", "lastChecked": "<ISO date>" }
```

## Mapping source → skill (examples)
`src/Core/Framework/DataAbstractionLayer/**` → shopware-data · `src/Storefront/**` → shopware-storefront ·
`src/Administration/**` → shopware-admin · `src/Core/Checkout/**` → shopware-checkout · `adr/*` → sw-adr-knowledge ·
new major → new `shopware-migration` skill.

## Drift criteria
new/removed classes and methods, changed signatures, new ADRs, deprecations, new major/minor. When in doubt:
report, no auto-apply.

→ Mechanics/modes: command `/sw-sync` (`--check` report / `--apply`); agent `shopware-librarian`.
