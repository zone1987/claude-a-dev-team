# Field — API Reference

## Composition Trees

### Single Field

```text
Field
├── FieldLabel
├── Input / Textarea / Switch / Select / Checkbox
├── FieldDescription
└── FieldError
```

### FieldGroup

```text
FieldGroup
├── Field
│   ├── FieldLabel
│   ├── Control
│   ├── FieldDescription
│   └── FieldError
├── FieldSeparator
└── Field
    ├── FieldLabel
    └── Control
```

### FieldSet

```text
FieldSet
├── FieldLegend
├── FieldDescription
└── FieldGroup
    ├── Field ...
    └── Field ...
```

### Horizontal Field with FieldContent

```text
Field (orientation="horizontal")
├── Checkbox / Switch
└── FieldContent
    ├── FieldTitle or FieldLabel
    └── FieldDescription
```

## Basic Usage

```tsx
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
  FieldTitle,
} from "@/components/ui/field"

<FieldSet>
  <FieldLegend>Profile</FieldLegend>
  <FieldDescription>This appears on invoices and emails.</FieldDescription>
  <FieldGroup>
    <Field>
      <FieldLabel htmlFor="name">Full name</FieldLabel>
      <Input id="name" autoComplete="off" placeholder="Evil Rabbit" />
      <FieldDescription>This appears on invoices and emails.</FieldDescription>
    </Field>
    <Field>
      <FieldLabel htmlFor="username">Username</FieldLabel>
      <Input id="username" autoComplete="off" aria-invalid />
      <FieldError>Choose another username.</FieldError>
    </Field>
    <Field orientation="horizontal">
      <Switch id="newsletter" />
      <FieldLabel htmlFor="newsletter">Subscribe to the newsletter</FieldLabel>
    </Field>
  </FieldGroup>
</FieldSet>
```

## Sub-component Props

### FieldSet

Renders a semantic `<fieldset>`.

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | –       | Additional CSS classes |

### FieldLegend

Legend element for `FieldSet`.

| Prop        | Type                    | Default    | Description                              |
| ----------- | ----------------------- | ---------- | ---------------------------------------- |
| `variant`   | `"legend" \| "label"` | `"legend"` | `label` applies `text-sm` label sizing   |
| `className` | `string`                | –          | Additional CSS classes                   |

### FieldGroup

Layout wrapper. Enables `@container/field-group` container queries for responsive orientation.

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | –       | Additional CSS classes |

### Field

Core wrapper for a single control. Renders `role="group"`.

| Prop            | Type                                           | Default      | Description                                |
| --------------- | ---------------------------------------------- | ------------ | ------------------------------------------ |
| `orientation`   | `"vertical" \| "horizontal" \| "responsive"`  | `"vertical"` | Layout direction                           |
| `data-invalid`  | `boolean`                                      | –            | Switches entire block into error state     |
| `className`     | `string`                                       | –            | Additional CSS classes                     |

### FieldContent

Flex column grouping control and descriptions (use when label sits beside the control).

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | –       | Additional CSS classes |

### FieldLabel

Styled `Label` with support for nested `Field` children (choice card pattern).

| Prop        | Type      | Default | Description            |
| ----------- | --------- | ------- | ---------------------- |
| `asChild`   | `boolean` | `false` | Render as child        |
| `className` | `string`  | –       | Additional CSS classes |

### FieldTitle

Title inside `FieldContent` with label styling (use instead of `FieldLabel` when no `htmlFor` needed).

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | –       | Additional CSS classes |

### FieldDescription

Muted helper text. Auto-balances in horizontal fields.

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | –       | Additional CSS classes |

### FieldSeparator

Visual divider between `FieldGroup` sections. Accepts optional inline text.

| Prop        | Type        | Default | Description                       |
| ----------- | ----------- | ------- | --------------------------------- |
| `children`  | `ReactNode` | –       | Optional centered label text      |
| `className` | `string`    | –       | Additional CSS classes            |

```tsx
<FieldSeparator>Or continue with</FieldSeparator>
```

### FieldError

Accessible error message. Renders `role="alert"` and nothing when empty.

| Prop        | Type                                        | Default | Description                                         |
| ----------- | ------------------------------------------- | ------- | --------------------------------------------------- |
| `errors`    | `Array<{ message?: string } \| undefined>` | –       | Array from react-hook-form or Standard Schema       |
| `children`  | `ReactNode`                                 | –       | Manual error message (takes precedence over errors) |
| `className` | `string`                                    | –       | Additional CSS classes                              |

Multiple errors render as a `<ul>` list automatically. Deduplicates by message.

## Validation Pattern

```tsx
{/* Set data-invalid on Field to style all children */}
<Field data-invalid>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  {/* Add aria-invalid on the input for a11y */}
  <Input id="email" type="email" aria-invalid />
  <FieldError>Enter a valid email address.</FieldError>
</Field>
```

## Responsive Orientation

Set `orientation="responsive"` on `Field` — vertical on small, horizontal on `@md` breakpoint (requires `@container/field-group` on `FieldGroup`).

```tsx
<FieldGroup className="@container/field-group">
  <Field orientation="responsive">
    <FieldLabel htmlFor="name">Name</FieldLabel>
    <Input id="name" />
  </Field>
</FieldGroup>
```

## Accessibility

- `FieldSet` + `FieldLegend` semantically group related controls.
- `Field` outputs `role="group"` — nested controls inherit labeling.
- `FieldError` uses `role="alert"` for screen readers.
- Apply `aria-invalid` on the input and `data-invalid` on `Field` together.

---

_Source: `apps/v4/content/docs/components/base/field.mdx`, `apps/v4/registry/new-york-v4/ui/field.tsx`_
