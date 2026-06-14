---
name: shadcn-blocks-signup
description: Complete code for all 5 shadcn/ui signup blocks (signup-01 to signup-05). Use when implementing shadcn signup block, shadcn Registrierungsseite, signup form shadcn, shadcn register page, shadcn signup-01, shadcn Registrierformular, create account UI shadcn.
---

# shadcn/ui Signup Blocks (signup-01 – signup-05)

Five ready-to-use signup/registration page blocks for shadcn/ui v4 (New York style).

## Installation

```bash
npx shadcn@latest add signup-01   # centered card, full fields
npx shadcn@latest add signup-02   # two-column hero image, GitHub social
npx shadcn@latest add signup-03   # muted bg, card, grid password fields
npx shadcn@latest add signup-04   # wide card with image panel, 3 social icons
npx shadcn@latest add signup-05   # minimal, logo-centered, email-only + social
```

## Block Overview

| Block | Layout | Fields | Social Auth |
|-------|--------|--------|-------------|
| signup-01 | Centered card | Name, Email, Password, Confirm | Google |
| signup-02 | Two-column hero | Name, Email, Password, Confirm | GitHub |
| signup-03 | Muted bg, card | Name, Email, Password+Confirm grid | None |
| signup-04 | Wide card, image | Email, Password+Confirm grid | Apple, Google, Meta |
| signup-05 | Minimal, no card | Email only | Apple, Google |

## Complete Source Code

See reference files:
- [references/signup-01-03.md](references/signup-01-03.md) — signup-01, signup-02, signup-03
- [references/signup-04-05.md](references/signup-04-05.md) — signup-04, signup-05

## Usage Pattern

All signup blocks use shadcn/ui `Field`, `FieldGroup`, `FieldLabel`, `FieldDescription`, `FieldSeparator` from the `field` component (v4 pattern), plus `Button`, `Input`, `Card`.

```tsx
// In your Next.js app router:
// Copy page.tsx → app/signup/page.tsx
// Copy components/signup-form.tsx → components/signup-form.tsx
```

## Source

`/tmp/shadcn-repo/apps/v4/registry/new-york-v4/blocks/signup-{01..05}/`
