<!-- project rule, verified against shopware/storefront v6.7.13.1 (browserslist 'defaults', autoprefixer 10.4) and caniuse.com -->

# Shopware Storefront — which CSS features a theme may use

A shop serves whoever arrives, including older and locked-down browsers. A layout that depends on a
feature one of them lacks does not degrade — it breaks, and the visitor cannot buy anything. This
file records what is safe here, what is not, and how to decide the cases it does not name.

## Contents

- [The rule](#the-rule)
- [Not usable: :has()](#not-usable-has)
- [Not usable: container queries](#not-usable-container-queries)
- [How Shopware itself uses :has()](#how-shopware-itself-uses-has)
- [Checking a feature](#checking-a-feature)
- [What the build does and does not fix](#what-the-build-does-and-does-not-fix)
- [Safe alternatives](#safe-alternatives)
- [Progressive enhancement with @supports](#progressive-enhancement-with-supports)

## The rule

**Layout and function never depend on a feature that is not universally supported.** A feature may
be used to *improve* a page when its absence changes nothing the visitor needs.

Two features are ruled out for this project regardless of what a support table says:

| Feature | Status here |
|---|---|
| `:has()` | **not usable** for layout or function |
| Container queries (`@container`, `container-type`) | **not usable** |

Both are otherwise attractive, which is exactly why the rule is written down: the temptation is to
reach for them and discover the problem in production.

## Not usable: :has()

The parent selector. Tempting because it removes a class that JavaScript would otherwise toggle:

```scss
// Do not do this: the layout depends on :has()
.product-box:has(.badge-discount) {
    border: 2px solid $primary;
    padding-top: 2rem;
}
```

Instead, put the state in the markup where every browser can see it:

```twig
<div class="card product-box{% if product.calculatedPrice.listPrice %} has-discount{% endif %}">
```

```scss
.product-box.has-discount { border: 2px solid $primary; padding-top: 2rem; }
```

Twig already knows the condition — a template variable is more reliable than a selector, and it
costs nothing at runtime.

## Not usable: container queries

Sizing a component by its container rather than the viewport. The obvious use is a product card that
must look different in a sidebar than in a four-column grid:

```scss
// Do not do this
.cms-element-product-box { container-type: inline-size; }
@container (min-width: 300px) { .product-box-content { flex-direction: row; } }
```

Use what the Storefront already provides:

- **The Bootstrap grid.** A CMS block knows its column count from the block type, and the section
  knows whether it is the sidebar — `block.sectionPosition` is `sidebar` or `main`.
- **A modifier class from Twig.** The product card already receives `layout` and `displayMode`, and
  renders `box-{{ layout }}`. Extend that rather than measuring.
- **Media queries** on the Bootstrap breakpoints, through `media-breakpoint-up()`.

The card variants (`box-standard`, `box-image`, `box-minimal`, `box-wishlist`) exist precisely
because Shopware solved this with templates instead of container queries.

## How Shopware itself uses :has()

The Storefront contains exactly two occurrences, and both are instructive:

```scss
// page/product-detail/_review.scss — a focus ring on the star rating
.product-detail-review-form-star {
    &:has(.product-detail-review-form-radio:focus-visible) {
        box-shadow: $input-btn-focus-box-shadow;
    }
}

// layout/_header.scss — swap two buttons while the search suggest is open
&:has(.search-suggest) {
    .header-search-btn { display: none; }
    .header-close-btn  { display: block; }
}
```

Neither carries layout or function. Without `:has()` the focus ring is missing — the radio still has
its own focus style — and the header shows the search button instead of the close button. The page
still works.

**That is the boundary.** `:has()` for a visual refinement whose absence nobody has to notice is
acceptable; `:has()` deciding whether an element is visible, positioned or sized is not.

## Checking a feature

For anything not named above, check [caniuse.com](https://caniuse.com) before using it, and read
three things rather than the headline percentage:

1. **What fails without it.** A missing `gap` in a flex container collapses a layout; a missing
   `text-wrap: balance` changes a line break. The first is a defect, the second is not.
2. **Which browsers lack it**, not just how many. A feature missing in one older Safari matters more
   for a shop than the global number suggests, because iOS users cannot update Safari
   independently of the OS.
3. **Whether it degrades or breaks.** A property an old browser ignores is safe when the rule before
   it still produces a usable result. A selector that fails takes its whole block with it.

Shopware's own `browserslist` is `defaults`, which is Browserslist's broad baseline rather than a
narrow modern-browser target. That is the audience a theme inherits.

## What the build does and does not fix

The asset build runs **Autoprefixer 10.4** through PostCSS, so vendor prefixes are added
automatically — never write `-webkit-` or `-moz-` by hand.

Autoprefixer adds prefixes. It does **not** polyfill: `:has()`, `@container`, `subgrid` and
`:is()`-style selectors either exist in the browser or do not. `postcss-pxtorem` converts px to rem
and changes nothing about support.

So a green build says nothing about whether a feature works for a visitor.

## Safe alternatives

| Instead of | Use |
|---|---|
| `:has()` for state | a class set in Twig, or toggled by a Storefront plugin |
| `:has()` for a parent-child relationship | a modifier class on the parent |
| container queries | the Bootstrap grid, `block.sectionPosition`, a variant template |
| `@container` for a card in two contexts | separate card templates, as `box-*` already does |
| `subgrid` | nested `.row` / `.col-*`, or explicit grid areas |
| `text-wrap: balance` | acceptable as pure enhancement — it only changes line breaks |
| `aspect-ratio` | Bootstrap's `.ratio` helper |
| `gap` in flex | supported everywhere Bootstrap 5.3 targets; safe |

## Progressive enhancement with @supports

When a feature genuinely earns its place and degrades cleanly, gate it:

```scss
.my-component {
    display: flex;                 // the baseline every browser gets
    flex-wrap: wrap;
}

@supports (display: grid) {
    .my-component {
        display: grid;             // the improvement
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
}
```

Write the baseline first and the enhancement second, and verify the baseline alone is usable — by
disabling the `@supports` block, not by assuming.

`@supports selector(:has(a))` exists for selectors, but a selector-level enhancement usually means
the layout is already depending on it. Prefer a class from Twig.
