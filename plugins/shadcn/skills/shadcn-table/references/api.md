# Table — API Reference

All sub-components forward their props to the underlying native HTML element and accept an optional `className` for Tailwind overrides. There are no custom props beyond the standard HTML element props.

---

## Table

Wraps the native `<table>` element inside a scrollable `<div>` container.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Applied to the inner `<table>` element. |
| `...props` | `React.ComponentProps<"table">` | — | All native `<table>` attributes (e.g. `id`, `aria-*`). |

**Note**: The outer `<div>` has `relative w-full overflow-x-auto` and carries `data-slot="table-container"`. It is not directly customizable via props — use a wrapping element if you need to style the container.

---

## TableHeader

Wraps `<thead>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with `[&_tr]:border-b`. |
| `...props` | `React.ComponentProps<"thead">` | — | All native `<thead>` attributes. |

---

## TableBody

Wraps `<tbody>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with `[&_tr:last-child]:border-0`. |
| `...props` | `React.ComponentProps<"tbody">` | — | All native `<tbody>` attributes. |

---

## TableFooter

Wraps `<tfoot>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with `border-t bg-muted/50 font-medium [&>tr]:last:border-b-0`. |
| `...props` | `React.ComponentProps<"tfoot">` | — | All native `<tfoot>` attributes. |

---

## TableRow

Wraps `<tr>`. Supports a selected state via `data-[state=selected]`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with hover and selected state styles. |
| `data-state` | `"selected"` \| `undefined` | — | When set to `"selected"`, applies `bg-muted` background. |
| `...props` | `React.ComponentProps<"tr">` | — | All native `<tr>` attributes. |

---

## TableHead

Wraps `<th>`. Used inside `<TableHeader>` rows to render column headings.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with `h-10 px-2 text-left align-middle font-medium whitespace-nowrap text-foreground`. |
| `...props` | `React.ComponentProps<"th">` | — | All native `<th>` attributes including `colSpan`, `scope`, `aria-sort`. |

---

## TableCell

Wraps `<td>`. Used inside `<TableBody>` rows for data cells.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with `p-2 align-middle whitespace-nowrap`. |
| `...props` | `React.ComponentProps<"td">` | — | All native `<td>` attributes including `colSpan`, `rowSpan`. |

---

## TableCaption

Wraps `<caption>`. Renders below the table (via `caption-bottom` on `<Table>`).

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Merged with `mt-4 text-sm text-muted-foreground`. |
| `...props` | `React.ComponentProps<"caption">` | — | All native `<caption>` attributes. |

---

## data-slot attributes

Each sub-component sets a `data-slot` attribute for styling hooks:

| Component | `data-slot` value |
|-----------|-------------------|
| Outer `<div>` | `table-container` |
| `Table` (`<table>`) | `table` |
| `TableHeader` | `table-header` |
| `TableBody` | `table-body` |
| `TableFooter` | `table-footer` |
| `TableRow` | `table-row` |
| `TableHead` | `table-head` |
| `TableCell` | `table-cell` |
| `TableCaption` | `table-caption` |
