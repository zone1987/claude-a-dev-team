---
name: reui-setup
description: ReUI installation in a shadcn project: components.json registries, the @reui namespace, REUI_LICENSE_KEY, base-nova vs radix-nova, RTL. Use when installing ReUI or editing an @reui entry.
---

# Installing ReUI

ReUI installs through the shadcn CLI into an existing shadcn project. There is no runtime package:
`add` copies source into the repository, so an update means running `add` again.

## The four things that must be right

1. **React 19 and Tailwind CSS v4**, with shadcn/ui already initialised.
2. **`components.json` → `style`** — `base-nova` (Base UI) or `radix-nova` (Radix UI). This decides
   which build the CLI installs *and* which API your code must be written against. Read it before
   writing a line of component code; never pass a style to the CLI.
3. **The `@reui` registry entry** in `components.json`, in one of two forms.
4. **`REUI_LICENSE_KEY`** in `.env.local`, for premium items only.

## The two registry forms

Free items — the 22 primitives, the documented `file-upload` pattern, and every `c-*` example —
install with the plain string:

```json
{ "registries": { "@reui": "https://reui.io/r/{style}/{name}.json" } }
```

Premium items — blocks, icons, templates — need the authenticated object form:

```json
{
  "registries": {
    "@reui": {
      "url": "https://reui.io/r/{style}/{name}.json",
      "headers": { "Authorization": "Bearer ${REUI_LICENSE_KEY}" }
    }
  }
}
```

The authenticated form installs free items too, so a project never needs both. The shadcn CLI
expands `${REUI_LICENSE_KEY}` from the environment — keep the real key in `.env.local`, never in a
committed file.

A premium install missing either half fails with a **401 after resolving dependencies**, which reads
like a network fault rather than a licence one.

## Reference map

- **[PREREQUISITES.md](references/PREREQUISITES.md)**: React and Tailwind versions, and the shadcn
  state the CLI expects.
- **[INSTALLATION.md](references/INSTALLATION.md)**: the full walkthrough with the exact commands for
  pnpm, npm, yarn and bun.
- **[REGISTRY-CONFIG.md](references/REGISTRY-CONFIG.md)**: both registry forms, the `{style}` and
  `{name}` placeholders, and how free items resolve their shared `@reui/*` dependencies.
- **[LICENSE-SETUP.md](references/LICENSE-SETUP.md)**: the key, the header, and what each tier
  unlocks at install.
- **[RTL.md](references/RTL.md)**: what the CLI converts for you and what stays your job.
- **[PLANS.md](references/PLANS.md)**: Free, Pro and Ultimate side by side.

## Source

[Get Started](https://reui.io/docs/get-started), [Registry](https://reui.io/docs/registry),
[License Setup](https://reui.io/docs/license-setup), [RTL](https://reui.io/docs/rtl), mirrored
2026-09-04.
