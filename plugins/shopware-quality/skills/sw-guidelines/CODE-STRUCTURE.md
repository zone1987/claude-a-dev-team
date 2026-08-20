# Shopware 6 — code structure and extension types

Complete reference: `CODE-STRUCTURE-DETAIL.md`

## Choosing an extension type

| Type | When | Characteristic |
|-----|------|-------------|
| **Custom bundle** | Project-owned installation, full control | No plugin lifecycle, plain Symfony bundle |
| **Static plugin** | Project-specific, few projects | Standard skeleton, keep overrides thin |
| **Managed plugin** | Shopware Store release | Strict metadata, BC guarantees, no project hacks |
| **App** | No PHP in the shop / SaaS / cloud | Manifest plus app server, multi-tenant |
| **Theme** | Adjust storefront appearance only | Stripped-down plugin; in the cloud via an app |

## Core conventions

- PSR-4 autoloading: map namespaces exactly to folder names
- `composer.json` type: `shopware-platform-plugin` or `shopware-bundle`
- DB changes: always via migrations (idempotent, non-destructive in `update()`)
- Encapsulate integration points (events, DAL extensions, decorators) behind service classes

## Upgrade orientation

- Few cross-plugin dependencies
- Do NOT split related logic across several plugins
- Prefer one repository with consistent tooling
- The more surface area is exposed to the platform core, the more upgrade effort it creates

Boundary: this skill covers structure and layout. Extension patterns (events/decorator)
→ `sw-extendability`. Coding style and static analysis → `sw-coding-guidelines`.
