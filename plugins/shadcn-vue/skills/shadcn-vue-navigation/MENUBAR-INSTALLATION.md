# Menubar — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add menubar
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. Folgende Dateien nach `src/components/ui/menubar/` kopieren:
   - `Menubar.vue`
   - `MenubarCheckboxItem.vue`
   - `MenubarContent.vue`
   - `MenubarGroup.vue`
   - `MenubarItem.vue`
   - `MenubarLabel.vue`
   - `MenubarMenu.vue`
   - `MenubarRadioGroup.vue`
   - `MenubarRadioItem.vue`
   - `MenubarSeparator.vue`
   - `MenubarShortcut.vue`
   - `MenubarSub.vue`
   - `MenubarSubContent.vue`
   - `MenubarSubTrigger.vue`
   - `MenubarTrigger.vue`
   - `index.ts`

## Imports

```ts
import {
  Menubar,
  MenubarCheckboxItem,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarLabel,
  MenubarMenu,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarSeparator,
  MenubarShortcut,
  MenubarSub,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarTrigger,
} from "@/components/ui/menubar"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/menubar/index.ts`
