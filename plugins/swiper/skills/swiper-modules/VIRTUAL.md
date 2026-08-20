# Swiper — Virtual Slides-Modul

Nur die im sichtbaren Bereich benötigten Slides im DOM halten — ideal für hunderte Slides.

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

**Hinweis:** Nicht kompatibel mit Grid-Modul und `slidesPerView: 'auto'`.

## Vertiefung
- [VIRTUAL-DETAIL.md](VIRTUAL-DETAIL.md) — alle Parameter, Properties, Methoden, React/Vue-Integration
