# Item — Installation

## CLI (empfohlen)

```bash
npx shadcn-vue@latest add item
```

## Manuell

1. Abhangigkeiten installieren:

```bash
npm install reka-ui class-variance-authority
```

2. Folgende Dateien nach `src/components/ui/item/` kopieren:
   - `Item.vue`
   - `ItemActions.vue`
   - `ItemContent.vue`
   - `ItemDescription.vue`
   - `ItemFooter.vue`
   - `ItemGroup.vue`
   - `ItemHeader.vue`
   - `ItemMedia.vue`
   - `ItemSeparator.vue`
   - `ItemTitle.vue`
   - `index.ts`

3. `Separator`-Komponente muss vorhanden sein (wird von `ItemSeparator` importiert):

```bash
npx shadcn-vue@latest add separator
```

## Imports

```ts
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemFooter,
  ItemGroup,
  ItemHeader,
  ItemMedia,
  ItemSeparator,
  ItemTitle,
} from "@/components/ui/item"
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/item/index.ts`
