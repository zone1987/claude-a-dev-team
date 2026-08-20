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

- `TAILWIND-V4-DETAIL.md` — Vollstaendige What's New-Liste, Framework-Links,
  Upgrade-Schritt-fuer-Schritt: Tailwind Upgrade Guide + Codemod, CSS-Variablen
  von HSL zu OKLCH migrieren mit @theme inline, size-* Utility verwenden,
  Abhaengigkeiten updaten (tw-animate-css, reka-ui, @lucide/vue, tailwind-merge, clsx)
