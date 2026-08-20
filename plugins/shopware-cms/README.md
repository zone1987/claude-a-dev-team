# shopware-cms

> Custom CMS building blocks for the Shopping Experiences.

`shopware-cms` specialises in the **Shopping Experiences** (CMS) and shows how to implement the three levels of a
custom CMS building block consistently.

Included: custom **CMS blocks** (layout containers with named slots — administration registration via
`cmsService` + block/preview component + storefront template), custom **CMS elements** (content building blocks —
administration component, config component, preview, **PHP DataResolver** with `collect()`/`enrich()`, storefront
template) as well as the **slot/element configuration** (`FieldConfig`, `source: static|mapped`).

Specialist **`shopware-cms`**; the scaffolders **`/sw-cms-element`** and **`/sw-cms-block`** generate all levels
with consistent names. **When to use:** for individual content building blocks in the page builder. Headless
rendering of the same content is handled by `shopware-frontends` (`@shopware/cms-base`); operating the Shopping
Experiences from the merchant's perspective by `shopware-merchant`.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official
sources and embedded; depth sits in flat reference files beside each SKILL.md, loaded on demand.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-cms@claude-a-dev-team
```

## Skills (2)

| Skill | Description |
|---|---|
| `sw-cms-block` | Shopware CMS blocks: registering a block, its administration component, slot configuration. Use when building a Shopware CMS block or Shopping Experience block |
| `sw-cms-element` | Shopware CMS elements: registering an element, its administration component, the storefront template, and the data resolver that loads its data. Use when building a Shopware CMS element |

## Agents (1)

| Agent | Description |
|---|---|
| `shopware-cms` | Specialist for the Shopware 6.7 CMS (Shopping Experiences): custom CMS blocks and CMS elements (administration components + DataResolver + storefront template), slot/element configuration |

## Commands (2)

| Command | Description |
|---|---|
| `/sw-cms-block` | Scaffolds a Shopware 6 CMS block — administration block/preview component + registerCmsBlock (slots) and storefront block template |
| `/sw-cms-element` | Scaffolds a complete Shopware 6 CMS element — administration (component/config/preview + registerCmsElement), PHP DataResolver and storefront template |
