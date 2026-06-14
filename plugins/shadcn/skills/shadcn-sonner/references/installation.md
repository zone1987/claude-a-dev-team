# Sonner — Installation

## CLI (recommended)

```bash
npx shadcn@latest add sonner
```

Then add `<Toaster />` to your root layout.

## Manual

### 1. Install dependencies

```bash
npm install sonner next-themes
```

### 2. Copy component source from [source.md](source.md).

### 3. Add Toaster to root layout

```tsx title="app/layout.tsx"
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <Toaster />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

## Triggering toasts

```tsx
import { toast } from "sonner"

// Basic
toast("Event has been created.")

// With description and action
toast("Event has been created", {
  description: "Sunday, December 03, 2023 at 9:00 AM",
  action: {
    label: "Undo",
    onClick: () => console.log("Undo"),
  },
})
```

## API Reference

https://sonner.emilkowal.ski/getting-started

## Source files

- `content/docs/components/base/sonner.mdx`
