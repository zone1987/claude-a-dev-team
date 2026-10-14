# Changelog

## 2.1.0 (2026-10-14)

### Added

- **Plugin rule book** in `sw-guidelines`: `PLUGIN-RULES.md` (index) plus eight chapter files
  (`PLUGIN-RULES-CODE`, `-SHOPWARE`, `-UI`, `-RESILIENCE-SECURITY`, `-INTEGRATION`, `-DATA`, `-TESTING`,
  `-PROCESS`). 84 binding decisions, merged without duplicates from the ADRs of nine plugins, written in English.
- Tables of contents in the long references.
- Decisions taken over from the testing standard of `shopware-testing`, so that decisions live in one place:
  six new testing decisions (`pest-is-rejected`, `five-phpunit-configs-not-one`,
  `coverage-thresholds-are-enforced-in-jest-and-read-in-php`, `phpat-over-deptrac`,
  `rector-type-perfect-is-kept-although-abandoned`, `coverage-reports-are-ignored-and-mutation-baselines-are-committed`)
  and one process decision (`built-assets-are-not-committed`). Details merged into `test-strategy`,
  `coverage-must-be-honest`, `a-test-run-leaves-the-shop-unchanged`, `mutation-testing-comes-last`,
  `git-workflow` (asking before the first commit, exact version pinning) and `shopware-first-and-the-core-is-read`.
- `PLUGIN-ADR.md` and `PLUGIN-CLAUDE-MD.md` took over the remaining detail of the testing plugin's decision records:
  why not comments, what deserves an ADR, binding ADRs, a worked example, the `CONTEXT.md` sections and rules.

### Changed

- **Ground rules updated:** code is English, every Markdown file of a plugin is German. `PLUGIN-ADR.md`,
  `PLUGIN-WORKFLOW.md` and `PLUGIN-CLAUDE-MD.md` aligned with the rule book (language, local `CONTEXT.md`,
  mutation testing last and on request, feature branch, the owner merges, never push).
- `shopware-reviewer` loads the rule book in addition to `sw-testing-standard`, names each preloaded skill where it
  is used and is described as the default entry point for Shopware code quality.
- Descriptions of `sw-guidelines` and `sw-analysis` shortened to under 200 characters.
- `DEPTRAC.md` is now linked from the `sw-analysis` reference map.
- The copied list of plugin rules in `shopware-reviewer` is replaced by a pointer to `sw-testing-standard` and the plugin rule book in `sw-guidelines`. The commit rule no longer asks before the first commit: the agent commits on a feature branch in Conventional Commits, the owner merges (`git-workflow`, ground rule 4, hook text).

## 2.0.0 — 2026-08-20

Restructured from 15 skills into 3 domain skills. **Breaking:** every skill ID changed.

### Why

15 skills cost 7,084 characters of the skill listing budget — 89 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **15 skills → 3**, grouped by domain. Listing cost 7,084 → 862 characters
  (89 % → 11 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 21 reference files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 15 skills, one per documentation topic.
