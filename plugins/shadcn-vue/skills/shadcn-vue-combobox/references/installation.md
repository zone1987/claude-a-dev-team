# Combobox — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add combobox
```

This also installs the Popover and Command components as dependencies if you use the classic composition pattern.

## Manual

### 1. Install dependencies

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

### 2. Copy source files

Copy all files from the `ui/combobox/` directory into your project (e.g. `src/components/ui/combobox/`).
See `references/source.md` for the complete source code.

### 3. Update import paths

Replace `@/registry/bases/reka/ui/combobox` (or `@/registry/new-york-v4/ui/combobox`) with your actual component path, e.g. `@/components/ui/combobox`.

Ensure `@/lib/utils` exports the `cn()` helper (clsx + tailwind-merge).

## Dependencies

- `reka-ui` — Headless UI primitives (ComboboxRoot, ComboboxAnchor, ComboboxInput, ComboboxTrigger, ComboboxContent, ComboboxPortal, ComboboxViewport, ComboboxItem, ComboboxItemIndicator, ComboboxEmpty, ComboboxGroup, ComboboxLabel, ComboboxSeparator, ComboboxCancel)
- `@vueuse/core` — `reactiveOmit`, `useForwardProps`
- `@lucide/vue` — `SearchIcon` icon used in `ComboboxInput`
- `class-variance-authority` — used transitively via `cn()` utility

## reka-ui API Reference

Full primitive API: https://reka-ui.com/docs/components/combobox

---
Source: `registry/new-york-v4/ui/combobox/`, `registry/bases/reka/ui/combobox/`
