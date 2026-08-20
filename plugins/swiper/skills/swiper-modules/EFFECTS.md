# Swiper — Übergangseffekte

Alle sechs Übergangseffekte mit vollständigen Parameterobjekten.

```js
import Swiper from 'swiper';
import { EffectFade, EffectCube, EffectCoverflow, EffectFlip, EffectCards, EffectCreative } from 'swiper/modules';

// Fade
const swiper = new Swiper('.swiper', {
  modules: [EffectFade],
  effect: 'fade',
  fadeEffect: { crossFade: true },
});

// Creative (eigene Transforms)
const swiper2 = new Swiper('.swiper', {
  modules: [EffectCreative],
  effect: 'creative',
  creativeEffect: {
    prev: { translate: [0, 0, -400] },
    next: { translate: ['100%', 0, 0] },
  },
});
```

## Vertiefung
- [EFFECTS-DETAIL.md](EFFECTS-DETAIL.md) — alle Effekte mit vollständigen Parameter-Tabellen, Transform-Objekt-Schema, Import-Namen
