# DropdownMenu — API

Reka-UI API-Referenz: https://reka-ui.com/docs/components/dropdown-menu#api-reference

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `DropdownMenu` | Root-Wrapper (DropdownMenuRoot) |
| `DropdownMenuTrigger` | Trigger-Element |
| `DropdownMenuPortal` | Portiert in `<body>` (re-export von reka-ui) |
| `DropdownMenuContent` | Dropdown-Container, `sideOffset: 4` |
| `DropdownMenuGroup` | Gruppiert verwandte Items |
| `DropdownMenuLabel` | Nicht-interaktives Label |
| `DropdownMenuItem` | Interaktives Item (default/destructive) |
| `DropdownMenuSeparator` | Horizontaler Trenner |
| `DropdownMenuShortcut` | Tastatur-Shortcut-Anzeige (rechts) |
| `DropdownMenuCheckboxItem` | Item mit Check-Indikator |
| `DropdownMenuRadioGroup` | Container fuer Radio-Items |
| `DropdownMenuRadioItem` | Item mit Radio-Indikator |
| `DropdownMenuSub` | Sub-Menu-Root |
| `DropdownMenuSubTrigger` | Trigger fuer Sub-Menu (ChevronRight) |
| `DropdownMenuSubContent` | Inhalt des Sub-Menus |

## DropdownMenu (Root)

| Prop | Typ | Standard |
|---|---|---|
| `open` | `boolean` | - |
| `defaultOpen` | `boolean` | `false` |
| `modal` | `boolean` | `true` |
| `dir` | `"ltr" \| "rtl"` | - |

## DropdownMenuItem

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | `"default" \| "destructive"` | `"default"` | Rot hervorgehoben bei destructive |
| `inset` | `boolean` | `false` | Links-Einzug (pl-8) |
| `disabled` | `boolean` | `false` | Item deaktiviert |
| `class` | `string` | - | - |

## DropdownMenuCheckboxItem

| Prop | Typ | Beschreibung |
|---|---|---|
| `checked` | `boolean \| "indeterminate"` | Zustand |
| `class` | `string` | - |

Emits: `update:checked`

Named slot `indicator-icon`: eigenes Icon anstelle des Check-Icons.

## DropdownMenuRadioGroup / RadioItem

RadioGroup: `v-model` / `modelValue`, emit `update:modelValue`.
RadioItem: `value` (required), `class`.

Named slot `indicator-icon` auf RadioItem.
