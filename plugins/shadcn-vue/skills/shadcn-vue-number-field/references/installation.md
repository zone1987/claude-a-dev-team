# NumberField — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add number-field
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. Folgende Dateien nach `src/components/ui/number-field/` kopieren:
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

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/number-field/index.ts`
