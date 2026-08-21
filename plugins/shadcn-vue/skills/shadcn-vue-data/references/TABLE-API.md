# API Reference

## Sub-components

| Component | HTML Element | Description |
|-----------|-------------|-------------|
| `Table` | `<div> + <table>` | Scrollable container + table root |
| `TableHeader` | `<thead>` | Table header section |
| `TableBody` | `<tbody>` | Table body section |
| `TableFooter` | `<tfoot>` | Table footer section |
| `TableRow` | `<tr>` | Table row |
| `TableHead` | `<th>` | Header cell |
| `TableCell` | `<td>` | Data cell |
| `TableCaption` | `<caption>` | Table caption (below table) |
| `TableEmpty` | `<tr> + <td>` | Empty state row spanning all columns |

## Props (all components)

All components accept:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional Tailwind CSS classes |

### TableEmpty Additional Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `colspan` | `number` | `1` | Spans across N columns |

### TableRow Data Attributes

| Attribute | Values | Description |
|-----------|--------|-------------|
| `data-state` | `selected` | Row is selected (e.g. with checkbox) |

## valueUpdater Utility (utils.ts)

Helper for TanStack Table integration:

```ts
import { valueUpdater } from "@/components/ui/table/utils"

// Usage in TanStack Table column state handler:
function setSorting(updaterOrValue) {
  valueUpdater(updaterOrValue, sorting)
}
```

## Slots

All components expose a default `<slot />`.
