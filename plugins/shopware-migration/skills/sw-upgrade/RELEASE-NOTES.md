# Shopware 6 — release notes & version highlights

A compact entry point. Detailed knowledge per version in the `references/deep/` files.

## Quick access

| File | Content |
|---|---|
| `RELEASE-NOTES-6.md` | Complete 6.7 highlights, grouped by area |
| `RELEASE-NOTES-VERSION-HIGHLIGHTS.md` | Overview of 6.5 / 6.6 / 6.7 / 6.8 with upgrade notes |

## Most important new features in 6.7 (short version)

- **Storefront**: new Twig component system (Twig UX Components), Vite dev server, CSS custom properties for theme configuration, global JS event system (`window.Shopware.emit/on`), JSON-LD structured data
- **Administration**: SFC migration (`.html.twig + index.js` → `.vue`), Composition API extension system, MCP server (experimental), OpenSearch for the Admin API (experimental)
- **Core**: Symfony 7.4, PHP 8.5 support, `product.type` (digital/physical, replaces `product.states`), DAL optimizations (EXISTS instead of LEFT JOINs), pluggable thumbnail processor
- **API**: Store API HTTP caching for numerous routes (`CACHE_REWORK` flag), Sync API foreign key resolver, new mail template preview routes
- **App system**: webhook rework (`WEBHOOKS_REWORK` flag → DB outbox, retry backoff), app requirements validation
- **Breaking changes (prepared for 6.8)**: `--json`→`--format json` for CLI commands, newsletter route signatures, `mail-template/validate` route removed

Complete information: `RELEASE-NOTES-6.md`
Comparison of all versions + upgrade paths: `RELEASE-NOTES-VERSION-HIGHLIGHTS.md`
