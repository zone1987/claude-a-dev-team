# shadcn-vue Sidebar Blocks (sidebar-01 to sidebar-16)

16 ready-made sidebar page layouts from shadcn-vue. Each block is a complete page layout
consisting of `page.vue` and a set of components under `components/`. All blocks
use `SidebarProvider` + `SidebarInset` as the outer scaffold.

## Contents

- [Overview of all 16 blocks](#overview-of-all-16-blocks)
- [sidebar-01](#sidebar-01)
- [sidebar-02](#sidebar-02)
- [sidebar-03](#sidebar-03)
- [sidebar-04](#sidebar-04)
- [sidebar-05](#sidebar-05)
- [sidebar-06](#sidebar-06)
- [sidebar-07](#sidebar-07)
- [sidebar-08](#sidebar-08)
- [sidebar-09](#sidebar-09)
- [sidebar-10](#sidebar-10)
- [sidebar-11](#sidebar-11)
- [sidebar-12](#sidebar-12)
- [sidebar-13](#sidebar-13)
- [sidebar-14](#sidebar-14)
- [sidebar-15](#sidebar-15)
- [sidebar-16](#sidebar-16)

## Overview of all 16 blocks

| Block | Description | Key Features |
|-------|-------------|--------------|
| sidebar-01 | Simple sidebar with navigation in sections | VersionSwitcher, SearchForm, SidebarRail |
| sidebar-02 | Sidebar with collapsible sections (inset style) | Collapsible + ChevronRight, sticky header |
| sidebar-03 | Sidebar with static submenus | SidebarMenuSub, GalleryVerticalEnd header |
| sidebar-04 | Sidebar with static submenus (floating style) | variant="floating", 19rem width |
| sidebar-05 | Sidebar with collapsible submenus (plus/minus) | Collapsible + Plus/Minus icons, SearchForm |
| sidebar-06 | Sidebar with submenus as dropdowns | DropdownMenu for subnavigation, opt-in card |
| sidebar-07 | Sidebar collapsible to icons (icon rail) | collapsible="icon", TeamSwitcher, NavUser |
| sidebar-08 | Sidebar inset variant with secondary navigation | variant="inset", NavSecondary mt-auto |
| sidebar-09 | Double sidebar: icon rail + mail list | Two nested sidebar components, Switch |
| sidebar-10 | Sidebar with team switcher and workspaces | TeamSwitcher, NavFavorites, NavWorkspaces |
| sidebar-11 | Sidebar with collapsible file tree | Tree component, changes list, SidebarRail |
| sidebar-12 | Sidebar with calendar in the footer | Calendar, DatePicker, Calendars, NavUser header |
| sidebar-13 | Sidebar inside a dialog (settings) | Dialog + SidebarProvider, settings navigation |
| sidebar-14 | Sidebar on the right-hand side (side="right") | AppSidebar side="right", table of contents |
| sidebar-15 | Two sidebars: left + right | SidebarLeft + SidebarRight, sticky header |
| sidebar-16 | Sidebar with a fixed SiteHeader on top | SiteHeader with SearchForm + SidebarIcon button |

---

## sidebar-01

Simple sidebar with navigation grouped into sections, VersionSwitcher and SearchForm.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-01
```

**Files:**
```
sidebar-01/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── VersionSwitcher.vue
    └── SearchForm.vue
```

**Key Features:**
- `VersionSwitcher` as a dropdown in the SidebarHeader (GalleryVerticalEnd icon)
- `SearchForm` with `SidebarInput` directly below the version switcher
- Navigation in static `SidebarGroup` sections (no Collapsible)
- `SidebarRail` for the resize handle

**Complete code:** see `SIDEBAR-01-04.md`

---

## sidebar-02

Sidebar with collapsible sections, inset style, sticky header.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-02
```

**Files:**
```
sidebar-02/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── VersionSwitcher.vue
    └── SearchForm.vue
```

**Key Features:**
- `Collapsible` + `ChevronRight` rotation for each navigation group
- `SidebarGroupLabel` as `CollapsibleTrigger` (hover styles)
- Sticky `bg-background` header in `page.vue`
- Scrollable list of items in the preview

**Complete code:** see `SIDEBAR-01-04.md`

---

## sidebar-03

Sidebar with collapsing subnavigation items, inset style.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-03
```

**Files:**
```
sidebar-03/
├── page.vue
└── components/
    └── AppSidebar.vue
```

**Key Features:**
- Static `SidebarMenuSub` / `SidebarMenuSubItem` (no Collapsible)
- `GalleryVerticalEnd` logo in the header
- Compact variant without the Collapsible overhead

**Complete code:** see `SIDEBAR-01-04.md`

---

## sidebar-04

Sidebar with collapsing subnavigation items, floating style.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-04
```

**Files:**
```
sidebar-04/
├── page.vue
└── components/
    └── AppSidebar.vue
```

**Key Features:**
- `variant: "floating"` via `withDefaults`
- Custom sidebar width `--sidebar-width: 19rem`
- Sub-items without a left border: `ml-0 border-l-0 px-1.5`
- No `SidebarRail`

**Complete code:** see `SIDEBAR-01-04.md`

---

## sidebar-05

Sidebar with collapsible subnavigation items and plus/minus toggle icons.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-05
```

**Files:**
```
sidebar-05/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── SearchForm.vue
```

**Key Features:**
- `Collapsible` with `Plus`/`Minus` icons instead of ChevronRight
- `SearchForm` in the SidebarHeader
- Second section open by default (`index === 1`)

**Complete code:** see `SIDEBAR-05-08.md`

---

## sidebar-06

Sidebar with subnavigation as dropdown menus (icon rail).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-06
```

**Files:**
```
sidebar-06/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── NavMain.vue
    └── SidebarOptInForm.vue
```

**Key Features:**
- `DropdownMenu` as subnavigation (no Collapsible), `MoreHorizontal` trigger
- `SidebarOptInForm` as a card in the SidebarFooter (newsletter opt-in)
- `useMediaQuery` for the mobile/desktop dropdown position

**Complete code:** see `SIDEBAR-05-08.md`

---

## sidebar-07

Sidebar collapsible to icons (teams/navbar/NavUser).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-07
```

**Files:**
```
sidebar-07/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── NavMain.vue
    ├── NavProjects.vue
    ├── NavUser.vue
    └── TeamSwitcher.vue
```

**Key Features:**
- `collapsible: "icon"` — the sidebar collapses to an icon bar
- `TeamSwitcher` with `ChevronsUpDown` and keyboard shortcuts
- `NavMain` with tooltip support for collapsed icons
- `NavUser` avatar dropdown in the footer

**Complete code:** see `SIDEBAR-05-08.md`

---

## sidebar-08

Sidebar inset variant with nested collapsible items and document management.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-08
```

**Files:**
```
sidebar-08/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── NavMain.vue
    ├── NavProjects.vue
    ├── NavSecondary.vue
    └── NavUser.vue
```

**Key Features:**
- `variant: "inset"` for an embedded sidebar layout
- `NavSecondary` with `mt-auto` at the bottom of the SidebarContent
- `SidebarMenuAction` as the Collapsible trigger with `data-[state=open]:rotate-90`
- No TeamSwitcher, a fixed command logo header instead

**Complete code:** see `SIDEBAR-05-08.md`

---

## sidebar-09

Sidebar with a workspace/team switcher (two nested sidebars).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-09
```

**Files:**
```
sidebar-09/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── NavUser.vue
```

**Key Features:**
- Two nested `<Sidebar>` components: icon rail + mail list
- Outer sidebar: `overflow-hidden *:data-[sidebar=sidebar]:flex-row`
- Inner icon sidebar: `collapsible="none"`, fixed icon width
- `Switch` + `Label` for the "Unreads" filter, `SidebarInput` for search

**Complete code:** see `SIDEBAR-09-12.md`

---

## sidebar-10

Sidebar with a user profile in the footer (NavUser with avatar).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-10
```

**Files:**
```
sidebar-10/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── NavActions.vue
    ├── NavFavorites.vue
    ├── NavMain.vue
    ├── NavSecondary.vue
    ├── NavWorkspaces.vue
    └── TeamSwitcher.vue
```

**Key Features:**
- `TeamSwitcher` with `ChevronDown` (compact variant, `w-fit px-1.5`)
- `NavFavorites` with emoji icons and a `DropdownMenu` per item
- `NavWorkspaces` with `Collapsible` + a `Plus` action per workspace
- `NavActions` as a popover menu on the right of the header

**Complete code:** see `SIDEBAR-09-12.md`

---

## sidebar-11

Sidebar with a collapsible file tree and floating action buttons.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-11
```

**Files:**
```
sidebar-11/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── Tree.vue
```

**Key Features:**
- Recursive `Tree` component for rendering the file tree
- "Changes" group with `SidebarMenuBadge` (M/U status badges)
- `Tree` supports files and folders (Collapsible with ChevronRight)
- `SidebarRail` for resizing

**Complete code:** see `SIDEBAR-09-12.md`

---

## sidebar-12

Sidebar with a date picker in the footer.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-12
```

**Files:**
```
sidebar-12/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── Calendars.vue
    ├── DatePicker.vue
    └── NavUser.vue
```

**Key Features:**
- `DatePicker` with the shadcn-vue `Calendar` component in the SidebarContent
- `Calendars` with collapsible groups and a checkbox-like state
- `NavUser` avatar in the SidebarHeader (not the footer)
- `SidebarSeparator` between DatePicker and Calendars

**Complete code:** see `SIDEBAR-09-12.md`

---

## sidebar-13

Minimal sidebar with search, no footer (settings dialog).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-13
```

**Files:**
```
sidebar-13/
├── page.vue
└── components/
    └── SettingsDialog.vue
```

**Key Features:**
- `Dialog` + `SidebarProvider` combined for a settings modal
- Sidebar `collapsible="none"` inside the dialog
- Breadcrumb shows the current settings area
- `DialogTitle`/`DialogDescription` with `sr-only` for a11y

**Complete code:** see `SIDEBAR-13-16.md`

---

## sidebar-14

Sidebar with a sticky site header and breadcrumb (sidebar side="right").

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-14
```

**Files:**
```
sidebar-14/
├── page.vue
└── components/
    └── AppSidebar.vue
```

**Key Features:**
- `AppSidebar` with `side="right"` — sidebar on the right
- `SidebarTrigger` rotates `rotate-180` and is positioned `ml-auto`
- `AppSidebar` shows a table of contents with `SidebarMenuSub`
- Simple layout without TeamSwitcher or NavUser

**Complete code:** see `SIDEBAR-13-16.md`

---

## sidebar-15

Sidebar with two sidebars side by side (left + right).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-15
```

**Files:**
```
sidebar-15/
├── page.vue
└── components/
    ├── SidebarLeft.vue
    ├── SidebarRight.vue
    ├── TeamSwitcher.vue
    ├── NavMain.vue
    ├── NavFavorites.vue
    ├── NavWorkspaces.vue
    ├── NavSecondary.vue
    ├── NavUser.vue
    ├── Calendars.vue
    └── DatePicker.vue
```

**Key Features:**
- `SidebarLeft` (left main navigation) + `SidebarRight` (calendar)
- `SidebarRight` is `sticky top-0 h-svh border-l`, `collapsible="none"` 
- `SidebarRight` visible only at `lg:flex`
- Same components as sidebar-10 (NavFavorites, NavWorkspaces)

**Complete code:** see `SIDEBAR-13-16.md`

---

## sidebar-16

Sidebar with a floating top navigation bar (SiteHeader).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-16
```

**Files:**
```
sidebar-16/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── SiteHeader.vue
    ├── NavMain.vue
    ├── NavProjects.vue
    ├── NavSecondary.vue
    ├── NavUser.vue
    └── SearchForm.vue
```

**Key Features:**
- `SiteHeader` as a sticky `z-50` header with a `SidebarIcon` button
- `--header-height: calc(--spacing(14))` CSS variable for layout coordination
- `AppSidebar` with `top-(--header-height)` and an adjusted height
- `SearchForm` in the SiteHeader (not in the sidebar)

**Complete code:** see `SIDEBAR-13-16.md`
