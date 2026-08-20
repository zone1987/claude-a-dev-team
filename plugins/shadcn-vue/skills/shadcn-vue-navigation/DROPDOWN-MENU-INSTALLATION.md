# DropdownMenu — Installation

## CLI

```bash
npx shadcn-vue@latest add dropdown-menu
```

## Manual

### Dependencies

```bash
npm install reka-ui
```

### Steps

1. Copy the source code to `components/ui/dropdown-menu/`
2. Adjust the import paths

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

Sources:
- https://reka-ui.com/docs/components/dropdown-menu
- https://reka-ui.com/docs/components/dropdown-menu#api-reference
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/dropdown-menu
