# shopware-cms

> Eigene CMS-Bausteine für die Erlebniswelten (Shopping Experiences).

`shopware-cms` ist auf die **Erlebniswelten** (Shopping Experiences / CMS) spezialisiert und zeigt, wie man die
drei Ebenen eines eigenen CMS-Bausteins konsistent umsetzt.

Enthalten: eigene **CMS-Blöcke** (Layout-Container mit benannten Slots — Admin-Registrierung via `cmsService` +
Block-/Preview-Komponente + Storefront-Template), eigene **CMS-Elemente** (Inhaltsbausteine — Admin-Komponente,
Config-Komponente, Preview, **PHP-DataResolver** mit `collect()`/`enrich()`, Storefront-Template) sowie die
**Slot-/Element-Konfiguration** (`FieldConfig`, `source: static|mapped`).

Spezialist **`shopware-cms`**; Scaffolder **`/sw-cms-element`** und **`/sw-cms-block`** erzeugen alle Ebenen mit
konsistenten Namen. **Wann nutzen:** für individuelle Inhaltsbausteine im Page-Builder. Das headless-Rendering der
gleichen Inhalte behandelt `shopware-frontends` (`@shopware/cms-base`); die Bedienung der Erlebniswelten aus
Betreibersicht `shopware-merchant`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-cms@claude-a-dev-team
```

## Skills (7)

`sw-cms-block`, `sw-cms-block-admin`, `sw-cms-data-resolver`, `sw-cms-element`, `sw-cms-element-admin`, `sw-cms-element-storefront`, `sw-cms-slot-config`

## Agents (1)

- **`shopware-cms`** — Spezialist für das Shopware-6.7 CMS (Erlebniswelten/Shopping Experiences): eigene CMS-Blöcke und CMS-Elemente (Admin-Komponenten + DataResolver + Storefront-Template), Slot-/Element-Konfiguration.

## Commands (2)

- **`/sw-cms-block`** — Scaffold eines Shopware-6 CMS-Blocks — Admin-Block-/Preview-Komponente + registerCmsBlock (Slots) und Storefront-Block-Template.
- **`/sw-cms-element`** — Scaffold eines kompletten Shopware-6 CMS-Elements — Admin (component/config/preview + registerCmsElement), PHP-DataResolver und Storefront-Template.
