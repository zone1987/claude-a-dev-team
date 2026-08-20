# shadcn-vue Blocks

## Contents

- [What are Blocks?](#what-are-blocks)
- [Installation](#installation)
- [Customization](#customization)
- [Block categories](#block-categories)
- [All available blocks](#all-available-blocks)
- [Related Skills](#related-skills)

## What are Blocks?

Blocks are complete, production-ready page layouts that you can copy straight into a project.
They are composed of existing shadcn-vue components and cover typical UI patterns:
authentication flows (login, signup, OTP), dashboards, product tables and sidebar layouts.

Unlike individual components, a block spans several files (page component, sub-components,
optionally data fixtures) and represents a complete page layout.

## Installation

```bash
npx shadcn-vue@latest add <block-name>
```

Example:

```bash
npx shadcn-vue@latest add dashboard-01
npx shadcn-vue@latest add login-02
npx shadcn-vue@latest add sidebar-07
```

The files are copied directly into the project (by default into `src/components/blocks/`)
and you can adapt them freely afterwards. There is no external dependency — after the
`add` command the block belongs entirely to your own codebase.

## Customization

Because blocks are installed by copying, every file is directly editable:

- Adjust layout and structure
- Change colors and spacing via Tailwind classes
- Replace data with real API calls
- Extract or rename sub-components
- Add or remove any shadcn-vue components

## Block categories

| Category | Description |
|---|---|
| `dashboard-*` | Admin dashboards with charts, tables, cards |
| `login-*` | Login forms (various layouts) |
| `signup-*` | Registration forms |
| `otp-*` | One-time password / code entry |
| `products-*` | Product tables and lists |
| `sidebar-*` | Application layouts with sidebar navigation |

## All available blocks

Detailed descriptions, file lists and use cases are documented in the reference:
`OVERVIEW-DETAIL.md`

### Dashboard

| Block | Description |
|---|---|
| `dashboard-01` | Dashboard with sidebar, data table, area chart and section cards |

### Authentication — Login

| Block | Description |
|---|---|
| `login-01` | Simple centered login form (email/password + Google OAuth) |
| `login-02` | Two columns: cover image on the left, GitHub OAuth on the right |
| `login-03` | Login on a muted background with social auth |
| `login-04` | Image on the left, card layout on the right |
| `login-05` | Minimal login without a card wrapper |

### Authentication — Signup

| Block | Description |
|---|---|
| `signup-01` | Simple centered signup form |
| `signup-02` | Two columns with cover image |
| `signup-03` | Signup on a muted background |
| `signup-04` | Signup with additional fields (first and last name) |
| `signup-05` | Minimal signup |

### Authentication — OTP

| Block | Description |
|---|---|
| `otp-01` | OTP entry with 6 digits, centered |
| `otp-02` | OTP with email display and resend link |
| `otp-03` | OTP minimal layout |
| `otp-04` | OTP with countdown timer |
| `otp-05` | OTP with instructions and help text |

### Products

| Block | Description |
|---|---|
| `products-01` | Product table with search and filters |

### Sidebar Layouts

| Block | Description |
|---|---|
| `sidebar-01` | Simple sidebar with navigation in groups |
| `sidebar-02` | Sidebar with collapsible subnavigation (inset variant) |
| `sidebar-03` | Sidebar with collapsible subnavigation (floating variant) |
| `sidebar-04` | Sidebar with collapsible subnavigation (without header) |
| `sidebar-05` | Sidebar with secondary navigation (floating) |
| `sidebar-06` | Sidebar with secondary navigation (icons only) |
| `sidebar-07` | Collapsible sidebar with icon rail |
| `sidebar-08` | Sidebar with nested sub-items and icons |
| `sidebar-09` | Sidebar with workspace/team switcher |
| `sidebar-10` | Sidebar with user profile in the footer |
| `sidebar-11` | Sidebar with floating action buttons |
| `sidebar-12` | Sidebar with date picker in the footer |
| `sidebar-13` | Sidebar with project/workspace navigation |
| `sidebar-14` | Sidebar with search and settings (minimal) |
| `sidebar-15` | Sidebar with breadcrumb and sticky header |
| `sidebar-16` | Sidebar with a floating top navigation bar |

## Related Skills

- `shadcn-vue-sidebar` — Sidebar component (single component, API, props, composable)
- `shadcn-vue-chart` — Chart components for dashboard blocks
- `shadcn-vue-data-table` — Data table component
- `shadcn-vue-input-otp` — OTP input component
