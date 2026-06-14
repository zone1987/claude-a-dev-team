# Resizable — Installation

## CLI (recommended)

```bash
npx shadcn@latest add resizable
```

## Manual

### 1. Install dependency

```bash
npm install react-resizable-panels
```

### 2. Copy component

Create `components/ui/resizable.tsx` with the source from [source.md](source.md).

### 3. Update import paths

Replace `@/lib/utils` with your project's `cn` utility path.

## Usage

```tsx
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
```

```tsx
<ResizablePanelGroup orientation="horizontal">
  <ResizablePanel>One</ResizablePanel>
  <ResizableHandle />
  <ResizablePanel>Two</ResizablePanel>
</ResizablePanelGroup>
```

## Composition

```text
ResizablePanelGroup
├── ResizablePanel
├── ResizableHandle
└── ResizablePanel
```

## Changelog

### 2025-02-02 — react-resizable-panels v4

| v3 API                       | v4 API                  |
| ---------------------------- | ----------------------- |
| `PanelGroup`                 | `Group`                 |
| `PanelResizeHandle`          | `Separator`             |
| `direction` prop             | `orientation` prop      |
| `defaultSize={50}`           | `defaultSize="50%"`     |
| `onLayout`                   | `onLayoutChange`        |
| `ImperativePanelHandle`      | `PanelImperativeHandle` |
| `ref` prop on Panel          | `panelRef` prop         |
| `data-panel-group-direction` | `aria-orientation`      |

The shadcn/ui wrapper components (`ResizablePanelGroup`, `ResizablePanel`, `ResizableHandle`) remain unchanged.

## Source files

- `content/docs/components/base/resizable.mdx`
- `content/docs/components/radix/resizable.mdx`
