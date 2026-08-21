# Empty — Installation

## CLI

```bash
npx shadcn-vue@latest add empty
```

## Manual

No external dependencies (only `class-variance-authority` for variants).

### Steps

1. Copy the source code into `components/ui/empty/`
2. Adjust import paths

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

Sources:
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/empty
