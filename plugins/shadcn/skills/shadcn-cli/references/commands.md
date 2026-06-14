# shadcn CLI — All Commands

## apply

Apply a preset to an existing project.

```bash
npx shadcn@latest apply a2r6bw
npx shadcn@latest apply a2r6bw --only theme
npx shadcn@latest apply a2r6bw --only font
```

`--only` supported values: `theme`, `font`

**Options:**
```
Usage: shadcn apply [options] [preset]

Options:
  --preset <preset>  preset configuration to apply
  --only [parts]     apply only parts: theme, font
  -y, --yes          skip confirmation (default: false)
  -c, --cwd <cwd>    working directory
  -s, --silent       mute output
```

---

## preset

Inspect and manage preset codes.

### preset decode

```bash
npx shadcn@latest preset decode a2r6bw
npx shadcn@latest preset decode a2r6bw --json
```

### preset resolve (alias: preset info)

```bash
npx shadcn@latest preset resolve
npx shadcn@latest preset info
npx shadcn@latest preset resolve --json
```

### preset url

```bash
npx shadcn@latest preset url a2r6bw
```

### preset open

```bash
npx shadcn@latest preset open a2r6bw
```

---

## view

View items from the registry before installing.

```bash
npx shadcn@latest view button
npx shadcn@latest view button card dialog
npx shadcn@latest view @acme/auth @v0/dashboard
```

**Options:**
```
Usage: shadcn view [options] <items...>

Options:
  -c, --cwd <cwd>  working directory
```

---

## search (alias: list)

Search for items from registries.

```bash
npx shadcn@latest search @shadcn
npx shadcn@latest search @shadcn -q "button"
npx shadcn@latest search @shadcn @v0 @acme
npx shadcn@latest list @acme
```

**Options:**
```
Usage: shadcn search|list [options] <registries...>

Options:
  -c, --cwd <cwd>        working directory
  -q, --query <query>    query string
  -l, --limit <number>   maximum items per registry (default: 100)
  -o, --offset <number>  items to skip (default: 0)
```

---

## build

Generate registry JSON files from `registry.json`.

```bash
npx shadcn@latest build
npx shadcn@latest build --output ./public/registry
```

**Options:**
```
Usage: shadcn build [options] [registry]

Arguments:
  registry             path to registry.json (default: ./registry.json)

Options:
  -o, --output <path>  destination for JSON files (default: ./public/r)
  -c, --cwd <cwd>      working directory
```

---

## docs

Fetch documentation and API references for components.

```bash
npx shadcn@latest docs button
npx shadcn@latest docs button --json
npx shadcn@latest docs button --base radix
```

**Options:**
```
Usage: shadcn docs [options] [component]

Options:
  -c, --cwd <cwd>    working directory
  -b, --base <base>  'base' or 'radix' (defaults to project base)
  --json             output as JSON
```

---

## info

Get information about your project.

```bash
npx shadcn@latest info
npx shadcn@latest info --json
```

---

## migrate

Run migrations on your project.

```bash
npx shadcn@latest migrate icons
npx shadcn@latest migrate radix
npx shadcn@latest migrate rtl
npx shadcn@latest migrate --list
```

**Available migrations:**

| Migration | Description |
|-----------|-------------|
| `icons`   | Migrate UI components to a different icon library |
| `radix`   | Migrate to radix-ui (unified package) |
| `rtl`     | Migrate components to support RTL |

### migrate rtl

```bash
npx shadcn@latest migrate rtl
# Specific files or glob
npx shadcn@latest migrate rtl src/components/ui/button.tsx
npx shadcn@latest migrate rtl "src/components/ui/**"
```

This:
1. Updates `components.json` to set `rtl: true`
2. Transforms physical CSS to logical equivalents (`ml-4` → `ms-4`,
   `text-left` → `text-start`)
3. Adds `rtl:` variants (`space-x-4` → `space-x-4 rtl:space-x-reverse`)

### migrate radix

```bash
npx shadcn@latest migrate radix
npx shadcn@latest migrate radix src/components/ui/dialog.tsx
npx shadcn@latest migrate radix "src/components/ui/**"
```

Transforms imports from `@radix-ui/react-*` to the unified `radix-ui` package:

Before:
```tsx
import * as DialogPrimitive from "@radix-ui/react-dialog"
import * as SelectPrimitive from "@radix-ui/react-select"
```

After:
```tsx
import { Dialog as DialogPrimitive, Select as SelectPrimitive } from "radix-ui"
```

**Options:**
```
Usage: shadcn migrate [options] [migration] [path]

Options:
  -c, --cwd <cwd>  working directory
  -l, --list       list all migrations
  -y, --yes        skip confirmation
```

---

## eject

Inline `shadcn/tailwind.css` into your global CSS file and remove the `shadcn`
dependency.

**This action is irreversible.** Future shadcn CLI updates to `shadcn/tailwind.css`
will not apply automatically.

```bash
npx shadcn@latest eject

# Monorepo
npx shadcn@latest eject -c packages/ui
```

Before:
```css
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
```

After: the content of `shadcn/tailwind.css` is inlined, including `@keyframes`,
`@custom-variant` definitions, and `@utility no-scrollbar`.

**Options:**
```
Usage: shadcn eject [options]

Options:
  -c, --cwd <cwd>  working directory
  -y, --yes        skip confirmation
  -s, --silent     mute output
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/cli.mdx`
