# Swiper — Event-Referenz

Events werden per `swiper.on(event, handler)` oder im Konstruktor via `on: { ... }` registriert.

```js
const swiper = new Swiper('.swiper', {
  on: {
    init(s) { console.log('bereit, activeIndex:', s.activeIndex); },
    slideChange(s) { console.log('zu Folie', s.activeIndex); },
    reachEnd(s) { console.log('Ende erreicht'); },
  }
});

// Nachträglich:
swiper.on('touchStart', (s, event) => { /* ... */ });
swiper.once('transitionEnd', (s) => { /* einmalig */ });
swiper.onAny((eventName, ...args) => { /* alle Events */ });
```

## Vertiefung
- [EVENTS-DETAIL.md](EVENTS-DETAIL.md) — vollständige Tabelle aller Events (Core, Navigation, Pagination, Scrollbar, Autoplay, Keyboard, Mousewheel, Zoom) mit Argumenten und Beschreibungen
