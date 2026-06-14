# AlertDialog — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add alert-dialog
```

## Manual

### 1. Install dependencies

```bash
npm install reka-ui @vueuse/core
```

The `AlertDialogAction` and `AlertDialogCancel` components depend on the **Button** component for `buttonVariants`.
Make sure it is installed first:

```bash
npx shadcn-vue@latest add button
```

### 2. Copy source files

Copy all files from the `ui/alert-dialog/` directory into your project (e.g. `src/components/ui/alert-dialog/`).
See `references/source.md` for the complete source code.

### 3. Update import paths

- Replace `@/registry/new-york-v4/ui/button` with your actual button path, e.g. `@/components/ui/button`
- Replace `@/lib/utils` with your project's `cn()` utility path if it differs

## Dependencies

- `reka-ui` — Headless UI primitives (`AlertDialogRoot`, `AlertDialogPortal`, `AlertDialogOverlay`, `AlertDialogContent`, `AlertDialogTrigger`, `AlertDialogTitle`, `AlertDialogDescription`, `AlertDialogAction`, `AlertDialogCancel`)
- `@vueuse/core` — `reactiveOmit` (used in Content, Title, Description, Action, Cancel)
- `@/components/ui/button` — `buttonVariants` function (used by Action and Cancel for consistent button styling)

---
Source: https://www.shadcn-vue.com/docs/components/alert-dialog
