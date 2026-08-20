# Item — Installation

## CLI

```bash
npx shadcn@latest add item
```

## Manual

Copy the component source from `references/source.md` into `components/ui/item.tsx` and update import paths.

### Dependencies

The `Item` component uses:
- `class-variance-authority` for `cva`
- `radix-ui` for `Slot.Root` (used when `asChild` is true)
- `@/components/ui/separator` for `ItemSeparator`
- `@/lib/utils` for the `cn` helper

```bash
npm install class-variance-authority radix-ui
```

---
Source: `content/docs/components/base/item.mdx`
