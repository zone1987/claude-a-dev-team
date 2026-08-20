# RTL Setup: Next.js

## Step 1: Create project

```bash
npx shadcn@latest create --template next --rtl
```

Produces `components.json` with `"rtl": true`.

## Step 2: Add DirectionProvider to layout

```tsx title="app/layout.tsx"
import { DirectionProvider } from "@/components/ui/direction"

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ar" dir="rtl">
      <body>
        <DirectionProvider direction="rtl">{children}</DirectionProvider>
      </body>
    </html>
  )
}
```

Update `lang="ar"` to your target language.

## Step 3: Add font (Noto via next/font)

```tsx title="app/layout.tsx"
import { Noto_Sans_Arabic } from "next/font/google"
import { DirectionProvider } from "@/components/ui/direction"

const fontSans = Noto_Sans_Arabic({
  subsets: ["arabic"],
  variable: "--font-sans",
})

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ar" dir="rtl" className={fontSans.variable}>
      <body>
        <DirectionProvider direction="rtl">{children}</DirectionProvider>
      </body>
    </html>
  )
}
```

For Hebrew: use `Noto_Sans_Hebrew` from `next/font/google`.

## Step 4: Add components

```bash
npx shadcn@latest add button
```

The CLI automatically transforms physical classes to logical equivalents.

Source: rtl/next.mdx
