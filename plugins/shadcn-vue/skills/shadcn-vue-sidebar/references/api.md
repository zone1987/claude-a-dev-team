# API Reference

## SidebarProvider

Root context provider. Must wrap all sidebar components.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `defaultOpen` | `boolean` | `true` (reads cookie) | Initial open state (uncontrolled) |
| `open` | `boolean` | `undefined` | Controlled open state |
| `class` | `string` | — | Additional CSS classes |

### Emits

| Event | Payload | Description |
|---|---|---|
| `update:open` | `boolean` | Fired when open state changes (controlled mode) |

### Constants

| Constant | Value | Description |
|---|---|---|
| `SIDEBAR_WIDTH` | `"16rem"` | Desktop sidebar width |
| `SIDEBAR_WIDTH_ICON` | `"3rem"` | Collapsed icon-only width |
| `SIDEBAR_WIDTH_MOBILE` | `"18rem"` | Mobile sheet width |
| `SIDEBAR_KEYBOARD_SHORTCUT` | `"b"` | Key used with Cmd/Ctrl to toggle |
| `SIDEBAR_COOKIE_NAME` | `"sidebar_state"` | Cookie name for persistence |
| `SIDEBAR_COOKIE_MAX_AGE` | `604800` (7 days) | Cookie TTL in seconds |

---

## useSidebar

Composable to access sidebar context. Must be called inside a `SidebarProvider` subtree.

### Returns

| Property | Type | Description |
|---|---|---|
| `state` | `ComputedRef<"expanded" \| "collapsed">` | Current sidebar state |
| `open` | `Ref<boolean>` | Whether the sidebar is open (desktop) |
| `setOpen` | `(value: boolean) => void` | Set open state (desktop) |
| `openMobile` | `Ref<boolean>` | Whether the mobile sheet is open |
| `setOpenMobile` | `(value: boolean) => void` | Set mobile sheet open state |
| `isMobile` | `Ref<boolean>` | Whether the viewport is mobile (<= 768px) |
| `toggleSidebar` | `() => void` | Toggle open state (respects mobile/desktop) |

---

## Sidebar

The main sidebar container. Renders as a Sheet on mobile and a fixed panel on desktop.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `side` | `"left" \| "right"` | `"left"` | Side the sidebar appears on |
| `variant` | `"sidebar" \| "floating" \| "inset"` | `"sidebar"` | Visual variant |
| `collapsible` | `"offcanvas" \| "icon" \| "none"` | `"offcanvas"` | Collapse behavior |
| `class` | `string` | — | Additional CSS classes |

### Collapsible Values

| Value | Behavior |
|---|---|
| `offcanvas` | Panel slides off-screen when collapsed |
| `icon` | Panel collapses to icon-only strip (width: `--sidebar-width-icon`) |
| `none` | Panel is always visible, cannot be collapsed |

### Variant Values

| Value | Behavior |
|---|---|
| `sidebar` | Standard attached sidebar with border |
| `floating` | Detached floating panel with border and shadow |
| `inset` | Inset layout; pair with `SidebarInset` for the main content area |

### Data Attributes (set automatically)

| Attribute | Values | Description |
|---|---|---|
| `data-state` | `"expanded"`, `"collapsed"` | Current open state |
| `data-collapsible` | `"offcanvas"`, `"icon"`, `""` | Active collapsible mode when collapsed |
| `data-variant` | `"sidebar"`, `"floating"`, `"inset"` | Current variant |
| `data-side` | `"left"`, `"right"` | Current side |

---

## SidebarContent

Scrollable content area inside `Sidebar`. Wraps `SidebarGroup` components.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarHeader

Non-scrolling header area at the top of the sidebar.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarFooter

Non-scrolling footer area at the bottom of the sidebar.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarGroup

Logical grouping of menu items. Provides padding and relative positioning.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarGroupLabel

Label for a `SidebarGroup`. Extends `PrimitiveProps` from reka-ui (supports `as` / `asChild`).
Hides with `-mt-8 opacity-0` when the sidebar is in `icon` collapsible mode.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | `string \| Component` | `"div"` | Rendered HTML element or component |
| `asChild` | `boolean` | `false` | Merge props onto child element |
| `class` | `string` | — | Additional CSS classes |

---

## SidebarGroupAction

