# shadcn-vue Resizable

The Resizable component provides resizable panel groups and layouts with full keyboard support. It is built on top of reka-ui's Splitter primitives (`SplitterGroup`, `SplitterPanel`, `SplitterResizeHandle`) and styled with Tailwind v4 utility classes.

## Architecture

The component consists of 3 sub-components:

- **ResizablePanelGroup** — wraps `SplitterGroup`; requires a `direction` prop (`"horizontal"` or `"vertical"`); applies `flex h-full w-full` and flips to `flex-col` for vertical orientation via the `data-[orientation=vertical]` selector
- **ResizablePanel** — wraps `SplitterPanel`; forwards all splitter panel props (size constraints, collapse behaviour) and exposes the panel ref via `useForwardExpose` for programmatic control
- **ResizableHandle** — wraps `SplitterResizeHandle`; renders a 1 px divider line with a wider invisible hit area (`after:w-1`); accepts a `withHandle` boolean prop that shows a visible grip bar containing a `GripVertical` Lucide icon; rotates 90 degrees automatically for vertical orientation via `[&[data-orientation=vertical]>div]:rotate-90`

## Keyboard Support

reka-ui's splitter handles keyboard interaction out of the box: arrow keys resize panels, `Home`/`End` jump to minimum/maximum size, and `Enter` toggles collapse when the panel is collapsible.

## Controlled Layout

Listen to the `@layout` event on `ResizablePanelGroup` to receive an array of panel sizes as percentages whenever the layout changes.

## References

- Source code: `RESIZABLE-SOURCE.md`
- API documentation: `RESIZABLE-API.md`
- Usage examples: `RESIZABLE-EXAMPLES.md`
- Installation: `RESIZABLE-INSTALLATION.md`
