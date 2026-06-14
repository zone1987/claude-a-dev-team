# DropdownMenu — Installation

## CLI

```bash
npx shadcn-vue@latest add dropdown-menu
```

## Manuell

### Abhaengigkeiten

```bash
npm install reka-ui
```

### Schritte

1. Quellcode kopieren nach `components/ui/dropdown-menu/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuPortal,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
</script>
```

Quellen:
- https://reka-ui.com/docs/components/dropdown-menu
- https://reka-ui.com/docs/components/dropdown-menu#api-reference
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/dropdown-menu
