# PinInput — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add pin-input
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. Folgende Dateien nach `src/components/ui/pin-input/` kopieren:
   - `PinInput.vue`
   - `PinInputGroup.vue`
   - `PinInputSeparator.vue`
   - `PinInputSlot.vue`
   - `index.ts`

## Imports

```ts
import {
  PinInput,
  PinInputGroup,
  PinInputSeparator,
  PinInputSlot,
} from "@/components/ui/pin-input"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/pin-input/index.ts`
