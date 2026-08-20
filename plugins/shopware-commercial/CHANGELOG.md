# Changelog

## 2.0.0 — 2026-08-20

Restructured from 23 skills into 4 domain skills. **Breaking:** every skill ID changed.

### Why

23 skills cost 9,907 characters of the skill listing budget — 124 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **23 skills → 4**, grouped by domain. Listing cost 9,907 → 1,162 characters
  (124 % → 15 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 47 reference files and 21 bundled files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 23 skills, one per documentation topic.
