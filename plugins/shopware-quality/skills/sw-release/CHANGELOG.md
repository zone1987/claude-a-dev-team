# Shopware 6 — Changelog

Plugin-`CHANGELOG.md` nach „Keep a Changelog" (de/en), pro Release Abschnitt mit Added/Changed/Fixed/Removed.

```markdown
## [1.2.0] - 2026-06-11
### Added
- FfExample: neues CMS-Element "Teaser"
### Fixed
- Preisberechnung bei Varianten
```

Der **Core** nutzt zusätzlich Flag-Files unter `changelog/` (`_unreleased`) mit Issue/Flag/Autor (ADR
„changelog release info process") — für Plugins meist die einfache `CHANGELOG.md` ausreichend. Version in
`composer.json` + Changelog konsistent halten. README/Doku: `shopware-readme`.
