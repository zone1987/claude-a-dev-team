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
- [PARAMETERS-DETAIL.md](PARAMETERS-DETAIL.md) — vollständige Tabellen aller Parameter mit Typ, Default und Beschreibung (Core, Navigation, Pagination, Scrollbar, Autoplay, FreeMode, Grid, alle Effekte, Thumbs, Zoom, Keyboard, Mousewheel, Virtual)
