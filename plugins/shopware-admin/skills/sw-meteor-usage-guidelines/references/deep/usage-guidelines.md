# Meteor Design System — Nutzungsrichtlinien & Best Practices

Quellen: `packages/component-library/src/docs/foundations/`,
`packages/component-library/LIFECYCLE.md`,
`packages/component-library/STORYBOOK_DOCS_STANDARD.md`

---

## 1. Design-Prinzipien

Aus dem offiziellen Meteor Storybook, Seite `Foundations/Design Principles`:

### Accessibility und Inklusivität

Design-Erfahrungen, die für alle Nutzer zugänglich sind. Accessibility ist keine nachträgliche Überlegung — sie prägt Interaktionsmuster, Farbkontrast, Tastaturverhalten und Texte von Anfang an. Basis ist WCAG 2.1 AA.

### Datengestützte Entscheidungen

Annahmen werden mit echten Nutzungsdaten, Usability-Sitzungen und Feedback validiert. Neue Erkenntnisse gehen vor früheren Entscheidungen.

### Sticky Merchant und Shopper Experience

Merchants arbeiten unter kommerziellem Druck und brauchen schnelle, sichere Entscheidungswege. Design reduziert den Abstand zwischen Nutzerziel und Erreichbarkeit.

### Reibung reduzieren, Einfachheit anstreben

Einfachheit bedeutet nicht Fehlende Features, sondern Fehlen unnötiger Hindernisse. Jedes Formularfeld, jedes Label, jeder Modal und jede Bestätigung hat einen Preis.

### Konsistente Erfahrungen

Konsistenz reduziert Lernaufwand. Wenn dasselbe Interaktionsmuster an verschiedenen Stellen erscheint, muss es nur einmal gelernt werden.

### Ethisches Design

Kein Dark-Pattern, keine täuschenden Defaults. Transparenz über gesammelte Daten und irreversible Aktionen.

---

## 2. Komponent-Lifecycle

Aus `packages/component-library/LIFECYCLE.md`:

Jede Komponente hat einen von drei Stadien:

### Future (Experimentell)

- Neue Ideen werden getestet, Feedback gesammelt
- Breaking Changes möglich ohne Vorankündigung
- Nicht produktiv einsetzen

### Stable (Produktionsreif)

Anforderungen für Stable:
- Automatisierte Tests vorhanden
- Meteor Design Tokens verwendet
- WCAG 2.1 AA Level erfüllt
- Storybook Stories als Dokumentation vorhanden

Breaking Changes werden mindestens eine Patch-Version vor einem Major-Release dokumentiert.

### Deprecated

- Nutzung wird abgeraten
- Wenn vorhanden, wird ein Upgrade-Leitfaden bereitgestellt
- Komponente wird in der nächsten Major-Version entfernt

---

## 3. Accessibility Guidelines

Aus `packages/component-library/src/docs/foundations/accessibility.mdx`:

### Was Meteor automatisch bietet

- **Tastaturnavigation**: Alle interaktiven Komponenten sind vollständig per Tastatur bedienbar
- **ARIA-Attribute**: Komponenten enthalten passende Roles, States und Properties
- **Fokus-Management**: In Modals, Dropdowns und Overlays wird der Fokus korrekt verwaltet
- **Farbkontrast**: Design Tokens erfüllen WCAG 2.1 AA für Text und UI-Elemente
- **Dark Mode**: Beide Themes behalten zugängliche Kontrastverhältnisse
- **Screen Reader**: Komponenten werden mit gängigen Assistive Technologies getestet

### Was zusätzlich beachtet werden muss

**Einfachheit wahren**
- Komplexe Flows vermeiden wo einfachere Alternativen existieren
- Konsistente Patterns über Seiten hinweg verwenden
- Prägnante, klare Sprache — passendes Leserlevel für die Zielgruppe

**Inklusiv sein**
- Inklusive Sprache durchgehend verwenden
- Keine Annahmen über Fähigkeiten der Nutzer
- Fachjargon, Metaphern und nicht-wörtliche Phrasen vermeiden

**Textalternativen bereitstellen**
- Klare, prägnante Labels und Alt-Text für alle bedeutsamen Bilder und Icons
- `decorative` Prop bei `mt-icon` für rein visuelle Icons setzen (bleiben aus dem Accessibility-Tree)
- Transkripte oder Untertitel für Video-Inhalte

**Niemals nur auf Farbe verlassen**
- Farbe immer mit sekundärem Indikator kombinieren (Icon, Label, Pattern)
- Semantische Icon-Tokens (`critical`, `positive`, `attention`) zur Verstärkung der Bedeutung nutzen

