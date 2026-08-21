# Label — API reference

## Label

Based on reka-ui `Label`.

### Props

| Prop | Type | Description |
|---|---|---|
| `htmlFor` | `string` | ID of the associated form element |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `LabelProps` from reka-ui | — | Fully forwarded via `reactiveOmit` |

### Slots

| Slot | Description |
|---|---|
| default | Label text or combined content (text + icon) |

### Automatic disabled styles

| Selector | Effect |
|---|---|
| `group-data-[disabled=true]` | `pointer-events-none opacity-50` |
| `peer-disabled` | `cursor-not-allowed opacity-50` |

### data-slot
`data-slot="label"` is set automatically.

## reka-ui reference
- https://reka-ui.com/docs/utilities/label
