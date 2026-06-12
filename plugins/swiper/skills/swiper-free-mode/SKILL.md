---
name: swiper-free-mode
description: >
  Vollständige Referenz des Swiper Free Mode-Moduls: momentum, momentumRatio,
  momentumVelocityRatio, momentumBounce, minimumVelocity, sticky — freies Scrollen ohne
  Snap-Punkte, mit Momentum-Physik.
  Trigger: "swiper free mode", "swiper freeMode", "swiper momentum", "swiper no snap",
  "swiper freeMode sticky", "swiper momentum bounce", "swiper free scroll",
  "swiper freeMode parameters", "swiper minimumVelocity", "swiper momentumRatio".
---

# Swiper — Free Mode-Modul

Freies Scrollen ohne Slide-Snap, mit konfigurierbarer Momentum-Physik.

```js
import Swiper from 'swiper';
import { FreeMode } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: {
    enabled: true,
    momentum: true,
    momentumRatio: 0.8,
    sticky: false,
  },
});
```

## Vertiefung
- [references/deep/free-mode.md](references/deep/free-mode.md) — alle Parameter mit Typ/Default/Beschreibung
