# Dialog — Installation

## CLI

```bash
npx shadcn-vue@latest add dialog
```

## Manuell

### Abhaengigkeiten

```bash
npm install reka-ui
```

### Manuelle Schritte

1. Quellcode kopieren (siehe `references/source.md`) nach `components/ui/dialog/`
2. Importpfade an das eigene Projekt anpassen (`@/lib/utils`, `@/registry/...` ersetzen)

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

Quellen:
- https://reka-ui.com/docs/components/dialog
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/dialog
