# Empty — Installation

## CLI

```bash
npx shadcn-vue@latest add empty
```

## Manuell

Keine externen Abhaengigkeiten (nur `class-variance-authority` fuer Varianten).

### Schritte

1. Quellcode kopieren nach `components/ui/empty/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from '@/components/ui/empty'
</script>
```

Quellen:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/empty
