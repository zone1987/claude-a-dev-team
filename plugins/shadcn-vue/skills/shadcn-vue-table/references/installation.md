# Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add table
```

## Manuell

Copy source files from GitHub into `src/components/ui/table/`:
https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/table

No additional npm dependencies required for basic usage.

### TanStack Table Integration

For use with `@tanstack/vue-table`, install it separately:

```bash
npm install @tanstack/vue-table
```

The `valueUpdater` helper in `utils.ts` bridges TanStack's `Updater<T>` type
with Vue refs.
