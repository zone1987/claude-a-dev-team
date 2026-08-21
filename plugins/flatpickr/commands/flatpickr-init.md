---
name: flatpickr-init
description: Scaffolds a flatpickr integration — npm/CDN setup including the CSS, init code with the options you want (range/time/inline/locale), events and hooks, and optionally one official plugin.
argument-hint: <selector> [--mode single|multiple|range|time] [--locale de] [--framework vanilla|react|vue]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /flatpickr-init

Produce a ready-to-use flatpickr integration. Skills: `flatpickr-api`, `flatpickr-extend`.

## Steps
1. Selector, mode (single/multiple/range/time), locale and framework from `$ARGUMENTS`.
2. Build the integration: CSS import (`flatpickr/dist/flatpickr.css` plus a theme if wanted), JS import or CDN tags.
3. Init code with the fitting options (e.g. `mode`, `enableTime`, `dateFormat`/`altInput`+`altFormat`,
   `minDate`/`maxDate`, `locale`) plus the relevant hooks (`onChange`/`onReady`).
4. Where asked for, wire in one official plugin (e.g. `rangePlugin`, `confirmDatePlugin`, `monthSelectPlugin`).
5. Framework variant: vanilla, `react-flatpickr` or the Vue wrapper.

Use documented options and tokens only (source: `flatpickr-api`). Do not omit the CSS or locale import.
