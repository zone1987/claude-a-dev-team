# Swiper — Mousewheel module

Mouse wheel / trackpad control for Swiper with configurable sensitivity.

```js
import Swiper from 'swiper';
import { Mousewheel } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Mousewheel],
  mousewheel: {
    enabled: true,
    invert: false,
    releaseOnEdges: true,
    sensitivity: 1,
  },
});
```

## Further reading
- [MOUSEWHEEL-DETAIL.md](MOUSEWHEEL-DETAIL.md) — all parameters, methods, events, using noMousewheelClass
