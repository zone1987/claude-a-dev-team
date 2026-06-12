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

`shopware-readme`, `sw-adr-knowledge`, `sw-changelog`, `sw-code-structure`, `sw-coding-guidelines`, `sw-deptrac`, `sw-documentation-guidelines`, `sw-domain-exceptions`, `sw-ecs-cs-fixer`, `sw-extendability`, `sw-knowledge-sync`, `sw-phpstan`, `sw-phpstan-shopware`, `sw-rector`, `sw-static-analysis`

## Agents (2)

- **`shopware-librarian`** — Selbst-Update-Agent der Shopware-Skill-Bibliothek. Prüft Upstream (shopware/shopware) auf neue Versionen/Releases und Trunk-Drift, mappt Änderungen auf betroffene sw-*-Skills und aktualisiert/ergänzt/entfernt Wissen, pfl
- **`shopware-reviewer`** — Qualitäts-/Review-Spezialist für Shopware-6-Plugins: prüft gegen Coding-Guidelines, Domain-Exceptions, Static-Analysis (ECS/PHPStan/Deptrac/Rector), Konventionen und ADRs; schlägt Fixes vor; erstellt README/Changelog.

## Commands (3)

- **`/sw-changelog`** — Fügt einem Shopware-6-Plugin einen Changelog-Eintrag hinzu (Keep-a-Changelog) und bumpt optional die Version in composer.json.
- **`/sw-readme`** — Generiert/aktualisiert eine README für ein Shopware-6-Plugin nach dem etablierten README-Schema (Installation, Konfiguration, Features, Kompatibilität).
- **`/sw-sync`** — Prüft das Upstream-Repo shopware/shopware auf neue Versionen/Releases (GitHub releases/tags API) und Trunk-Drift und aktualisiert die sw-*-Skill-Bibliothek.

## Hooks

- **PostToolUse** (Edit/Write): kontextsensitive Lint-/Katalog-Reminder bei Shopware-Dateien (ecs/phpstan, stylelint, eslint, ludtwig; Katalog-Refresh). Siehe `hooks/hooks.json`.
