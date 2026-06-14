---
name: shadcn-vue-form
description: >
  Form-Komponente (shadcn-vue): Zugaengliche Formular-Abstraktion ueber vee-validate und Zod.
  Automatische ARIA-Attribute, eindeutige IDs, typgeprueft via toTypedSchema. Re-exportiert
  Form, FormField, FormFieldArray aus vee-validate. Abloesung durch Field-Komponente empfohlen.
triggers:
  - shadcn-vue form
  - Form vee-validate vue
  - FormField vue shadcn
  - vee-validate zod vue
  - useForm vue
  - form validation shadcn
---

# shadcn-vue Form

Zugaengliche Formular-Abstraktion ueber vee-validate + Zod. Setzt automatisch ARIA-Attribute
(aria-describedby, aria-invalid) und verwaltet eindeutige IDs pro Feld.

Hinweis: shadcn-vue empfiehlt fuer neue Projekte die `Field`-Komponente statt `Form`.

## Verwendung

Lade die Referenzen:
- `references/installation.md` — CLI- und manuelle Installation
- `references/source.md` — Vollstaendiger Quellcode aller Komponenten
- `references/api.md` — Komponenten, useFormField Composable
- `references/examples.md` — Basic Form und Form mit Checkbox
