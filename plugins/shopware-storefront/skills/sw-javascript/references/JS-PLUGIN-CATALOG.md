# Shopware 6 — JS plugin catalog (project introspection)

Answers: **"which Storefront JS plugins exist in THIS project?"** — from a cached catalog.

## Usage
1. The catalog lives at `.shopware-catalog/js-plugins.md` in the project root.
2. **Missing/outdated** → regenerate with `/sw-js-plugin-map` (agent `shopware-js-plugin-mapper`, haiku).
3. Look up: plugin name → file, purpose, selector, options, override points — before overriding a core plugin
   (`sw-js-plugin-override`) or extending it (`sw-js-plugin-extend`).

## When to regenerate
- After `git pull` / plugin install/update, after creating or changing your own JS plugins or the `main.js` registry.

To **build** new JS plugins, use the reference skills (`sw-storefront-js-plugin`, `sw-js-plugin-override`,
`sw-js-plugin-extend`); the catalog is the source of truth about existing plugins.
