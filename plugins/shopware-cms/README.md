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

| Skill | Beschreibung |
|---|---|
| `sw-cms-block` | Einen eigenen CMS-Block in Shopware 6 (Erlebniswelten/Shopping Experiences) erstellen: Block-Registrierung im Admin (Shopware.Service('cmsService').registerCmsBlock), Slots, Storefront-Template |
| `sw-cms-block-admin` | Die Admin-Seite eines Shopware-6 CMS-Blocks: Block-Komponente (sw-cms-block-*) + Preview-Komponente (sw-cms-preview-*), Slot-Markup, Registrierung |
| `sw-cms-data-resolver` | Ein CmsElementResolver (DataResolver) in Shopware 6: AbstractCmsElementResolver, collect() (Criteria-Collection) + enrich() (Daten ans Element), Slot-Config auswerten |
| `sw-cms-element` | Ein eigenes CMS-Element in Shopware 6 erstellen (Inhaltsbaustein in Block-Slots): registerCmsElement (Admin) + DataResolver (PHP) + Storefront-Template |
| `sw-cms-element-admin` | Die Admin-Komponenten eines Shopware-6 CMS-Elements: Element-Komponente (sw-cms-el-*), Config-Komponente (sw-cms-el-config-*), Preview (sw-cms-el-preview-*), cms-element/cms-config-Mixin, defaultConfig |
| `sw-cms-element-storefront` | Das Storefront-Template eines Shopware-6 CMS-Elements: cms-element-<name>.html.twig, Zugriff auf element.data/ element.config, Block-/Slot-Rendering |
| `sw-cms-slot-config` | Slot-/Element-Konfiguration in Shopware 6 CMS: FieldConfig/FieldConfigCollection, source 'static' vs |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-cms` | Spezialist für das Shopware-6.7 CMS (Erlebniswelten/Shopping Experiences): eigene CMS-Blöcke und CMS-Elemente (Admin-Komponenten + DataResolver + Storefront-Template), Slot-/Element-Konfiguration |

## Commands (2)

| Command | Beschreibung |
|---|---|
| `/sw-cms-block` | Scaffold eines Shopware-6 CMS-Blocks — Admin-Block-/Preview-Komponente + registerCmsBlock (Slots) und Storefront-Block-Template |
| `/sw-cms-element` | Scaffold eines kompletten Shopware-6 CMS-Elements — Admin (component/config/preview + registerCmsElement), PHP-DataResolver und Storefront-Template |
