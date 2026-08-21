# Swiper History module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [data-history attribute](#data-history-attribute)
- [URL scheme](#url-scheme)
- [Complete configuration examples](#complete-configuration-examples)
- [Difference from Hash Navigation](#difference-from-hash-navigation)

## Concept

The History module integrates Swiper into the browser history. Every slide receives its own URL, so users can navigate with the browser back/forward buttons and direct links to specific slides become possible.

## Import and activation

```js
import Swiper from 'swiper';
import { History } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [History],
  history: {
    key: 'slides',
    replaceState: false,
    keepQuery: true,
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `true` | Enable the History module |
| `key` | `string` | `'slides'` | URL prefix; produces URLs such as `/slides/slide-name` |
| `replaceState` | `boolean` | `false` | Use `history.replaceState` instead of `pushState` (no history entry) |
| `keepQuery` | `boolean` | `false` | Keep the query parameters of the current URL |
| `root` | `string` | `''` | Root path for History URLs |

## data-history attribute

Every slide needs a `data-history` attribute holding the URL segment:

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <!-- URL becomes: /slides/introduction -->
    <div class="swiper-slide" data-history="introduction">
      Introduction
    </div>
    <!-- URL becomes: /slides/chapter-1 -->
    <div class="swiper-slide" data-history="chapter-1">
      Chapter 1
    </div>
    <!-- URL becomes: /slides/conclusion -->
    <div class="swiper-slide" data-history="conclusion">
      Conclusion
    </div>
  </div>
</div>
```

## URL scheme

With `key: 'slides'` and `root: '/'`:

| Active slide | Resulting URL |
|---------------|------------------|
| `data-history="intro"` | `/slides/intro` |
| `data-history="chapter-2"` | `/slides/chapter-2` |
| `data-history="end"` | `/slides/end` |

## Complete configuration examples

### Presentation with a clean URL scheme

```js
import Swiper from 'swiper';
import { History, Keyboard } from 'swiper/modules';

const swiper = new Swiper('.presentation', {
  modules: [History, Keyboard],
  slidesPerView: 1,
  keyboard: { enabled: true },
  history: {
    key: 'slide',
    replaceState: false,
    keepQuery: false,
    root: '/presentation',
  },
  speed: 600,
});
```

HTML:
```html
<div class="swiper-slide" data-history="intro">...</div>
<div class="swiper-slide" data-history="background">...</div>
<!-- produces: /presentation/slide/intro -->
```

### With replaceState (no history entries, but the URL updates)

```js
const swiper = new Swiper('.swiper', {
  modules: [History],
  history: {
    key: 'tab',
    replaceState: true,  // No history entry
    keepQuery: true,     // ?utm_source=... is preserved
  },
});
```

## Difference from Hash Navigation

| Feature | History module | Hash Navigation module |
|---------|---------------|----------------------|
| URL format | `/slides/slide-name` | `#slide-name` |
| Browser history | `pushState` / `replaceState` | Hash change |
| Server configuration | Needs rewrite rules | No server change |
| SEO | Better (real URLs) | Limited |
| Attribute on the slide | `data-history` | `data-hash` |

---
Source: https://swiperjs.com/swiper-api#history
