# DropdownMenu — API

Reka-UI API reference: https://reka-ui.com/docs/components/dropdown-menu#api-reference

## Sub-components

| Component | Description |
|---|---|
| `DropdownMenu` | Root wrapper (DropdownMenuRoot) |
| `DropdownMenuTrigger` | Trigger element |
| `DropdownMenuPortal` | Ported into `<body>` (re-export from reka-ui) |
| `DropdownMenuContent` | Dropdown container, `sideOffset: 4` |
| `DropdownMenuGroup` | Groups related items |
| `DropdownMenuLabel` | Non-interactive label |
| `DropdownMenuItem` | Interactive item (default/destructive) |
| `DropdownMenuSeparator` | Horizontal divider |
| `DropdownMenuShortcut` | Keyboard shortcut display (right) |
| `DropdownMenuCheckboxItem` | Item with check indicator |
| `DropdownMenuRadioGroup` | Container for radio items |
| `DropdownMenuRadioItem` | Item with radio indicator |
| `DropdownMenuSub` | Submenu root |
| `DropdownMenuSubTrigger` | Trigger for submenu (ChevronRight) |
| `DropdownMenuSubContent` | Content of the submenu |

## DropdownMenu (Root)

| Prop | Type | Default |
|---|---|---|
| `open` | `boolean` | - |
| `defaultOpen` | `boolean` | `false` |
| `modal` | `boolean` | `true` |
| `dir` | `"ltr" \| "rtl"` | - |

## DropdownMenuItem

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "destructive"` | `"default"` | Highlighted in red when destructive |
| `inset` | `boolean` | `false` | Left indent (pl-8) |
| `disabled` | `boolean` | `false` | Item disabled |
| `class` | `string` | - | - |

## DropdownMenuCheckboxItem

| Prop | Type | Description |
|---|---|---|
| `checked` | `boolean \| "indeterminate"` | State |
| `class` | `string` | - |

Emits: `update:checked`

Named slot `indicator-icon`: custom icon instead of the check icon.

## DropdownMenuRadioGroup / RadioItem

RadioGroup: `v-model` / `modelValue`, emit `update:modelValue`.
RadioItem: `value` (required), `class`.

Named slot `indicator-icon` on RadioItem.
