---
name: swiper-init
description: Scaffolds a Swiper integration — the variant (core/element/React/Vue), the HTML structure, CSS imports, module registration (navigation/pagination/autoplay/effects/…) and init code with the parameters you want.
argument-hint: <selector> [--variant core|element|react|vue] [--modules navigation,pagination,autoplay] [--effect slide|fade|coverflow|cards]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /swiper-init

Produce a ready-to-use Swiper integration. Skills: `swiper-core`, the module skills you need,
`swiper-frameworks`.

## Steps
1. Variant, selector, modules and effect from `$ARGUMENTS`.
2. **HTML** (`.swiper > .swiper-wrapper > .swiper-slide`; with the element, `<swiper-container>/<swiper-slide>`).
3. **CSS imports**: `swiper/css` plus one per module (`swiper/css/navigation`, `/pagination`, `/effect-fade` …).
4. **JS**: import and register the modules (`modules: [...]`), init with the parameters (slidesPerView,
   spaceBetween, loop, breakpoints, autoplay, pagination/navigation, effect options …) plus events where
   needed (`on: { slideChange }`).
5. Per variant: the core class, the Swiper element (`register()` plus attributes), or the React/Vue component.

Use documented parameters and modules only (source: `swiper-core` plus the module skills). Never omit the CSS
imports; from v9 on, register modules explicitly.
