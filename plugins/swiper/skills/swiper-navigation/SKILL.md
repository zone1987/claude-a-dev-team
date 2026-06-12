---
name: swiper-navigation
description: >
  Vollständige Referenz des Swiper Navigation-Moduls: nextEl/prevEl, disabledClass, hiddenClass,
  lockClass, addIcons, hideOnClick, CSS-Variablen, Events, Methoden.
  Trigger: "swiper navigation", "swiper next prev button", "swiper navigationNext",
  "swiper navigation module", "swiper arrow buttons", "swiper nextEl prevEl",
  "swiper navigation disabled", "swiper navigation hidden", "swiper button-next button-prev",
  "navigation arrows swiper", "swiper navigation parameters".
---

# Swiper — Navigation-Modul

Prev/Next-Schaltflächen zum Navigieren zwischen Slides.

```js
import Swiper from 'swiper';
import { Navigation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Navigation],
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
```

HTML:
```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
  </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>
```

## Vertiefung
- [references/deep/navigation.md](references/deep/navigation.md) — alle Parameter, CSS-Variablen, Events, Methoden, Properties
