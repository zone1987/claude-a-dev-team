# Swiper — Mousewheel-Modul

Mausrad-/Trackpad-Steuerung für Swiper mit konfigurierbarer Sensitivität.

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

## Vertiefung
- [MOUSEWHEEL-DETAIL.md](MOUSEWHEEL-DETAIL.md) — alle Parameter, Methoden, Events, noMousewheelClass-Verwendung
