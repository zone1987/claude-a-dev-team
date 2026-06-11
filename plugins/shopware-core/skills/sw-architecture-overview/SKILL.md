---
name: sw-architecture-overview
description: >
  Shopware 6 Grundarchitektur & Orientierung — wann ist Shopware NICHT Standard-Symfony/Doctrine.
  Trigger: "Shopware Architektur", "wie funktioniert Shopware", "DAL vs Doctrine", "welche API",
  "Store API vs Admin API", "Decorator oder Event", "shopware orientation", "bundle structure". Shopware 6.7.
---

# Shopware 6 — Architektur-Orientierung

Shopware ist API-first (drei APIs) mit eigenem **Data Abstraction Layer (DAL)** statt Doctrine-ORM und
einem **event-getriebenen** Erweiterungssystem. Vor jeder Aufgabe diese Eckpunkte beachten:

## NICHT Standard-Symfony/Doctrine
- **Kein Doctrine-ORM** → `EntityDefinition`-Klassen + `EntityRepository`. Siehe `sw-entity-definition`.
- **Kein QueryBuilder** → `Criteria`-API (Filter/Sorting/Aggregation). Siehe `sw-criteria`.
- **Keine Doctrine-Annotations/Repositories** → DAL. Plain SQL nur in begründeten Fällen (`sw-plain-sql-vs-dal`).

## Erweiterungs-Priorität
1. **Events bevorzugen** — `EventSubscriberInterface` deckt die meisten Fälle ab (`sw-events-subscriber`).
2. **Decorator nur**, wenn das Event-Timing nicht passt (`sw-service-decoration`).
3. **Extension Points** für definierte Erweiterungsstellen (`sw-extension-points`).

## Drei APIs
| API | Pfad | Zweck |
|---|---|---|
| Admin | `/api/` | volle CRUD-/Admin-Operationen |
| Store | `/store-api/` | kundenseitig / Storefront |
| Sync | `/api/_action/sync` | Bulk-Operationen |

## Bundle-Struktur (Quelle)
`src/Core` (Business + Framework), `src/Administration` (Vue 3 Admin), `src/Storefront` (Twig/JS),
`src/Elasticsearch`. Plugins liegen unter `custom/plugins/<PluginName>` mit `src/`-PSR-4-Root.

## Stack-Fixpunkte (6.7)
PHP 8.2+, Symfony 7, DBAL 4, Vue 3 + Pinia/Vite (Admin, `mt-*`), Twig + Bootstrap 5 + Webpack (Storefront),
MySQL 8/MariaDB 10.11+, OpenSearch 2/ES 8, Redis optional, PHPUnit/PHPStan/Jest/Playwright.

Für konkrete Bausteine: `shopware-core` (Fundamentals), `shopware-data` (DAL), `shopware-framework`,
`shopware-storefront`, `shopware-admin`, `shopware-cms`, `shopware-checkout`.
