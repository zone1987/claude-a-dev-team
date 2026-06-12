---
name: swiper-a11y
description: >
  Vollständige Referenz des Swiper A11y (Accessibility)-Moduls: ARIA-Attribute,
  prevSlideMessage, nextSlideMessage, firstSlideMessage, lastSlideMessage,
  paginationBulletMessage, notificationClass — Screen-Reader-Unterstützung.
  Trigger: "swiper a11y", "swiper accessibility", "swiper screen reader", "swiper aria",
  "swiper a11y module", "swiper prevSlideMessage", "swiper accessibility parameters",
  "swiper a11y enabled", "swiper ARIA labels", "swiper accessible".
---

# Swiper — A11y (Accessibility)-Modul

ARIA-Attribute und Screen-Reader-Nachrichten für barrierefreie Swiper.

```js
import Swiper from 'swiper';
import { A11y } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [A11y],
  a11y: {
    prevSlideMessage: 'Vorheriger Slide',
    nextSlideMessage: 'Nächster Slide',
    firstSlideMessage: 'Dies ist der erste Slide',
    lastSlideMessage: 'Dies ist der letzte Slide',
    paginationBulletMessage: 'Gehe zu Slide {{index}}',
  },
});
```

## Vertiefung
- [references/deep/a11y.md](references/deep/a11y.md) — alle Parameter, ARIA-Rollen, CSS-Klassen
