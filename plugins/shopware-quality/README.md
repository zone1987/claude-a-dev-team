# shopware-quality

> Quality, conventions, static analysis — and the library's own self-update.

`shopware-quality` enforces **convention compliance and code quality** — and keeps the whole library current.

Covered: the **core coding guidelines** (extendability, `final`/`@internal`, decorator pattern, deprecation,
DB migrations, code written for static analysis) including the complete guideline reference, **domain exceptions**
(factory with stable `code`s), **extendability** and **code structure**, the distilled **ADR knowledge** (index of all
~150 ADRs) and the **static analysis tools** **ECS/PHP-CS-Fixer**, **PHPStan** (+ `phpstan-shopware` rules),
**Deptrac** and **Rector**. Plus the **README generator** and the **changelog** convention.

The centerpiece is the **knowledge sync** (skill `sw-release`, agent **`shopware-librarian`**, command
**`/sw-sync`**): it checks the upstream repository `shopware/shopware` via the **releases/tags API** *and* the **trunk diff**,
maps changes onto the affected skills and proposes updates (`--check`) or applies them (`--apply`).
In addition, **hooks** provide context-sensitive lint/catalog reminders after file changes. Specialist:
**`shopware-reviewer`**. **When to use:** for code reviews, quality gates, README/changelog and keeping
the library up to date.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. The knowledge is distilled from the official sources and embedded; each skill keeps its depth in flat SCREAMING-CASE.md reference files next to its `SKILL.md`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-quality@claude-a-dev-team
```

## Skills (3)

| Skill | Description |
|---|---|
| `sw-analysis` | Shopware static analysis: PHPStan and its Shopware extension, ECS and PHP-CS-Fixer, Deptrac, Rector. Use when configuring or fixing Shopware static analysis |
| `sw-guidelines` | Shopware coding guidelines: code structure, domain exceptions, extendability rules, ADR knowledge, documentation guidelines. Use when reviewing Shopware code against the platform's own conventions |
| `sw-release` | Shopware release hygiene: README and changelog conventions, and the knowledge-sync process for keeping distilled documentation current. Use when preparing a Shopware plugin release |

## Agents (2)

| Agent | Description |
|---|---|
| `shopware-librarian` | Self-update agent for the Shopware skill library. Checks upstream (shopware/shopware) for new versions/releases and trunk drift, maps changes onto the affected sw-* skills and updates/extends/removes knowledge, maintains the .sync-state |
| `shopware-reviewer` | Quality/review specialist for Shopware 6 plugins: checks against coding guidelines, domain exceptions, static analysis (ECS/PHPStan/Deptrac/Rector), conventions and ADRs; proposes fixes; creates README/changelog |

## Commands (3)

| Command | Description |
|---|---|
| `/sw-changelog` | Adds a changelog entry to a Shopware 6 plugin (Keep a Changelog) and optionally bumps the version in composer.json |
| `/sw-readme` | Generates/updates a README for a Shopware 6 plugin following the established README schema (installation, configuration, features, compatibility) |
| `/sw-sync` | Checks the upstream repository shopware/shopware for new versions/releases (GitHub releases/tags API) and trunk drift and updates the sw-* skill library |

## Hooks (1)

| Hook | Description |
|---|---|
| `PostToolUse` | Edit/Write/MultiEdit — context-sensitive lint/catalog reminders on matching files; non-blocking (`hooks/hooks.json`) |
