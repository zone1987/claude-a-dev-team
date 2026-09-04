# Premium blocks — Application

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 292 entries. Do not edit by hand.

**Licence: Pro or Ultimate.** Install with `shadcn add @reui/<name>` once `REUI_LICENSE_KEY` is set.

## Contents

- [app-shell (21)](#app-shell-21)
- [auth (20)](#auth-20)
- [card (43)](#card-43)
- [chart (30)](#chart-30)
- [dashboard (8)](#dashboard-8)
- [dialog (14)](#dialog-14)
- [empty-state (14)](#empty-state-14)
- [event-calendar (6)](#event-calendar-6)
- [form (12)](#form-12)
- [gantt (4)](#gantt-4)
- [kanban-board (10)](#kanban-board-10)
- [list (11)](#list-11)
- [navbar (13)](#navbar-13)
- [onboarding (9)](#onboarding-9)
- [profile (9)](#profile-9)
- [schedule (10)](#schedule-10)
- [settings (16)](#settings-16)
- [sheet (11)](#sheet-11)
- [stats (15)](#stats-15)
- [timeline (9)](#timeline-9)
- [wizard (7)](#wizard-7)

## app-shell (21)

### `app-shell-1`

Collapsible icon-rail sidebar app shell with workspace switcher, nested nav, and user menu

Dashboard app shell with an icon-collapsible sidebar: workspace switcher, nested platform nav with count badges, pinned resources with row action menus, theme toggle, breadcrumb header. ReUI Badge, shadcn Sidebar, DropdownMenu, Avatar, Breadcrumb.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-2`

Floating icon-collapsible sidebar shell with command-K search, nested nav, and workspace switcher

App shell with a floating collapsible-to-icon Sidebar, command-K search Dialog, nested Platform nav with a live status pulse, workspace switcher Dropdown, and Breadcrumb header. Uses Sidebar, Breadcrumb, Avatar, Dialog, Kbd. Dashboard, admin panel.

### `app-shell-3`

Inset sidebar app shell with per-project progress rings and a multi-type notifications popover

Inset collapsible sidebar dashboard shell with workspace switcher, command search, project donut progress rings, usage limit meter, and notifications popover. ReUI Frame, Badge, Rating plus shadcn Sidebar, Popover, DropdownMenu, Progress, Avatar.

Uses: `@reui/badge`, `@reui/frame`, `@reui/rating`

npm: `next-themes`

### `app-shell-4`

Mail inbox app shell with icon folder rail, wide message list, and selected-message action header

Mail and inbox shell: folder icon rail plus a wide 440px message list with live search, filter tabs, rich preview rows, and a selected-message action header (reply, star, delete). ReUI Badge, shadcn Sidebar, Tabs, Avatar, DropdownMenu.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-5`

Calendar app shell, icon-rail sidebar switching Calendar, Schedule, Contacts, Notifications panels

Calendar workspace with a dual-pane icon-rail Sidebar swapping mini-Calendar accounts, date-grouped Schedule, searchable Contacts, and Notifications. Uses ReUI Badge with shadcn Sidebar, Calendar, Avatar, DropdownMenu.

Uses: `@reui/badge`

npm: `next-themes`, `react-day-picker`

### `app-shell-6`

Dual Sidebar App Shell with Dark Nav Rail and Slide-In Calendar Context Panel

Three-column workspace shell: dark collapsible nav rail with command search, team list and usage meter, breadcrumb header, and a slide-in right Calendar panel with agenda and account toggles. ReUI Frame, Badge, Rating plus shadcn Sidebar, Calendar.

Uses: `@reui/badge`, `@reui/frame`, `@reui/rating`

npm: `next-themes`, `react-day-picker`

### `app-shell-7`

Breadcrumb-switcher app shell with org/app/environment dropdowns and a live system monitor popover

Header-first shell with a breadcrumb of org, app, and environment switcher dropdowns, a live system monitor popover with resource sparklines, command-palette search, and collapsible nested sidebar nav. ReUI Badge, Kbd, shadcn Sidebar, DropdownMenu.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-8`

Inset icon-rail app shell with per-section secondary nav, org/app/env switchers, and notifications

Two-level dashboard shell: icon rail plus a per-section secondary nav with live-metric/storage footers, org/app/env switchers, command-K search, and notifications drawer. ReUI Badge, Rating; shadcn Sidebar, Sheet, Dialog. Inventory, ops admin.

Uses: `@reui/badge`, `@reui/rating`

npm: `next-themes`

### `app-shell-9`

Dark inset-sidebar team workspace shell with member presence rail and notifications feed

Dark collapsible-sidebar team shell: presence member rail, notifications feed, command search, AI-credit usage card, workspace switcher. ReUI Frame, Badge; shadcn Sidebar, Avatar, DropdownMenu, Progress. For SaaS dashboards and team apps.

Uses: `@reui/badge`, `@reui/frame`

npm: `next-themes`

### `app-shell-10`

AI Agents App Shell with Collapsible Sidebar, Active-Project Rings, and Rich Notifications

Inset sidebar shell for an AI agents console: command-K search, collapsible agent nav, projects with progress rings, usage-limit card, org and theme switcher, notifications popover. ReUI Frame, Badge, Rating; shadcn Sidebar, Popover, DropdownMenu.

Uses: `@reui/badge`, `@reui/frame`, `@reui/rating`

npm: `next-themes`

### `app-shell-11`

Operations app shell with four toggleable regions and a resizable bottom workbench sheet

Dense operations console: collapsible nav, resizable split panes, an expandable bottom workbench sheet, and a right calendar and agenda rail. ReUI Badge, Frame, Rating with shadcn Sidebar, Resizable, Tabs, Calendar. Admin shell, SaaS dashboard.

Uses: `@reui/badge`, `@reui/frame`, `@reui/rating`

npm: `next-themes`, `react-day-picker`

### `app-shell-12`

Icon-rail sidebar app shell with command-K search, notifications feed, apps grid, and theme menu

Dashboard shell: collapsible icon-rail sidebar with nested nav, Soon badges, and project progress rings, plus a header command-K search, rich notifications feed, apps grid, and theme account menu. ReUI Badge, Rating; shadcn Sidebar, Popover, Dialog.

Uses: `@reui/badge`, `@reui/rating`

npm: `next-themes`

### `app-shell-13`

Community feed app shell with full-width header above a collapsible icon-rail sidebar

Full-width header over a collapsible icon-rail sidebar for community feed apps. Search, Create button, avatar menu, theme toggle, grouped nav with badges, nested Manage Feeds dropdown. ReUI Badge, shadcn Sidebar, Button, Card, DropdownMenu, Avatar.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-14`

Mini icon-rail app shell with per-section secondary nav and a tabbed workspace toolbar

Three-region workspace shell: icon rail, a toggleable secondary nav that swaps per section, and a toolbar with List, Kanban, Calendar, Dashboard tabs plus Sort, View, Filter, Search. ReUI Badge, shadcn Sidebar, Tabs, DropdownMenu, Avatar.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-15`

Dark full-width topbar app shell with workspace switcher, pinnable sidebar nav, and favorites

Dashboard shell with a fixed dark topbar over an icon-collapsible sidebar: workspace switcher, pin/unpin nav with badges, favorites group, gradient Upgrade menu, team avatars. ReUI Badge, shadcn Sidebar, DropdownMenu, Avatar, Button, Card.

Uses: `@reui/badge`

### `app-shell-16`

Dual sidebar app shell with icon rail and collapsible secondary navigation panel

Two-level dashboard layout: icon rail plus a toggleable secondary nav that swaps per section, with workspace switcher, breadcrumb header, search, and account menu with theme toggle. ReUI Badge, shadcn Sidebar, DropdownMenu, Avatar.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-17`

AI chat assistant app shell with floating sidebar, model picker grid, and prompt composer

AI chat workspace: floating collapsible sidebar with a GPT-4/Claude/Gemini model picker, pinned and recent threads, a welcome canvas, and an InputGroup composer. shadcn Sidebar, DropdownMenu, Avatar, ReUI Badge. LLM assistant, chatbot, copilot UI.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-18`

Task workspace app shell with collapsible floating sidebar and a toggleable AI chat assistant panel

Three-panel to-do shell: floating Sidebar with task lists, count Badges, color tags and a Progress focus card, plus a toggleable AI chat panel (in-flow at desktop, Sheet on mobile). Built on ReUI Badge, shadcn Sidebar, Dialog, DropdownMenu.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-19`

Calendar app shell with inset sidebar date picker, up-next agenda, and Day/Week/Month view switcher

Calendar app layout: inset Sidebar with a Calendar date picker, up-next agenda, calendars menu, account menu, and a header Day/Week/Month switcher. ReUI Badge, shadcn Sidebar, Calendar, DropdownMenu, Avatar. For scheduling apps and planners.

Uses: `@reui/badge`

npm: `next-themes`

### `app-shell-20`

Mail client app shell with folder sidebar, split list and reading panes, and icon app rail

Email workspace: inset Sidebar with account menu, compose dialog, folders, labels and contacts, a search and category-filter message list, a reading pane, and a right icon rail. shadcn Sidebar, Card, Empty, Dialog, ReUI Badge. Mail inbox, webmail UI.

Uses: `@reui/badge`, `@reui/icon-stack`

npm: `next-themes`

### `app-shell-21`

AI chat app shell with resizable thread sidebar, collapsible icon rail, and model picker

AI chat workspace: resizable thread sidebar collapsing to an icon rail, pinned and grouped chats, a search palette, and a header model picker with memory toggle. shadcn Resizable, Sidebar, Dialog, ReUI Badge. Chatbot UI, AI assistant, LLM chat.

Uses: `@reui/badge`

npm: `next-themes`, `react-resizable-panels`


## auth (20)

### `auth-1`

Split-screen login page with animated grid backdrop and editorial image panel

Sign-in page pairing an email or username and password form with show/hide toggle and Google plus Apple buttons over a masked animated grid and a full-height photo. Uses ReUI Field, InputGroup, Separator, Button, Card. Login, auth, sign in screen.

npm: `motion`

### `auth-2`

Split-screen login with an autoplay founder testimonial carousel and Trustpilot rating panel

Email or username and password sign-in with show/hide toggle and Google, Apple, GitHub buttons, beside a dark panel with an autoplay founder testimonial carousel and Trustpilot rating. ReUI Carousel, Card, Field, InputGroup. Login, social auth, SaaS.

npm: `embla-carousel-autoplay`, `motion`

### `auth-3`

Split-screen magic-link sign-in with testimonial and trust-brand sidebar on a dot-grid canvas

Passwordless magic-link sign-in with a single work-email field and Google, Apple, GitHub buttons, beside a testimonial and trust-brand sidebar on a twinkling dot canvas. ReUI Field, Input, Button, Avatar, Separator. Login, passwordless auth.

### `auth-4`

Framed password sign-in card with email or username, social provider row, and footer nav

Login on a noise-textured background: ReUI Frame card with email-or-username and password fields, show/hide toggle, full-width submit, plus a Google/Apple/GitHub row and footer nav. shadcn Field, Input, InputGroup, Button. Sign in / log in page.

Uses: `@reui/frame`

### `auth-5`

Split-screen marketing trial signup page with animated gradient blob background and social login

Full-page registration with a marketing hero, OAuth buttons (Google, GitHub), email and show/hide password fields, and a brand logo trust strip over drifting gradient blobs. ReUI Frame, shadcn Button, Field, InputGroup, Separator.

Uses: `@reui/frame`

### `auth-6`

Split-screen login with social OAuth and testimonial sidebar over an animated grid background

Two-column sign-in page: email or username, password with show/hide toggle, Forgot password, and Google/Apple/GitHub OAuth, beside a customer testimonial and brand-logo panel on an animated grid. Uses Button, Input, InputGroup, Field, Separator.

npm: `motion`

### `auth-7`

Blueprint-framed passwordless sign-in card with magic-link email and customer trust logos

Centered dark magic-link sign-in: email field sends a sign-in link, with Google, Apple and GitHub OAuth, a dashed crosshair-cornered frame, and a customer logo trust strip. Uses Button, Field, InputGroup. For login and auth pages.

### `auth-8`

Centered Frame login card over a softened photo backdrop with social provider sign-in

Single-card sign-in centered on a blurred Unsplash photo with noise grain: email or username and password fields, show/hide toggle, Forgot password, and Google, Apple, GitHub buttons. ReUI Frame; shadcn Field, InputGroup, Button. Login page.

Uses: `@reui/frame`

### `auth-9`

Split magic-link sign-in with an animated brand-logo grid sidebar and rotating star testimonial

Split passwordless login: a work-email field emails a 15-minute magic link, with Google, Apple, GitHub buttons, beside a sidebar of brand logos animating in a grid under a rotating star testimonial. ReUI Field, Input, Button, Avatar. Login, auth.

npm: `motion`

### `auth-10`

Split magic-link sign-in with a framed testimonial and customer logo wall trust sidebar

Split passwordless login: magic-link email field plus Google, Apple, and GitHub SSO, beside a Frame trust card with a star-rated testimonial and brand logo wall. ReUI Frame; shadcn Field, Input, Button, Avatar. Login, social auth, SaaS onboarding.

Uses: `@reui/frame`

### `auth-11`

Split-screen login with testimonial sidebar and animated dot backdrop

Two-column login: email or username plus password with show/hide toggle, Google and Apple buttons, and a sidebar with a star-rated testimonial and trust-brand wordmarks over a twinkling dot canvas. ReUI Field, InputGroup, Button, Separator, Avatar.

### `auth-12`

Split login method picker with passkey, SAML SSO, and a framed brand-logo testimonial sidebar

Login with Google, email, WebAuthn passkey, SAML SSO, and backup code, a two-step email reveal, and a framed sidebar with an animated brand-logo grid and rotating star testimonials. ReUI Alert; shadcn Button, Field, Input, Avatar. Sign-in, SSO.

Uses: `@reui/alert`

npm: `motion`, `sonner`

### `auth-13`

Split-screen magic-link sign-in with left image sidebar and social login buttons

Magic-link login page: work email field sends a secure sign-in link, plus Google, Apple, and GitHub social buttons. Two-column split with a full-cover image sidebar. ReUI Frame, shadcn Field, Input, Button, Separator.

Uses: `@reui/frame`

### `auth-14`

Split-screen workspace sign-in with animated stacked media panel and social SSO

Two-column workspace login page: email and password with show/hide toggle, forgot-password, and Google, Apple, GitHub SSO buttons beside an auto-cycling stacked photo panel. Uses Field, Input, InputGroup, Button, Separator.

npm: `motion`

### `auth-15`

Centered magic-link email login with logo, social sign-in buttons, and legal footer

Passwordless email login that sends a magic link, plus Google, Apple, and GitHub sign-in and a terms and copyright footer. Built with ReUI InputGroup, Field, Button, Separator. For login, SSO, passwordless auth screens.

### `auth-16`

Full-page sign-in with app header, SSO and email-continue form, and customer logo trust strip footer

Single-column sign-in: app header with create-workspace link, centered Google, GitHub, and SSO buttons over one work-email Continue field, plus a footer customer logo wall. shadcn Button, Field, Input, Separator. Login, social auth, SaaS onboarding.

npm: `lucide-react`

### `auth-17`

Centered login method picker with WebAuthn passkey sign-in and email reveal step

Two-step sign-in: a centered method picker (Google, email, SAML SSO, passkey, backup code) that reveals an email field, with real WebAuthn passkey auth and toasts. Uses shadcn Button, Input, Field, Item and ReUI Alert. Login / auth page.

Uses: `@reui/alert`

npm: `sonner`

### `auth-18`

Split-screen sign-in with testimonial sidebar, social login, and password show/hide toggle

Two-column login: email or username field, password Input with show/hide toggle, Google and Apple buttons, plus a testimonial and trust-brand sidebar. Uses ReUI Field, InputGroup, Avatar, Item, Separator, Button. For login and sign-in pages.

npm: `motion`

### `auth-19`

Passwordless workspace sign-in page with magic-link work email and Google plus GitHub login

Full-page login screen that emails a secure sign-in link to an approved work address, with Google and GitHub OAuth buttons above an or divider. Built from ReUI Card, Field, InputGroup, Separator, Button. For SSO, magic link, passwordless signin.

### `auth-20`

Centered sign-in card with Google and Apple buttons, password visibility toggle, and email login

Login page with social sign-in (Google, Apple), an email or username field, and a show or hide password toggle, plus forgot-password and create-account links. Built on ReUI Card, Field, Input, InputGroup, Button, and Separator.


## card (43)

### `card-1`

Brand logo grid card with centered icon tile and linked name per company

Responsive grid of compact brand cards, each centering a company logo in a bordered tile over a linked name. ReUI Frame plus shadcn Item, ItemMedia. For integrations, partners, tech stack, or logo wall.

Uses: `@reui/frame`, `@reui/icon-tile`

### `card-2`

Feature highlights grid of icon-tile cards with a faded dot-pattern background

Container-query feature cards that scale from one to four columns, each pairing a bordered icon tile, linked title, and muted blurb over a dotted backdrop. ReUI Frame, shadcn Item. For benefits, services, capabilities sections.

Uses: `@reui/frame`, `@reui/icon-tile`

### `card-3`

Investor profile card with availability badge, stats strip, and ranked funding sources list

Investor profile card: avatar, name, status badge, three-column stats strip, and a ranked funding sources list with colored icon tiles and amounts. ReUI Frame, Badge plus shadcn Item, AspectRatio, Button. For fundraising, VC, fund directory cards.

Uses: `@reui/badge`, `@reui/frame`, `@reui/icon-tile`

### `card-4`

Colorful dark KPI stat cards with trend badge, grid-mesh background, and footer report link

Grid of dark metric cards on colored panels, each with a big value, an up-trend Badge with percent, an icon tile, and a footer report link. Built with ReUI Frame and Badge plus shadcn Item for KPI, stats, and analytics dashboards.

Uses: `@reui/badge`, `@reui/frame`

### `card-5`

Integration Cards with Brand Logo, Connector Diagram, and Tier Badge over a Dotted Backdrop

Integration cards pairing a brand logo (Resend, PayPal, Supabase) with flanking icons on a dashed connector line over a dotted canvas, plus a title link, tier Badge, and blurb. ReUI Frame, Badge, shadcn Item. Marketplace, connectors, plugins.

Uses: `@reui/badge`, `@reui/frame`

### `card-6`

Numbered setup-step card grid with ordinal labels and a responsive one to four column Frame layout

Onboarding or setup walkthrough showing numbered steps (0.1 to 0.4) as titled, hover-linked cards in a responsive container-query grid that flows one to four columns. Built on ReUI Frame and FramePanel. For getting-started and how-it-works sections.

Uses: `@reui/frame`

### `card-7`

Detail stat card grid with label, value, and swappable logo, badge, or avatar group accent

Responsive grid of compact detail cards, each with a labeled value plus a trailing brand logo, status Badge, or stacked Avatar group. Uses ReUI Frame, Badge and shadcn Avatar. For dashboards, company, profile, and metric cards.

Uses: `@reui/badge`, `@reui/frame`

### `card-8`

Service status card grid with icon box, linked title, color-coded status dot and timestamp

Three-column grid of status cards, each pairing an icon box, a linked title, a color-coded status dot and label (Online, Synced, Idle) and a timestamp on a dot-pattern panel. ReUI Frame, FramePanel, Item. For infrastructure and uptime monitoring.

Uses: `@reui/frame`

### `card-9`

Applicant profile card with detail columns, copy-action contact fields, and skill badges

Horizontal candidate summary card: labeled columns for role, location, and contact with copy-icon buttons, plus a wrapped skill-badge row over a dot-pattern panel. ReUI Frame, Badge, shadcn Button. For ATS, recruiting, and applicant detail views.

Uses: `@reui/badge`, `@reui/frame`

### `card-10`

Color-tinted stacked Frame cards with date header, actions menu, and category badges

Responsive card grid of pastel stacked Frames, each with an uppercase date, ReUI Frame and Badge plus shadcn DropdownMenu, Button, and Separator. For reports, updates, announcements, and activity feeds.

Uses: `@reui/badge`, `@reui/frame`

### `card-11`

Minimal text-only notice card grid with accent label and faded dot-pattern background

Responsive container-query grid of text-only notice cards built on the ReUI Frame, each pairing an accent-colored label with a description over a faded dotted SVG pattern. For reminders, tips, alerts, status callouts.

Uses: `@reui/frame`

### `card-12`

Compact icon-and-title link card grid, no description text, built on ReUI Frame

Responsive grid of clickable cards, each a link with a top icon and title only and no body copy, with hover and focus-ring states. Uses ReUI Frame and FramePanel. For category tiles, quick-link menus, dashboard navigation, and feature shortcuts.

Uses: `@reui/frame`

### `card-13`

Two-column card grid with link title, description, and a row of bordered logo chips

Showcase sponsors, affiliates, or integration partners: each card pairs a hover link heading and muted description with a wrap of bordered brand logo badges. Built with ReUI Frame and shadcn Item.

Uses: `@reui/frame`

### `card-14`

Delivery tracking card with icon-labeled detail rows, status badge, header menu, and notes section

Single order delivery card showing address, ETA, and tracking number as icon rows with a Home badge, a notes block, and a header actions menu. Built with ReUI Frame and Badge plus shadcn Item, DropdownMenu, Button. Order tracking, shipment status.

Uses: `@reui/badge`, `@reui/frame`

### `card-15`

Meeting cards grid with attendee avatars, duration badge, and a Join Meeting link

Two-column grid of agenda meeting cards: title, time, duration badge, attendee AvatarGroup with overflow count, kebab menu, and a Google Meet Join link. ReUI Frame, Badge with shadcn Avatar, DropdownMenu, Button. For calendars, schedules, agendas.

Uses: `@reui/badge`, `@reui/frame`

### `card-16`

Dark integration app card with patterned header, status badge, ellipsis menu and avatar group

Integration card for app marketplaces: patterned dark header with status Badge and ellipsis DropdownMenu, brand logo, title, description, user AvatarGroup and full-width outline Button. Uses ReUI Frame, Badge with shadcn Avatar, Button, DropdownMenu.

Uses: `@reui/badge`, `@reui/frame`

### `card-17`

Shortcut cards grid with colored icon tiles, dotted canvas backdrop, and a labeled action link

Responsive grid of navigation shortcut cards, each with a colored rounded icon tile, a masked dot-pattern canvas background, title, description, and a chevron action link. ReUI Frame, FramePanel with shadcn Item. Quick links, hub, launcher, jump-to.

Uses: `@reui/frame`

### `card-18`

Compact info card grid with icon-label header, description, and source link in framed panels

Responsive 3-column grid of compact info cards using ReUI Frame, FrameHeader, and FramePanel. Each card pairs an icon-and-label header with a short description and an underlined source link. For stat tiles, resource lists, or dashboard cards.

Uses: `@reui/frame`

### `card-19`

Crypto asset price card with ticker, large quote, percent-change delta and Follow plus Trade actions

Asset overview card showing a market ticker, large price quote, green percent-change delta, last-updated time, and outline Follow plus primary Trade buttons. ReUI Frame, shadcn Button. For crypto, stock, watchlist, and trading dashboards.

Uses: `@reui/frame`

### `card-20`

Help center guide cards grid with colored icon badge and bordered article link list

Three-up help center grid where each ReUI Frame card pairs a colored icon badge, title, and summary with a bordered list of guide links carrying arrow icons. Docs hub, knowledge base, resource directory. Built with ReUI Frame and shadcn Item.

Uses: `@reui/frame`

### `card-21`

Project task cards grid with client name, due-date countdown, and share action

Three-column grid of project cards, each with an icon badge, project title link, client name, and a Due countdown. Built with ReUI Frame, shadcn Button and Item. For project lists, task boards, deadlines.

Uses: `@reui/frame`

### `card-22`

Centered promo card with overlapping tilted image pair, pill badge, and rounded CTA button

Vertical promo card pairing two rotated, overlapping square thumbnails with an outline Badge, heading, subtext, and icon Button. For upsell, demo, feature highlight, or onboarding tiles. Built with ReUI Frame plus shadcn AspectRatio, Badge, Button.

Uses: `@reui/badge`, `@reui/frame`

### `card-23`

AI monitoring promo card with stacked Frame, 24/7 uptime metric, integration logo tiles, and CTA

Stacked two-panel ReUI Frame promo: a large 24/7 monitoring metric over a faded grid with AI integration logo tiles, plus a headline, blurb, and shadcn Button CTA. For uptime, monitoring, and SaaS marketing cards.

Uses: `@reui/frame`

### `card-24`

Recommended job role card with company logo, location, work mode, and salary meta row

Job recommendation card with company logo tile, role title, and an icon meta row for location, work mode, and salary, plus a description and Quick Apply / View Details buttons. ReUI Frame, shadcn Button, Separator. Job board, careers, hiring.

Uses: `@reui/frame`

### `card-25`

Account balance summary card grid with colored icon tiles and signed percent-change indicators

Multi-account balance overview: per-account cards showing balance, type label, and color-coded gain/loss delta with a colored icon tile. Built on ReUI Frame, FramePanel, and shadcn Item. For wallet, treasury, and finance dashboards.

Uses: `@reui/frame`

### `card-26`

Three-column metric card grid with icon-and-label headers and linked titles in framed panels

Responsive 3-up grid of compact stat cards built on the ReUI Frame, each with an icon and label header plus a panel holding a clickable title link and muted description. For dashboard metrics, KPI summaries, and overview tiles.

Uses: `@reui/frame`

### `card-27`

Horizontal application summary card with labeled metadata columns, status dot, and team avatar group

Single-row record card with details in labeled columns (created, status, mobile, email, domain, team), a green status dot, info Badge, and overflow avatar group on a faded dot grid. ReUI Frame, Badge, shadcn Avatar group. Account summary row.

Uses: `@reui/badge`, `@reui/frame`

### `card-28`

KPI metric card grid with two-tone numeric values and per-panel trend Badge with period label

Responsive 1 to 4 column stat grid where each panel shows a large two-tone value with faint decimals, a metric label, and an up or down trend Badge with percent and period. ReUI Frame, FramePanel, Badge. Dashboard KPIs, analytics tiles.

Uses: `@reui/badge`, `@reui/frame`

### `card-29`

KPI metric stat grid in a bordered frame with per-cell area charts and trend badges

Dashboard KPI stat grid: bordered Frame splits into metric cells, each with an icon, large value, delta Badge, and an area chart. ReUI Frame, FramePanel, Badge. Analytics overview, stats cards, metric tiles.

Uses: `@reui/badge`, `@reui/frame`

### `card-30`

Stat card grid with icon tile, actions menu, and trend badge per metric

Responsive metric card grid (1 to 4 columns); each tile has an icon, large value, label, colored status badge with trend arrow, and an actions dropdown (Edit, Copy, Delete). KPI dashboard, analytics summary. ReUI Frame, Badge; shadcn DropdownMenu.

Uses: `@reui/badge`, `@reui/frame`

### `card-31`

KPI stat cards in a responsive grid with faded line-grid backgrounds and glossy colored icon tiles

Four-up metric cards showing a big number, label, and a colored icon tile over a masked square-mesh grid pattern. Built on ReUI Frame and FramePanel. For dashboards, analytics overviews, and KPI stat summaries.

Uses: `@reui/frame`

### `card-32`

Horizontal stats summary card with labeled metric columns, status icons, and a team avatar group

Single-row summary splitting metrics across divided columns, each with a colored status icon, value, and unit, plus an overflow team avatar column. Built with ReUI Frame and shadcn Avatar, AvatarGroup. For compliance, security, or KPI overview cards.

Uses: `@reui/frame`

### `card-33`

Inventory stat card grid with gradient icon badge, dotted backdrop, and per-card actions menu

Responsive four-up grid of inventory stat cards, each with a gradient icon badge, dotted backdrop, linked title, value, and an ellipsis menu (Edit, Copy link, Delete). Uses ReUI Frame, shadcn DropdownMenu, Item, Button. Dashboard KPIs and stats.

Uses: `@reui/frame`

### `card-34`

KPI metric cards with bold value, faint decimal fraction, and up or down trend badge per period

Responsive grid of compact stat cards: each shows a metric label, large value with a faded decimal tail, and a colored trend Badge (up or down) with a period label. Built on ReUI Frame, FramePanel, Badge. For dashboards, analytics, KPI summaries.

Uses: `@reui/badge`, `@reui/frame`

### `card-35`

KPI stat card grid with metric label, large value, and halftone dot-pattern backdrop

Responsive grid of compact metric cards, each pairing a muted label with a bold value over a masked halftone dot pattern. Built on the ReUI Frame and FramePanel. For dashboard KPI tiles, stats overview, and analytics summary cards.

Uses: `@reui/frame`

### `card-36`

KPI stat card grid with big metric over label and a masked dot-grid backdrop

Responsive container-query grid of compact KPI stat cards, each pairing a large metric value with a muted label over a masked dot-grid pattern. Built on ReUI Frame and FramePanel for dashboards, analytics, and metrics overviews.

Uses: `@reui/frame`

### `card-37`

Compact KPI stat tile grid with muted labels and green metric icons

Responsive 3-column grid of compact KPI tiles, each a muted label over a green icon plus bold metric value (MRR, revenue, growth). Built on ReUI Frame and FramePanel for stats summaries, metric cards, company snapshots.

Uses: `@reui/frame`

### `card-38`

Horizontal stat strip card with divided metric columns and a dotted accent cell

Horizontal KPI strip in a ReUI Frame: equal stat columns with bold value over muted label, hairline dividers, and a dotted-texture final cell. Profile or dashboard summary stats, metric row.

Uses: `@reui/frame`

### `card-39`

Icon-badge resource card grid linking to help, docs, and platform sections

Responsive grid of clickable resource cards, each with an icon badge, title link, and short blurb. Built on ReUI Frame and FramePanel with shadcn Item and ItemMedia. For docs hubs, help centers, onboarding, and platform overview sections.

Uses: `@reui/frame`

### `card-40`

Compact two-column metric stat grid with large value, unit, and muted label tiles

Two-column grid of metric tiles, each pairing a large value with a small unit and a muted label, for KPI summaries, fitness and activity stats, and dashboard quick stats. Built on ReUI Frame and FramePanel.

Uses: `@reui/frame`

### `card-41`

Topic Link Card Grid with Colored Icon Tiles and Hover Title Links

Responsive grid of compact topic cards, each a colored icon tile, linked title, and one-line summary. Built on ReUI Frame with shadcn Item and ItemMedia. For help center topics, quick links, resource and feature shortcuts.

Uses: `@reui/frame`

### `card-42`

Profile card with verified name, online badge, team avatar group, stats row, and connect button

Profile card with avatar, online status badge, verified name, company and email, team avatar group, 3-column stats row, and a Connected button. ReUI Frame with shadcn Avatar, AvatarGroup, Item, Separator, Button. For team, contact, or account cards.

Uses: `@reui/frame`

### `card-43`

Profile card with cover banner, verified avatar, and horizontal project portfolio rail

Profile card with a desaturated cover banner, ring avatar with status badge and verified check, and a horizontal-scrolling portfolio rail of project thumbnails. Built with ReUI Frame, Avatar, ScrollArea, Button. For team or contributor profiles.

Uses: `@reui/frame`

npm: `@base-ui/react`


## chart (30)

### `chart-1`

Inventory KPI summary card with period tabs and per-metric sparkline trends

Catalog health overview: Week/Month/Year tabs switch four inventory KPIs (in stock, out-of-stock, restock, slow movers), each with a recharts sparkline and tone-coded delta. ReUI Frame and Badge; shadcn Tabs, Chart, Button. Stats dashboard widget.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-2`

Four-column KPI stat row with corner line sparklines and trend badges

Bordered row of compact KPI stat cards, each pairing a big value with a top-right line sparkline (hover tooltip) and an up/down trend badge. Built with ReUI Frame and Badge plus shadcn Chart over Recharts. For dashboard metric strips and analytics.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-3`

Portfolio Balance Cards with Bottom-Anchored Line Charts on a Dotted Bed

Three-column grid of balance cards, each with an icon tile, total value, up or down percent change, and a full-width line chart over a dotted background. Built with ReUI Frame and shadcn ChartContainer for wallet, fund, and portfolio dashboards.

Uses: `@reui/frame`

npm: `recharts`

### `chart-4`

Account Balance Line Chart with Reference Line, Peak Dots and Stat Header

Portfolio balance tracker: a stat header (balance, trend, High, Low, Change) over a recharts line chart with a date reference line and custom dots on peaks and troughs. ReUI Frame, FramePanel, shadcn ChartContainer. For finance, trading dashboards.

Uses: `@reui/frame`

npm: `recharts`

### `chart-5`

Finance KPI metric grid with delta badges, brand logo stacks and mini area sparklines

Finance overview KPI grid: net worth, portfolio, investments and cashflow cards with delta badges, brand logo stacks, and mini area-chart sparklines. Uses ReUI Frame and Badge plus shadcn Chart. For wealth, fintech, crypto dashboards.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-6`

Metric-switcher line chart card with clickable KPI tabs and pulsing animated dots

Platform analytics card where four KPI tabs (orders, response, revenue, users) with percent-change badges switch a single dashed line series. ReUI Frame, Badge, shadcn Button, ChartContainer, recharts LineChart. Metrics dashboard, trend chart.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-7`

Two metric panels with semicircular segmented arc gauges and reviewer avatar stacks

Side-by-side metric cards showing uptime and code coverage as SVG segmented arc gauges with status label, value, and overlapping reviewer avatars. ReUI Frame, shadcn Avatar group, Button. KPI dashboard, gauge widget.

Uses: `@reui/frame`

### `chart-8`

Three-column KPI metric row with radial segmented gauges and trend indicators

Stat card row for API and ops monitoring: each metric pairs a segmented radial gauge with a value, unit, and up or down trend delta. Built on ReUI Frame and FramePanel with shadcn Button. Use for dashboard KPI strips, metrics overview, and stats.

Uses: `@reui/frame`

### `chart-9`

Capital Inflows fund breakdown card with segmented distribution bar and range filter

Fund inflow card: compact total with success trend Badge, a segmented distribution bar of each fund's share, and a logo, name, capital-in list. Top 3 to All filter via Select. ReUI Frame, Badge, shadcn Select. For treasury dashboards.

Uses: `@reui/badge`, `@reui/frame`

### `chart-10`

Heart rate metric card with segmented zone bar and large bpm readout

Compact health stat card showing a big bpm value, heart icon tile, and a 4-segment heart-rate zone meter (rest to peak) with one active band. Built on ReUI Frame and shadcn Button. For fitness, wearable, and vitals dashboards.

Uses: `@reui/frame`

### `chart-11`

Distance Metric Card with Week, Month, Year Tabs and Dotted Sparkline Fill

Cycling distance KPI card that swaps a dotted area sparkline and value across Week, Month, and Year tabs. Built with ReUI Frame and shadcn Tabs for fitness, activity, or analytics stat panels and metric widgets.

Uses: `@reui/frame`

### `chart-12`

Capital inflows semicircular gauge card with source breakdown and range switcher

Half-donut radial gauge of capital inflows by source, with center total, a range switcher (week, month, quarter), and per-source metric breakdown. Built with ReUI Card, DropdownMenu, Item, Separator, and a recharts PieChart. For finance dashboards.

npm: `recharts`

### `chart-13`

Capital inflows donut chart card with Week, Month, Year tabs and a per-source legend

Donut chart card breaking down capital inflows by source, with Week/Month/Year tabs, center total, and a legend of each source's amount and percent share. ReUI Frame plus shadcn Chart (recharts pie), Tabs, Tooltip. For finance and revenue breakdowns.

Uses: `@reui/frame`

npm: `recharts`

### `chart-14`

Portfolio Allocation Card with Week/Month/Year Tabs and Segmented Bar Meter

Finance allocation card: percentage metric with up delta, a segmented vertical-bar meter, equities exposure, and a member avatar stack. Card, Tabs, Tooltip, Avatar. For portfolio, investment, fund dashboards.

### `chart-15`

Three KPI stat cards with gradient sparkline area charts and hover tooltips

Responsive row of metric cards, each pairing an icon, label, period and big value with a compact gradient area sparkline and hover tooltip. ReUI Frame, Recharts AreaChart. KPI dashboard, revenue and user stats overview.

Uses: `@reui/frame`

npm: `recharts`

### `chart-16`

Conversion Funnel Stacked Area Chart with Stage KPI Tiles and Period Selector

Ecommerce funnel as a stacked area chart over visits, product views, add to cart, and checkout, with four KPI tiles (value plus trend), a 7d/30d/90d/12m period selector, and custom tooltip. ReUI Frame, shadcn ChartContainer and Select.

Uses: `@reui/frame`

npm: `recharts`

### `chart-17`

Compact campaign analytics card with gradient area chart and 5D to 6M period tabs

Marketing impressions card: total stat with +42% trend, gradient AreaChart (recharts), and period tabs (5D, 2W, 1M, 6M) that swap the dataset. ReUI Frame plus shadcn Tabs, Item, Tooltip, Button, Chart. For analytics dashboard, campaign KPI widget.

Uses: `@reui/frame`

npm: `recharts`

### `chart-18`

Orders overview card with period tabs, stat tiles, and animated gradient area chart

Analytics overview card with Day, Week, Month, Year range Tabs, three stat tiles showing delta changes, and a recharts area chart with animated reveal and dark tooltip. ReUI Frame, shadcn Tabs, Item. For dashboard revenue or sales summary panels.

Uses: `@reui/frame`

npm: `recharts`

### `chart-19`

Dark finance metric card with composed area-and-line chart and day, week, month period tabs

Dark DeFi-style stats card pairing Total Value Locked, Deposits and Borrowed KPIs with a Recharts composed chart of two gradient areas, monotone lines and a custom tooltip. Day, week, month switch via ReUI Card, Tabs. Crypto dashboard.

npm: `recharts`

### `chart-20`

Sales vs goals composed line and area chart with vertical reference line marker

Sales overview card plotting actual vs goal lines over a gradient area fill, with a dashed vertical reference marker, dollar-to-millions axis, custom tooltip, and Export/Filter/Share dropdown. ReUI Card, Button, DropdownMenu. For revenue dashboards.

npm: `recharts`

### `chart-21`

Cashflow area and line chart card with period range selector and total plus percentage trend

Cashflow chart card pairing a gradient Area with a dotted Line, a 6m/12m/2y range Select, a total with a green percentage trend, and a custom tooltip. Built with ReUI Frame, shadcn Select and ChartContainer. For finance and analytics dashboards.

Uses: `@reui/frame`

npm: `recharts`

### `chart-22`

Revenue performance card with line chart and period tabs (5D / 2W / 1M)

Compact revenue KPI card with a single-series recharts line chart, a total computed from the active period, and 5D / 2W / 1M tab switching. Uses ReUI Card, Tabs, Button, Item, ChartContainer. For analytics, finance, and sales reporting widgets.

npm: `recharts`

### `chart-23`

Multi-line social media activity chart with platform comparison and time-range selector

Multi-line chart comparing Facebook, Instagram and LinkedIn activity over a selectable time range, with custom tooltip and dot legend. ReUI Frame and Select, shadcn ChartContainer, Recharts LineChart. For analytics dashboards and engagement trends.

Uses: `@reui/frame`

npm: `recharts`

### `chart-24`

Dual-axis e-commerce sales vs views line chart with period selector and KPI trend badges

Plots sales and views on two independent Y-axes as solid and dashed recharts lines, with a 30 vs 90 day Select, KPI totals plus trend Badges, and a dark custom tooltip in a ReUI Frame. For e-commerce analytics and revenue vs traffic dashboards.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-25`

Order Metrics List Card with Per-Row Line Sparklines and Trend Badges

Vertical KPI metrics list: each row pairs a value, suffix, and up or down trend Badge with a compact line sparkline over a grid. Uses ReUI Frame, Badge and shadcn ChartContainer, Separator. For orders, spend and finance dashboards.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-26`

Dark floor price analytics card with period tabs and monotone line chart

Crypto and NFT floor price tracker on a dark Card: Month / Max Tabs toggle, recharts monotone LineChart, large current price with percent change. For asset dashboards, token price and portfolio widgets. Uses ReUI Card, Tabs, Button, Chart.

npm: `recharts`

### `chart-27`

Browser usage donut chart card with 5D, 2W and 1M period tabs and total visitors KPI

Donut chart of visitor share across browsers with a 5D/2W/1M tab switcher, total visitors stat, trend badge and slice labels. Uses ReUI Frame and Badge plus shadcn Tabs, Item, Button and recharts Pie. For analytics dashboards and traffic widgets.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-28`

Operational KPI metric cards with segmented bar gauge for utilization and capacity tracking

Three operational KPI cards in a responsive grid, each with an icon, title, large value over total, and a 40-segment bar gauge showing utilization. Built with ReUI Frame, recharts BarChart, shadcn Item and Button. For dashboards and capacity metrics.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-29`

Inventory velocity bar chart card with diagonal hatched bars and dotted backdrop

Vertical bar chart in a card showing warehouse turnover by category, with diagonal hatched-pattern bars, dotted grid backdrop, grow-up reveal animation, and a custom tooltip. Uses ReUI Frame, Badge, recharts. Analytics, dashboard, KPI.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `chart-30`

Grouped air vs sea freight bar chart with hover-dimmed bars and live region readout

Grouped bar chart comparing air vs sea freight transit days across global regions, with hover that dims other bars, a live region readout, custom tooltip, and trend badge. ReUI Frame, Badge; shadcn Chart on Recharts. Logistics shipping dashboard.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`


## dashboard (8)

### `dashboard-1`

Operations dashboard with KPI stat cards, capacity charts, and a filterable exception data grid

Fulfillment control center: metric cards, shift performance, capacity allocation tabs, a donut flow chart, and a searchable paginated exception queue. Uses ReUI Frame, Badge, DataGrid plus Tabs, Select, Progress, breadcrumb, and a date-range picker.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`, `recharts`, `sonner`

### `dashboard-2`

Operations Dashboard with Sparkline Metric Cards and Searchable Module Data Grid

Operations console: sticky navbar with team presence and invite, three area-chart metric cards, and a paginated module DataGrid with progress rings, search, sort, and status filters. ReUI DataGrid, Badge; shadcn Card, Avatar, Popover, DropdownMenu.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`

npm: `@tanstack/react-table`, `recharts`, `sonner`

### `dashboard-3`

Project delivery dashboard with tabbed header and weekly per-person worklog timesheet grid

Delivery workspace: tabbed header with breadcrumb and collaborator avatars, account summary cards, a filterable weekly worklog timesheet DataGrid with week navigation, integration cards and Empty tab states. ReUI Frame, DataGrid, Badge; shadcn Tabs.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/icon-stack`

npm: `@tanstack/react-table`, `date-fns`

### `dashboard-4`

Voice Agent Call Analytics Dashboard with Tabbed Metric Switcher and Composed Area Chart

Call analytics overview for voice AI ops: six-metric tab switcher (calls, duration, cost, LLM cost) over a recharts area-line chart, ranked agent bars, and integration status list. ReUI Frame, Badge with shadcn Button, Select, Chart, Item.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `dashboard-5`

Edge Security Telemetry Dashboard with KPI Sparkline Tiles, Threat Charts and Node Load Bars

Security ops dashboard: 4 KPI tiles with SVG sparklines, threat-vector and network-flow charts, per-node cluster load bars, active threat progress lanes, date-range picker. ReUI Badge, shadcn Card, Chart, Breadcrumb. SOC, NOC, monitoring.

Uses: `@reui/badge`

npm: `date-fns`, `react-day-picker`, `recharts`, `sonner`

### `dashboard-6`

Field Workforce Coverage Dashboard with Crew Table, Action Queue, and Supply vs Forecast Chart

Workforce ops dashboard for shift coverage: metric tiles, a crew Table with coverage progress bars and status, an action queue, and a stacked supply vs forecast ComposedChart. Uses ReUI Frame, Badge with shadcn Table, Avatar, Item, Chart, Breadcrumb.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`, `sonner`

### `dashboard-7`

Retail revenue dashboard with KPI sparkline cards, stacked sales charts, and a sortable order queue

Commerce revenue dashboard: 4 KPI cards with sparklines and trend deltas, a stacked area revenue chart, a channel-mix bar chart, and a searchable, paginated order queue with fulfillment bars. ReUI Frame, Badge, DataGrid; shadcn Chart and Calendar.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`, `recharts`

### `dashboard-8`

Creator royalty payout dashboard with sweep-lane payout control and a sortable ledger DataGrid

Creator finance desk to clear royalties: command band with claimable balance, receipts vs buffer area chart, payout buffer progress and sweep lanes, plus a searchable ledger. ReUI Frame, Badge, DataGrid; shadcn Calendar, Select, DropdownMenu, Chart.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`

npm: `@tanstack/react-table`, `date-fns`, `react-day-picker`, `recharts`, `sonner`


## dialog (14)

### `dialog-1`

Duration picker dialog with start and end time selects plus quick preset toggles

Modal for choosing a time span: start and end time Selects plus quick presets (30 min to 1 day) that auto-adjust the end time. Built with ReUI Dialog, Select, ToggleGroup, Field, Tooltip, Button. Time range picker, schedule, booking duration.

### `dialog-2`

Workspace invite dialog with multi-email input and role select dropdown

Team invite modal that parses comma or space separated emails, dedupes them, and shows a live 'Send N invites' count. Pick a role per invite. Uses ReUI Badge with shadcn Dialog, Input, Field, Select, Button.

Uses: `@reui/badge`

### `dialog-3`

Plan cancellation dialog with multi-select reason checkboxes, feedback textarea, and warning banner

Subscription offboarding dialog: warning Alert with dismiss and manage actions, a checkbox grid of reasons, a feedback Textarea, and a Cancel plan button gated until a reason is picked. ReUI Alert, shadcn Dialog, Checkbox, Tooltip. Churn flows.

Uses: `@reui/alert`

### `dialog-4`

Workspace launch checklist dialog with accordion sections and inline-editable fields

Setup dialog with accordion sections, status badges, click-to-edit field rows, and a searchable connected-apps list with Connect or Manage. ReUI Badge, shadcn Dialog, Accordion, Item, InputGroup. Workspace setup, launch checklist, settings wizard.

Uses: `@reui/badge`

npm: `sonner`

### `dialog-5`

Wide template library dialog with category rail, live search, and selectable template cards

Template gallery picker dialog: fixed category rail (radio group), live search input, and selectable cards with thumbnail and badges. Uses ReUI Badge with Dialog, Input, ScrollArea, RadioGroup, Item. Starter library, template browser, asset picker.

Uses: `@reui/badge`

### `dialog-6`

App connection dialog with searchable integration grid and single-select checkbox cards

Modal to connect a workspace app: search-filtered grid of brand-logo cards with round single-select Checkbox and a footer add button disabled until a pick. Uses ReUI Dialog, InputGroup, Kbd, Item, Empty. Integrations picker, connect-app, marketplace.

### `dialog-7`

Help and support hub dialog with self-serve routes plus advisor and direct-desk escalation cards

Support hub modal: help routes (guides, walkthroughs, feedback) above an escalation grid pairing an advisor office-hours card with an email-support desk. Uses shadcn Dialog, Item, Card, Avatar, Button and ReUI Badge. Contact support, help center.

Uses: `@reui/badge`

### `dialog-8`

Multi-row collaborator invite dialog with per-row email field and role select

Invite teammates by email with a per-row role select (Member, Contributor, Reviewer, Admin), add and remove rows, and inline email validation. Uses ReUI Dialog, Input, Field, Select, Button. Team invite modal, add members, share access.

### `dialog-9`

Create project dialog with cover image upload and status, priority, assignee, and label comboboxes

Modal new-project form with drag-and-drop cover upload, name, key, brief fields, single-select status and priority plus multi-select assignee and label comboboxes. Dialog, Combobox, Avatar, Tooltip, Alert. Add project, create workspace.

Uses: `@reui/alert`, `@reui/use-file-upload`

### `dialog-10`

Tabbed account settings dialog with sidebar rail for profile, workspace, team and billing

Modal account settings dialog with a 5-tab sidebar (Profile, Workspace, Team, Billing, Preferences); each scrollable panel pairs labels with avatar upload, Inputs, Selects, Switches and a verified Badge. Uses Dialog, Tabs, ScrollArea, Field.

Uses: `@reui/badge`, `@reui/use-file-upload`

### `dialog-11`

Two-pane finance account creation dialog with live account card preview

Split dialog to create a finance account: account name, acct_ tag, and statement label fields beside a live-updating account card on a gradient panel. Uses ReUI Dialog, Card, Field, Input, InputGroup, Button. For payout, banking, onboarding setup.

### `dialog-12`

Tabbed create-entry dialog with status, assignee, due date, priority and label comboboxes

Quick-create record dialog with five entry-type tabs, each a title and notes field plus shared Status, Assignee, Due date, Priority and Labels comboboxes. Uses ReUI Combobox, Tabs, Dialog, Calendar, Avatar. For task creation and new-item modals.

npm: `date-fns`, `sonner`

### `dialog-13`

Full-screen create project dialog with template prefill and multi-select labels

Full-screen create-project form: a template dropdown prefills fields, status, assignee, due date and priority Selects with avatars and dots, plus checkbox label cards with a selected count. ReUI Badge, shadcn Dialog, Select, InputGroup, Field.

Uses: `@reui/badge`

### `dialog-14`

OAuth connection consent dialog with provider logo rail and radio sync-scope picker

App integration consent modal: paired provider logos, permission notes, and a radio-group scope selector with cancel/continue. Built with ReUI Dialog, RadioGroup, Item, Field, Button. For OAuth handoff, connect-account, grant-access flows.


## empty-state (14)

### `empty-state-1`

Records empty state with stacked-cards illustration, dual primary actions, and quick-guide link rows

First-run empty state for a records or workspace table: stacked-cards illustration, Connect source and Upload CSV buttons, plus a two-up Quick guides list. Built with ReUI Empty, Button, and Item. Use for zero-data, onboarding, or no results screens.

### `empty-state-2`

Search no-results empty state with suggestion chips and a stacked result-card illustration

Workspace search zero-state: a stacked result-card illustration, paired Browse library and Refine filters actions, and a 'Try these searches' row of pill suggestion chips. Built with ReUI Empty, ButtonGroup, Button. For no-results, search hints.

### `empty-state-3`

Projects empty state with hero illustration, dual actions, and quick-start template list

No-projects empty state for a workspace: hero illustration, New project and Explore templates buttons, and a Quick starts grid of clickable template cards. Uses ReUI Empty, Button, Item. Good for onboarding, first-run, zero-data screens.

### `empty-state-4`

Two-column reports empty state with icon, dual actions, and preview screenshot slot

Split empty state for an empty reports or analytics workspace: icon, title, helper copy, and Add report plus View sample buttons beside a blank screenshot preview panel. Uses ReUI Card and Empty with shadcn Button.

### `empty-state-5`

Two-column empty state in a ReUI Frame with icon, dual actions, and a preview panel

Split empty state for a no-data briefing or report view. Left column pairs an icon, title, and description with primary and outline Buttons; right column is a preview surface. Uses ReUI Frame, shadcn Empty and Button. For blank dashboards.

Uses: `@reui/frame`

### `empty-state-6`

Team workspace onboarding empty state with two action buttons and three colored setup-step tiles

Centered team workspace onboarding empty state pairing two outline action Buttons with three colored clickable setup tiles. Uses ReUI Empty and Item primitives. For workspace setup, first-run onboarding, getting-started checklist.

### `empty-state-7`

Workspace member invite empty state with circular icon and dual invite and copy-link buttons

Centered empty state prompting the first workspace invite, with a ring-framed icon, title, description, and two CTAs (Invite members, Copy invite link). Uses ReUI Empty and Button. For team onboarding, members page, no-members placeholder.

### `empty-state-8`

Project settings empty state with line tabs and per-section setup prompts

Settings header over line-style Tabs (project states, labels); each tab shows a left-aligned Empty with icon, title and Enable button. ReUI IconStack with shadcn Tabs, ScrollArea, Empty, Button. For settings onboarding and zero-states.

Uses: `@reui/icon-stack`

### `empty-state-9`

Workspace member invite empty state with layered 3D icon-stack illustration and dual invite actions

Centered empty state prompting the first workspace invite, with a stacked-card icon illustration, title, supporting text, and primary Invite members plus outline Copy invite link buttons. Uses ReUI IconStack, shadcn Empty, Button.

Uses: `@reui/icon-stack`

### `empty-state-10`

Card-wrapped empty state with section heading and horizontal media-beside-text layout

Empty state inside a Card under a section heading for a template or blueprint library with no items. Horizontal media beside title, description, and two buttons. ReUI IconStack with shadcn Card, Empty, Button. For blank library or first-run views.

Uses: `@reui/icon-stack`

### `empty-state-11`

Section-header empty state with action button above a muted card and stacked icon illustration

Empty state for a list or feed section: heading, subtext, and Add button over a muted Card holding a layered stacked-icon illustration, title, and hint. ReUI IconStack with shadcn Empty, Card, Button. For zero-data panels and intake views.

Uses: `@reui/icon-stack`

### `empty-state-12`

Activity exports empty state with audience, workspace, and date-range filter toolbar

Export empty state: header, three dropdown filters (audience, workspace, date range), and a split Execute button with CSV, PDF, and scheduled delivery. Uses ReUI IconStack, shadcn Empty, ButtonGroup, DropdownMenu. For export no-results screens.

Uses: `@reui/icon-stack`

npm: `sonner`

### `empty-state-13`

File sources empty state with cloud storage connector grid (Dropbox, Box, Drive, OneDrive)

Empty state for linking cloud storage: header, IconStack illustration, and a responsive grid of brand-logo connect buttons (Dropbox, Box, Google Drive, OneDrive). ReUI Frame, IconStack, shadcn Empty, Separator. For integrations screens.

Uses: `@reui/frame`, `@reui/icon-stack`

### `empty-state-14`

Organizations setup empty state with framed enable card, building icon, and tooltip help link

Organizations settings empty state to enable multi-org with team members and role-based access. Framed card with stacked building icon, enable CTA, and a tooltip help link. ReUI Frame, IconStack, shadcn Empty, Button, Tooltip, Separator.

Uses: `@reui/frame`, `@reui/icon-stack`


## event-calendar (6)

### `event-calendar-1`

Event calendar with month, week, day, N-day, and agenda views plus drag-and-drop editing

Scheduling workspace on ReUI Event Calendar: month, week, day, N-day, agenda and resource views, drag to move, resize and create events, recurrence, and an edit dialog. ReUI Event Calendar with shadcn Dialog, Select. Booking calendar, scheduler.

Uses: `@reui/badge`, `@reui/event-calendar`, `@reui/event-calendar-content`, `@reui/event-calendar-event`, `@reui/event-calendar-nav`, `@reui/event-calendar-types`

npm: `date-fns`, `sonner`

### `event-calendar-2`

Calendar workspace with mini month picker, calendars visibility list, and up-next agenda sidebar

Two-panel calendar workspace: a sidebar mini month picker, calendars visibility list, and up-next agenda drive a week-view event calendar with drag, resize, and full event plus calendar CRUD.

Uses: `@reui/badge`, `@reui/event-calendar`, `@reui/event-calendar-content`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-nav`, `@reui/event-calendar-recurrence`, `@reui/event-calendar-types`

npm: `date-fns`, `react-day-picker`, `sonner`

### `event-calendar-3`

Hotel front-desk booking board with arrivals agenda and color-coded service streams

Front-desk hotel booking board on a week time grid: a sidebar mini month picker, arrivals agenda, and colour-coded service streams drive an hourly calendar of check-ins, check-outs, housekeeping turnovers, functions, and guest services, with drag, resize, and full booking plus stream CRUD.

Uses: `@reui/badge`, `@reui/event-calendar`, `@reui/event-calendar-content`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-nav`, `@reui/event-calendar-recurrence`, `@reui/event-calendar-types`, `@reui/icon-tile`

npm: `date-fns`, `react-day-picker`, `sonner`

### `event-calendar-4`

Workforce shift roster with coverage avatars, open-slot warnings, and a double-booking guard

Workforce shift scheduling board for HR and operations teams: a day, week, and month event calendar of staffing shifts grouped into color-coded departments, with per-shift coverage showing assigned staff avatars, required headcount, and open-slot warnings, plus search across shifts and staff, an open-slots filter, drag and resize with a double-booking guard, publish and unpublish locking, and full CRUD on shifts, assignments, and departments.

Uses: `@reui/alert`, `@reui/badge`, `@reui/event-calendar`, `@reui/event-calendar-content`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-nav`, `@reui/event-calendar-types`, `@reui/number-field`

npm: `date-fns`, `sonner`

### `event-calendar-5`

Clinic chair board with per-practitioner columns, status-tinted chips, and drop-rejecting clinic holds

Clinic day board on the event calendar resource view: one column per practitioner with avatar headers and live patient counts, status-tinted appointment chips, hatched clinic holds that reject drops, a searchable patient lookup, day and week switching, a multi-select chair picker and status filters, full appointment CRUD, and a Log History tab fed by every desk action.

Uses: `@reui/badge`, `@reui/event-calendar`, `@reui/event-calendar-content`, `@reui/event-calendar-nav`, `@reui/event-calendar-types`, `@reui/icon-tile`

npm: `date-fns`, `sonner`

### `event-calendar-6`

Commercial lending calendar with multi-row deal chips and covenant detail cards on hover

Commercial lending calendar in month, week, day, and agenda views. Multi-row chips carry a loan reference, category tag, counterparty, attendee avatars, and a task progress bar, stage, or join-call row. Hovering a chip opens a detail card with the covenant clause, due date, and pass or fail tallies.

Uses: `@reui/badge`, `@reui/event-calendar`, `@reui/event-calendar-content`, `@reui/event-calendar-lib`, `@reui/event-calendar-nav`, `@reui/event-calendar-types`

npm: `date-fns`, `sonner`


## form (12)

### `form-1`

Profile settings card form with completion badge and date-plus-time availability picker

Profile settings Card form: avatar upload, birth date and availability date-time Calendar pickers, multi-select specialty Combobox chips, visibility Select, available-to-hire Switch, completion Badge. For account settings, edit profile, preferences.

Uses: `@reui/badge`, `@reui/use-file-upload`

npm: `date-fns`, `sonner`

### `form-2`

Hosted checkout setup form with label-and-control rows, Select dropdowns, and checkbox groups

Configure a hosted checkout: offer type, button copy, and handoff via ReUI Frame and Badge with shadcn Field rows, Select, Checkbox groups, InputGroup, Tooltip, and Button. Settings form, payment config, store admin panel.

Uses: `@reui/badge`, `@reui/frame`

npm: `sonner`

### `form-3`

Invoice creator form with editable line-items table and live discount, tax, and total summary

Invoice builder with customer combobox, date pickers, currency and term selects, an editable line-items table, and a live subtotal, discount, tax, and total panel. ReUI Badge with shadcn Card, Table, Combobox, Calendar. For billing and invoicing.

Uses: `@reui/badge`

npm: `date-fns`, `sonner`

### `form-4`

Authentication settings form with line tabs for email, phone, password, passkey, and lockout policy

Auth method config page: line tabs switch Email, Phone, Password, Passkeys, Protection, and User Model panels of Switch, Select, RadioGroup, and Input rows with Pro/Beta badges, tooltips, alerts, and a save/discard toast footer.

Uses: `@reui/alert`, `@reui/badge`

npm: `sonner`

### `form-5`

Tabbed user profile settings form with sticky audit rail and activity heatmap

Admin profile editor with Profile, Organizations, Security tabs, a sticky audit rail of IDs and timestamps, completion Progress, and activity heatmap. ReUI Badge with shadcn Card, Field, Combobox, Switch. For account settings, member detail pages.

Uses: `@reui/badge`, `@reui/use-file-upload`

npm: `@base-ui/react`, `sonner`

### `form-6`

Business Verification Review Page with Editable Detail Sections and Dialog Forms

KYC business verification summary with read-only Frame panels for legal, public, and ownership details, each opening a Dialog edit form. ReUI Frame, Badge plus shadcn Dialog, Field, Select, Tooltip. Account review, onboarding, compliance.

Uses: `@reui/badge`, `@reui/frame`

npm: `sonner`

### `form-7`

Inline-editable ticket details panel with per-row save, status and SLA badges, tags and owner chips

Support ticket detail panel where each field edits inline with save, cancel, and async saving toasts. Status, priority, SLA, due-date, tag and owner chips. ReUI Frame, Badge with Select, Combobox, Calendar, Switch. For helpdesk and issue trackers.

Uses: `@reui/badge`, `@reui/frame`

npm: `sonner`

### `form-8`

API keys management panel with per-stack env snippet quick-copy and reveal, rotate, revoke rows

API keys settings page: copy framework .env snippets, reveal, rotate, or revoke masked keys, plus a create-key dialog with scopes, owners, and expiration. ReUI Frame, Badge, Alert with Dialog, Combobox, Select, InputGroup.

Uses: `@reui/alert`, `@reui/badge`, `@reui/frame`

npm: `@base-ui/react`, `sonner`

### `form-9`

Enterprise member invite form with searchable role permission tree and access guardrails

Invite teammates and assign scoped workspace roles: email combobox chips, workspace and expiry selects, member-type radios, SSO switches, and a searchable checkbox role tree with privileged badges. ReUI Badge and Tree, shadcn Card. For RBAC.

Uses: `@reui/badge`, `@reui/tree`

npm: `@headless-tree/core`, `@headless-tree/react`, `sonner`

### `form-10`

Customer onboarding intake form in a Card with labeled rows and multi-owner combobox

New-workspace setup form: company, slug, intent radios, team size, launch window, template, data source, owner chips, sample-data toggle, notes. Uses ReUI Badge, shadcn Card, Combobox, RadioGroup, Select, Switch, Textarea. Account setup wizard.

Uses: `@reui/badge`

npm: `sonner`

### `form-11`

New App Launch Form with Gradient Summary Banner and Label-Control Rows

App launch form in a Card with a gradient banner that live-mirrors picks. Rows pair a brief Textarea, prefixed App URL InputGroup, name Input, and starter, source, runtime, region Selects. For deploy and project setup wizards.

Uses: `@reui/badge`

npm: `sonner`

### `form-12`

Ecommerce product creation form with image upload, pricing, inventory, and collections combobox

Create product form in a Card with label-control rows: multi-image thumbnail dropzone, Select status and category, currency InputGroup pricing, SKU and stock, Switch toggles, multi-select Combobox collections. Product catalog, add product, admin.

Uses: `@reui/alert`, `@reui/badge`, `@reui/use-file-upload`

npm: `sonner`


## gantt (4)

### `gantt-1`

Project gantt with resizable tree columns, split timeline panes, and inline editing

Project timeline on ReUI Gantt: task tree in a resizable split pane beside a day-to-year timeline, drag and resize bars with live validation, progress rollups, and an edit dialog. ReUI Gantt with shadcn Dialog, Select. Roadmap, project planner.

Uses: `@reui/badge`, `@reui/gantt`, `@reui/gantt-bar`, `@reui/gantt-lib`, `@reui/gantt-nav`, `@reui/gantt-types`, `@reui/gantt-view`

npm: `date-fns`, `sonner`

### `gantt-2`

Day dispatch gantt with technician rows and timed jobs on an hour grid

Hour grid day dispatch with technician rows and timed jobs

Uses: `@reui/badge`, `@reui/gantt`, `@reui/gantt-nav`, `@reui/gantt-types`, `@reui/gantt-view`

npm: `sonner`

### `gantt-3`

Agent playbook gantt with enforced stage dependencies, retry lanes, and a critical path

Agent playbook board with enforced stage dependencies, retry lanes and critical path

Uses: `@reui/alert`, `@reui/badge`, `@reui/gantt`, `@reui/gantt-nav`, `@reui/gantt-types`, `@reui/gantt-view`

npm: `sonner`

### `gantt-4`

Capacity-aware resource gantt with booking cards, drag guardrails, and full CRUD

Capacity aware resource gantt with booking cards, drag guardrails and full CRUD

Uses: `@reui/alert`, `@reui/badge`, `@reui/gantt`, `@reui/gantt-nav`, `@reui/gantt-types`, `@reui/gantt-view`

npm: `date-fns`, `sonner`


## kanban-board (10)

### `kanban-board-1`

Drag-and-drop issue tracking kanban board with six status columns and per-task completion rings

Bug tracking board: drag tasks across six status columns, reorder columns, with priority, signal dots, owner avatars, due dates, and SVG completion rings. ReUI Kanban, Badge; shadcn Card, Avatar, Button. Sprint board, backlog, task tracker.

Uses: `@reui/badge`, `@reui/kanban`

npm: `@base-ui/react`

### `kanban-board-2`

Workflow kanban board with collapsible status columns and draggable cards plus columns

Drag-and-drop kanban for project and CRM workflows: 8 status columns collapse to vertical rails, reorderable cards and columns, count badges, deal value and assignee avatars. Uses ReUI Kanban and Badge with shadcn Card, Button, Avatar.

Uses: `@reui/badge`, `@reui/kanban`

npm: `@base-ui/react`, `@dnd-kit/sortable`

### `kanban-board-3`

Sales pipeline kanban board with draggable deal cards and reorderable stages

CRM sales pipeline board with drag-and-drop deals across six stages. Deal cards show company logo, value, next step, owner avatar, star rating, and attachment/comment counts. ReUI Kanban, Badge, Rating, shadcn Card, Avatar, Button.

Uses: `@reui/badge`, `@reui/kanban`, `@reui/rating`

npm: `@base-ui/react`, `@dnd-kit/sortable`

### `kanban-board-4`

Feature roadmap kanban board with vote-weighted cards across six delivery stages

Drag-and-drop product roadmap board with six status columns and reorderable cards showing votes, vote-trend arrows, progress bars, and impact or ARR. Feature voting, planning board, backlog. ReUI Kanban, Frame, Badge with Progress, Button.

Uses: `@reui/badge`, `@reui/frame`, `@reui/kanban`

npm: `@base-ui/react`, `@dnd-kit/sortable`

### `kanban-board-5`

Workflow status kanban board with collapsible column rails and per-task progress rings

Drag-and-drop status workflow kanban: reorder cards and columns, collapse columns to vertical rails, with progress rings, owner avatars, and status badges. ReUI Kanban, Badge plus shadcn Card, Item, Avatar. Task board, project tracker, sprint board.

Uses: `@reui/badge`, `@reui/kanban`

npm: `@base-ui/react`, `@dnd-kit/sortable`

### `kanban-board-6`

Support escalation kanban board with SLA timer chips, priority badges, and draggable columns

Help-desk board with six SLA-state columns. Drag-and-drop ticket cards and reorderable columns show SLA countdown chips, priority badges, and assignee avatars. ReUI Kanban, Badge; shadcn Card, Item, Avatar. For support queue and ticket triage tools.

Uses: `@reui/badge`, `@reui/kanban`

npm: `@base-ui/react`, `@dnd-kit/sortable`

### `kanban-board-7`

Customer renewals risk kanban board with ARR, health score, and risk-tier account cards

Drag-and-drop renewals board, six risk stages, account cards with ARR, renewal date, days left, color-coded health bar, owner, and Critical/Warning/Clear status. CSM pipeline, churn risk. ReUI Kanban, Badge; shadcn Card, Progress, Avatar.

Uses: `@reui/badge`, `@reui/icon-stack`, `@reui/kanban`

npm: `@base-ui/react`, `@dnd-kit/sortable`

### `kanban-board-8`

Release readiness kanban board with risk badges, checklist progress, and drag-and-drop change cards

Six-column pipeline (Intake to Shipped) with draggable change cards showing risk badge, service, environment, owner avatar, launch window, and checklist progress. ReUI Kanban, Frame, Badge plus shadcn Item, Avatar, Progress. Deploy and release board.

Uses: `@reui/badge`, `@reui/frame`, `@reui/kanban`

npm: `@base-ui/react`

### `kanban-board-9`

Recruiting pipeline kanban board with candidate match scores and scorecard status

Applicant tracking board: six draggable pipeline stages from Sourced to Offer, candidate cards with match-score progress bars, scorecard badges, and risk flags. ReUI Kanban, Frame, Badge, Progress, Avatar, Button for ATS and hiring boards.

Uses: `@reui/badge`, `@reui/frame`, `@reui/kanban`

npm: `@base-ui/react`

### `kanban-board-10`

Access review kanban board with risk badges, star confidence rating, and reviewer avatars

IAM access certification board with draggable cards and columns across Intake, Owner Review, Risk, Exception, Removal, Certified. Risk-tiered cards show request IDs and avatars. ReUI Kanban, Badge, Rating with shadcn Card. Access governance, audit.

Uses: `@reui/badge`, `@reui/kanban`, `@reui/rating`

npm: `@base-ui/react`, `@dnd-kit/sortable`


## list (11)

### `list-1`

Order Metrics List Card with Icon Tiles and Up Down Trend Badges

Compact KPI metric list: framed icon tile, large value, colored up/down trend badge, and open-details button per divided row. ReUI Frame, Badge, shadcn Item, Button, Separator. Stats summary, dashboard, finance overview.

Uses: `@reui/badge`, `@reui/frame`

### `list-2`

Capital inflows fund leaderboard list with logo badges and a range filter select

Ranked fund inflow rows with a colored brand-logo badge, name, and Capital In amount, plus a Select to switch Top 3 / Top 5 / All. ReUI Frame, shadcn Select, Item, Separator. For leaderboards, top contributors, investor summary widgets.

Uses: `@reui/frame`

### `list-3`

Capital Inflows Card with Period Tabs and Ranked Fund List Showing Amount and Share

Capital inflows widget switching ranked fund rows by period tabs (Weekly, All Time); each row shows logo, name, dollar amount, percentage share. ReUI Frame, shadcn Tabs, Tooltip, Separator. For finance dashboards, top contributors, leaderboards.

Uses: `@reui/frame`

### `list-4`

Crypto Portfolio Snapshot List with Period Tabs and Per-Asset Trend Badges

Crypto holdings card switching between Weekly and All Time tabs, listing coins with logo, price, up or down trend badge, value and holdings. ReUI Frame, Badge with shadcn Tabs, Button, Separator. Portfolio, watchlist, asset tracker.

Uses: `@reui/badge`, `@reui/frame`

### `list-5`

Crypto Transactions List with Color-Coded Credit and Debit Amounts

Compact crypto transaction history list with directional credit/debit icons, title, date, and color-coded amounts. Uses ReUI Frame plus shadcn Item, Tabs, Separator. For wallet activity feeds and finance dashboards.

Uses: `@reui/frame`

### `list-6`

Crypto transaction list card with period tabs and dual-token swap amounts

Wallet activity card listing received, sent, swapped, and failed crypto transfers with token logos, truncated addresses, and color-coded amounts. Weekly and All Time tabs plus a View All footer. Uses ReUI Frame with Tabs, Item, Separator, Button.

Uses: `@reui/frame`

### `list-7`

Wallet Transactions List with Period Tabs and Color-Coded Category Icons

Transaction card with Weekly and All Time tabs; each row pairs a colored category icon with title, date, and a signed amount tinted green for credits or red for debits. ReUI Frame, shadcn Tabs, Item, Button. For wallet, banking, fintech feeds.

Uses: `@reui/frame`

### `list-8`

Integrations directory list with brand logos and per-row Connect buttons

Integrations directory card listing apps with brand logos, name, description, and a per-row Connect button, plus a See All footer link. ReUI Frame with shadcn Button and Separator. App marketplace, connected accounts, settings.

Uses: `@reui/frame`

### `list-9`

Manual integrations picker list with icon tiles, per-row add buttons, and Browse More footer

Integrations picker list with icon tiles, name plus truncated description per row, plus-button add actions, dashed dividers, and a Browse More footer. Uses ReUI Frame with shadcn Item, Button, Separator.

Uses: `@reui/frame`

### `list-10`

Recent Investments Card with Searchable Gain-Loss Table and Company Logos

Investments card: header with ⌘K search input, fixed table of company logo, name, date, sector, and green or red value change. ReUI Frame, FramePanel; shadcn Table, InputGroup, Item, Kbd.

Uses: `@reui/frame`

### `list-11`

Top movers list table with company logos, status badges, and up/down trend values

Top movers leaderboard table: company rows with logo and location, status badges (Active, New, On Hold), and a trend column with gain/loss value and up/down arrow. Header search with Cmd-K hint. ReUI Frame, Badge, shadcn Table, InputGroup, Kbd.

Uses: `@reui/badge`, `@reui/frame`


## navbar (13)

### `navbar-1`

Project workspace navbar with breadcrumb, line tabs, and a collaborator avatar stack

Project workspace header: breadcrumb trail, line tabs with a count Badge, search/star/more actions, an expanding Create New button, and a collaborator Avatar stack. Uses ReUI Badge, shadcn Tabs, Breadcrumb, Avatar, DropdownMenu, Button.

Uses: `@reui/badge`

### `navbar-2`

Sticky workspace navbar with breadcrumb trail, team presence avatars, and filter and sort menus

Slim sticky app bar: breadcrumb trail, team avatar group with invite popover, and filter, sort, and overflow dropdown menus. ReUI Breadcrumb, AvatarGroup, Popover, DropdownMenu, Button. For workspace headers and project toolbars.

### `navbar-3`

Developer platform top navbar with breadcrumb org, project and environment switchers

Header for dev tools and PaaS dashboards: breadcrumb of organization, project and color-dotted environment switchers, docs and settings menus, Upgrade button, avatar menu with light/dark/system theme toggle. ReUI Breadcrumb, DropdownMenu, Avatar.

npm: `next-themes`

### `navbar-4`

Admin console top navbar with centered Cmd+K command search and a notifications popover feed

Admin top bar: brand, centered Cmd+K command search Dialog with Kbd hint, notifications Popover feed (avatars, actions, progress, ratings) and a user DropdownMenu with theme toggle. ReUI Badge, Rating.

Uses: `@reui/badge`, `@reui/rating`

npm: `next-themes`

### `navbar-5`

Compact workflow editor navbar with active toggle, Test Run action, and history

Slim sticky toolbar for a workflow or automation builder: back link, active/inactive Switch, run-history button, Test Run action, and a more-options DropdownMenu (Export JSON, Duplicate, Share, Delete). Uses Button, Switch, Separator, DropdownMenu.

### `navbar-6`

Two-row analytics dashboard navbar with date range picker, compare toggle, and command-K search

Sticky analytics toolbar with breadcrumb title, calendar date range picker, compare toggle, auto-refresh select, share, export/embed dropdown, and command-K search dialog. ReUI Breadcrumb, Popover, Calendar, Select, DropdownMenu, Dialog, Kbd.

npm: `date-fns`, `next-themes`

### `navbar-7`

CMS editor navbar with co-presence avatars and a split Publish button

Sticky editor toolbar for content apps: back link and breadcrumb, AvatarGroup co-presence, Preview, and a ButtonGroup split Publish with Schedule and Save as draft, plus a more-actions DropdownMenu (duplicate, history, archive, delete).

### `navbar-8`

AI agent marketplace navbar with category filter pills, Deploy CTA, and notifications popover

Sticky AI agent marketplace navbar: centered category filter pills, Deploy CTA, notifications popover (avatar groups, star rating, progress, actions), and avatar dropdown with theme toggle. ReUI Badge, Rating, shadcn ButtonGroup, Popover.

Uses: `@reui/badge`, `@reui/rating`

npm: `next-themes`

### `navbar-9`

Code editor app header with repo path breadcrumb and branch dropdown selector

Sticky IDE-style navbar for a code collaboration tool: brand tile, org/repo Breadcrumb path, branch-picker DropdownMenu with deploy targets, and Share plus Run Button actions. ReUI Breadcrumb, DropdownMenu, Button, Item, Separator.

### `navbar-10`

API developer portal navbar with service switcher, HTTP request bar, and account menu

Top bar for an API console or dev portal: brand, service switcher (OpenAI, Stripe, Supabase logos), an inline HTTP method Select with endpoint Input and Send button, and an avatar menu with theme toggle. Uses ButtonGroup, DropdownMenu, Avatar.

npm: `next-themes`

### `navbar-11`

Design system manager top navbar with center section tabs, version badge, and sync source switcher

DesignOps app header: brand mark, version Badge, centered Tabs (Patterns, Tokens, Icons, Motion), sync-source DropdownMenu (shadcn, Cursor, Paper), and avatar menu with light/dark/system theme toggle. For design-system, tokens, and admin toolbars.

Uses: `@reui/badge`

npm: `next-themes`

### `navbar-12`

Marketing navbar with icon mega-menu dropdowns and a sliding-arrow Get Started button

Marketing top bar with two-column mega-menu dropdowns for Product and Company, a Pricing link, and a Get Started button with a hover slide-in arrow. Built on ReUI NavigationMenu, Item, Separator, Button. Use for SaaS site header or landing page nav.

### `navbar-13`

Compact editor action bar navbar with close button, document title, and submit action

Focused-mode bar for an invoice or document editor: close (X) button, vertical Separator, truncating title, a preview collapse toggle, and a submit button that confirms after click. Uses ReUI Button and Separator. For editor toolbar, draft bar.


## onboarding (9)

### `onboarding-1`

Six-step workspace onboarding wizard with stepper progress and a live inbox preview pane

Multi-step account and workspace setup flow: profile, role, discovery source, workspace, goals, invites, then a success state, with a synced product preview. ReUI Stepper plus shadcn Card, Combobox, RadioGroup, Select, Switch, Field.

Uses: `@reui/icon-stack`, `@reui/stepper`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`

### `onboarding-2`

Six-step workspace onboarding wizard with left sidebar vertical stepper and animated success state

Six-step setup wizard (profile, role, source, workspace, goals, invites) with a clickable sidebar stepper, animated transitions, and a success screen. ReUI Frame and Stepper plus shadcn Field, Combobox, RadioGroup, Switch. Onboarding, signup wizard.

Uses: `@reui/frame`, `@reui/icon-stack`, `@reui/stepper`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`

### `onboarding-3`

Split-screen workspace onboarding wizard with vertical stepper sidebar and animated dot-sphere panel

Six-step signup: profile, role, source, workspace, goals, invites, plus success screen. Dark sidebar pairs a vertical ReUI Stepper with animated dot-sphere canvas. Field, Combobox, RadioGroup, Checkbox, Switch, Select. Setup wizard, account creation.

Uses: `@reui/icon-stack`, `@reui/stepper`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`

### `onboarding-4`

Six-step workspace onboarding wizard with top progress bar and success screen

Multi-step flow to create a team workspace: profile with avatar upload, role and goal pickers, team size, teammate invites, animated top progress bar and ready screen. Uses ReUI Frame, Stepper, Combobox, Select, Field. Onboarding wizard, setup flow.

Uses: `@reui/frame`, `@reui/icon-stack`, `@reui/stepper`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`

### `onboarding-5`

Multi-step workspace onboarding dialog with dot stepper, animated steps, and success screen

Six-step modal wizard (profile, role, workspace, goals, teammate invites) with clickable dot stepper, animated steps, and a success screen. ReUI Dialog, Field, Combobox, Select, RadioGroup, Switch, Avatar upload, Button. For signup flow, get started.

Uses: `@reui/icon-stack`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`

### `onboarding-6`

Eight-step workspace onboarding wizard with progress stepper, AI agent picker, copyable API setup

Eight-step workspace onboarding wizard ending in AI agent selection and API key setup with copyable terminal commands. Profile, role, goals, and invite steps. ReUI Stepper, Frame plus shadcn Combobox, RadioGroup, Select. Account setup flow.

Uses: `@reui/frame`, `@reui/icon-stack`, `@reui/stepper`, `@reui/use-copy-to-clipboard`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`

### `onboarding-7`

Six-step workspace onboarding wizard with top progress bar and screenshot carousel rail

Multi-step signup flow: profile, role, source, workspace, goals, invites, with a top Stepper progress bar, animated stacked-screenshot rail, and a success state. ReUI Stepper, Badge; shadcn Field, Combobox, RadioGroup, Select, Switch.

Uses: `@reui/badge`, `@reui/icon-stack`, `@reui/stepper`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`

### `onboarding-8`

Dark 8-step workspace onboarding wizard with progress bar, agent picker, and CLI setup checklist

Full-page dark onboarding flow: profile, role, workspace, goals, teammate invites, AI agent pick, and Codex CLI setup with a success screen. Animated progress bar, copyable commands. ReUI Stepper, Frame, Badge plus Combobox, Select, RadioGroup.

Uses: `@reui/badge`, `@reui/frame`, `@reui/icon-stack`, `@reui/stepper`, `@reui/use-copy-to-clipboard`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `lucide-react`, `motion`

### `onboarding-9`

Six-step workspace onboarding wizard with marketing hero and animated progress bar

Profile, role, source, workspace, goals, and invite steps beside a marketing hero, with photo upload, goal pickers, timezone Combobox, success state. ReUI Stepper plus shadcn Card, Select, RadioGroup, Switch. First-run setup, getting-started flow.

Uses: `@reui/icon-stack`, `@reui/stepper`, `@reui/use-file-upload`

npm: `@hugeicons/core-free-icons`, `@hugeicons/react`, `motion`


## profile (9)

### `profile-1`

Account settings shell with vertical sidebar tabs for profile, workspace, team, and billing

SaaS account settings page: a vertical Tabs sidebar switching Profile, Workspace, Team, and Billing panels on ReUI Frame and Badge, plus a searchable, filterable, paginated ReUI DataGrid of team members and shadcn Field, Input, Switch, and Combobox.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/phone-input`, `@reui/use-copy-to-clipboard`, `@reui/use-file-upload`

npm: `@tanstack/react-table`, `sonner`

### `profile-2`

Admin settings page with line tabs spanning profile, members, permissions, and integrations

Tabbed workspace admin settings: profile form, member DataGrid with row actions, permission checkbox matrix, notification and integration toggles. Account settings, team admin, access control. ReUI Tabs, DataGrid, Badge, Alert, shadcn Switch, Card.

Uses: `@reui/alert`, `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/phone-input`, `@reui/use-file-upload`

npm: `@base-ui/react`, `@tanstack/react-table`, `sonner`

### `profile-3`

Profile settings form with avatar upload, verified email, and regional preferences in a single card

Account profile settings page: avatar upload, identity fields (name, verified email, username, role, phone), regional preferences (timezone, week start, language), dismissible sync alert. ReUI Alert, Badge, PhoneInput; shadcn Card, InputGroup.

Uses: `@reui/alert`, `@reui/badge`, `@reui/phone-input`, `@reui/use-file-upload`

### `profile-4`

Outreach inbox account settings page with connected mailboxes, reply routing, and signature toggles

Mailbox settings page: account cards with status badges, per-row dropdown actions, connect-provider buttons, and signature toggles. ReUI Badge, shadcn Card, Item, Avatar, DropdownMenu, Switch. For outreach, inbox, and email account settings.

Uses: `@reui/badge`

### `profile-5`

Notification settings with daily digest controls and a per-channel email and in-app alert matrix

Notification preferences page: a daily digest stat summary with Progress bars and tooltips, a Switch toggle, plus a per-alert email and in-app delivery matrix. ReUI Badge with Card, Table, Checkbox, Switch, Field, Progress.

Uses: `@reui/badge`

### `profile-6`

Partner referral rewards profile with copy-link share card, reward tier ladder, referral activity

Referral and partner rewards page: metric cards with progress, a copy-link InputGroup share card, an unlocked/next/locked reward ladder, next-unlock progress, and a referrals activity list. ReUI Badge, shadcn Card, Progress, Avatar, Tooltip.

Uses: `@reui/badge`, `@reui/use-copy-to-clipboard`

npm: `sonner`

### `profile-7`

Meeting Capture Settings Card with Recording Mode, Consent, Notes Template, and Output Toggles

Single-card meeting recording settings: capture mode, consent, and notes template selects, output checkbox group, prompt textarea, auto-share and transcript switches, Reset and Save with toast. ReUI Badge, shadcn Card, Select, Checkbox, Switch.

Uses: `@reui/badge`

npm: `sonner`

### `profile-8`

Billing settings page with plan summary, 3-column usage metrics, and invoice history table

Subscription billing settings page: trial alert, plan summary with renewal facts, 3-column usage metrics, billing detail rows with tooltip hints, and an invoice history table. Built with ReUI Alert, Badge, shadcn Card, Table, Field, Tooltip, Button.

Uses: `@reui/alert`, `@reui/badge`

### `profile-9`

Account settings hub with grouped collapsible sidebar navigation and 11 swappable form panels

Workspace settings page where a collapsible grouped sidebar switches 11 card-based form panels: authentication, profile, billing, API keys, webhooks, audit. ReUI Badge with shadcn Sidebar, Card, Field, Input, Select, Switch, Checkbox, RadioGroup.

Uses: `@reui/badge`

npm: `sonner`


## schedule (10)

### `schedule-1`

Schedule with date-picker calendar and filterable day agenda of status events

Two-pane schedule: a month Calendar with event dots beside a status-filterable day agenda of event cards with status Badge, attendee AvatarGroup, time and location. ReUI Frame, Badge plus shadcn Calendar, Select, Avatar. Planner, appointments.

Uses: `@reui/badge`, `@reui/frame`

npm: `react-day-picker`

### `schedule-2`

Session time picker card with start and end Selects, quick-duration presets and live duration

Booking card to pick a meeting or work-session time: ReUI Frame with Avatar header, Select start and end menus, quick-duration preset Buttons, Tooltip and live duration, Cancel and Apply. Schedule, time-slot, duration picker.

Uses: `@reui/frame`

### `schedule-3`

Meeting scheduler card with calendar, time-slot list, duration and recurrence selects, and switches

Schedule a meeting: pick a date, choose an available time slot, set duration and recurrence, add title and notes, toggle waiting room and auto-record. Booking form using ReUI Frame, shadcn Calendar, Select, Switch, Input, Textarea, Button.

Uses: `@reui/frame`

npm: `date-fns`

### `schedule-4`

Calendly-style meeting booking widget with month calendar, availability dots, and time-slot picker

Pick a date on the month calendar (available days dotted), choose a time slot, confirm. Side panel shows host, session type, platform, duration. ReUI Frame with shadcn Calendar, Select, Avatar, ScrollArea. Appointment scheduling, booking pages.

Uses: `@reui/frame`

npm: `date-fns`, `react-day-picker`

### `schedule-5`

Compact team attendance calendar card with status filter and bar-chart stat rows

Team attendance widget: month Select, status filter DropdownMenu, single-date Calendar with today highlight, AvatarGroup, and Attendance/Absences/Delayed rows with bar sparklines. ReUI Frame, Badge; shadcn Calendar, Avatar, Chart. Presence tracker.

Uses: `@reui/badge`, `@reui/frame`

npm: `recharts`

### `schedule-6`

Schedule creation form with member multi-select, date picker, and file upload

Schedule creation form: name input, member multi-select with avatars, date picker, start and end time selects, drag-drop image upload, link and description. ReUI Frame, Combobox, Avatar, Field, Calendar, Select. For meeting and booking forms.

Uses: `@reui/alert`, `@reui/frame`, `@reui/use-file-upload`

npm: `date-fns`

### `schedule-7`

Webinar event detail card with collapsible overview, presenters, and Yes/Skip/Maybe RSVP sections

Event card with three collapsible sections: overview rows with live stream and recording switches, presenters, and agenda with Yes/Skip/Maybe RSVP. ReUI Frame and Badge, shadcn Collapsible, Avatar, Switch, Button. For meeting invites and webinars.

Uses: `@reui/badge`, `@reui/frame`

### `schedule-8`

Compact month calendar card with per-day category dots, filter chips, and attendee-avatar agenda

Month calendar card with colored category dots per day, category filter chips, and a scrollable day agenda of events with attendee avatar groups. ReUI Frame, shadcn Calendar, Select, Avatar, ScrollArea. Mini schedule, team agenda widget.

Uses: `@reui/frame`

npm: `little-date`, `react-day-picker`

### `schedule-9`

Session booking scheduler with single-date calendar, duration toggle, and scrollable time slots

Appointment booking widget for meetings and consultations. Single-date Calendar with month and year dropdowns, 15m to 90m duration toggle, scrollable time-slot picker, confirm footer. ReUI Frame, shadcn Calendar, Select, ScrollArea, Button.

Uses: `@reui/frame`

### `schedule-10`

Date and Time Scheduling Popover with Quick Shortcut Rows, Calendar, and Time Slots

Schedule a date and time: quick shortcut rows (Today, Tomorrow, Next week), month and year calendar, and scrollable time-slot column with disabled slots. Uses ReUI Frame, shadcn Calendar, Item, Select, ScrollArea, Button. Due-date / deadline picker.

Uses: `@reui/frame`

npm: `date-fns`


## settings (16)

### `settings-1`

Import services settings step with selectable integration cards and a 2-pick limit

Wizard step to import data from third-party services. Selectable integration cards with logo, status badge, and checkbox, capped at 2 picks via a toast, with back and next. ReUI Badge, Frame; shadcn Card, Checkbox, Button. Connect integrations.

Uses: `@reui/badge`, `@reui/frame`

npm: `sonner`

### `settings-2`

Privacy and preferences settings card with mixed-control rows, switches, buttons and Pro/Beta badges

Privacy settings panel of icon rows whose action varies per setting: toggle switch, single button, or a paired Enable all / Disable all control, plus Pro and Beta tags. ReUI Frame, Badge; shadcn Switch, Button, Item. Account privacy, preferences.

Uses: `@reui/badge`, `@reui/frame`

### `settings-3`

General Settings Form with Per-Row Controls, Required and Pro Badges

Stacked settings rows in a ReUI Frame, each pairing a labeled description with its own control: Input, prefixed URL InputGroup, Select, ToggleGroup, color swatches, Switch list, plus Required and Pro badges. Preferences, app config, account settings.

Uses: `@reui/badge`, `@reui/frame`

### `settings-4`

App connections settings page with integrations grouped into labeled sections and per-row status

Connected apps settings: integration rows grouped into labeled sections, each with brand logo, Connected or Needs review status, and a per-row menu to sync, manage, or disconnect. ReUI Frame, Badge; shadcn Item, DropdownMenu, Button.

Uses: `@reui/badge`, `@reui/frame`

### `settings-5`

Role Permissions Settings Panel with Two-Column Switch Toggle Grid

Role-based access settings: a two-column grid of outlined permission cards, each with title, description, and on/off Switch, under a header with a New Permission button. ReUI Frame, Badge; shadcn Item, Switch, Button. For roles, access control, RBAC.

Uses: `@reui/badge`, `@reui/frame`

### `settings-6`

Integrations settings list with brand-logo cards and connect or disconnect toggle buttons

Connected apps settings page: per-integration cards with brand logo, name, and Connect/Disconnect button that reveals per-channel notification toggles. ReUI Frame plus shadcn Item, Button, Switch. App connections, integrations, webhooks.

Uses: `@reui/frame`

### `settings-7`

Account settings page with side-tab navigation for profile, security, notifications, and billing

Tabbed account settings shell with a side tab rail. Profile with avatar upload, two-step verification, active sessions, delete account, and billing plans. ReUI Alert and Badge with shadcn Tabs, Card, Field, Input, Select, Switch, Item, Avatar.

Uses: `@reui/alert`, `@reui/badge`, `@reui/use-file-upload`

### `settings-8`

Webhook endpoints settings list with per-endpoint delivery-health alerts and enable toggle

Webhook developer settings managing endpoint routes with delivery-health tooltip alerts, status badges (Delivering, Retrying, Paused), enable Switch, copy URL, rotate-secret and remove actions. ReUI Frame, Badge; shadcn Item, Switch, DropdownMenu.

Uses: `@reui/badge`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `sonner`

### `settings-9`

Workspace Preferences Settings With Collapsible Sections of Select and Switch Rows

Workspace settings page grouping preference rows into collapsible General and Display sections, each row mixing select dropdowns and switch toggles with status badges. ReUI Frame, Badge; shadcn Collapsible, Item, Select, Switch, Separator.

Uses: `@reui/badge`, `@reui/frame`

### `settings-10`

Workspace security settings in Frame cards mixing toggles, a timeout select, and plan-tier badges

Security settings page grouping session policy, login methods, and access restrictions into ReUI Frame cards. Rows mix Switch toggles, a timeout Select, and plan-tier Badges (Basic, Business, Enterprise) on shadcn Item. For 2FA, SSO, access controls.

Uses: `@reui/badge`, `@reui/frame`

### `settings-11`

Notification preferences settings with tabbed channel matrix table for Email, Slack, and In-app

Notification settings grouping events under Projects, Messages, Reports, and System tabs, each a table with per-row Email/Slack/In-app checkboxes. Uses ReUI Tabs (line), Table, Checkbox. For alert preferences and channel opt-in.

### `settings-12`

Notification settings page with per-channel delivery modes and collapsible auto-follow toggles

Notification preferences page: per-channel delivery-mode Selects for inbox, email, browser, and mobile, Slack, Zoom, and Google Meet connect rows, plus a collapsible auto-follow section. Uses ReUI Badge with shadcn Card, Select, Switch, Collapsible.

Uses: `@reui/badge`

npm: `sonner`

### `settings-13`

Integrations settings gallery, app cards in a grid with connect button and toggle switch

Integrations settings page: responsive grid of app cards with brand logo, description, connect/disconnect button and a toggle switch. Connected apps marketplace, integration directory. ReUI Frame with shadcn Item, Button, Switch.

Uses: `@reui/frame`

### `settings-14`

API integrations settings data grid with copyable keys, status switches, and pause-all toggle

Sortable, paginated table of connected API integrations: brand logos, copy-to-clipboard API key badges, daily call counts, per-row enable switches, and a pause-all toggle. ReUI DataGrid, Frame, Badge; shadcn Switch. Connected apps, API keys settings.

Uses: `@reui/badge`, `@reui/data-grid`, `@reui/data-grid-column-header`, `@reui/data-grid-pagination`, `@reui/data-grid-scroll-area`, `@reui/data-grid-table`, `@reui/frame`, `@reui/use-copy-to-clipboard`

npm: `@tanstack/react-table`, `sonner`

### `settings-15`

Workspace settings with grouped preference cards, toggles, badges, and a team avatar row

Workspace preferences page grouping AI, publishing, collaboration, and notification settings into Frame cards with Switch toggles, status Badges, action Buttons, and an AvatarGroup team row.

Uses: `@reui/badge`, `@reui/frame`

### `settings-16`

Connected apps integration settings with per-row status badges and connect actions

Connected apps panel listing integrations as rows with logo, name, status badge (Connected, Available, Preview), and Configure or Install action. Uses ReUI Frame, Badge, shadcn Item, Button. For integrations, connectors, app directory.

Uses: `@reui/badge`, `@reui/frame`


## sheet (11)

### `sheet-1`

Inset right project create Sheet with inline metadata comboboxes and target date picker

Create-project side drawer: name Input and description Textarea over inline Combobox pickers for status, priority, lead, members, milestone, target date, and labels. Uses ReUI Sheet, Combobox, Calendar, Dialog, AvatarGroup. New project or issue form.

npm: `date-fns`

### `sheet-2`

Right-side help and support Sheet with search field and grouped guide links

Help center side panel: searchable InputGroup, grouped guide Items with status Badges and Tooltips, scrollable body, footer support links. For in-app help, docs drawers, support menus. Uses ReUI Badge, Sheet, InputGroup, Item, ScrollArea, Tooltip.

Uses: `@reui/badge`

### `sheet-3`

Searchable keyboard shortcuts reference in a right inset sheet, grouped by section

Right-side inset Sheet listing app keyboard shortcuts grouped into sections with Kbd key chords, a live search InputGroup, ScrollArea, and empty state. For a shortcuts panel, cheat sheet, or hotkeys help. Sheet, Kbd, InputGroup, ScrollArea, Empty.

### `sheet-4`

Inset right AI assistant sheet with model selector, suggestion chips, and composer toolbar

Floating right-side AI chat panel with a header model-switch Select, user and assistant message bubbles, suggestion chips, and an InputGroup composer toolbar. Uses ReUI Sheet, InputGroup, ScrollArea, Tooltip. AI copilot drawer, chatbot panel.

### `sheet-5`

Inset right comment thread Sheet with reply, react, resolve and open-only filter

Client discussion sheet for collaboration and review apps. Comments with reply, emoji react, resolve and reopen, open-versus-all filter and a composer. ReUI Badge, shadcn Sheet, Item, Avatar, InputGroup, DropdownMenu, ScrollArea, Tooltip.

Uses: `@reui/badge`

### `sheet-6`

Inset right view customizer sheet with quick toggles and layout mode picker

Floating right sheet to customize a workspace view: Switch toggles plus a RadioGroup of layout cards with SVG skeleton previews and a hint Tooltip. ReUI Sheet, Field, Switch, RadioGroup, ScrollArea. Settings panel, preferences drawer.

### `sheet-7`

Inset right notifications sheet with unread badge, mark-all-read, and rich activity feed

Floating right-anchored notification panel for in-app activity. Scrollable feed with unread count, mark-all-as-read, approvals, attachments, avatar groups, ratings, and progress. ReUI Badge, Rating; Sheet, Avatar, Button, ScrollArea.

Uses: `@reui/badge`, `@reui/rating`

### `sheet-8`

Inset right settings sheet with scrollable two-section form, header and sticky footer

Floating inset right Sheet for relay settings, with scrollable Delivery and Routing sections, Input, Select, and Switch fields, tooltip hints, and a sticky Reset / Save footer. ReUI Sheet, Field, Select, Switch. Settings panel, preferences drawer.

### `sheet-9`

Inset right ticket details Sheet with inline per-row editing and save actions

Right-side ticket panel where each field edits in place via Select, Combobox, Calendar, Switch, or InputGroup, with Badge status, avatar chips, and async save toast. ReUI Badge, shadcn Sheet, Combobox. Ticket detail, issue properties, record drawer.

Uses: `@reui/badge`

npm: `sonner`

### `sheet-10`

Inset right AI assistant chat sheet with prompt suggestions and pinned composer toolbar

Floating right-side AI chat panel with scrollable history, prompt suggestion chips, and a pinned InputGroup composer (attach, voice, send) plus header new-chat and refresh actions. Uses Sheet, ScrollArea, DropdownMenu. Copilot, assistant drawer.

### `sheet-11`

Right-Side Metric Detail Sheet with Target Progress, Owners, Alert Rule, and Changes Timeline

Right drawer for one KPI: current value with delta badge, target progress bar, definition facts, owner avatars, alert rule, and a recent-changes timeline. ReUI Badge, Timeline; shadcn Sheet, Progress, AvatarGroup. Metric detail, analytics drilldown.

Uses: `@reui/badge`, `@reui/timeline`


## stats (15)

### `stats-1`

KPI stat card grid with up or down trend badges and a per-card overflow action menu

Responsive four-column KPI cards: large formatted metric, colored up or down delta badge, vs-last-month line, plus a per-card overflow menu. Uses ReUI Frame and Badge with shadcn DropdownMenu, Button, Separator. Stats overview, metrics, analytics.

Uses: `@reui/badge`, `@reui/frame`

### `stats-2`

Color-block KPI stat cards with delta badge, vs-last-month row, and overflow menu

Four KPI metric cards on solid color backgrounds with delta arrow badge, vs-last-month comparison, and per-card overflow menu. Built with ReUI Badge, shadcn Card, Button, DropdownMenu. Dashboard stats, KPI tiles, scorecard.

Uses: `@reui/badge`

### `stats-3`

Subscription stats card with plan-tier segmented bar and expiring-soon renewal list

Subscription metrics card: revenue and subscriber counts, a stacked Free/Pro/Enterprise tier bar with legend, and an Expiring Soon list with plan badges, days left, and renew links. ReUI Badge, shadcn Card, Select, Tooltip. For SaaS billing.

Uses: `@reui/badge`

### `stats-4`

Leads overview stats card with range filter, progress bar and segmented returning-leads meter

Lead summary card with a time-range Select, new vs returning counts, percent Badge, Progress bar and a 30-segment meter, plus top source and conversion rate Tooltip. ReUI Frame, Badge; shadcn Progress, Select, Tooltip. For CRM, marketing dashboards.

Uses: `@reui/badge`, `@reui/frame`

### `stats-5`

Dark balance stat card with segmented multi-currency allocation bar and topup action

Wallet balance card with total amount, positive percent change, and a color-coded segmented bar splitting holdings by currency (USD, GBP, EUR) plus a Topup button. Uses shadcn Card and Button. For finance dashboards, crypto and banking apps.

### `stats-6`

Staff performance card with KPI trend grid, pipeline progress bar, and activity feed

Sales rep performance summary: a 3-up KPI grid with up/down trend deltas, a pipeline progress bar, a recent activity list, and a quarter filter. ReUI Frame, Badge with shadcn Progress, Select, DropdownMenu, Button. For dashboards and scorecards.

Uses: `@reui/badge`, `@reui/frame`

### `stats-7`

Three-column stats panel with divided cells, large metric values and trend badges

Bordered ReUI Frame panel split into three divided cells, each with a title, large metric value, colored trend Badge and period comparison subtext. KPI overview, dashboard stats, sales and churn metrics row.

Uses: `@reui/badge`, `@reui/frame`

### `stats-8`

Three-column KPI stat cards with icon tiles, trend badges, and date range footer

Responsive 1 to 3 column metric grid; each card pairs a colored icon tile with a value, label, up/down trend Badge, and reporting date range. ReUI Frame, Badge, shadcn Item. For dashboards, analytics overview, KPI summary.

Uses: `@reui/badge`, `@reui/frame`

### `stats-9`

Tasks overview stat card with animated completion progress bar and AI finish-time prediction

Task summary card: animated Tasks Done Progress bar, range Select filter, 3-column Backlog/In Progress/In Review buckets with colored counts, and AI prediction footer. ReUI Frame, shadcn Progress, Select. Project dashboard, productivity stats widget.

Uses: `@reui/frame`

### `stats-10`

Total Revenue stat card with trend badge, dropdown actions menu, and supporting metric rows

Single KPI revenue card: large currency figure, USD label, red trend Badge for quarter-over-quarter change, and stacked metric rows. Built on ReUI Frame and Badge with shadcn Button and DropdownMenu actions. For dashboards, analytics, finance.

Uses: `@reui/badge`, `@reui/frame`

### `stats-11`

API call quota usage card with progress bar, billed cost, and renewal date

Single-stat usage card tracking API calls against a monthly quota: Progress bar for used vs total, dollar cost, remaining free calls, and a renewal-date footer. ReUI Frame, shadcn Progress and Button. Usage meter, billing, plan limit.

Uses: `@reui/frame`

### `stats-12`

Support metrics stat card grid with colored icon tiles and status badges

Three-column support KPI grid: each Frame card pairs a colored bordered icon tile with a bold value, label, and status Badge (tickets, resolved rate, satisfaction). Uses ReUI Frame, Badge, Item. For support dashboards and service overview stats.

Uses: `@reui/badge`, `@reui/frame`

### `stats-13`

Compliance checks stat card with segmented bar gauge and overflow actions menu

Single-metric card tracking compliance checks passing with a segmented filled-block gauge, percentage readout, and actions dropdown. Built on ReUI Frame plus shadcn Button and DropdownMenu. For security, audit, and status dashboard widgets.

Uses: `@reui/frame`

### `stats-14`

Feature adoption stat card with segmented stacked indigo bar chart and actions dropdown

Single metric card showing a large 84% adoption rate over a segmented bar chart of graduated indigo blocks, plus a header actions menu. ReUI Frame with shadcn Button and DropdownMenu. For KPI, analytics, and feature usage dashboards.

Uses: `@reui/frame`

### `stats-15`

Three color-filled hero stat cards with metric, summary, and dark CTA action bar

Three full-bleed colored metric cards, each with an icon, large KPI value, title, summary line, and a dark bottom CTA bar with a sliding arrow. Built on ReUI Card. For dashboards, KPI highlights, and stats callouts.


## timeline (9)

### `timeline-1`

Vertical customer activation timeline with collapsible milestone cards and status indicators

Customer onboarding timeline where each activation milestone is a collapsible card with owner, priority and status badges, assignee avatars and due date. ReUI Timeline, Frame, Badge plus shadcn Avatar, Collapsible, Spinner. Onboarding tracker.

Uses: `@reui/badge`, `@reui/frame`, `@reui/timeline`

npm: `lucide-react`

### `timeline-2`

Vertical Account Rollout Timeline with Owner, Status Badges, Star Rating and File Attachments

Vertical activity timeline of onboarding milestones, each with date, action title, owner, colored status and risk badges, optional star rating and downloadable attachment. ReUI Timeline, Badge, Rating. Customer success, audit log, milestone feed.

Uses: `@reui/badge`, `@reui/rating`, `@reui/timeline`

### `timeline-3`

Finance activity timeline with avatar nodes, status badges, attachments, and inline actions

Vertical finance feed of payouts, risk flags, invoices, and ledger updates. Avatar nodes, dot plus colored status Badges, attachments, participant AvatarGroup, inline action Buttons. ReUI Timeline, Badge, Avatar, Button. Audit log, activity feed.

Uses: `@reui/badge`, `@reui/timeline`

### `timeline-4`

Team activity feed timeline with avatars, attachments, progress, ratings, and per-event action menu

Vertical activity stream mixing actor avatars, attachment downloads, participant avatar groups, status badges, progress bars, star ratings, and a per-event action menu. Uses ReUI Timeline, Badge, Rating, Avatar, Progress, DropdownMenu.

Uses: `@reui/badge`, `@reui/rating`, `@reui/timeline`

### `timeline-5`

Release changelog timeline with side date rail and color-coded type, impact, and change badges

Vertical changelog feed: each release shows a version title, summary, and tagged badges for type (New, Fixed), impact, and changes, with a left date rail. ReUI Timeline, Badge. Release notes, product updates, version history.

Uses: `@reui/badge`, `@reui/timeline`

### `timeline-6`

Horizontal scrolling approval workflow timeline with file attachments, ratings, and owner avatars

Horizontal scrollable timeline tracking approval steps, each with a phase status badge, attachment download, star rating, action button, and owner avatar. ReUI Timeline, Badge, Rating with shadcn Avatar, Button, ButtonGroup. For approval flows.

Uses: `@reui/badge`, `@reui/rating`, `@reui/timeline`

npm: `@base-ui/react`

### `timeline-7`

Account rollout activity dropdown with scrollable vertical timeline and per-step badges

Dropdown holding a scrollable vertical timeline of rollout steps, each with date, owner, status badge, dot-meta badge, attachment and star rating. ReUI Timeline, Badge, Rating with shadcn DropdownMenu, ScrollArea. Activity feed, audit log.

Uses: `@reui/badge`, `@reui/rating`, `@reui/timeline`

npm: `@base-ui/react`

### `timeline-8`

Slide-out team activity timeline panel in a right sheet with avatars, badges, and progress

Right-side activity feed panel listing team events as timeline entries with avatars, status badges, progress bars, attachments, ratings, and a per-item action menu. ReUI Timeline, Badge, Rating with shadcn Sheet, Avatar, DropdownMenu, ScrollArea.

Uses: `@reui/badge`, `@reui/rating`, `@reui/timeline`

npm: `@base-ui/react`

### `timeline-9`

Inset right sheet with a scrollable finance activity feed timeline and avatar indicators

Floating right sheet with a scrollable activity feed of payouts, risk reviews, and ledger entries with avatar indicators, status badges, attachment downloads, and inline actions. ReUI Timeline, Badge; shadcn Sheet, Avatar. Audit log, notifications.

Uses: `@reui/badge`, `@reui/timeline`

npm: `@base-ui/react`


## wizard (7)

### `wizard-1`

Three-step billing setup wizard card with horizontal stepper, per-step validation, review summary

Multi-step account and payment onboarding wizard in a Card: ReUI Stepper nav gates locked steps, validates each step, then shows a review summary with Badge. Uses Field, Input, InputGroup, Select, Switch, Button. For billing, checkout, onboarding.

Uses: `@reui/badge`, `@reui/stepper`

npm: `lucide-react`, `sonner`

### `wizard-2`

Three-step procurement vendor onboarding wizard with per-step validation and review summary

Multi-step vendor KYC intake: company details, compliance with repeatable beneficial owners and tax ID, then a document checklist and review summary. Per-step validation. ReUI Stepper, Frame, Badge plus shadcn Field, Input, Select, Checkbox, Tooltip.

Uses: `@reui/badge`, `@reui/frame`, `@reui/stepper`

npm: `sonner`

### `wizard-3`

Invoice send wizard with step progress bar, line-item table, and live tax and discount totals

Four-step invoice send flow with progress Stepper, editable line-item Table, and live subtotal, tax, discount, and total. ReUI Stepper, Badge, Combobox; shadcn Card, Select, Calendar, Table, Tooltip. For billing, checkout, invoicing wizards.

Uses: `@reui/badge`, `@reui/stepper`

npm: `motion`, `sonner`

### `wizard-4`

Four-step billing upgrade wizard with live invoice preview sidebar and due-today total

Plan, seats, payment, and review flow that recalculates seat subtotal, annual discount, and support fee into a draft invoice. Uses ReUI Stepper, Badge, Alert plus Card, RadioGroup, Slider, Select, and Calendar. For checkout and seat upgrade screens.

Uses: `@reui/alert`, `@reui/badge`, `@reui/stepper`

npm: `date-fns`

### `wizard-5`

Three step team invitation wizard with per-row role assignment and pre-send review

Add member emails with inline validation and per-row roles, set sender and expiry, then review a recipients table and send-readiness checks before queuing. ReUI Stepper, Frame, Badge plus shadcn Table, Select, Avatar. For onboarding and seat invites.

Uses: `@reui/alert`, `@reui/badge`, `@reui/frame`, `@reui/stepper`

npm: `sonner`

### `wizard-6`

Five-step ecommerce product creation wizard with variant options and SKU matrix

Add-product flow across details, image gallery, variant option groups, pricing, and a per-variant SKU matrix table. ReUI Stepper, Badge, Alert with shadcn Card, Select, Switch, Table, Dialog. Product setup wizard, multi-step form.

Uses: `@reui/alert`, `@reui/badge`, `@reui/stepper`, `@reui/use-file-upload`

npm: `@base-ui/react`, `sonner`

### `wizard-7`

Four-step fund transfer wizard with payee search, currency combobox, and balance checks

Money transfer flow over a 4-step Stepper: pick payee, set amount and funding source, review, authorize with a 6-digit code. Recent-payee grid, searchable saved accounts, multi-currency Combobox, low-balance Alert. ReUI Stepper plus shadcn Combobox.

Uses: `@reui/alert`, `@reui/icon-stack`, `@reui/stepper`

npm: `motion`, `sonner`

