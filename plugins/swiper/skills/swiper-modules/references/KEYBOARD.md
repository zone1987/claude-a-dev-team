# Swiper — Keyboard module

Keyboard navigation (arrow keys, Page Up/Down) for Swiper instances.

```js
import Swiper from 'swiper';
import { Keyboard } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Keyboard],
  keyboard: {
    enabled: true,
    onlyInViewport: true,
    pageUpDown: true,
  },
});

// Programmatic control
swiper.keyboard.enable();
swiper.keyboard.disable();
```

## Further reading
- [KEYBOARD-DETAIL.md](KEYBOARD-DETAIL.md) — all parameters, methods, events
