# Input — Installation

## CLI

```bash
npx shadcn-vue@latest add input
```

## Manuell

Keine externen Abhaengigkeiten ausser `@vueuse/core` (useVModel).

### Schritte

1. Quellcode kopieren (siehe `references/source.md`) nach `components/ui/input/`
2. Importpfad `@/lib/utils` anpassen

### Import

```vue
<script setup lang="ts">
import { Input } from '@/components/ui/input'
</script>
```

Quellen:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/input
