---
name: shadcn-vue-combobox
description: >
  shadcn-vue Combobox component (Vue-Port von shadcn/ui, reka-ui, Tailwind v4, SFC .vue).
  Triggers (DE): "Combobox shadcn-vue", "Autocomplete Input shadcn", "Combobox reka-ui", "ComboboxItem shadcn",
  "Combobox Vue", "Autocomplete Select Vue", "Suchfeld mit Auswahl Vue", "Combobox Komponente Vue".
  Triggers (EN): "combobox shadcn-vue", "autocomplete select vue", "reka-ui combobox", "ComboboxList shadcn",
  "combobox component vue", "searchable select vue", "combobox popup vue", "combobox with groups vue".
---

# shadcn-vue: Combobox

An autocomplete input and command palette with a list of suggestions.
Built on top of reka-ui ComboboxRoot. Supports inline and popup modes, grouped items,
multi-select, disabled state, and custom filter functions.

## Sub-Components

- `Combobox` — Root container (wraps reka-ui ComboboxRoot)
- `ComboboxAnchor` — Positions the floating list relative to the input
- `ComboboxInput` — Search input with integrated SearchIcon
- `ComboboxTrigger` — Button to open the combobox popup
- `ComboboxList` — Floating content panel (wraps ComboboxContent + ComboboxPortal)
- `ComboboxViewport` — Scrollable item container inside the list
- `ComboboxItem` — Individual selectable option
- `ComboboxItemIndicator` — Visual checkmark shown on selected item
- `ComboboxEmpty` — Displayed when no items match the search
- `ComboboxGroup` — Groups items with an optional heading label
- `ComboboxSeparator` — Horizontal divider between items or groups
- `ComboboxCancel` — Re-exported from reka-ui directly

## Key Features

- Inline mode (input + list without popup) and popup mode (trigger button + floating list)
- Built-in search/filter via reka-ui `items` prop and `filterFunction` override
- Animated open/close via Tailwind `data-[state=open/closed]` classes
- Grouped items via `ComboboxGroup` with optional `heading` prop
- Multi-select via `:multiple="true"` on root
- Disabled combobox via `:disabled="true"` on root
- Fully accessible (WAI-ARIA)
- Classic alternative pattern: Popover + Command components composition

## Reference Files

- `references/installation.md` — CLI and manual installation steps
- `references/source.md` — Complete Vue source code for all component files
- `references/api.md` — Props, emits, slots, reka-ui API link
- `references/examples.md` — All demo examples with full code (basic, popup, disabled, groups, classic Popover+Command pattern)
