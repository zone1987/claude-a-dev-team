# Drawer — Installation

## CLI

```bash
npx shadcn-vue@latest add drawer
```

## Manuell

### Abhaengigkeiten

```bash
npm install reka-ui vaul-vue
```

### Manuelle Schritte

1. Quellcode kopieren (siehe `references/source.md`) nach `components/ui/drawer/`
2. Importpfade anpassen (`@/lib/utils` etc.)

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

Quellen:
- https://reka-ui.com/docs/components/dialog (vaul-vue basiert auf Dialog-Pattern)
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/drawer
