# Swiper — Manipulation module

Add, insert, and remove slides dynamically in the DOM.

```js
import Swiper from 'swiper';
import { Manipulation } from 'swiper/modules';

const swiper = new Swiper('.swiper', { modules: [Manipulation] });

// Adding
swiper.appendSlide('<div class="swiper-slide">New at the end</div>');
swiper.prependSlide('<div class="swiper-slide">New at the beginning</div>');
swiper.addSlide(2, '<div class="swiper-slide">At position 2</div>');

// Several at once
swiper.appendSlide([
  '<div class="swiper-slide">A</div>',
  '<div class="swiper-slide">B</div>',
]);

// Removing
swiper.removeSlide(0);           // single
swiper.removeSlide([0, 1, 2]);   // several
swiper.removeAllSlides();        // all
```

**Note:** This module is intended for Swiper Core, not for the React/Vue integrations.

## Further reading
- [MANIPULATION-DETAIL.md](MANIPULATION-DETAIL.md) — all method signatures, parameter types, framework notes
