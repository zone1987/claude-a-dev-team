---
name: swiper-thumbs
description: >
  Vollständige Referenz des Swiper Thumbs-Moduls: swiper-Instanz verknüpfen,
  multipleActiveThumbs, autoScrollOffset, slideThumbActiveClass, thumbsContainerClass,
  Methoden init/update — Thumbnail-Galerie-Navigation.
  Trigger: "swiper thumbs", "swiper thumbnail navigation", "swiper thumbs module",
  "swiper gallery thumbs", "swiper thumbs swiper", "swiper multipleActiveThumbs",
  "swiper thumbnail gallery", "swiper thumbs parameters", "swiper slideThumbActiveClass".
---

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
- [references/deep/thumbs.md](references/deep/thumbs.md) — alle Parameter, Properties, Methoden
