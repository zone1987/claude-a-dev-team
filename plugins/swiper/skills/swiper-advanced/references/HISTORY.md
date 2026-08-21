# Swiper — History module

Every slide gets its own browser history URL.

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
<!-- produces URL: /slides/product-detail -->
<div class="swiper-slide" data-history="product-detail">...</div>
```

## Further reading
- [HISTORY-DETAIL.md](HISTORY-DETAIL.md) — all parameters, the data-history attribute, URL scheme
