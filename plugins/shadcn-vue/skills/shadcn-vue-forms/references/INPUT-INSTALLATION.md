# Input — Installation

## CLI

```bash
npx shadcn-vue@latest add input
```

## Manual

No external dependencies except `@vueuse/core` (useVModel).

### Steps

1. Copy source code (see `references/source.md`) to `components/ui/input/`
2. Adjust the `@/lib/utils` import path

### Import

```vue
<script setup lang="ts">
import { Input } from '@/components/ui/input'
</script>
```

Sources:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/input
