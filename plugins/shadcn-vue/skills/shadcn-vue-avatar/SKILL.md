---
name: shadcn-vue-avatar
description: >
  shadcn-vue Avatar component (Vue-Port von shadcn/ui, reka-ui, Tailwind v4, SFC .vue).
  Triggers: "shadcn-vue avatar", "avatar vue", "profilbild vue", "user avatar vue",
  "avatar nuxt", "benutzerbild vue", "user image vue", "profile picture vue"
---

# shadcn-vue Avatar

## Triggers
`shadcn-vue avatar`, `avatar vue`, `profilbild vue`, `user avatar vue`, `avatar nuxt`, `benutzerbild vue`

## Overview

The Avatar component displays a user profile image with an automatic fallback when the image fails to load or is not provided. It is built on top of **reka-ui's `AvatarRoot`** (Radix-Vue successor) and ships three coordinated sub-components:

| Component | reka-ui base | Purpose |
|---|---|---|
| `Avatar` | `AvatarRoot` | Circular 8 × 8 (32 px) container |
| `AvatarImage` | `AvatarImage` | Lazy-loads the image; hidden until loaded |
| `AvatarFallback` | `AvatarFallback` | Shown while image loads or on error |

### Key behaviour
- **Lazy image loading** — `AvatarImage` (reka-ui) waits for the native image to fully load before rendering it. While loading or on error the `AvatarFallback` is shown instead.
- **Fallback delay** — `AvatarFallback` accepts a `delayMs` prop (from reka-ui) to avoid a flash of fallback content on fast connections.
- **Default size** — `Avatar` sets `size-8` (32 × 32 px), `rounded-full`, `overflow-hidden` and `shrink-0` via Tailwind.
- **Custom sizing** — pass a Tailwind class directly via the `class` prop, e.g. `class="size-12"`.

### Extended variants (not in base install)
The shadcn-vue example pages also demonstrate **`AvatarGroup`**, **`AvatarGroupCount`**, and **`AvatarBadge`** (online indicator). These come from the **`reka` extras / new-york-v4 extension layer**, not from the three files in `components/ui/avatar/`. If you need group layouts or badge overlays, you must add those components separately.

## References
- [Installation](references/installation.md)
- [Source code](references/source.md)
- [API reference](references/api.md)
- [Examples](references/examples.md)
- [reka-ui Avatar docs](https://reka-ui.com/docs/components/avatar)
