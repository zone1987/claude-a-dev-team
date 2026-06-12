# shopware-cms

**Wofür:** CMS / Erlebniswelten: eigene CMS-Blöcke, CMS-Elemente und DataResolver (Admin- und Storefront-Seite).

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-cms@claude-a-dev-team
```

## Skills (7)

`sw-cms-block`, `sw-cms-block-admin`, `sw-cms-data-resolver`, `sw-cms-element`, `sw-cms-element-admin`, `sw-cms-element-storefront`, `sw-cms-slot-config`

## Agents (1)

- **`shopware-cms`** — Spezialist für das Shopware-6.7 CMS (Erlebniswelten/Shopping Experiences): eigene CMS-Blöcke und CMS-Elemente (Admin-Komponenten + DataResolver + Storefront-Template), Slot-/Element-Konfiguration.

## Commands (2)

- **`/sw-cms-block`** — Scaffold eines Shopware-6 CMS-Blocks — Admin-Block-/Preview-Komponente + registerCmsBlock (Slots) und Storefront-Block-Template.
- **`/sw-cms-element`** — Scaffold eines kompletten Shopware-6 CMS-Elements — Admin (component/config/preview + registerCmsElement), PHP-DataResolver und Storefront-Template.
