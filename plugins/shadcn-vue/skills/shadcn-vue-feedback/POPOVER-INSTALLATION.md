# Popover — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add popover
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui @vueuse/core
```

2. Folgende Dateien nach `src/components/ui/popover/` kopieren:
   - `Popover.vue`
   - `PopoverAnchor.vue`
   - `PopoverContent.vue`
   - `PopoverTrigger.vue`
   - `index.ts`

## Imports

```ts
import {
  Popover,
  PopoverAnchor,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/popover/index.ts`
