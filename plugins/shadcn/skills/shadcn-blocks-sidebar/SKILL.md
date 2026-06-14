---
name: shadcn-blocks-sidebar
description: shadcn/ui v4 Sidebar Blocks (sidebar-01..16): vollstaendiger Code aller 16 Sidebar-Block-Varianten fuer Next.js/React. Includes all component files.
triggers:
  - shadcn sidebar block
  - sidebar-01
  - sidebar-02
  - sidebar-03
  - sidebar-04
  - sidebar-05
  - sidebar-06
  - sidebar-07
  - sidebar-08
  - sidebar-09
  - sidebar-10
  - sidebar-11
  - sidebar-12
  - sidebar-13
  - sidebar-14
  - sidebar-15
  - sidebar-16
  - shadcn sidebar variante
  - shadcn sidebar block code
  - sidebar block installieren
  - shadcn collapsible sidebar
  - shadcn icon sidebar
  - shadcn inset sidebar
  - shadcn floating sidebar
  - shadcn sidebar dual
  - shadcn sidebar calendar
  - shadcn sidebar settings dialog
  - shadcn sidebar toc
  - shadcn sidebar file tree
  - shadcn sidebar notion
  - sidebar block npx
---

# shadcn/ui Sidebar Blocks (sidebar-01..16)

All 16 sidebar blocks from shadcn/ui v4 (New York style).

## Installation

```bash
npx shadcn@latest add sidebar-01
npx shadcn@latest add sidebar-02
npx shadcn@latest add sidebar-03
npx shadcn@latest add sidebar-04
npx shadcn@latest add sidebar-05
npx shadcn@latest add sidebar-06
npx shadcn@latest add sidebar-07
npx shadcn@latest add sidebar-08
npx shadcn@latest add sidebar-09
npx shadcn@latest add sidebar-10
npx shadcn@latest add sidebar-11
npx shadcn@latest add sidebar-12
npx shadcn@latest add sidebar-13
npx shadcn@latest add sidebar-14
npx shadcn@latest add sidebar-15
npx shadcn@latest add sidebar-16
```

## Block Overview

| Block | Variant | Key Features |
|---|---|---|
| sidebar-01 | default | VersionSwitcher + SearchForm + grouped nav, SidebarRail |
| sidebar-02 | default | Same as 01 but with collapsible ChevronRight sections |
| sidebar-03 | default | Logo header + SubMenu tree, no search/version, SidebarRail |
| sidebar-04 | floating | `variant="floating"`, SubMenu tree, 19rem wide, no SidebarRail |
| sidebar-05 | default | Logo + SearchForm + Plus/Minus collapsible sections + SidebarRail |
| sidebar-06 | default | Logo + NavMain DropdownMenu subitems + SidebarOptInForm footer |
| sidebar-07 | default | Full app: TeamSwitcher + NavMain + NavProjects + NavUser, `collapsible="icon"` |
| sidebar-08 | inset | NavMain separate collapse trigger + NavProjects + NavSecondary + NavUser |
| sidebar-09 | default | Dual sidebar: icon strip + email list panel, `--sidebar-width: 350px` |
| sidebar-10 | default | Notion-style: TeamSwitcher + NavMain flat + NavFavorites emoji + NavWorkspaces |
| sidebar-11 | default | File tree: Changes list with M/U badges + recursive Tree component |
| sidebar-12 | default | Calendar: NavUser header + DatePicker + Calendars collapsible groups |
| sidebar-13 | default | Settings Dialog: Sidebar inside Dialog for 12 settings categories |
| sidebar-14 | right | `side="right"`, SidebarTrigger rotated 180deg, Table of Contents |
| sidebar-15 | default | Dual layout: SidebarLeft (Notion) + SidebarRight (Calendar), 10 component files |
| sidebar-16 | default | Sticky header: SiteHeader with SearchForm + `useSidebar().toggleSidebar` |

## Reference Files

- [sidebar-01-04.md](references/sidebar-01-04.md) — Complete code for sidebar-01, sidebar-02, sidebar-03, sidebar-04
- [sidebar-05-08.md](references/sidebar-05-08.md) — Complete code for sidebar-05, sidebar-06, sidebar-07, sidebar-08
- [sidebar-09-12.md](references/sidebar-09-12.md) — Complete code for sidebar-09, sidebar-10, sidebar-11, sidebar-12
- [sidebar-13-16.md](references/sidebar-13-16.md) — Complete code for sidebar-13, sidebar-14, sidebar-15, sidebar-16

## Common Patterns

All sidebar blocks use `SidebarProvider` wrapping `AppSidebar` + `SidebarInset`:

```tsx
<SidebarProvider>
  <AppSidebar />
  <SidebarInset>
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
      <SidebarTrigger className="-ml-1" />
      {/* ... */}
    </header>
    {/* main content */}
  </SidebarInset>
</SidebarProvider>
```

Import path for sidebar primitives:
```tsx
import { Sidebar, SidebarProvider, SidebarInset, SidebarTrigger, ... } from "@/registry/new-york-v4/ui/sidebar"
```
