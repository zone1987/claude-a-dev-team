# Swiper Grid module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Fill directions explained](#fill-directions-explained)
- [Compatibility notes](#compatibility-notes)
- [Complete examples](#complete-examples)

## Concept

The Grid module enables multi-row slide layouts. Slides are arranged in a grid, and the fill direction (row by row or column by column) is configurable.

## Import and activation

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

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rows` | `number` | `1` | Number of slide rows in the multi-row layout |
| `fill` | `'row' \| 'column'` | `'column'` | Fill direction: `'column'` = column by column, `'row'` = row by row |

## Fill directions explained

### `fill: 'column'` (default)
Slides fill column by column: first all rows of one column, then the next column.

```
Slide 1 | Slide 3 | Slide 5
Slide 2 | Slide 4 | Slide 6
```

### `fill: 'row'`
Slides fill row by row: first all columns of one row, then the next row.

```
Slide 1 | Slide 2 | Slide 3
Slide 4 | Slide 5 | Slide 6
```

## Compatibility notes

- **Not compatible** with the Virtual Slides module
- **Loop mode:** requires enough slides or `loopAddBlankSlides: true`
- **`slidesPerView: 'auto'`:** only partially compatible

## Complete examples

### 2x3 grid (2 rows, 3 visible columns)

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

### Responsive grid with breakpoints

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

### With navigation and loop

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
Source: https://swiperjs.com/swiper-api#grid
