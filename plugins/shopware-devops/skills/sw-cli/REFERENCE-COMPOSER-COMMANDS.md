# Shopware 6 — Composer Dev-Commands Referenz

> Quelle: `resources/references/core-reference/composer-commands-reference.md`
> Nur verfügbar im `shopware/shopware` GitHub-Repository (Kern-Entwicklung), nicht in regulären Projekten.
> Reguläre Projekte verwenden `./bin/*.sh`-Skripte.

```bash
composer [command] [parameter]
```

---

## Setup & Build

| Befehl | Beschreibung |
|:-------|:-------------|
| `setup` | Setzt diese Shopware-Instanz zurück und re-installiert sie (Datenbank wird gelöscht!) |
| `build:js` | Baut Administration & Storefront (Kombination aus `build:js:admin` & `build:js:storefront`) |
| `build:js:admin` | Baut die Administration — inkl. `bundle:dump`, `feature:dump`, `admin:generate-entity-schema-types`, `assets:install` |
| `build:js:component-library` | Baut die Component Library |
| `watch:admin` | Baut Administration mit Hot Module Reloading |
| `build:js:storefront` | Baut Storefront-JavaScript — inkl. `bundle:dump`, `feature:dump`, `theme:compile` |
| `check:license` | Prüft Drittanbieter-Lizenzen für Composer-Abhängigkeiten |
| `reset` | Setzt Shopware zurück ohne `composer install` / `npm install` (schneller wenn keine Dependencies geändert) |

---

## Administration

| Befehl | Beschreibung |
|:-------|:-------------|
| `admin:create:test` | Generiert ein Test-Boilerplate |
| `admin:generate-entity-schema-types` | Konvertiert Entity-Schemas in Datentypen |
| `admin:unit` | Startet die Jest-Unit-Test-Suite für die Administration |
| `admin:unit:watch` | Startet den interaktiven Jest-Unit-Test-Watcher für die Administration |
| `admin:unit:prepare-vue3` | Bereitet die Jest-Test-Suite für die Administration mit Vue3 vor |
| `admin:unit:vue3` | Startet die Jest-Unit-Test-Suite für die Administration mit Vue3 |
| `admin:unit:watch:vue3` | Startet den interaktiven Jest-Unit-Test-Watcher für die Administration mit Vue3 |
| `npm:admin:check-license` | Prüft Drittanbieter-Lizenzen für die Administration |
| `watch:admin` | Baut Administration mit Hot Module Reloading |

---

## Storefront

| Befehl | Beschreibung |
|:-------|:-------------|
| `build:js:storefront` | Baut Storefront-JavaScript — inkl. `bundle:dump`, `feature:dump`, `theme:compile` |
| `npm:storefront:check-license` | Prüft Drittanbieter-Lizenzen für den Storefront |
| `watch:storefront` | Baut Storefront mit Hot Module Reloading |

---

## Testsuite & Entwicklung

| Befehl | Beschreibung |
|:-------|:-------------|
| `bc-check` | Prüft auf Rückwärtskompatibilitäts-Brüche im aktuellen Branch |
| `e2e:setup` | Installiert eine saubere Shopware-Instanz für E2E und startet `e2e:prepare` |
| `e2e:open` | Öffnet die Cypress-E2E-Test-Suite-UI |
| `e2e:prepare` | Installiert das Admin Extension SDK Test-Plugin mit Fixtures und dumpt die Datenbank |
| `ecs` | Prüft alle Dateien mit Easy Coding Standard |
| `ecs-fix` | Prüft und behebt ECS-Issues wenn möglich |
| `eslint` | Code-Style-Prüfung aller JS/TS-Dateien (Administration/Storefront/E2E) |
| `eslint:admin` | Code-Style-Prüfung Administration JS/TS |
| `eslint:admin:fix` | Code-Style-Prüfung und Fix Administration JS/TS |
| `eslint:e2e` | Code-Style-Prüfung E2E JS/TS |
| `eslint:e2e:fix` | Code-Style-Prüfung und Fix E2E JS/TS |
| `eslint:storefront` | Code-Style-Prüfung Storefront JS/TS |
| `init:testdb` | Initialisiert die Test-Datenbank |
| `lint` | Shorthand für `stylelint`, `eslint`, `ecs`, `lint:changelog`, `lint:snippets` |
| `lint:changelog` | Validiert Changelogs |
| `lint:snippets` | Validiert Snippet-Existenz in allen Core-Sprachen |
| `phpstan` | Führt PHP-Static-Analysis-Tool aus |
| `phpunit` | Startet die PHP-Unit-Test-Suite |
| `phpunit:quarantined` | Startet PHP-Unit-Test-Suite für quarantänisierte Tests |
| `storefront:unit` | Startet die Jest-Unit-Test-Suite für den Storefront |
| `storefront:unit:watch` | Startet den interaktiven Jest-Unit-Test-Watcher für den Storefront |
