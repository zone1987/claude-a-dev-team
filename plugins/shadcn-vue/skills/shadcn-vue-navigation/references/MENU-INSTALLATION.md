# NavigationMenu — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add navigation-menu
```

## Manual

1. Install dependencies:

```bash
npm install reka-ui @vueuse/core @lucide/vue class-variance-authority
```

2. Copy the following files to `src/components/ui/navigation-menu/`:
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

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/navigation-menu/index.ts`
