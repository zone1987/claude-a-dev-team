# shadcn/ui — Vite Installation

## Option A: Use shadcn/create
```bash
npx shadcn@latest init --preset [CODE] --template vite
```

## Option B: CLI scaffold
```bash
npx shadcn@latest init -t vite

# Monorepo
npx shadcn@latest init -t vite --monorepo
```

## Option C: Existing Vite project

### Step 1 — Create project
```bash
npm create vite@latest   # select React + TypeScript
```

### Step 2 — Add Tailwind CSS
```bash
npm install tailwindcss @tailwindcss/vite
```
Replace `src/index.css`:
```css
@import "tailwindcss";
```

### Step 3 — Edit tsconfig.json
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```
Also add to `tsconfig.app.json`:
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

### Step 4 — Update vite.config.ts
```bash
npm install -D @types/node
```
```typescript
import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
```

### Step 5 — Run the CLI
```bash
npx shadcn@latest init
```

### Step 6 — Add components
```bash
npx shadcn@latest add button
```
```tsx
import { Button } from "@/components/ui/button"
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/vite.mdx`
