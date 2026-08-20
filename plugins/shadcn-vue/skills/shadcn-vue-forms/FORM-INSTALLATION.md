# Form — Installation

## CLI

```bash
npx shadcn-vue@latest add form
```

## Manuell

### Abhaengigkeiten

```bash
npm install reka-ui vee-validate @vee-validate/zod zod
```

### Schritte

1. Quellcode kopieren nach `components/ui/form/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormFieldArray,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
</script>
```

Quellen:
- https://vee-validate.logaretm.com/v4/guide/overview/
- https://zod.dev
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/form
