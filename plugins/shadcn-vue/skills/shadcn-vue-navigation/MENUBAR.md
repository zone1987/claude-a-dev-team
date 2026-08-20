# shadcn-vue Menubar Component

## Triggers
shadcn-vue menubar, menubar vue, menuleiste vue, menubar component shadcn, menubar reka-ui vue,
menubar submenu vue, menubar checkbox vue, menubar radio vue, menubar shortcut vue,
menubar separator vue, app menu vue

## Overview

The `Menubar` component provides a desktop-app-style horizontal menu bar. It is built on reka-ui's `MenubarRoot` and renders nested dropdown menus with full keyboard navigation, submenus, checkbox items, radio groups, and shortcuts.

## Sub-components

| Component | reka-ui Base | Description |
|---|---|---|
| `Menubar` | `MenubarRoot` | Root container, horizontal bar |
| `MenubarMenu` | `MenubarMenu` | Individual menu in the bar |
| `MenubarTrigger` | `MenubarTrigger` | Clickable menu tab |
| `MenubarContent` | `MenubarContent` + `MenubarPortal` | Dropdown panel |
| `MenubarItem` | `MenubarItem` | Clickable menu entry |
| `MenubarGroup` | `MenubarGroup` | Groups items without visual separator |
| `MenubarLabel` | `MenubarLabel` | Non-interactive label in dropdown |
| `MenubarSeparator` | `MenubarSeparator` | Horizontal divider |
| `MenubarShortcut` | `<span>` | Keyboard shortcut display |
| `MenubarCheckboxItem` | `MenubarCheckboxItem` | Toggleable checkbox item |
| `MenubarRadioGroup` | `MenubarRadioGroup` | Radio group container |
| `MenubarRadioItem` | `MenubarRadioItem` | Radio-selectable item |
| `MenubarSub` | `MenubarSub` | Submenu root |
| `MenubarSubTrigger` | `MenubarSubTrigger` | Submenu trigger with chevron |
| `MenubarSubContent` | `MenubarSubContent` + `MenubarPortal` | Submenu panel |

## MenubarItem Props

| Prop | Type | Description |
|---|---|---|
| `inset` | `boolean` | Adds left padding (pl-8) to align with icons |
| `variant` | `"default" \| "destructive"` | Color variant |
| `disabled` | `boolean` | Disables the item |

## MenubarLabel Props

| Prop | Type | Description |
|---|---|---|
| `inset` | `boolean` | Adds left padding (pl-8) |

## References
- Source: `MENUBAR-SOURCE.md`
- API: `MENUBAR-API.md`
- Examples: `MENUBAR-EXAMPLES.md`
- Installation: `MENUBAR-INSTALLATION.md`
