---
name: swiper-grid
description: >
  Vollständige Referenz des Swiper Grid-Moduls: rows, fill (column/row) —
  mehrzeilige Slide-Layouts mit Swiper Grid.
  Trigger: "swiper grid", "swiper grid module", "swiper multiple rows", "swiper grid rows",
  "swiper grid fill", "swiper multirow", "swiper grid layout", "swiper rows parameter",
  "swiper grid parameters", "swiper column fill row fill".
---

# Swiper — Grid-Modul

Mehrzeilige Slide-Layouts (Raster) mit konfigurierbarer Füllrichtung.

```js
import Swiper from 'swiper';
import { Grid } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Grid],
  slidesPerView: 3,
  grid: {
    rows: 2,
    fill: 'column',
  },
  spaceBetween: 10,
});
```

**Hinweis:** Funktioniert mit Loop-Modus, wenn genügend Slides vorhanden oder `loopAddBlankSlides: true` gesetzt.

## Vertiefung
- [references/deep/grid.md](references/deep/grid.md) — Parameter rows/fill mit Typ/Default/Beschreibung, Kompatibilitätshinweise
