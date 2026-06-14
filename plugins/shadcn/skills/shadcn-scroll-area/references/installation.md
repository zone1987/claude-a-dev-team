# Scroll Area — Installation

## CLI (recommended)

```bash
npx shadcn@latest add scroll-area
```

## Manual (Radix variant)

### 1. Install dependency

```bash
npm install radix-ui
```

### 2. Copy component

Create `components/ui/scroll-area.tsx` with the source from [source.md](source.md).

### 3. Update import paths

Replace `@/lib/utils` with your project's `cn` utility path.

## Manual (Base UI variant)

### 1. Install dependency

```bash
npm install @base-ui/react
```

### 2. Use base variant source from [source.md](source.md).

## Usage

```tsx
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
```

```tsx
<ScrollArea className="h-[200px] w-[350px] rounded-md border p-4">
  Your scrollable content here.
</ScrollArea>
```

## Composition

```text
ScrollArea
└── ScrollBar
```

Note: `ScrollBar` is auto-rendered inside `ScrollArea` for vertical.
Add an explicit `<ScrollBar orientation="horizontal" />` for horizontal scrolling.

## API Reference

- Radix: https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference
- Base UI: https://base-ui.com/react/components/scroll-area#api-reference

## Source files

- `content/docs/components/base/scroll-area.mdx`
- `content/docs/components/radix/scroll-area.mdx`
