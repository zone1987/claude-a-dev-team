# Slider — Installation

## CLI (recommended)

```bash
npx shadcn@latest add slider
```

## Manual (Radix variant)

### 1. Install dependency

```bash
npm install radix-ui
```

### 2. Copy component source from [source.md](source.md).

## Manual (Base UI variant)

### 1. Install dependency

```bash
npm install @base-ui/react
```

### 2. Use base variant source from [source.md](source.md).

## Usage

```tsx
import { Slider } from "@/components/ui/slider"
```

```tsx
<Slider defaultValue={[33]} max={100} step={1} />
```

## Single value vs range

```tsx
{/* Single thumb */}
<Slider defaultValue={[50]} />

{/* Range (two thumbs) */}
<Slider defaultValue={[20, 80]} />

{/* Multiple thumbs */}
<Slider defaultValue={[10, 50, 90]} />
```

## Vertical

```tsx
<Slider orientation="vertical" defaultValue={[50]} className="h-48" />
```

## API Reference

- Radix: https://www.radix-ui.com/docs/primitives/components/slider#api-reference
- Base UI: https://base-ui.com/react/components/slider#api-reference

## Source files

- `content/docs/components/base/slider.mdx`
- `content/docs/components/radix/slider.mdx`
