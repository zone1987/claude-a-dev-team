# RTL Setup: Vite

## Step 1: Create project

```bash
npx shadcn@latest create --template vite --rtl
```

Produces `components.json` with `"rtl": true`.

## Step 2: Add dir and lang to index.html

```html title="index.html"
<!doctype html>
<html lang="ar" dir="rtl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## Step 3: Add DirectionProvider to main.tsx

```tsx title="src/main.tsx"
import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import { DirectionProvider } from "@/components/ui/direction"
import App from "./App"
import "./index.css"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <DirectionProvider direction="rtl">
      <App />
    </DirectionProvider>
  </StrictMode>
)
```

## Step 4: Add font (Fontsource)

```bash
npm install @fontsource-variable/noto-sans-arabic
```

```css title="src/index.css"
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
@import "@fontsource-variable/noto-sans-arabic";

@theme inline {
  --font-sans: "Noto Sans Arabic Variable", sans-serif;
}
```

For Hebrew: `@fontsource-variable/noto-sans-hebrew`.

## Step 5: Add components

```bash
npx shadcn@latest add button
```

Source: rtl/vite.mdx
