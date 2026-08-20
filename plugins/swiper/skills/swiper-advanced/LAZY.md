# Swiper — Lazy loading

Images load only once they become visible (native browser lazy loading).

```html
<div class="swiper-slide">
  <img src="bild.jpg" loading="lazy" />
  <div class="swiper-lazy-preloader"></div>
</div>

<!-- Light variant for dark backgrounds -->
<div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
```

```js
import Swiper from 'swiper';

const swiper = new Swiper('.swiper', {
  lazyPreloadPrevNext: 2,   // preload 2 slides before/after the active one
});
```

**Note:** No separate module import required — `lazyPreloadPrevNext` is a core parameter.

## Further reading
- [LAZY-DETAIL.md](LAZY-DETAIL.md) — lazyPreloadPrevNext/lazyPreloaderClass parameters, preloader CSS, srcset support
