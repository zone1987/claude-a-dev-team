---
name: sw-block-find
description: Find which Shopware Storefront template defines a Twig block, CSS class or data attribute, with its nesting, inheritance chain and the SCSS and JS attached to it.
argument-hint: <block name|css class|data attribute|element type>
allowed-tools: Read, Glob, Grep
model: haiku
---

Locate `$ARGUMENTS` in the Storefront structure.

Load the `sw-structure` skill, then answer from its catalogues:

1. **Which template defines it** and where it sits in that template's block nesting.
2. **The narrowest block to override** for a change at this point, and what overriding a parent
   instead would replace.
3. **Who else is affected** — templates extending this one, and other templates including it.
4. **What is attached** — the SCSS file carrying the class, the `data-*` attribute driving a JS
   plugin, and for a CMS element its resolver and configuration fields.

If the project has a `.shopware-catalog/structure.md`, check it too and name any local override.

Report file paths and block names exactly as the catalogue records them. Invent nothing.
