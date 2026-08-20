# Swiper Hash Navigation module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [data-hash attribute](#data-hash-attribute)
- [URL format](#url-format)
- [watchState — external hash navigation](#watchstate--external-hash-navigation)
- [Complete examples](#complete-examples)
- [Difference from the History module](#difference-from-the-history-module)

## Concept

The Hash Navigation module updates the URL hash on slide change and, conversely, navigates on hash changes (for example browser back, or a direct link containing a hash). Simpler than the History module — it requires no server configuration.

## Import and activation

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

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `true` | Enable hash navigation |
| `replaceState` | `boolean` | `false` | Use `history.replaceState` for hash updates (no history entry) |
| `watchState` | `boolean` | `false` | Watch and react to external hash changes (browser back, direct URL) |

## data-hash attribute

Every slide gets a `data-hash` attribute:

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <!-- URL hash becomes: #slide-1 -->
    <div class="swiper-slide" data-hash="slide-1">Slide 1</div>
    <!-- URL hash becomes: #slide-2 -->
    <div class="swiper-slide" data-hash="slide-2">Slide 2</div>
    <!-- URL hash becomes: #slide-3 -->
    <div class="swiper-slide" data-hash="slide-3">Slide 3</div>
  </div>
</div>
```

## URL format

| Active slide | URL |
|---------------|-----|
| `data-hash="intro"` | `https://example.com/#intro` |
| `data-hash="gallery"` | `https://example.com/#gallery` |
| `data-hash="contact"` | `https://example.com/#contact` |

## watchState — external hash navigation

With `watchState: true`, Swiper reacts to external hash changes:

```js
// The user navigates with browser back/forward
// or opens https://example.com/#slide-3 directly
// -> Swiper jumps to the slide with data-hash="slide-3"
const swiper = new Swiper('.swiper', {
  modules: [HashNavigation],
  hashNavigation: {
    watchState: true,
  },
});
```

## Complete examples

### Single page with anchorable sections

```js
import Swiper from 'swiper';
import { HashNavigation, Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [HashNavigation, Navigation, Pagination],
  direction: 'vertical',
  hashNavigation: {
    enabled: true,
    watchState: true,
    replaceState: false,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});
```

HTML:
```html
<div class="swiper-slide" data-hash="home">Home</div>
<div class="swiper-slide" data-hash="ueber-uns">About us</div>
<div class="swiper-slide" data-hash="leistungen">Services</div>
<div class="swiper-slide" data-hash="kontakt">Contact</div>
```

### External link to a slide

```html
<!-- Direct link to the contact slide -->
<a href="/page#kontakt">Open contact</a>
```

## Difference from the History module

| Feature | Hash Navigation | History module |
|---------|-----------------|---------------|
| URL format | `/#slide-name` | `/slides/slide-name` |
| Server rewrite | Not needed | Required for direct links |
| Attribute | `data-hash` | `data-history` |
| Parameter key | — | `key` (URL prefix) |

---
Source: https://swiperjs.com/swiper-api#hash-navigation
