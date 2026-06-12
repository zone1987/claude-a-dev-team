# shopware-quality

> Qualität, Konventionen, Static-Analysis — und die Selbst-Aktualisierung der Bibliothek.

`shopware-quality` sorgt für **Konventionskonformität, Code-Qualität** — und hält die gesamte Bibliothek aktuell.

Abgedeckt: die **Core-Coding-Guidelines** (Extendability, `final`/`@internal`, Decorator-Pattern, Deprecation,
DB-Migrationen, Code für Static Analysis) inklusive der vollständigen Guideline-Referenz, **Domain-Exceptions**
(Factory mit stabilen `code`s), **Extendability** und **Code-Struktur**, das destillierte **ADR-Wissen** (Index aller
~150 ADRs) und die **Static-Analysis-Werkzeuge** **ECS/PHP-CS-Fixer**, **PHPStan** (+ `phpstan-shopware`-Regeln),
**Deptrac** und **Rector**. Dazu der **README-Generator** und die **Changelog**-Konvention.

Das Herzstück ist der **Knowledge-Sync** (Skill `sw-knowledge-sync`, Agent **`shopware-librarian`**, Command
**`/sw-sync`**): er prüft das Upstream-Repo `shopware/shopware` über die **Releases-/Tags-API** *und* den **Trunk-Diff**,
mappt Änderungen auf betroffene Skills und schlägt Aktualisierungen vor (`--check`) bzw. wendet sie an (`--apply`).
Ergänzend liefern **Hooks** kontextsensitive Lint-/Katalog-Reminder nach Datei-Änderungen. Spezialist:
**`shopware-reviewer`**. **Wann nutzen:** für Code-Reviews, Qualitäts-Gates, README/Changelog und das Aktuell-Halten
der Bibliothek.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-quality@claude-a-dev-team
```

## Skills (15)

| Skill | Beschreibung |
|---|---|
| `shopware-readme` | Generiert und aktualisiert README.md-Dateien für Shopware 6 Plugins nach einem einheitlichen Schema |
| `sw-adr-knowledge` | Wissen über die Shopware-6 Architecture Decision Records (ADRs): warum bestimmte Muster gelten (Events vor Decorators, domain-exceptions, nested line items, payment flow, custom entities, UUIDv7, Pinia statt Vuex, Meteor, transactional flow |
| `sw-changelog` | Changelog-Konvention für Shopware-6-Plugins: CHANGELOG.md (Keep-a-Changelog), changelog/_unreleased Flag-Files im Core-Stil, Version-Bump |
| `sw-code-structure` | Shopware-6 Bundle- und Plugin-Code-Struktur: welcher Extension-Typ für welchen Use Case (Plugin, App, Bundle, Theme), Verzeichnis-Layout, Namespace-Konventionen, Domänen-Schnitt, Upgrade-orientierte Struktur, Isolierung von Integration-Poin |
| `sw-coding-guidelines` | Shopware-6 Core-Coding-Guidelines: final & internal, Extendability (Events vor Decorators), Decorator-Pattern, Domain-Exceptions, Feature-Flags, DB-Migrationen, Code für Static Analysis, Deprecation-Strategie |
| `sw-deptrac` | Architektur-/Schichten-Prüfung für Shopware-6-Plugins mit Deptrac: Layer definieren, erlaubte Abhängigkeiten, deptrac.yaml, Verstöße finden |
| `sw-documentation-guidelines` | Shopware Dokumentations-Guidelines: wie Shopware-Doku und Markdown für Contributions geschrieben wird — Zielgruppen, Dokumentationsstruktur (Concepts/Guides/Resources), Sprache & Grammatik, Formatierungsregeln, Asset-Management, Doc-Prozess |
| `sw-domain-exceptions` | Domain-Exceptions in Shopware 6 (ADR domain-exceptions): pro Domäne eine Exception-Factory-Klasse mit statischen Factory-Methoden, stabile error-codes, HttpException-Mapping, Log-Level |
| `sw-ecs-cs-fixer` | Code-Style für Shopware-6-Plugins mit Easy Coding Standard (ECS) / PHP-CS-Fixer: Config, Shopware-Regelset, composer ecs / ecs-fix |
| `sw-extendability` | Shopware-6 Erweiterbarkeits-Prinzipien: wann Events vs. Decorator vs |
| `sw-knowledge-sync` | Selbst-Aktualisierung der Shopware-Skill-Bibliothek gegen das Upstream-Repo: neue Versionen/Releases (GitHub releases/tags API) + Trunk-Drift (Commits/Changelog/ADRs) erkennen, betroffene Skills anpassen/ergänzen/entfernen, State pflegen |
| `sw-phpstan` | PHPStan für Shopware-6-Plugins: phpstan.neon einrichten, Level, Bootstrap/Autoload des Shopware-Kernels, Baseline, composer phpstan |
| `sw-phpstan-shopware` | PHPStan-Extension für Shopware-Plugins |
| `sw-rector` | Automatisierte Code-Modernisierung/Migration für Shopware-6-Plugins mit Rector: rector.php, Shopware-Rule-Set, PHP-Level-Upgrades, Deprecation-Fixes |
| `sw-static-analysis` | Static-Analysis & Lint-Pipeline für Shopware-6-Plugins: Überblick ECS/PHP-CS-Fixer, PHPStan, Deptrac, Rector, ESLint, Stylelint, ludtwig — welche Befehle, wann |

## Agents (2)

| Agent | Beschreibung |
|---|---|
| `shopware-librarian` | Selbst-Update-Agent der Shopware-Skill-Bibliothek. Prüft Upstream (shopware/shopware) auf neue Versionen/Releases und Trunk-Drift, mappt Änderungen auf betroffene sw-*-Skills und aktualisiert/ergänzt/entfernt Wissen, pflegt die .sync-state. |
| `shopware-reviewer` | Qualitäts-/Review-Spezialist für Shopware-6-Plugins: prüft gegen Coding-Guidelines, Domain-Exceptions, Static-Analysis (ECS/PHPStan/Deptrac/Rector), Konventionen und ADRs; schlägt Fixes vor; erstellt README/Changelog |

## Commands (3)

| Command | Beschreibung |
|---|---|
| `/sw-changelog` | Fügt einem Shopware-6-Plugin einen Changelog-Eintrag hinzu (Keep-a-Changelog) und bumpt optional die Version in composer.json |
| `/sw-readme` | Generiert/aktualisiert eine README für ein Shopware-6-Plugin nach dem etablierten README-Schema (Installation, Konfiguration, Features, Kompatibilität) |
| `/sw-sync` | Prüft das Upstream-Repo shopware/shopware auf neue Versionen/Releases (GitHub releases/tags API) und Trunk-Drift und aktualisiert die sw-*-Skill-Bibliothek |

## Hooks (1)

| Hook | Beschreibung |
|---|---|
| `PostToolUse` | Edit/Write/MultiEdit — kontextsensitive Lint-/Katalog-Reminder bei passenden Dateien; nicht-blockierend (`hooks/hooks.json`) |
