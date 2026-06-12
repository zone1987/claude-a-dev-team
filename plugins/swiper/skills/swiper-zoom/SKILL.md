---
name: swiper-zoom
description: >
  Vollständige Referenz des Swiper Zoom-Moduls: maxRatio, minRatio, toggle, limitToOriginalSize,
  panOnMouseMove, containerClass, Methoden zoom.in/out/toggle, Event zoomChange,
  data-swiper-zoom Attribut per Slide.
  Trigger: "swiper zoom", "swiper zoom module", "swiper zoom in out", "swiper pinch zoom",
  "swiper zoom maxRatio", "swiper zoom toggle", "swiper zoomChange", "swiper zoom parameters",
  "swiper zoom container", "swiper zoom events", "swiper panOnMouseMove".
---

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
- [references/deep/zoom.md](references/deep/zoom.md) — alle Parameter, Properties, Methoden, Events, HTML-Struktur
