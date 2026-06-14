# Combobox — API Reference

## Composition Patterns

### Simple (single select)

```text
Combobox
├── ComboboxInput
└── ComboboxContent
    ├── ComboboxEmpty
    └── ComboboxList
        ├── ComboboxItem
        └── ComboboxItem
```

### With chips (multi-select)

```text
Combobox
├── ComboboxChips
│   ├── ComboboxValue
│   │   └── ComboboxChip
│   └── ComboboxChipsInput
└── ComboboxContent
    ├── ComboboxEmpty
    └── ComboboxList
        ├── ComboboxItem
        └── ComboboxItem
```

### With groups

```text
Combobox
├── ComboboxInput
└── ComboboxContent
    ├── ComboboxEmpty
    └── ComboboxList
        ├── ComboboxGroup
        │   ├── ComboboxLabel
        │   └── ComboboxCollection
        │       ├── ComboboxItem
        │       └── ComboboxItem
        ├── ComboboxSeparator
        └── ComboboxGroup
            ├── ComboboxLabel
            └── ComboboxCollection
                ├── ComboboxItem
                └── ComboboxItem
```

## Core Usage

```tsx
import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"

const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

export function ExampleCombobox() {
  return (
    <Combobox items={frameworks}>
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(item) => (
            <ComboboxItem key={item} value={item}>
              {item}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Sub-Component Props

### Combobox (Root)

Direct re-export of `ComboboxPrimitive.Root` from `@base-ui/react`.

| Prop                  | Type                          | Default | Description                                        |
| --------------------- | ----------------------------- | ------- | -------------------------------------------------- |
| `items`               | `T[]`                         | required | Data array to populate the list                  |
| `itemToStringValue`   | `(item: T) => string`         | -       | Required when items are objects (not strings)      |
| `multiple`            | `boolean`                     | `false` | Enable multi-selection                             |
| `value`               | `T \| T[]`                    | -       | Controlled selected value                          |
| `defaultValue`        | `T \| T[]`                    | -       | Uncontrolled initial value                         |
| `onValueChange`       | `(value: T \| T[]) => void`   | -       | Callback on value change                           |
| `disabled`            | `boolean`                     | `false` | Disable the combobox                               |
| `autoHighlight`       | `boolean`                     | `false` | Auto-highlight first item on filter                |

### ComboboxInput

Text input with optional trigger/clear addons.

| Prop          | Type      | Default | Description                         |
| ------------- | --------- | ------- | ----------------------------------- |
| `placeholder` | `string`  | -       | Input placeholder text              |
| `showTrigger` | `boolean` | `true`  | Show the chevron trigger button     |
| `showClear`   | `boolean` | `false` | Show the clear (X) button           |
| `disabled`    | `boolean` | `false` | Disable the input                   |
| `className`   | `string`  | -       |                                     |

### ComboboxContent

The dropdown popup. Wraps `ComboboxPrimitive.Positioner` + `ComboboxPrimitive.Popup`.

| Prop          | Type     | Default    | Description                             |
| ------------- | -------- | ---------- | --------------------------------------- |
| `side`        | string   | `"bottom"` | Popup side relative to trigger          |
| `sideOffset`  | number   | `6`        | Distance from trigger                   |
| `align`       | string   | `"start"`  | Popup alignment                         |
| `alignOffset` | number   | `0`        | Alignment offset                        |
| `anchor`      | any      | -          | Custom anchor (for chips input mode)    |
| `className`   | `string` | -          |                                         |

### ComboboxList

Scrollable list of items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### ComboboxItem

A single selectable item. Shows a checkmark when selected.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `value`     | `T`      | required |
| `disabled`  | `boolean`| `false` |
| `className` | `string` | -       |

### ComboboxEmpty

Shown when the filtered list is empty.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### ComboboxGroup / ComboboxLabel / ComboboxCollection / ComboboxSeparator

For grouped lists. Wrap items in `ComboboxGroup`, add a `ComboboxLabel`, use `ComboboxCollection` with the data array render prop, separate groups with `ComboboxSeparator`.

### ComboboxChips / ComboboxChip / ComboboxChipsInput / ComboboxValue

For multi-select with chip display:
- `ComboboxChips` — container replacing `ComboboxInput` for multi-select
- `ComboboxValue` — renders the array of selected chip values
- `ComboboxChip` — individual selected item chip (shows remove button by default)
- `ComboboxChipsInput` — the text input inside chips container

| Prop         | Type      | Default | Description                          |
| ------------ | --------- | ------- | ------------------------------------ |
| `showRemove` | `boolean` | `true`  | (`ComboboxChip`) Show remove button  |

### useComboboxAnchor

```ts
import { useComboboxAnchor } from "@/components/ui/combobox"
const anchor = useComboboxAnchor()
```

Returns a `ref` to attach to a `ComboboxChips` container; pass it to `ComboboxContent anchor={anchor}` so the popup anchors to the chips container.

## Custom Items (Object Arrays)

```tsx
type Framework = { label: string; value: string }

const frameworks: Framework[] = [
  { label: "Next.js", value: "next" },
  { label: "SvelteKit", value: "sveltekit" },
]

<Combobox
  items={frameworks}
  itemToStringValue={(framework) => framework.label}
>
  <ComboboxInput placeholder="Select a framework" />
  <ComboboxContent>
    <ComboboxEmpty>No items found.</ComboboxEmpty>
    <ComboboxList>
      {(framework) => (
        <ComboboxItem key={framework.value} value={framework}>
          {framework.label}
        </ComboboxItem>
      )}
    </ComboboxList>
  </ComboboxContent>
</Combobox>
```

## Multi-Select with Chips

```tsx
const [value, setValue] = React.useState<string[]>([])

<Combobox items={frameworks} multiple value={value} onValueChange={setValue}>
  <ComboboxChips>
    <ComboboxValue>
      {value.map((item) => (
        <ComboboxChip key={item}>{item}</ComboboxChip>
      ))}
    </ComboboxValue>
    <ComboboxChipsInput placeholder="Add framework" />
  </ComboboxChips>
  <ComboboxContent>
    <ComboboxEmpty>No items found.</ComboboxEmpty>
    <ComboboxList>
      {(item) => (
        <ComboboxItem key={item} value={item}>
          {item}
        </ComboboxItem>
      )}
    </ComboboxList>
  </ComboboxContent>
</Combobox>
```

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/combobox.mdx`_
