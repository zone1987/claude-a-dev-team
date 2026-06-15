---
name: shadcn-vue-tailwind-v4
description: >
  shadcn-vue mit Tailwind CSS v4: Neuigkeiten (@theme inline, oklch, data-slot,
  new-york Style, Sonner statt Toast), Upgrade-Anleitung (Tailwind Upgrade Guide,
  CSS-Variablen migrieren, @theme inline, size-* Utility, Abhaengigkeiten updaten).
  Triggers: "shadcn vue tailwind v4", "tailwind v4 shadcn", "@theme inline shadcn",
  "oklch shadcn vue", "shadcn vue upgrade tailwind", "tailwind v4 setup shadcn",
  "shadcn vue new-york", "tw-animate-css", "reka ui v2 shadcn", "shadcn vue v4",
  "upgrade shadcn tailwind v4", "@tailwindcss/upgrade"
---

# shadcn-vue: Tailwind v4

Tailwind v4 wird vollstaendig unterstuetzt. Neue Projekte starten automatisch mit v4.
Bestehende v3-Projekte funktionieren weiterhin ohne Aenderungen.

## Wichtigste Neuerungen

- CLI initialisiert Projekte mit Tailwind v4
- Vollstaendige Unterstuetzung fuer `@theme` und `@theme inline`
- Alle Komponenten aktualisiert fuer Tailwind v4
- Jedes Primitive hat ein `data-slot`-Attribut (fuer CSS-Targeting)
- `toast`-Komponente deprecated zugunsten `sonner`
- Buttons verwenden Standard-Cursor (kein `cursor-pointer` mehr per Default)
- `default`-Style deprecated, neue Projekte verwenden `new-york`
- HSL-Farben konvertiert zu OKLCH

Demo: https://v4.shadcn-vue.com

## Reference Files

- `references/tailwind-v4.md` — Vollstaendige What's New-Liste, Framework-Links,
  Upgrade-Schritt-fuer-Schritt: Tailwind Upgrade Guide + Codemod, CSS-Variablen
  von HSL zu OKLCH migrieren mit @theme inline, size-* Utility verwenden,
  Abhaengigkeiten updaten (tw-animate-css, reka-ui, @lucide/vue, tailwind-merge, clsx)
