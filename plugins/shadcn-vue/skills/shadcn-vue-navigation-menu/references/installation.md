# NavigationMenu — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add navigation-menu
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui @vueuse/core @lucide/vue class-variance-authority
```

2. Folgende Dateien nach `src/components/ui/navigation-menu/` kopieren:
   - `NavigationMenu.vue`
   - `NavigationMenuContent.vue`
   - `NavigationMenuIndicator.vue`
   - `NavigationMenuItem.vue`
   - `NavigationMenuLink.vue`
   - `NavigationMenuList.vue`
   - `NavigationMenuTrigger.vue`
   - `NavigationMenuViewport.vue`
   - `index.ts`

## Imports

```ts
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/navigation-menu/index.ts`
