# Swiper — History-Modul

Jeder Slide bekommt eine eigene Browser-History-URL.

```js
import Swiper from 'swiper';
import { History } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [History],
  history: {
    key: 'slides',
    replaceState: false,
    keepQuery: true,
    root: '/',
  },
});
```

HTML:
```html
<!-- erzeugt URL: /slides/produkt-detail -->
<div class="swiper-slide" data-history="produkt-detail">...</div>
```

## Vertiefung
- [HISTORY-DETAIL.md](HISTORY-DETAIL.md) — alle Parameter, data-history-Attribut, URL-Schema
