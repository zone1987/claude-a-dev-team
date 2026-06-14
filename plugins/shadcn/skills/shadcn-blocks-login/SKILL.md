---
name: shadcn-blocks-login
description: Complete code for all 5 shadcn/ui login blocks (login-01 to login-05). Use when implementing shadcn login block, shadcn Anmeldeseite, login form shadcn, shadcn login page, shadcn login-01, shadcn Loginformular, authentication UI shadcn.
---

# shadcn/ui Login Blocks (login-01 – login-05)

Five ready-to-use login page blocks for shadcn/ui v4 (New York style).

## Installation

```bash
npx shadcn@latest add login-01   # centered card, simple
npx shadcn@latest add login-02   # two-column with hero image, left form
npx shadcn@latest add login-03   # muted bg, card, social buttons top
npx shadcn@latest add login-04   # wide card with image panel, 3 social icons
npx shadcn@latest add login-05   # minimal, logo-centered, email-only + social
```

## Block Overview

| Block | Layout | Social Auth | Notes |
|-------|--------|-------------|-------|
| login-01 | Centered card | Google (button) | Simple email + password |
| login-02 | Two-column hero image | GitHub (button) | Full-page split |
| login-03 | Muted bg, centered | Apple + Google | Social first, then email |
| login-04 | Wide card, image right | Apple + Google + Meta | 3 icon-only social buttons |
| login-05 | Minimal, no card | Apple + Google | Email-only magic link style |

## Complete Source Code

See reference files:
- [references/login-01-03.md](references/login-01-03.md) — login-01, login-02, login-03
- [references/login-04-05.md](references/login-04-05.md) — login-04, login-05

## Usage Pattern

All login blocks use shadcn/ui `Field`, `FieldGroup`, `FieldLabel`, `FieldDescription`, `FieldSeparator` from the `field` component (v4 pattern), plus `Button`, `Input`, `Card`.

```tsx
// In your Next.js app router:
// Copy page.tsx → app/login/page.tsx
// Copy components/login-form.tsx → components/login-form.tsx
```

## Source

`/tmp/shadcn-repo/apps/v4/registry/new-york-v4/blocks/login-{01..05}/`
