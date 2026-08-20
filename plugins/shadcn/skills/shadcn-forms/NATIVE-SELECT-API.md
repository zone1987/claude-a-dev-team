# NativeSelect — API Reference

## Composition

### Simple

```text
NativeSelect
├── NativeSelectOption
├── NativeSelectOption
└── NativeSelectOption
```

### With groups

```text
NativeSelect
├── NativeSelectOptGroup
│   ├── NativeSelectOption
│   └── NativeSelectOption
└── NativeSelectOptGroup
    ├── NativeSelectOption
    └── NativeSelectOption
```

## NativeSelect

Wraps the native `<select>` in a relative container that adds a `ChevronDownIcon` and handles disabled state opacity.

| Prop       | Type                   | Default     | Description              |
| ---------- | ---------------------- | ----------- | ------------------------ |
| `size`     | `"default" \| "sm"`    | `"default"` | Height: 36px or 32px     |
| `disabled` | `boolean`              | `false`     | Disables and grays out   |
| `aria-invalid` | `boolean \| "true"` |             | Shows destructive border |

Inherits all native `<select>` props except `size` (overridden).

### Validation

Use `aria-invalid="true"` to trigger the destructive border/ring state:

```tsx
<NativeSelect aria-invalid="true">
  ...
</NativeSelect>
```

## NativeSelectOption

Thin wrapper around `<option>` with `bg-[Canvas] text-[CanvasText]` for cross-browser color consistency.

| Prop       | Type      | Default | Description       |
| ---------- | --------- | ------- | ----------------- |
| `value`    | `string`  |         | Option value      |
| `disabled` | `boolean` | `false` | Disables option   |

## NativeSelectOptGroup

Thin wrapper around `<optgroup>` for grouping options.

| Prop       | Type      | Default | Description         |
| ---------- | --------- | ------- | ------------------- |
| `label`    | `string`  |         | Group heading label |
| `disabled` | `boolean` | `false` | Disables all options in group |

## NativeSelect vs Select

| Feature               | NativeSelect        | Select (Radix)         |
| --------------------- | ------------------- | ---------------------- |
| Browser native UI     | Yes                 | No                     |
| Mobile optimized      | Yes                 | No                     |
| Custom animations     | No                  | Yes                    |
| Complex interactions  | Limited             | Full                   |
| Performance           | Better              | Heavier                |
| Accessibility         | Native              | WAI-ARIA compliant     |

---
Source: `content/docs/components/base/native-select.mdx`
