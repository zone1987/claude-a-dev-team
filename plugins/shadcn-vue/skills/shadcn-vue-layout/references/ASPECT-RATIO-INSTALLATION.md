# AspectRatio — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add aspect-ratio
```

This automatically installs the reka-ui dependency and copies the component into `src/components/ui/aspect-ratio/`.

## Manual

### 1. Install the dependency

```bash
npm install reka-ui
```

### 2. Copy the component files

Create `src/components/ui/aspect-ratio/AspectRatio.vue` and `src/components/ui/aspect-ratio/index.ts` — see `references/source.md` for the full file contents.

### 3. Update import paths

Ensure `@/components/ui/aspect-ratio` resolves to the directory you created. With a standard Vite + Vue 3 project the `@` alias points to `src/`, so no extra configuration is needed.
