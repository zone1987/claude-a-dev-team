# shadcn-vue NavigationMenu Component

## Triggers
shadcn-vue navigation-menu, navigation menu vue, navigationsmenue vue, navigation menu component shadcn,
navbar dropdown vue, navigation menu reka-ui vue, nav menu trigger vue, navigation menu viewport vue,
nav link vue

## Overview

The `NavigationMenu` component builds accessible horizontal navigation with animated dropdown panels. It wraps reka-ui's `NavigationMenuRoot` and exports a `navigationMenuTriggerStyle` CVA utility for standalone link styling.

## Sub-components

| Component | reka-ui Base | Description |
|---|---|---|
| `NavigationMenu` | `NavigationMenuRoot` | Root container, auto-includes viewport |
| `NavigationMenuList` | `NavigationMenuList` | Horizontal list of menu items |
| `NavigationMenuItem` | `NavigationMenuItem` | Single nav entry |
| `NavigationMenuTrigger` | `NavigationMenuTrigger` | Button that opens a dropdown |
| `NavigationMenuContent` | `NavigationMenuContent` | Dropdown content panel |
| `NavigationMenuLink` | `NavigationMenuLink` | Active-state-aware nav link |
| `NavigationMenuViewport` | `NavigationMenuViewport` | Animated floating viewport |
| `NavigationMenuIndicator` | `NavigationMenuIndicator` | Animated arrow indicator |

## NavigationMenu Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `viewport` | `boolean` | `true` | Whether to include the floating viewport |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS |
| All `NavigationMenuRootProps` | — | — | Forwarded to reka-ui |

## Exported Utility

```ts
import { navigationMenuTriggerStyle } from "@/components/ui/navigation-menu"
// Returns CVA className string for use on standalone links
```

## Viewport Behavior
- `viewport=true` (default): animated floating panel, content slides in/out
- `viewport=false`: inline content with zoom animations (no floating layer)

## References
- Source: `MENU-SOURCE.md`
- API: `MENU-API.md`
- Examples: `MENU-EXAMPLES.md`
- Installation: `MENU-INSTALLATION.md`
