# API Reference

Full reka-ui API reference: https://reka-ui.com/docs/components/splitter#api-reference

---

## ResizablePanelGroup

Wraps reka-ui's `SplitterGroup`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `"horizontal" \| "vertical"` | required | Orientation of the panel group. |
| `keyboardResizeBy` | `number` | `10` | Percentage to resize by when using keyboard arrow keys. |
| `storage` | `PanelGroupStorage` | — | Custom storage implementation for persisting layout (e.g. `localStorage`). |
| `autoSaveId` | `string` | — | Key used together with `storage` to persist and restore panel sizes. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Defaults include `flex h-full w-full` and `data-[orientation=vertical]:flex-col`. |

**Emits**

| Event | Payload | Description |
|-------|---------|-------------|
| `layout` | `number[]` | Fired whenever the panel sizes change. Each number is a percentage (0–100). |

---

## ResizablePanel

Wraps reka-ui's `SplitterPanel`. Exposes the underlying panel element ref via `useForwardExpose` for programmatic control (e.g. calling `collapse()` / `expand()` / `resize()`).

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultSize` | `number` | — | Initial size as a percentage of the group. |
| `minSize` | `number` | `0` | Minimum allowed size as a percentage. |
| `maxSize` | `number` | `100` | Maximum allowed size as a percentage. |
| `collapsible` | `boolean` | `false` | Whether the panel can be collapsed to `collapsedSize`. |
| `collapsedSize` | `number` | `0` | Size (percentage) when collapsed. Only relevant when `collapsible` is `true`. |
| `id` | `string` | — | Explicit panel ID. Used by `autoSaveId` storage and for imperative access. |
| `order` | `number` | — | Explicit render order within the group (useful for SSR). |
| `onCollapse` | `() => void` | — | Callback fired when the panel collapses. |
| `onExpand` | `() => void` | — | Callback fired when the panel expands from a collapsed state. |
| `onResize` | `(size: number) => void` | — | Callback fired on every resize with the new size percentage. |

---

## ResizableHandle

Wraps reka-ui's `SplitterResizeHandle`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `withHandle` | `boolean` | `false` | When `true`, renders a visible grip bar with a `GripVertical` icon centred on the handle. |
| `disabled` | `boolean` | `false` | Disables drag and keyboard resize for this handle. |
| `id` | `string` | — | Explicit handle ID. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes on the handle element. |

**Emits**

| Event | Payload | Description |
|-------|---------|-------------|
| `dragging` | `boolean` | Fired when dragging starts (`true`) and stops (`false`). |

**Data attributes set by reka-ui**

| Attribute | Description |
|-----------|-------------|
| `data-orientation` | `"horizontal"` or `"vertical"`, inherited from the parent group. |
| `data-resize-handle-active` | Present while the handle is being dragged. |
| `data-resize-handle-enabled` | Present when the handle is not disabled. |

**Keyboard interaction**

When the handle is focused, the following keys resize the adjacent panels:

| Key | Behaviour |
|-----|-----------|
| `ArrowLeft` / `ArrowUp` | Decrease size by `keyboardResizeBy` percent. |
| `ArrowRight` / `ArrowDown` | Increase size by `keyboardResizeBy` percent. |
| `Home` | Collapse the panel to its minimum size. |
| `End` | Expand the panel to its maximum size. |
| `Enter` | Toggle collapse/expand (only when `collapsible` is `true`). |
