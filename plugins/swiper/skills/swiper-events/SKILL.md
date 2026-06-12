---
name: swiper-events
description: >
  Alle Swiper-Events: init, slideChange, transitionStart/End, touchStart/Move/End,
  reachBeginning, reachEnd, progress, autoplay, pagination, navigation, zoom und mehr.
  Trigger: "swiper events", "swiper event listener", "swiper on", "swiper slideChange",
  "swiper transitionEnd", "swiper touchStart", "swiper reachEnd", "swiper callbacks",
  "swiper event handling", "swiper all events", "swiper event reference".
---

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
- [references/deep/events.md](references/deep/events.md) — vollständige Tabelle aller Events (Core, Navigation, Pagination, Scrollbar, Autoplay, Keyboard, Mousewheel, Zoom) mit Argumenten und Beschreibungen
