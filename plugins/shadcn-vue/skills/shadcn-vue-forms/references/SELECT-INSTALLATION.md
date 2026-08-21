# Select — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add select
```

This adds all 11 component files and `index.ts` to your components directory.

## Manual

1. Install the reka-ui peer dependency:

```bash
npm install reka-ui
```

2. Install lucide-vue for icons:

```bash
npm install @lucide/vue
```

3. Ensure `@vueuse/core` is installed (provides `reactiveOmit`):

```bash
npm install @vueuse/core
```

4. Copy all component files from [source.md](SELECT-SOURCE.md) into your components directory (e.g. `src/components/ui/select/`).

5. Ensure `@/lib/utils` exports the `cn` helper (clsx + tailwind-merge).
