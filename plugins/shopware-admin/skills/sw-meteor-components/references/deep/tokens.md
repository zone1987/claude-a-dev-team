# Meteor Tokens — Design-Token-Referenz

Paket: `@shopware-ag/meteor-tokens`

## Einbindung

```css
/* Primitive Farb-Palette (reine Farben, nicht semantisch) */
@import '@shopware-ag/meteor-tokens/deliverables/foundation/primitives.css';

/* Semantische Admin-Tokens — Light-Theme */
@import '@shopware-ag/meteor-tokens/deliverables/administration/light.css';

/* Semantische Admin-Tokens — Dark-Theme */
@import '@shopware-ag/meteor-tokens/deliverables/administration/dark.css';
```

Das Light-Theme gilt für `:root`, das Dark-Theme für `[data-theme='dark']`.

## Token-Kategorien

### Farb-Primitive (`foundation/primitives.css`)

Basis-Farbpaletten als CSS-Custom-Properties, nicht direkt verwenden (werden von semantischen Tokens referenziert):

| Palette | Stufen | Beispiel |
|---|---|---|
| `--color-slate-*` | 50–950 | `--color-slate-900: #2b2e3a` |
| `--color-blue-*` | 50–900 | `--color-blue-500: #189eff` |
| `--color-yellow-*` | 50–900 | |
| `--color-pumpkin-*` | 50–900 | |
| `--color-pink-*` | 50–900 | |
| `--color-purple-*` | 50–900 | |
| `--color-emerald-*` | 50–900 | |
| `--color-zinc-*` | 0–950 | `--color-zinc-0: #ffffff` |
| `--color-scale-size-*` | 0–640 (in 4px-Schritten) | `--scale-size-16: 1rem` |

### Interaktion (`--color-interaction-*`)

Für interaktive Elemente (Buttons etc.):

```css
--color-interaction-primary-default    /* Primär-Button Hintergrund */
--color-interaction-primary-hover
--color-interaction-primary-pressed
--color-interaction-primary-disabled
--color-interaction-secondary-default  /* Sekundär-Button */
--color-interaction-secondary-hover
--color-interaction-secondary-pressed
--color-interaction-secondary-disabled
--color-interaction-secondary-dark
--color-interaction-critical-default   /* Kritische Aktion */
--color-interaction-critical-hover
--color-interaction-critical-pressed
--color-interaction-critical-disabled
```

### Elevation / Oberflächen (`--color-elevation-*`)

Für Hintergründe von Cards, Modals, Overlays:

```css
--color-elevation-surface-sunken      /* Abgesenkte Bereiche */
--color-elevation-surface-default     /* Standard-Oberfläche */
--color-elevation-surface-selected    /* Ausgewählter Zustand */
--color-elevation-surface-hover       /* Hover-Zustand */
--color-elevation-surface-raised      /* Erhöhte Elemente */
--color-elevation-surface-overlay     /* Overlay-Hintergrund */
--color-elevation-surface-frame       /* Frame-Hintergrund */
--color-elevation-surface-backdrop    /* Modal-Backdrop */
--color-elevation-surface-floating    /* Floating UI (Tooltips, Dropdowns) */
--color-elevation-backdrop-default    /* Backdrop-Farbe mit Opacity */
--color-elevation-floating-default    /* Floating-Elemente */
--color-elevation-shadow-default      /* Box-Shadow */
```

### Hintergrundfarben (`--color-background-*`)

Für semantische Hintergründe:

```css
--color-background-primary-default
--color-background-primary-disabled
--color-background-secondary-default
--color-background-tertiary-default
--color-background-brand-default     /* Brand-Blau-Hintergrund */
--color-background-critical-default  /* Rot-Hintergrund */
--color-background-critical-dark
--color-background-attention-default /* Gelb/Orange-Hintergrund */
--color-background-positive-default  /* Grün-Hintergrund */
--color-background-accent-default    /* Lila-Hintergrund */
```

### Icon-Farben (`--color-icon-*`)

```css
--color-icon-primary-default         /* Standard-Icons */
--color-icon-primary-disabled
--color-icon-primary-inverse
--color-icon-secondary-default       /* Sekundäre Icons */
--color-icon-brand-default           /* Brand-Icons */
--color-icon-critical-default        /* Fehler-Icons */
--color-icon-attention-default       /* Warn-Icons */
--color-icon-positive-default        /* Erfolgs-Icons */
--color-icon-accent-default          /* Akzent-Icons */
--color-icon-static-default          /* Immer weiß */
--color-icon-static-dark             /* Immer schwarz */
```

