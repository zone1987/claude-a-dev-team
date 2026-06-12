---
name: swiper-effects
description: >
  Vollständige Referenz aller Swiper-Übergangseffekte: fade, cube, coverflow, flip, cards,
  creative — je mit vollständigem Parameter-Objekt (fadeEffect, cubeEffect, coverflowEffect,
  flipEffect, cardsEffect, creativeEffect inkl. prev/next Transform-Objekt).
  Trigger: "swiper effect", "swiper fade effect", "swiper cube effect", "swiper coverflow",
  "swiper flip effect", "swiper cards effect", "swiper creative effect", "swiper fadeEffect",
  "swiper cubeEffect", "swiper coverflowEffect", "swiper flipEffect", "swiper cardsEffect",
  "swiper creativeEffect", "swiper 3d effect", "swiper transition effect".
---

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
- [references/deep/effects.md](references/deep/effects.md) — alle Effekte mit vollständigen Parameter-Tabellen, Transform-Objekt-Schema, Import-Namen
