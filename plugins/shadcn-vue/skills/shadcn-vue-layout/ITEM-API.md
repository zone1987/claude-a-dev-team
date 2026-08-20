# Item — API Reference

## Contents

- [Item (Root)](#item-root)
- [ItemGroup](#itemgroup)
- [ItemContent](#itemcontent)
- [ItemTitle](#itemtitle)
- [ItemDescription](#itemdescription)
- [ItemMedia](#itemmedia)
- [ItemActions](#itemactions)
- [ItemHeader](#itemheader)
- [ItemFooter](#itemfooter)
- [ItemSeparator](#itemseparator)
- [Exported Types](#exported-types)
- [reka-ui Reference](#reka-ui-reference)

## Item (Root)

Based on the reka-ui `Primitive` — polymorphic element.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | `string \| Component` | `"div"` | HTML tag or component |
| `asChild` | `boolean` | `false` | Renders as child element (slot-based) |
| `variant` | `"default" \| "outline" \| "muted"` | `"default"` | Visual style |
| `size` | `"default" \| "sm"` | `"default"` | Size/spacing |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### Slots

| Slot | Description |
|---|---|
| default | Any Item sub-components |

---

## ItemGroup

```html
<div role="list" data-slot="item-group">
```

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemContent

Flex column, grows to `flex-1`. A second `ItemContent` is automatically set to `flex-none`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemTitle

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemDescription

Renders as `<p>`. Links are underlined automatically.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemMedia

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "icon" \| "image"` | `"default"` | Layout type |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### itemMediaVariants Details

| Variant | Size | Description |
|---|---|---|
| `default` | — | No layout of its own |
| `icon` | `size-8` | Square with border + muted bg, SVG 4x4 |
| `image` | `size-10` | Square, overflow hidden, `img` fills it |

---

## ItemActions

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemHeader

Full width (`basis-full`), `justify-between`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemFooter

Full width (`basis-full`), `justify-between`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## ItemSeparator

Based on `Separator` (reka-ui), always `orientation="horizontal"`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `SeparatorProps` | — | Are forwarded |

---

## Exported Types

```ts
import type { ItemVariants, ItemMediaVariants } from "@/components/ui/item"
```

## reka-ui Reference
- https://reka-ui.com/docs/utilities/primitive
