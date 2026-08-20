# shadcn/ui Dashboard Block (dashboard-01)

Complete application dashboard with sidebar, data table (drag-and-drop), interactive area chart, and KPI section cards.

## Installation

```bash
npx shadcn@latest add dashboard-01
```

## Component Structure

```
dashboard-01/
  page.tsx                          # Root: SidebarProvider + AppSidebar (inset) + SiteHeader + content
  components/
    app-sidebar.tsx                 # AppSidebar: NavMain + NavDocuments + NavSecondary + NavUser
    nav-main.tsx                    # Flat icon list + "Quick Create" primary button
    nav-documents.tsx               # Documents group with dropdown actions
    nav-secondary.tsx               # Simple icon link list (Settings, Help, Search)
    nav-user.tsx                    # Avatar dropdown: Account/Billing/Notifications
    site-header.tsx                 # Fixed header: SidebarTrigger + title + GitHub link
    section-cards.tsx               # 4 KPI cards with container queries
    chart-area-interactive.tsx      # Interactive area chart with ToggleGroup time range
    data-table.tsx                  # Full data table with DnD, pagination, Drawer detail
  data.json                         # Sample data (68 rows) for DataTable
```

## Key Dependencies

- `@tabler/icons-react` — icons throughout (not lucide-react)
- `@dnd-kit/core`, `@dnd-kit/sortable`, `@dnd-kit/modifiers`, `@dnd-kit/utilities` — drag-and-drop in DataTable
- `@tanstack/react-table` — DataTable
- `recharts` — AreaChart
- `sonner` — toast notifications in DataTable
- `zod` — DataTable row schema

## Layout CSS Variables

```tsx
// page.tsx SidebarProvider style
style={
  {
    "--sidebar-width": "350px",
    "--header-height": "calc(var(--spacing) * 12)",
  } as React.CSSProperties
}
```

## Reference Files

- [dashboard-01-core.md](`DASHBOARD-01-CORE.md`) — page.tsx, app-sidebar.tsx, nav-main.tsx, nav-documents.tsx, nav-secondary.tsx, nav-user.tsx, site-header.tsx, section-cards.tsx
- [dashboard-01-chart-table.md](`DASHBOARD-01-CHART-TABLE.md`) — chart-area-interactive.tsx, data-table.tsx, data.json
