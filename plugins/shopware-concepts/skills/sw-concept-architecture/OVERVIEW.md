# Shopware 6 — Architektur-Konzept

Vollständige Konzept-Doku: `OVERVIEW-DETAIL.md`

## Kurzüberblick

Shopware folgt einer modularen, API-first-Architektur auf Basis von Symfony mit drei primären Domänen:

- **Core** — Backend-Fundament: Business-Logik, DAL, APIs, Extension-Mechanismus
- **Storefront** — PHP-Frontend: Twig-Templates, Pages/Pagelets, Themes, JS-Plugins
- **Administration** — Vue.js-SPA: kommuniziert ausschließlich über Admin API

Alle drei teilen eine gemeinsame API-Schicht. Storefront und Admin haben keine eigene Business-Logik.

## Kernprinzipien

- API-first: alle Funktionalität über APIs erreichbar (headless möglich)
- Separation of Concerns: Presentation von Business-Logik getrennt
- Erweiterbarkeit via Events, Services und Extension Points
- Asynchrone Verarbeitung via Symfony Messenger

Technische Umsetzung: `shopware-core`, `shopware-storefront`, `shopware-admin` (Dev-Plugins)
