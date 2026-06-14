---
name: shadcn-blocks-overview
description: shadcn/ui v4 Blocks Uebersicht: alle 27 Blocks (dashboard, login, sidebar, signup), Installation via npx, Lift Mode, Open in v0, Beschreibungen.
triggers:
  - shadcn blocks
  - shadcn block uebersicht
  - shadcn blocks overview
  - shadcn blocks liste
  - shadcn alle blocks
  - npx shadcn add block
  - shadcn block installieren
  - shadcn lift mode
  - shadcn open in v0
  - shadcn blocks was ist das
  - shadcn blocks erklaerung
  - shadcn blocks new york
  - shadcn v4 blocks
  - shadcn blocks dashboard login sidebar signup
---

# shadcn/ui Blocks — Overview

Blocks are pre-built, composable sections that can be added directly to any project. Each block is a complete, working UI pattern built on top of shadcn/ui components.

## What are Blocks?

- Ready-to-use page sections (layouts, auth forms, dashboards, sidebars)
- Built with shadcn/ui components + Tailwind CSS
- New York v4 style (the default in shadcn v4)
- Copy-paste or install via CLI
- Fully customizable after installation

## Installation

```bash
# Install a single block by name
npx shadcn@latest add <block-name>

# Examples
npx shadcn@latest add dashboard-01
npx shadcn@latest add login-01
npx shadcn@latest add sidebar-07
npx shadcn@latest add signup-01
```

## Lift Mode

Lift Mode lets you copy individual components out of a block — without taking the entire block.

1. Open any block on [ui.shadcn.com/blocks](https://ui.shadcn.com/blocks)
2. Click the "Lift Mode" toggle in the top-right
3. Hover over a component within the block
4. Click "Copy" to copy only that component's code

Useful when you only need a specific part (e.g., the NavUser or TeamSwitcher from a sidebar block).

## Open in v0

Every block has an "Open in v0" button that opens it in [v0.dev](https://v0.dev) for AI-assisted customization and iteration.

## All 27 Blocks

### Dashboard Blocks (1)

| Block | Description |
|---|---|
| dashboard-01 | Full dashboard: AppSidebar (inset, offcanvas) + SiteHeader + SectionCards (4 KPI) + ChartAreaInteractive (area chart with time filter) + DataTable (DnD sortable, paginated, Drawer detail). Uses @tabler/icons-react, @dnd-kit, @tanstack/react-table, recharts. |

### Login Blocks (5)

| Block | Layout | Social Auth | Notes |
|---|---|---|---|
| login-01 | Centered card | Google | Standard email + password |
| login-02 | Two-column split | GitHub | Image panel on right |
| login-03 | Muted background | Apple + Google | Social buttons first |
| login-04 | Wide card + image panel | Apple + Google + Meta (icon-only) | 3 icon-only social buttons |
| login-05 | Minimal, logo-centered | None | Email only, no password field shown |

### Sidebar Blocks (16)

| Block | Variant | Key Features |
|---|---|---|
| sidebar-01 | default | VersionSwitcher dropdown + SearchForm + grouped static nav, SidebarRail |
| sidebar-02 | default | Same as sidebar-01 but sections are collapsible with ChevronRight |
| sidebar-03 | default | Logo header + SubMenu tree style, no search/version, SidebarRail |
| sidebar-04 | floating | `variant="floating"`, SubMenu tree, 19rem wide, no SidebarRail |
| sidebar-05 | default | Logo + SearchForm + Plus/Minus collapsible sections + SidebarRail |
| sidebar-06 | default | Logo + NavMain with DropdownMenu subitems + SidebarOptInForm in footer |
| sidebar-07 | default | Full app sidebar: TeamSwitcher + NavMain (collapsible, ChevronRight) + NavProjects + NavUser, `collapsible="icon"` |
| sidebar-08 | inset | NavMain with separate collapse trigger action + NavProjects + NavSecondary + NavUser |
| sidebar-09 | default | Dual sidebar: icon strip (`collapsible="icon"`) + email list panel (`collapsible="none"`), `--sidebar-width: 350px` |
| sidebar-10 | default | Notion-style: TeamSwitcher (ChevronDown) + NavMain (flat icons) + NavFavorites (emoji items) + NavWorkspaces (collapsible groups) + NavSecondary + NavActions (popover), `border-r-0` |
| sidebar-11 | default | File tree: Changes list (with M/U badges) + recursive Tree component (folders + files) |
| sidebar-12 | default | Calendar: NavUser in header + DatePicker (Calendar component) + Calendars (collapsible groups with checkboxes) + "New Calendar" footer button |
| sidebar-13 | default | Settings Dialog: Sidebar inside a Dialog component for 12 settings categories |
| sidebar-14 | right | `side="right"`, SidebarTrigger rotated 180deg, Table of Contents label |
| sidebar-15 | default | Dual layout: SidebarLeft (Notion-style like sidebar-10) + SidebarRight (Calendar like sidebar-12), 10 component files |
| sidebar-16 | default | Sticky header: SiteHeader with SearchForm + `useSidebar().toggleSidebar` button in header, `--header-height` CSS var, sidebar offset by header |

### Signup Blocks (5)

| Block | Layout | Social Auth | Notes |
|---|---|---|---|
| signup-01 | Centered card | Google | Standard name + email + password |
| signup-02 | Two-column split | GitHub | Image panel on right |
| signup-03 | Muted background | Apple + Google | Social buttons first |
| signup-04 | Wide card + image panel | Apple + Google + Meta (icon-only) | Terms of service link |
| signup-05 | Minimal, logo-centered | None | Email only |

## Related Skills

- `shadcn-blocks-dashboard` — Complete code for dashboard-01
- `shadcn-blocks-login` — Complete code for login-01..05
- `shadcn-blocks-sidebar` — Complete code for sidebar-01..16
- `shadcn-blocks-signup` — Complete code for signup-01..05
