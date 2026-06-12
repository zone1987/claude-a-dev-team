---
name: swiper-pagination
description: >
  Vollständige Referenz des Swiper Pagination-Moduls: bullets/fraction/progressbar/custom,
  clickable, dynamicBullets, renderBullet/Fraction/Custom/Progressbar, CSS-Variablen, Events.
  Trigger: "swiper pagination", "swiper bullets", "swiper fraction pagination",
  "swiper progressbar pagination", "swiper custom pagination", "swiper renderBullet",
  "swiper dynamicBullets", "swiper pagination clickable", "swiper pagination module",
  "swiper paginationRender", "swiper pagination parameters", "swiper dot navigation".
---

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
- [references/deep/pagination.md](references/deep/pagination.md) — alle Parameter mit Typ/Default/Beschreibung, alle Render-Funktions-Signaturen, CSS-Variablen, Events, Methoden
