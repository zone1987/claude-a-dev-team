# shopware-concepts

Konzept-Plugin für Shopware 6 — destilliertes Architektur- und Konzept-Wissen aus der offiziellen Shopware-Dokumentation.

## Zweck

Dieses Plugin beantwortet konzeptionelle Fragen der Art „Wie funktioniert X architektonisch in Shopware?" — ohne Implementierungsdetails, aber mit dem notwendigen Hintergrundwissen für fundierte Entwicklungsentscheidungen.

## Skills (Konzeptbereiche)

| Skill | Thema |
|---|---|
| `sw-concept-architecture` | Shopware-Architektur: Core, Storefront, Administration, API-first |
| `sw-concept-dal` | Data Abstraction Layer: Repositories, Criteria, Inheritance, Versioning |
| `sw-concept-api` | Admin API & Store API: Zweck, Auth, Unterschiede |
| `sw-concept-catalog` | Produktkatalog: Products, Categories, Sales Channels |
| `sw-concept-checkout` | Checkout: Cart, Orders, Payments |
| `sw-concept-content-cms` | Shopping Experiences (CMS): Struktur, Hydration, Headless |
| `sw-concept-rule-system` | Rule Builder & Rule-System: Evaluation, Scopes, Container Rules |
| `sw-concept-translations` | Übersetzungssystem: Fallback-Layers, Built-in Translation, Snippet-Dateien |
| `sw-concept-extensions` | Apps vs. Plugins: Unterschiede, Einsatzgebiete |
| `sw-concept-app-system` | App-System: Manifest, Webhooks, App Scripts, Cloud-Kompatibilität |
| `sw-concept-data-stores` | Weitere Konzepte: Messaging, Flow Builder, HTTP Cache, Elasticsearch, Migrations |
| `sw-concept-messaging` | Symfony Messenger in Shopware: Bus, Handler, Transport, Async |

## Agent

`shopware-concepts` — Berater-Agent für konzeptionelle Fragen. Nutzt die Konzept-Skills und verweist für technische Umsetzung auf die passenden Dev-Plugins (`shopware-core`, `shopware-data`, `shopware-checkout`, etc.).

## Quellen

Destilliert aus `docs-main/concepts/` — vollständig eingearbeitet (37 Dateien).
