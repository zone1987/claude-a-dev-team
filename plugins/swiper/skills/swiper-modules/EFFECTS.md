# Swiper — Transition effects

All six transition effects with complete parameter objects.

```js
import Swiper from 'swiper';
import { EffectFade, EffectCube, EffectCoverflow, EffectFlip, EffectCards, EffectCreative } from 'swiper/modules';

// Fade
const swiper = new Swiper('.swiper', {
  modules: [EffectFade],
  effect: 'fade',
  fadeEffect: { crossFade: true },
});

// Creative (custom transforms)
const swiper2 = new Swiper('.swiper', {
  modules: [EffectCreative],
  effect: 'creative',
  creativeEffect: {
    prev: { translate: [0, 0, -400] },
    next: { translate: ['100%', 0, 0] },
  },
});
```

## Further reading
- [EFFECTS-DETAIL.md](EFFECTS-DETAIL.md) — all effects with complete parameter tables, transform object schema, import names
