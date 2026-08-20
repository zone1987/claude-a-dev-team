# Drawer — Installation

## CLI

```bash
npx shadcn-vue@latest add drawer
```

## Manual

### Dependencies

```bash
npm install reka-ui vaul-vue
```

### Manual steps

1. Copy the source code (see `references/source.md`) into `components/ui/drawer/`
2. Adjust import paths (`@/lib/utils` etc.)

### Imports

```vue
<script setup lang="ts">
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerOverlay,
  DrawerTitle,
  DrawerTrigger,
} from '@/components/ui/drawer'
</script>
```

Sources:
- https://reka-ui.com/docs/components/dialog (vaul-vue is based on the Dialog pattern)
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/drawer
