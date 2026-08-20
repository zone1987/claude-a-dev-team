# Swiper — Navigation module

Prev/next buttons for navigating between slides.

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

## Deep dive
- [NAVIGATION-DETAIL.md](NAVIGATION-DETAIL.md) — all parameters, CSS variables, events, methods, properties
