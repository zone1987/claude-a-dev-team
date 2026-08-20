# shadcn-vue Blocks

## Contents

- [What are Blocks?](#what-are-blocks)
- [Installation](#installation)
- [Customization](#customization)
- [Block-Kategorien](#block-kategorien)
- [Alle verfuegbaren Blocks](#alle-verfuegbaren-blocks)
- [Related Skills](#related-skills)

## What are Blocks?

Blocks sind vollstaendige, produktionsreife Seiten-Layouts, die direkt in ein Projekt kopiert
werden koennen. Sie sind aus bestehenden shadcn-vue Komponenten zusammengesetzt und decken
typische UI-Patterns ab: Authentifizierungs-Flows (Login, Signup, OTP), Dashboards, Produkt-
tabellen und Sidebar-Layouts.

Im Unterschied zu einzelnen Komponenten umfasst ein Block mehrere Dateien (Page-Komponente,
Sub-Komponenten, ggf. Daten-Fixtures) und bildet ein vollstaendiges Seiten-Layout ab.

## Installation

```bash
npx shadcn-vue@latest add <block-name>
```

Beispiel:

```bash
npx shadcn-vue@latest add dashboard-01
npx shadcn-vue@latest add login-02
npx shadcn-vue@latest add sidebar-07
```

Die Dateien werden direkt ins Projekt kopiert (standardmaessig nach `src/components/blocks/`)
und koennen anschliessend beliebig angepasst werden. Es gibt keine externe Abhaengigkeit — der
Block gehoert nach dem `add`-Befehl vollstaendig zum eigenen Codebase.

## Customization

Da Blocks durch Kopieren installiert werden, ist jede Datei direkt editierbar:

- Layout und Struktur anpassen
- Farben und Abstande via Tailwind-Klassen aendern
- Daten durch echte API-Calls ersetzen
- Sub-Komponenten extrahieren oder umbenennen
- Beliebige shadcn-vue Komponenten erganzen oder entfernen

## Block-Kategorien

| Kategorie | Beschreibung |
|---|---|
| `dashboard-*` | Admin-Dashboards mit Charts, Tabellen, Karten |
| `login-*` | Login-Formulare (verschiedene Layouts) |
| `signup-*` | Registrierungs-Formulare |
| `otp-*` | One-Time-Password / Code-Eingabe |
| `products-*` | Produkt-Tabellen und -Listen |
| `sidebar-*` | Anwendungs-Layouts mit Sidebar-Navigation |

## Alle verfuegbaren Blocks

Detaillierte Beschreibungen, Dateilisten und Anwendungsfaelle sind in der Referenz dokumentiert:
`OVERVIEW-DETAIL.md`

### Dashboard

| Block | Beschreibung |
|---|---|
| `dashboard-01` | Dashboard mit Sidebar, Datentabelle, Area-Chart und Section-Cards |

### Authentication — Login

| Block | Beschreibung |
|---|---|
| `login-01` | Einfaches zentriertes Login-Formular (E-Mail/Passwort + Google OAuth) |
| `login-02` | Zweispaltig: Cover-Bild links, GitHub OAuth rechts |
| `login-03` | Login auf geda mpftem Hintergrund mit Social Auth |
| `login-04` | Bild links, Card-Layout rechts |
| `login-05` | Minimales Login ohne Card-Wrapper |

### Authentication — Signup

| Block | Beschreibung |
|---|---|
| `signup-01` | Einfaches zentriertes Signup-Formular |
| `signup-02` | Zweispaltig mit Cover-Bild |
| `signup-03` | Signup auf geda mpftem Hintergrund |
| `signup-04` | Signup mit zusaetzlichen Feldern (Vor- und Nachname) |
| `signup-05` | Minimales Signup |

### Authentication — OTP

| Block | Beschreibung |
|---|---|
| `otp-01` | OTP-Eingabe mit 6 Ziffern, zentriert |
| `otp-02` | OTP mit E-Mail-Anzeige und Resend-Link |
| `otp-03` | OTP minimales Layout |
| `otp-04` | OTP mit Countdown-Timer |
| `otp-05` | OTP mit Anleitung und Hilfetext |

### Products

| Block | Beschreibung |
|---|---|
| `products-01` | Produkttabelle mit Suche und Filter |

### Sidebar Layouts

| Block | Beschreibung |
|---|---|
| `sidebar-01` | Einfache Sidebar mit Navigation in Gruppen |
| `sidebar-02` | Sidebar mit aufklappbarer Subnavigation (inset-Variante) |
| `sidebar-03` | Sidebar mit aufklappbarer Subnavigation (floating-Variante) |
| `sidebar-04` | Sidebar mit aufklappbarer Subnavigation (ohne Header) |
| `sidebar-05` | Sidebar mit sekundaerer Navigation (floating) |
| `sidebar-06` | Sidebar mit sekundaerer Navigation (nur Icons) |
| `sidebar-07` | Kollabierbare Sidebar mit Icon-Rail |
| `sidebar-08` | Sidebar mit verschachtelten Unterpunkten und Icons |
| `sidebar-09` | Sidebar mit Workspace-/Team-Switcher |
| `sidebar-10` | Sidebar mit Benutzerprofil im Footer |
| `sidebar-11` | Sidebar mit Floating-Action-Buttons |
| `sidebar-12` | Sidebar mit Datepicker im Footer |
| `sidebar-13` | Sidebar mit Projekt-/Workspace-Navigation |
| `sidebar-14` | Sidebar mit Suche und Einstellungen (minimal) |
| `sidebar-15` | Sidebar mit Breadcrumb und klebrigem Header |
| `sidebar-16` | Sidebar mit schwebender Top-Navigationsleiste |

## Related Skills

- `shadcn-vue-sidebar` — Sidebar-Komponente (Einzelkomponente, API, Props, Composable)
- `shadcn-vue-chart` — Chart-Komponenten fuer Dashboard-Blocks
- `shadcn-vue-data-table` — Datentabellen-Komponente
- `shadcn-vue-input-otp` — OTP-Input-Komponente
