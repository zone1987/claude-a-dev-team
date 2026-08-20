# Shopware 6 — Release Notes & Versions-Highlights

Kompakter Einstieg. Detailwissen je Version in den `references/deep/`-Dateien.

## Schnellzugriff

| Datei | Inhalt |
|---|---|
| `RELEASE-NOTES-6.md` | Vollständige 6.7-Highlights, gruppiert nach Bereich |
| `RELEASE-NOTES-VERSION-HIGHLIGHTS.md` | Übersicht 6.5 / 6.6 / 6.7 / 6.8 mit Upgrade-Hinweisen |

## Wichtigste Neuerungen 6.7 (Kurzfassung)

- **Storefront**: Neues Twig-Komponenten-System (Twig UX Components), Vite-Dev-Server, CSS Custom Properties für Theme-Konfiguration, globales JS-Event-System (`window.Shopware.emit/on`), JSON-LD Structured Data
- **Administration**: SFC-Migration (`.html.twig + index.js` → `.vue`), Composition API Extension System, MCP-Server (experimentell), OpenSearch für Admin-API (experimentell)
- **Core**: Symfony 7.4, PHP 8.5-Support, `product.type` (digital/physical, ersetzt `product.states`), DAL-Optimierungen (EXISTS statt LEFT JOINs), pluggable Thumbnail-Processor
- **API**: Store-API HTTP-Caching für zahlreiche Routen (`CACHE_REWORK`-Flag), Sync-API Foreign-Key-Resolver, neue Mail-Template-Preview-Routes
- **App System**: Webhook-Rework (`WEBHOOKS_REWORK`-Flag → DB-Outbox, Retry-Backoff), App-Requirements-Validierung
- **Breaking Changes (vorbereitet für 6.8)**: `--json`→`--format json` bei CLI-Befehlen, Newsletter-Route-Signaturen, `mail-template/validate`-Route entfernt

Vollständige Informationen: `RELEASE-NOTES-6.md`
Vergleich aller Versionen + Upgrade-Pfade: `RELEASE-NOTES-VERSION-HIGHLIGHTS.md`
