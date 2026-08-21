# Swiper — Pagination module

Bullet, fraction, progressbar or custom pagination.

```js
import Swiper from 'swiper';
import { Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
    dynamicBullets: true,
  },
});
```

## Deep dive
- [PAGINATION-DETAIL.md](PAGINATION-DETAIL.md) — all parameters with type/default/description, all render function signatures, CSS variables, events, methods
