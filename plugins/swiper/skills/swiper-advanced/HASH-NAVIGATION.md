# Swiper — Hash Navigation-Modul

URL-Hash wird beim Slide-Wechsel aktualisiert; Hash-Änderungen navigieren Slides.

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
<!-- URL wird zu #slide-2 beim Wechsel -->
<div class="swiper-slide" data-hash="slide-1">Slide 1</div>
<div class="swiper-slide" data-hash="slide-2">Slide 2</div>
```

## Vertiefung
- [HASH-NAVIGATION-DETAIL.md](HASH-NAVIGATION-DETAIL.md) — alle Parameter, data-hash-Attribut, Unterschied zu History-Modul
