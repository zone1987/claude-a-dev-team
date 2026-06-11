# Konventionen — Shopware-Entwicklungsbibliothek

Verbindliche Regeln für alle Plugins, Skills, Agents, Commands und Hooks in diesem Marketplace.
Wissensquelle (kanonisch): die Shopware-6.7-Trunk-Source unter `…/Claude-Plugins/shopware`
(`src/`, `adr/` (151 ADRs), `coding-guidelines/`, `AGENTS.md`, `UPGRADE-*`, `RELEASE_INFO-*`, `changelog/`).

## Marketplace-Layout

```
claude-a-dev-team/
├── .claude-plugin/marketplace.json     # registriert alle Plugins + deren Skills
├── CONVENTIONS.md                      # dieses Dokument
└── plugins/
    └── <plugin>/
        ├── .claude-plugin/plugin.json  # flache Form: name, version, description, author, license, keywords, category
        ├── README.md
        ├── .gitignore
        ├── skills/<skill>/SKILL.md (+ references/, optional examples/)
        ├── agents/<agent>.md            # auto-discovered
        ├── commands/<command>.md        # auto-discovered
        └── hooks/hooks.json             # optional
```

Plugin-Namen: `shopware-<thema>` (Themen-Plugin) bzw. produktspezifisch (`ff-octo-api`).
Neue Skills in `marketplace.json` unter dem passenden Plugin in `skills: []` eintragen.

## Naming

| Artefakt | Schema | Beispiel |
|---|---|---|
| Plugin | `shopware-<thema>` | `shopware-data` |
| Skill (generisch) | `sw-<thema>` | `sw-entity-definition` |
| Skill (produktspez.) | `<prefix>-<name>` | `ff-octo-api` |
| Agent | `shopware-<rolle>` | `shopware-dal-expert` |
| Command | `/sw-<verb-objekt>` | `/sw-entity` |
| Katalog-Datei (Introspektion) | `.shopware-catalog/<thema>.md` | `.shopware-catalog/entities.md` |

Alles kebab-case.

## Token-Sparsamkeit (zentral)

1. **Skills haben kein `model:`-Feld.** Sparsamkeit entsteht durch **progressive disclosure**:
   - `SKILL.md` schlank (**Ziel < 80 Zeilen**): Trigger, Kurzüberblick, Verweise auf `references/`.
   - Tiefe (vollständige Klassen, lange Beispiele, Edge-Cases) gehört in `references/*.md` — wird nur geladen, wenn gebraucht.
2. **Commands/Agents wählen das günstigste taugliche Model:**
   - `haiku` → mechanisch/Template-getrieben: Scaffolder (`/sw-config-create`, `/sw-custom-field`), Code-Scanner/Mapper (`shopware-entity-mapper`).
   - `sonnet` → fokussierte Spezialisten und urteilende Commands (`/sw-entity`, `shopware-dal-expert`).
   - `opus` → nur Orchestrator (`shopware-dev`), Migrator (`shopware-migrator`), Knowledge-Sync (`shopware-librarian`).
3. **Wissen einbetten, nicht verlinken.** `references/` enthalten destilliertes Wissen — KEINE Verweise auf Trunk-Pfade (Trunk liegt im Nutzerprojekt nicht vor).

## Frontmatter-Templates

### Skill — `skills/<name>/SKILL.md`
```markdown
---
name: sw-entity-definition
description: >
  <Was + wann>. Trigger: "<konkrete Trigger-Phrasen, DE+EN>". Shopware 6.7.
---

# <Titel>

<1–3 Sätze Überblick. Minimal-Beispiel.>

## Vertiefung
- [references/full-example.md](references/full-example.md) — <wofür>
```

### Agent — `agents/<name>.md`
```markdown
---
name: shopware-dal-expert
description: >
  <Rolle + wann delegieren>.
tools: Read, Grep, Glob, Bash, Edit, Write
model: sonnet
skills: sw-entity-definition, sw-field-types, sw-associations-onetomany
---

# <Titel>
<Anweisungen, Hotspots, Vorgehensweise.>
```

### Command — `commands/<name>.md`
```markdown
---
name: sw-entity
description: Scaffold einer DAL-Entity (Definition + Entity + Collection + Migration + services.xml).
argument-hint: <EntityName> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

<Anweisungen für die Generierung.>
```

### Hook — `hooks/hooks.json`
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "<script-or-echo>" }
        ]
      }
    ]
  }
}
```

## Referenz-Skill vs. Introspektion

- **Referenz-Skill** = „wie baut man X" (statisch, aus Trunk destilliert).
- **Introspektion** = „was existiert in DIESEM Projekt" → ein `haiku`-Mapper-Agent + Command scannt Vendor + `custom/plugins` und schreibt einen gecachten Markdown-Katalog nach `.shopware-catalog/`. Andere Skills/Agents lesen den Katalog.

## Stack-Fixpunkte (Shopware 6.7)

PHP 8.2+, Symfony 7, Doctrine DBAL 4 (kein ORM — DAL + `Criteria`), Vue 3 + Pinia/Vite (Admin, `mt-*`),
Twig + Bootstrap 5 + Webpack (Storefront), MySQL/MariaDB, OpenSearch/ES, PHPUnit/PHPStan/Jest/Playwright.
Extensibilität: **Events vor Decorators**. Drei APIs: `/api/` (Admin), `/store-api/` (Store), `/api/_action/sync` (Sync).
Lint: `composer ecs[-fix]`, `composer phpstan`, `composer eslint:admin|storefront[:fix]`, `composer stylelint`, `composer ludtwig:storefront`.
