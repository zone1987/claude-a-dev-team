# Meteor design system — usage guidelines & best practices

Sources: `packages/component-library/src/docs/foundations/`,
`packages/component-library/LIFECYCLE.md`,
`packages/component-library/STORYBOOK_DOCS_STANDARD.md`

---

## Contents

- [1. Design principles](#1-design-principles)
- [2. Component lifecycle](#2-component-lifecycle)
- [3. Accessibility guidelines](#3-accessibility-guidelines)
- [4. Content & wording guidelines](#4-content-wording-guidelines)
- [5. Storybook docs standard](#5-storybook-docs-standard)
- [When to use](#when-to-use)
- [Examples](#examples)
- [Anatomy](#anatomy)
- [API reference](#api-reference)
- [Do](#do)
- [Don't](#dont)
- [Behavior notes](#behavior-notes)
- [Accessibility notes](#accessibility-notes)
- [Comparisons](#comparisons)
- [6. Token usage — do & don't](#6-token-usage-do-dont)
- [7. Key token reference overview](#7-key-token-reference-overview)

## 1. Design principles

From the official Meteor Storybook, page `Foundations/Design Principles`:

### Accessibility and inclusivity

Design experiences that are accessible to all users. Accessibility is not an afterthought — it shapes interaction patterns, colour contrast, keyboard behaviour and copy from the start. The basis is WCAG 2.1 AA.

### Data-informed decisions

Assumptions are validated with real usage data, usability sessions and feedback. New insights take precedence over earlier decisions.

### Sticky merchant and shopper experience

Merchants work under commercial pressure and need fast, safe decision paths. Design reduces the distance between a user's goal and reaching it.

### Reduce friction, aim for simplicity

Simplicity does not mean missing features, but the absence of unnecessary obstacles. Every form field, every label, every modal and every confirmation has a price.

### Consistent experiences

Consistency reduces the learning effort. When the same interaction pattern appears in different places, it only has to be learned once.

### Ethical design

No dark patterns, no deceptive defaults. Transparency about the data collected and about irreversible actions.

---

## 2. Component lifecycle

From `packages/component-library/LIFECYCLE.md`:

Every component is in one of three stages:

### Future (experimental)

- New ideas are being tested, feedback is being collected
- Breaking changes are possible without prior notice
- Do not use in production

### Stable (production ready)

Requirements for stable:
- Automated tests present
- Meteor design tokens used
- WCAG 2.1 AA level met
- Storybook stories present as documentation

Breaking changes are documented at least one patch version before a major release.

### Deprecated

- Usage is discouraged
- Where one exists, an upgrade guide is provided
- The component is removed in the next major version

---

## 3. Accessibility guidelines

From `packages/component-library/src/docs/foundations/accessibility.mdx`:

### What Meteor provides automatically

- **Keyboard navigation**: all interactive components are fully operable by keyboard
- **ARIA attributes**: components carry the matching roles, states and properties
- **Focus management**: in modals, dropdowns and overlays the focus is managed correctly
- **Colour contrast**: design tokens meet WCAG 2.1 AA for text and UI elements
- **Dark mode**: both themes keep accessible contrast ratios
- **Screen readers**: components are tested with common assistive technologies

### What you have to take care of yourself

**Keep it simple**
- Avoid complex flows where simpler alternatives exist
- Use consistent patterns across pages
- Concise, clear language — a reading level appropriate for the audience

**Be inclusive**
- Use inclusive language throughout
- Make no assumptions about users' abilities
- Avoid jargon, metaphors and non-literal phrases

**Provide text alternatives**
- Clear, concise labels and alt text for all meaningful images and icons
- Set the `decorative` prop on `mt-icon` for purely visual icons (they stay out of the accessibility tree)
- Transcripts or captions for video content

**Never rely on colour alone**
- Always combine colour with a secondary indicator (icon, label, pattern)
- Use semantic icon tokens (`critical`, `positive`, `attention`) to reinforce the meaning

**Semantic HTML**
- Landmark elements (`header`, `nav`, `main`, `footer`) for the page structure
- Do not use `div` and `span` as interactive elements
- Keep the heading hierarchy logical

**Give users control**
- Layouts adapt to every screen size (reflow)
- Respect `prefers-reduced-motion`
- Enough time for time-critical interactions

**Test broadly**
- Test keyboard-only navigation
- Test with screen readers (VoiceOver, NVDA or JAWS)
- Where possible, test with real users with disabilities

### Pre-ship checklist

- All interactive elements reachable and operable by keyboard alone
- No keyboard focus traps outside modals/overlays
- All images and meaningful icons have descriptive labels or alt text
- Colour is never the only indicator of state or meaning
- Text and UI elements meet WCAG 2.1 AA contrast ratios
- Heading levels follow a logical hierarchy without skips
- Form fields have visible labels via `for`/`id` or `aria-labelledby`
- Animations and transitions respect `prefers-reduced-motion`

### Recommended tools

- **[WAVE](https://wave.webaim.org/)**: visual feedback tool for an accessibility check
- **[Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/)**: built into Chrome DevTools, provides an accessibility score

---

## 4. Content & wording guidelines

From `packages/component-library/src/docs/foundations/content/wording.mdx`:

### Writing goals

- **Empower**: language that informs and encourages
- **Respect**: not condescending, inclusive and considerate
- **Educate**: exactly the information needed, no marketing speak
- **Engage**: relevant content, conversational tone

### How we write

- **Clear**: simple words and sentences
- **Useful**: always ask: what purpose does this serve? Who reads it? What do they need to know?
- **Friendly**: write like a human — all content should feel warm and human
- **Appropriate**: adjust the tone to the audience and the topic

### Active voice

Write in the active voice almost always. Active: the subject performs the action. Passive: the action is performed on the subject.

```
✓ Jennifer logged into the account
✗ The account was logged into by Jennifer
```

Use the passive only when: Shopware/I as the subject should be avoided; the action was not performed personally; the object matters more than the subject.

### Inclusive language

People-first language. Never focus on characteristics such as gender, sexual orientation, religion or abilities unless they are relevant.

| Topic | Right | Wrong |
|---|---|---|
| Technology | `allowlist`, `blocklist` | `whitelist`, `blacklist` |
| Technology | `main`, `primary` | `master` |
| Gender | `they` | `him/her`, `he/she` |
| Groups | `people`, `folks`, `teammates` | `guys` |
| Roles | neutral titles | `ninja`, `rockstar`, `wizard` |
| Resources | `workforce` | `manpower` |
| Relationships | `spouse`, `partner` | `wife/husband` |

### Abbreviations and acronyms

Spell them out on first occurrence, then use the short form. Use well-known abbreviations (API, HTML) directly.

### Capitalisation

Shopware feature names are always capitalised: Rule Builder, Sales Channel, Flow Builder, B2B Components.

### Buttons

- Keep button labels as short as possible
- A verb that describes the action: `Save`, `Delete`, `Continue to checkout`
- No article: `Save product`, not `Save the product`

### Addressing the user

In English: `you` and `your` for every audience.

In German: the informal address (Du). In the Shopware administration, Du, Dich, Dir and Dein are capitalised (as a sign of respect).

Example (German): *Speichere das Produkt, bevor Du die Seite verlässt.* ("Save the product before you leave the page.")

---

## 5. Storybook docs standard

From `packages/component-library/STORYBOOK_DOCS_STANDARD.md`:

### Page structure for component documentation

```mdx
<StorybookPageHeader
  title="Component name"
  tagName="mt-component-name"
  packageImports="MtComponentName"
  sourcePath="packages/component-library/src/components/group/mt-component-name"
>
  Short description
</StorybookPageHeader>

## When to use

## Examples

### Basic

Main example

### Another example

## Anatomy

## API reference

## Do

## Don't

## Behavior notes

## Accessibility notes

## Comparisons
```

### Rules

- `StorybookPageHeader` starts every page — it contains the H1
- Format: `Component name (mt-component-name)`
- `sourcePath`: repo-relative path to the component folder (for the GitHub link)
- Short description as children of `StorybookPageHeader` (MDX rich text)
- Default status: `Available`; `Experimental` or `Deprecated` when a stronger signal is needed
- `Examples` is mandatory
- `Anatomy`, `Behavior notes`, `Comparisons` are optional, only when they add real value

### Optional sections

- **Anatomy**: when structure, composition or internal parts have to be explained
- **Behavior notes**: when the behaviour is non-obvious, stateful or easy to misunderstand
- **Comparisons**: when users are likely to choose between this and another component

### Stories

- Every component has a `Default` story (the most common state)
- Further stories: human-readable, user-facing names, first letter capitalised: `Variants`, `Sizes`, `Inline edit`
- At least one `Canvas` example that shows the recommended usage
- Prefer static, copyable story code for documentation examples

### In prose

- Component names in **bold** and capitalised: **Button**, **Badge**, **Promo Badge**
- No `mt-*` tag names in running text, except when the tag name itself is being explained

### API reference

- Storybook API tables for props, slots and events wherever possible
- The table goes directly below `API reference`, without a sub-section
- A separate section for `exposed methods` only when the component actually exposes public methods

### Companion exports

When components have related parts without their own page (e.g. `mt-action-menu-item`, `mt-modal-root`), those are documented on the parent page. Explain: what each part does, when it is used, how the parts fit together, ordering/nesting requirements.

Important comparisons for Storybook:
- tooltip vs help text
- floating ui vs action menu
- select vs radio group
- checkbox vs radio group vs select

---

## 6. Token usage — do & don't

### Spacing

```css
/* ✓ Right */
a { margin: var(--scale-size-10); }
.grid { row-gap: var(--scale-size-8); }

/* ✗ Wrong */
a { margin: 10px; }
.grid { row-gap: 0.5rem; }
```

Negation: `calc(var(--scale-size-8) * -1)` instead of `-8px`.

### Border radius

```css
/* ✓ Right */
.card { border-radius: var(--border-radius-card); }
.badge { border-radius: var(--border-radius-round); }

/* ✗ Wrong */
.badge { border-radius: 999px; }
.badge { border-radius: 50%; }
```

Do **not** use `--scale-size-*` for `border-radius` — that bypasses the semantic layer.

### Elevation surfaces

```css
/* ✓ Right */
.page-bg { background: var(--color-elevation-surface-default); }
.card { background: var(--color-elevation-surface-raised); }
.sidebar { background: var(--color-elevation-surface-sunken); }

/* ✗ Wrong */
.page-bg { background: #f5f5f5; }
```

### Colours

```css
/* ✓ Right */
a { color: var(--color-text-primary-default); }
button { background-color: var(--color-interaction-primary-default); }
div { background-color: var(--color-elevation-surface-default); }

/* ✗ Wrong */
a { color: var(--gray-800); }         /* primitive token */
a { color: #1a1a1a; }                 /* hardcoded */
button { background-color: #189eff; } /* hardcoded */
```

### Typography

```css
/* ✓ Right */
a { font-size: var(--font-size-s); }
a { font-family: var(--font-family-body); }

/* ✗ Wrong */
a { font-size: 16px; }
a { font-family: Inter; }
```

### Token customization

Do NOT override existing Meteor tokens (it can lead to unexpected divergence and breaks on token renames).

Define your own tokens with your own prefix:

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

## 7. Key token reference overview

### Token naming structure

```
[type]-[category]-[instance]-[variant]
```

- **Type**: `color`, `font`, `scale`, `border-radius`
- **Category**: `icon`, `text`, `background`, `elevation` (within `color`)
- **Instance**: `primary`, `positive`, `critical`
- **Variant**: `default`, `hover`, `pressed`, `disabled`

### Spacing scale (--scale-size-*)

| Token | Value |
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

Guideline:
- **4–8px**: tight internal spacing (icon-to-label gap, badge padding)
- **12–16px**: standard component padding and item spacing
- **24–40px**: between form elements, sections within a view
- **48–64px**: between main layout regions

### Border radius tokens

**Element-specific tokens (prefer these):**
| Token | Value | Usage |
|---|---|---|
| `--border-radius-card` | 8px | cards and container surfaces |
| `--border-radius-button` | 4px | buttons and button-like controls |
| `--border-radius-checkbox` | 4px | checkboxes and similar input toggles |

**Semantic tokens (fallback):**
| Token | Value |
|---|---|
| `--border-radius-none` | 0px |
| `--border-radius-xs` | 4px |
| `--border-radius-s` | 6px |
| `--border-radius-m` | 8px |
| `--border-radius-l` | 12px |
| `--border-radius-round` | 9999px |

### Elevation surface tokens

| Token | Usage |
|---|---|
| `--color-elevation-surface-sunken` | inset areas: sidebar sections, table zebra stripes, code blocks |
| `--color-elevation-surface-default` | main page / application background |
| `--color-elevation-surface-raised` | cards, panels, containers above the background |
| `--color-elevation-floating-default` | tooltips and floating elements |
| `--color-elevation-backdrop-default` | semi-transparent scrim behind modals/drawers |
| `--color-elevation-shadow-default` | box-shadow colour for raised elements such as popovers |

### Typography tokens

```css
--font-family-headings: "Inter";
--font-family-body: "Inter";

/* Weights */
--font-weight-regular: 400;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

**Scale (name → usage):**
- `3xl`, `2xl`: page titles, main section headers
- `xl`, `l`: sub-sections
- `m`, `s`: card and section headings
- `xs`: body text, supporting labels, metadata

**Rule**: always combine `--font-size-*` with the matching `--font-line-height-*`.

Maximum line length for body text: `max-width: 65ch`

### Using mt-text

```html
<mt-text size="2xl" weight="semibold">Page title</mt-text>
<mt-text size="s">Body text</mt-text>
<mt-text size="xs" color="color-text-secondary-default">Supporting label</mt-text>
<mt-text size="s" as="span">Inline text</mt-text>
```

The `as` prop controls the HTML element (default: `p`).
