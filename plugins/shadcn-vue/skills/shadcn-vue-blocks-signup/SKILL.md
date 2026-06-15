---
name: shadcn-vue-blocks-signup
description: >
  shadcn-vue Signup-Blocks (signup-01 bis signup-05) — fertige Registrierungsseiten mit
  Email/Passwort, Social-Auth, Cover-Image, Card-Layout. Triggers: "shadcn-vue signup block",
  "shadcn vue signup", "signup page vue", "registration form block", "shadcn registration",
  "registrierungsseite vue", "signup mit google vue", "signup vue shadcn", "neues konto vue"
---

# shadcn-vue Signup Blocks

Diese Sammlung enthält 5 fertige Registrierungsseiten-Blöcke für shadcn-vue. Jeder Block kann direkt per CLI installiert werden und liefert eine vollständige `page.vue` + `SignupForm.vue`-Komponentenstruktur.

**Gemeinsame Merkmale aller Blöcke:**
- Vue 3 Composition API mit `<script setup lang="ts">`
- shadcn-vue UI-Komponenten: `Field`, `FieldGroup`, `FieldLabel`, `FieldDescription`, `Input`, `Button`
- Vollständig typisiert (TypeScript)
- Dark-Mode-kompatibel
- Responsive (mobile-first)

**Referenzdateien:**
- `references/signup-01-02.md` — Blocks signup-01 und signup-02 (vollständiger Code)
- `references/signup-03-04.md` — Blocks signup-03 und signup-04 (vollständiger Code)
- `references/signup-05.md` — Block signup-05 (vollständiger Code)

---

## signup-01: Einfaches Registrierungsformular mit Card-Layout

**Installation:**
```bash
npx shadcn-vue@latest add signup-01
```

**Dateien:**
- `page.vue` — Zentriertes Layout, max-w-sm
- `components/SignupForm.vue` — Card mit Name, Email, Passwort, Passwort-Bestätigung + Google-Button

**Beschreibung:** Klassisches Card-basiertes Registrierungsformular mit vollständigen Feldern (Full Name, Email, Passwort + Bestätigung) und einem "Sign up with Google"-Button. Einfachstes Layout ohne Cover-Image.

---

## signup-02: Zwei-Spalten-Layout mit Cover-Image

**Installation:**
```bash
npx shadcn-vue@latest add signup-02
```

**Dateien:**
- `page.vue` — Zwei-Spalten-Grid (Formular links, Bild rechts), Logo-Header
- `components/SignupForm.vue` — Inline-Form (kein Card) mit Name, Email, Passwort, Bestätigung + GitHub-Button + Separator

**Beschreibung:** Zwei-Spalten-Layout mit Logo-Header links und einem Cover-Bild rechts (nur Desktop). Das Formular verwendet kein Card-Wrapper, sondern ein inline `<form>` mit `FieldGroup`. Social-Auth via GitHub mit SVG-Icon.

---

## signup-03: Muted Background mit Card und Social-Auth-Hinweis

**Installation:**
```bash
npx shadcn-vue@latest add signup-03
```

**Dateien:**
- `page.vue` — `bg-muted`-Hintergrund, zentriertes Layout mit Logo-Link
- `components/SignupForm.vue` — Card mit zentriertem Header, Name, Email, Passwort-Grid (2 Spalten) + ToS-Hinweis unten

**Beschreibung:** Muted-Background-Layout mit Logo oben. Das Formular ist in eine Card eingebettet mit zentriertem Header. Passwort und Passwort-Bestätigung liegen nebeneinander in einem 2-Spalten-Grid. Unten ein ToS/Privacy-Policy-Hinweis außerhalb der Card.

---

## signup-04: Card mit Cover-Image und Multi-Provider Social-Auth

**Installation:**
```bash
npx shadcn-vue@latest add signup-04
```

**Dateien:**
- `page.vue` — `bg-muted`-Hintergrund, Card max-w-4xl
- `components/SignupForm.vue` — Card mit 2-Spalten-Content (Form + Bild), Apple/Google/Meta Icon-Buttons (3er-Grid)

**Beschreibung:** Breite Card (max-w-4xl) mit Formular auf der linken Seite und einem Cover-Bild auf der rechten Seite (Desktop). Social-Auth mit drei Icon-only-Buttons (Apple, Google, Meta) in einem 3-Spalten-Grid. Passwort-Felder im 2-Spalten-Grid. ToS-Hinweis unterhalb der Card.

---

## signup-05: Minimales Email-first-Layout mit Social-Auth

**Installation:**
```bash
npx shadcn-vue@latest add signup-05
```

**Dateien:**
- `page.vue` — `bg-background`, zentriertes Layout, max-w-sm
- `components/SignupForm.vue` — Logo-Link oben, nur Email-Feld, dann Separator + Apple/Google-Buttons (2er-Grid)

**Beschreibung:** Minimales Registrierungsformular ohne Card-Wrapper. Nur ein einzelnes Email-Feld, danach ein "Or"-Separator und zwei Social-Auth-Buttons (Apple, Google) nebeneinander. Logo als zentrierter Link ganz oben. Gleiche Struktur wie login-05, aber für die Registrierung.
