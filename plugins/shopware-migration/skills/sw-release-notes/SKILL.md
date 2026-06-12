---
name: sw-release-notes
description: >
  Shopware-6-Release-Notes und Versions-Highlights (6.5–6.8). Trigger: "Release Notes Shopware",
  "was ist neu in 6.7", "Neuerungen Version", "release highlights", "what's new shopware",
  "Shopware 6.7 Features", "Changelog shopware", "neue Features 6.8". Shopware 6.7.
---

# Shopware 6 — Release Notes & Versions-Highlights

Kompakter Einstieg. Detailwissen je Version in den `references/deep/`-Dateien.

## Schnellzugriff

| Datei | Inhalt |
|---|---|
| `references/deep/release-notes-6.7.md` | Vollständige 6.7-Highlights, gruppiert nach Bereich |
| `references/deep/version-highlights.md` | Übersicht 6.5 / 6.6 / 6.7 / 6.8 mit Upgrade-Hinweisen |

## Wichtigste Neuerungen 6.7 (Kurzfassung)

- **Storefront**: Neues Twig-Komponenten-System (Twig UX Components), Vite-Dev-Server, CSS Custom Properties für Theme-Konfiguration, globales JS-Event-System (`window.Shopware.emit/on`), JSON-LD Structured Data
- **Administration**: SFC-Migration (`.html.twig + index.js` → `.vue`), Composition API Extension System, MCP-Server (experimentell), OpenSearch für Admin-API (experimentell)
- **Core**: Symfony 7.4, PHP 8.5-Support, `product.type` (digital/physical, ersetzt `product.states`), DAL-Optimierungen (EXISTS statt LEFT JOINs), pluggable Thumbnail-Processor
- **API**: Store-API HTTP-Caching für zahlreiche Routen (`CACHE_REWORK`-Flag), Sync-API Foreign-Key-Resolver, neue Mail-Template-Preview-Routes
- **App System**: Webhook-Rework (`WEBHOOKS_REWORK`-Flag → DB-Outbox, Retry-Backoff), App-Requirements-Validierung
- **Breaking Changes (vorbereitet für 6.8)**: `--json`→`--format json` bei CLI-Befehlen, Newsletter-Route-Signaturen, `mail-template/validate`-Route entfernt

Vollständige Informationen: `references/deep/release-notes-6.7.md`
Vergleich aller Versionen + Upgrade-Pfade: `references/deep/version-highlights.md`
