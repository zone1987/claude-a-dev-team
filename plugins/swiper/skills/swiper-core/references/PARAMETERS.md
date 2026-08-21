# Swiper — Parameter reference

All configuration options for `new Swiper(el, options)`.

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

## Further reading
- [PARAMETERS-DETAIL.md](PARAMETERS-DETAIL.md) — complete tables of all parameters with type, default and description (Core, Navigation, Pagination, Scrollbar, Autoplay, FreeMode, Grid, all effects, Thumbs, Zoom, Keyboard, Mousewheel, Virtual)
