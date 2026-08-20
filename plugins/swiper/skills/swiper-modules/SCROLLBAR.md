# Swiper — Scrollbar module

Scrollbar with optional drag for Swiper navigation.

```js
import Swiper from 'swiper';
import { Scrollbar } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Scrollbar],
  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true,
    snapOnRelease: true,
  },
});
```

## Deep dive
- [SCROLLBAR-DETAIL.md](SCROLLBAR-DETAIL.md) — all parameters, CSS variables, events, methods, properties
