# Changelog

All notable changes to the `discord` plugin.

## 1.0.0 — 2026-08-26

First release. The Discord developer documentation, distilled in full.

### Added

- **Eleven skills.** Ten cover all 159 pages of `docs.discord.com/developers`: `discord-bots`,
  `discord-rest`, `discord-gateway`, `discord-interactions`, `discord-oauth2`, `discord-activities`,
  `discord-social-sdk`, `discord-monetization`, `discord-rpc-voice`, `discord-platform`. The
  eleventh, `discord-local-testing`, is a cross-cut: it gathers running and testing an app locally
  from ten pages that document it in passing, because the documentation never treats it as one
  subject. It names what the documentation does not state rather than filling those gaps in.
- **Four agents**: `discord-dev` (orchestrator and entry point), `discord-api-expert`
  (endpoint and schema lookup), `discord-bot-builder` (implementation), `discord-activity-dev`
  (Activities and the Embedded App SDK).
- **Three commands**: `/discord-lookup`, `/discord-bot-scaffold`, `/discord-docs-sync`.
- **One hook**: `UserPromptSubmit` routing on exact Discord API vocabulary, deliberately silent on
  the bare word "discord".
- **Verification, on three levels**: `scripts/verify_references.py` proves every reference file is
  reachable from its `SKILL.md` and every relative link resolves; `scripts/verify_page_coverage.py`
  proves every documented page reached a skill that carries content, in both directions, against the
  recorded sitemap hash; `scripts/audit_terms.py` proves the *content* arrived, comparing every
  identifier, constant, route and table number of each source page against the reference files, and
  reporting plugin terms absent upstream so invention surfaces.
- **`INVENTORY.json`** plus `scripts/build_inventory.py`: per page, its sha256, source line count and
  covering files, so completeness is re-checked by hash comparison instead of by re-reading 159 pages.
- **`PAGE-COVERAGE.json`**: the page-to-skill map, with the sitemap's sha256 and retrieval date, so a
  page Discord adds later surfaces as a gap rather than going unnoticed.

### Verified at release

- Forge validator `--strict`: **clean** — 0 errors, 0 warnings.
- Every reference reachable from its `SKILL.md`, every relative link resolves.
- All 159 pages claimed by a skill that carries content.
- **99.7 % source term coverage** (4,303 of 4,316). The 13 remaining are rendering artefacts, each
  verified individually against the mirror: MDX anchor attributes (`bymonth` beside the real
  `by_month` field), markdown escapes (`$browser` for `"browser"`), a shell quote, and `type:6`
  written without its space. No documented fact is absent.
- 84 reference files, 55,002 lines, from 51,480 lines of source markdown.
- Listing cost 3,003 characters, 37.5 % of budget, 25 to 42 characters of headroom per description.

### Source

Distilled from [docs.discord.com](https://docs.discord.com/developers/intro), sitemap sha256
`5f88bd8ed24253a5fc624762d2cfaf5b31fde94edb9ec2f1bbc71851082900ed`, all 159 pages retrieved
2026-08-26 as their markdown twins.
