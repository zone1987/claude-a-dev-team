# Dialog — Installation

## CLI

```bash
npx shadcn-vue@latest add dialog
```

## Manual

### Dependencies

```bash
npm install reka-ui
```

### Manual Steps

1. Copy the source code (see `references/source.md`) into `components/ui/dialog/`
2. Adjust the import paths to your own project (replace `@/lib/utils`, `@/registry/...`)

### Imports

```vue
<script setup lang="ts">
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogOverlay,
  DialogScrollContent,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
</script>
```

Sources:
- https://reka-ui.com/docs/components/dialog
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/dialog
