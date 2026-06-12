---
name: swiper-lazy
description: >
  Vollständige Referenz des Swiper Lazy Loading: loading="lazy" native Browser-Integration,
  lazyPreloadPrevNext, lazyPreloaderClass, swiper-lazy-preloader HTML-Element.
  Trigger: "swiper lazy", "swiper lazy loading", "swiper lazy load images",
  "swiper lazyPreloadPrevNext", "swiper lazy preloader", "swiper loading lazy",
  "swiper lazy module", "swiper image lazy load", "swiper lazy parameters",
  "swiper swiper-lazy-preloader".
---

# Swiper — Lazy Loading

Bilder werden erst beim Sichtbarwerden geladen (natives Browser-Lazy-Loading).

```html
<div class="swiper-slide">
  <img src="bild.jpg" loading="lazy" />
  <div class="swiper-lazy-preloader"></div>
</div>

<!-- Helle Variante für dunkle Hintergründe -->
<div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
```

```js
import Swiper from 'swiper';

const swiper = new Swiper('.swiper', {
  lazyPreloadPrevNext: 2,   // 2 Slides vor/nach aktiv vorladen
});
```

**Hinweis:** Kein separates Modul-Import notwendig — `lazyPreloadPrevNext` ist ein Core-Parameter.

## Vertiefung
- [references/deep/lazy.md](references/deep/lazy.md) — Parameter lazyPreloadPrevNext/lazyPreloaderClass, Preloader-CSS, srcset-Support
