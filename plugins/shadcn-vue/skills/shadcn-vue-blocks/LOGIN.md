# shadcn-vue Login Blocks

This skill reference contains 5 ready-made login page blocks from the shadcn-vue registry (new-york-v4). Each block consists of a `page.vue` and a `components/LoginForm.vue` and can be installed directly via the CLI.

## Overview

| Block | Layout | Social-Auth |
|-------|--------|-------------|
| login-01 | Centered card form | Google |
| login-02 | Two columns with cover image | GitHub |
| login-03 | Muted background, card with social buttons | Apple + Google |
| login-04 | Muted background, card with side image | Apple + Google + Meta |
| login-05 | Minimalist, email-only with social | Apple + Google |

---

## login-01: simple login form (card layout, centered)

**Installation:**
```bash
npx shadcn-vue@latest add login-01
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Description:** Centered login form inside a card component. Email and password fields, "Forgot your password?" link, login button, Google OAuth button and sign-up link. Uses `Card`, `Field`, `FieldGroup`, `Input`, `Button`.

---

## login-02: two-column layout with cover image

**Installation:**
```bash
npx shadcn-vue@latest add login-02
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Description:** Two-column layout: the login form with logo and brand name on the left, a cover image on the right (bg-muted, hidden on mobile). No card wrapper — the form sits directly inside a `<form>` tag. GitHub OAuth button. Uses `FieldSeparator`.

---

## login-03: muted background with card and social auth on top

**Installation:**
```bash
npx shadcn-vue@latest add login-03
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Description:** Muted background page with a logo link at the top. Card with a centered header ("Welcome back"). The social buttons (Apple + Google) come before the email/password form, separated by a `FieldSeparator`. Includes a terms-of-service note below the card.

---

## login-04: muted background with card and side image (Apple + Google + Meta)

**Installation:**
```bash
npx shadcn-vue@latest add login-04
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Description:** Muted background with a card that is internally two-column (`md:grid-cols-2`): the form on the left, a placeholder image on the right (hidden on mobile). Social icons (Apple, Google, Meta) as icon-only buttons in a 3-column grid. Includes a terms note below the card.

---

## login-05: minimalist email-only login with social buttons

**Installation:**
```bash
npx shadcn-vue@latest add login-05
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Description:** Very lean design without a card wrapper. Logo icon, title, sign-up link, a single email input field, login button, separator and two social buttons (Apple + Google) side by side in a responsive 2-column grid. Terms note below.

---

## Reference files

- [LOGIN-01-02.md](LOGIN-01-02.md) — Complete code for login-01 and login-02
- [LOGIN-03-04.md](LOGIN-03-04.md) — Complete code for login-03 and login-04
- [LOGIN-05.md](LOGIN-05.md) — Complete code for login-05
