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
- [GRID-DETAIL.md](GRID-DETAIL.md) — Parameter rows/fill mit Typ/Default/Beschreibung, Kompatibilitätshinweise
