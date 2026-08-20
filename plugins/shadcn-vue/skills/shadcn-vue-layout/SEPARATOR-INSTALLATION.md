# Separator — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add separator
```

This adds `Separator.vue` and `index.ts` to your components directory.

## Manual

1. Install the reka-ui peer dependency:

```bash
npm install reka-ui
```

2. Ensure `@vueuse/core` is installed (provides `reactiveOmit`):

```bash
npm install @vueuse/core
```

3. Copy `Separator.vue` and `index.ts` from [source.md](source.md) into your components directory (e.g. `src/components/ui/separator/`).

4. Ensure `@/lib/utils` exports the `cn` helper (clsx + tailwind-merge).
