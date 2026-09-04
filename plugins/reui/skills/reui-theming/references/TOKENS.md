# Extended Semantic Tokens

ReUI extends the official shadcn/ui theming system with additional semantic tokens for precise,
context-aware UI states (used by components such as Alerts, Badges, and Data Grids).

**Scope statement:** the upstream Styling page documents only these extended tokens. It
explicitly defers general customization (adding custom colors, switching between utility classes
and variables) to the official shadcn/ui documentation. There is no broader ReUI-specific theme
system beyond what is shown below — nothing else is invented here.

Upstream recommends adopting these custom color tokens (over plain standard shadcn/ui themes) to
ensure the intended design quality and consistent contrast across all component states.

## Token list

| Token | Purpose |
|---|---|
| `--destructive-foreground` | Foreground color specifically for destructive actions / high-contrast destructive actions and error states. |
| `--info` | Background color for informational states. |
| `--info-foreground` | Text color for informational alerts and badges. |
| `--success` | Background color for success/positive outcomes. |
| `--success-foreground` | Text color for success indicators and positive states. |
| `--warning` | Background color for cautionary states. |
| `--warning-foreground` | Text color for cautionary callouts and warnings. |
| `--invert` | Background color for invert states. |
| `--invert-foreground` | Text color for inverse states. |

## Verbatim code block (`app/globals.css`)

```css
@theme inline {
  --color-destructive-foreground: var(--destructive-foreground);
  --color-info: var(--info);
  --color-info-foreground: var(--info-foreground);
  --color-success: var(--success);
  --color-success-foreground: var(--success-foreground);
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
  --color-invert: var(--invert);
  --color-invert-foreground: var(--invert-foreground);
}

:root {
  --destructive-foreground: var(--color-red-800);
  --info: var(--color-violet-500);
  --info-foreground: var(--color-violet-900);
  --success: var(--color-emerald-500);
  --success-foreground: var(--color-emerald-900);
  --warning: var(--color-yellow-500);
  --warning-foreground: var(--color-yellow-900);
  --invert: var(--color-zinc-900);
  --invert-foreground: var(--color-zinc-50);
}

.dark {
  --destructive-foreground: var(--color-red-600);
  --info: var(--color-violet-500);
  --info-foreground: var(--color-violet-600);
  --success: var(--color-emerald-500);
  --success-foreground: var(--color-emerald-600);
  --warning: var(--color-yellow-500);
  --warning-foreground: var(--color-yellow-600);
  --invert: var(--color-zinc-700);
  --invert-foreground: var(--color-zinc-50);
}
```

## Light vs dark value reference

| Token | `:root` (light) | `.dark` |
|---|---|---|
| `--destructive-foreground` | `var(--color-red-800)` | `var(--color-red-600)` |
| `--info` | `var(--color-violet-500)` | `var(--color-violet-500)` |
| `--info-foreground` | `var(--color-violet-900)` | `var(--color-violet-600)` |
| `--success` | `var(--color-emerald-500)` | `var(--color-emerald-500)` |
| `--success-foreground` | `var(--color-emerald-900)` | `var(--color-emerald-600)` |
| `--warning` | `var(--color-yellow-500)` | `var(--color-yellow-500)` |
| `--warning-foreground` | `var(--color-yellow-900)` | `var(--color-yellow-600)` |
| `--invert` | `var(--color-zinc-900)` | `var(--color-zinc-700)` |
| `--invert-foreground` | `var(--color-zinc-50)` | `var(--color-zinc-50)` |

Note: `--info` and `--success` and `--warning` keep the identical base color value between light
and dark (only their `-foreground` counterparts change); `--destructive-foreground` and
`--invert`/`--invert-foreground` change in both modes as shown. This is exactly what the source
`:root`/`.dark` blocks state — no interpretation added.

## Where to go for everything else

"For general customization guidelines such as adding your own custom colors or switching between
utility classes and variables, please refer to the official shadcn/ui documentation." The
upstream ReUI Styling page states nothing further about the theming system.

## Source

https://reui.io/docs/styling — mirrored 2026-09-04.
