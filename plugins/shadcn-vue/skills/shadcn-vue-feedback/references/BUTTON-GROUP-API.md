# ButtonGroup — API Reference

## ButtonGroup Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Layout direction. Horizontal merges left/right borders; vertical merges top/bottom borders. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes merged via `cn()`. |

### Rendered attributes

| Attribute | Value |
|---|---|
| `role` | `"group"` |
| `data-slot` | `"button-group"` |
| `data-orientation` | The current `orientation` value |

---

## ButtonGroupSeparator Props

Extends all `SeparatorProps` from `reka-ui`.

| Prop | Type | Default | Description |
|---|---|---|---|
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` | Direction of the separator line. Use `"horizontal"` inside a vertical `ButtonGroup`. |
| `decorative` | `boolean` | `false` | When `true`, the separator is purely visual and hidden from the accessibility tree. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |

### Rendered attributes

| Attribute | Value |
|---|---|
| `data-slot` | `"button-group-separator"` |
| `data-orientation` | The current `orientation` value |

---

## ButtonGroupText Props

Extends `PrimitiveProps` from `reka-ui` (supports `as` and `asChild`).

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | `string \| Component` | `"div"` | HTML element or Vue component to render as. |
| `asChild` | `boolean` | `false` | Merges props/styles onto the direct child element instead of rendering a wrapper. |
| `orientation` | `"horizontal" \| "vertical"` | — | Forwarded as `data-orientation` for CSS targeting. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |

### Common use case: as Label

```vue
<ButtonGroupText as-child>
  <label for="my-input">Prefix</label>
</ButtonGroupText>
```

---

## buttonGroupVariants (CVA)

```ts
buttonGroupVariants({ orientation?: "horizontal" | "vertical" }): string
```

| Variant key | Values | Default |
|---|---|---|
| `orientation` | `"horizontal"`, `"vertical"` | `"horizontal"` |

### Base classes applied to all orientations

| Class | Effect |
|---|---|
| `flex w-fit items-stretch` | Flex container, shrinks to content width, children stretch to equal height |
| `[&>*]:focus-visible:z-10` | Focused child floats above siblings (prevents border overlap hiding focus ring) |
| `[&>*]:focus-visible:relative` | Enables `z-index` on focused child |
| `has-[>[data-slot=button-group]]:gap-2` | Adds gap between nested `ButtonGroup` children |
| `[&>input]:flex-1` | Inputs inside the group expand to fill available space |

### Horizontal-specific classes

| Class | Effect |
|---|---|
| `[&>*:not(:first-child)]:rounded-l-none` | Removes left radius from all but first child |
| `[&>*:not(:first-child)]:border-l-0` | Collapses duplicate left border |
| `[&>*:not(:last-child)]:rounded-r-none` | Removes right radius from all but last child |

### Vertical-specific classes

| Class | Effect |
|---|---|
| `flex-col` | Stacks children vertically |
| `[&>*:not(:first-child)]:rounded-t-none` | Removes top radius from all but first child |
| `[&>*:not(:first-child)]:border-t-0` | Collapses duplicate top border |
| `[&>*:not(:last-child)]:rounded-b-none` | Removes bottom radius from all but last child |
