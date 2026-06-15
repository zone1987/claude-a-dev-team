---
name: shadcn-vue-blocks-sidebar
description: >
  shadcn-vue Sidebar-Blocks (sidebar-01 bis sidebar-16) — 16 fertige Sidebar-Layouts mit
  Navigation, Collapsible-Gruppen, Icons, Team-Switcher, User-Footer, Suchleiste und mehr.
  Triggers: "shadcn-vue sidebar block", "shadcn vue sidebar layout", "sidebar navigation vue",
  "sidebar block installieren", "app sidebar vue", "navigation sidebar shadcn",
  "sidebar mit icons vue", "sidebar collapsible vue", "sidebar team switcher",
  "sidebar floating vue", "seitenleiste vue shadcn"
---

# shadcn-vue Sidebar Blocks (sidebar-01 bis sidebar-16)

16 fertige Sidebar-Seitenlayouts aus shadcn-vue. Jeder Block ist ein vollstaendiges Seitenlayout
bestehend aus `page.vue` und einer Reihe von Komponenten unter `components/`. Alle Bloecke
verwenden `SidebarProvider` + `SidebarInset` als aeusseres Geruest.

## Uebersicht aller 16 Bloecke

| Block | Beschreibung | Key Features |
|-------|-------------|--------------|
| sidebar-01 | Einfache Sidebar mit Navigation in Abschnitten | VersionSwitcher, SearchForm, SidebarRail |
| sidebar-02 | Sidebar mit einklappbaren Abschnitten (inset style) | Collapsible + ChevronRight, sticky Header |
| sidebar-03 | Sidebar mit statischen Submenus | SidebarMenuSub, GalleryVerticalEnd Header |
| sidebar-04 | Sidebar mit statischen Submenus (floating style) | variant="floating", 19rem Breite |
| sidebar-05 | Sidebar mit einklappbaren Submenus (Plus/Minus) | Collapsible + Plus/Minus Icons, SearchForm |
| sidebar-06 | Sidebar mit Submenus als Dropdowns | DropdownMenu fuer Subnavigation, Opt-In Card |
| sidebar-07 | Sidebar kollabierbar zu Icons (icon-rail) | collapsible="icon", TeamSwitcher, NavUser |
| sidebar-08 | Sidebar Inset-Variante mit sekundaerer Navigation | variant="inset", NavSecondary mt-auto |
| sidebar-09 | Doppelte Sidebar: Icon-Rail + Mail-Liste | Zwei verschachtelte Sidebar-Komponenten, Switch |
| sidebar-10 | Sidebar mit Team-Switcher und Workspaces | TeamSwitcher, NavFavorites, NavWorkspaces |
| sidebar-11 | Sidebar mit einklappbarem Dateibaum | Tree-Komponente, Changes-Liste, SidebarRail |
| sidebar-12 | Sidebar mit Kalender im Footer | Calendar, DatePicker, Calendars, NavUser Header |
| sidebar-13 | Sidebar innerhalb eines Dialogs (Settings) | Dialog + SidebarProvider, Settings-Navigation |
| sidebar-14 | Sidebar rechtsseitig (side="right") | AppSidebar side="right", Table-of-Contents |
| sidebar-15 | Zwei Sidebars: links + rechts | SidebarLeft + SidebarRight, sticky Header |
| sidebar-16 | Sidebar mit festem SiteHeader oben | SiteHeader mit SearchForm + SidebarIcon Button |

---

## sidebar-01

Einfache Sidebar mit Navigation gruppiert nach Abschnitten, VersionSwitcher und SearchForm.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-01
```

**Dateien:**
```
sidebar-01/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── VersionSwitcher.vue
    └── SearchForm.vue
```

**Key Features:**
- `VersionSwitcher` als Dropdown im SidebarHeader (GalleryVerticalEnd Icon)
- `SearchForm` mit `SidebarInput` direkt unter dem Version-Switcher
- Navigation in statischen `SidebarGroup`-Abschnitten (kein Collapsible)
- `SidebarRail` fuer Resize-Handle

**Vollstaendiger Code:** siehe `references/sidebar-01-04.md`

---

## sidebar-02

Sidebar mit einklappbaren Abschnitten, inset style, sticky Header.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-02
```

**Dateien:**
```
sidebar-02/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── VersionSwitcher.vue
    └── SearchForm.vue
```

