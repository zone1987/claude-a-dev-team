# Checkbox — API

The `Checkbox` component wraps reka-ui `CheckboxRoot` and forwards all props and emits transparently.

## Props

All `CheckboxRootProps` from reka-ui are accepted, plus:

| Prop             | Type                              | Default     | Description                                                  |
| ---------------- | --------------------------------- | ----------- | ------------------------------------------------------------ |
| `checked`        | `boolean \| 'indeterminate'`      | —           | Controlled checked state                                     |
| `defaultChecked` | `boolean`                         | `false`     | Initial checked state (uncontrolled)                         |
| `disabled`       | `boolean`                         | `false`     | Prevents interaction and applies reduced opacity             |
| `required`       | `boolean`                         | `false`     | Marks the checkbox as required in a form context             |
| `name`           | `string`                          | —           | Name submitted with the form                                 |
| `value`          | `string`                          | `'on'`      | Value submitted with the form when checked                   |
| `id`             | `string`                          | —           | HTML id for pairing with a `<label>`                         |
| `class`          | `HTMLAttributes['class']`         | —           | Additional CSS classes merged via `cn()`                     |

## Emits

| Event            | Payload                           | Description                                    |
| ---------------- | --------------------------------- | ---------------------------------------------- |
| `update:checked` | `boolean \| 'indeterminate'`      | Fired when the checked state changes           |

## Slots

| Slot      | Slot props   | Description                                                           |
| --------- | ------------ | --------------------------------------------------------------------- |
| `default` | `slotProps`  | Custom indicator content; defaults to a `<Check class="size-3.5" />` |

## v-model

```vue
<Checkbox v-model:checked="myValue" />
```

## Full reka-ui API reference

https://reka-ui.com/docs/components/checkbox#api-reference
