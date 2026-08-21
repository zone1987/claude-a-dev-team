# Field — API

## Sub-Components

| Component | Element | Description |
|---|---|---|
| `Field` | `<div role="group">` | Root container with orientation variants |
| `FieldGroup` | `<div>` | Groups multiple Fields (`@container/field-group`) |
| `FieldContent` | `<div>` | Area for label + description with checkboxes/radios |
| `FieldLabel` | `<Label>` | Accessible label (wraps reka-ui Label) |
| `FieldTitle` | `<div>` | Non-label title text (for FieldContent) |
| `FieldDescription` | `<p>` | Help text below the input field |
| `FieldError` | `<div role="alert">` | Error message(s), deduplicated |
| `FieldLegend` | `<legend>` | Legend for `<fieldset>` (FieldSet) |
| `FieldSet` | `<fieldset>` | Native fieldset for radio/checkbox groups |
| `FieldSeparator` | `<div>` | Horizontal separator inside a FieldGroup |

## Field

| Prop | Type | Default | Description |
|---|---|---|---|
| `orientation` | `"vertical" \| "horizontal" \| "responsive"` | `"vertical"` | Layout direction |
| `class` | `string` | - | - |

### Data Attributes (data-*)

| Attribute | Description |
|---|---|
| `data-invalid` | Marks the field as invalid (color set to destructive) |
| `data-disabled` | Marks the field as disabled (opacity-50 on label) |

### Orientation Variants

| Variant | Behavior |
|---|---|
| `vertical` (default) | Elements stacked vertically, full width |
| `horizontal` | Label left (`flex-auto`), control right (`items-center`) |
| `responsive` | Vertical by default, horizontal from `@md` (container query) |

Note: `responsive` uses the `@md/field-group` container query — a FieldGroup must be present.

## FieldError

| Prop | Type | Description |
|---|---|---|
| `errors` | `Array<string \| { message: string \| undefined } \| undefined>` | Error messages (Zod, Valibot, ArkType compatible) |
| `class` | `string` | - |

Behavior:
- No `errors` array: renders `<slot>` (manual content)
- 1 unique error: inline text
- Multiple unique errors: `<ul>` list
- Duplicates are filtered automatically

## FieldLegend

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"legend" \| "label"` | - | `legend`: text-base, `label`: text-sm |
| `class` | `string` | - | - |

## FieldLabel (Choice Card Pattern)

When FieldLabel contains a `<Field>` as a child, it renders as a "choice card":
- `w-full flex-col rounded-md border`
- `has-data-[state=checked]:bg-primary/5 border-primary` when selected

Usage: checkbox/radio inside a FieldLabel for a clickable card style.

## FieldSeparator

Optional slot for a text label in the middle of the separator line (CSS overlay technique).

```vue
<FieldSeparator>or</FieldSeparator>
```
