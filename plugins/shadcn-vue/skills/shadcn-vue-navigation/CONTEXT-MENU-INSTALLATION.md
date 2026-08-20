# Context Menu — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add context-menu
```

This installs the component files into `components/ui/context-menu/` and adds `reka-ui` as a dependency automatically.

## Manual Installation

### 1. Install dependency

```bash
npm install reka-ui
```

### 2. Copy source files

Copy all files from `registry/new-york-v4/ui/context-menu/` into your project's `components/ui/context-menu/` directory:

- `ContextMenu.vue`
- `ContextMenuCheckboxItem.vue`
- `ContextMenuContent.vue`
- `ContextMenuGroup.vue`
- `ContextMenuItem.vue`
- `ContextMenuLabel.vue`
- `ContextMenuRadioGroup.vue`
- `ContextMenuRadioItem.vue`
- `ContextMenuSeparator.vue`
- `ContextMenuShortcut.vue`
- `ContextMenuSub.vue`
- `ContextMenuSubContent.vue`
- `ContextMenuSubTrigger.vue`
- `ContextMenuTrigger.vue`
- `index.ts`

### 3. Update imports

Replace registry-specific import paths with your own:

```ts
// Before
import { ... } from "@/registry/new-york-v4/ui/context-menu"

// After
import { ... } from "@/components/ui/context-menu"
```

Also ensure you have `@/lib/utils` providing the `cn` helper (clsx + tailwind-merge).

## reka-ui Reference

The Context Menu component is built on top of reka-ui's ContextMenu primitives:

- **API Reference:** https://reka-ui.com/docs/components/context-menu
- **API Reference (detailed):** https://reka-ui.com/docs/components/context-menu#api-reference
