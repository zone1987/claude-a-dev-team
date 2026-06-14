# Sheet — Installation

## CLI (recommended)

```bash
npx shadcn@latest add sheet
```

## Manual (Radix variant)

### 1. Install dependency

```bash
npm install radix-ui
```

### 2. Copy component

Create `components/ui/sheet.tsx` with the source from [source.md](source.md).

## Manual (Base UI variant)

### 1. Install dependency

```bash
npm install @base-ui/react
```

### 2. Use base variant source from [source.md](source.md).

## Usage

```tsx
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
```

```tsx
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Are you absolutely sure?</SheetTitle>
      <SheetDescription>This action cannot be undone.</SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```

## Composition

```text
Sheet
├── SheetTrigger
└── SheetContent
    ├── SheetHeader
    │   ├── SheetTitle
    │   └── SheetDescription
    └── SheetFooter
```

## API Reference

- Radix: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
- Base UI: https://base-ui.com/react/components/dialog#api-reference

## Source files

- `content/docs/components/base/sheet.mdx`
- `content/docs/components/radix/sheet.mdx`
