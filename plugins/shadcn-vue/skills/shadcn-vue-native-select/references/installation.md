# NativeSelect — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add native-select
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install @vueuse/core @lucide/vue
```

2. Folgende Dateien nach `src/components/ui/native-select/` kopieren:
   - `NativeSelect.vue`
   - `NativeSelectOptGroup.vue`
   - `NativeSelectOption.vue`
   - `index.ts`

## Imports

```ts
import {
  NativeSelect,
  NativeSelectOptGroup,
  NativeSelectOption,
} from "@/components/ui/native-select"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/native-select/index.ts`
