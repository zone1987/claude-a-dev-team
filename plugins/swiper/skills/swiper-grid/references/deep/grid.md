# Swiper Grid-Modul — Vollständige Referenz

## Konzept

Das Grid-Modul ermöglicht mehrzeilige Slide-Layouts. Slides werden in einem Raster angeordnet, wobei die Füllrichtung (zeilenweise oder spaltenweise) konfigurierbar ist.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Grid } from 'swiper/modules';
import 'swiper/css/grid';

const swiper = new Swiper('.swiper', {
  modules: [Grid],
  slidesPerView: 2,
  grid: {
    rows: 2,
    fill: 'column',
  },
  spaceBetween: 10,
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `rows` | `number` | `1` | Anzahl der Slide-Zeilen im mehrzeiligen Layout |
| `fill` | `'row' \| 'column'` | `'column'` | Füllrichtung: `'column'` = spaltenweise, `'row'` = zeilenweise |

## Fill-Richtungen erklärt

### `fill: 'column'` (Standard)
Slides füllen spaltenweise: erst alle Zeilen einer Spalte, dann die nächste Spalte.

```
Slide 1 | Slide 3 | Slide 5
Slide 2 | Slide 4 | Slide 6
```

### `fill: 'row'`
Slides füllen zeilenweise: erst alle Spalten einer Zeile, dann die nächste Zeile.

```
Slide 1 | Slide 2 | Slide 3
Slide 4 | Slide 5 | Slide 6
```

## Kompatibilitätshinweise

- **Nicht kompatibel** mit Virtual Slides-Modul
- **Loop-Modus:** Erfordert genügend Slides oder `loopAddBlankSlides: true`
- **`slidesPerView: 'auto'`:** Eingeschränkt kompatibel

## Vollständige Beispiele

### 2x3 Raster (2 Zeilen, 3 sichtbare Spalten)

```js
const swiper = new Swiper('.swiper', {
  modules: [Grid],
  slidesPerView: 3,
  grid: {
    rows: 2,
    fill: 'column',
  },
  spaceBetween: 16,
});
```

### Responsive Grid mit Breakpoints

```js
const swiper = new Swiper('.swiper', {
  modules: [Grid],
  slidesPerView: 2,
  grid: {
    rows: 2,
  },
  spaceBetween: 10,
  breakpoints: {
    768: {
      slidesPerView: 3,
      grid: {
        rows: 2,
      },
    },
    1024: {
      slidesPerView: 4,
      grid: {
        rows: 1,
      },
    },
  },
});
```

### Mit Navigation und Loop

```js
import Swiper from 'swiper';
import { Grid, Navigation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Grid, Navigation],
  slidesPerView: 3,
  slidesPerGroup: 3,
  grid: {
    rows: 2,
    fill: 'row',
  },
  spaceBetween: 12,
  loop: true,
  loopAddBlankSlides: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
```

---
Quelle: https://swiperjs.com/swiper-api#grid
