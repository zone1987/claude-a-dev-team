# Premium blocks — Solutions

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 65 entries. Do not edit by hand.

**Licence: Pro or Ultimate.** Install with `shadcn add @reui/<name>` once `REUI_LICENSE_KEY` is set.

## Contents

- [solution-agents (10)](#solution-agents-10)
- [solution-ai-ops (9)](#solution-ai-ops-9)
- [solution-analytics (9)](#solution-analytics-9)
- [solution-billing (9)](#solution-billing-9)
- [solution-bookings (3)](#solution-bookings-3)
- [solution-crm (6)](#solution-crm-6)
- [solution-files (1)](#solution-files-1)
- [solution-inventory (11)](#solution-inventory-11)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [Reused Blocks](#reused-blocks)
- [Layout Grid](#layout-grid)
- [LLM Guidance](#llm-guidance)
- [solution-users (7)](#solution-users-7)

## solution-agents (10)

### `solution-agents-1`

AI Agent Operations Dashboard with Run Queue, Throughput Chart and Incident Timeline

Full-page console to monitor autonomous agent runs, approval backlogs, tool reliability and incidents. KPI cards, throughput chart, incident timeline, filterable run queue with row actions. ReUI Frame, DataGrid, Badge; shadcn Chart. Agent ops.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/timeline`

npm: `@tanstack/react-table`, `lucide-react`, `recharts`, `sonner`

### `solution-agents-2`

Agent Run Queue with Collapsible Status Groups and Attention Filters

Triage table for agent runs in collapsible Running, Waiting, Failed, Completed groups with search, attention filter, density toggle, and per-row actions. ReUI DataGrid, Badge; shadcn Button, Avatar, Switch. For agent ops dashboards, run monitoring.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`

### `solution-agents-3`

Agent Run Detail with Inline Step Trace and Editable Settings Panel

Single-page detail for one agent run: header with live actions, step trace with per-step tool calls and latency, plus a row-editable settings panel. ReUI Frame, Timeline, Badge, Alert; shadcn Avatar, Button. Use: run debugging, ops monitoring.

Uses: `@reui/alert`, `@reui/badge`, `@reui/frame`, `@reui/timeline`

npm: `lucide-react`, `sonner`

### `solution-agents-4`

Agent Tool Access Matrix with Approval Routing and Run Policies

Per-agent tool governance: a DataGrid sets each tool's access mode (Auto Run, Approval, Blocked), rate limit, and approver, plus run-policy switches with save or discard. ReUI DataGrid, Filters, Frame; shadcn Switch, Select. Permissions, guardrails.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `solution-agents-5`

Agent Action Approval Inbox with Risk-Tiered Queue and Bulk Approve or Reject

Full-page console for triaging pending agent actions: filter by risk and status, bulk approve or reject, and inspect payloads in a detail sheet. ReUI DataGrid, Badge, Timeline; shadcn Sheet, Select, Checkbox. Approval inbox, human-in-the-loop queue.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/timeline`

npm: `@tanstack/react-table`, `sonner`

### `solution-agents-6`

Agent Playbook Builder Wizard with Live Summary Card and Tool Allowlist

Five-step wizard to build an agent playbook: trigger, condition rows, tool allowlist, approval gate, then review and publish with a live summary card. ReUI Stepper, Alert, Badge; shadcn Card, Select, RadioGroup. For workflow automation, approvals.

Uses: `@reui/alert`, `@reui/badge`, `@reui/stepper`

npm: `sonner`

### `solution-agents-7`

Failed Agent Run Triage Board with Detail Sheet and Retry Ladder

Triage failed agent runs in a data grid with metric cards, then open a detail sheet tabbed into error, retry attempts, and payload. ReUI Data Grid, Badge, Alert, Timeline; shadcn Sheet, Card, Button, Tabs. Agent ops, error monitoring, run dashboards.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/timeline`

npm: `@tanstack/react-table`, `sonner`

### `solution-agents-8`

Agent Evaluation Report with Pass Rate Trend and Release Markers

Read-mostly nightly agent eval report: pass rate trend with release markers, per-suite progress, and a regressions table comparing two releases. Period selector, regressions-only toggle, export. ReUI Frame, Badge, Filters; shadcn Chart, Progress.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`, `recharts`, `sonner`

### `solution-agents-9`

Agent memory manager with scope rail and confidence-scored entries grid

Curate the facts agents retain: a scope rail with per-scope counts beside a confidence-scored grid, with pin, forget, and filter actions. Uses ReUI DataGrid, Badge, Filters, Frame; shadcn Button, Avatar. For agent ops and memory management pages.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/icon-stack`

npm: `@tanstack/react-table`, `sonner`

### `solution-agents-10`

Agent run-configuration settings form with picker, validated timeout, and locked policy row

Configure how an agent runs: pick an agent, set reasoning model, concurrency, validated timeout and autonomy, toggle sandbox and retry policies plus one locked PII row. ReUI Frame, Badge; shadcn Select, Button, InputGroup, Switch. Agent settings page

Uses: `@reui/badge`, `@reui/frame`, `@reui/icon-tile`

npm: `sonner`


## solution-ai-ops (9)

### `solution-ai-ops-1`

AI Operations Dashboard with Provider Failover Timeline and Token Activity Chart

Full-page LLM ops dashboard for provider health, token usage, routing rules, and safety drift: metric cards, failover timeline, token activity chart, routing grid. ReUI Frame, Timeline, DataGrid, Badge; shadcn Button, Chart. Admin panel, monitoring.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/timeline`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `lucide-react`, `recharts`, `sonner`

### `solution-ai-ops-2`

AI model provider settings page with priority and fallback routing rows

Manage AI model provider connections, route priority, fallbacks, and endpoint health with status badges and connect, pause, test, save actions. ReUI Badge, Frame; shadcn Button, Dialog, Dropdown-Menu, Item, Select, Switch. Provider and routing setup.

Uses: `@reui/badge`, `@reui/frame`

npm: `sonner`

### `solution-ai-ops-3`

Tabbed AI Ops Prompt Registry Queue with Table and Card View Toggle

AI operations prompt queue with tabs, owner/risk/status filters, table-and-card view switch, display settings, export, and row actions to advance review. Uses ReUI DataGrid, Filters; shadcn Tabs, Card, Button, Select. Operator console, review queue.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/icon-stack`

npm: `@tanstack/react-table`, `sonner`

### `solution-ai-ops-4`

Prompt Editor with Configuration and Evaluation Details

Full-page prompt editor with tabbed sections for overview, text, safety, evaluations, and access. Status badges, form fields, timeline, save-discard workflow. ReUI Badge; shadcn Button, Tabs. For AI ops dashboards and model operator portals.

Uses: `@reui/alert`, `@reui/badge`, `@reui/timeline`

npm: `@base-ui/react`, `lucide-react`, `sonner`

### `solution-ai-ops-5`

AI Ops Routing Rules Settings with Risk-Tiered Policy Toggle Grid

Full-page AI routing controls: per-route policy toggle grid, provider fallback Select with validation, and reset confirmation. ReUI Frame, Badge; shadcn Switch, Select, Dialog, Dropdown Menu. AI platform ops, model settings, risk management.

Uses: `@reui/badge`, `@reui/frame`

npm: `sonner`

### `solution-ai-ops-6`

AI Feature Flags Data Grid with Rollout Stage Tabs and Inline Enable Switches

Manage AI feature flags by rollout stage with tabs, owner and segment filters, inline enable switches, detail sheet, archive dialog, operations Kanban. ReUI DataGrid, Badge, Filters, Kanban; shadcn Sheet, Switch, Tabs. Flag console, rollout admin.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/kanban`, `@reui/rating`

npm: `@tanstack/react-table`, `date-fns`, `sonner`

### `solution-ai-ops-7`

AI Safety Policy Builder Wizard with Stepper Rail and Policy Rule Coverage Table

Four-step wizard to configure, validate, and review AI model safety policies: enforcement modes, risk tiers, evaluators, and a rule coverage table. ReUI Stepper, Alert, Badge; shadcn Card, Table, Select, Dialog. Use for AI governance, model risk.

Uses: `@reui/alert`, `@reui/badge`, `@reui/stepper`

npm: `sonner`

### `solution-ai-ops-8`

AI Token Spend Ledger Data Grid with Budget Status and CSV Export

Full-page grid auditing token usage and cost by model provider and prompt, with filtering, sorting, CSV export, a row-detail sheet, and budget-alert toggles. ReUI DataGrid, Filters, Frame, Badge; shadcn Button, Switch, Sheet. AI ops cost tracking.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `solution-ai-ops-9`

AI Ops Cost Dashboard with Spend Pace Chart and Tabbed Provider Cost Grid

Tracks AI model spend, token volume, and budget alerts with KPI cards, a spend-vs-budget line chart, provider mix breakdown, and a tabbed cost-event grid. ReUI Badge, Data Grid; shadcn Card, Tabs, Chart. For AI ops, cost monitoring, budgets.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `recharts`


## solution-analytics (9)

### `solution-analytics-1`

Product Analytics Dashboard with Scored Signal Backlog

Tracks activation, retention, adoption, and backlog risk. Scored signal grid with sparklines, filtering, reporting ranges, health overview, and export. ReUI Badge, Frame, Data-Grid; shadcn Button, Chart, Progress. Product analytics, SaaS dashboard.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `recharts`, `sonner`

### `solution-analytics-2`

Feature Adoption Analytics Report with Trend Chart and Scored Feature Grid

Read-only product analytics report comparing feature adoption by segment and period. Overview metrics, trend chart, and scored feature grid with sparklines and filtering. ReUI DataGrid, Badge, Frame; shadcn Chart, Select, Progress. SaaS usage report.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `recharts`, `sonner`

### `solution-analytics-3`

Activation Funnel Report with Conversion Area Chart and Segment Mix

Tracks workspaces from signup to week 4 retention via a stacked funnel chart, segment mix pie, and risk-flagged cohort grid with period, segment, and export filters. ReUI DataGrid, Badge, Frame; shadcn Button, Select, Tabs. Funnel and cohort reports.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `recharts`

### `solution-analytics-4`

Cohort Retention Analytics Report with Retention Curve Chart and Cohort Table

Period-over-period retention report: 4W-16W curve chart with period tabs, cohort health notes, and a sortable cohort grid by segment and event. ReUI Frame, DataGrid, Badge; shadcn Chart, Tabs, Item. For product analytics, retention, cohort views.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `recharts`

### `solution-analytics-5`

Event Explorer - Analytics Dashboard with Chart Grid

Event catalog with health metrics grid and dense data table. Filtering, sorting, bulk owner reassignment, detail drawer. Built with DataGrid, Select, Checkbox, InputGroup, Button. Use for event audits, catalog management, and quality assessment.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `recharts`, `sonner`

### `solution-analytics-6`

Segment validation workspace with health metrics, review calendar, and weekly rule coverage grid

Analytics segment-validation dashboard with health metric cards and sparklines, a review schedule calendar, and a filterable weekly rule coverage grid. ReUI Frame, DataGrid, Badge; shadcn Tabs, Calendar, Select. For segment management, reporting.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`

### `solution-analytics-7`

A/B Experiment Report with Ship Decision, Evidence Grid and Guardrails

Read-only experiment analysis: ship-decision verdict card, tabbed evidence grid with period/segment filters and export, rollout plan and guardrails. ReUI Badge, DataGrid; shadcn Card, Tabs, Button. For A/B test reports, variant lift analysis.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`

### `solution-analytics-8`

Single-Metric Analytics Detail Page with Target-Tracked Trend Chart

Single-metric detail page: health-badge header, four-up KPI rail, trend chart against a target line, cohort breakdown, changes timeline. ReUI Frame, Badge, Timeline; shadcn Chart, Select, Progress. For analytics dashboards, KPI tracking, metrics.

Uses: `@reui/badge`, `@reui/frame`, `@reui/timeline`

npm: `recharts`, `sonner`

### `solution-analytics-9`

Alert Rules Settings Form with Tabs and Validation

Tabbed settings form for configuring alert thresholds, delivery channels, quiet hours, and escalation with validation and save/discard. ReUI Alert, Badge; shadcn Button, Card, Tabs, Select, Switch. Analytics settings, configuration form.

Uses: `@reui/alert`, `@reui/badge`

npm: `sonner`


## solution-billing (9)

### `solution-billing-1`

Billing operator workspace with invoice ledger and past due recovery

Review the billing position and recover overdue invoices. Pairs a statement summary card and past due alert with a filterable invoice ledger. Uses ReUI Alert, Badge, DataGrid, Filters; shadcn Card, Button. For accounts receivable and billing pages.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/timeline`

npm: `@tanstack/react-table`, `sonner`

### `solution-billing-2`

Plan and pricing catalog editor with tiered plan tiles and status toggles

Plan catalog editor for billing teams to manage tiered plans, pricing, billing intervals, seats, entitlements, add-ons, and active/draft/archived status. ReUI Frame, Badge, Alert; shadcn Item, Button, Switch. For subscription and pricing settings.

Uses: `@reui/alert`, `@reui/badge`, `@reui/frame`

npm: `sonner`

### `solution-billing-3`

Subscription Management Workspace with Quick-Action Cards and Lifecycle Grid

Manage subscriptions across active, trialing, past due, and canceled states. Quick-action cards with budget progress lead a filterable, searchable grid with row actions. ReUI Frame, DataGrid; shadcn Tabs, Select, Avatar. Billing ops, revenue recovery

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/rating`

npm: `@tanstack/react-table`, `lucide-react`, `sonner`

### `solution-billing-4`

Customer Billing Account Detail with Tabbed Invoices, Subscription, and Activity Rail

Single-account billing detail: identity header, tabbed invoice history, subscription, and payment methods beside a scoped activity timeline. shadcn Card, Tabs, Table, Button; ReUI Badge. Account detail, billing management, subscription page.

Uses: `@reui/badge`, `@reui/icon-stack`, `@reui/timeline`

npm: `lucide-react`, `sonner`

### `solution-billing-5`

Four-step invoice builder wizard with a live receipt-style review preview

Guided invoice composer: pick a customer, edit line items with per-line tax and discount, then send. Live receipt review with draft and sent states. ReUI Stepper, Alert, Badge; shadcn Card, Table, Combobox, Select. For billing and invoicing pages.

Uses: `@reui/alert`, `@reui/badge`, `@reui/stepper`

npm: `sonner`

### `solution-billing-6`

Expandable Dunning Queue for SaaS Failed Payment Recovery

Sortable, filterable dunning queue for SaaS billing operators to recover failed charges. Expands inline to retry timeline. Features ReUI DataGrid, Frame, Filters; shadcn Button, Separator. Payment recovery, dunning list, failed billing.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `solution-billing-7`

Metered usage event ledger with tree meter scope selection

Audit metered events by meter and period with tree sidebar nav filtering, date picker, and export. ReUI DataGrid, Filters, Frame, Badge; shadcn Button, Calendar, Breadcrumb. Usage based billing, consumption tracking, subscription auditing.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/icon-stack`, `@reui/tree`, `@reui/use-copy-to-clipboard`

npm: `@headless-tree/core`, `@headless-tree/react`, `@tanstack/react-table`, `date-fns`, `react-day-picker`, `sonner`

### `solution-billing-8`

Subscription Plan Change Wizard with Live Proration Preview

Stepped wizard to move a subscription to a new tier with a proration rail recomputing credit, charge, and due-today as plan and timing change. ReUI Stepper, Badge, Alert; shadcn Card, Button, RadioGroup, Item, Avatar. For plan upgrades, downgrades.

Uses: `@reui/alert`, `@reui/badge`, `@reui/stepper`

### `solution-billing-9`

Coupon and promotion manager with inline redemption rule editor

Manage coupon and promo codes; each row expands inline to edit discount type, duration, redemption limits, and eligible plans. ReUI Badge, Frame; shadcn Button, Collapsible, Dialog, Select. Discount admin, promo codes, billing settings.

Uses: `@reui/badge`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `sonner`


## solution-bookings (3)

### `solution-bookings-1`

Salon Front-Desk Booking Dashboard with Appointment Queue and Chair Capacity

Front-desk surface for daily salon scheduling: KPI cards, a chair-capacity donut, and a searchable appointment queue with status badges and no-show tracking. ReUI Frame, Badge, DataGrid; shadcn Avatar. Booking dashboard, appointment scheduler.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/timeline`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`, `sonner`

### `solution-bookings-2`

Salon Appointment Calendar with Day/Week Views and Double-Book Alerts

Full-page booking calendar for salon operators: month grid with category dots, Day/Week toggle, staff filter, double-book conflict alerts. ReUI Alert, Badge; shadcn Calendar, Card, Select, ToggleGroup. Schedule, staff roster, appointment booking.

Uses: `@reui/alert`, `@reui/badge`, `@reui/icon-stack`

npm: `react-day-picker`, `sonner`

### `solution-bookings-3`

Appointment Detail Sheet with Deposit Payment and Booking Timeline

Inset right sheet over an appointment list showing client, service, staff, deposit-progress payment, internal note, and a booking activity timeline. Uses ReUI Badge, Timeline; shadcn Avatar, Button, Item, Progress, ScrollArea, Sheet, Textarea.

Uses: `@reui/badge`, `@reui/timeline`

npm: `sonner`


## solution-crm (6)

### `solution-crm-1`

Sales Pipeline CRM Dashboard with Metric Charts and Open-Deals Grid

Sales pipeline command center tracking pipeline value, forecast, and win rate via metric charts, plus a dense open-deals grid for search, sort, stage filters, and row actions. ReUI Badge, DataGrid; shadcn Card, Button, Avatar. CRM sales dashboard.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `recharts`, `sonner`

### `solution-crm-2`

CRM deal pipeline kanban board with risk signals and confidence scores

Sales pipeline board tracking deals across six stages by risk signal, value, close date, confidence, and owner. ReUI Kanban, Badge, IconStack; shadcn Card, Avatar, Progress, Button. Deal pipeline, CRM dashboard, sales board.

Uses: `@reui/badge`, `@reui/icon-stack`, `@reui/kanban`

npm: `@base-ui/react`

### `solution-crm-3`

CRM Contacts Grid with Bulk Owner Assignment and Detail Sheet

Full-page contacts directory for sales teams. Sort and filter rows, multi-select for bulk owner assignment or add-to-list, open a contact detail sheet. ReUI DataGrid, Filters, Frame, Badge; shadcn Button, Avatar, Sheet, Select. CRM, leads, accounts.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `solution-crm-4`

CRM Deal Detail Sheet with Inline Stage Select and Win Probability

Right-side sheet to inspect and advance a deal: inline stage Select drives win-probability Progress, deal team avatars, activity Timeline, and tasks. ReUI Badge, Timeline; shadcn Sheet, Select, Avatar, Progress. For pipeline and deal management.

Uses: `@reui/badge`, `@reui/timeline`

npm: `sonner`

### `solution-crm-5`

CRM Activity Timeline with Day Buckets, Type and Owner Filters

Chronological sales activity log grouped by day buckets (Today, Yesterday, This week) with type and owner filters, collapsible detail panels, and outcome badges. ReUI Badge, Frame, Timeline; shadcn ToggleGroup, Select. Activity log, deal tracker.

Uses: `@reui/badge`, `@reui/frame`, `@reui/icon-stack`, `@reui/timeline`

npm: `lucide-react`, `sonner`

### `solution-crm-6`

Five-Step CRM CSV Import Wizard with Column Mapping and Validation

Guides bulk CSV uploads into CRM contacts and deals via column mapping, row validation counts, and duplicate handling. ReUI Frame, Stepper, Badge, Alert; shadcn Select, RadioGroup, Table, Switch. Data import, bulk upload, onboarding wizard.

Uses: `@reui/alert`, `@reui/badge`, `@reui/frame`, `@reui/stepper`, `@reui/use-file-upload`

npm: `sonner`


## solution-files (1)

### `solution-files-1`

Drive Explorer with Folder Tree Rail and Switchable List or Grid Views

Drive Explorer is a full-height file manager module for browsing team storage: a headless-tree folder rail with secondary scope links and a storage meter, a folders band above the browse surface, a ReUI DataGrid list with owner, type, size and modified columns, a switchable card grid, a view settings popover for density, sort and visible properties, bulk selection actions, and separate empty states for an empty folder and a filtered miss.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/icon-stack`, `@reui/icon-tile`, `@reui/timeline`, `@reui/tree`, `@reui/use-file-upload`

npm: `@headless-tree/core`, `@headless-tree/react`, `@tanstack/react-table`, `sonner`


## solution-inventory (11)

### `solution-inventory-1`

SKU Inventory Operations Dashboard with Stock-Health Bar and Tabbed SKU Grid

Full-page inventory ops dashboard: KPI stat tiles, stock-health status bar, velocity chart, low-stock alerts, and a tabbed, filterable SKU table. ReUI Frame, Badge, DataGrid; shadcn Button, Tabs, Chart. For warehouse, stock, and ecommerce ops.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `recharts`, `sonner`

### `solution-inventory-2`

Full-Page SKU Inventory Ledger with Stock Health Metrics

Stock ledger with KPI and health bar, filterable SKU grid (search, category, supplier, location, status), row actions, bulk operations, and detail sheet. ReUI DataGrid, Frame, Badge; shadcn Button, Select. Inventory management and warehouse tracking.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/timeline`

npm: `@tanstack/react-table`, `sonner`

### `solution-inventory-3`

Low Stock Reorder Queue with At-Risk Value KPI and Bulk Create PO DataGrid

At-risk value KPI and urgency bar over a searchable, filterable SKU DataGrid with multi-select bulk Create PO and a reorder detail sheet. ReUI DataGrid, Frame, Badge; shadcn Button, Select, InputGroup. For procurement and inventory dashboards.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `solution-inventory-4`

Purchase Order Receiving Page with Line-Item Tracking and Activity Timeline

Full-page purchase order detail for receiving stock against a PO: supplier and terms form, line-item receive table with backorders, costs, totals, and a note timeline. ReUI Badge, Timeline; shadcn Card, Table, Input. PO receiving, inventory intake.

Uses: `@reui/badge`, `@reui/timeline`

npm: `date-fns`, `sonner`

### `solution-inventory-5`

Shop Activity Dashboard

Inventory dashboard: 4 KPI stat tiles + inventory velocity bar chart + top categories list + tabbed shop activity table (Products / Recent activities / Orders). Composed by adapting existing application blocks (stats-1, chart-29, list-1) into a single shop-management surface.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/rating`

npm: `@tanstack/react-table`, `recharts`

## Purpose
The landing dashboard for a shop / inventory admin panel. Surfaces the four numbers a stock manager wants first thing in the morning (Total SKUs, Stock value, Low stock, Out of stock), then a category-by-category velocity bar chart, a ranked Top categories list, and a tabbed table that switches between Products, Recent activities, and Orders, so the operator can drill from headline metrics into the specific rows that need action without leaving the page.

The block is a composition of existing application blocks rather than fresh code: stat tiles are the `stats-1` pattern with inventory data; the chart card is `chart-29` (inventory velocity) tuned for category turnover; the right-side list is `list-1` rebuilt as Top categories; the tabbed table uses shadcn `Tabs` + `Table` to keep the table light while reusing all the project's primitives.

## Best Fit
- shop admin landing page for a single-store ecommerce dashboard
- warehouse manager command center where stock health, velocity, and live activity all sit on one screen
- back-office inventory review for buyers who alternate between Products, stock movements, and Orders
- demo / handoff surface that showcases how the registry's primitives compose into a real shop dashboard

## Main Pieces
- **Stats row** (`Stats`, adapted from `application/stats/stats-1`): 4-up `Frame` + `FramePanel` tiles with title, overflow menu (View report / Add alert / Export CSV / Pin to dashboard / Remove), large value, delta `Badge` (success-light when healthy, destructive-light when worsening), separator, and "Vs last month" subtitle. The `positive` flag is independent of `delta` sign so the Out-of-stock tile correctly shows a green badge with a down arrow.
- **Velocity chart** (`VelocityChart`, adapted from `application/chart/chart-29`): `Frame` + `FramePanel` with a recharts `BarChart` using the hatched-bar shape and dotted background pattern from chart-29. Title carries a `success-light` Badge with the trailing-period trend.
- **Top categories** (`TopCategories`, adapted from `application/list/list-1`): `Frame` + `FramePanel` with a header (title + "View all" button), separator, then a list of category rows. Each row uses the `Item` + `ItemMedia` icon container from list-1, a value, and a `success-light` / `destructive-light` trend `Badge`.
- **Shop activity tabs** (`ActivityTabs`): `Frame` + `FramePanel` containing shadcn `Tabs variant="line"` with three panels:
  - **Products**, SKU, name, category, on-hand, reorder point, status `Badge` (in stock / low stock / out of stock), and an Adjust action
  - **Recent activities**, kind icon (received / sold / adjusted / transferred / returned), product, signed delta, source (PO #, order #, reason), actor, and a relative timestamp
  - **Orders**, order id, customer, items, total, status `Badge` (fulfilled / processing / backorder / cancelled), and placed-at relative time

## Reused Blocks
- `application/stats/stats-1`, entire stat tile pattern (component scaffold, dropdown menu structure, delta `Badge` logic), data replaced with inventory metrics
- `application/chart/chart-29`, entire chart card pattern (custom hatched bar shape, dotted background pattern, custom tooltip), data replaced with category velocity
- `application/list/list-1`, entire list pattern (Frame + FramePanel + `Item` icon container + trend `Badge`), data and labels replaced with Top categories

## Layout Grid
- Outer container: `max-w-7xl flex-col gap-6` so the entire dashboard breathes at 28px gaps
- Charts row: `grid-cols-1 @4xl:grid-cols-3` with the velocity chart spanning `col-span-2` at `@4xl`, the top categories list filling the remaining third. Collapses cleanly to a stacked column below the container breakpoint.
- Tabbed table: full-width below the charts row

## LLM Guidance
Keep the four-piece composition (`Stats` / `VelocityChart` / `TopCategories` / `ActivityTabs`). Add a new section by appending it to the dashboard root container with the same `gap-6` rhythm. When replacing demo data, keep the discriminated unions (`StockStatus`, `ActivityKind`, `OrderStatus`) so the `*_VARIANT` and `*_LABEL` lookups stay total. The Tabs use `variant="line"` to read as a soft section separator, not as a heavy chrome control, switch to default tabs if the page already has other navigation context. For the source patterns see `application/stats/stats-1`, `application/chart/chart-29`, and `application/list/list-1`.

### `solution-inventory-6`

Stock Health Grid

Inventory overview block: total asset value KPI + segmented stock health bar (in stock / low / out of stock) above a filterable product DataGrid with search, date range, category and supplier filters, row selection, and pagination.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`

## Purpose
A buyer/operator's inventory dashboard in a single screen. Pairs a hero KPI strip (total asset value + product mix by stock health) with a filterable product DataGrid so the operator can read overall stock health and drill into individual SKUs without leaving the page.

## Best Fit
- shop admin inventory landing page with a single dense product table
- warehouse manager mid-screen view that surfaces stock health and per-SKU flow at once
- procurement workspace where Stock Planner is the next action after reviewing stock status

## Main Pieces
- **StatsHeader** (adapted from `application/stats/stats-3`): Frame + FramePanel split into two columns - Total Asset Value on the left, product count + segmented stock health bar + emerald/amber/destructive legend on the right.
- **InventoryDataGrid** (adapted from `application/data-grid/data-grid-10`): Frame + FramePanel containing a toolbar (search, date range button, category Select, supplier Select, Stock Planner CTA), the ReuiDataGrid (`DataGrid` + `DataGridScrollArea` + `DataGridTable`), and `DataGridPagination` inside a `FrameFooter`. Columns: row select, Product Info, Stock Flow (on-hand / inbound / outbound with icons), Delta badge, Price, Category, Supplier (initial chip + name), Updated, row actions menu.

## Reused Blocks
- `application/stats/stats-3` - segmented progress bar pattern for the stock health strip, adapted to inventory states (in stock / low / out of stock).
- `application/data-grid/data-grid-10` - toolbar + DataGrid + pagination chrome, adapted with inventory-specific columns and filters.

## Layout Grid
Single column at any breakpoint. Header card spans the full width above the table; both share the `max-w-7xl` container and 24px (`gap-6`) vertical rhythm.

## LLM Guidance
Keep the two-piece composition (`StatsHeader` + `InventoryDataGrid`). When extending, add new toolbar controls inside the toolbar `div`, and new columns in `productColumns` in `columns.tsx`. The stacked bar reads percentages from `inventorySummary` in `data.ts` - swap that single object when wiring real data. The supplier chip uses the `SUPPLIERS` lookup to map a name to an initial + tailwind background class; add new suppliers to that map rather than inlining classes in cells.

### `solution-inventory-7`

Stock Planner

Stock planner sheet: a wide right-anchored sheet built on the sheet-6 shell. Header carries title, product name + Live badge, SKU/created/updated meta, and the Customer View / Remove / Edit Product action cluster. Scrollable two-column body pairs left-side Inventory KPIs, an Analytics card with two sparkline area charts, and a Variants table (size/color/price/availability/on-hand) with a right-side product gallery + thumbnails + spec list (category, fit, color swatches, sizes, star rating + reviews).

Uses: `@reui/badge`, `@reui/frame`, `@reui/rating`

npm: `recharts`

## Purpose
A detail surface the operator opens from any product list (e.g. the solutions/inventory/solution-inventory-6 grid) to review inventory health, sales velocity, and per-variant stock without leaving the parent screen. The sheet is wider than the standard sheet-6 (72rem) so the two-column dashboard layout fits comfortably without horizontal scroll.

## Best Fit
- side-drawer detail view triggered from a product DataGrid row
- buyer/operator review screen pairing stock KPIs with sales velocity and variant breakdown
- merch-ops handoff sheet where the same actions (Customer View / Remove / Edit Product) live in both header and footer

## Main Pieces
- **Sheet shell** (adapted from `application/sheet/sheet-6`): right-anchored `Sheet` with inset rounded corners, no built-in close button, `SheetHeader` carrying the title row + a secondary row with product name/badge/meta and the action cluster, `ScrollArea` body, `SheetFooter` mirroring the action cluster.
- **Inventory** (shadcn `Card`): grid of 5 inline KPIs - Status badge, In Stock count, Delta badge, Velocity, Updated By.
- **Analytics** (shadcn `Card`): two stat blocks - Sales price + Sales - each with a trend `Badge` and a recharts `AreaChart` sparkline (`h-[88px]`, no axes, monotone curve with vertical gradient fill).
- **Variants** (shadcn `Card` + `Table`): rows for each size/color combination with price, availability, on-hand, and per-row edit action. Header carries a `Manage Variants` link styled with the standard `ECOMMERCE_LINK_CLASS_NAME`.
- **Product gallery**: square hero image + 5-thumbnail strip (selected state via 2px ring) with selection state held in component state.
- **Spec list**: `<dl>` with Category, Fit, Colors (color swatches), Sizes (EU/US/UK), Rating (`Rating` primitive + reviews link).

## Reused Blocks
- `application/sheet/sheet-6` - sheet anatomy: trigger button, custom-width `SheetContent`, sticky `SheetHeader`/`SheetFooter`, `ScrollArea` body
- `ecommerce/category-card/category-card-1..6` - `ECOMMERCE_LINK_CLASS_NAME` convention for hover-underline links
- `application/chart/chart-17` - `AreaChart` + gradient sparkline pattern (adapted with no tooltip + no axes for compact KPI display)

## Layout Grid
- Sheet width: `w-[min(72rem,calc(100vw-2rem))]` - never exceeds 1152px, never less than viewport - 2rem padding
- Inner body: `grid-cols-1 lg:grid-cols-12` with left section spanning `col-span-7` and the gallery/specs spanning `col-span-5`; stacks on smaller widths
- Inventory KPIs: `grid-cols-2 sm:grid-cols-3 lg:grid-cols-5` so KPIs reflow on narrower body widths

## LLM Guidance
Keep the three-piece left column (`InventorySection` / `AnalyticsSection` / `VariantsSection`) and two-piece right column (`ProductMedia` / `ProductSpecs`). To add another KPI to the Inventory card, extend the `stats` array - the grid will reflow automatically. To swap or add charts, edit the trend data arrays in `data.ts`; the `Sparkline` component takes any `[{ day, value }]` shape. The trend `Badge` reuses success-light / destructive-light tones - pass a `direction` prop or compute it from the value sign. The action cluster (`HeaderActions`) is intentionally rendered twice (header + footer) - keep both in sync by editing the single component. The sheet defaults to `open: true` so the preview reads at full state; in production wire `open`/`onOpenChange` to the parent grid's row trigger.

### `solution-inventory-8`

Stock Detail

Per-product stock detail sheet: a wide right-anchored Sheet (inset, sheet-6 anatomy) with a Current Stock + Reorder Now row, an Inventory Rules Frame (threshold / safe / reorder / lead-time inputs + status / delta / velocity / next-reorder / updated-by stats + Auto Reorder switch in the header), a Shipping Frame (Custom / Carrier tabs + package name, type, weight, dimensions + save-package checkbox), and a right-side product summary (image, name, description, SKU / category / rating / price). Footer: Print Label · Cancel · Save.

Uses: `@reui/badge`, `@reui/frame`, `@reui/rating`

## Purpose
A focused per-SKU stock editor opened from any product list. Pairs the inventory reorder rules and shipping configuration on the left with a product summary on the right so the operator can review what they are editing without losing context.

## Best Fit
- per-product stock & reorder-rules editor opened from an inventory DataGrid
- shipping configuration sheet for a fulfilment workflow where label print + save are the primary actions
- merch-ops drawer that combines inventory thresholds, shipping package config, and a product reference card on one surface

## Main Pieces
- **Sheet shell** (adapted from `application/sheet/sheet-6` and `solutions/inventory/solution-inventory-7`): right-anchored Sheet with inset rounded corners, no built-in close, `SheetHeader` carrying the title row + product name + SKU/created/updated meta, `ScrollArea` body, and a `SheetFooter` with `Print Label` on the left and `Cancel` / `Save` on the right.
- **Current Stock** (`Field` + `Input` + `Button`): editable stock value with a `Reorder Now` outline button on the right.
- **InventoryRulesSection** (ReUI `Frame` + `FrameHeader` + `FramePanel`, `dense spacing="sm"`, `shadow-none!`): header carries title + Auto Reorder `Switch`; panel contains a 2x2 grid of inputs (Threshold Qty, Safe Stock Qty, Reorder Qty, Lead Time with `InputGroupAddon` `days` suffix) followed by a 5-column stats strip (Status badge, Delta badge, Velocity, Next Reorder, Updated By).
- **ShippingSection** (Frame + Tabs in the header): `Custom Package` / `Carrier Package` line-style tabs; panel contains Package Name input, a 2-column row (Package Type Select + Total Weight `InputGroupAddon` `kg`), a 4-column dimension row (Length / Width / Height inputs + unit `Select` aligned to the input baseline via grid `items-end`), and a `Save package for future orders` `Checkbox`.
- **ProductPanel** (right column): product image card, name + description, then a small `<dl>` with SKU (mono), Category, `Rating` primitive, Price.

## Reused Blocks
- `application/sheet/sheet-6` - sheet anatomy: trigger + custom-width `SheetContent` + sticky header / scrollable body / sticky footer
- `solutions/inventory/solution-inventory-7` - responsive body pattern (single ScrollArea below `lg`, two side-by-side ScrollAreas above `lg` joined by a vertical `Separator`), `Frame dense spacing="sm"` + `FrameHeader` `py-1.5!` + `FramePanel` `shadow-none!` conventions, header SKU/created/updated meta with reui-dot separators, and the wide sheet width `w-[min(60rem,calc(100vw-2rem))]`.

## Layout Grid
- Sheet width: `w-[min(60rem,calc(100vw-2rem))]` - never exceeds 960px, never narrower than viewport - 2rem padding
- Body responsiveness:
  - Below `lg`: a single `<ScrollArea>` wraps left + right content stacked with a horizontal `Separator` between them so every input on the left stays reachable on mobile
  - At `lg+`: a `flex-row` with the left panel taking `flex-1` and the right panel at `w-[320px]`, each with its own `<ScrollArea>` and a vertical `Separator` between
- Inventory Rules form: 2-column grid for inputs, 5-column grid for the stats strip - both reflow to 2-up on narrow widths
- Shipping dimensions row: `grid-cols-[1fr_1fr_1fr_5rem]` with `items-end` so the unit `Select` aligns to the bottom of the labeled inputs without inheriting a separate label slot

## LLM Guidance
Keep the three-section left column (`CurrentStockRow` / `InventoryRulesSection` / `ShippingSection`) and the single right column (`ProductPanel`). The Frame primitives use the same `dense spacing="sm"` + `py-1.5!` + `shadow-none!` overrides as solution-inventory-7 - keep that triad together when adding new sections so density stays consistent across the sheet. When the form needs more fields, append them inside the existing `FieldGroup` blocks (gap-4) rather than introducing new wrappers. The Auto Reorder switch lives inside FrameHeader; if you need to add more header controls, keep them inside a horizontal `Field` so the label/control gap stays at 8px. The bottom action cluster is split intentionally - `Print Label` on the left signals the secondary side-effect action, while `Cancel` and `Save` cluster on the right per the sheet-6 pattern. The right-rail summary is read-only by design; if you need to edit fields from there, move them into the left panel rather than wiring inputs into the summary `<dl>`.

### `solution-inventory-9`

Track Shipping

Track Shipping sheet: a right-anchored single-column Sheet (sheet-6 + solution-inventory-7 anatomy) showing a shipment header (id + Shipped badge + placed-date / Order ID link meta + Cancel Order / Notify Customer actions), an origin-to-destination route with a carrier chip, a 4-step horizontal progress stepper (Picking / Packed / Shipping / Delivered with done / active / pending states), a Shipping Data summary (Total Time, Dep. Time, Exp. Arrival, Tracking No.), and a vertical Shipping Log timeline. Full-width Close button in the footer.

Uses: `@reui/badge`, `@reui/frame`, `@reui/timeline`

## Purpose
Live-tracking detail surface opened from an orders or shipments table. Surfaces the shipment id + status, route, current step, summary data, and the chronological event log on a single column so the operator can quickly answer "where is this package?" without leaving the parent screen.

## Best Fit
- shipment tracker drawer opened from a shipping/orders DataGrid row
- customer-success workspace where an operator needs to read the status + log without losing the parent screen
- fulfilment workflow where Cancel Order and Notify Customer are the two next actions

## Main Pieces
- **Sheet shell** (adapted from `application/sheet/sheet-6` and `solutions/inventory/solution-inventory-7`): right-anchored Sheet with inset rounded corners, no built-in close button, `SheetHeader` carrying the title row + shipment id + Shipped badge + placed-date / Order ID meta + Cancel Order (ghost) / Notify Customer (outline) action cluster, a single-column `ScrollArea` body, and a `SheetFooter` with a full-width `Close` outline button.
- **RouteAndStepper** (ReUI `Frame` + `FramePanel`, `dense spacing="sm"`, `shadow-none!`): two-stop origin → destination list with vertical dot-and-line connector, plus a carrier chip on the right (small colored square holding the carrier initials next to the carrier name). Below the route, a 4-step horizontal `Stepper` - segmented progress bars on top, then a row of `done` (filled emerald check) / `active` (outline emerald check) / `pending` (gray outline) state icons + labels.
- **ShippingDataSection** (Frame): 4-column stat strip - Total Time, Dep. Time, Exp. Arrival, and Tracking No. (mono).
- **ShippingLogSection** (Frame): vertical log timeline - each entry has a left-side dot connected by a thin vertical line, the event title + timestamp on the same line, a description below, and an optional location row with a small `MapPin` icon.

## Reused Blocks
- `application/sheet/sheet-6` - sheet anatomy: trigger + custom-width `SheetContent` + sticky header / scrollable body / sticky footer
- `solutions/inventory/solution-inventory-7` - `Frame dense spacing="sm"` + `FramePanel shadow-none!` convention, header SKU/created/updated meta pattern (adapted for Placed / Order ID), the action-cluster pattern with a `Button` rendered as an anchor for the Cancel Order link

## Layout Grid
- Sheet width: `w-[min(48rem,calc(100vw-2rem))]` - never exceeds 768px (narrower than solution-inventory-7's 60rem because this is single-column content), never less than viewport - 2rem padding
- Body: single `<ScrollArea>` wrapping a vertical flex of three Frames + a route+stepper composite. Same shell works mobile and desktop - no two-panel split needed since the design is intrinsically one column.
- Inner grids: Shipping Data uses `grid-cols-2 sm:grid-cols-4` so the 4 stats reflow to 2-up on narrow widths. The Stepper uses `grid-cols-4` and the route stops always stack vertically (typical from → to pattern).

## LLM Guidance
Keep the three-piece body composition (`RouteAndStepper` / `ShippingDataSection` / `ShippingLogSection`). The Stepper state taxonomy (`done` / `active` / `pending`) drives both the bar fill (emerald vs muted) and the icon (filled check / outline check / empty circle); keep the two in sync when extending states. The Shipping Log timeline uses a single `<ul>` with absolutely-positioned dots and connector lines drawn via `before`/sibling pseudo-elements - when adding entries, the last one drops the connector line via the `isLast` prop. The carrier chip is a generic colored-tile + initials + name pattern; swap the initial + tile bg when adapting to FedEx / USPS / DHL etc. Cancel Order is rendered as a `Button` rendered as an anchor with `variant="ghost"` so the action group reads as a row of buttons (no inline-link styling) - consistent with solution-inventory-7's HeaderActions. The bottom action is intentionally a single full-width Close - Notify Customer and Cancel Order live in the header per the design.

### `solution-inventory-10`

Create Shipping Label

Create shipping label dialog: a wide centered dialog with a sticky header carrying the title + close action, a two-column scrollable body, and a sticky footer with terms link plus Cancel / Buy Shipping Label actions. Left column stacks a pickup-to-destination route + order meta card, a Products card with per-item Weight inputs (kg), and a Packaging card with Custom Package / Carrier Package line tabs containing package name, type select, total weight, length/width/height + unit dropdown, and a save-for-future checkbox. Right column carries a Summary card (Shipping to + address + price details + total) followed by a Shipping Date input with calendar affordance and a Send Shipping Info to Customer checkbox.

Uses: `@reui/frame`, `@reui/timeline`

## Purpose
A buyer/operator dialog for assembling a shipping label from an order. Operators confirm pickup and destination, edit per-item weight, pick or describe packaging, then buy a label without leaving the order page.

## Best Fit
- order list / order detail page that needs to send a shipment for selected items
- fulfilment center workflow where carrier vs. custom packaging is a deliberate switch
- post-checkout admin tool that bundles order summary, shipping price details, and label purchase in one surface

## Main Pieces
- **Dialog shell**: centered `Dialog` with a custom sticky header (title + accessible close button), scrolling two-column body, and a sticky footer carrying the Shipping Terms link + Cancel / Buy Shipping Label actions.
- **Route + order card** (ReUI `Frame`): pickup → destination addresses with a vertical dot/line connector reused from `solution-inventory-9`, separator, then a 4-column meta row (Order ID, Placed, Total Price, Shipping Priority).
- **Products section** (ReUI `Frame` + shadcn `Item`): product rows pair an `ItemMedia variant="image"` shell (anchored image), product name (anchored), SKU/Color metadata, and a per-row `InputGroup` Weight field with a `kg` suffix.
- **Packaging section** (ReUI `Frame` + shadcn `Tabs` line variant): line-style `TabsList` lives inside the `FrameHeader`. Custom Package panel uses `Field` + `Input` + `Select` + `InputGroup` for Package Name, Package Type, Total Weight (kg), Length / Width / Height + Unit (sm / in), and a Save-for-future checkbox. Carrier Package panel offers a short empty/secondary state with a Browse Carrier Boxes action.
- **Summary card** (ReUI `Frame`): shipping destination + address, separator, price details `<dl>`, separator, and bold Total row.
- **Shipping date + notify**: `InputGroup` with a `CalendarIcon` end addon followed by a checkbox that links the word `Shipping Info` to a destination anchor.

## Reused Blocks
- `application/dialog/dialog-9` - sticky-header + scrolling-body dialog pattern with a custom `DialogClose` and footer action cluster
- `solutions/inventory/solution-inventory-7` - `Frame` / `FrameHeader` / `FramePanel` rhythm for stacked operational cards and the `ECOMMERCE_LINK_CLASS_NAME` convention
- `solutions/inventory/solution-inventory-9` - pickup → destination dot+line route connector

## Layout Grid
- Dialog width: `w-[min(64rem,calc(100vw-1.5rem))]` - never exceeds 1024px, never less than viewport - 1.5rem padding
- Body grid: `grid-cols-1 lg:grid-cols-[minmax(0,1fr)_18rem]` so the right summary rail collapses below the main column on narrower widths
- Dimensions row: `grid-cols-2 sm:grid-cols-[1fr_1fr_1fr_5rem]` keeps Length / Width / Height even-width and pins the Unit select to a compact column

## LLM Guidance
Keep the three left-column blocks (Route+Order / Products / Packaging) and the two right-column blocks (Summary / Shipping Date + notify). To add a product line, push another `ShipmentItem` onto `SHIPMENT_ITEMS` - the Products section maps over the array and `itemWeights` state seeds from `weightKg`. To support imperial dimensions, the `Select` next to Height owns the unit and is wired to `DIMENSION_UNITS`. The packaging Custom / Carrier toggle is a controlled `Tabs` value held in component state; the Carrier panel is an intentionally light empty state so teams can swap in a carrier picker without redesigning the dialog. The dialog defaults to `open: true` so previews read at full state; in production wire `open`/`onOpenChange` to the parent screen's trigger.

### `solution-inventory-11`

Order Details

Order details sheet: a right-anchored fulfillment review surface that reuses the solution-inventory-7 sheet shell. Header carries an Order Details title row, the order id + Shipped badge, a Created / Customer meta line, and a vertically-centered Delete / Order Tracking / View Shipping Label action cluster. The scrollable two-column body pairs an Order Data Frame (Items, Total Price, Shipping Priority, Delivery Method), a Products Frame with Item-based rows (image + name + SKU/color, inline weight input on the right), and a title-less Shipping Frame combining a vertical route Timeline, a UPS Global carrier chip, a Separator, and a four-step Picking / Packed / Shipping / Delivered status stepper. The right rail is a Summary Frame with shipping-to address, price details (Subtotal / Shipping / Tax / Total), and a separated total row. All frames use `dense spacing="sm"` for an operator-density default. The footer mirrors the header action cluster with a Read Shipping Terms & Conditions link on the left.

Uses: `@reui/badge`, `@reui/frame`, `@reui/timeline`

## Purpose
A fulfillment review surface the operator opens from any order list (e.g. an order DataGrid row) to verify items, weight, shipping route, status, and totals before printing the shipping label. The sheet shares the solution-inventory-7 inset-anchored shell so it slots in next to solution-inventory-7 / solution-inventory-8 / solution-inventory-9 as a consistent right-anchored operator sheet family.

## Best Fit
- detail review triggered from an orders/fulfillment DataGrid row
- pre-ship verification screen that combines order metadata, item weights, route, and totals in one surface
- ops handoff sheet where the same Delete / Order Tracking / View Shipping Label cluster lives in both header and footer

## Main Pieces
- **Sheet shell** (adapted from `solutions/inventory/solution-inventory-7`): right-anchored `Sheet` with inset rounded corners, no built-in close button, custom `SheetHeader` carrying the title row + order id + meta line + action cluster, `ScrollArea` body, custom `SheetFooter` with terms link + action cluster. The header sub-row uses `lg:items-center` so the action cluster vertically centers with the title+meta block.
- **Order Data** (ReUI `Frame` dense spacing="sm"): 4-up grid of Items, Total Price, Shipping Priority, Delivery Method.
- **Products** (ReUI `Frame` dense spacing="sm"): shadcn `Item` rows (`<Item>` + `<ItemMedia variant="image">` + `<ItemContent>` + `<ItemTitle>` + `<ItemDescription>`) for each product. The image is a 40px (`size-10`) bordered tile, and the right slot carries a `Label` + `InputGroup` weight input suffixed with `kg`. Pattern matches `solutions/inventory/solution-inventory-10` exactly.
- **Shipping** (ReUI `Frame` dense spacing="sm", title-less): single `FramePanel` containing a vertical `Timeline` route with two address stops, a `UpsLogo` carrier chip on the right, a `Separator`, and a four-step horizontal `Stepper` (Picking / Packed / Shipping / Delivered).
- **Summary** (ReUI `Frame` dense spacing="sm"): destination header + address, a separator, a `Price Details` block (Subtotal / Shipping / Tax / Total), and a final separated total row.

## Reused Blocks
- `solutions/inventory/solution-inventory-7` - sheet anatomy: trigger button, custom-width `SheetContent`, sticky header/footer, two-column body, mobile-stacked / `lg+` side-by-side split with independent `ScrollArea`s
- `solutions/inventory/solution-inventory-10` - product `Item` row pattern (Item + ItemMedia/ItemContent/ItemTitle/ItemDescription with `px-0 py-0` Item, `size-10` bordered ItemMedia image, right-slot weight `InputGroup`), `bg-primary` Timeline indicator/separator colors, and combined route + stepper inside a single `FramePanel` separated by `Separator`
- `solutions/inventory/solution-inventory-9` - `Stepper` / `StepIcon` indicator pattern (emerald dot for done, ringed check for active, hollow circle for pending) and original `CarrierChip` pattern (adapted for UPS Global)

## Layout Grid
- Sheet width: `w-[min(64rem,calc(100vw-2rem))]` - never exceeds 1024px, never less than viewport - 2rem padding
- Inner body: stacked `ScrollArea` on mobile; `lg+` splits into a flex-1 left column and a `w-[320px]` right rail with a vertical `Separator`
- Order Data: `grid-cols-2 sm:grid-cols-4` so KPIs reflow on narrower body widths
- Product rows: shadcn `Item` with `items-center gap-3 px-0 py-0` so image, content, and weight input read as one compact row

## LLM Guidance
Keep the three-piece left column (`OrderDataSection` / `ProductsSection` / `ShippingSection`) and the single right-column `SummarySection`. To add another KPI to Order Data, extend the `stats` array - the grid will reflow. To add another product line, append to `ORDER.items` (rendered via `ProductItemRow`). The `HeaderActions` cluster is intentionally rendered twice (header + footer) - edit the single component to keep both in sync. The sheet defaults to `open: true` so the preview reads at full state; in production wire `open`/`onOpenChange` to the parent grid's row trigger. The `UpsLogo` SVG is inline; replace it with a different carrier mark by swapping the SVG and the `name` passed to `CarrierChip`.


## solution-users (7)

### `solution-users-1`

Workspace Members Directory Grid with Roles, SSO/2FA Status, and Bulk Role Actions

Full-page admin console for workspace members: sort/filter rows, multi-select bulk role changes, SSO/2FA columns, member detail sheet. ReUI DataGrid, Frame, Filters, Badge; shadcn Button, Sheet. For user management, access control, team admin.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/filters`, `@reui/filters-query`, `@reui/filters-types`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `solution-users-2`

Member Detail Page with Sidebar Tabs for Access, Authentication, and Sessions

Full-page admin screen to manage one member's roles, teams, MFA factors, sessions, activity, and a danger zone via a vertical tab rail. ReUI Badge; shadcn Avatar, Tabs, Select, AlertDialog. User management, permissions, account security.

Uses: `@reui/badge`, `@reui/frame`, `@reui/timeline`

npm: `sonner`

### `solution-users-3`

Workspace roles and permissions access matrix with locked Owner column and grouped scope toggles

Full-page matrix mapping workspace roles to grouped permission scopes: per-cell toggles, locked Owner access, group tabs, and a dirty save bar. ReUI DataGrid, Frame, Badge, Alert; shadcn Button, Tabs, Dialog. Admin panel, role management, RBAC.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `sonner`

### `solution-users-4`

Invitations Queue Data Grid with Status Filter and Bulk Resend or Revoke

Full-page invitations grid tracking pending, accepted, expired, and revoked invites with search, status filter, bulk resend or revoke, and an invite people dialog. ReUI DataGrid, Badge; shadcn Button, Select, InputGroup. Admin panel, team management.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `solution-users-5`

Just-in-Time Access Request Queue with Inline Approvals and Policy Review

Admin grid to review, approve, or deny just-in-time access requests with inline decisions, bulk approve, and status/approver filters, plus a policy-check detail sheet. ReUI DataGrid, Badge; shadcn Sheet, Button. Access control, permission approval.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-column-visibility`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `sonner`

### `solution-users-6`

Day-Grouped Audit Log Timeline with Expandable Event Details and CSV Export

Full-page audit timeline grouping access events by day with severity badges, expandable details, type filters, and CSV export. ReUI Timeline, Frame, Badge; shadcn Avatar, Button, Collapsible, Select, ToggleGroup. Activity log, compliance, access.

Uses: `@reui/badge`, `@reui/frame`, `@reui/timeline`

npm: `sonner`

### `solution-users-7`

Enterprise SSO and SCIM Security Settings Page with Policy Controls

Workspace admin page to manage SSO providers, SCIM provisioning, 2FA and password policy, session timeouts, and allowed domains, with status rows and a dirty-state save bar. ReUI Frame, Alert, Badge; shadcn Button, Select, Switch. Security settings.

Uses: `@reui/alert`, `@reui/badge`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `sonner`

