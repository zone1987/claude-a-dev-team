# Button — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add button
```

To also enable `cursor: pointer` for buttons (Tailwind v4 changed the default to `cursor: default`):

```bash
npx shadcn-vue@latest add button --pointer
# or during project init:
npx shadcn-vue@latest init --pointer
```

## Manual

### 1. Install dependencies

```bash
npm install reka-ui class-variance-authority
npm install @vueuse/core  # required by many shadcn-vue components
```

### 2. Add the utility helper (if not already present)

`src/lib/utils.ts`:
```ts
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### 3. Copy component files

Create `src/components/ui/button/` and add `index.ts` and `Button.vue` from the [source reference](source.md).

### 4. (Optional) Restore pointer cursor in Tailwind v4

Add to your global CSS file (e.g. `src/assets/index.css`):

```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```
