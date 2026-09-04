# Premium blocks — Data Grid

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 37 entries. Do not edit by hand.

**Licence: Pro or Ultimate.** Install with `shadcn add @reui/<name>` once `REUI_LICENSE_KEY` is set.

## Contents

- [data-grid-base (7)](#data-grid-base-7)
- [data-grid-columns (5)](#data-grid-columns-5)
- [data-grid-drag-drop (4)](#data-grid-drag-drop-4)
- [data-grid-editing (5)](#data-grid-editing-5)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Editing Model](#editing-model)
- [shadcn Primitives Used](#shadcn-primitives-used)
- [ReUI Primitives Used](#reui-primitives-used)
- [Third-Party Libraries](#third-party-libraries)
- [How To Use](#how-to-use)
- [What Not To Do](#what-not-to-do)
- [Real Data Integration](#real-data-integration)
- [LLM Guidance](#llm-guidance)
- [data-grid-expansion (3)](#data-grid-expansion-3)
- [data-grid-filtering (4)](#data-grid-filtering-4)
- [data-grid-grouping (7)](#data-grid-grouping-7)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [shadcn Primitives Used](#shadcn-primitives-used)
- [ReUI Primitives Used](#reui-primitives-used)
- [Third-Party Libraries](#third-party-libraries)
- [How To Use](#how-to-use)
- [What Not To Do](#what-not-to-do)
- [Real Data Integration](#real-data-integration)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [shadcn Primitives Used](#shadcn-primitives-used)
- [ReUI Primitives Used](#reui-primitives-used)
- [Third-Party Libraries](#third-party-libraries)
- [How To Use](#how-to-use)
- [What Not To Do](#what-not-to-do)
- [Real Data Integration](#real-data-integration)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [shadcn Primitives Used](#shadcn-primitives-used)
- [ReUI Primitives Used](#reui-primitives-used)
- [Third-Party Libraries](#third-party-libraries)
- [How To Use](#how-to-use)
- [What Not To Do](#what-not-to-do)
- [Real Data Integration](#real-data-integration)
- [LLM Guidance](#llm-guidance)
- [data-grid-virtualization (2)](#data-grid-virtualization-2)

## data-grid-base (7)

### `data-grid-base-1`

Customer CRM data grid with avatar rows, balance trends, and row actions menu

Customer table for CRM and admin dashboards: search, status filter, avatar rows, balance trend tooltips, sortable resizable columns, pagination, and a row actions menu with delete confirm. ReUI DataGrid, Frame, Badge plus shadcn Avatar, DropdownMenu.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-base-2`

CRM contacts data grid with lead scoring, pinned rows, and a faceted filter builder

Contacts table for a CRM or sales pipeline: pinned rows, a multi-field Filters builder, lead-score Progress bars, sparklines, status and category Badges, and column show/hide/resize/reorder. ReUI DataGrid, Filters, Frame, Badge, shadcn Avatar.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-base-3`

CRM sales opportunities data grid with pinned priority rows and faceted pipeline filters

CRM deal pipeline table: pin top opportunities, filter by owner, stage, industry and alerts, sortable columns, circular progress rings, alert tooltips and a row actions menu. Uses ReUI DataGrid, Filters, Frame, Badge, Avatar, DropdownMenu.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-base-4`

Weekly team timesheet data grid with per-day hours and billable target tracking

People rows plus seven day cells of logged hours with progress bars, and a weekly Total with target-coverage. Team, tracked-time, and billable Select filters, a Calendar week navigator, pagination. ReUI DataGrid, Frame; shadcn Avatar, Tooltip.

Uses: `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`

### `data-grid-base-5`

Support ticket queue data grid with SLA countdown, status filters, and bulk owner assignment

Support ticket queue table in a Card: search, queue and multi-status filters, bulk assign-owner/status bar, SLA countdown cells, priority badges, close-ticket dialog. ReUI DataGrid, Badge; shadcn Card, Avatar, Select, Popover. Help desk, ticketing.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-base-6`

Members data grid with avatar rows, tabbed role and billing filters, and hover actions

Team members table for admin and settings pages: avatar cells, billing status dots, search, a tabbed Role/Billing/Auth filter menu, and hover view, edit, delete actions. ReUI DataGrid, DataGridPagination, Badge with shadcn Avatar, DropdownMenu, Tabs.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-base-7`

Modules data grid with circular progress rings, status badges, and row actions

Project modules table with per-row circular progress ring, task counts, date window, and status badges. Search, sort, status-filter, pagination, and row actions. ReUI DataGrid and Badge with shadcn DropdownMenu and InputGroup. For module manager.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`


## data-grid-columns (5)

### `data-grid-columns-1`

Workspace permissions data grid with tab-swapped scope columns and per-cell access toggles

Access review matrix whose columns swap per General, Tags, and Permissions tab, each scope a Switch toggle cell with row pinning, sorting, role filter, and search. Uses ReUI DataGrid, Frame, Tabs, Switch, Avatar. For RBAC admin, roles, team access.

Uses: `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-columns-2`

Course Catalog Data Grid with Settings Popover for Density and Column Visibility

Course catalog table with thumbnail rows, category Badge, star Rating, assignee AvatarGroup, and completion rings. Status Tabs, category Select, search, plus a Popover for density, resizable and movable columns, and column visibility. LMS admin grid.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/rating`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-columns-3`

Work queue data grid with table and card view toggle and column display controls

Work queue task tracker with tabs, table/card view switch, and a Display popover for density, sticky header, resizable and movable columns, and toggled properties. Filter row, sorting, pagination. ReUI DataGrid, Filters, Badge plus shadcn Card, Tabs.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/icon-stack`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-columns-4`

Members directory data grid with toggleable display columns and view settings popover

Member directory table for admin and people pages. A settings popover toggles display columns, sets ordering, and hides paused members. Built with ReUI DataGrid, Filters, Badge, and Rating plus Avatar, Popover, Switch, and a row-actions DropdownMenu.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/icon-stack`, `@reui/rating`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-columns-5`

CRM companies grid with a drill-down cascader that adds real columns on demand

Companies grid whose columns are added at runtime by a Cascader attribute picker: drillable groups, cross-level search, added columns checked, a footer submenu that creates an attribute by type. ReUI Filters, hide, reorder, pin.

Uses: `@reui/badge`, `@reui/cascader`, `@reui/cascader-footer`, `@reui/cascader-item`, `@reui/cascader-nav`, `@reui/cascader-types`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`


## data-grid-drag-drop (4)

### `data-grid-drag-drop-1`

Sprint backlog data grid with drag handle row reordering and live priority rank

Drag-to-prioritize task table where reordering rewrites the rank column; row handles, move-to-top/bottom and remove menu, reset, empty state. ReUI DataGrid, Frame, Badge; shadcn Avatar, DropdownMenu. Backlog, sprint, priority queue.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table-dnd-rows`, `@reui/frame`, `@reui/icon-stack`

npm: `@dnd-kit/core`, `@dnd-kit/sortable`, `@tanstack/react-table`

### `data-grid-drag-drop-2`

Routing rules data grid with drag-to-reorder priority and per-row enable switches

First-match-wins rule list where dragging a row sets precedence. Drag-drop rows, per-row Switch toggles, menu to move top/bottom or delete, reset, empty state. ReUI DataGrid, Badge; shadcn Card, DropdownMenu. For automations, routing config, rules.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table-dnd-rows`, `@reui/icon-stack`

npm: `@dnd-kit/core`, `@dnd-kit/sortable`, `@tanstack/react-table`

### `data-grid-drag-drop-3`

Fulfillment dispatch data grid with drag-to-reorder columns and saved layout presets

Warehouse wave dispatch board with draggable, resizable columns, layout preset buttons (Dispatch, Dock, Risk), reset, and a live numbered review-order strip. ReUI DataGrid, Frame, Badge, Button, status pills, capacity bars.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table-dnd`, `@reui/frame`

npm: `@dnd-kit/core`, `@dnd-kit/sortable`, `@tanstack/react-table`

### `data-grid-drag-drop-4`

Shared drive tree grid with reparenting drag and drop and tri-state folder checkboxes

Nested file storage browser on the ReUI DataGrid: a recursive folder tree with getSubRows and DataGridTableRowExpand depth indentation, file manager style tree drag and drop that reparents, dropping on a folder to go inside it and between rows to reorder, with an insertion line and a folder tint as the only feedback so no row moves for the length of a drag, the drop depth read off the pointer's horizontal travel, a closed folder reachable by a plain vertical drag and opened once it receives a row, and a carried folder taking its whole subtree, tri-state folder checkboxes that cascade to every descendant, rolled up folder size and item count, expand all and collapse all controls, a bulk selection bar, and an honest empty state.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/data-grid-table-dnd-rows`, `@reui/frame`, `@reui/icon-stack`

npm: `@dnd-kit/core`, `@dnd-kit/sortable`, `@tanstack/react-table`, `date-fns`, `sonner`


## data-grid-editing (5)

### `data-grid-editing-1`

Labels manager data grid with inline create and edit form, color picker, and drag-to-reorder rows

Manage project labels in a DataGrid: inline add and edit form with hex color picker Popover, drag-to-reorder rows, and delete confirmation. Uses ReUI DataGrid plus shadcn Button, Input, Field, AlertDialog, Empty. For label, tag, and taxonomy UIs.

Uses: `@reui/icon-stack`, `@reui/sortable`

npm: `@hookform/resolvers`, `react-hook-form`, `zod`

### `data-grid-editing-2`

Inline-editable product inventory data grid with per-cell validation and a dirty-state save bar

Edit inventory rows in place with text, number, and select cell editors, live validation, and a dirty-tracking Save / Discard bar. Search, status filter, add, duplicate, delete. ReUI DataGrid, Frame, Badge with shadcn Input, Select, Switch.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-editing-3`

Inline-editable project intake data grid with dirty-state Save and Discard bar

Editable request intake table with click-to-edit text, number, and select cells, validation, search, status and priority filters, approval Switch, and unsaved-change tracking. ReUI DataGrid, Badge; shadcn Card, Input, Select, AlertDialog.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-editing-4`

Pricing Plan Editor With Per-Row Edit Mode and Inline Validation

Per-row edit-mode data grid for pricing plans: the table is read-only until one row is checked out with Edit, its fields turn into inline inputs and selects bound to a single draft, and Save or Cancel commits or reverts that one row on its own with no global save bar and no bulk actions

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

## Purpose
A per-row edit-mode data grid for billing, revenue, and product teams that maintain a small pricing catalog: the whole table stays read-only until you check out a single plan with Edit, that row's fields become inline editors bound to one draft, and Save or Cancel commits or reverts that row on its own. There is no always-live cell editing, no global save bar, and no bulk selection. It is the row-scoped, one-at-a-time counterpart to a spreadsheet-style grid.

## Best Fit
- pricing and packaging plan editors
- rate cards, tier tables, and subscription plan management
- any admin grid where a row is a record that should be edited and committed as a unit
- catalogs where users expect an explicit Edit, then Save or Cancel, per row

## Main Pieces
- a ReUI `Frame` shell (`FrameHeader`, `FramePanel`, `FrameFooter`) whose muted backdrop frames the grid as an inset panel, with a title zone above and a summary footer below
- header controls: a Visibility filter and an Add plan action, both locked while a row is being edited
- a ReUI `DataGrid` with one row per plan; each row shows read-only values until it is checked out
- per-row edit mode: Edit turns that row into inline editors (text for name, numeric for price, seats, and trial, `Select` for audience and visibility, a live `Switch` for featured), and the action cell swaps to Save and Cancel
- a left accent bar marks the checked-out row, and every other row's Edit is disabled so only one plan edits at a time
- inline validation across the whole row: Save is blocked while any field is invalid, and each message renders under its input in a reserved slot
- a footer that summarizes plan count and public count, or names the row being edited while locked
- row actions for duplicate and delete, both opening the copy in edit mode or confirming with an `AlertDialog`

## Editing Model
- The whole grid is read-only by default. `startEdit` snapshots one plan into a single string-based `draft`; only that row renders editors, and `editingRowId` plus `isLocked` keep every other row and the toolbar disabled until the draft resolves.
- Editing handlers and the draft are threaded into cells through TanStack `table.options.meta`, so the column definitions never rebuild and the checked-out row's inputs stay controlled by the one draft.
- Numeric fields are held as raw input text in the draft so an in-progress value is never lost to an early parse; `draftToPlan` converts them back to numbers only on a validated Save.
- Save commits that row immediately into `rows` and clears the draft; Cancel discards the draft and, for a row added or duplicated in this session, removes it. Each row is its own commit; there is no working-versus-saved diff and no batch save.

## shadcn Primitives Used
- Button
- Input
- Select
- Switch
- DropdownMenu
- AlertDialog
- Tooltip

## ReUI Primitives Used
- Frame
- DataGrid
- DataGridContainer
- DataGridScrollArea
- DataGridTable
- DataGridColumnHeader
- Badge

## Third-Party Libraries
- `@tanstack/react-table` for the core row model, stable row ids, and the cell meta channel
- `sonner` for preview-safe save feedback

## How To Use
1. Replace `PLANS`, `PLAN_AUDIENCES`, and `PLAN_VISIBILITIES` with your real catalog and option sets.
2. Keep raw `price`, `seats`, and `trialDays` as numbers in the data; format only in the cells.
3. Reuse the validators (`validatePlanName`, `validatePrice`, `validateSeats`, `validateTrialDays`) or extend them per field; Save stays disabled while any returns a message.
4. Wire the `saveEdit` commit to your billing API and keep local state as the source of truth for read rows.
5. Keep the editing handlers and the draft on `table.options.meta` and read them with the `PlanTableMeta` type inside cells.

## What Not To Do
- Do not make cells always editable or add a global save bar; the point of this block is one row checked out at a time and committed on its own.
- Do not move editing state into the column factory closure; it forces a column rebuild on every keystroke. Use the meta channel.
- Do not let a second row enter edit mode while one is open; the lock keeps a single draft honest.
- Do not commit an invalid row; the validators must gate Save and the messages must render.
- Do not store the numeric drafts as numbers while typing; keep them as text and parse on Save.
- Do not copy real plan prices, seat caps, or product names into this block.

## Real Data Integration
Back each row with a stable id, name, code, audience, price, seats, trialDays, visibility, and featured flag. For server-backed editing, send one update per Save carrying just that row, reconcile the returned record into local state, and surface server validation errors through the same inline slots. Because each row commits independently, optimistic updates and per-row retries are natural.

## LLM Guidance
Use this block when the user asks for a row-edit or edit-in-place data grid, a pricing plan or tier editor, a rate card, or any table where a record is edited and saved as a unit rather than cell by cell. Preserve the per-row edit mode, the single draft on the meta channel, the one-row lock, the gating validators, the ReUI Frame shell, and the summary footer unless the brief changes the record shape or the editing model. This is deliberately distinct from the always-live-cell, global-save-bar editing grids in this family.

### `data-grid-editing-5`

Spreadsheet Task Grid With Cell Range Editing, Custom Cell Controls, and Undo

Virtualized spreadsheet task grid with cell ranges, clipboard paste, drag-to-fill, in-cell selects and date pickers, and an undo stack instead of a save bar. Built on ReUI DataGrid, Frame and Cascader. For launch runbooks and Airtable style tables.

Uses: `@reui/badge`, `@reui/cascader`, `@reui/cascader-footer`, `@reui/cascader-item`, `@reui/cascader-nav`, `@reui/cascader-types`, `@reui/data-grid`, `@reui/data-grid-cell-selection`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table-virtual`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`


## data-grid-expansion (3)

### `data-grid-expansion-1`

Task queue data grid with expandable parent rows that reveal nested sub-tasks inline

Issue tracker / task management grid where parent tasks expand to inline sub-tasks with their own checkboxes, status and assignee. Tabs, filters, settings popover for ordering and columns. ReUI DataGrid, Filters, Frame, Badge, shadcn Tabs, Checkbox.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-expansion-2`

Treasury Waterfall Data Grid with Expandable Lines and Actuals, Plan, Variance Tabs

Cash-flow grid: expandable parent lines drill into child items, Actuals/Plan/Variance tabs, Calendar month-range picker, search, plan-match and variance tooltips. For treasury, FP&A, budget, and burn dashboards. ReUI DataGrid, Frame, Badge.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`

### `data-grid-expansion-3`

Release Review Data Grid with Expandable Rows Revealing a Checklist Card Rail

Release approval queue where TanStack rows expand into a rail of check cards with rating and coverage rings. Search and status filters, View Settings popover, readiness rings, approve and escalate actions. ReUI DataGrid, Badge, Rating; shadcn Card.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/rating`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`


## data-grid-filtering (4)

### `data-grid-filtering-1`

Billing transactions data grid with multi-field filter bar and async skeleton loading

Transactions ledger grid with a Filters bar (text, searchable selects, contains/between operators), clear-all, async skeleton loading, sorting, pagination, and row actions. ReUI DataGrid, Filters, Frame, Badge. Payments, billing, fintech table.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-filtering-2`

Workflow automation library data grid with status tabs and a multi-field filter popover

Automation library table with counted status tabs (Live, Needs approval, Draft, Paused) and a Filters popover for search, owner team, delivery mode and last updated. ReUI DataGrid, Frame, Filters, Rating, Badge; shadcn Tabs, Switch, DropdownMenu.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/rating`

npm: `@tanstack/react-table`, `date-fns`, `sonner`

### `data-grid-filtering-3`

Renewals data grid with multi-field filter builder, bulk owner and stage actions

Revenue-ops renewals table with a Filters builder (account, stage, risk, window, owner), a settings popover for density and column visibility, and bulk owner/stage reassign on row select. ReUI DataGrid, Filters, Badge; shadcn Card, Select, Popover.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-filtering-4`

Renewals risk data grid with multi-field filter builder and pinned at-risk accounts

Customer success renewals queue: filter builder (account, owner, stage, signals, alerts), pinned at-risk rows, density and column settings, health Progress bars. ReUI DataGrid, Filters, Badge, shadcn Card, Popover, DropdownMenu, HoverCard.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`


## data-grid-grouping (7)

### `data-grid-grouping-1`

Roadmap Queue Data Grid Grouped by Stage with Collapsible Category Rows

Tasks grouped under expandable stage rows with owner avatars, due dates, completion rings, and signal badges. Search, signal filter, density and column toggles. ReUI DataGrid, Badge, Avatar, shadcn Popover. Roadmap, issue tracker, project board.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-grouping-2`

Account revenue grouped by region with collapsible rows and ARR subtotals

Region-grouped accounts, collapsible rows, per-region ARR and weighted NRR, grand-total footer. Health filter, search, density and column toggles. ReUI DataGrid, Frame, Badge; shadcn Button, DropdownMenu, InputGroup, Popover, Select. CRM, NRR.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-grouping-3`

Patient access cohort DataGrid with switchable grouping and outcome heatmap

Grouped DataGrid bucketing intake signals by area, booking strength, or hold risk. Color-graded heatmap cells, footer totals, hold-risk filter, cohort benchmark. ReUI DataGrid, Frame, Badge; shadcn Button, Separator. Intake triage, cohort analysis.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-grouping-4`

Bill Of Materials Tree Grid With Rolled-Up Cost And Supply Risk

Multi-level DataGrid tree mode for a bill of materials: recursive subRows at arbitrary depth, DataGridTableRowExpand depth indentation, quantity multiplied down the tree, cost and lead time rolled up, supply risk badges, a depth level control and a grand-total footer.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/icon-tile`

npm: `@tanstack/react-table`, `sonner`

## Purpose
A bill of materials cost explorer for hardware engineering and sourcing teams that need to expand a product into systems, assemblies, sub-assemblies and purchased parts, and see where cost, lead time and supply risk actually sit.

## Best Fit
- bill of materials and product structure explorers
- any hierarchy deeper than one grouping level: cost centres, chart of accounts, folder trees, org rollups, cloud spend by account and service
- costed hierarchies where a parent value must be the sum of its children
- sourcing reviews that need critical-path lead time and per-part supply status

## Main Pieces
- a `Frame` shell with title, product and revision line, three build KPIs (Build cost, Critical path, At risk), and an `Export` action
- a ReUI `DataGrid` in true tree mode: recursive `getSubRows` with no depth cap, and the `DataGridTableRowExpand` primitive supplying per-level indentation from `row.depth`
- a leaf spacer next to the expand toggle so a part and an assembly at the same depth share one label spine
- a depth control (`Collapse`, `1`, `2`, `All`) that expands the whole tree to a chosen level and reports `-1` once a row is toggled by hand
- a per-node icon map (`BOM_NODE_ICONS`) keyed by node id, falling back to `BOM_KIND_ICONS`, so a long tree does not repeat one glyph
- a supply filter whose options render the same `Badge` as the column, so the option matches the cell it selects
- rolled-up measures computed once in `buildBomRows`: effective quantity multiplied down the tree, extended cost and part count summed upward, longest lead time as the critical path, worst descendant supply status
- an extended-cost cell that pairs the rolled-up figure with a share-of-build donut and percentage on branch rows, so the expensive branch reads before any number does
- ancestor-preserving search: a matching part keeps its whole path back to the product, and a matching assembly keeps its subtree
- a `DataGridTable` grand-total footer built one cell per visible column so it tracks column toggles
- a `Display` popover with density, a part detail line, and column toggles for number, unit cost, lead time, and supply
- original cargo e-bike BOM data across four depth levels, pinned to a fixed revision date

## shadcn Primitives Used
- Button
- DropdownMenu
- Popover
- Field
- InputGroup
- Select
- Switch

## ReUI Primitives Used
- Frame
- DataGrid
- DataGridContainer
- DataGridScrollArea
- DataGridTable
- DataGridTableRowExpand
- IconTile
- Badge

## Third-Party Libraries
- `@tanstack/react-table` for recursive nested rows, controlled expansion state, stable row ids, column visibility, and flattened row rendering
- `sonner` for preview-safe action feedback

## How To Use
1. Replace `BOM_TREE` with your real product structure; nodes are self-recursive, so depth is whatever your data has.
2. Keep raw per-parent `qty`, per-unit `unitCost`, and `leadTimeDays` in the data. Every rolled-up figure derives in `buildBomRows`.
3. Preserve globally unique node ids; `getRowId` returns them flat, so expansion state stays predictable at any depth.
4. `getFirstPathExpandedState` opens the first branch at every level on first paint; swap it for `getLevelExpandedState(rows, n)` if you want a uniform depth instead.
5. Tune `TREE_INDENT` in `columns.tsx` and the leaf spacer widths together; they are a pair, and the spacer tracks the density switch because the primitive's toggle does.
6. Wire row actions and `Export` to your PLM, ERP, or sourcing flow.

## What Not To Do
- Do not hand-roll the expand toggle or a fixed `ps-8` indent; `DataGridTableRowExpand` is what makes depth beyond one level work.
- Do not cap `getSubRows` on a node kind; return `row.children` at every level or the tree silently flattens.
- Do not hard-code subtotals, the build cost, or the critical path; they derive from the leaf parts.
- Do not drop the leaf spacer beside the toggle, and keep it tracking the density switch; without it, parts and assemblies at the same depth lose their shared label spine.
- Do not band the root rows with a background; depth is carried by the indent, the icon and the label weight.
- Do not put a solid `secondary` badge in the `FrameHeader`; it sits on the `Frame` gutter tint and reads as plain text.
- Do not let search return bare leaves; a part without its ancestors is unreadable in a tree.
- Do not copy real manufacturer names, part numbers, or costs into this block.

## Real Data Integration
Back each node with a stable id, part number, name, kind, per-parent quantity, and, for purchased parts, a unit cost, lead time, supply status and supplier. For server-backed data, fetch the flat node list with a parent id and build the child arrays on the client or server before passing the tree into TanStack Table. Roll quantity down the tree and cost up it, so a sub-assembly used twice counts its parts twice. If filtering becomes server-backed, return whole ancestor paths rather than bare leaves, and preserve the same controlled expanded state and flat row id shape.

## LLM Guidance
Use this block when the user asks for a data grid whose hierarchy is deeper than one grouping level: a bill of materials, product structure, chart of accounts, cost rollup, folder tree, or any parent-child table where parent values must derive from descendants. This is the tree-mode sibling in the grouping family; `data-grid-grouping-1` is a flat headerless grouped list, `data-grid-grouping-2` a one-level region rollup with a grand total, and `data-grid-grouping-3` a grouped cohort heatmap. Preserve the recursive `getSubRows`, the `DataGridTableRowExpand` indentation with its leaf spacer, the single-pass `buildBomRows` derivation, the ancestor-preserving filter, the depth level control, the share-of-build donut, the per-node icon map, the derived grand-total footer, the portable `IconPlaceholder` mappings, and the semantic Badge usage unless the brief explicitly changes the hierarchy or the measures.

### `data-grid-grouping-5`

Reporting Hierarchy Tree Grid With Span Of Control And Cascading Selection

Multi-level DataGrid tree mode for an HR org chart: recursive subRows at arbitrary depth, DataGridTableRowExpand indentation, org size and open roles rolled up each reporting line, tree-cascading row selection with a corrected tri-state checkbox, sticky header, depth control and a bulk selection bar.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

## Purpose
A reporting-hierarchy explorer for people teams and leaders who need to walk an org from the chief executive down to an individual contributor, and see span of control, open roles and who needs attention roll up every reporting line.

## Best Fit
- org charts and reporting-line browsers
- headcount planning and span-of-control review
- any people hierarchy where a manager's row must summarise their whole line
- bulk people operations that act on a team rather than a person

## Main Pieces
- a `Frame` shell with company and snapshot line, four org KPIs (Headcount, Layers, Avg span, Open roles), and an `Export` action
- a ReUI `DataGrid` in tree mode: recursive `getSubRows` with no depth cap and `DataGridTableRowExpand` supplying per-level indentation from `row.depth`
- tree-cascading row selection: checking a manager selects their entire reporting line, including collapsed reports
- a block-level `TreeRowSelect` that fixes the primitive checkbox, which is not tri-state on a tree in either direction
- a selection bar that appears only while a line is selected, with team-level verbs
- a sticky header over a bounded scroll area, so the column names survive a fully expanded org
- root-only default expansion: the leadership line is on screen and every branch below it is a deliberate click
- a depth control (`1`, `2`, `3`, `All`) that expands the whole tree to a chosen level
- rolled-up measures computed once in `buildOrgRows`: org size, direct reports, open roles, layers below, and people needing attention
- a span-of-control cell that reads direct reports large and the whole line small, and a dash for individual contributors
- ancestor-preserving search where a manager is tested on their own merits, because in an org tree the branch is a person
- a `DataGridTable` footer built one cell per visible column so it tracks column toggles
- original 18-person org across five levels, with portraits and a fixed snapshot date

## shadcn Primitives Used
- Button
- Checkbox
- DropdownMenu
- Popover
- Field
- InputGroup
- Select
- Switch
- ToggleGroup
- Avatar

## ReUI Primitives Used
- Frame
- DataGrid
- DataGridContainer
- DataGridScrollArea
- DataGridTable
- DataGridTableRowExpand
- DataGridTableRowSelectAll
- Badge

## Third-Party Libraries
- `@tanstack/react-table` for recursive nested rows, controlled expansion and selection state, stable row ids, column visibility, and flattened row rendering
- `sonner` for preview-safe action feedback

## How To Use
1. Replace `ORG_TREE` with your real reporting lines; nodes are self-recursive, so depth is whatever your org has.
2. Keep raw per-person values in the data. Every rolled-up figure derives in `buildOrgRows`.
3. Preserve globally unique person ids; `getRowId` returns them flat, so expansion and selection stay predictable at any depth.
4. `getRootExpandedState` opens the root and nothing else; swap it for `getLevelExpandedState(rows, n)` for a uniform depth.
5. Tune `TREE_INDENT` in `columns.tsx` and the leaf spacer widths together; they are a pair, and the spacer tracks the density switch because the primitive's toggle does.
6. Wire the row actions, the selection bar and `Export` to your HRIS.

## What Not To Do
- Do not ship the primitive `DataGridTableRowSelect` on a tree; it renders a manager solid-checked after one report is unchecked, and blank when every report was checked individually. Derive from `getIsAllSubRowsSelected()`.
- Do not count a selection with `getSelectedRowModel().rows`; that model is nested and drops a selected report whose manager is unselected. Use `flatRows`.
- Do not set `headerSticky` without bounding the scroll area; the viewport grows to content, so the header never sticks.
- Do not declare `meta.expandedContent` anywhere in a tree block; it shares `row.getIsExpanded()` with the tree, so every expanded manager grows a detail row inside their own subtree, and hiding the column does not switch it off.
- Do not call `table.toggleAllRowsExpanded()`; it writes the boolean `true`, which makes every row including leaves report as expanded.
- Do not cap `getSubRows` on a node kind; return `row.children` at every level or the tree silently flattens.
- Do not copy real employee names, photos, or reporting lines into this block.

## Real Data Integration
Back each person with a stable id, name, title, level, department, location, employment status, hire date, and the open roles attached directly to them. For server-backed data, fetch the flat person list with a manager id and build the child arrays on the client or server before passing the tree into TanStack Table. Sum counts upward and take the deepest branch for layers, so a manager's row always describes their whole line. If filtering becomes server-backed, return whole manager paths rather than bare people, and preserve the same controlled expanded and selection state shape.

## LLM Guidance
Use this block when the user asks for an org chart, a reporting hierarchy, a people tree, or any parent-child table of humans where a manager summarises their reports. This is the people tree in the grouping family; `data-grid-grouping-1` is a flat headerless grouped list, `data-grid-grouping-2` a one-level region rollup, `data-grid-grouping-3` a grouped cohort heatmap, and `data-grid-grouping-4` a bill-of-materials tree keyed on parts rather than people. Preserve the recursive `getSubRows`, the `DataGridTableRowExpand` indentation with its density-aware leaf spacer, the block-level `TreeRowSelect`, the flat-row selection count, the bounded scroll area under the sticky header, the single-pass `buildOrgRows` derivation, the ancestor-preserving filter, the root-only default expansion, and the semantic Badge usage unless the brief explicitly changes the hierarchy or the measures.

### `data-grid-grouping-6`

Editorial Production Desk With Per Section Tables And Repeated Headers

Sectioned DataGrid layout for an editorial story pipeline: one independent DataGrid per group so every stage repeats its own column header row, a switchable Stage, Desk or Issue grouping dimension, tinted stage bands with counts and an add button, AvatarGroup bylines, flag placement badges and asset and note count chips.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

## Purpose
An editorial production desk for magazine and newsroom teams who need to see every commissioned story at once, split into the stage of the pipeline it sits in, without losing the column names as they scan down the page.

## Best Fit
- editorial and content production pipelines
- any workflow list where each stage should read as its own table with its own header row
- kanban-style stage grouping for teams who want a table rather than a board
- lists whose grouping dimension changes per user, not per page

## Main Pieces
- a `Frame` shell with publication and snapshot line, three desk KPIs (Stories, Unchecked, Ready), and a `New story` action
- a `Group by` `ToggleGroup` (Stage, Desk, Issue) that rebuilds the sections rather than re-sorting one table
- one section card per group, each a tinted band (stage dot, label, count badge, add button) over its own `DataGrid`
- a separate `useTable` instance per section (TanStack Table v9, `features: dataGridFeatures`), so the column header row repeats for every group
- one column array built once per view and passed to every section, which is what keeps the columns aligned across separate tables
- rows carrying story title with a slug, a truncated angle, an `AvatarGroup` byline that rolls into an `AvatarGroupCount` at three, a filed date, a publish date, a placement badge, an assets count chip and a desk-notes count chip
- desk and placement filters whose placement options render the same badge the column shows
- every group in the current dimension renders, including empty ones, so a filter narrows the desk without collapsing its shape
- original 13-story fixture across four stages, four desks and two issues, pinned to a fixed production date

## shadcn Primitives Used
- Button
- DropdownMenu
- InputGroup
- ToggleGroup
- Avatar
- AvatarGroup

## ReUI Primitives Used
- Frame
- DataGrid
- DataGridContainer
- DataGridTable
- DataGridColumnHeader
- Badge

## Third-Party Libraries
- `@tanstack/react-table` v9 for one table instance per section and stable row ids
- `sonner` for preview-safe action feedback

## How To Use
1. Replace `STORIES` and `BYLINES` with your own records; the grouping dimensions read straight off `stage`, `desk` and `issue`.
2. Add a value to any of those unions to get a new section, with no other change.
3. Build the column array once in the view and pass the same instance to every section; never rebuild it per section.
4. Give every column an explicit `size` and leave `columnsResizable` off.
5. Wire the row actions, the per-section add button and `New story` to your CMS.

## What Not To Do
- Do not rebuild the column array per section, and do not let the column sizes exceed the narrowest section's content box; separate tables only line up while they share one array, one explicit size per column, and resizing stays off.
- Do not add `DataGridPagination` to a section. Nothing here needs it, and the primitive's last-row border rule keys off a `:has()` match on the element directly wrapping a grid and its pagination, so adding it changes that section's last-row border for no gain.
- Do not drop the per-section `DataGridContainer` or its `DataGridScrollArea`. The container is `w-full overflow-hidden`, so without the scroll area a narrow viewport clips the right-hand columns with no way to reach them.
- Do not turn the group bands into table rows; the repeated header row is the point of this layout, and a band row would force the header off.
- Do not copy real publications, staff names, or unpublished story titles into this block.

## Real Data Integration
Back each story with a stable id, a slug, a title, a one-line angle, a stage, a desk, an issue, a placement, byline ids, an ISO filed date and publish date each paired with a display label, and the asset and note counts. Keep the dates as ISO plus a pre-formatted label so nothing is built at render time. For server-backed data, fetch the flat story list and group it on the client; `buildSections` already returns every group in the dimension's own order, including empty ones.

## LLM Guidance
Use this block when the user asks for a grouped list whose sections must each be their own table with their own column header, or for a stage pipeline rendered as tables rather than a board. This is the sectioned grid in the grouping family; `data-grid-grouping-1` is one flat table with group rows and the header suppressed, `data-grid-grouping-2` a one-level region rollup, `data-grid-grouping-3` a cohort heatmap, `data-grid-grouping-4` a bill-of-materials tree, and `data-grid-grouping-5` an HR org tree. Preserve the one-DataGrid-per-section mounting, the shared module-scope column array, the absence of pagination, the per-section `DataGridContainer`, the switchable grouping dimension, the tinted stage band with its count and add button, and the semantic Badge usage unless the brief explicitly changes the grouping model.

### `data-grid-grouping-7`

Delivery Board With Per Stage Column Headers And Segmented Completion Meters

Studio delivery board grouped by stage: one DataGrid per stage so every stage repeats its full column header row, sharing one sort and selection state. Client brand tiles, a segmented completion meter, crew AvatarGroup, milestone dates. Search, stage filter, density and column toggles, per-stage select all.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`


## data-grid-virtualization (2)

### `data-grid-virtualization-1`

Virtualized data grid with infinite scroll and bulk row actions

Transaction table that virtualizes rows and loads on scroll. Search, sorting, filter dropdowns, column visibility, bulk export/refund. ReUI DataGrid, Frame, Badge, Filters; shadcn Button, InputGroup, Popover, Switch. Payments ledger, admin panel.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/data-grid-table-virtual`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `data-grid-virtualization-2`

Virtualized shipment exception queue with infinite scroll

Exception queue over 8,000 virtualized rows with infinite-scroll paging, row selection, bulk assign/release, faceted filters, search, and sorting. ReUI DataGrid, Frame; shadcn Button, Separator, Tooltip. Operations dashboard, shipment tracking.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/data-grid-table-virtual`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

