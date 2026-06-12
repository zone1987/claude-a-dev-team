# Swiper Lazy Loading — Vollständige Referenz

## Konzept

Swiper nutzt seit v9 das native Browser-Lazy-Loading (`loading="lazy"`). Es ist kein separates Modul mehr nötig — Lazy Loading wird über HTML-Attribute und zwei Core-Parameter gesteuert.

## Grundlegende Implementierung

```html
<div class="swiper">
  <div class="swiper-wrapper">

    <!-- Lazy-Bild mit Preloader-Spinner -->
    <div class="swiper-slide">
      <img src="bild-1.jpg" loading="lazy" />
      <div class="swiper-lazy-preloader"></div>
    </div>

    <!-- Mit srcset für responsive Bilder -->
    <div class="swiper-slide">
      <img
        src="bild-small.jpg"
        srcset="bild-large.jpg 2x"
        loading="lazy"
      />
      <div class="swiper-lazy-preloader"></div>
    </div>

    <!-- Heller Preloader für dunkle Hintergründe -->
    <div class="swiper-slide">
      <img src="bild-3.jpg" loading="lazy" />
      <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
    </div>

  </div>
</div>
```

## Parameter (Core-Parameter, kein Modul-Import)

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `lazyPreloadPrevNext` | `number` | `0` | Anzahl der Slides vor und nach dem aktiven Slide die vorab geladen werden (über `loading="lazy"` hinaus) |
| `lazyPreloaderClass` | `string` | `'swiper-lazy-preloader'` | CSS-Klasse für den Preloader-Spinner |

```js
import Swiper from 'swiper';
// Kein Modul-Import nötig!

const swiper = new Swiper('.swiper', {
  lazyPreloadPrevNext: 2,           // 2 Slides vor und nach aktiv vorladen
  lazyPreloaderClass: 'swiper-lazy-preloader',
});
```

## CSS-Preloader-Varianten

### Dunkler Preloader (Standard)

```html
<div class="swiper-lazy-preloader"></div>
```

CSS automatisch aus `swiper/css`:
```css
.swiper-lazy-preloader {
  width: 42px;
  height: 42px;
  position: absolute;
  left: 50%;
  top: 50%;
  margin-left: -21px;
  margin-top: -21px;
  z-index: 10;
  transform-origin: 50%;
  box-sizing: border-box;
  border: 4px solid var(--swiper-preloader-color, var(--swiper-theme-color));
  border-top-color: transparent;
  border-radius: 50%;
  animation: swiper-preloader-spin 1s infinite linear;
}
```

### Heller Preloader

```html
<div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
```

## Preloader-Verhalten

- Der Preloader-Spinner wird automatisch entfernt sobald das Bild geladen ist
- Swiper hört auf das `load`-Event des `<img>`-Tags
- Bei Fehler (404 etc.) bleibt der Preloader sichtbar

## Vollständiges Beispiel

```js
import Swiper from 'swiper';
import { Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Navigation, Pagination],
  slidesPerView: 1,
  spaceBetween: 16,
  // Lazy Loading — nur Core-Parameter, kein Modul
  lazyPreloadPrevNext: 3,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    type: 'fraction',
  },
});
```

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <!-- Erstes Bild: eager laden (above the fold) -->
      <img src="hero.jpg" loading="eager" />
    </div>
    <div class="swiper-slide">
      <img src="slide-2.jpg" loading="lazy" />
      <div class="swiper-lazy-preloader"></div>
    </div>
    <div class="swiper-slide">
      <img src="slide-3.jpg" loading="lazy" />
      <div class="swiper-lazy-preloader"></div>
    </div>
  </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
  <div class="swiper-pagination"></div>
</div>
```

## Migration von Swiper v8 (lazy-Modul) zu v9+

**Alt (v8):**
```js
import { Lazy } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Lazy],
  lazy: {
    loadPrevNext: true,
    loadPrevNextAmount: 2,
  },
});
```

```html
<!-- Alt: data-src statt src -->
<img data-src="bild.jpg" class="swiper-lazy" />
<div class="swiper-lazy-preloader"></div>
```

**Neu (v9+):**
```js
// Kein Modul-Import!
const swiper = new Swiper('.swiper', {
  lazyPreloadPrevNext: 2,
});
```

```html
<!-- Neu: natives loading-Attribut -->
<img src="bild.jpg" loading="lazy" />
<div class="swiper-lazy-preloader"></div>
```

---
Quelle: https://swiperjs.com/swiper-api#lazy-loading
