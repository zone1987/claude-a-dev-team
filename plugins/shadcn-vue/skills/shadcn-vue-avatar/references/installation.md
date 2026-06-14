# Avatar — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add avatar
```

This adds `components/ui/avatar/Avatar.vue`, `AvatarImage.vue`, `AvatarFallback.vue`, and `index.ts` to your project and installs the required peer dependency.

## Manual

### 1. Install reka-ui

```bash
npm install reka-ui
```

`@vueuse/core` is also required for `AvatarFallback` (uses `reactiveOmit`):

```bash
npm install @vueuse/core
```

### 2. Copy the component files

Create `components/ui/avatar/` and add the three Vue files plus `index.ts`. See [source.md](source.md) for the complete file contents.

### 3. Import in your component

```ts
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"
```

### Dependencies

| Package | Minimum version | Notes |
|---|---|---|
| `reka-ui` | latest | Provides `AvatarRoot`, `AvatarImage`, `AvatarFallback` primitives |
| `@vueuse/core` | latest | `reactiveOmit` used in `AvatarFallback.vue` |
| `tailwindcss` | v4 | Utility classes for sizing and shape |
