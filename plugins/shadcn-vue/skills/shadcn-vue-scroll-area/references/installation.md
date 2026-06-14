# ScrollArea — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add scroll-area
```

This adds `ScrollArea.vue`, `ScrollBar.vue`, and `index.ts` to your components directory.

## Manual

1. Install the reka-ui peer dependency:

```bash
npm install reka-ui
```

2. Copy `ScrollArea.vue`, `ScrollBar.vue`, and `index.ts` from [source.md](source.md) into your components directory (e.g. `src/components/ui/scroll-area/`).

3. Ensure `@/lib/utils` exports the `cn` helper (clsx + tailwind-merge).

4. Ensure `@vueuse/core` is installed (provides `reactiveOmit`):

```bash
npm install @vueuse/core
```
