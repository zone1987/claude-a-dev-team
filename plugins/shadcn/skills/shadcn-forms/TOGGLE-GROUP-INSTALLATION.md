# ToggleGroup — Installation

## CLI (recommended)

```bash
npx shadcn@latest add toggle-group
```

Automatically installs `toggle` as a dependency (uses `toggleVariants`).

## Manual

Install dependency:

```bash
npm install radix-ui
```

Copy `components/ui/toggle-group.tsx` and `components/ui/toggle.tsx` (see source.md).
Update import paths to match your project.

## Usage

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

```tsx
<ToggleGroup type="single">
  <ToggleGroupItem value="a">A</ToggleGroupItem>
  <ToggleGroupItem value="b">B</ToggleGroupItem>
  <ToggleGroupItem value="c">C</ToggleGroupItem>
</ToggleGroup>
```

## Changelog

### 2026-05-17 Default Spacing

Changed the default `spacing` from `0` to `2` so toggle groups render with space between items
by default. Use `spacing={0}` for connected items.

Sources: content/docs/components/radix/toggle-group.mdx
