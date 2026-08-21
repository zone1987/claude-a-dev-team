# Field — Installation

## CLI

```bash
npx shadcn-vue@latest add field
```

## Manual

No external headless dependencies (only `class-variance-authority`).
Internal dependencies: `ui/label` and `ui/separator`.

### Steps

1. Copy source code to `components/ui/field/`
2. Adjust import paths

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

Sources:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/field
