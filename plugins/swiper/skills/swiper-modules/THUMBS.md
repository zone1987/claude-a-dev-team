# Swiper — Thumbs-Modul

Thumbnail-Swiper mit Haupt-Swiper synchronisieren.

```js
import Swiper from 'swiper';
import { Thumbs } from 'swiper/modules';

const thumbsSwiper = new Swiper('.swiper-thumbs', {
  spaceBetween: 10,
  slidesPerView: 4,
  watchSlidesProgress: true,
});

const mainSwiper = new Swiper('.swiper-main', {
  modules: [Thumbs],
  spaceBetween: 10,
  thumbs: {
    swiper: thumbsSwiper,
    multipleActiveThumbs: false,
    autoScrollOffset: 0,
  },
});
```

## Vertiefung
- [THUMBS-DETAIL.md](THUMBS-DETAIL.md) — alle Parameter, Properties, Methoden
