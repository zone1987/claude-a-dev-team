# shadcn-vue Login Blocks

Diese Skill-Referenz enthält 5 fertige Login-Seiten-Blöcke aus der shadcn-vue Registry (new-york-v4). Jeder Block besteht aus einer `page.vue` und einer `components/LoginForm.vue` und kann per CLI direkt installiert werden.

## Überblick

| Block | Layout | Social-Auth |
|-------|--------|-------------|
| login-01 | Zentriertes Card-Formular | Google |
| login-02 | Zwei Spalten mit Cover-Image | GitHub |
| login-03 | Muted Background, Card mit Social-Buttons | Apple + Google |
| login-04 | Muted Background, Card mit Side-Image | Apple + Google + Meta |
| login-05 | Minimalistisch, Email-only mit Social | Apple + Google |

---

## login-01: Einfaches Login-Formular (Card-Layout, zentriert)

**Installation:**
```bash
npx shadcn-vue@latest add login-01
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Beschreibung:** Zentriertes Login-Formular in einer Card-Komponente. Email- und Passwort-Felder, "Forgot your password?"-Link, Login-Button, Google-OAuth-Button und Sign-up-Link. Verwendet `Card`, `Field`, `FieldGroup`, `Input`, `Button`.

---

## login-02: Zwei-Spalten-Layout mit Cover-Image

**Installation:**
```bash
npx shadcn-vue@latest add login-02
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Beschreibung:** Zweispaltiges Layout: links das Login-Formular mit Logo und Markenname, rechts ein Cover-Bild (bg-muted, hidden auf Mobile). Keine Card-Wrapper — das Formular steht direkt in einem `<form>`-Tag. GitHub-OAuth-Button. Verwendet `FieldSeparator`.

---

## login-03: Muted Background mit Card und Social-Auth oben

**Installation:**
```bash
npx shadcn-vue@latest add login-03
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Beschreibung:** Muted Background-Seite mit Logo-Link oben. Card mit zentriertem Header ("Welcome back"). Social-Buttons (Apple + Google) stehen vor dem Email/Passwort-Formular, getrennt durch einen `FieldSeparator`. Enthält Terms-of-Service-Hinweis unterhalb der Card.

---

## login-04: Muted Background mit Card und Seiten-Image (Apple + Google + Meta)

**Installation:**
```bash
npx shadcn-vue@latest add login-04
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Beschreibung:** Muted Background mit einer Card, die intern zweispaltig (`md:grid-cols-2`) ist: links das Formular, rechts ein Placeholder-Bild (hidden auf Mobile). Social-Icons (Apple, Google, Meta) als Icon-only Buttons in einem 3-Spalten-Grid. Enthält Terms-Hinweis unter der Card.

---

## login-05: Minimalistisches Email-only Login mit Social-Buttons

**Installation:**
```bash
npx shadcn-vue@latest add login-05
```

**Files:**
- `page.vue`
- `components/LoginForm.vue`

**Beschreibung:** Sehr schlankes Design ohne Card-Wrapper. Logo-Icon, Titel, Sign-up-Link, nur ein Email-Eingabefeld, Login-Button, Trenner und zwei Social-Buttons (Apple + Google) nebeneinander in einem responsiven 2-Spalten-Grid. Terms-Hinweis darunter.

---

## Referenz-Dateien

- [LOGIN-01-02.md](LOGIN-01-02.md) — Vollständiger Code für login-01 und login-02
- [LOGIN-03-04.md](LOGIN-03-04.md) — Vollständiger Code für login-03 und login-04
- [LOGIN-05.md](LOGIN-05.md) — Vollständiger Code für login-05
