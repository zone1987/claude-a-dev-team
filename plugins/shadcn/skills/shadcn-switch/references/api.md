# Switch — API Reference

## Switch

The root toggle element. Renders as a `<button role="switch">`.

### Props (new-york-v4 / Radix base)

Extends `React.ComponentProps<typeof SwitchPrimitive.Root>` plus:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `size` | `"sm" \| "default"` | `"default"` | Controls the rendered dimensions of the switch track and thumb. `default` = 1.15rem × 2rem track, 1rem thumb. `sm` = 0.875rem × 1.5rem track, 0.75rem thumb. |
| `checked` | `boolean` | — | Controlled checked state. |
| `defaultChecked` | `boolean` | — | Uncontrolled initial checked state. |
| `onCheckedChange` | `(checked: boolean) => void` | — | Callback fired when the checked state changes. |
| `disabled` | `boolean` | `false` | Prevents interaction and applies reduced opacity. |
| `required` | `boolean` | `false` | Marks the switch as required within a form. |
| `name` | `string` | — | The name of the switch when submitted with a form. |
| `value` | `string` | `"on"` | The value submitted with a form when `checked` is true. |
| `className` | `string` | — | Additional CSS classes merged via `cn`. |
| `ref` | `React.Ref<HTMLButtonElement>` | — | Forwarded ref to the underlying button element. |

### Props (Base UI variant)

Extends `SwitchPrimitive.Root.Props` plus `size?: "sm" | "default"`. The underlying prop names are identical to the Radix variant; Base UI mirrors the same surface for `checked`, `defaultChecked`, `onCheckedChange`, `disabled`, `required`, `name`, and `value`.

## Data attributes

These attributes are set by the component and can be used for CSS targeting:

| Attribute | Values | Set by |
|-----------|--------|--------|
| `data-slot="switch"` | always present | Root |
| `data-slot="switch-thumb"` | always present | Thumb |
| `data-size` | `"default"` \| `"sm"` | Root (via `size` prop) |
| `data-state` | `"checked"` \| `"unchecked"` | Root (Radix) |
| `data-disabled` | present when disabled | Root (Base UI) |

## Accessibility

- Renders as `<button role="switch" aria-checked>`.
- Keyboard: `Space` toggles the switch; `Enter` also works in most browsers.
- Associate with a `<Label>` via `htmlFor` / `id` for accessible naming.
- Use `aria-invalid` on the root to mark the field as invalid.
- Use `aria-describedby` pointing to a description element for additional context.
