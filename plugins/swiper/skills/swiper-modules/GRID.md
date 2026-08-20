# Swiper — Grid module

Multi-row slide layouts (grids) with configurable fill direction.

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

**Note:** Works with loop mode when there are enough slides or `loopAddBlankSlides: true` is set.

## Further reading
- [GRID-DETAIL.md](GRID-DETAIL.md) — rows/fill parameters with type/default/description, compatibility notes
