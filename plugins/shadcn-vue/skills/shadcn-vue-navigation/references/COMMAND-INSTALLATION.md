# Command — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add command
```

This installs the component files into `components/ui/command/` and adds `reka-ui` as a dependency automatically.

## Manual Installation

### 1. Install dependency

```bash
npm install reka-ui
```

### 2. Copy source files

Copy all files from `registry/new-york-v4/ui/command/` into your project's `components/ui/command/` directory:

- `Command.vue`
- `CommandDialog.vue`
- `CommandEmpty.vue`
- `CommandGroup.vue`
- `CommandInput.vue`
- `CommandItem.vue`
- `CommandList.vue`
- `CommandSeparator.vue`
- `CommandShortcut.vue`
- `index.ts`

### 3. Update imports

Replace registry-specific import paths with your own:

```ts
// Before
import { ... } from "@/registry/new-york-v4/ui/command"

// After
import { ... } from "@/components/ui/command"
```

Also ensure you have `@/lib/utils` providing the `cn` helper (clsx + tailwind-merge).

## reka-ui Reference

The Command component is built on top of reka-ui's Combobox/Listbox API:

- **API Reference:** https://reka-ui.com/docs/components/combobox
- **Listbox:** https://reka-ui.com/docs/components/listbox
