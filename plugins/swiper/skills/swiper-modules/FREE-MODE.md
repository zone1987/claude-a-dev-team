# Swiper — Free Mode-Modul

Freies Scrollen ohne Slide-Snap, mit konfigurierbarer Momentum-Physik.

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

## Vertiefung
- [FREE-MODE-DETAIL.md](FREE-MODE-DETAIL.md) — alle Parameter mit Typ/Default/Beschreibung
