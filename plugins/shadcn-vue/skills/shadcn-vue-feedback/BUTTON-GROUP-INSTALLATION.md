# ButtonGroup — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add button-group
```

This adds `ButtonGroup.vue`, `ButtonGroupSeparator.vue`, `ButtonGroupText.vue`, and `index.ts` to `src/components/ui/button-group/`.

## Manual installation

### 1. Prerequisites

Ensure the following are already installed:

- `reka-ui` — provides `Primitive`, `Separator`
- `class-variance-authority` — CVA for variants
- `@vueuse/core` — `reactiveOmit` used in `ButtonGroupSeparator`
- shadcn-vue `Separator` component (`src/components/ui/separator/`)
- shadcn-vue `Button` component (optional, but the typical consumer)

```bash
npm install reka-ui class-variance-authority @vueuse/core
```

### 2. Add the Separator component (if not present)

```bash
npx shadcn-vue@latest add separator
```

### 3. Create `src/components/ui/button-group/index.ts`

See [Source](source.md) for the full content.

### 4. Create the Vue SFCs

Copy `ButtonGroup.vue`, `ButtonGroupSeparator.vue`, and `ButtonGroupText.vue` from [Source](source.md) into `src/components/ui/button-group/`.

### 5. Update your barrel import (optional)

If you maintain a central `src/components/ui/index.ts`:

```ts
export * from "./button-group"
```

## Import in a component

```ts
import {
  ButtonGroup,
  ButtonGroupSeparator,
  ButtonGroupText,
} from "@/components/ui/button-group"
```
