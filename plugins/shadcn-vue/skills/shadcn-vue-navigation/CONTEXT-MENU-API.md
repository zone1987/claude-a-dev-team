# Context Menu — API Reference

## Contents

- [Sub-components Overview](#sub-components-overview)
- [ContextMenu (Root)](#contextmenu-root)
- [ContextMenuTrigger](#contextmenutrigger)
- [ContextMenuContent](#contextmenucontent)
- [ContextMenuItem](#contextmenuitem)
- [ContextMenuLabel](#contextmenulabel)
- [ContextMenuCheckboxItem](#contextmenucheckboxitem)
- [ContextMenuRadioGroup](#contextmenuradiogroup)
- [ContextMenuRadioItem](#contextmenuradioitem)
- [ContextMenuSub / ContextMenuSubTrigger / ContextMenuSubContent](#contextmenusub-contextmenusubtrigger-contextmenusubcontent)
- [ContextMenuShortcut](#contextmenushortcut)
- [reka-ui API Reference](#reka-ui-api-reference)

## Sub-components Overview

| Component | Description |
|---|---|
| `ContextMenu` | Root container. Wraps `ContextMenuRoot` from reka-ui. |
| `ContextMenuTrigger` | The element that triggers the context menu on right-click. Wraps `ContextMenuTrigger` from reka-ui. |
| `ContextMenuContent` | The dropdown panel. Rendered in a portal. Includes enter/exit animations. |
| `ContextMenuGroup` | Groups related items. No visual separator — use `ContextMenuLabel` + items. |
| `ContextMenuItem` | Standard menu item. Supports `inset` and `variant` props. |
| `ContextMenuLabel` | Non-interactive label. Supports `inset` prop. |
| `ContextMenuSeparator` | Horizontal rule between groups or items. |
| `ContextMenuShortcut` | Display-only span for keyboard shortcut hints. |
| `ContextMenuCheckboxItem` | Checkbox item with check indicator. |
| `ContextMenuRadioGroup` | Groups radio items, manages active value. |
| `ContextMenuRadioItem` | Radio item with circle indicator. |
| `ContextMenuSub` | Root for a nested submenu. |
| `ContextMenuSubTrigger` | Item that opens the nested submenu. Renders a `ChevronRight` icon automatically. |
| `ContextMenuSubContent` | The content panel of the nested submenu. |

---

## ContextMenu (Root)

Extends `ContextMenuRootProps` from reka-ui.

```vue
<ContextMenu>
  <ContextMenuTrigger>Right-click me</ContextMenuTrigger>
  <ContextMenuContent>
    ...
  </ContextMenuContent>
</ContextMenu>
```

---

## ContextMenuTrigger

Extends `ContextMenuTriggerProps` from reka-ui.

The element wrapped by this component becomes the right-click target.

---

## ContextMenuContent

Extends `ContextMenuContentProps` plus `class`.

Automatically wraps in `ContextMenuPortal`. Applies animated open/close transitions.

---

## ContextMenuItem

Props:

| Prop | Type | Default | Description |
|---|---|---|---|
| `inset` | `boolean` | `false` | Adds left padding (`pl-8`) to align with items that have icons |
| `variant` | `"default" \| "destructive"` | `"default"` | Destructive variant applies red text and red hover background |
| `class` | `string?` | — | Additional CSS classes |
| + all `ContextMenuItemProps` | — | — | reka-ui ContextMenuItem props (disabled, etc.) |

```vue
<ContextMenuItem variant="destructive">Delete</ContextMenuItem>
```

---

## ContextMenuLabel

Props:

| Prop | Type | Description |
|---|---|---|
| `inset` | `boolean?` | Adds `pl-8` for alignment with inset items |
| `class` | `string?` | Additional CSS classes |
| + all `ContextMenuLabelProps` | — | reka-ui ContextMenuLabel props |

---

## ContextMenuCheckboxItem

Extends `ContextMenuCheckboxItemProps` plus `class`.

Uses `v-model:checked` (bound via `ContextMenuCheckboxItemProps`) to toggle.

The check indicator slot is named `indicator-icon` and defaults to a `Check` icon.

```vue
<ContextMenuCheckboxItem v-model:checked="checked">
  Show Bookmarks
</ContextMenuCheckboxItem>
```

---

## ContextMenuRadioGroup

Extends `ContextMenuRadioGroupProps` plus emits for `v-model:modelValue`.

```vue
<ContextMenuRadioGroup v-model="position">
  <ContextMenuRadioItem value="top">Top</ContextMenuRadioItem>
  <ContextMenuRadioItem value="bottom">Bottom</ContextMenuRadioItem>
</ContextMenuRadioGroup>
```

---

## ContextMenuRadioItem

Extends `ContextMenuRadioItemProps` plus `class`.

The indicator slot is named `indicator-icon` and defaults to a filled `Circle` icon.

---

## ContextMenuSub / ContextMenuSubTrigger / ContextMenuSubContent

Nested submenu pattern:

```vue
<ContextMenuSub>
  <ContextMenuSubTrigger>More Tools</ContextMenuSubTrigger>
  <ContextMenuSubContent>
    <ContextMenuItem>Save Page As...</ContextMenuItem>
    <ContextMenuItem>Developer Tools</ContextMenuItem>
  </ContextMenuSubContent>
</ContextMenuSub>
```

`ContextMenuSubTrigger` automatically appends a `ChevronRight` icon. Supports `inset` prop.

`ContextMenuSubContent` applies origin and animation classes from `--reka-context-menu-content-transform-origin`.

---

## ContextMenuShortcut

Pure display component. Renders a right-aligned small muted `<span>`.

```vue
<ContextMenuItem>
  New Tab
  <ContextMenuShortcut>⌘T</ContextMenuShortcut>
</ContextMenuItem>
```

---

## reka-ui API Reference

- ContextMenu: https://reka-ui.com/docs/components/context-menu
- Full API Reference: https://reka-ui.com/docs/components/context-menu#api-reference