**Semantisches HTML**
- Landmark-Elemente (`header`, `nav`, `main`, `footer`) für Seitenstruktur
- `div` und `span` nicht als interaktive Elemente verwenden
- Überschriften-Hierarchie logisch einhalten

**Nutzerkontrolle geben**
- Layouts passen sich allen Bildschirmgrößen an (Reflow)
- `prefers-reduced-motion` respektieren
- Ausreichend Zeit für zeitkritische Interaktionen

**Breit testen**
- Tastatur-only Navigation testen
- Screen Reader testen (VoiceOver, NVDA oder JAWS)
- Möglichst Tests mit echten Nutzern mit Behinderungen

### Pre-Ship Checkliste

- Alle interaktiven Elemente per Tastatur allein erreichbar und bedienbar
- Keine Tastatur-Fokus-Traps außerhalb von Modals/Overlays
- Alle Bilder und bedeutsame Icons haben beschreibende Labels oder Alt-Text
- Farbe ist niemals der einzige Indikator für Zustand oder Bedeutung
- Text und UI-Elemente erfüllen WCAG 2.1 AA Kontrastverhältnisse
- Überschriften-Level folgen logischer Hierarchie ohne Sprünge
- Formularfelder haben sichtbare Labels via `for`/`id` oder `aria-labelledby`
- Animationen und Übergänge respektieren `prefers-reduced-motion`

### Empfohlene Tools

