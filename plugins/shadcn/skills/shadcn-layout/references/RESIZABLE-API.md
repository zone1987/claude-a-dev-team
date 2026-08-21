# Resizable — API Reference

Full API: https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels

## ResizablePanelGroup

Wraps `react-resizable-panels` `Group`. Accepts all `GroupProps`.

| Prop              | Type                          | Default        | Description                                |
| ----------------- | ----------------------------- | -------------- | ------------------------------------------ |
| `orientation`     | `"horizontal" \| "vertical"`  | `"horizontal"` | Layout direction of the panels             |
| `className`       | `string`                      | —              | Additional CSS classes                     |
| `onLayoutChange`  | `(sizes: number[]) => void`   | —              | Callback when panel sizes change           |
| `storage`         | `PanelGroupStorage`           | cookie         | Custom storage for persisting layout       |
| `autoSaveId`      | `string`                      | —              | Key to auto-save layout to storage         |

`data-slot="resizable-panel-group"`

## ResizablePanel

Wraps `react-resizable-panels` `Panel`. Accepts all `PanelProps`.

| Prop              | Type                             | Default | Description                                 |
| ----------------- | -------------------------------- | ------- | ------------------------------------------- |
| `defaultSize`     | `string` (e.g. `"50%"`)         | —       | Initial size as percentage string (v4)      |
| `minSize`         | `string` (e.g. `"10%"`)         | —       | Minimum panel size                          |
| `maxSize`         | `string` (e.g. `"90%"`)         | —       | Maximum panel size                          |
| `collapsible`     | `boolean`                        | `false` | Whether panel can be collapsed              |
| `collapsedSize`   | `string`                         | —       | Size when collapsed                         |
| `onCollapse`      | `() => void`                     | —       | Called when panel collapses                 |
| `onExpand`        | `() => void`                     | —       | Called when panel expands                   |
| `panelRef`        | `React.Ref<PanelImperativeHandle>` | —     | Imperative handle ref (v4 replaces `ref`)   |

`data-slot="resizable-panel"`

## ResizableHandle

Wraps `react-resizable-panels` `Separator`. Accepts all `SeparatorProps` plus:

| Prop         | Type      | Default | Description                                      |
| ------------ | --------- | ------- | ------------------------------------------------ |
| `withHandle` | `boolean` | `false` | Show a visible grip icon on the handle           |
| `className`  | `string`  | —       | Additional CSS classes                           |

`data-slot="resizable-handle"`

## Keyboard Support

| Key             | Action                            |
| --------------- | --------------------------------- |
| `ArrowLeft`     | Resize panel (horizontal)         |
| `ArrowRight`    | Resize panel (horizontal)         |
| `ArrowUp`       | Resize panel (vertical)           |
| `ArrowDown`     | Resize panel (vertical)           |
| `Home`          | Collapse panel to min size        |
| `End`           | Expand panel to max size          |

## Source files

- `registry/new-york-v4/ui/resizable.tsx`
