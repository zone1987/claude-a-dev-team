# shopware-quality

**Wofür:** Qualität & Selbst-Update: Coding-Guidelines, Extendability, Code-Struktur, Domain-Exceptions, ADR-Wissen, Static-Analysis (ECS/PHPStan/Deptrac/Rector), README/Changelog — plus Knowledge-Sync gegen Upstream und Lint-/Katalog-Hooks.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-quality@claude-a-dev-team
```

## Skills (15)

`shopware-readme`, `sw-adr-knowledge`, `sw-changelog`, `sw-code-structure`, `sw-coding-guidelines`, `sw-deptrac`, `sw-documentation-guidelines`, `sw-domain-exceptions`, `sw-ecs-cs-fixer`, `sw-extendability`, `sw-knowledge-sync`, `sw-phpstan`, `sw-phpstan-shopware`, `sw-rector`, `sw-static-analysis`

## Agents (2)

- **`shopware-librarian`** — Selbst-Update-Agent der Shopware-Skill-Bibliothek. Prüft Upstream (shopware/shopware) auf neue Versionen/Releases und Trunk-Drift, mappt Änderungen auf betroffene sw-*-Skills und aktualisiert/ergänzt/
- **`shopware-reviewer`** — Qualitäts-/Review-Spezialist für Shopware-6-Plugins: prüft gegen Coding-Guidelines, Domain-Exceptions, Static-Analysis (ECS/PHPStan/Deptrac/Rector), Konventionen und ADRs; schlägt Fixes vor; erstellt 

## Commands (3)

- **`/sw-changelog`** — Fügt einem Shopware-6-Plugin einen Changelog-Eintrag hinzu (Keep-a-Changelog) und bumpt optional die Version in composer.json.
- **`/sw-readme`** — Generiert/aktualisiert eine README für ein Shopware-6-Plugin nach dem etablierten README-Schema (Installation, Konfiguration, Features, Kompatibilität).
- **`/sw-sync`** — Prüft das Upstream-Repo shopware/shopware auf neue Versionen/Releases (GitHub releases/tags API) und Trunk-Drift und aktualisiert die sw-*-Skill-Bibliothek.

## Hooks

- **PostToolUse** (Edit/Write): kontextsensitive Lint-/Katalog-Reminder bei Shopware-Dateien (ecs/phpstan, stylelint, eslint, ludtwig; Katalog-Refresh). Siehe `hooks/hooks.json`.
