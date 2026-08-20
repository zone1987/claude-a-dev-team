# Kbd — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add kbd
```

## Manuell

1. Keine externen Abhangigkeiten (keine reka-ui-Primitive benotigt)

2. Folgende Dateien nach `src/components/ui/kbd/` kopieren:
   - `Kbd.vue`
   - `KbdGroup.vue`
   - `index.ts`

## Imports

```ts
import { Kbd, KbdGroup } from "@/components/ui/kbd"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/kbd/index.ts`