**Key Features:**
- `Collapsible` + `ChevronRight`-Rotation fuer jede Navigationsgruppe
- `SidebarGroupLabel` als `CollapsibleTrigger` (hover-Styles)
- Sticky `bg-background` Header in `page.vue`
- Scrollbare Liste von Items in der Vorschau

**Vollstaendiger Code:** siehe `references/sidebar-01-04.md`

---

## sidebar-03

Sidebar mit kollabierenden Subnavigations-Items, inset style.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-03
```

**Dateien:**
```
sidebar-03/
├── page.vue
└── components/
    └── AppSidebar.vue
```

**Key Features:**
- Statische `SidebarMenuSub` / `SidebarMenuSubItem` (kein Collapsible)
- `GalleryVerticalEnd` Logo im Header
- Kompakte Variante ohne Collapsible-Overhead

**Vollstaendiger Code:** siehe `references/sidebar-01-04.md`

---

## sidebar-04

Sidebar mit kollabierenden Subnavigations-Items, floating style.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-04
```

**Dateien:**
```
sidebar-04/
├── page.vue
└── components/
    └── AppSidebar.vue
```

**Key Features:**
- `variant: "floating"` via `withDefaults`
- Benutzerdefinierte Sidebar-Breite `--sidebar-width: 19rem`
- Sub-Items ohne linken Rahmen: `ml-0 border-l-0 px-1.5`
- Kein `SidebarRail`

**Vollstaendiger Code:** siehe `references/sidebar-01-04.md`

---

## sidebar-05

Sidebar mit einklappbaren Subnavigations-Items und Plus/Minus Toggle-Icons.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-05
```

**Dateien:**
```
sidebar-05/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── SearchForm.vue
```

**Key Features:**
- `Collapsible` mit `Plus`/`Minus` Icons statt ChevronRight
- `SearchForm` im SidebarHeader
- Zweiter Abschnitt standardmaessig offen (`index === 1`)

**Vollstaendiger Code:** siehe `references/sidebar-05-08.md`

---

## sidebar-06

Sidebar mit Subnavigation als Dropdown-Menus (icon-rail).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-06
```

**Dateien:**
```
sidebar-06/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── NavMain.vue
    └── SidebarOptInForm.vue
```

**Key Features:**
- `DropdownMenu` als Subnavigation (kein Collapsible), `MoreHorizontal` Trigger
- `SidebarOptInForm` als Card im SidebarFooter (Newsletter Opt-In)
- `useMediaQuery` fuer mobile/desktop Dropdown-Position

**Vollstaendiger Code:** siehe `references/sidebar-05-08.md`

---

## sidebar-07

Sidebar kollabierbar zu Icons (Teams/Navbar/NavUser).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-07
```

**Dateien:**
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
- `collapsible: "icon"` — Sidebar kollabiert zu Icon-Leiste
- `TeamSwitcher` mit `ChevronsUpDown` und Keyboard-Shortcuts
- `NavMain` mit Tooltip-Support fuer kollabierte Icons
- `NavUser` Avatar-Dropdown im Footer

**Vollstaendiger Code:** siehe `references/sidebar-05-08.md`

---

## sidebar-08

Sidebar Inset-Variante mit verschachtelten einklappbaren Items und Dokumenten-Verwaltung.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-08
```

**Dateien:**
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
- `variant: "inset"` fuer eingebettetes Sidebar-Layout
- `NavSecondary` mit `mt-auto` am unteren Ende des SidebarContent
- `SidebarMenuAction` als Collapsible-Trigger mit `data-[state=open]:rotate-90`
- Kein TeamSwitcher, stattdessen fester Command-Logo-Header

**Vollstaendiger Code:** siehe `references/sidebar-05-08.md`

---

## sidebar-09

Sidebar mit Workspace/Team-Switcher (doppelte verschachtelte Sidebars).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-09
```

**Dateien:**
```
sidebar-09/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── NavUser.vue
```

**Key Features:**
- Zwei verschachtelte `<Sidebar>`-Komponenten: Icon-Rail + Mail-Liste
- Aeussere Sidebar: `overflow-hidden *:data-[sidebar=sidebar]:flex-row`
- Innere Icon-Sidebar: `collapsible="none"`, feste Icon-Breite
- `Switch` + `Label` fuer "Unreads"-Filter, `SidebarInput` fuer Suche

**Vollstaendiger Code:** siehe `references/sidebar-09-12.md`

---

## sidebar-10

Sidebar mit Benutzerprofil im Footer (NavUser mit Avatar).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-10
```

