# Changelog

## 2.1.0 (2026-10-14)

### Fixed

- `sw-cli`: the release archive excludes are `build.zip.pack.excludes.paths` (an object with `paths`, not a list, and no
  `excluded_paths` key), the preferred file is `.config/shopware-extension.yml`, `extension zip` is deprecated in favour
  of `extension package`, which needs `shopware/core` under `require`.

## 2.0.1 (2026-10-14)

### Changed

- The copied list of plugin rules in the agents is replaced by a pointer to `sw-testing-standard` and the plugin rule book in `sw-guidelines`.

## 2.0.0 — 2026-08-20

Restructured from 37 skills into 5 domain skills. **Breaking:** every skill ID changed.

### Why

37 skills cost 19,664 characters of the skill listing budget — 246 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **37 skills → 5**, grouped by domain. Listing cost 19,664 → 1,433 characters
  (246 % → 18 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 82 reference files and 8 bundled files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 37 skills, one per documentation topic.
