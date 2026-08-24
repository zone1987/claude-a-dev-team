---
name: sw-admin-component
description: Scaffolds an administration component in Shopware 6, or an override of a core one, with its Component.register, Twig template and optional SCSS.
argument-hint: <component-name> [--plugin <PluginName>] [--override <coreComponent>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-admin-component

Produce an admin component, or an override. Skills: `sw-components`, `sw-meteor`, `sw-build`.

## Steps
1. Settle the component name (kebab-case with an owner prefix) and the target plugin. With
   `--override <coreComponent>`, produce an override instead.
2. Files in `.../component/<name>/` (or `view/`): `index.js` (`Component.register`, or
   `Component.override`), `<name>.html.twig` (Meteor `mt-*`; for an override, `{% parent %}`), and
   optionally `<name>.scss`.
3. When overriding: `this.$super('method')` for the original logic, and take the block names from the
   core component.
4. Import it in `main.js` or the module. Note the follow-up: the build, plus `eslint:admin` and
   `stylelint`.

Before adding a component, check the admin catalogue (`/sw-admin-map`) for one that already fits.
