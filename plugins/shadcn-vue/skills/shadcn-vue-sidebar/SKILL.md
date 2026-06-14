---
name: shadcn-vue-sidebar
description: >
  shadcn-vue Sidebar component (composable, collapsible, mobile-responsive, Tailwind v4 Vue SFC).
  Triggers: "shadcn-vue sidebar", "sidebar vue", "seitenleiste vue",
  "collapsible sidebar vue", "sidebar reka-ui", "app navigation vue shadcn"
---

# shadcn-vue Sidebar Component

## Overview

The Sidebar is a composable, themeable, customizable navigation sidebar built for complex
application layouts. It supports collapsible modes (icon-only, offcanvas), mobile sheet mode,
keyboard shortcuts, and persisted state via cookies. It is composed of 24+ sub-components.

## Architecture

```
SidebarProvider  (context + keyboard shortcut + cookie persistence)
  Sidebar        (responsive: mobile=Sheet, desktop=fixed panel)
    SidebarHeader
    SidebarContent  (scrollable)
      SidebarGroup
        SidebarGroupLabel
        SidebarGroupAction
        SidebarGroupContent
          SidebarMenu
            SidebarMenuItem
              SidebarMenuButton  (with optional Tooltip)
              SidebarMenuAction
              SidebarMenuBadge
              SidebarMenuSub
                SidebarMenuSubItem
                  SidebarMenuSubButton
    SidebarFooter
    SidebarRail    (hover-to-expand rail)
    SidebarSeparator
    SidebarInput
  SidebarInset     (main content area)
  SidebarTrigger   (toggle button)
```

## Quick Start

```vue
<script setup lang="ts">
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
  SidebarRail,
  SidebarTrigger,
} from '@/components/ui/sidebar'
</script>

<template>
  <SidebarProvider>
    <Sidebar>
      <SidebarHeader />
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem>
                <SidebarMenuButton as-child>
                  <a href="#">Home</a>
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter />
      <SidebarRail />
    </Sidebar>
    <SidebarInset>
      <SidebarTrigger />
      <slot />
    </SidebarInset>
  </SidebarProvider>
</template>
```

## useSidebar Composable

```vue
<script setup lang="ts">
import { useSidebar } from '@/components/ui/sidebar'

const {
  state,        // ComputedRef<'expanded' | 'collapsed'>
  open,         // Ref<boolean>
  setOpen,      // (value: boolean) => void
  openMobile,   // Ref<boolean>
  setOpenMobile,// (value: boolean) => void
  isMobile,     // Ref<boolean>
  toggleSidebar,// () => void
} = useSidebar()
</script>
```

## Collapsible Modes

| Mode | Description |
|---|---|
| `offcanvas` | Slides off-screen when collapsed (default) |
| `icon` | Collapses to icon-only strip |
| `none` | Not collapsible |

## Variants

| Variant | Description |
|---|---|
| `sidebar` | Standard attached sidebar (default) |
| `floating` | Floating panel with border and shadow |
| `inset` | Inset layout, used with `SidebarInset` |

## Theming (CSS Variables)

```css
:root {
  --sidebar-background: 0 0% 98%;
  --sidebar-foreground: 240 5.3% 26.1%;
  --sidebar-primary: 240 5.9% 10%;
  --sidebar-primary-foreground: 0 0% 98%;
  --sidebar-accent: 240 4.8% 95.9%;
  --sidebar-accent-foreground: 240 5.9% 10%;
  --sidebar-border: 220 13% 91%;
  --sidebar-ring: 217.2 91.2% 59.8%;
}
.dark {
  --sidebar-background: 240 5.9% 10%;
  --sidebar-foreground: 240 4.8% 95.9%;
  --sidebar-primary: 224.3 76.3% 48%;
  --sidebar-primary-foreground: 0 0% 100%;
  --sidebar-accent: 240 3.7% 15.9%;
  --sidebar-accent-foreground: 240 4.8% 95.9%;
  --sidebar-border: 240 3.7% 15.9%;
  --sidebar-ring: 217.2 91.2% 59.8%;
}
```

## Keyboard Shortcut

Default: `Cmd+B` / `Ctrl+B` to toggle. Customizable via `SIDEBAR_KEYBOARD_SHORTCUT` constant.

## State Persistence

The open state is persisted in a cookie (`sidebar_state`, 7-day TTL). Use `defaultOpen`
on `SidebarProvider` to set the initial state.
