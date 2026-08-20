# ScrollArea — API

## ScrollArea

Wraps `ScrollAreaRoot` + `ScrollAreaViewport` + `ScrollBar` + `ScrollAreaCorner`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| class | `HTMLAttributes["class"]` | — | Additional CSS classes applied to the root element |
| type | `"auto" \| "always" \| "scroll" \| "hover"` | `"hover"` | Controls when the scrollbar is visible |
| dir | `"ltr" \| "rtl"` | — | Reading direction |
| scrollHideDelay | `number` | `600` | Delay in ms before scrollbar hides (only when `type` is `"scroll"` or `"hover"`) |

All other `ScrollAreaRootProps` from reka-ui are forwarded via `v-bind`.

## ScrollBar

Wraps `ScrollAreaScrollbar` + `ScrollAreaThumb`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| orientation | `"vertical" \| "horizontal"` | `"vertical"` | Scrollbar orientation |
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |
| forceMount | `boolean` | — | Force mount the scrollbar regardless of scroll state |

All other `ScrollAreaScrollbarProps` from reka-ui are forwarded via `v-bind`.

## Usage Notes

- For horizontal scroll, add `<ScrollBar orientation="horizontal" />` explicitly inside `<ScrollArea>` or use it standalone
- The default `<ScrollBar />` inside `ScrollArea.vue` is always vertical; override by placing your own `<ScrollBar orientation="horizontal" />` in the default slot
- `ScrollAreaCorner` is rendered automatically to fill the corner when both scrollbars are visible

## reka-ui API Reference

https://reka-ui.com/docs/components/scroll-area#api-reference
