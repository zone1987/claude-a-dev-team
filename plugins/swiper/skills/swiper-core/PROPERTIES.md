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
- [PROPERTIES-DETAIL.md](PROPERTIES-DETAIL.md) — vollständige Tabelle aller Properties (Core, Navigation, Pagination, Scrollbar, Autoplay, Thumbs, Zoom, Keyboard, Mousewheel) mit Typ und Beschreibung
