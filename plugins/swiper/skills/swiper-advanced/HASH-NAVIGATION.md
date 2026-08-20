# Swiper — Hash Navigation module

The URL hash updates on slide change; hash changes navigate slides.

```js
import Swiper from 'swiper';
import { HashNavigation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [HashNavigation],
  hashNavigation: {
    enabled: true,
    replaceState: false,
    watchState: true,
  },
});
```

HTML:
```html
<!-- URL becomes #slide-2 on change -->
<div class="swiper-slide" data-hash="slide-1">Slide 1</div>
<div class="swiper-slide" data-hash="slide-2">Slide 2</div>
```

## Further reading
- [HASH-NAVIGATION-DETAIL.md](HASH-NAVIGATION-DETAIL.md) — all parameters, the data-hash attribute, difference from the History module
