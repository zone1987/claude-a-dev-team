# Accordion — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add accordion
```

## Manual

### 1. Install dependency

```bash
npm install reka-ui
```

### 2. Copy source files

Copy all files from the `ui/accordion/` directory into your project (e.g. `src/components/ui/accordion/`).
See `references/source.md` for the complete source code.

### 3. Update import paths

Replace `@/registry/new-york-v4/ui/accordion` with your actual component path, e.g. `@/components/ui/accordion`.

## Dependencies

- `reka-ui` — Headless UI primitives (AccordionRoot, AccordionItem, AccordionHeader, AccordionTrigger, AccordionContent)
- `@vueuse/core` — `reactiveOmit`, `useForwardProps`
- `@lucide/vue` — `ChevronDown` icon
- `class-variance-authority` — not used directly in accordion, but used by `cn()` utility

---
Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/accordion.md`
