# Changelog

## 2.0.0 — 2026-08-20

Restructured from 17 skills into 3 domain skills. **Breaking:** every skill ID changed.

### Why

17 skills cost 8,653 characters of the skill listing budget — 108 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **17 skills → 3**, grouped by domain. Listing cost 8,653 → 885 characters
  (108 % → 11 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 22 reference files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 17 skills, one per documentation topic.