### Rahmenfarben (`--color-border-*`)

```css
--color-border-primary-default
--color-border-secondary-default
--color-border-brand-selected
--color-border-brand-default
--color-border-brand-disabled
--color-border-critical-default
--color-border-critical-dark
--color-border-critical-disabled
--color-border-attention-default
--color-border-positive-default
--color-border-accent-default
```

### Textfarben (`--color-text-*`)

```css
--color-text-primary-default         /* Haupt-Text */
--color-text-primary-disabled
--color-text-primary-inverse         /* Text auf dunklem Hintergrund */
--color-text-secondary-default       /* Sekundärer Text */
--color-text-secondary-disabled
--color-text-brand-default           /* Brand-farbener Text */
--color-text-brand-hover
--color-text-brand-pressed
--color-text-brand-disabled
--color-text-brand-inverse
--color-text-critical-default        /* Fehler-Text */
--color-text-critical-hover
--color-text-attention-default       /* Warn-Text */
--color-text-positive-default        /* Erfolgs-Text */
--color-text-accent-default          /* Akzent-Text */
--color-text-static-default          /* Immer weiß */
--color-text-static-dark             /* Immer schwarz */
--color-text-inverse-default
--color-static-white: #ffffff
--color-static-black: #09090b
```

### Typografie

```css
--font-family-headings: 'Inter'
--font-family-body: 'Inter'

/* Schriftgrößen */
--font-size-2xs: 0.75rem    /* 12px */
--font-size-xs: 0.875rem    /* 14px */
--font-size-s: 1rem          /* 16px */
--font-size-m: 1.125rem     /* 18px */
--font-size-l: 1.25rem      /* 20px */
--font-size-xl: 1.5rem      /* 24px */
--font-size-2xl: 1.75rem    /* 28px */
--font-size-3xl: 2rem        /* 32px */

/* Schriftstärken */
--font-weight-regular: 400
--font-weight-medium: 500
--font-weight-semibold: 600
--font-weight-bold: 700

/* Zeilenhöhen */
--font-line-height-2xs: 1.125rem
--font-line-height-xs: 1.375rem
--font-line-height-s: 1.625rem
--font-line-height-m: 1.75rem
--font-line-height-l: 1.875rem
--font-line-height-xl: 2rem
--font-line-height-2xl: 2.25rem
--font-line-height-3xl: 2.5rem
```

### Border-Radius

```css
--border-radius-card: 0.5rem      /* 8px — Karten */
--border-radius-overlay: 0.25rem  /* 4px — Modals, Dropdowns */
--border-radius-button: 0.25rem   /* 4px — Buttons */
--border-radius-checkbox: 0.25rem
--border-radius-none: 0
--border-radius-2xs: 0.125rem    /* 2px */
--border-radius-xs: 0.25rem      /* 4px */
--border-radius-s: 0.375rem      /* 6px */
--border-radius-m: 0.5rem        /* 8px */
--border-radius-l: 0.75rem       /* 12px */
--border-radius-xl: 1rem         /* 16px */
--border-radius-2xl: 1.25rem     /* 20px */
--border-radius-3xl: 1.5rem      /* 24px */
--border-radius-4xl: 2rem        /* 32px */
--border-radius-round: 624.9375rem  /* Vollständig rund */
```

### Skalierungsgrößen (`--scale-size-*`)

Abstände und Größen in 4px-Schritten (Grundlage 0.25rem = 4px):

```css
--scale-size-0: 0
--scale-size-2: 0.125rem   /* 2px */
--scale-size-4: 0.25rem    /* 4px */
--scale-size-8: 0.5rem     /* 8px */
--scale-size-12: 0.75rem   /* 12px */
--scale-size-16: 1rem      /* 16px */
--scale-size-20: 1.25rem   /* 20px */
--scale-size-24: 1.5rem    /* 24px */
--scale-size-32: 2rem      /* 32px */
--scale-size-40: 2.5rem    /* 40px */
--scale-size-48: 3rem      /* 48px */
/* ... bis --scale-size-640 */
```

## Tailwind-Integration

```css
/* Standard */
@import '@shopware-ag/meteor-tokens/deliverables/tailwind.css';

/* Administration-spezifisch */
@import '@shopware-ag/meteor-tokens/deliverables/tailwind-administration.css';
```

Die Tailwind-Dateien mappen die CSS-Custom-Properties auf Tailwind-Utility-Klassen.
