# Menubar — API reference

## Contents

- [Menubar (Root)](#menubar-root)
- [MenubarMenu](#menubarmenu)
- [MenubarTrigger](#menubartrigger)
- [MenubarContent](#menubarcontent)
- [MenubarItem](#menubaritem)
- [MenubarLabel](#menubarlabel)
- [MenubarCheckboxItem](#menubarcheckboxitem)
- [MenubarRadioGroup](#menubarradiogroup)
- [MenubarRadioItem](#menubarradioitem)
- [MenubarSub / MenubarSubTrigger / MenubarSubContent](#menubarsub-menubarsubtrigger-menubarsubcontent)
- [MenubarSeparator](#menubarseparator)
- [MenubarShortcut](#menubarshortcut)
- [reka-ui reference](#reka-ui-reference)

## Menubar (Root)

Based on reka-ui `MenubarRoot`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `MenubarRootProps` | — | Forwarded |

### Emits

| Event | Type | Description |
|---|---|---|
| All `MenubarRootEmits` | — | Forwarded |

---

## MenubarMenu

No styling of its own. Wrapper for `MenubarTrigger` + `MenubarContent`.

### Props

| Prop | Type | Description |
|---|---|---|
| All `MenubarMenuProps` | — | Forwarded (value etc.) |

---

## MenubarTrigger

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `MenubarTriggerProps` | — | Forwarded |

---

## MenubarContent

Rendered inside `MenubarPortal`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `align` | `"start" \| "center" \| "end"` | `"start"` | Alignment |
| `alignOffset` | `number` | `-4` | Offset along the alignment axis |
| `sideOffset` | `number` | `8` | Distance from the trigger |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

---

## MenubarItem

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `inset` | `boolean` | `false` | Left indent (pl-8) to align with icons |
| `variant` | `"default" \| "destructive"` | `"default"` | Color variant |
| `disabled` | `boolean` | `false` | Disabled |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### Emits

| Event | Description |
|---|---|
| `select` | Fired on click/Enter |

---

## MenubarLabel

### Props

| Prop | Type | Description |
|---|---|---|
| `inset` | `boolean` | Left indent (pl-8) |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## MenubarCheckboxItem

### Props

| Prop | Type | Description |
|---|---|---|
| `checked` | `boolean` | Checked state |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

### Slots

| Slot | Description |
|---|---|
| default | Item content |
| `indicator-icon` | Custom check icon (default: `<Check>`) |

---

## MenubarRadioGroup

### Props

| Prop | Type | Description |
|---|---|---|
| `modelValue` | `string` | Currently selected value |

### Emits

| Event | Type | Description |
|---|---|---|
| `update:modelValue` | `string` | Value changes |

---

## MenubarRadioItem

### Props

| Prop | Type | Description |
|---|---|---|
| `value` | `string` | Value of this radio item |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

### Slots

| Slot | Description |
|---|---|
| default | Item content |
| `indicator-icon` | Custom radio icon (default: `<Circle>`) |

---

## MenubarSub / MenubarSubTrigger / MenubarSubContent

| Prop | Type | Description |
|---|---|---|
| `inset` (SubTrigger) | `boolean` | Left indent |
| `open` / `defaultOpen` (Sub) | `boolean` | Controlled/uncontrolled |

---

## MenubarSeparator

Horizontal divider.

---

## MenubarShortcut

Purely presentational `<span>` component for keyboard shortcuts.

## reka-ui reference
- https://reka-ui.com/docs/components/menubar
