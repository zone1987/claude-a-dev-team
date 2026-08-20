# Changelog

## 2.0.0 — 2026-08-20

Restructured from 109 skills into 16 domain skills. **Breaking:** every skill ID changed.

### Why

109 skills cost 48,591 characters of the skill listing budget — 607 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating. Reference material
also sat two levels deep in `references/deep/`, where files are only partially read.

### Changed

- **109 skills → 16**, grouped by administration area. Listing cost 48,591 → 4,569 characters
  (607 % → 57 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file, every one of the
  150 reference files and all 290 screenshots carried over — verified by content hash.
- **References are flat siblings**, one level deep, with a table of contents in each of the 105 files
  over 100 lines.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on Shopware admin vocabulary (`Bestellungen`, `Verkaufskanal`, `Einstellungen`) rather
  than generic nouns.
- **`license` MIT** (was `proprietary`); author reduced to a GitHub handle.

### Skill mapping

| Former skills | Now |
|---|---|
| `sw-merchant-catalog*` (8) | `sw-merchant-catalog` |
| `sw-merchant-orders*` (7) | `sw-merchant-orders` |
| `sw-merchant-customers*` (6) | `sw-merchant-customers` |
| `sw-merchant-content*` (5) | `sw-merchant-content` |
| `sw-merchant-marketing*` (5) | `sw-merchant-marketing` |
| `sw-merchant-settings*` (17) | `sw-merchant-settings` |
| `sw-merchant-sales-channels*` (9) | `sw-merchant-sales` |
| `sw-merchant-commercial*` (13) | `sw-merchant-commercial` |
| `sw-merchant-services*` (9) | `sw-merchant-services` |
| `sw-merchant-cloud*` (3) | `sw-merchant-cloud` |
| `sw-merchant-update-guides*` (4) | `sw-merchant-update` |
| `sw-merchant-migration*` (3) | `sw-merchant-migration` |
| `sw-merchant-spatial*` (4) | `sw-merchant-spatial` |
| `sw-merchant-insider-previews*` (3) | `sw-merchant-insider` |
| `sw-merchant-tutorials*` (8) | `sw-merchant-tutorials` |
| `overview`, `features`, `extensions`, `getting-started`, `vs-shopify` | `sw-merchant-general` |

Inside each domain, a former skill is now a file named after its topic: `sw-merchant-orders-states`
became `skills/sw-merchant-orders/STATES.md`, and its deep reference `STATES-DETAIL.md`.

## 1.0.0

Initial release — 109 skills, one per documentation page.
