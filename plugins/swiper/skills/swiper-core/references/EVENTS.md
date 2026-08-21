# Swiper — Event reference

Register events with `swiper.on(event, handler)` or in the constructor via `on: { ... }`.

```js
const swiper = new Swiper('.swiper', {
  on: {
    init(s) { console.log('ready, activeIndex:', s.activeIndex); },
    slideChange(s) { console.log('to slide', s.activeIndex); },
    reachEnd(s) { console.log('end reached'); },
  }
});

// Later on:
swiper.on('touchStart', (s, event) => { /* ... */ });
swiper.once('transitionEnd', (s) => { /* only once */ });
swiper.onAny((eventName, ...args) => { /* all events */ });
```

## Further reading
- [EVENTS-DETAIL.md](EVENTS-DETAIL.md) — complete table of all events (core, Navigation, Pagination, Scrollbar, Autoplay, Keyboard, Mousewheel, Zoom) with arguments and descriptions
