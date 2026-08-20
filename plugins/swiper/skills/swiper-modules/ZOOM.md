# Swiper — Zoom module

Pinch-to-zoom and programmatic zooming of individual slides.

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

// Programmatically
swiper.zoom.in(2);    // zoom to 2x
swiper.zoom.out();    // back to minRatio
swiper.zoom.toggle(event);
```

HTML structure:
```html
<div class="swiper-slide">
  <div class="swiper-zoom-container" data-swiper-zoom="5">
    <img src="image.jpg" />
  </div>
</div>
```

## Deep dive
- [ZOOM-DETAIL.md](ZOOM-DETAIL.md) — all parameters, properties, methods, events, HTML structure
