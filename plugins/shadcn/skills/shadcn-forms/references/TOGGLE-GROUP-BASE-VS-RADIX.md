# ToggleGroup — new-york-v4 vs. Radix base

## Key differences

### 1. Default spacing

| Variant | Default `spacing` | Visual result |
|---------|-------------------|---------------|
| new-york-v4 | `0` | Items are connected (no gap, shared borders) |
| radix base | `2` | Items have a gap between them |

Use `spacing={0}` explicitly on the radix base variant for connected button groups.

### 2. Orientation support

| Variant | `orientation` prop | Vertical layout |
|---------|--------------------|-----------------|
| new-york-v4 | Not supported | No built-in vertical support |
| radix base | `"horizontal" \| "vertical"` | `data-vertical:flex-col data-vertical:items-stretch` |

The radix base variant sets `data-orientation` on the root and uses `data-vertical` / `data-horizontal` Tailwind selectors to switch between row and column layouts.

### 3. Styling approach

| Variant | Approach |
|---------|----------|
| new-york-v4 | Full Tailwind utility classes on the elements |
| radix base | Marker classes `cn-toggle-group` and `cn-toggle-group-item` used as hooks for the theme system, alongside Tailwind utilities |

### 4. Context propagation

Both variants use React Context (`ToggleGroupContext`) to propagate `variant` and `size` from the `ToggleGroup` root to each `ToggleGroupItem`, so you only set these props once on the container. The radix base additionally propagates `orientation` through context.

### 5. Connected-item border handling

Both handle the `spacing=0` + `outline` variant case (removing duplicate borders between adjacent items), but the radix base handles both horizontal and vertical directions:

- new-york-v4: removes left border and adds it back only on `:first-child` (horizontal only)
- radix base: uses `group-data-horizontal` and `group-data-vertical` selectors to handle both axis directions for borders
