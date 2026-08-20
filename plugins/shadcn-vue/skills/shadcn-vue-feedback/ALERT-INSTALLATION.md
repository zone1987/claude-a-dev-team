# Alert — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add alert
```

## Manual

### 1. No extra dependencies needed

Alert has no reka-ui dependency. Only requires `class-variance-authority` and your `cn()` utility.

### 2. Copy source files

Copy all files from the `ui/alert/` directory into your project (e.g. `src/components/ui/alert/`).
See `references/source.md` for the complete source code.

### 3. Update import paths

Replace `@/registry/new-york-v4/ui/alert` with your actual component path, e.g. `@/components/ui/alert`.

## Dependencies

- `class-variance-authority` (cva) — for alertVariants
- `cn()` utility from `@/lib/utils`

---
Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/alert.md`
