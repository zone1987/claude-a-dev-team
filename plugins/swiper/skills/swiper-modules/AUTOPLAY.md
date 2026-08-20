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
- [AUTOPLAY-DETAIL.md](AUTOPLAY-DETAIL.md) — alle Parameter, Properties, Methoden, Events inkl. autoplayTimeLeft
