---
name: sw-cms-block
description: Scaffold eines Shopware-6 CMS-Blocks — Admin-Block-/Preview-Komponente + registerCmsBlock (Slots) und Storefront-Block-Template.
argument-hint: <block-name> [--plugin <PluginName>] [--slots left,right]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-cms-block

Erzeuge einen CMS-Block. Skills: `sw-cms-block`, `sw-cms-block-admin`.

## Ablauf
1. Block-Name (kebab, Owner-Präfix) + Ziel-Plugin + Slots (Name → Default-Element).
2. Admin (`.../module/sw-cms/blocks/<category>/<name>/`): `index.js` (`registerCmsBlock` mit slots/defaultConfig +
   `Component.register` für Block- und Preview-Komponente), `.html.twig` mit `<slot name="...">` je Slot.
3. Storefront-Template `views/storefront/block/cms-block-<name>.html.twig`.
4. In main.js importieren. Hinweis: Admin-Build.

Slots in Admin-Template, `registerCmsBlock.slots` und Storefront konsistent halten. Elemente erzeugt `/sw-cms-element`.
