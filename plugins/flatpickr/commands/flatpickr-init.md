---
name: flatpickr-init
description: Scaffold einer flatpickr-Einbindung — npm/CDN-Setup inkl. CSS, Init-Code mit gewünschten Optionen (Range/Zeit/inline/Locale), Events/Hooks und optional einem offiziellen Plugin.
argument-hint: <selector> [--mode single|multiple|range|time] [--locale de] [--framework vanilla|react|vue]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /flatpickr-init

Erzeuge eine einsatzfertige flatpickr-Einbindung. Skills: `flatpickr-getting-started`, `flatpickr-options`,
`flatpickr-events`, `flatpickr-localization`, `flatpickr-plugins`.

## Ablauf
1. Selector + Modus (single/multiple/range/time) + Locale + Framework aus `$ARGUMENTS`.
2. Einbindung erzeugen: CSS-Import (`flatpickr/dist/flatpickr.css` + ggf. Theme), JS-Import bzw. CDN-Tags.
3. Init-Code mit den passenden Optionen (z.B. `mode`, `enableTime`, `dateFormat`/`altInput`+`altFormat`,
   `minDate`/`maxDate`, `locale`) + relevante Hooks (`onChange`/`onReady`).
4. Bei Bedarf ein offizielles Plugin einbinden (z.B. `rangePlugin`, `confirmDatePlugin`, `monthSelectPlugin`).
5. Framework-Variante: Vanilla, `react-flatpickr` oder Vue-Wrapper.

Nur dokumentierte Optionen/Tokens (Quelle: `flatpickr-options`/`-formatting`). CSS/Locale-Import nicht vergessen.
