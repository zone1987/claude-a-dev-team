---
name: swiper-scrollbar
description: >
  Vollständige Referenz des Swiper Scrollbar-Moduls: el, draggable, dragSize, hide,
  snapOnRelease, CSS-Variablen, Events (scrollbarDragStart/Move/End), Methoden.
  Trigger: "swiper scrollbar", "swiper scrollbar draggable", "swiper scrollbar module",
  "swiper scrollbar snapOnRelease", "swiper scrollbar hide", "swiper scrollbar drag",
  "swiper scrollbarDragStart", "swiper scrollbar parameters", "swiper scrollbar events".
---

# Swiper — Scrollbar-Modul

Scrollleiste mit optionalem Drag für die Swiper-Navigation.

```js
import Swiper from 'swiper';
import { Scrollbar } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Scrollbar],
  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true,
    snapOnRelease: true,
  },
});
```

## Vertiefung
- [references/deep/scrollbar.md](references/deep/scrollbar.md) — alle Parameter, CSS-Variablen, Events, Methoden, Properties
