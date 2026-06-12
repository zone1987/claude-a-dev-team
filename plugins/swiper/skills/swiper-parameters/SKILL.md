---
name: swiper-parameters
description: >
  Erschöpfende Referenz aller Swiper-Konfigurationsparameter: Core, Navigation, Pagination,
  Scrollbar, Autoplay, FreeMode, Grid, Effekte, Thumbs, Zoom, Keyboard, Mousewheel, Virtual.
  Trigger: "swiper parameter", "swiper optionen", "swiper konfiguration", "swiper config",
  "swiper breakpoints", "swiper loop", "swiper slidesPerView", "swiper spaceBetween",
  "swiper autoplay", "swiper navigation", "swiper pagination", "swiper effect",
  "swiper options reference", "swiper all parameters", "swiper settings".
---

# Swiper — Parameter-Referenz

Alle Konfigurationsoptionen für `new Swiper(el, options)`.

```js
import Swiper from 'swiper';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Navigation, Pagination, Autoplay],
  slidesPerView: 3,
  spaceBetween: 30,
  loop: true,
  autoplay: { delay: 2500, disableOnInteraction: false },
  navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
  pagination: { el: '.swiper-pagination', clickable: true },
});
```

## Vertiefung
- [references/deep/parameters.md](references/deep/parameters.md) — vollständige Tabellen aller Parameter mit Typ, Default und Beschreibung (Core, Navigation, Pagination, Scrollbar, Autoplay, FreeMode, Grid, alle Effekte, Thumbs, Zoom, Keyboard, Mousewheel, Virtual)
