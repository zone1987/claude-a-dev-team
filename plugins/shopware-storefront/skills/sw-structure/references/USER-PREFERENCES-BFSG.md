# Shopware Storefront — user preference media features and BFSG

German shops fall under the **BFSG** (Barrierefreiheitsstärkungsgesetz), in force since **28 June
2025**, which requires **EN 301 549** and with it **WCAG 2.1 AA**. Several of those criteria are met
by honouring what the visitor has already configured in their operating system — the `prefers-*`
media features are how a page reads that.

This matters most in a theme, because a theme is where animation, colour and contrast are decided.

## Contents

- [The seven features](#the-seven-features)
- [prefers-reduced-motion](#prefers-reduced-motion)
- [What Shopware already handles](#what-shopware-already-handles)
- [What Shopware does not handle](#what-shopware-does-not-handle)
- [Applying it in a theme](#applying-it-in-a-theme)
- [Detecting it in JavaScript](#detecting-it-in-javascript)
- [prefers-contrast and forced-colors](#prefers-contrast-and-forced-colors)
- [prefers-color-scheme](#prefers-color-scheme)
- [The other three](#the-other-three)
- [The WCAG criteria these serve](#the-wcag-criteria-these-serve)
- [Testing](#testing)

## The seven features

| Feature | Values | Meaning |
|---|---|---|
| `prefers-reduced-motion` | `no-preference` \| `reduce` | the visitor wants less motion |
| `prefers-contrast` | `no-preference` \| `more` \| `less` | more or less contrast between adjacent colours |
| `prefers-color-scheme` | `light` \| `dark` | a light or dark palette |
| `prefers-reduced-transparency` | `no-preference` \| `reduce` | fewer translucent layers |
| `prefers-reduced-data` | `no-preference` \| `reduce` | less network traffic |
| `forced-colors` | `none` \| `active` | the user agent overrides the palette, e.g. Windows High Contrast |
| `inverted-colors` | `none` \| `inverted` | the OS is inverting colours |

All are Media Queries Level 5. `prefers-reduced-motion` has been available across browsers since
January 2020 and is the one with both the widest support and the clearest legal relevance.

## prefers-reduced-motion

Written either way — the shorthand means `reduce`:

```css
@media (prefers-reduced-motion: reduce) { }
@media (prefers-reduced-motion) { }          /* identical */
```

The recommended approach is **not** to switch animation off wholesale, but to replace motion with a
calmer equivalent. A visitor with a vestibular disorder is harmed by movement across the screen —
scaling, panning, parallax — not by a fade:

```css
.my-teaser {
    animation: slide-in 400ms ease-out;
}

@media (prefers-reduced-motion: reduce) {
    .my-teaser {
        animation: fade-in 200ms linear;   /* opacity, not movement */
    }
}
```

Put the reduced rule **after** the default so it wins at equal specificity.

## What Shopware already handles

**Bootstrap does, Shopware relies on it.** `$enable-reduced-motion: true` (the default) makes
Bootstrap's `transition()` mixin wrap every transition in a `prefers-reduced-motion` guard, and
`_reboot.scss`, `_spinners.scss` and `_progress.scss` carry their own guards.

So anything using a Bootstrap component's transition — modal, off-canvas, collapse, dropdown,
carousel, spinner, progress bar — already respects the preference. Do not switch
`$enable-reduced-motion` off.

## What Shopware does not handle

Shopware's **own** stylesheets contain **7 `@keyframes`, 8 `animation:` declarations and 15
`transition:` declarations**, and **none of them is inside a `prefers-reduced-motion` query**.
Neither is any JavaScript: there is no `matchMedia` call anywhere in the Storefront sources.

Affected files include `component/_loader.scss`, `component/_base-slider.scss`,
`component/_ar-overlay.scss`, `layout/_scroll-up.scss`, `layout/_offcanvas-cart.scss`,
`layout/_navigation-offcanvas.scss` and `component/_cms-element.scss`.

The sliders are the sharper problem. `base-slider.plugin.js` supports **autoplay**, which moves
content without any user action — WCAG 2.2.2 requires that such motion can be paused, stopped or
hidden, and a visitor asking for reduced motion has effectively asked for exactly that.

**Treat this as a gap you close in your theme**, not as something the platform will do for you.

## Applying it in a theme

A single defensive rule in the theme's SCSS, placed after the Storefront import:

```scss
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
```

`0.01ms` rather than `none` is deliberate: an animation that never runs never fires its
`animationend` event, and JavaScript waiting for that event stalls. A near-zero duration keeps the
event and removes the motion.

`scroll-behavior: auto` cancels smooth scrolling, which is itself motion.

Then handle the cases the blanket rule cannot: disable slider autoplay, and replace any deliberate
movement of your own with a fade.

## Detecting it in JavaScript

```javascript
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

if (reduceMotion.matches) {
    this._disableAutoplay();
}

// The preference can change while the page is open.
reduceMotion.addEventListener('change', (event) => {
    event.matches ? this._disableAutoplay() : this._enableAutoplay();
});
```

In a Storefront plugin, read it in `init()` and subscribe for changes. For a slider, pass
`autoplay: false` into the settings rather than starting and stopping it — starting autoplay at all
is the thing to avoid.

## prefers-contrast and forced-colors

```css
@media (prefers-contrast: more) {
    .btn-primary { border: 2px solid currentColor; }
}

@media (forced-colors: active) {
    .my-component {
        forced-color-adjust: none;      /* only where the override breaks meaning */
        border: 1px solid CanvasText;   /* system colour keywords */
    }
}
```

`forced-colors: active` (Windows High Contrast and equivalents) replaces the palette entirely.
Two failures follow, and both are common in a Shopware theme:

- **Meaning carried only by colour disappears.** A stock indicator that is only green or red, a
  selected filter marked only by a background colour — add a shape, an icon or text.
- **Backgrounds on images vanish.** An icon drawn as a CSS background is removed; use an `<img>`,
  an inline SVG or `sw_icon`, which the Storefront renders as inline SVG and which survives.

Use system colour keywords (`CanvasText`, `Canvas`, `LinkText`, `ButtonText`) inside a
`forced-colors` block rather than fixed values.

## prefers-color-scheme

Shopware's default theme ships **no dark mode**, and Bootstrap 5.3's colour modes are not wired up
in the Storefront. A dark theme is therefore entirely your own work.

Note the interaction: `prefers-color-scheme` is a *preference*, not an accessibility requirement,
while `prefers-contrast` and `forced-colors` are. Shipping dark mode does not satisfy BFSG; meeting
the contrast ratios does.

If you build one, define the palette as CSS custom properties so both schemes share one set of
tokens:

```scss
:root { --my-surface: #{$white}; --my-text: #{$gray-900}; }

@media (prefers-color-scheme: dark) {
    :root { --my-surface: #{$gray-900}; --my-text: #{$white}; }
}
```

## The other three

- **`prefers-reduced-transparency: reduce`** — replace translucent overlays with opaque ones. The
  off-canvas backdrop and the cookie bar are the candidates in a Shopware theme.
- **`prefers-reduced-data: reduce`** — serve smaller images and skip decorative media. Pairs with
  `sw_thumbnails`, which already emits a `srcset`.
- **`inverted-colors: inverted`** — the OS inverts everything; images and logos end up negative.
  Rarely handled, and worth knowing mainly so an odd screenshot can be explained.

## The WCAG criteria these serve

| Criterion | Level | What it requires | Feature |
|---|---|---|---|
| 2.2.2 Pause, Stop, Hide | A | motion lasting over 5 s can be paused | `prefers-reduced-motion`, slider autoplay |
| 2.3.1 Three Flashes | A | nothing flashes more than three times per second | animation review |
| 2.3.3 Animation from Interactions | AAA | motion from interaction can be disabled | `prefers-reduced-motion` |
| 1.4.3 Contrast (Minimum) | AA | 4.5:1 for text, 3:1 for large text | palette, `prefers-contrast` |
| 1.4.11 Non-text Contrast | AA | 3:1 for controls and meaningful graphics | palette, `forced-colors` |
| 1.4.1 Use of Colour | A | colour is never the only carrier of meaning | `forced-colors` |

2.2.2 is the one an autoplaying slider fails at level A — the lowest level, and therefore
unambiguously required.

## Testing

- **macOS** — System Settings → Accessibility → Display → Reduce motion, Increase contrast.
- **Windows** — Settings → Accessibility → Visual effects → Animation effects; High Contrast for
  `forced-colors`.
- **Chrome DevTools** — Rendering panel → "Emulate CSS media feature", which covers
  `prefers-reduced-motion`, `prefers-contrast`, `prefers-color-scheme` and `forced-colors`.
- **Firefox** — `ui.prefersReducedMotion` in `about:config`.

Test the storefront's own moving parts specifically: product and gallery sliders, the off-canvas
transitions, the loading spinner, the scroll-up button and any parallax in a CMS block.

## Source

[MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
and [MDN: @media](https://developer.mozilla.org/en-US/docs/Web/CSS/@media), retrieved 2026-08-26.
Shopware coverage measured against the Storefront sources at v6.7.13.1 and the vendored Bootstrap
5.3.8. Accessibility guidance for Shopware extensions: call the Skill tool with "sw-features".
