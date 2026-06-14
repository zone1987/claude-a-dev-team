# NavigationMenu — API Reference

## Composition

```text
NavigationMenu
├── NavigationMenuList
│   ├── NavigationMenuItem
│   │   ├── NavigationMenuTrigger
│   │   └── NavigationMenuContent
│   │       ├── NavigationMenuLink
│   │       └── NavigationMenuLink
│   └── NavigationMenuItem
│       └── NavigationMenuLink
└── NavigationMenuIndicator
```

## NavigationMenu

Root component. Renders the viewport by default.

| Prop       | Type      | Default | Description                                       |
| ---------- | --------- | ------- | ------------------------------------------------- |
| `viewport` | `boolean` | `true`  | Set `false` to disable the animated viewport panel |

When `viewport=false`, content renders directly below the trigger with zoom animation instead of using the shared viewport.

## NavigationMenuList

Horizontal list container. Use `className` to override flex behavior (e.g. `flex-wrap` for responsive).

## NavigationMenuItem

Wraps a single trigger+content pair. Positioned `relative`.

## NavigationMenuTrigger

Renders a button with a rotating `ChevronDownIcon`. Uses `navigationMenuTriggerStyle()` CVA.

## navigationMenuTriggerStyle

CVA utility function. Apply to `NavigationMenuLink` to give it the same styling as a trigger (useful for top-level links without dropdown content):

```tsx
import { navigationMenuTriggerStyle } from "@/components/ui/navigation-menu"

<NavigationMenuLink className={navigationMenuTriggerStyle()}>
  Docs
</NavigationMenuLink>
```

## NavigationMenuContent

Dropdown content panel. Supports directional slide animations (`data-motion`).

## NavigationMenuViewport

Shared animated viewport that all content panels slide into.

## NavigationMenuLink

A styled link within content panels. Supports `data-[active=true]` for current route highlighting.

Use `asChild` / `render` prop for Next.js `<Link>` integration:

```tsx
import Link from "next/link"
import { NavigationMenuLink, navigationMenuTriggerStyle } from "@/components/ui/navigation-menu"

<NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
  <Link href="/docs">Documentation</Link>
</NavigationMenuLink>
```

## NavigationMenuIndicator

Optional animated arrow indicator below the active trigger.

---
Source: `content/docs/components/base/navigation-menu.mdx`
