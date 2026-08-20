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
- [NAVIGATION-DETAIL.md](NAVIGATION-DETAIL.md) — alle Parameter, CSS-Variablen, Events, Methoden, Properties
