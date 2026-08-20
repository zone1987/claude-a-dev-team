# Swiper — Instanz-Methoden

Alle Methoden werden auf der Swiper-Instanz aufgerufen.

```js
const swiper = new Swiper('.swiper', { ... });

swiper.slideNext();           // Nächste Folie
swiper.slidePrev();           // Vorherige Folie
swiper.slideTo(3, 500);       // Zu Index 3 in 500 ms
swiper.update();              // Nach DOM-Änderungen neu berechnen
swiper.destroy();             // Instanz zerstören

swiper.on('slideChange', (s) => console.log(s.activeIndex));
```

## Vertiefung
- [METHODS-DETAIL.md](METHODS-DETAIL.md) — vollständige Tabelle aller Methoden (Core, Navigation, Pagination, Scrollbar, Autoplay, Manipulation, Thumbs, Zoom, Keyboard, Mousewheel) mit Signaturen und Beschreibungen
