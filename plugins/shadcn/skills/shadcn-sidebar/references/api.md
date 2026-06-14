# Sidebar — API Reference

## useSidebar hook

Must be used inside a `SidebarProvider`.

```tsx
import { useSidebar } from "@/components/ui/sidebar"

const {
  state,
  open,
  setOpen,
  openMobile,
  setOpenMobile,
  isMobile,
  toggleSidebar,
} = useSidebar()
```

| Property        | Type                      | Description                                   |
| --------------- | ------------------------- | --------------------------------------------- |
| `state`         | `"expanded" \| "collapsed"` | Current state of the sidebar                |
| `open`          | `boolean`                 | Whether the sidebar is open                   |
| `setOpen`       | `(open: boolean) => void` | Sets the open state                           |
| `openMobile`    | `boolean`                 | Whether sidebar is open on mobile             |
| `setOpenMobile` | `(open: boolean) => void` | Sets mobile open state                        |
| `isMobile`      | `boolean`                 | Whether viewport is mobile                    |
| `toggleSidebar` | `() => void`              | Toggles sidebar (desktop and mobile)          |

## SidebarProvider

| Prop           | Type                      | Default | Description                                  |
| -------------- | ------------------------- | ------- | -------------------------------------------- |
| `defaultOpen`  | `boolean`                 | `true`  | Default open state                           |
| `open`         | `boolean`                 | —       | Controlled open state                        |
| `onOpenChange` | `(open: boolean) => void` | —       | Controlled setter                            |
| `style`        | `React.CSSProperties`     | —       | Use `--sidebar-width` CSS var here           |
| `className`    | `string`                  | —       | Additional CSS classes                       |

`data-slot="sidebar-wrapper"`

## Sidebar

| Prop          | Type                                          | Default      | Description                                |
| ------------- | --------------------------------------------- | ------------ | ------------------------------------------ |
| `side`        | `"left" \| "right"`                          | `"left"`     | Which side the sidebar is on               |
| `variant`     | `"sidebar" \| "floating" \| "inset"`         | `"sidebar"`  | Visual variant                             |
| `collapsible` | `"offcanvas" \| "icon" \| "none"`            | `"offcanvas"` | Collapse behavior                         |
| `className`   | `string`                                      | —            | Additional CSS classes                     |

`data-slot="sidebar"`, `data-state`, `data-collapsible`, `data-variant`, `data-side`

**Collapsible modes:**
- `offcanvas` — slides off screen
- `icon` — collapses to icon-only width (`--sidebar-width-icon = 3rem`)
- `none` — not collapsible

## SidebarTrigger

Button (ghost, icon) that calls `toggleSidebar()`. Accepts all `Button` props.

`data-slot="sidebar-trigger"`, `data-sidebar="trigger"`

## SidebarRail

Invisible clickable rail on the edge of the sidebar for toggling.

`data-slot="sidebar-rail"`, `data-sidebar="rail"`

## SidebarInset

Main content area wrapper when using `variant="inset"`. Renders as `<main>`.

`data-slot="sidebar-inset"`

## SidebarHeader / SidebarFooter / SidebarContent

Plain `div` wrappers with predefined spacing.

| Component       | Layout                                     |
| --------------- | ------------------------------------------ |
| `SidebarHeader` | `flex flex-col gap-2 p-2` (sticky top)    |
| `SidebarFooter` | `flex flex-col gap-2 p-2` (sticky bottom) |
| `SidebarContent`| `flex flex-col gap-2 overflow-auto`        |

## SidebarSeparator

A `Separator` styled for the sidebar.

`data-slot="sidebar-separator"`

## SidebarInput

An `Input` styled for the sidebar search.

`data-slot="sidebar-input"`

## SidebarGroup

Container for a navigation section.

`data-slot="sidebar-group"`, `data-sidebar="group"`

### SidebarGroupLabel

| Prop      | Type      | Default | Description                     |
| --------- | --------- | ------- | ------------------------------- |
| `asChild` | `boolean` | `false` | Render as child element         |

`data-slot="sidebar-group-label"`
Hides with transition when `collapsible="icon"`.

### SidebarGroupAction

Optional action button positioned top-right of a group. Accepts `asChild`.

`data-slot="sidebar-group-action"`
Hidden when `collapsible="icon"`.

### SidebarGroupContent

Content wrapper inside a group.

`data-slot="sidebar-group-content"`

## SidebarMenu / SidebarMenuItem

`SidebarMenu` renders as `<ul>`, `SidebarMenuItem` as `<li>`.

## SidebarMenuButton

| Prop        | Type                                         | Default     | Description                                   |
| ----------- | -------------------------------------------- | ----------- | --------------------------------------------- |
| `asChild`   | `boolean`                                    | `false`     | Render as child element (e.g. `<a>` for links) |
| `isActive`  | `boolean`                                    | `false`     | Mark as active (applies accent styles)        |
| `variant`   | `"default" \| "outline"`                    | `"default"` | Visual variant                                |
| `size`      | `"default" \| "sm" \| "lg"`                | `"default"` | Size variant                                  |
| `tooltip`   | `string \| TooltipContent props`             | —           | Tooltip shown when sidebar is icon-collapsed  |

`data-slot="sidebar-menu-button"`, `data-active`, `data-size`

## SidebarMenuAction

| Prop          | Type      | Default | Description                                        |
| ------------- | --------- | ------- | -------------------------------------------------- |
| `asChild`     | `boolean` | `false` | Render as child element                            |
| `showOnHover` | `boolean` | `false` | Only show action on hover/focus of menu item       |

`data-slot="sidebar-menu-action"`
Hidden when `collapsible="icon"`.

## SidebarMenuBadge

Numeric badge inside a menu item.

`data-slot="sidebar-menu-badge"`
Hidden when `collapsible="icon"`.

## SidebarMenuSkeleton

| Prop       | Type      | Default | Description                         |
| ---------- | --------- | ------- | ----------------------------------- |
| `showIcon` | `boolean` | `false` | Whether to show an icon placeholder |

`data-slot="sidebar-menu-skeleton"`

## SidebarMenuSub / SidebarMenuSubItem / SidebarMenuSubButton

Nested submenu components.

`SidebarMenuSubButton` props:
| Prop       | Type             | Default | Description              |
| ---------- | ---------------- | ------- | ------------------------ |
| `asChild`  | `boolean`        | `false` | Render as child          |
| `size`     | `"sm" \| "md"`  | `"md"`  | Text size                |
| `isActive` | `boolean`        | `false` | Active state styling     |

All hidden when `collapsible="icon"`.

## CSS constants

| Constant                   | Value    |
| -------------------------- | -------- |
| `SIDEBAR_WIDTH`            | `16rem`  |
| `SIDEBAR_WIDTH_MOBILE`     | `18rem`  |
| `SIDEBAR_WIDTH_ICON`       | `3rem`   |
| `SIDEBAR_KEYBOARD_SHORTCUT`| `"b"`    |
| `SIDEBAR_COOKIE_NAME`      | `"sidebar_state"` |

## Source files

- `registry/new-york-v4/ui/sidebar.tsx`
