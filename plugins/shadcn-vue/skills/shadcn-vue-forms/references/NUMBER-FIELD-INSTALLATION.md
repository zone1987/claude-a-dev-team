# NumberField — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add number-field
```

## Manual

1. Install dependencies:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. Copy the following files to `src/components/ui/number-field/`:
   - `NumberField.vue`
   - `NumberFieldContent.vue`
   - `NumberFieldDecrement.vue`
   - `NumberFieldIncrement.vue`
   - `NumberFieldInput.vue`
   - `index.ts`

## Imports

```ts
import {
  NumberField,
  NumberFieldContent,
  NumberFieldDecrement,
  NumberFieldIncrement,
  NumberFieldInput,
} from "@/components/ui/number-field"
```

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/number-field/index.ts`
