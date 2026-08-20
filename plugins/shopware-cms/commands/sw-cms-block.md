---
name: sw-cms-block
description: Scaffold a Shopware 6 CMS block — admin block and preview component + registerCmsBlock (slots) and the storefront block template.
argument-hint: <block-name> [--plugin <PluginName>] [--slots left,right]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-cms-block

Create a CMS block. Skills: `sw-cms-block`.

## Steps
1. Block name (kebab-case, owner prefix) + target plugin + slots (name → default element).
2. Admin (`.../module/sw-cms/blocks/<category>/<name>/`): `index.js` (`registerCmsBlock` with slots/defaultConfig +
   `Component.register` for the block and preview components), `.html.twig` with a `<slot name="...">` per slot.
3. Storefront template `views/storefront/block/cms-block-<name>.html.twig`.
4. Import it in main.js. Note: admin build.

Keep the slots consistent across the admin template, `registerCmsBlock.slots` and the storefront. Elements are created by `/sw-cms-element`.
