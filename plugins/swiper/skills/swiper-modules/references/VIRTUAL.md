# Swiper — Virtual Slides module

Keep only the slides needed in the visible area in the DOM — ideal for hundreds of slides.

```js
import Swiper from 'swiper';
import { Virtual } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Virtual],
  virtual: {
    slides: Array.from({ length: 500 }, (_, i) => `Slide ${i + 1}`),
    cache: true,
    addSlidesBefore: 2,
    addSlidesAfter: 2,
    renderSlide: (slide, index) => `<div class="swiper-slide">${slide}</div>`,
  },
});
```

**Note:** Not compatible with the Grid module and `slidesPerView: 'auto'`.

## Deep dive
- [VIRTUAL-DETAIL.md](VIRTUAL-DETAIL.md) — all parameters, properties, methods, React/Vue integration
