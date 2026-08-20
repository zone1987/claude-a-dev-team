# Swiper — Free Mode module

Free scrolling without slide snapping, with configurable momentum physics.

```js
import Swiper from 'swiper';
import { FreeMode } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: {
    enabled: true,
    momentum: true,
    momentumRatio: 0.8,
    sticky: false,
  },
});
```

## Further reading
- [FREE-MODE-DETAIL.md](FREE-MODE-DETAIL.md) — all parameters with type/default/description
