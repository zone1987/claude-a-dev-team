# Field — Installation

## CLI

```bash
npx shadcn-vue@latest add field
```

## Manuell

Keine externen Headless-Abhaengigkeiten (nur `class-variance-authority`).
Interne Abhaengigkeiten: `ui/label` und `ui/separator`.

### Schritte

1. Quellcode kopieren nach `components/ui/field/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
  FieldTitle,
} from '@/components/ui/field'
</script>
```

Quellen:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/field
