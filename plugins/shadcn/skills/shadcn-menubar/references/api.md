# Menubar — API Reference

## Composition

```text
Menubar
├── MenubarMenu
│   ├── MenubarTrigger
│   └── MenubarContent
│       ├── MenubarGroup
│       │   ├── MenubarLabel
│       │   ├── MenubarItem
│       │   └── MenubarItem
│       ├── MenubarSeparator
│       ├── MenubarGroup
│       │   ├── MenubarLabel
│       │   ├── MenubarCheckboxItem
│       │   └── MenubarCheckboxItem
│       ├── MenubarSeparator
│       ├── MenubarGroup
│       │   ├── MenubarLabel
│       │   └── MenubarRadioGroup
│       │       ├── MenubarRadioItem
│       │       └── MenubarRadioItem
│       └── MenubarSub
│           ├── MenubarSubTrigger
│           └── MenubarSubContent
│               └── MenubarGroup
│                   ├── MenubarLabel
│                   ├── MenubarItem
│                   └── MenubarItem
└── MenubarMenu
    ├── MenubarTrigger
    └── MenubarContent
```

## Menubar

Root container. Renders a horizontal bar of menus.

Inherits `MenubarPrimitive.Root` props from `@radix-ui/react-menubar`.

## MenubarMenu

Groups a trigger and its content. No visual output itself.

## MenubarTrigger

Button that opens a `MenubarContent` dropdown.

| Prop        | Type     | Description            |
| ----------- | -------- | ---------------------- |
| `className` | `string` | Additional CSS classes |

## MenubarContent

The dropdown panel. Defaults: `align="start"`, `alignOffset=-4`, `sideOffset=8`. Renders inside a `MenubarPortal`.

## MenubarGroup

Logical group of items. Use with `MenubarLabel` for labelled sections.

## MenubarLabel

Section heading inside a `MenubarContent`. Add `inset` prop to align with non-icon items.

| Prop    | Type      | Default | Description              |
| ------- | --------- | ------- | ------------------------ |
| `inset` | `boolean` | `false` | Left-pads to align text  |

## MenubarItem

A clickable menu item.

| Prop      | Type                          | Default     | Description                  |
| --------- | ----------------------------- | ----------- | ---------------------------- |
| `inset`   | `boolean`                     | `false`     | Left-pads to align with icons |
| `variant` | `"default" \| "destructive"`  | `"default"` | Destructive items show red   |

## MenubarCheckboxItem

A togglable menu item with a checkmark indicator.

| Prop      | Type                          | Default | Description       |
| --------- | ----------------------------- | ------- | ----------------- |
| `checked` | `boolean \| "indeterminate"`  |         | Checked state     |

## MenubarRadioGroup

Wraps `MenubarRadioItem` elements for single-select behavior.

| Prop    | Type     | Description           |
| ------- | -------- | --------------------- |
| `value` | `string` | Currently selected value |

## MenubarRadioItem

A radio-style menu item with a dot indicator.

| Prop    | Type     | Description           |
| ------- | -------- | --------------------- |
| `value` | `string` | This item's value     |

## MenubarSeparator

A horizontal rule between groups, `-mx-1 my-1 h-px bg-border`.

## MenubarShortcut

Inline span for keyboard shortcut labels, `ml-auto text-xs text-muted-foreground`.

## MenubarSub / MenubarSubTrigger / MenubarSubContent

Nested submenu. `MenubarSubTrigger` shows a `ChevronRightIcon`. `MenubarSubContent` has the same animation classes as `MenubarContent`.

---
Source: `content/docs/components/base/menubar.mdx`
