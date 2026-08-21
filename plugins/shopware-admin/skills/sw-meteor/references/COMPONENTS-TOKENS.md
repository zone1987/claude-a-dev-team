# Meteor Tokens — design token reference

Package: `@shopware-ag/meteor-tokens`

Additional sources: `packages/component-library/src/docs/foundations/tokens/` (Storybook),
`packages/tokens/README.md`

## Contents

- [What design tokens are](#what-design-tokens-are)
- [Token naming structure](#token-naming-structure)
- [Color palette (primitives)](#color-palette-primitives)
- [Token customization](#token-customization)
- [Proposing a new token](#proposing-a-new-token)
- [Inclusion](#inclusion)
- [Token categories](#token-categories)
- [Spacing guidelines](#spacing-guidelines)
- [Border radius guidelines](#border-radius-guidelines)
- [Elevation surface — semantic usage](#elevation-surface--semantic-usage)
- [Typography guidelines](#typography-guidelines)
- [Tailwind integration](#tailwind-integration)

## What design tokens are

Design tokens are standardized name-value pairs that encode design decisions (colors, typography,
spacing, motion). They are the bridge between design and development and ensure
consistency across platforms and tools.

## Token naming structure

Semantic color tokens follow the 4-part structure:

```
[type]-[category]-[instance]-[variant]
```

| Part | Description | Examples |
|---|---|---|
| **Type** | Broadest classification | `color`, `font`, `scale`, `border-radius` |
| **Category** | Functional group within the type | `icon`, `text`, `background`, `elevation` |
| **Instance** | Concrete usage | `primary`, `positive`, `critical` |
| **Variant** | State or modification | `default`, `hover`, `pressed`, `disabled` |

Examples:
- `--color-text-primary-default` → color / text / primary / default state
- `--color-interaction-primary-hover` → color / interaction / primary / hover state
- `--color-icon-critical-default` → color / icon / critical / default

Simpler tokens such as `--font-size-s` or `--scale-size-8` have fewer parts because they carry no state.

## Color palette (primitives)

Palette values carry no semantic meaning. They are the toolbox for semantic tokens and themes.
**In product code always use tokens instead of primitive palette values.** Palette values bypass
the abstraction layer and break theming.

Every palette hue has a numeric shade (50 = lightest through 950 = darkest):
- `--color-blue-50` = nearly white; `--color-blue-950` = nearly black
- Higher number = always darker, independent of the hue

## Token customization

**Recommendation**: do NOT override existing Meteor tokens. Overrides can lead to unexpected
visual divergence and break when token values change in future releases.

**Instead**: define your own tokens with your own prefix:

```css
@import "@shopware-ag/meteor-tokens/administration/light.css";
@import "@shopware-ag/meteor-tokens/administration/dark.css";

/* Own tokens with a custom prefix */
:root {
  --myapp-color-brand-default: #7c3aed;
  --myapp-color-brand-hover: #6d28d9;
}

[data-theme="dark"] {
  --myapp-color-brand-default: #8b5cf6;
  --myapp-color-brand-hover: #7c3aed;
}
```

## Proposing a new token

New tokens require approval from design and engineering. Process:

1. **Initiation**: design or engineering identify a gap (GitHub issue, Figma comment, Meteor Slack)
2. **Proposal content**:
   - What the token represents and where it is used
   - Proposed name following the `type-category-instance-variant` structure
   - Intended value in all available themes
   - Whether an existing token could cover the need
3. **Review**: design team + Meteor engineering check name, necessity, theme compatibility
4. **Figma → code**: token first into the Figma Variables Library, then into the package via the sync workflow

## Inclusion

```css
/* Primitive color palette (pure colors, not semantic) */
@import '@shopware-ag/meteor-tokens/deliverables/foundation/primitives.css';

/* Semantic admin tokens — light theme */
@import '@shopware-ag/meteor-tokens/deliverables/administration/light.css';

/* Semantic admin tokens — dark theme */
@import '@shopware-ag/meteor-tokens/deliverables/administration/dark.css';
```

The light theme applies to `:root`, the dark theme to `[data-theme='dark']`.

## Token categories

### Color primitives (`foundation/primitives.css`)

Base color palettes as CSS custom properties, not to be used directly (they are referenced by semantic tokens):

| Palette | Steps | Example |
|---|---|---|
| `--color-slate-*` | 50–950 | `--color-slate-900: #2b2e3a` |
| `--color-blue-*` | 50–900 | `--color-blue-500: #189eff` |
| `--color-yellow-*` | 50–900 | |
| `--color-pumpkin-*` | 50–900 | |
| `--color-pink-*` | 50–900 | |
| `--color-purple-*` | 50–900 | |
| `--color-emerald-*` | 50–900 | |
| `--color-zinc-*` | 0–950 | `--color-zinc-0: #ffffff` |
| `--color-scale-size-*` | 0–640 (in 4px steps) | `--scale-size-16: 1rem` |

### Interaction (`--color-interaction-*`)

For interactive elements (buttons etc.):

```css
--color-interaction-primary-default    /* Primary button background */
--color-interaction-primary-hover
--color-interaction-primary-pressed
--color-interaction-primary-disabled
--color-interaction-secondary-default  /* Secondary button */
--color-interaction-secondary-hover
--color-interaction-secondary-pressed
--color-interaction-secondary-disabled
--color-interaction-secondary-dark
--color-interaction-critical-default   /* Critical action */
--color-interaction-critical-hover
--color-interaction-critical-pressed
--color-interaction-critical-disabled
```

### Elevation / surfaces (`--color-elevation-*`)

For backgrounds of cards, modals, overlays:

```css
--color-elevation-surface-sunken      /* Sunken areas */
--color-elevation-surface-default     /* Default surface */
--color-elevation-surface-selected    /* Selected state */
--color-elevation-surface-hover       /* Hover state */
--color-elevation-surface-raised      /* Raised elements */
--color-elevation-surface-overlay     /* Overlay background */
--color-elevation-surface-frame       /* Frame background */
--color-elevation-surface-backdrop    /* Modal backdrop */
--color-elevation-surface-floating    /* Floating UI (tooltips, dropdowns) */
--color-elevation-backdrop-default    /* Backdrop color with opacity */
--color-elevation-floating-default    /* Floating elements */
--color-elevation-shadow-default      /* Box shadow */
```

### Background colors (`--color-background-*`)

For semantic backgrounds:

```css
--color-background-primary-default
--color-background-primary-disabled
--color-background-secondary-default
--color-background-tertiary-default
--color-background-brand-default     /* Brand blue background */
--color-background-critical-default  /* Red background */
--color-background-critical-dark
--color-background-attention-default /* Yellow/orange background */
--color-background-positive-default  /* Green background */
--color-background-accent-default    /* Purple background */
```

### Icon colors (`--color-icon-*`)

```css
--color-icon-primary-default         /* Default icons */
--color-icon-primary-disabled
--color-icon-primary-inverse
--color-icon-secondary-default       /* Secondary icons */
--color-icon-brand-default           /* Brand icons */
--color-icon-critical-default        /* Error icons */
--color-icon-attention-default       /* Warning icons */
--color-icon-positive-default        /* Success icons */
--color-icon-accent-default          /* Accent icons */
--color-icon-static-default          /* Always white */
--color-icon-static-dark             /* Always black */
```

### Border colors (`--color-border-*`)

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

### Text colors (`--color-text-*`)

```css
--color-text-primary-default         /* Main text */
--color-text-primary-disabled
--color-text-primary-inverse         /* Text on a dark background */
--color-text-secondary-default       /* Secondary text */
--color-text-secondary-disabled
--color-text-brand-default           /* Brand colored text */
--color-text-brand-hover
--color-text-brand-pressed
--color-text-brand-disabled
--color-text-brand-inverse
--color-text-critical-default        /* Error text */
--color-text-critical-hover
--color-text-attention-default       /* Warning text */
--color-text-positive-default        /* Success text */
--color-text-accent-default          /* Accent text */
--color-text-static-default          /* Always white */
--color-text-static-dark             /* Always black */
--color-text-inverse-default
--color-static-white: #ffffff
--color-static-black: #09090b
```

### Typography

```css
--font-family-headings: 'Inter'
--font-family-body: 'Inter'

/* Font sizes */
--font-size-2xs: 0.75rem    /* 12px */
--font-size-xs: 0.875rem    /* 14px */
--font-size-s: 1rem          /* 16px */
--font-size-m: 1.125rem     /* 18px */
--font-size-l: 1.25rem      /* 20px */
--font-size-xl: 1.5rem      /* 24px */
--font-size-2xl: 1.75rem    /* 28px */
--font-size-3xl: 2rem        /* 32px */

/* Font weights */
--font-weight-regular: 400
--font-weight-medium: 500
--font-weight-semibold: 600
--font-weight-bold: 700

/* Line heights */
--font-line-height-2xs: 1.125rem
--font-line-height-xs: 1.375rem
--font-line-height-s: 1.625rem
--font-line-height-m: 1.75rem
--font-line-height-l: 1.875rem
--font-line-height-xl: 2rem
--font-line-height-2xl: 2.25rem
--font-line-height-3xl: 2.5rem
```

### Border radius

```css
--border-radius-card: 0.5rem      /* 8px — cards */
--border-radius-overlay: 0.25rem  /* 4px — modals, dropdowns */
--border-radius-button: 0.25rem   /* 4px — buttons */
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
--border-radius-round: 624.9375rem  /* Fully round */
```

### Scale sizes (`--scale-size-*`)

Spacing and sizes in 4px steps (base 0.25rem = 4px):

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
/* ... up to --scale-size-640 */
```

## Spacing guidelines

The spacing scale is numeric: `--scale-size-8` = 8px. No semantic intermediate layer.

Recommendations:
- **4–8px**: tight internal spacing (icon-to-label gap, badge padding)
- **12–16px**: default component padding and item spacing
- **24–40px**: between form elements, sections within a view
- **48–64px**: between main layout regions

Negation: `calc(var(--scale-size-8) * -1)` instead of `-8px`.

Do **not** use `--scale-size-*` for `border-radius` — that is its own token type.

## Border radius guidelines

Order of preference:
1. **Element-specific tokens** (where available): `--border-radius-card`, `--border-radius-button`, `--border-radius-checkbox`
2. **Semantic tokens** as a fallback: `--border-radius-xs` through `--border-radius-round`
3. **Never**: arbitrary px values or `50%`

For pills/avatar circles/fully rounded tags: `--border-radius-round`.

## Elevation surface — semantic usage

| Token | Usage |
|---|---|
| `--color-elevation-surface-sunken` | Sidebar sections, zebra table rows, code blocks, large page backgrounds (when default is used for the main area) |
| `--color-elevation-surface-default` | Main application background / page |
| `--color-elevation-surface-raised` | Cards, panels, containers above the background |
| `--color-elevation-floating-default` | Tooltips — need high contrast against the page |
| `--color-elevation-backdrop-default` | Semi-transparent scrim behind modals/drawers |
| `--color-elevation-shadow-default` | Box shadow color for raised elements such as popovers |

Token values switch automatically under `data-theme="dark"`.

## Typography guidelines

Always combine `--font-size-*` with a matching `--font-line-height-*`.

Hierarchy recommendation:
- `3xl`, `2xl`: page titles, main section headers
- `xl`, `l`: sub-sections
- `m`, `s`: card and section headings
- `xs`: body text, support labels, metadata

Secondary information: `--color-text-secondary-default` instead of a smaller font size.
Body text line length: `max-width: 65ch` for optimal readability.

## Tailwind integration

```css
/* Default */
@import '@shopware-ag/meteor-tokens/deliverables/tailwind.css';

/* Administration specific */
@import '@shopware-ag/meteor-tokens/deliverables/tailwind-administration.css';
```

The Tailwind files map the CSS custom properties onto Tailwind utility classes.
