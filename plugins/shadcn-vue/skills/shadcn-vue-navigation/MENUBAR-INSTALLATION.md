# Menubar — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add menubar
```

## Manual

1. Install dependencies:

```bash
npm install reka-ui @vueuse/core @lucide/vue
```

2. Copy the following files to `src/components/ui/menubar/`:
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

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/menubar/index.ts`
