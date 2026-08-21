# Swiper — Autoplay module

Automatic slide transition with configurable delay and control.

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

// Control programmatically
swiper.autoplay.pause();
swiper.autoplay.resume();
```

## Further reading
- [AUTOPLAY-DETAIL.md](AUTOPLAY-DETAIL.md) — all parameters, properties, methods, events including autoplayTimeLeft
