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
- [SCROLLBAR-DETAIL.md](SCROLLBAR-DETAIL.md) — alle Parameter, CSS-Variablen, Events, Methoden, Properties
