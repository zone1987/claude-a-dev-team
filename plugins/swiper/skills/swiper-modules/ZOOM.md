# Swiper — Zoom-Modul

Pinch-to-Zoom und programmatisches Zoomen einzelner Slides.

```js
import Swiper from 'swiper';
import { Zoom } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Zoom],
  zoom: {
    maxRatio: 3,
    minRatio: 1,
    toggle: true,
  },
});

// Programmatisch
swiper.zoom.in(2);    // auf 2x zoomen
swiper.zoom.out();    // zurück auf minRatio
swiper.zoom.toggle(event);
```

HTML-Struktur:
```html
<div class="swiper-slide">
  <div class="swiper-zoom-container" data-swiper-zoom="5">
    <img src="image.jpg" />
  </div>
</div>
```

## Vertiefung
- [ZOOM-DETAIL.md](ZOOM-DETAIL.md) — alle Parameter, Properties, Methoden, Events, HTML-Struktur
