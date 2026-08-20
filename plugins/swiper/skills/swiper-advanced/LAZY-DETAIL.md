# Swiper lazy loading — Complete reference

## Contents

- [Concept](#concept)
- [Basic implementation](#basic-implementation)
- [Parameters (core parameters, no module import)](#parameters-core-parameters-no-module-import)
- [CSS preloader variants](#css-preloader-variants)
- [Preloader behavior](#preloader-behavior)
- [Complete example](#complete-example)
- [Migration from Swiper v8 (lazy module) to v9+](#migration-from-swiper-v8-lazy-module-to-v9)

## Concept

Since v9, Swiper uses native browser lazy loading (`loading="lazy"`). A separate module is no longer needed — lazy loading is driven by HTML attributes and two core parameters.

## Basic implementation

```html
<div class="swiper">
  <div class="swiper-wrapper">

    <!-- Lazy image with preloader spinner -->
    <div class="swiper-slide">
      <img src="image-1.jpg" loading="lazy" />
      <div class="swiper-lazy-preloader"></div>
    </div>

    <!-- With srcset for responsive images -->
    <div class="swiper-slide">
      <img
        src="image-small.jpg"
        srcset="image-large.jpg 2x"
        loading="lazy"
      />
      <div class="swiper-lazy-preloader"></div>
    </div>

    <!-- Light preloader for dark backgrounds -->
    <div class="swiper-slide">
      <img src="image-3.jpg" loading="lazy" />
      <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
    </div>

  </div>
</div>
```

## Parameters (core parameters, no module import)

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `lazyPreloadPrevNext` | `number` | `0` | Number of slides before and after the active slide that are preloaded (beyond `loading="lazy"`) |
| `lazyPreloaderClass` | `string` | `'swiper-lazy-preloader'` | CSS class for the preloader spinner |

```js
import Swiper from 'swiper';
// No module import needed!

const swiper = new Swiper('.swiper', {
  lazyPreloadPrevNext: 2,           // preload 2 slides before and after the active one
  lazyPreloaderClass: 'swiper-lazy-preloader',
});
```

## CSS preloader variants

### Dark preloader (default)

```html
<div class="swiper-lazy-preloader"></div>
```

CSS comes automatically from `swiper/css`:
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

### Light preloader

```html
<div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
```

## Preloader behavior

- The preloader spinner is removed automatically as soon as the image has loaded
- Swiper listens for the `load` event of the `<img>` tag
- On failure (404 etc.) the preloader stays visible

## Complete example

```js
import Swiper from 'swiper';
import { Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Navigation, Pagination],
  slidesPerView: 1,
  spaceBetween: 16,
  // Lazy loading — core parameters only, no module
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
      <!-- First image: load eagerly (above the fold) -->
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

## Migration from Swiper v8 (lazy module) to v9+

**Old (v8):**
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
<!-- Old: data-src instead of src -->
<img data-src="image.jpg" class="swiper-lazy" />
<div class="swiper-lazy-preloader"></div>
```

**New (v9+):**
```js
// No module import!
const swiper = new Swiper('.swiper', {
  lazyPreloadPrevNext: 2,
});
```

```html
<!-- New: native loading attribute -->
<img src="image.jpg" loading="lazy" />
<div class="swiper-lazy-preloader"></div>
```

---
Source: https://swiperjs.com/swiper-api#lazy-loading
