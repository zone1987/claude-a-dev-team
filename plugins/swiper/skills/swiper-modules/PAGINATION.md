# Swiper — Pagination-Modul

Bullet-, Bruch-, Fortschrittsbalken- oder benutzerdefinierte Pagination.

```js
import Swiper from 'swiper';
import { Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
    dynamicBullets: true,
  },
});
```

## Vertiefung
- [PAGINATION-DETAIL.md](PAGINATION-DETAIL.md) — alle Parameter mit Typ/Default/Beschreibung, alle Render-Funktions-Signaturen, CSS-Variablen, Events, Methoden
