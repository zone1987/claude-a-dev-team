# RadioGroup — API Reference

## Composition

```text
RadioGroup
├── RadioGroupItem
└── RadioGroupItem
```

## RadioGroup

Root container managing the selection state.

| Prop             | Type                      | Default | Description                                  |
| ---------------- | ------------------------- | ------- | -------------------------------------------- |
| `defaultValue`   | `string`                  |         | Initial selected value (uncontrolled)        |
| `value`          | `string`                  |         | Controlled selected value                    |
| `onValueChange`  | `(value: string) => void` |         | Callback when selection changes              |
| `disabled`       | `boolean`                 | `false` | Disables all items in the group              |
| `required`       | `boolean`                 | `false` | Marks the group as required in forms         |
| `orientation`    | `"horizontal" \| "vertical"` | `"vertical"` | Arrow key navigation direction        |
| `className`      | `string`                  |         | Defaults to `grid gap-3`                     |

## RadioGroupItem

Individual radio button item.

| Prop          | Type      | Default | Description                              |
| ------------- | --------- | ------- | ---------------------------------------- |
| `value`       | `string`  |         | The value this item represents (required)|
| `id`          | `string`  |         | For pairing with `<Label htmlFor="...">`  |
| `disabled`    | `boolean` | `false` | Disables this individual item            |
| `aria-invalid` | `boolean \| "true"` |  | Shows destructive border/ring for validation |

### Pairing with Label

Always pair `RadioGroupItem` with a `Label` using `id`/`htmlFor`:

```tsx
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

<RadioGroup defaultValue="option-one">
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-one" id="option-one" />
    <Label htmlFor="option-one">Option One</Label>
  </div>
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-two" id="option-two" />
    <Label htmlFor="option-two">Option Two</Label>
  </div>
</RadioGroup>
```

---
Source: `content/docs/components/base/radio-group.mdx`
