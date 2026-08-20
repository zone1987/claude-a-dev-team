# Swiper — Keyboard-Modul

Tastaturnavigation (Pfeiltasten, Page Up/Down) für Swiper-Instanzen.

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

// Programmgesteuert
swiper.keyboard.enable();
swiper.keyboard.disable();
```

## Vertiefung
- [KEYBOARD-DETAIL.md](KEYBOARD-DETAIL.md) — alle Parameter, Methoden, Events
