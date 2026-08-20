# Shopware 6 — Admin catalog (project introspection)

Answers: **"which admin building blocks exist in THIS project?"** — modules, components, services, mixins,
directives, filters, ApiServices (core + custom) — from a cached catalog.

For each **component** the catalog additionally contains its anatomy: **props, events, slots and Twig blocks** (override points)
plus purpose/structure — so before building/overriding you know exactly which slots/props a component offers.

## Usage
1. The catalog lives at `.shopware-catalog/admin.md` in the project root.
2. **Missing/outdated** → regenerate with `/sw-admin-map` (agent `shopware-admin-mapper`, haiku).
3. Look things up before building: does a service/mixin/component already exist? What is the module/selector called?
   → reuse instead of reinventing; override an existing component (`sw-admin-component-override`).

## When to regenerate
- After `git pull` / plugin install/update, after creating or changing your own modules/components/services/mixins.

For **building**, use the reference skills (`sw-admin-module`, `sw-admin-component`, `sw-admin-services`, `sw-admin-mixins`,
`sw-admin-utils-filters`); the catalog is the source of truth about the admin building blocks that exist.
