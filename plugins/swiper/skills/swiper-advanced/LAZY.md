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
- [LAZY-DETAIL.md](LAZY-DETAIL.md) — Parameter lazyPreloadPrevNext/lazyPreloaderClass, Preloader-CSS, srcset-Support
