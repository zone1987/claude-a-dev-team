---
name: shadcn-vue-blocks-dashboard
description: >
  shadcn-vue Dashboard- und Products-Blocks (dashboard-01, products-01) — vollstaendige
  Dashboard-Seite mit Sidebar, Datentabelle, Flaechendiagramm und KPI-Cards; Products-Tabelle
  mit Filter. Triggers: "shadcn-vue dashboard block", "shadcn vue dashboard", "dashboard layout vue",
  "admin dashboard vue", "analytics dashboard shadcn", "products table vue", "datentabelle vue shadcn",
  "kpi cards vue", "area chart vue", "draggable table vue"
---

# shadcn-vue Blocks: dashboard-01 & products-01

Diese Skill-Referenz enthält den vollständigen Code für zwei fertige shadcn-vue Blocks:

- **dashboard-01** — eine komplette Admin-Dashboard-Seite mit Sidebar-Navigation, KPI-Cards, interaktivem Flächendiagramm und einer drag-&-drop-fähigen Datentabelle mit Paginierung.
- **products-01** — eine Produkttabelle mit Status-Badges, Kategoriefiltern, Preis- und Statusfilter-Selects sowie Paginierung.

Beide Blocks nutzen shadcn-vue UI-Komponenten (Button, Badge, Card, Table, Tabs, Select, Sidebar, Dropdown u.a.) und Tabler Icons bzw. Lucide Icons.

---

## dashboard-01: Dashboard with Sidebar, Data Table, Area Chart, Section Cards

Der `dashboard-01`-Block liefert eine vollständige Dashboard-Seite bestehend aus:

- **AppSidebar** — Collapsible Offcanvas-Sidebar mit Logo, Hauptnavigation (NavMain), Dokument-Links (NavDocuments), sekundärer Navigation (NavSecondary) und Nutzer-Footer (NavUser).
- **NavMain** — Hauptnavigationsgruppe mit "Quick Create"-Button und Icon-Links (Dashboard, Lifecycle, Analytics, Projects, Team).
- **NavDocuments** — Sidebar-Gruppe "Documents" mit Dropdown-Aktionen (Open, Share, Delete) pro Eintrag.
- **NavSecondary** — Sekundäre Links (Settings, Get Help, Search) am unteren Sidebar-Rand.
- **NavUser** — Avatar + Name + Email im Sidebar-Footer, öffnet Dropdown mit Account, Billing, Notifications, Logout.
- **SiteHeader** — Sticky Header mit SidebarTrigger, Separator und Seitentitel "Documents".
- **SectionCards** — Responsive Grid mit 4 KPI-Cards: Total Revenue, New Customers, Active Accounts, Growth Rate — jeweils mit Trendpfeil-Badge und Footer-Text.
- **ChartAreaInteractive** — Flächendiagramm (Desktop vs. Mobile Visitors) mit Zeitraumfilter (90d / 30d / 7d), basiert auf `@unovis/vue`.
- **DataTable** — TanStack Vue Table mit Drag-&-Drop-Sortierung (dnd-kit-vue), Tabs (Outline / Past Performance / Key Personnel / Focus Documents), Spalten-Visibility-Menü, Paginierung und Zeilenauswahl. Zod-Schema als exportierter Typ.
- **DraggableRow** — Wrapper-Komponente für draggable Tabellenzeilen via `useSortable`.
- **DragHandle** — Grip-Icon-Button als Drag-Handle via `useSortableContext`.

### Installation

```bash
npx shadcn-vue@latest add dashboard-01
```

### Dateien (12)

```
dashboard-01/
├── page.vue
└── components/
    ├── AppSidebar.vue
    ├── ChartAreaInteractive.vue
    ├── DataTable.vue
    ├── DraggableRow.vue
    ├── DragHandle.vue
    ├── NavDocuments.vue
    ├── NavMain.vue
    ├── NavSecondary.vue
    ├── NavUser.vue
    ├── SectionCards.vue
    └── SiteHeader.vue
```

Vollständiger Code: `references/dashboard-01.md`

---

## products-01: Products Table

Der `products-01`-Block liefert eine einsatzbereite Produkttabelle mit:

- **Tabs** — All Products / In Stock / Low Stock / Archived / Add Product.
- **Filter-Selects** — Category, Price-Range, Status.
- **Tabelle** — Checkbox-Selektion, Produkt-Name, Preis, Lagerbestand, Status-Badge (grün/orange), Hinzufügedatum, Row-Actions-Dropdown (Edit / Delete).
- **Pagination** — Seitennummerierung mit Ellipsis.

### Installation

```bash
npx shadcn-vue@latest add products-01
```

### Dateien (2)

```
products-01/
├── page.vue
└── components/
    └── ProductsTable.vue
```

Vollständiger Code: `references/products-01.md`
