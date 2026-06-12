---
name: swiper-keyboard
description: >
  Vollständige Referenz des Swiper Keyboard-Moduls: enabled, onlyInViewport, pageUpDown,
  Methoden enable/disable, Event keyPress — Tastaturnavigation für Swiper.
  Trigger: "swiper keyboard", "swiper keyboard control", "swiper keyboard navigation",
  "swiper keyboard module", "swiper arrow keys", "swiper page up down",
  "swiper onlyInViewport", "swiper keyboard enabled", "swiper keyPress event",
  "swiper keyboard parameters".
---

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
- [references/deep/keyboard.md](references/deep/keyboard.md) — alle Parameter, Methoden, Events
