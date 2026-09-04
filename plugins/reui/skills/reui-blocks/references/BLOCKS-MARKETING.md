# Premium blocks — Marketing

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 40 entries. Do not edit by hand.

**Licence: Pro or Ultimate.** Install with `shadcn add @reui/<name>` once `REUI_LICENSE_KEY` is set.

## Contents

- [blog (6)](#blog-6)
- [contact (6)](#contact-6)
- [cta (6)](#cta-6)
- [faq (6)](#faq-6)
- [hero (16)](#hero-16)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Purpose](#purpose)
- [Best Fit](#best-fit)
- [Main Pieces](#main-pieces)
- [LLM Guidance](#llm-guidance)
- [Source](#source)

## blog (6)

### `blog-1`

Blog index with cover-image post cards in a responsive three-column grid and author footers

Blog listing on a responsive 1/2/3-column grid of Cards: 16:10 cover, date and read-time, clamped title and excerpt, author footer with Avatar and Read link. Built on Card, CardContent, Avatar. For blog index, article archive, news, or changelog.

### `blog-2`

Full-image blog post cards with titles overlaid on covers, hover zoom, and pill category badges

Blog index of three full-bleed cover-image cards with a gradient scrim, title and tone label overlaid on the photo, a white pill category Badge, and hover zoom. ReUI Badge, shadcn Card. For articles index, news grid, insights, or journal pages.

Uses: `@reui/badge`

### `blog-3`

Blog article carousel with cover cards, circular prev/next controls and a progress-line indicator

Featured-article blog carousel with circular prev/next buttons and a 1px progress line as position indicator. Cover scales on hover; category badge and read time. ReUI Carousel, Progress, AspectRatio, Badge, Card. Article slider, featured posts.

Uses: `@reui/badge`

### `blog-4`

Three-column blog index with stacked Frame cards, grayscale hover-zoom covers, and author footers

Blog index listing posts as stacked ReUI Frame cards in a three-column row: grayscale cover that zooms on hover, category, date, title, excerpt, and an author footer with shadcn Avatar and Read link. For news, insights, and article listings.

Uses: `@reui/frame`

### `blog-5`

Blog post detail page with gradient overlay image hero, byline, pull quote, and related posts list

Reading page for one blog post, news, changelog, or case study. Cover with gradient scrim, overlaid title and category badge, byline, sections, pull quote, author bio, and text-only related posts. Uses ReUI Card, AspectRatio, Avatar, Badge, Item.

Uses: `@reui/badge`

### `blog-6`

Single-column blog post detail page with breadcrumb, author byline, topic badges, Read Next grid

Centered max-w-3xl blog post detail page: breadcrumb, headline, author byline, cover image, body sections, topic badges, and a two-up Read Next grid of related posts. Built on ReUI Breadcrumb, Card, Item, Avatar, Badge, Separator. For release notes.

Uses: `@reui/badge`


## contact (6)

### `contact-1`

Centered single-email contact card with framed mail row and full-width email action button

Centered contact section with one direct-email path instead of a form: eyebrow, heading, a framed mail-icon row, and a full-width outline button showing the support email. Uses ReUI Frame, shadcn Item and Button. For contact us and support pages.

Uses: `@reui/frame`

### `contact-2`

Split contact card with project intake form and abstract SVG scope panel

Two-column Card pairing a project intake form (Project Type and Timeline Selects, budget InputGroup with $ addon, Textarea, Button) with a gradient SVG panel of mailto and tel Item links. For agency, studio, or SaaS quote and project-brief pages.

Uses: `@reui/badge`

### `contact-3`

Frameless split contact form with topic Select and image-backed Card panel of email and phone links

Split contact-us section: frameless form (Name, Email, topic Select, Subject, Textarea) beside an image-backed Card of email and phone links. Field, Input, Select, Textarea, Button, Card, Item. Contact page, support form, sales inquiry, lead capture.

Uses: `@reui/badge`

### `contact-4`

Contact section with global office columns ordered west to east as a follow-the-sun timezone band

Form-free contact band: three office columns split by dividers, each with city, postal address, UTC offset, business hours, and a directions link, plus an email and CTA button. Uses shadcn Button and Separator. For contact us, our offices, find us.

### `contact-5`

Two-column contact Card pairing a tinted contact-details panel with a short project inquiry form

Framed Card with a tinted left details panel (email, response time, studio location) beside a right project form. ReUI Card, Field, Input, Textarea, Button. For contact us, get in touch, start a project, sales inquiry, lead capture.

### `contact-6`

Channel-first contact section with clickable Frame panels for chat, email, and GitHub community

Channel-first contact section: three clickable Frame panels (Live Chat, Email Us, GitHub Community) over a muted docs and FAQ card. ReUI Frame, FramePanel; shadcn Card, Item, Button. Contact us, get in touch, support channels page.

Uses: `@reui/frame`


## cta (6)

### `cta-1`

Centered newsletter signup CTA with mail-prefixed email input and avatar-stack subscriber proof

Centered newsletter CTA: badge eyebrow, headline, lede, a mail-prefixed email field with Subscribe button, and an overlapping avatar stack with subscriber count. ReUI Badge, shadcn InputGroup, Avatar, Button. Email capture, mailing-list opt-in.

Uses: `@reui/badge`

### `cta-2`

Split CTA card with image media panel, badge eyebrow, dual link buttons, and feature trust strip

Two-column marketing CTA pairing copy with an image media panel on a radial dot-grid backdrop. Badge eyebrow, headline, two icon link Buttons, and a feature strip. ReUI Badge, shadcn Card, Button, Item. Landing CTA, get-started banner, product promo.

Uses: `@reui/badge`

### `cta-3`

Centered Frame CTA with animated grid background, badge eyebrow, and single email capture form

Compact centered email-capture CTA: a ReUI Frame and FramePanel surface over an animated motion/react SVG grid, with a Badge eyebrow, h2 heading, lede, and an inline shadcn Input plus Button. For waitlist, signup, lead-capture, and launch sections.

Uses: `@reui/badge`, `@reui/frame`

npm: `motion`

### `cta-4`

Centered marketing CTA with badge eyebrow, framed three-column proof grid, and dual link buttons

Centered conversion CTA: Badge eyebrow, heading, lede above a ReUI Frame three-column FramePanel proof grid of bordered Item icon tiles, then primary and outline link Buttons. Landing, pricing, product closer; feature grid, dual button CTA.

Uses: `@reui/badge`, `@reui/frame`

### `cta-5`

Full-width aurora-gradient CTA banner with a two-line headline and one rounded-full pill button

Full-bleed single-message conversion band: one bold two-line headline and a single rounded-full action over a static OKLCH aurora gradient. Built on shadcn Card and Button. For closing CTA sections, hero banners, sign up and get-started callouts.

### `cta-6`

Dark violet CTA banner with animated neon sine-wave line-stream backdrop and one rounded-full button

Closing CTA banner: two-line heading, supporting line, and one rounded-full anchor button on a deep violet surface lit by an animated, looping neon line-stream. Built on shadcn Card and Button. For a final conversion band or dark hero section.


## faq (6)

### `faq-1`

Two-column FAQ with sticky intro, line-tab category filter, and multi-open accordion cards

Two-column FAQ: sticky intro plus a line-variant Tabs row that filters questions by category and re-mounts a multiple-mode Accordion of bordered Cards, first answer open. ReUI Badge, shadcn Tabs, Accordion, Card, Button. For help and FAQ pages.

Uses: `@reui/badge`

### `faq-2`

Centered two-column FAQ with multi-open divider accordion and a dot-grid framed support panel

Centered two-column marketing FAQ that keeps one answer open per column. Divider-row Accordion over a dot-grid Frame support panel and outline link CTA. ReUI Badge, Frame, FramePanel, shadcn Accordion, Button. For help, support, pricing FAQ, docs.

Uses: `@reui/badge`, `@reui/frame`

### `faq-3`

Open no-accordion FAQ with always-visible two-column answer grid and two-CTA support row

Open FAQ section showing every answer at once, no accordion: a hairline-divided two-column question and answer grid that stacks on mobile, plus a support row with two CTAs. Uses shadcn Button, Item, ItemMedia. For help, support, pricing FAQ, docs.

### `faq-4`

Centered single-column FAQ with help eyebrow and borderless single-open accordion

Centered single-column FAQ: help-icon eyebrow over a shadcn Accordion of seven Q&A rows split by thin border dividers (no cards, single-open, first open), with a "Talk to the team" arrow link. For FAQ, help, support, pricing FAQ, onboarding pages.

### `faq-5`

Two-column FAQ pairing a single-open accordion card with a sticky support-CTA sidecard

Two-column marketing FAQ: a single-open Accordion in a Card (hairline rows, first open) beside a sticky dashed support CTA card with a contact link Button and email fallback. ReUI Badge, shadcn Accordion, Card, Button. For help, support, FAQ pages.

Uses: `@reui/badge`

### `faq-6`

Single-column FAQ accordion with built-in contact-support footer inside one stacked ReUI Frame tray

One-column Q and A: a single-open Accordion above a muted footer with Read The Docs and Contact Support buttons, boxed in stacked ReUI Frame. Built on shadcn Accordion, Item, Button. For FAQ, help, support, and pricing-questions pages.

Uses: `@reui/frame`


## hero (16)

### `hero-1`

Dark MCP usage hero with an animated isometric bar chart and a flagged usage spike

Dark split marketing hero for an MCP usage product: status badge, highlighted headline, capability chips, dual call to action, brand row, and an animated isometric bar chart charting agent usage velocity with a flagged spike.

Uses: `@reui/badge`, `@reui/icon-tile`

## Purpose
A conversion hero for developer tooling that has a usage or telemetry story to tell. The left column carries the pitch and the calls to action; the right column renders an isometric MCP usage chart that gives the surface its point of view.

## Best Fit
Top of a marketing page for an API, agent platform, or usage-metered product. The chart reads as product evidence rather than decoration, so it suits pricing-adjacent and developer-audience pages.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the dark surface, the conversion column, and the chart.
- `components/usage-velocity-chart.tsx` draws the isometric scene as one inline SVG on a fixed 624 by 600 canvas and animates it with CSS keyframes.
- `components/data.tsx` holds the bar geometry, capability chips, and brand marks.

## LLM Guidance
The surface is intentionally dark in both themes, so neutrals are literal while accents use the teal scale. The conversion column is a `@container`, so the headline scales with the column rather than the viewport. Bar `extrusion` is stored per bar because the source design sized the bars by eye; it is not derived from `value`. Swap `USAGE_BARS` for real readings and keep one bar flagged with `accent` so the callout still has a subject.

### `hero-2`

Aurora Console Hero

Split marketing hero for a component registry: Next.js badge, lime-highlighted headline, call to action with an inline star rating, brand row, and a rebuilt analytics console floating on a drifting gradient backdrop, with full dark mode.

Uses: `@reui/badge`, `@reui/icon-tile`, `@reui/rating`

npm: `motion`

## Purpose
A conversion hero for a developer product whose proof is the product itself. The left column runs badge, highlighted headline, subtitle, a call-to-action row that carries the star rating inline, and a brand row under a separator. The right column is a rebuilt analytics console floating on the design's own gradient backdrop rather than a screenshot.

## Best Fit
Top of a marketing page for a registry, component library, template store, or any tool that wants to show its interface and its social proof in the same glance. The rating sits inside the action row, so it reads as reassurance at the click rather than as a separate testimonial band.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the section, the conversion column, and the layered right column. The frame is pinned to 4:3, and its two insets are `cqw` shares of the frame width rather than breakpoint steps, so the whole assembly scales as one piece.
- `components/app-frame.tsx` rebuilds the product shot as real markup (`Card`, `Table`, `Item`, `Progress`, `Badge`, `IconTile`, `Avatar` and `Kbd`), exposed to assistive tech as a single `role="img"` so no focusable control is planted inside decorative art.
- `components/frame-backdrop.tsx` is the photographic backdrop, loaded from Unsplash's CDN rather than approximated with gradient stops or inlined as base64. `rot=180` is baked into the URL, so the element needs no rotation of its own and the drift keeps `transform` to itself. It is the block's only other client component, which is what keeps `motion` off the static conversion column.
- `components/data.tsx` holds the brand marks and the rating figures.

## LLM Guidance
The conversion column is a `@container`, so the headline scales with the column rather than the viewport. The lime highlight is an inline `box-decoration-clone` span with its ink pinned, because lime stays light in both themes.

The console is authored at a real desktop size (1400 x 1000) and scaled down as one piece, which is what makes it read as a screenshot; authoring it at final size forces type up to a ~23px desktop equivalent and the panels crowd. Retheming it means editing the `PANEL` constant and the paired `dark:` classes in `app-frame.tsx` rather than the block's tokens, because it stands on a photograph rather than on the page: neutrals invert, tinted status pills become low-alpha fills of their own hue, and the chart hues stay identical in both themes so a series keeps its identity.

Motion is split on purpose. The backdrop drift is one always-on loop, so it uses the `motion` library with `useReducedMotion`, and its `initial` scale is server-rendered so the first paint has nothing to pop from. The console keeps CSS keyframes injected via `<style>`, killed by a `prefers-reduced-motion` rule: it runs 65 ambient layers, 52 of them sparkline and stacked bars, and 7 of them are `td::after` pseudo-elements no JS library can target. Do not port those to `motion`, it would move 65 compositor animations onto the main thread. Ambient loops in the console are staggered by a `--hero2-delay` custom property set per element, which is what stops the four KPI values rising on the same frame; periods are mutually non-harmonic so they never resolve into one pulse. Swap `HERO_BRANDS` for real logos and `HERO_RATING` for real figures; the star row is `aria-hidden` because the line under it states the same numbers. Swap the backdrop by editing `FRAME_BACKDROP_SRC`: any wide abstract image works, and the CDN query owns the crop, so drop `rot=180` unless the replacement also needs turning. Leave `auto=format` off, this gradient encodes larger as AVIF than as JPEG.

### `hero-3`

Emerald registry hero with an animated isometric scene of floating product blocks

Dark emerald marketing hero for a component registry: Next.js badge, highlighted headline, MCP and Agent Skills capability chips, lime primary call to action, trusted-by brand row, and an animated isometric scene of eight extruded product cards with staggered entrance, ambient float, hover lift, axis packets, and expanding ground pulses.

Uses: `@reui/badge`, `@reui/frame`, `@reui/icon-tile`

npm: `motion`

## Purpose
A conversion hero for a component registry or developer platform that wants to show the product itself rather than describe it. The left column carries the pitch; the right column renders eight real blocks as extruded solids on an isometric plane.

## Best Fit
Top of a marketing page for a registry, design system, or template library. The scene doubles as a product shot, so it suits pages where catalog breadth is the argument.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the emerald surface, the conversion column, and the scene mount.
- `components/isometric-scene.tsx` projects every solid with a 2D matrix, sweeps its thickness from the same matrix, and owns all motion as CSS keyframes.
- `components/scene-cards.tsx` holds the eight card faces, each composed from stock primitives.
- `components/hero-dot-field.tsx` tiles the section-wide dot pattern.
- `components/data.tsx` holds the scene geometry, capability chips, and brand marks.

## LLM Guidance
The surface is dark in both themes, so the greens and the lime accent are literal. The scene is drawn on a fixed 624 by 600 canvas and scaled with `calc(100cqw/624)`, so never convert its coordinates to percentages. Each card face is authored at a natural size and scaled onto its plane face, which is why `contentWidth / contentHeight` must keep the same ratio as `width / height`. `PROJECTIONS` carries the four matrices used in the scene together with the 6 unit extrusion in face space, and `extrusionShadow` sweeps the rounded face along it, so a new card needs only a projection name and never hand drawn side faces. The scene re-scopes the theme tokens to light, so card faces should use stock primitive surfaces and add no colour classes.

### `hero-4`

Split Registry Hero With A Console On A Drifting Photo Backdrop

Split marketing hero for a component registry: live-status badge with a success dot, two-tone headline, subtitle, Next.js and v0 capability rows, a primary and outline action pair, and a rebuilt analytics console floating on a drifting photographic backdrop, with full dark mode.

Uses: `@reui/badge`

npm: `motion`

## Purpose
A conversion hero for a developer product whose proof is the product itself. The left column runs a live-status badge, a two-tone headline whose second line drops to muted ink, a subtitle, two capability rows, and a primary plus outline action pair. The right column is a rebuilt analytics console floating on the design's own photographic backdrop.

## Best Fit
Top of a marketing page for a registry, component library, or template store that wants the interface visible above the fold. The capability rows carry stack compatibility as plain statements rather than as a logo wall, so they read as facts rather than as social proof.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the section, the conversion column, and the layered right column. The frame is pinned to 4:3, and its two insets are `cqw` shares of the frame width rather than breakpoint steps, so the whole assembly scales as one piece.
- `components/app-frame.tsx` rebuilds the product shot as real markup (`Card`, `Table`, `Item`, `Progress`, `Badge`, `IconTile`, `Avatar` and `Kbd`), exposed to assistive tech as a single `role="img"` so no focusable control is planted inside decorative art.
- `components/frame-backdrop.tsx` draws the backdrop and owns its drift, requesting the design's own photograph from the Unsplash CDN.
- `components/data.tsx` holds the capability rows and their brand marks.

## LLM Guidance
The conversion column is a `@container`, so the headline scales with the column rather than the viewport. The headline's second line is `text-muted-foreground`; that two-tone split is the design's own emphasis and should survive a copy change.

The console is authored at a real desktop size (1400 x 1000) and scaled down as one piece, which is what makes it read as a screenshot; authoring it at final size forces type up to a ~23px desktop equivalent and the panels crowd. Retheming it means editing the `PANEL` constant and the paired `dark:` classes in `app-frame.tsx` rather than the block's tokens, because it stands on a photograph rather than on the page.

The backdrop is cropped to the frame's 4:3 by the `rect` parameter on its request URL, so it needs no runtime `object-fit` and `transform` stays free for the drift. Do not re-fit it; swap the whole URL if you change the art. All motion is CSS keyframes injected via `<style>` in the component that owns it, and every animation is killed by a `prefers-reduced-motion` rule. Swap `HERO_CAPABILITIES` for the real stack claims.

### `hero-5`

Integrations Hero With An Isometric Grid Of Floating Brand Tiles

Split marketing hero for an integrations or MCP product: outline badge, two-line headline, subtitle, blue primary action with an outline companion, an assurance row under a separator, and an isometric grid of eleven extruded brand tiles floating over a masked ground plane with a dot field backdrop.

Uses: `@reui/badge`

npm: `motion`

## Purpose
A conversion hero for a product whose value is what it connects to. The left column runs badge, headline, subtitle, a primary and outline action pair, and three assurances under a separator. The right column is an isometric grid of extruded tiles, each carrying a real brand mark, floating over a masked ground plane.

## Best Fit
Top of a marketing page for an integrations platform, an MCP server catalog, an automation tool, or anything whose pitch is breadth of ecosystem. The grid reads as a catalog at a glance, so it does the work a logo wall usually does while staying a product shot.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the dark surface, the conversion column, and the scaled grid mount.
- `components/stack-grid.tsx` projects every tile with a 2D matrix, sweeps its thickness from the same matrix, draws the ground plane and its guide runs, and owns entrance, float and hover.
- `components/hero-dot-field.tsx` tiles the section-wide dot pattern.
- `components/data.tsx` holds the grid geometry, the brand marks, and the assurance labels.

## LLM Guidance
The surface is dark in both themes, so the ink values are literal rather than token driven. The conversion column is a `@container`, so the headline scales with the column rather than the viewport.

The grid is drawn on a fixed 624 by 600 canvas and scaled with `calc(100cqw/624)`, so never convert its coordinates to percentages. `ISO_MATRIX` is the ground projection and `TILE_EXTRUDE` is the 20 unit thickness in the face's own space; `extrusionShadow` sweeps the rounded face along it, so a new tile needs only a left/top and a mark, never hand drawn side faces. Brand marks lie on the face under the same matrix, which is what the design does: its 24 unit square logo measures 24 * sqrt(3) wide as an instance, and that only holds under this projection.

Entrance, ambient float, the hover lift and the guide-run pulse are Motion and sit on separate elements, because the wrapper that carries the entrance already owns a transform. The pointer listener sits on a wrapper that never transforms; putting it on the element that lifts makes the tile slide out from under the cursor and flicker. `MotionConfig reducedMotion="user"` is what honours the OS setting. Swap `STACK_TILES` for the real integration set; the ground plane and caption stay put.

### `hero-6`

Split registry hero with a live security console over a tower skyline

Conversion hero for a component registry: badge, two-tone headline, action pair, and a frame whose security console is live markup with ambient chart motion, set over twin towers against a rose-to-coral sky, cropped at the frame edge. Uses ReUI Badge, IconTile, Card. For landing page, SaaS hero.

Uses: `@reui/badge`, `@reui/icon-tile`

### `hero-7`

Split cloud platform hero with a pointer-tilted crew console on a black frame

Conversion hero for a cloud platform: Azure badge, two-tone headline, email capture with an lg Join button, and proof lines beside a product frame whose crew coverage console is live markup with ambient chart motion, tilted in 3D by the pointer. Uses ReUI Badge, IconTile, Card, Progress, shadcn InputGroup and the motion library. For landing page, SaaS hero, product screenshot.

Uses: `@reui/badge`, `@reui/icon-tile`

### `hero-8`

Cloud platform hero with inline email capture and a live analytics console

Conversion hero for a cloud or infrastructure product: brand badge, two-tone headline, an email capture that confirms in place, and two proof points beside a 4:3 frame whose analytics console is live markup with ambient chart motion on a drawn bloom backdrop. Uses ReUI Badge, IconTile, InputGroup, Card, Table. For landing page, SaaS hero, waitlist signup.

Uses: `@reui/badge`, `@reui/icon-tile`

### `hero-9`

Registry hero with a tabbed console on a sky field

Conversion hero for a shadcn/ui registry or MCP tool: an eyebrow badge, a headline with an amber marker highlight, a star rating with review count, and an Open in Cursor / View in Figma action pair. Below it a framed registry console floats on a sky backdrop: a fixed top bar and sidebar stay put while a six-tab bar swaps the workspace between Overview (registry KPIs, trending blocks, recent activity, and an installs chart), Components, Workflows, Integrations, Templates, and an empty Docs state. Built on ReUI Tabs, Card, Item, Progress, IconTile, Badge, Rating, and Button. For landing page, dev-tool, and product-launch heroes.

Uses: `@reui/badge`, `@reui/icon-tile`, `@reui/rating`

### `hero-10`

Centered AI-registry hero with an editable code card and social proof

Conversion hero for a developer tool: an 'Agent Skills Ready' pill, a two-tone headline, a lede, an editable script.js code card with copy, reset and model/run controls, and a social-proof row of an overlapping avatar group beside a 4.5 star rating and review count. Uses ReUI Badge and Rating, shadcn Avatar group, InputGroup, Separator and IconPlaceholder. For landing pages, dev-tool and SaaS heroes, registry marketing.

Uses: `@reui/badge`, `@reui/rating`

### `hero-11`

Split registry hero with a feature card and a framed analytics console

Marketing hero for a shadcn registry or dev tool: a 'Meet 485+ PRO Blocks' pill over a two-tone headline, a lede with 'Start with Cursor' and 'Read Docs' calls to action, and a content band pairing a three-cell feature card with a 4:3 analytics console rendered as live markup on a prismatic backdrop. Uses ReUI Badge, IconTile, shadcn Button, Card and Table. For landing pages, registry marketing and SaaS heroes.

Uses: `@reui/badge`, `@reui/icon-tile`

## Purpose
A conversion hero for a component registry, MCP-native product, or developer tool. The header band carries the pitch and the two calls to action; the content band below pairs a feature card that spells out the value with a framed analytics console that gives the surface its product evidence.

## Best Fit
Top of a marketing page for a shadcn registry, agent platform, or design-system product. The three feature cells read as a capability list, and the console reads as a real screen rather than decoration.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the header band and the content band.
- `components/data.tsx` holds the three feature cells (icon, title, body); keep the lead cell `featured` so it takes the primary tile and tinted surface.
- `components/app-frame.tsx` draws the analytics console as one `role="img"` on a 1400-wide canvas that scales to fill its frame, with ambient chart motion that respects reduced motion.
- `components/frame-backdrop.tsx` draws the prismatic backdrop the console stands on.

## LLM Guidance
The header and content bands wrap to a single column below the card's min width, so the block is safe in narrow containers. Colors are semantic: the badge, tiles, and buttons follow the active theme, while the framed console and its backdrop are fixed art that holds its color in both themes. Swap the copy in `hero.tsx` and the cells in `data.tsx`; the console content lives in the `KPIS`, `ORDERS`, and `NAV_ITEMS` arrays inside `app-frame.tsx`.

### `hero-12`

Centered registry hero with a brand cloud and a framed analytics console

Conversion hero for a shadcn registry or MCP-native dev tool: a 'Meet 485+ Blocks in ReUI Pro' pill over a two-tone headline, a lede with 'Explore Blocks' and 'Choose Plan' calls to action, a single-row brand cloud of real ReUI wordmarks (Vercel, n8n, Supabase, Stripe, GitHub, OpenAI, Bolt, PayPal), and a wide crew-coverage console rendered as live markup on an azure field. Uses ReUI Badge, IconTile, shadcn Button, Card, Table, Progress and Avatar. For landing pages, registry marketing and SaaS heroes.

Uses: `@reui/badge`, `@reui/icon-tile`

## Purpose
A conversion hero for a component registry, MCP-native product, or developer tool. The centred copy column carries the pitch and the two calls to action; the brand cloud below it supplies social proof from recognizable wordmarks; the framed console gives the surface its product evidence.

## Best Fit
Top of a marketing page for a shadcn registry, agent platform, or design-system product. The brand row reads as a trust bar, and the console reads as a real screen rather than decoration.

## Main Pieces
- `page.tsx` renders the section edge to edge.
- `components/hero.tsx` composes the copy column, the brand cloud, and the framed console.
- `components/data.tsx` holds the brand cloud as `HERO_BRANDS`; every entry is a real ReUI wordmark from `components/ui/svgs`, and marks whose ink is baked in ship a light/dark pair so only the matching one shows.
- `components/app-frame.tsx` draws the crew-coverage console as one `role="img"` on a fixed 1440 by 900 canvas, with ambient chart motion that respects reduced motion. Content lives in the `KPIS`, `CREWS`, `ACTIONS` and `NAV_ITEMS` arrays.
- `components/frame-backdrop.tsx` draws the azure field the console stands on as layered CSS gradients, so the block ships no external art.

## LLM Guidance
The copy column, brand cloud, and framed console stack in a single column at every width, so the block is safe in narrow containers. Colors are semantic - the badge, buttons, and headline follow the active theme - while the framed console and its azure backdrop are fixed art that hold their color in both themes. Swap the copy in `hero.tsx`, the wordmarks in `data.tsx` (keep each as a light/dark pair), and the console content in the arrays inside `app-frame.tsx`.

### `hero-13`

Centered registry hero with a creator cloud and dual calls to action

Conversion hero for a shadcn registry or AI-agent dev tool: an 'Agent Skills Available' announcement pill over a two-tone 'First-class shadcn for AI agents' headline, a curated-registry lede, a seven-person creator cloud paired with a 4.5-star '13.9k Ratings' proof line and a reviews link, and two calls to action, 'Preview in Figma' and a primary 'Start with Cursor' with the Cursor wordmark, over a quiet scroll cue. Uses ReUI Badge and Rating, shadcn Avatar, AvatarGroup and Button, and portable IconPlaceholder icons. For landing pages, registry marketing, and developer-tool heroes.

Uses: `@reui/badge`, `@reui/rating`

### `hero-14`

Split-header hero with a product console on a dark wave field

Editorial marketing hero for a shadcn registry or MCP developer tool: an 'Explore 495+ ReUI Blocks' announcement pill over a two-tone 'Design-ready shadcn / MCP native' headline on the left, a curated-registry lede with 'Buy Now' and 'Explore' calls to action on the right, both bottom-aligned, above a wide 16:10 framed product console standing on a mirrored dark wave field. The console is a crew-coverage operations dashboard rebuilt as real markup, with a KPI strip, a coverage review table, an action queue, and a demand-mix chart, scaled as one screenshot with subtle ambient motion. Uses ReUI Badge, IconTile, shadcn Card, Table, Progress, Item, Avatar and Button, and portable IconPlaceholder icons. For landing pages, registry marketing, and developer-tool heroes.

Uses: `@reui/badge`, `@reui/icon-tile`

### `hero-15`

Bordered blueprint hero with an announcement badge and a three-cell feature grid

Marketing hero for a shadcn/ui registry or MCP tool: an announcement badge, a keyword-emphasized headline and lede, and a Connect/Browse action pair over a three-cell feature grid of icon-tile links. Built on ReUI Badge, IconTile, Item, Button. For landing page and dev-tool heroes.

Uses: `@reui/badge`, `@reui/icon-tile`

### `hero-16`

Split hero with a Built to ship checklist and a bleeding app-shell carousel

Two-column marketing hero for a shadcn/ui registry or MCP tool: a headline, a Built to ship feature checklist, a connect-your-stack logo row (Clerk, n8n, Supabase), and a Connect MCP / Browse Registry action pair, beside an auto-advancing carousel of five product app-shells that bleed off the right edge. The shells are rendered markup rather than screenshots, so they follow the theme in full dark mode. Built on ReUI Card, Button, Item, IconTile, Kbd, IconPlaceholder. For landing page, dev-tool, and product-launch heroes.

Uses: `@reui/badge`, `@reui/icon-tile`

npm: `embla-carousel-autoplay`


## Source

Generated from [`https://reui.io/r/registry.json`](https://reui.io/r/registry.json), sha256 `a598d3b8b544a0fa1fc834d7a590b2b04642c080890c46790c7a5df5e1ea239f`, mirrored 2026-09-04, by `scripts/gen_registry_refs.py`. Counts cross-checked against [`https://reui.io/llms.txt`](https://reui.io/llms.txt) (sha256 `a58bc32429b11535`). Regenerate with `/reui-sync`.
