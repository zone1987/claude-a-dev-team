# API Reference

reka-ui API: https://reka-ui.com/docs/components/tags-input#api-reference

## Sub-Komponenten

| Component | Description |
|-----------|-------------|
| `TagsInput` | Root container (`TagsInputRoot`), manages tag list |
| `TagsInputInput` | Text input for entering new tags |
| `TagsInputItem` | Individual tag chip wrapper |
| `TagsInputItemText` | Text label inside a tag chip |
| `TagsInputItemDelete` | Delete button inside a tag chip |

## TagsInput (Root) Props

Extends `TagsInputRootProps` from reka-ui:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `string[]` | — | Controlled tag list |
| `defaultValue` | `string[]` | `[]` | Uncontrolled initial tags |
| `disabled` | `boolean` | `false` | Disables all interactions |
| `delimiter` | `string \| string[]` | `','` | Characters that trigger tag creation |
| `addOnPaste` | `boolean` | `false` | Create tags on paste |
| `max` | `number` | — | Maximum number of tags |
| `duplicate` | `boolean` | `false` | Allow duplicate tags |
| `dir` | `'ltr' \| 'rtl'` | — | Text direction |
| `class` | `string` | — | Additional CSS classes |

## TagsInput Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `string[]` | Emitted when tags change |

## TagsInputItem Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `string` | yes | Tag value for this chip |
| `disabled` | `boolean` | — | Disables this tag |
| `class` | `string` | — | Additional CSS classes |

## TagsInputInput Props

Extends `TagsInputInputProps` from reka-ui:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `placeholder` | `string` | — | Input placeholder text |
| `autoFocus` | `boolean` | `false` | Focus on mount |
| `maxLength` | `number` | — | Max input length |
| `class` | `string` | — | Additional CSS classes |

## TagsInputItemDelete Slots

| Slot | Description |
|------|-------------|
| default | Custom delete icon (default: X icon from lucide) |

## Data Attributes (reka-ui)

| Attribute | Values | Description |
|-----------|--------|-------------|
| `data-state` | `active \| inactive` | Tag item focus state |
| `data-disabled` | present | Component is disabled |
| `aria-invalid` | `true` | Triggers destructive ring styling |
