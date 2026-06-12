---
name: swiper-properties
description: >
  Alle Swiper-Instanz-Properties: activeIndex, realIndex, previousIndex, slides, translate,
  progress, isBeginning, isEnd, params, el, wrapperEl, snapGrid, slidesGrid und Modul-Properties.
  Trigger: "swiper properties", "swiper activeIndex", "swiper realIndex", "swiper isBeginning",
  "swiper isEnd", "swiper translate", "swiper progress", "swiper slides array",
  "swiper instance properties", "swiper property reference", "swiper state".
---

# Swiper — Instanz-Properties

Alle Properties sind read-only (sofern nicht anders angegeben) und direkt auf der Instanz verfügbar.

```js
const swiper = new Swiper('.swiper', { ... });

console.log(swiper.activeIndex);    // aktueller Index
console.log(swiper.realIndex);      // realer Index (loop-bereinigt)
console.log(swiper.isBeginning);    // true wenn erste Folie aktiv
console.log(swiper.isEnd);          // true wenn letzte Folie aktiv
console.log(swiper.progress);       // 0..1 Fortschritt des Wrappers
console.log(swiper.slides);         // Array aller Slide-HTMLElements
console.log(swiper.params);         // Aktive Konfiguration
```

## Vertiefung
- [references/deep/properties.md](references/deep/properties.md) — vollständige Tabelle aller Properties (Core, Navigation, Pagination, Scrollbar, Autoplay, Thumbs, Zoom, Keyboard, Mousewheel) mit Typ und Beschreibung
