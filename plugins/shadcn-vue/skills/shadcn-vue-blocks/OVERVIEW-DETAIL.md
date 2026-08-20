# shadcn-vue Blocks — Complete Reference

## Contents

- [What are Blocks?](#what-are-blocks)
- [Installation](#installation)
- [Customization](#customization)
- [All Blocks](#all-blocks)
- [Block Anatomy](#block-anatomy)
- [Frequently asked questions](#frequently-asked-questions)

## What are Blocks?

Blocks are complete, ready-to-use page layouts built from shadcn-vue components. They cover
common application UI patterns such as authentication flows, dashboards, product listings, and
sidebar-based application shells.

Key characteristics:

- **Copy-paste installation**: blocks are copied into your project via the CLI, not installed as
  a dependency. You own the code after installation.
- **Built from shadcn-vue components**: all building blocks (Button, Card, Input, Sidebar, Table,
  Chart, etc.) are already in your project or are added automatically.
- **Fully editable**: every file is yours to modify — layout, data, styles, sub-components.
- **Multiple files per block**: a block typically includes a main page component, one or more
  sub-components, and optionally sample data fixtures.

## Installation

### CLI (recommended)

```bash
npx shadcn-vue@latest add <block-name>
```

Examples:

```bash
# Install a dashboard layout
npx shadcn-vue@latest add dashboard-01

# Install a two-column login
npx shadcn-vue@latest add login-02

# Install a sidebar with collapsible icon rail
npx shadcn-vue@latest add sidebar-07
```

The CLI will:
1. Copy all block files to `src/components/blocks/<block-name>/`
2. Install any missing shadcn-vue component dependencies
3. Leave your existing files untouched

### Manual installation

1. Browse the block at `https://www.shadcn-vue.com/blocks`
2. Click "Copy code" for each file shown in the block preview
3. Paste into your project under a suitable directory

## Customization

After installation, blocks are plain Vue SFC files. Common customizations:

- Replace hardcoded data arrays with API calls or Pinia stores
- Swap placeholder text and labels for real copy
- Adjust Tailwind utility classes for spacing, colors, and typography
- Extract repeated sub-components into shared files
- Add or remove shadcn-vue components (e.g. add a `Drawer` for mobile detail views)
- Wire up router links via `<RouterLink>` or `as-child` props

## All Blocks

### Dashboard

| Block Name | Category | Description | Key Files |
|---|---|---|---|
| `dashboard-01` | Dashboard | Dashboard with sidebar, data table, area chart, and section cards | `dashboard-01.vue`, `components/` |

### Authentication — Login

| Block Name | Category | Description | Key Files |
|---|---|---|---|
| `login-01` | Login | Simple centered login form — email/password fields plus Google OAuth button | `login-01.vue` |
| `login-02` | Login | Two-column layout: decorative cover image on the left, GitHub OAuth card on the right | `login-02.vue` |
| `login-03` | Login | Login form on a muted/dimmed background with social authentication options | `login-03.vue` |
| `login-04` | Login | Full-height image on the left, login card on the right | `login-04.vue` |
| `login-05` | Login | Minimal login without a card wrapper — bare form on a plain background | `login-05.vue` |

### Authentication — Signup

| Block Name | Category | Description | Key Files |
|---|---|---|---|
| `signup-01` | Signup | Simple centered signup form | `signup-01.vue` |
| `signup-02` | Signup | Two-column signup with decorative cover image | `signup-02.vue` |
| `signup-03` | Signup | Signup form on a muted background | `signup-03.vue` |
| `signup-04` | Signup | Signup with additional fields: first name and last name | `signup-04.vue` |
| `signup-05` | Signup | Minimal signup without card wrapper | `signup-05.vue` |

### Authentication — OTP

| Block Name | Category | Description | Key Files |
|---|---|---|---|
| `otp-01` | OTP | 6-digit OTP input, centered layout | `otp-01.vue` |
| `otp-02` | OTP | OTP with masked email address display and resend link | `otp-02.vue` |
| `otp-03` | OTP | Minimal OTP layout | `otp-03.vue` |
| `otp-04` | OTP | OTP with countdown timer for resend cooldown | `otp-04.vue` |
| `otp-05` | OTP | OTP with step-by-step instructions and contextual help text | `otp-05.vue` |

### Products

| Block Name | Category | Description | Key Files |
|---|---|---|---|
| `products-01` | Products | Product listing table with search input and filter controls | `products-01.vue`, `components/` |

### Sidebar Layouts

| Block Name | Category | Description | Key Files |
|---|---|---|---|
| `sidebar-01` | Sidebar | Simple sidebar with navigation items grouped by section | `sidebar-01.vue`, `components/app-sidebar.vue` |
| `sidebar-02` | Sidebar | Sidebar with collapsible sub-navigation (inset variant) | `sidebar-02.vue`, `components/` |
| `sidebar-03` | Sidebar | Sidebar with collapsible sub-navigation (floating variant) | `sidebar-03.vue`, `components/` |
| `sidebar-04` | Sidebar | Sidebar with collapsible sub-navigation, no visible header | `sidebar-04.vue`, `components/` |
| `sidebar-05` | Sidebar | Sidebar with secondary navigation panel (floating) | `sidebar-05.vue`, `components/` |
| `sidebar-06` | Sidebar | Sidebar with icon-only secondary navigation | `sidebar-06.vue`, `components/` |
| `sidebar-07` | Sidebar | Collapsible sidebar with an icon rail — collapses to icon strip | `sidebar-07.vue`, `components/` |
| `sidebar-08` | Sidebar | Sidebar with deeply nested collapsible items and icon support | `sidebar-08.vue`, `components/` |
| `sidebar-09` | Sidebar | Sidebar with workspace or team switcher in the header | `sidebar-09.vue`, `components/` |
| `sidebar-10` | Sidebar | Sidebar with user profile card in the footer | `sidebar-10.vue`, `components/` |
| `sidebar-11` | Sidebar | Sidebar with floating action buttons | `sidebar-11.vue`, `components/` |
| `sidebar-12` | Sidebar | Sidebar with an inline date picker in the footer | `sidebar-12.vue`, `components/` |
| `sidebar-13` | Sidebar | Sidebar with project or workspace navigation and context switching | `sidebar-13.vue`, `components/` |
| `sidebar-14` | Sidebar | Minimal sidebar with search field and settings link | `sidebar-14.vue`, `components/` |
| `sidebar-15` | Sidebar | Sidebar with breadcrumb trail and sticky page header | `sidebar-15.vue`, `components/` |
| `sidebar-16` | Sidebar | Sidebar paired with a floating top navigation bar | `sidebar-16.vue`, `components/` |

## Block Anatomy

A typical block directory after installation:

```
src/components/blocks/
  dashboard-01/
    dashboard-01.vue        # Main page component — use as a route component
    components/
      data-table.vue        # Sub-components used within the block
      area-chart.vue
      section-cards.vue
      app-sidebar.vue
```

The main file (`dashboard-01.vue`) is the entry point and can be registered directly as a Vue
Router route or embedded as a full-page component.

## Frequently asked questions

**Can I use multiple blocks in one project?**
Yes. Each block lives in its own subdirectory and has no global side effects.

**Do blocks get updates when shadcn-vue releases a new version?**
No. Once copied, blocks are static. You apply updates manually, the same way you would with any
component you own.

**Can I mix blocks from different categories?**
Yes. For example, you can use `sidebar-07` as the application shell and place `products-01`
inside `SidebarInset` as the main content area.

**Where is the online preview?**
`https://www.shadcn-vue.com/blocks`
