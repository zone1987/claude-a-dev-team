---
name: swiper-hash-navigation
description: >
  Vollständige Referenz des Swiper Hash Navigation-Moduls: enabled, replaceState,
  watchState — URL-Hash-basierte Slide-Navigation mit data-hash-Attribut.
  Trigger: "swiper hash navigation", "swiper hash", "swiper hash module",
  "swiper url hash", "swiper hashNavigation", "swiper replaceState hash",
  "swiper watchState", "swiper data-hash", "swiper hash parameters",
  "swiper anchor navigation".
---

# Swiper — Hash Navigation-Modul

URL-Hash wird beim Slide-Wechsel aktualisiert; Hash-Änderungen navigieren Slides.

```js
import Swiper from 'swiper';
import { HashNavigation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [HashNavigation],
  hashNavigation: {
    enabled: true,
    replaceState: false,
    watchState: true,
  },
});
```

HTML:
```html
<!-- URL wird zu #slide-2 beim Wechsel -->
<div class="swiper-slide" data-hash="slide-1">Slide 1</div>
<div class="swiper-slide" data-hash="slide-2">Slide 2</div>
```

## Vertiefung
- [references/deep/hash-navigation.md](references/deep/hash-navigation.md) — alle Parameter, data-hash-Attribut, Unterschied zu History-Modul
