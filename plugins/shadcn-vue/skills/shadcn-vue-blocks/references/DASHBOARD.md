# shadcn-vue Blocks: dashboard-01 & products-01

This skill reference contains the complete code for two ready-made shadcn-vue blocks:

- **dashboard-01** — a complete admin dashboard page with sidebar navigation, KPI cards, an interactive area chart and a drag-and-drop data table with pagination.
- **products-01** — a product table with status badges, category filters, price and status filter selects, plus pagination.

Both blocks use shadcn-vue UI components (Button, Badge, Card, Table, Tabs, Select, Sidebar, Dropdown and others) and Tabler Icons or Lucide Icons.

---

## dashboard-01: Dashboard with Sidebar, Data Table, Area Chart, Section Cards

The `dashboard-01` block delivers a complete dashboard page consisting of:

- **AppSidebar** — collapsible offcanvas sidebar with logo, main navigation (NavMain), document links (NavDocuments), secondary navigation (NavSecondary) and user footer (NavUser).
- **NavMain** — main navigation group with a "Quick Create" button and icon links (Dashboard, Lifecycle, Analytics, Projects, Team).
- **NavDocuments** — sidebar group "Documents" with dropdown actions (Open, Share, Delete) per entry.
- **NavSecondary** — secondary links (Settings, Get Help, Search) at the bottom edge of the sidebar.
- **NavUser** — avatar + name + email in the sidebar footer, opens a dropdown with Account, Billing, Notifications, Logout.
- **SiteHeader** — sticky header with SidebarTrigger, Separator and the page title "Documents".
- **SectionCards** — responsive grid with 4 KPI cards: Total Revenue, New Customers, Active Accounts, Growth Rate — each with a trend arrow badge and footer text.
- **ChartAreaInteractive** — area chart (Desktop vs. Mobile Visitors) with a time range filter (90d / 30d / 7d), based on `@unovis/vue`.
- **DataTable** — TanStack Vue Table with drag-and-drop sorting (dnd-kit-vue), tabs (Outline / Past Performance / Key Personnel / Focus Documents), column visibility menu, pagination and row selection. Zod schema as an exported type.
- **DraggableRow** — wrapper component for draggable table rows via `useSortable`.
- **DragHandle** — grip icon button as a drag handle via `useSortableContext`.

### Installation

```bash
npx shadcn-vue@latest add dashboard-01
```

### Files (12)

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

Complete code: `DASHBOARD-01.md`

---

## products-01: Products Table

The `products-01` block delivers a ready-to-use product table with:

- **Tabs** — All Products / In Stock / Low Stock / Archived / Add Product.
- **Filter selects** — Category, price range, status.
- **Table** — checkbox selection, product name, price, stock level, status badge (green/orange), date added, row actions dropdown (Edit / Delete).
- **Pagination** — page numbering with ellipsis.

### Installation

```bash
npx shadcn-vue@latest add products-01
```

### Files (2)

```
products-01/
├── page.vue
└── components/
    └── ProductsTable.vue
```

Complete code: `DASHBOARD-PRODUCTS-01.md`
