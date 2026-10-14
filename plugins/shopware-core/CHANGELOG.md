# Changelog

## 2.2.0 (2026-10-14)

### Added

- `sw-plugin` reference `PLUGIN-EXTENSION-CONFIG.md`: every plugin carries `.config/shopware-extension.yml` with
  `compatibility_date` and `build.zip.pack.excludes.paths`, so ADRs, tests, tool configurations, `docs/` and the
  working notes never reach the release archive. Shape and traps measured against `shopware-cli` 0.19.1.

### Changed

- `PLUGIN-STRUCTURE.md`, `PLUGIN-CHECKLIST.md` and `/sw-plugin-create` create `.config/shopware-extension.yml` for every
  plugin.
- `docs/DEPRECATIONS.md` and `docs/UPGRADE-{shopwareNext}.md` live under `docs/` and are linked from `README.md` and
  `CLAUDE.md`.

## 2.1.0 (2026-10-14)

### Changed

- `shopware-dev` loads the plugin rule book (`shopware-quality:sw-guidelines`, `PLUGIN-RULES.md`) together with
  `shopware-testing:sw-testing-standard` and names both when delegating.
- Language row corrected: code is English, every Markdown file of a plugin is German.
- New rule rows: every PhpStorm inspection is resolved, nothing internal from Shopware (not even in tests), the plugin
  never stops the shop.
- Tables of contents added to five references.
- The copied list of plugin rules in `shopware-dev` and `shopware-backend` is replaced by a pointer to `sw-testing-standard` and the plugin rule book in `sw-guidelines`.

## 2.0.0 — 2026-08-20

Restructured from 18 skills into 3 domain skills. **Breaking:** every skill ID changed.

### Why

18 skills cost 8,109 characters of the skill listing budget — 101 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **18 skills → 3**, grouped by domain. Listing cost 8,109 → 858 characters
  (101 % → 11 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 27 reference files and 7 bundled files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 18 skills, one per documentation topic.
