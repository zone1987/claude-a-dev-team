# Dark Mode — Next.js

Uses `next-themes` package.

## Step 1 — Install next-themes

```bash
npm install next-themes
```

## Step 2 — Create ThemeProvider

```tsx
// components/theme-provider.tsx
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"

export function ThemeProvider({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

## Step 3 — Wrap root layout

Add `suppressHydrationWarning` to `<html>`:

```tsx
// app/layout.tsx
import { ThemeProvider } from "@/components/theme-provider"

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <>
      <html lang="en" suppressHydrationWarning>
        <head />
        <body>
          <ThemeProvider
            attribute="class"
            defaultTheme="system"
            enableSystem
            disableTransitionOnChange
          >
            {children}
          </ThemeProvider>
        </body>
      </html>
    </>
  )
}
```

## Step 4 — Add mode toggle

Use the shadcn `mode-toggle` component or create your own:

```bash
npx shadcn@latest add dropdown-menu
```

The mode toggle renders a sun/moon icon button with a dropdown to select
Light / Dark / System.

Source: `/tmp/shadcn-repo/apps/v4/content/docs/dark-mode/next.mdx`
