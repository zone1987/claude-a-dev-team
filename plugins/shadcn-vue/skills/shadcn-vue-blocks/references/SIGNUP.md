# shadcn-vue Signup Blocks

This collection contains 5 ready-made signup page blocks for shadcn-vue. Each block can be installed directly via the CLI and delivers a complete `page.vue` + `SignupForm.vue` component structure.

**Features shared by all blocks:**
- Vue 3 Composition API with `<script setup lang="ts">`
- shadcn-vue UI components: `Field`, `FieldGroup`, `FieldLabel`, `FieldDescription`, `Input`, `Button`
- Fully typed (TypeScript)
- Dark mode compatible
- Responsive (mobile-first)

**Reference files:**
- `SIGNUP-01-02.md` — Blocks signup-01 and signup-02 (complete code)
- `SIGNUP-03-04.md` — Blocks signup-03 and signup-04 (complete code)
- `SIGNUP-05.md` — Block signup-05 (complete code)

---

## signup-01: simple signup form with card layout

**Installation:**
```bash
npx shadcn-vue@latest add signup-01
```

**Files:**
- `page.vue` — Centered layout, max-w-sm
- `components/SignupForm.vue` — Card with name, email, password, password confirmation + Google button

**Description:** Classic card-based signup form with the full set of fields (full name, email, password + confirmation) and a "Sign up with Google" button. The simplest layout, without a cover image.

---

## signup-02: two-column layout with cover image

**Installation:**
```bash
npx shadcn-vue@latest add signup-02
```

**Files:**
- `page.vue` — Two-column grid (form left, image right), logo header
- `components/SignupForm.vue` — Inline form (no card) with name, email, password, confirmation + GitHub button + separator

**Description:** Two-column layout with a logo header on the left and a cover image on the right (desktop only). The form uses no card wrapper but an inline `<form>` with `FieldGroup`. Social auth via GitHub with an SVG icon.

---

## signup-03: muted background with card and social auth note

**Installation:**
```bash
npx shadcn-vue@latest add signup-03
```

**Files:**
- `page.vue` — `bg-muted` background, centered layout with logo link
- `components/SignupForm.vue` — Card with centered header, name, email, password grid (2 columns) + ToS note below

**Description:** Muted background layout with the logo on top. The form is embedded in a card with a centered header. Password and password confirmation sit side by side in a 2-column grid. Below, a ToS/privacy policy note outside the card.

---

## signup-04: card with cover image and multi-provider social auth

**Installation:**
```bash
npx shadcn-vue@latest add signup-04
```

**Files:**
- `page.vue` — `bg-muted` background, card max-w-4xl
- `components/SignupForm.vue` — Card with 2-column content (form + image), Apple/Google/Meta icon buttons (3-column grid)

**Description:** Wide card (max-w-4xl) with the form on the left side and a cover image on the right side (desktop). Social auth with three icon-only buttons (Apple, Google, Meta) in a 3-column grid. Password fields in a 2-column grid. ToS note below the card.

---

## signup-05: minimal email-first layout with social auth

**Installation:**
```bash
npx shadcn-vue@latest add signup-05
```

**Files:**
- `page.vue` — `bg-background`, centered layout, max-w-sm
- `components/SignupForm.vue` — Logo link on top, email field only, then separator + Apple/Google buttons (2-column grid)

**Description:** Minimal signup form without a card wrapper. Only a single email field, then an "Or" separator and two social auth buttons (Apple, Google) side by side. The logo is a centered link at the very top. Same structure as login-05, but for signup.
