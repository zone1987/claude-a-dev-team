---
name: swiper-virtual
description: >
  Vollständige Referenz des Swiper Virtual Slides-Moduls: slides-Array, renderSlide,
  renderExternal, cache, addSlidesBefore/After — performantes DOM-Rendering großer Slide-Mengen.
  Trigger: "swiper virtual", "swiper virtual slides", "swiper virtual module",
  "swiper renderSlide", "swiper renderExternal", "swiper virtual cache",
  "swiper virtual addSlidesBefore", "swiper large slides performance",
  "swiper virtual slides array", "swiper virtual parameters".
---

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
- [references/deep/virtual.md](references/deep/virtual.md) — alle Parameter, Properties, Methoden, React/Vue-Integration
