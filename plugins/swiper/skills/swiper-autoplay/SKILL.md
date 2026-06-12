---
name: swiper-autoplay
description: >
  Vollständige Referenz des Swiper Autoplay-Moduls: delay, disableOnInteraction,
  pauseOnMouseEnter, reverseDirection, stopOnLastSlide, waitForTransition,
  Methoden start/stop/pause/resume, Events autoplayTimeLeft.
  Trigger: "swiper autoplay", "swiper auto slide", "swiper autoplay delay",
  "swiper autoplay pause", "swiper pauseOnMouseEnter", "swiper autoplay stop",
  "swiper autoplay module", "swiper autoplay events", "swiper autoplay parameters",
  "swiper disableOnInteraction", "swiper autoplay reverseDirection".
---

# Swiper — Autoplay-Modul

Automatische Slide-Transition mit konfigurierbarem Delay und Steuerung.

```js
import Swiper from 'swiper';
import { Autoplay } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Autoplay],
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
  },
});

// Programmatisch steuern
swiper.autoplay.pause();
swiper.autoplay.resume();
```

## Vertiefung
- [references/deep/autoplay.md](references/deep/autoplay.md) — alle Parameter, Properties, Methoden, Events inkl. autoplayTimeLeft