**Dateien:**
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
- `TeamSwitcher` mit `ChevronDown` (kompakte Variante, `w-fit px-1.5`)
- `NavFavorites` mit Emoji-Icons und `DropdownMenu` pro Item
- `NavWorkspaces` mit `Collapsible` + `Plus`-Action per Workspace
- `NavActions` als Popover-Menu rechts im Header

**Vollstaendiger Code:** siehe `references/sidebar-09-12.md`

---

## sidebar-11

Sidebar mit einklappbarem Dateibaum und schwebenden Aktionsschaltflaechen.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-11
```

**Dateien:**
```
sidebar-11/
├── page.vue
└── components/
    ├── AppSidebar.vue
    └── Tree.vue
```

**Key Features:**
- Rekursive `Tree`-Komponente fuer Dateibaum-Darstellung
- "Changes"-Gruppe mit `SidebarMenuBadge` (M/U Status-Badges)
- `Tree` unterstuetzt Dateien und Ordner (Collapsible mit ChevronRight)
- `SidebarRail` fuer Resize

**Vollstaendiger Code:** siehe `references/sidebar-09-12.md`

---

## sidebar-12

Sidebar mit Datumsauswahl im Footer.

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-12
```

**Dateien:**
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
- `DatePicker` mit shadcn-vue `Calendar`-Komponente im SidebarContent
- `Calendars` mit Collapsible-Gruppen und Checkbox-artigem Status
- `NavUser` Avatar im SidebarHeader (nicht Footer)
- `SidebarSeparator` zwischen DatePicker und Calendars

**Vollstaendiger Code:** siehe `references/sidebar-09-12.md`

---

## sidebar-13

Sidebar minimal mit Suche, kein Footer (Settings-Dialog).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-13
```

**Dateien:**
```
sidebar-13/
├── page.vue
└── components/
    └── SettingsDialog.vue
```

**Key Features:**
- `Dialog` + `SidebarProvider` kombiniert fuer Settings-Modal
- Sidebar `collapsible="none"` innerhalb des Dialogs
- Breadcrumb zeigt aktuellen Settings-Bereich
- `DialogTitle`/`DialogDescription` mit `sr-only` fuer A11y

**Vollstaendiger Code:** siehe `references/sidebar-13-16.md`

---

## sidebar-14

Sidebar mit stickigem Site-Header und Breadcrumb (sidebar side="right").

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-14
```

**Dateien:**
```
sidebar-14/
├── page.vue
└── components/
    └── AppSidebar.vue
```

**Key Features:**
- `AppSidebar` mit `side="right"` — Sidebar rechts
- `SidebarTrigger` rotiert `rotate-180` und positioniert `ml-auto`
- `AppSidebar` zeigt Table-of-Contents mit `SidebarMenuSub`
- Einfaches Layout ohne TeamSwitcher oder NavUser

**Vollstaendiger Code:** siehe `references/sidebar-13-16.md`

---

## sidebar-15

Sidebar mit zwei Sidebars nebeneinander (links + rechts).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-15
```

**Dateien:**
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
- `SidebarLeft` (linke Hauptnavigation) + `SidebarRight` (Kalender)
- `SidebarRight` ist `sticky top-0 h-svh border-l`, `collapsible="none"` 
- `SidebarRight` nur auf `lg:flex` sichtbar
- Gleiche Komponenten wie sidebar-10 (NavFavorites, NavWorkspaces)

**Vollstaendiger Code:** siehe `references/sidebar-13-16.md`

---

## sidebar-16

Sidebar mit schwebender Top-Navigationsleiste (SiteHeader).

**Installation:**
```bash
npx shadcn-vue@latest add sidebar-16
```

**Dateien:**
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
- `SiteHeader` als sticky `z-50` Header mit `SidebarIcon`-Button
- `--header-height: calc(--spacing(14))` CSS-Variable fuer Layout-Koordination
- `AppSidebar` mit `top-(--header-height)` und angepasster Hoehe
- `SearchForm` im SiteHeader (nicht in der Sidebar)

**Vollstaendiger Code:** siehe `references/sidebar-13-16.md`