- **[WAVE](https://wave.webaim.org/)**: Visuelles Feedback-Tool für Barrierefreiheits-Check
- **[Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/)**: Eingebaut in Chrome DevTools, bietet Accessibility-Score

---

## 4. Content & Wording Guidelines

Aus `packages/component-library/src/docs/foundations/content/wording.mdx`:

### Schreibziele

- **Befähigen (Empower)**: Sprache, die informiert und ermutigt
- **Respektieren**: Nicht herablassend, inklusiv und rücksichtsvoll
- **Lehren (Educate)**: Genau die nötigen Informationen, keine Marketing-Sprache
- **Einbinden (Engage)**: Relevanter Inhalt, konversationaler Ton

### Unsere Schreibweise

- **Klar**: Einfache Wörter und Sätze
- **Nützlich**: Immer fragen: Welchen Zweck erfüllt das? Wer liest es? Was müssen sie wissen?
- **Freundlich**: Wie ein Mensch schreiben — alle Inhalte sollen warm und menschlich sein
- **Angemessen**: Ton je nach Zielgruppe und Thema anpassen

### Aktive Stimme

Fast immer aktiv schreiben. Aktiv: Subjekt macht die Aktion. Passiv: Aktion wird am Subjekt vollzogen.

```
✓ Jennifer logged into the account
✗ The account was logged into by Jennifer
```

Passiv nur wenn: Shopware/ich als Subjekt vermieden werden soll; die Aktion nicht persönlich ausgeführt wurde; das Objekt wichtiger als das Subjekt ist.

### Inklusive Sprache

Menschen-zuerst-Sprache. Nie auf Charakteristika wie Geschlecht, sexuelle Orientierung, Religion oder Fähigkeiten konzentrieren, außer es ist relevant.

| Thema | Richtig | Falsch |
|---|---|---|
| Technik | `allowlist`, `blocklist` | `whitelist`, `blacklist` |
| Technik | `main`, `primary` | `master` |
| Geschlecht | `they` | `him/her`, `he/she` |
| Gruppen | `people`, `folks`, `teammates` | `guys` |
| Rollen | Neutrale Titel | `ninja`, `rockstar`, `wizard` |
| Ressourcen | `workforce` | `manpower` |
| Beziehungen | `spouse`, `partner` | `wife/husband` |

### Abkürzungen und Akronyme

Beim ersten Vorkommen ausschreiben, dann Kurzform verwenden. Bekannte Abkürzungen (API, HTML) direkt nutzen.

### Groß-/Kleinschreibung

Shopware-Feature-Namen werden immer großgeschrieben: Rule Builder, Sales Channel, Flow Builder, B2B Components.

### Buttons

- Button-Labels so kurz wie möglich
- Verb, das die Aktion beschreibt: `Save`, `Delete`, `Continue to checkout`
- Kein Artikel: `Save product` nicht `Save the product`

### Nutzer ansprechen

Im Englischen: `you` und `your` für alle Zielgruppen.

Im Deutschen: Informelle Anrede (Du). In der Shopware-Administration sind Du, Dich, Dir und Dein großgeschrieben (als Zeichen des Respekts).

Beispiel: *Speichere das Produkt, bevor Du die Seite verlässt.*

---

## 5. Storybook Docs Standard

Aus `packages/component-library/STORYBOOK_DOCS_STANDARD.md`:

### Seitenstruktur für Komponent-Dokumentation

```mdx
<StorybookPageHeader
  title="Component name"
  tagName="mt-component-name"
  packageImports="MtComponentName"
  sourcePath="packages/component-library/src/components/group/mt-component-name"
>
  Kurzbeschreibung
</StorybookPageHeader>

## When to use

## Examples

### Basic

Hauptbeispiel

### Weiteres Beispiel

## Anatomy

## API reference

## Do

## Don't

## Behavior notes

## Accessibility notes

## Comparisons
```

### Regeln

- `StorybookPageHeader` startet jede Seite — enthält H1
- Format: `Component name (mt-component-name)`
- `sourcePath`: Repo-relativer Pfad zum Komponent-Ordner (für GitHub-Link)
- Kurzebeschreibung als Kinder von `StorybookPageHeader` (MDX-Richtext)
- Standard-Status: `Available`; `Experimental` oder `Deprecated` wenn stärker signalisiert werden muss
- `Examples` ist Pflicht
- `Anatomy`, `Behavior notes`, `Comparisons` optional, nur wenn echter Mehrwert

### Optionale Sektionen

- **Anatomy**: Wenn Struktur, Komposition oder interne Teile erklärt werden müssen
- **Behavior notes**: Wenn Verhalten nicht-offensichtlich, stateful oder leicht misszuverstehen ist
- **Comparisons**: Wenn Nutzer wahrscheinlich zwischen dieser und einer anderen Komponente wählen

### Stories

- Jede Komponente hat eine `Default`-Story (häufigster Zustand)
- Weitere Stories: menschenlesbare, nutzerseitige Namen, erster Buchstabe groß: `Variants`, `Sizes`, `Inline edit`
- Mindestens ein `Canvas`-Beispiel das empfohlene Verwendung zeigt
- Statische, kopierfähige Story-Code für Doku-Beispiele bevorzugen

### In Prose

- Komponent-Namen in **fett** und groß: **Button**, **Badge**, **Promo Badge**
- Keine `mt-*`-Tagnamen in Fließtext außer wenn der Tagname selbst erklärt wird

### API Reference

- Storybook API-Tabellen für Props, Slots und Events wo möglich
- Tabelle direkt unter `API reference` ohne Untersektion
- Eigener Abschnitt für `exposed methods` nur wenn Komponente tatsächlich öffentliche Methoden exponiert

### Companion Exports

Wenn Komponenten zusammengehörige Teile ohne eigene Seite haben (z.B. `mt-action-menu-item`, `mt-modal-root`), werden diese auf der Elternseite dokumentiert. Erklären: was jeder Teil macht, wann er verwendet wird, wie Teile zusammenpassen, Reihenfolge-/Verschachtelungsanforderungen.

Wichtige Vergleiche für Storybook:
- tooltip vs help text
- floating ui vs action menu
- select vs radio group
- checkbox vs radio group vs select

---

## 6. Token-Nutzung — Do & Don't

### Spacing

```css
/* ✓ Richtig */
a { margin: var(--scale-size-10); }
.grid { row-gap: var(--scale-size-8); }

/* ✗ Falsch */
a { margin: 10px; }
.grid { row-gap: 0.5rem; }
```

Negierung: `calc(var(--scale-size-8) * -1)` statt `-8px`.

### Border-Radius

```css
/* ✓ Richtig */
.card { border-radius: var(--border-radius-card); }
.badge { border-radius: var(--border-radius-round); }

/* ✗ Falsch */
.badge { border-radius: 999px; }
.badge { border-radius: 50%; }
```

**Nicht** `--scale-size-*` für `border-radius` verwenden — das umgeht den semantischen Layer.

### Elevation Surfaces

```css
/* ✓ Richtig */
.page-bg { background: var(--color-elevation-surface-default); }
.card { background: var(--color-elevation-surface-raised); }
.sidebar { background: var(--color-elevation-surface-sunken); }

/* ✗ Falsch */
.page-bg { background: #f5f5f5; }
```

### Farben

```css
/* ✓ Richtig */
a { color: var(--color-text-primary-default); }
button { background-color: var(--color-interaction-primary-default); }
div { background-color: var(--color-elevation-surface-default); }

/* ✗ Falsch */
a { color: var(--gray-800); }         /* primitiver Token */
a { color: #1a1a1a; }                 /* Hardcode */
button { background-color: #189eff; } /* Hardcode */
```

### Typografie

```css
/* ✓ Richtig */
a { font-size: var(--font-size-s); }
a { font-family: var(--font-family-body); }

/* ✗ Falsch */
a { font-size: 16px; }
a { font-family: Inter; }
```

### Token-Anpassung (Customization)

Bestehende Meteor-Tokens NICHT überschreiben (kann zu unerwartetem Divergenz führen und bricht bei Token-Renames).

Eigene Tokens mit eigenem Präfix definieren:

```css
@import "@shopware-ag/meteor-tokens/administration/light.css";
@import "@shopware-ag/meteor-tokens/administration/dark.css";

:root {
  --myapp-color-brand-default: #7c3aed;
  --myapp-color-brand-hover: #6d28d9;
}

[data-theme="dark"] {
  --myapp-color-brand-default: #8b5cf6;
  --myapp-color-brand-hover: #7c3aed;
}
```

---

## 7. Wichtige Token-Referenz-Übersicht

### Token-Namensstruktur

```
[type]-[category]-[instance]-[variant]
```

- **Type**: `color`, `font`, `scale`, `border-radius`
- **Category**: `icon`, `text`, `background`, `elevation` (innerhalb von `color`)
- **Instance**: `primary`, `positive`, `critical`
- **Variant**: `default`, `hover`, `pressed`, `disabled`

### Spacing Scale (--scale-size-*)

| Token | Wert |
|---|---|
| `--scale-size-0` | 0px |
| `--scale-size-1` | 1px |
| `--scale-size-2` | 2px |
| `--scale-size-4` | 4px |
| `--scale-size-8` | 8px |
| `--scale-size-12` | 12px |
| `--scale-size-16` | 16px (= 1rem) |
| `--scale-size-24` | 24px |
| `--scale-size-32` | 32px |
| `--scale-size-40` | 40px |
| `--scale-size-48` | 48px |
| `--scale-size-64` | 64px |
| `--scale-size-96` | 96px |
| `--scale-size-128` | 128px |

Richtlinie:
- **4–8px**: Enger interner Abstand (Icon-zu-Label-Gap, Badge-Padding)
- **12–16px**: Standard Komponent-Padding und Item-Spacing
- **24–40px**: Zwischen Formularelementen, Abschnitte innerhalb einer View
- **48–64px**: Zwischen Haupt-Layout-Regionen

### Border-Radius Tokens

**Element-spezifische Tokens (bevorzugen):**
| Token | Wert | Verwendung |
|---|---|---|
| `--border-radius-card` | 8px | Cards und Container-Flächen |
| `--border-radius-button` | 4px | Buttons und Button-ähnliche Controls |
| `--border-radius-checkbox` | 4px | Checkboxen und ähnliche Input-Toggles |

**Semantische Tokens (Fallback):**
| Token | Wert |
|---|---|
| `--border-radius-none` | 0px |
| `--border-radius-xs` | 4px |
| `--border-radius-s` | 6px |
| `--border-radius-m` | 8px |
| `--border-radius-l` | 12px |
| `--border-radius-round` | 9999px |

### Elevation Surface Tokens

| Token | Verwendung |
|---|---|
| `--color-elevation-surface-sunken` | Eingebettete Bereiche: Sidebar-Sektionen, Tabellen-Zebra-Streifen, Code-Blocks |
| `--color-elevation-surface-default` | Hauptseite / Anwendungshintergrund |
| `--color-elevation-surface-raised` | Cards, Panels, Container über dem Hintergrund |
| `--color-elevation-floating-default` | Tooltips und schwebende Elemente |
| `--color-elevation-backdrop-default` | Halbtransparenter Scrim hinter Modals/Drawers |
| `--color-elevation-shadow-default` | Box-Shadow-Farbe für erhobene Elemente wie Popovers |

### Typografie Tokens

```css
--font-family-headings: "Inter";
--font-family-body: "Inter";

/* Gewichte */
--font-weight-regular: 400;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

**Scale (Name → Verwendung):**
- `3xl`, `2xl`: Seitentitel, Haupt-Section-Header
- `xl`, `l`: Sub-Sektionen
- `m`, `s`: Card- und Abschnitts-Überschriften
- `xs`: Body-Text, Support-Labels, Metadaten

**Regel**: `--font-size-*` immer mit passendem `--font-line-height-*` kombinieren.

Maximale Zeilenlänge für Body-Text: `max-width: 65ch`

### Verwendung von mt-text

```html
<mt-text size="2xl" weight="semibold">Seitentitel</mt-text>
<mt-text size="s">Body-Text</mt-text>
<mt-text size="xs" color="color-text-secondary-default">Unterstützendes Label</mt-text>
<mt-text size="s" as="span">Inline-Text</mt-text>
```

Das `as`-Prop steuert das HTML-Element (Standard: `p`).
