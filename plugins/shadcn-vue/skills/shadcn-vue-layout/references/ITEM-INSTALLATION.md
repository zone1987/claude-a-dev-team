# Item — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add item
```

## Manual

1. Install dependencies:

```bash
npm install reka-ui class-variance-authority
```

2. Copy the following files into `src/components/ui/item/`:
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

3. The `Separator` component must be present (imported by `ItemSeparator`):

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

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/item/index.ts`
