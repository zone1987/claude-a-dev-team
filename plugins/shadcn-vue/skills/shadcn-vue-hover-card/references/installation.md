# HoverCard — Installation

## CLI

```bash
npx shadcn-vue@latest add hover-card
```

## Manuell

### Abhaengigkeiten

```bash
npm install reka-ui
```

### Schritte

1. Quellcode kopieren nach `components/ui/hover-card/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from '@/components/ui/hover-card'
</script>
```

Quellen:
- https://reka-ui.com/docs/components/hover-card
- https://reka-ui.com/docs/components/hover-card#api-reference
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/hover-card
