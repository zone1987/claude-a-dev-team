---
name: swiper-controller
description: >
  Vollständige Referenz des Swiper Controller-Moduls: control, inverse, by (slide/progress)
  — mehrere Swiper-Instanzen synchronisieren, bidirektionale Steuerung.
  Trigger: "swiper controller", "swiper sync swipers", "swiper controller module",
  "swiper multiple swipers", "swiper controller inverse", "swiper by slide progress",
  "swiper controller control", "swiper synchronize", "swiper controller parameters".
---

# Swiper — Controller-Modul

Zwei oder mehr Swiper-Instanzen miteinander synchronisieren.

```js
import Swiper from 'swiper';
import { Controller } from 'swiper/modules';

const swiper1 = new Swiper('.swiper-1', { modules: [Controller] });
const swiper2 = new Swiper('.swiper-2', {
  modules: [Controller],
  controller: {
    control: swiper1,
    inverse: false,
    by: 'slide',
  },
});

// Bidirektional
swiper1.controller.control = swiper2;
swiper2.controller.control = swiper1;
```

## Vertiefung
- [references/deep/controller.md](references/deep/controller.md) — alle Parameter, Properties, Methoden, bidirektionale Sync-Pattern
