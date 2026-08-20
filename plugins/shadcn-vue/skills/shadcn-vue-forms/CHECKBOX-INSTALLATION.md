# Checkbox — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add checkbox
```

This adds `src/components/ui/checkbox/Checkbox.vue` and `src/components/ui/checkbox/index.ts` to your project.

## Manual

1. Install the reka-ui peer dependency:

```bash
npm install reka-ui
```

2. Copy the source files (see [source.md](CHECKBOX-SOURCE.md)) into your project, e.g. `src/components/ui/checkbox/`.

3. Ensure `@/lib/utils` exports a `cn` helper (clsx + tailwind-merge) and that `@lucide/vue` is installed:

```bash
npm install @lucide/vue @vueuse/core
```

4. Update import paths as needed to match your project structure.

## reka-ui API reference

https://reka-ui.com/docs/components/checkbox
