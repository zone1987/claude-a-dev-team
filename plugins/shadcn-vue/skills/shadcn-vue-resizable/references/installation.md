# Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add resizable
```

This copies all 3 component files into your project's UI directory and updates the component index automatically.

## Manual Installation

### 1. Install dependencies

```bash
npm install reka-ui @vueuse/core
```

### 2. Copy source files

Copy `ResizableHandle.vue`, `ResizablePanel.vue`, `ResizablePanelGroup.vue`, and `index.ts` from `references/source.md` into your UI components directory, for example `src/components/ui/resizable/`.

### 3. Update imports

Ensure `@/lib/utils` exports the `cn` helper (a `clsx` + `tailwind-merge` wrapper).

### 4. Lucide icons

`ResizableHandle` imports `GripVertical` from `@lucide/vue`. Install if not already present:

```bash
npm install @lucide/vue
```
