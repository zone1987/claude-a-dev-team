# RTL Setup: TanStack Start

## Step 1: Create project

```bash
npx shadcn@latest create --template start --rtl
```

Produces `components.json` with `"rtl": true`.

## Step 2: Add DirectionProvider to __root.tsx

```tsx title="src/routes/__root.tsx"
import { DirectionProvider } from "@/components/ui/direction"

export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
    <html lang="ar" dir="rtl">
      <head>
        <Meta />
      </head>
      <body>
        <DirectionProvider direction="rtl">{children}</DirectionProvider>
        <Scripts />
      </body>
    </html>
  )
}
```

Update `lang="ar"` to your target language.

## Step 3: Add font (Fontsource)

```bash
npm install @fontsource-variable/noto-sans-arabic
```

```css title="src/styles.css"
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
@import "@fontsource-variable/noto-sans-arabic";

@theme inline {
  --font-sans: "Noto Sans Arabic Variable", sans-serif;
}
```

For Hebrew: `@fontsource-variable/noto-sans-hebrew`.

## Step 4: Add components

```bash
npx shadcn@latest add button
```

Source: rtl/start.mdx
