# Shopware 6 — Storefront JS event catalog (project introspection)

Answers: **"which JS events exist, where are they published/subscribed, what do they carry?"** — from a
cached catalog. The basis for cross-plugin JS communication (`sw-js-events`).

## Usage
1. The catalog lives at `.shopware-catalog/js-events.md` in the project root.
2. **Missing/outdated** → regenerate with `/sw-js-plugin-map` (agent `shopware-js-plugin-mapper`, haiku) — the
   mapper writes both `js-plugins.md` and `js-events.md`.
3. Look up: event name → publish location(s), subscribe location(s), arguments (`event.detail` fields), type
   (emitter / native / PluginManager lifecycle).

## Covered event types
- **$emitter events**: `this.$emitter.publish('name', detail)` ↔ `document.$emitter.subscribe('name', cb)`.
- **Native DOM events**: `dispatchEvent(new CustomEvent('name', { detail }))` / `addEventListener`.
- **PluginManager lifecycle**: initialization/update events.

## When to regenerate
- After `git pull` / plugin install/update, after creating your own JS events.

To **publish/subscribe** in code: `sw-js-events`. The catalog is the source of truth about existing JS events.
