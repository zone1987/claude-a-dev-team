# Changelog

## 2.0.0 — 2026-08-20

Restructured from 7 skills into 2 domain skills. **Breaking:** every skill ID changed.

### Why

7 skills cost 3,022 characters of the skill listing budget — 38 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **7 skills → 2**, grouped by domain. Listing cost 3,022 → 564 characters
  (38 % → 7 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 9 reference files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 7 skills, one per documentation topic.
