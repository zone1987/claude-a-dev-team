---
name: swiper-history
description: >
  Vollständige Referenz des Swiper History-Moduls: key, replaceState, keepQuery, root —
  Browser-History-Integration mit data-history-Attribut je Slide.
  Trigger: "swiper history", "swiper history module", "swiper browser history",
  "swiper push state", "swiper history replaceState", "swiper data-history",
  "swiper url navigation", "swiper history key", "swiper history parameters".
---

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
- [references/deep/history.md](references/deep/history.md) — alle Parameter, data-history-Attribut, URL-Schema
