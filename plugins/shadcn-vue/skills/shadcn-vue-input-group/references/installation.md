# InputGroup — Installation

## CLI

```bash
npx shadcn-vue@latest add input-group
```

## Manuell

### Abhaengigkeiten

```bash
npm install reka-ui
```

### Schritte

1. Quellcode kopieren nach `components/ui/input-group/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from '@/components/ui/input-group'
</script>
```

Quellen:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/input-group
