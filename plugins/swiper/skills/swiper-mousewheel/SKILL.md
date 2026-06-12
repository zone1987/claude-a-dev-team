---
name: swiper-mousewheel
description: >
  Vollständige Referenz des Swiper Mousewheel-Moduls: enabled, invert, forceToAxis,
  releaseOnEdges, sensitivity, thresholdDelta, thresholdTime, eventsTarget,
  noMousewheelClass, Methoden enable/disable, Event scroll.
  Trigger: "swiper mousewheel", "swiper scroll wheel", "swiper mousewheel module",
  "swiper mousewheel invert", "swiper releaseOnEdges", "swiper mousewheel sensitivity",
  "swiper mousewheel parameters", "swiper mousewheel events", "swiper scroll event".
---

# Swiper — Mousewheel-Modul

Mausrad-/Trackpad-Steuerung für Swiper mit konfigurierbarer Sensitivität.

```js
import Swiper from 'swiper';
import { Mousewheel } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Mousewheel],
  mousewheel: {
    enabled: true,
    invert: false,
    releaseOnEdges: true,
    sensitivity: 1,
  },
});
```

## Vertiefung
- [references/deep/mousewheel.md](references/deep/mousewheel.md) — alle Parameter, Methoden, Events, noMousewheelClass-Verwendung
