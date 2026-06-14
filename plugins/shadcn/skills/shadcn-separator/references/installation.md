# Separator — Installation

## CLI (recommended)

```bash
npx shadcn@latest add separator
```

## Manual (Radix variant)

### 1. Install dependency

```bash
npm install radix-ui
```

### 2. Copy component

Create `components/ui/separator.tsx` with the source from [source.md](source.md).

## Manual (Base UI variant)

### 1. Install dependency

```bash
npm install @base-ui/react
```

### 2. Use base variant source from [source.md](source.md).

## Usage

```tsx
import { Separator } from "@/components/ui/separator"
```

```tsx
<Separator />
```

```tsx
<Separator orientation="vertical" />
```

## API Reference

- Radix: https://www.radix-ui.com/docs/primitives/components/separator#api-reference
- Base UI: https://base-ui.com/react/components/separator#api-reference

## Source files

- `content/docs/components/base/separator.mdx`
- `content/docs/components/radix/separator.mdx`
