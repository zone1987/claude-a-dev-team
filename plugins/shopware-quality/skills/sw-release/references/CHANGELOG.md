# Shopware 6 — Changelog

Plugin `CHANGELOG.md` following "Keep a Changelog" (de/en), one section per release with Added/Changed/Fixed/Removed.

```markdown
## [1.2.0] - 2026-06-11
### Added
- FfExample: new CMS element "Teaser"
### Fixed
- Price calculation for variants
```

The **core** additionally uses flag files under `changelog/` (`_unreleased`) with issue/flag/author (ADR
"changelog release info process") — for plugins the plain `CHANGELOG.md` is usually sufficient. Keep the version in
`composer.json` and the changelog consistent. README/documentation: `shopware-readme`.