Action button absolutely positioned in the top-right of a `SidebarGroup`.
Extends `PrimitiveProps`. Hidden in icon collapse mode.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | `string \| Component` | `"button"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge props onto child |
| `class` | `string` | — | Additional CSS classes |

---

## SidebarGroupContent

Wrapper for the content (menu list) inside a `SidebarGroup`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenu

Unordered list (`<ul>`) container for `SidebarMenuItem` components.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuItem

List item (`<li>`) wrapping a single menu entry. Sets up the `group/menu-item` context.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuButton

Interactive button for a menu item. Supports optional tooltip shown when sidebar is collapsed.
Internally renders `SidebarMenuButtonChild` wrapped in a reka-ui `Tooltip` when `tooltip` is set.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "outline"` | `"default"` | Button visual style |
| `size` | `"default" \| "sm" \| "lg"` | `"default"` | Button size |
| `isActive` | `boolean` | `false` | Marks button as active (highlighted) |
| `tooltip` | `string \| Component` | — | Tooltip content shown when collapsed |
| `as` | `string \| Component` | `"button"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge props onto child |
| `class` | `string` | — | Additional CSS classes |

### Size Values

| Value | Height | Font Size |
|---|---|---|
| `default` | `h-8` | `text-sm` |
| `sm` | `h-7` | `text-xs` |
| `lg` | `h-12` | `text-sm` (icon mode: `p-0`) |

### Variant Values

| Value | Style |
|---|---|
| `default` | Accent background on hover |
| `outline` | Background with border shadow, accent on hover |

---

## SidebarMenuAction

Action button absolutely positioned at the right edge of a menu item.
Hidden in icon collapse mode. Extends `PrimitiveProps`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `showOnHover` | `boolean` | `false` | Only visible on hover/focus of the menu item |
| `as` | `string \| Component` | `"button"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge props onto child |
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuBadge

Absolute-positioned badge shown at the right of a menu button.
Hidden in icon collapse mode.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuSkeleton

Skeleton placeholder for loading states in a menu.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `showIcon` | `boolean` | `false` | Show an icon-sized skeleton before the text |
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuSub

Nested sub-menu list (`<ul>`) with left border. Hidden in icon collapse mode.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuSubItem

List item (`<li>`) inside a `SidebarMenuSub`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarMenuSubButton

Interactive button inside a `SidebarMenuSub`. Extends `PrimitiveProps`.
Hidden in icon collapse mode.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `"sm" \| "md"` | `"md"` | Text size |
| `isActive` | `boolean` | `false` | Marks button as active |
| `as` | `string \| Component` | `"a"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge props onto child |
| `class` | `string` | — | Additional CSS classes |

---

## SidebarInput

Search/filter input styled for the sidebar. Wraps the `Input` component.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarInset

Main content area to place beside the sidebar. Applies responsive margin/rounding
when the sidebar variant is `inset`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarRail

Thin clickable rail on the edge of the sidebar for hover-to-expand and toggle.
Only visible on `sm` breakpoint and above.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarSeparator

Horizontal separator styled for the sidebar. Wraps reka-ui `Separator`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## SidebarTrigger

Toggle button for the sidebar. Uses a `PanelLeft` Lucide icon. Calls `toggleSidebar()`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | — | Additional CSS classes |

---

## data-sidebar Attribute Reference

Every sub-component sets a `data-sidebar` attribute for styling and targeting with CSS selectors.

| Value | Component | Purpose |
|---|---|---|
| `sidebar` | `Sidebar` | The sidebar panel element |
| `content` | `SidebarContent` | Scrollable content wrapper |
| `header` | `SidebarHeader` | Non-scrolling header |
| `footer` | `SidebarFooter` | Non-scrolling footer |
| `group` | `SidebarGroup` | Logical group container |
| `group-label` | `SidebarGroupLabel` | Group heading text |
| `group-action` | `SidebarGroupAction` | Group action button |
| `group-content` | `SidebarGroupContent` | Group content wrapper |
| `menu` | `SidebarMenu` | Menu list (`<ul>`) |
| `menu-item` | `SidebarMenuItem` | Menu list item (`<li>`) |
| `menu-button` | `SidebarMenuButton` / `SidebarMenuButtonChild` | Menu interactive button |
| `menu-action` | `SidebarMenuAction` | Per-item action button |
| `menu-badge` | `SidebarMenuBadge` | Per-item badge |
| `menu-skeleton` | `SidebarMenuSkeleton` | Skeleton loading container |
| `menu-skeleton-icon` | `SidebarMenuSkeleton` | Skeleton icon element |
| `menu-skeleton-text` | `SidebarMenuSkeleton` | Skeleton text element |
| `menu-sub` | `SidebarMenuSub` | Sub-menu list |
| `menu-sub-item` | `SidebarMenuSubItem` | Sub-menu list item |
| `menu-sub-button` | `SidebarMenuSubButton` | Sub-menu button |
| `input` | `SidebarInput` | Search input |
| `separator` | `SidebarSeparator` | Horizontal divider |
| `rail` | `SidebarRail` | Edge toggle rail |
| `trigger` | `SidebarTrigger` | Toggle trigger button |

---

## reka-ui Integration

| Feature | reka-ui Component | Usage |
|---|---|---|
| Tooltip (collapsed state) | `TooltipProvider`, `Tooltip`, `TooltipTrigger`, `TooltipContent` | Wraps `SidebarMenuButton` when `tooltip` prop is set; `TooltipProvider` is in `SidebarProvider` |
| Mobile sheet | `Sheet`, `SheetContent`, `SheetHeader`, `SheetTitle`, `SheetDescription` | Renders the sidebar as a slide-in sheet on mobile |
| Polymorphic rendering | `Primitive` | Used by `SidebarGroupLabel`, `SidebarGroupAction`, `SidebarMenuButtonChild`, `SidebarMenuAction`, `SidebarMenuSubButton` |
| Context | `createContext` | Provides `useSidebar` / `provideSidebarContext` via `utils.ts` |
