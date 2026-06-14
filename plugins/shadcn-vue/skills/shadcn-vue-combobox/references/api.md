# Combobox — API Reference

Full reka-ui API: https://reka-ui.com/docs/components/combobox#api-reference

---

## Combobox (Root)

Wraps `ComboboxRoot` from reka-ui. Forwards all props and emits.

### Key Props (`ComboboxRootProps`)

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `AcceptableValue \| AcceptableValue[]` | — | The controlled selected value(s). Use with `v-model`. |
| `defaultValue` | `AcceptableValue \| AcceptableValue[]` | — | The default selected value(s) for uncontrolled usage. |
| `open` | `boolean` | — | Controlled open state of the combobox popup. |
| `defaultOpen` | `boolean` | `false` | Default open state for uncontrolled usage. |
| `disabled` | `boolean` | `false` | Disables the entire combobox. |
| `multiple` | `boolean` | `false` | Allows selecting multiple items. |
| `items` | `string[] \| object[]` | — | Array of items for built-in filtering. When provided, reka-ui filters automatically on input. |
| `filterFunction` | `(items: string[], searchTerm: string) => string[]` | — | Custom filter function overriding the built-in filter. |
| `displayValue` | `(value: AcceptableValue) => string` | — | Function to derive the display string from a selected value object. |
| `name` | `string` | — | Name attribute for form submission. |
| `resetSearchTermOnBlur` | `boolean` | `true` | Whether to reset the search term when the combobox loses focus. |
| `dir` | `'ltr' \| 'rtl'` | — | Reading direction. |
| `as` | `AsTag \| Component` | `'div'` | Element or component to render as. |
| `asChild` | `boolean` | `false` | Merge props onto child element instead of rendering a wrapper. |

### Emits (`ComboboxRootEmits`)

| Event | Payload | Description |
|---|---|---|
| `update:modelValue` | `AcceptableValue \| AcceptableValue[]` | Fired when the selected value changes. |
| `update:open` | `boolean` | Fired when the open state changes. |

### Slots

| Slot | Props | Description |
|---|---|---|
| `default` | `{ open: boolean, modelValue: ... }` | Default slot with scoped open state and modelValue. |

---

## ComboboxAnchor

Wraps `ComboboxAnchor` from reka-ui. Positions the floating list relative to the trigger element.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| `as` | `AsTag \| Component` | `'div'` | Element or component to render as. |
| `asChild` | `boolean` | `false` | Merge props onto child element. |

Default width: `w-[200px]` (override via `:class`).

---

## ComboboxInput

Wraps `ComboboxInput` from reka-ui. Renders a search field with a `SearchIcon` prefix.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes applied to the `<input>` element. |
| `placeholder` | `string` | — | Placeholder text. |
| `autoFocus` | `boolean` | — | Auto-focus on mount. |
| `disabled` | `boolean` | — | Disables the input. |
| All other `ComboboxInputProps` | — | — | Forwarded to reka-ui `ComboboxInput`. |

Note: `inheritAttrs: false` — extra attributes are merged manually alongside forwarded props.

---

## ComboboxTrigger

Wraps `ComboboxTrigger` from reka-ui. A button that opens/closes the combobox popup.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| `disabled` | `boolean` | — | Disables the trigger. |
| `asChild` | `boolean` | `false` | Merge props onto child element (e.g. use with a `Button`). |
| All other `ComboboxTriggerProps` | — | — | Forwarded to reka-ui `ComboboxTrigger`. |

Always has `tabindex="0"`.

---

## ComboboxList

Wraps `ComboboxContent` inside `ComboboxPortal` from reka-ui. The floating dropdown panel.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| `position` | `'popper' \| 'item-aligned'` | `'popper'` | Positioning strategy. |
| `align` | `'start' \| 'center' \| 'end'` | `'center'` | Alignment relative to the anchor. |
| `sideOffset` | `number` | `4` | Distance in px from the anchor. |
| `side` | `'top' \| 'right' \| 'bottom' \| 'left'` | `'bottom'` | Preferred side to render. |
| All other `ComboboxContentProps` | — | — | Forwarded to reka-ui `ComboboxContent`. |

Note: `inheritAttrs: false` — extra attributes are merged manually.

Default width: `w-[200px]` (override via `:class`).

---

## ComboboxViewport

Wraps `ComboboxViewport` from reka-ui. Scrollable container for items inside `ComboboxList`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| All other `ComboboxViewportProps` | — | — | Forwarded to reka-ui `ComboboxViewport`. |

Default: `max-h-[300px]` scrollable viewport.

---

## ComboboxItem

Wraps `ComboboxItem` from reka-ui. A selectable option in the list.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `AcceptableValue` | — | **Required.** The value this item represents. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| `disabled` | `boolean` | `false` | Disables this item. |
| All other `ComboboxItemProps` | — | — | Forwarded to reka-ui `ComboboxItem`. |

### Emits

| Event | Payload | Description |
|---|---|---|
| `select` | `ComboboxItemSelectEvent` | Fired when the item is selected. |

Data attributes: `data-[highlighted]`, `data-[disabled]`, `data-[selected]`.

---

## ComboboxItemIndicator

Wraps `ComboboxItemIndicator` from reka-ui. Renders its children only when the parent item is selected.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Applied with `ml-auto`. |
| All other `ComboboxItemIndicatorProps` | — | — | Forwarded to reka-ui. |

### Slots

| Slot | Description |
|---|---|
| `default` | Content shown when item is selected (typically a `CheckIcon`). |

---

## ComboboxEmpty

Wraps `ComboboxEmpty` from reka-ui. Displayed when no items match the current search term.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| All other `ComboboxEmptyProps` | — | — | Forwarded to reka-ui. |

Default classes: `py-6 text-center text-sm`.

---

## ComboboxGroup

Wraps `ComboboxGroup` from reka-ui. Groups related items with an optional label heading.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `heading` | `string` | — | Optional group heading text. Rendered as a `ComboboxLabel`. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| All other `ComboboxGroupProps` | — | — | Forwarded to reka-ui. |

---

## ComboboxSeparator

Wraps `ComboboxSeparator` from reka-ui. A horizontal divider line.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |
| All other `ComboboxSeparatorProps` | — | — | Forwarded to reka-ui. |

Default classes: `bg-border -mx-1 h-px`.

---

## ComboboxCancel

Re-exported directly from `reka-ui`. Use to clear the current search term or selection.

```ts
import { ComboboxCancel } from "@/components/ui/combobox"
// or directly:
import { ComboboxCancel } from "reka-ui"
```
