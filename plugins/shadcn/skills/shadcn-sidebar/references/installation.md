# Sidebar — Installation

## CLI (recommended)

```bash
npx shadcn@latest add sidebar
```

This also installs `button`, `input`, `separator`, `sheet`, `skeleton`, `tooltip` as dependencies.

## Manual

Copy the full `components/ui/sidebar.tsx` from [source.md](source.md).

The Sidebar component also requires:
- `button`, `input`, `separator`, `sheet`, `skeleton`, `tooltip` components
- `useIsMobile` hook (`registry/new-york-v4/hooks/use-mobile`)
- `class-variance-authority` (`cva`)

## App layout integration

```tsx title="app/layout.tsx"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

## Minimal AppSidebar component

```tsx title="components/app-sidebar.tsx"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
} from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader />
      <SidebarContent>
        <SidebarGroup />
        <SidebarGroup />
      </SidebarContent>
      <SidebarFooter />
    </Sidebar>
  )
}
```

## Keyboard shortcut

`Cmd+B` (macOS) / `Ctrl+B` (Windows) toggles the sidebar globally.

Configured via `SIDEBAR_KEYBOARD_SHORTCUT = "b"` in sidebar.tsx.

## Inset variant layout

```tsx
<SidebarProvider>
  <Sidebar variant="inset" />
  <SidebarInset>
    <main>{children}</main>
  </SidebarInset>
</SidebarProvider>
```

## Custom width

```tsx
<SidebarProvider
  style={{
    "--sidebar-width": "20rem",
    "--sidebar-width-mobile": "20rem",
  } as React.CSSProperties}
>
  <Sidebar />
</SidebarProvider>
```

## Source files

- `content/docs/components/base/sidebar.mdx`
- `content/docs/components/radix/sidebar.mdx`
