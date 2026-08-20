# Form — Installation

## CLI

```bash
npx shadcn-vue@latest add form
```

## Manual

### Dependencies

```bash
npm install reka-ui vee-validate @vee-validate/zod zod
```

### Steps

1. Copy source code to `components/ui/form/`
2. Adjust import paths

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

Sources:
- https://vee-validate.logaretm.com/v4/guide/overview/
- https://zod.dev
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/form
