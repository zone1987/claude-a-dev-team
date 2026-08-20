# NativeSelect — API reference

## NativeSelect

Renders a native `<select>` with a chevron icon wrapper.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `AcceptableValue \| AcceptableValue[]` | `""` | v-model value |
| `class` | `HTMLAttributes["class"]` | — | Applied to `<select>` |
| All native `<select>` attrs | — | Forwarded via `$attrs` |

### Emits

| Event | Type | Description |
|---|---|---|
| `update:modelValue` | `AcceptableValue` | Fires on change |

### Slots

| Slot | Description |
|---|---|
| default | `NativeSelectOption` and `NativeSelectOptGroup` |

### Notable details
- `inheritAttrs: false` — attrs are forwarded to `<select>` manually
- `useVModel` with `passive: true` and `defaultValue: ""`
- Wrapper div: `has-[select:disabled]:opacity-50`
- The chevron icon is `pointer-events-none` and `aria-hidden`

---

## NativeSelectOptGroup

Renders `<optgroup>`.

### Props

| Prop | Type | Description |
|---|---|---|
| `label` | `string` | Group label (native HTML attr) |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## NativeSelectOption

Renders `<option>`.

### Props

| Prop | Type | Description |
|---|---|---|
| `value` | `string` | Option value |
| `disabled` | `boolean` | Disabled |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## Note
`NativeSelect` has no reka-ui base and uses no custom dropdown logic. The dropdown behavior comes entirely from the browser.
