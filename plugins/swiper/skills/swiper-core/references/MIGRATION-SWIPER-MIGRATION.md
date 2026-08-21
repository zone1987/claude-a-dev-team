# Swiper Migration Guide — v9, v10, v11

All breaking changes per major version with before/after code examples.

---

## Contents

- [Migrating to Swiper v11](#migrating-to-swiper-v11)
- [Migrating to Swiper v10](#migrating-to-swiper-v10)
- [Migrating to Swiper v9](#migrating-to-swiper-v9)
- [Breaking changes overview](#breaking-changes-overview)
- [Quick checklist for upgrading to v11](#quick-checklist-for-upgrading-to-v11)
- [Quick checklist for upgrading to v10](#quick-checklist-for-upgrading-to-v10)
- [Quick checklist for upgrading to v9](#quick-checklist-for-upgrading-to-v9)

## Migrating to Swiper v11

Official page: https://swiperjs.com/migration-guide-v11

### 1. `loopedSlides` parameter removed

The `loopedSlides` parameter has been removed.

```javascript
// OLD (v10):
const swiper = new Swiper('.swiper', {
  loop: true,
  loopedSlides: 5, // REMOVED
});

// NEW (v11):
const swiper = new Swiper('.swiper', {
  loop: true,
  loopAdditionalSlides: 5, // New parameter (if needed)
});
```

### 2. Element events prefix (BREAKING: default changed)

As of v11, all Swiper element events carry the prefix `swiper` by default.

```javascript
// OLD (v10 — no prefix):
swiperEl.addEventListener('slidechange', handler);
swiperEl.addEventListener('progress', handler);
swiperEl.addEventListener('reachend', handler);

// NEW (v11 — prefix "swiper" by default):
swiperEl.addEventListener('swiperslidechange', handler);
swiperEl.addEventListener('swiperprogress', handler);
swiperEl.addEventListener('swiperreachend', handler);
```

Keep the old behavior (no prefix):
```html
<swiper-container events-prefix="">
  <!-- Events: "slidechange", "progress" as in v10 -->
</swiper-container>
```

```javascript
Object.assign(swiperEl, {
  eventsPrefix: '', // No prefix
});
```

### 3. Container `overflow` CSS default

The container now defaults to `overflow: hidden`.

```css
/* If old layouts break — override it yourself: */
.swiper {
  overflow: clip; /* or: overflow: visible */
}
```

---

## Migrating to Swiper v10

Official page: https://swiperjs.com/migration-guide-v10

### 1. Module imports (MAJOR BREAKING CHANGE)

```javascript
// OLD (v9):
import Swiper, { Navigation, Pagination, Autoplay } from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/react';

// NEW (v10):
import Swiper from 'swiper';
import { Navigation, Pagination, Autoplay } from 'swiper/modules'; // NEW PATH
import { Swiper, SwiperSlide } from 'swiper/react'; // Unchanged
```

### 2. Swiper element DOM structure changed

v10 added an extra `.swiper` wrapper div:

**v9 shadow DOM structure:**
```html
<swiper-container>
  #shadow-root
    <div class="swiper-wrapper">
      <slot />   ← slides land here directly
    </div>
</swiper-container>
```

**v10 shadow DOM structure:**
```html
<swiper-container>
  #shadow-root
    <div class="swiper">          ← NEW: extra wrapper
      <div class="swiper-wrapper">
        <slot />
      </div>
    </div>
</swiper-container>
```

Code that accesses shadow DOM internals directly must be adjusted.

### 3. Swiper element no longer injects global styles

```javascript
// OLD (v9 — Swiper element injected styles globally):
// No extra action needed

// NEW (v10 — styles live in the shadow DOM only):
// Custom navigation/pagination/scrollbar elements need their own styles:
Object.assign(swiperEl, {
  injectStyles: [`
    .swiper-button-next,
    .swiper-button-prev {
      /* Your own styles */
    }
  `],
});
```

### 4. Package structure changed

```javascript
// OLD (v9 — direct file paths):
import Swiper from 'swiper/swiper.esm.js';
import 'swiper/swiper.min.css';

// NEW (v10 — new paths):
import Swiper from 'swiper';                    // Package root
import 'swiper/css';                            // Core CSS
import { Navigation } from 'swiper/modules';   // Modules
```

- `.esm.js` → `.mjs` (extension changed)
- `.browser.esm.js` → `.mjs` (unified)
- All module files were moved

### 5. CSS import paths

```javascript
// OLD (v9):
import 'swiper/css/swiper.css';
import 'swiper/swiper-bundle.css';

// NEW (v10):
import 'swiper/css';
import 'swiper/css/bundle';     // Bundle (all modules)
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-fade';
// etc.
```

---

## Migrating to Swiper v9

Official page: https://swiperjs.com/migration-guide-v9

### 1. Touch events removed — pointer events only

```javascript
// OLD (v8 — touch events):
swiper.on('touchStart', handler);
swiper.on('touchMove', handler);
swiper.on('touchEnd', handler);

// NEW (v9 — pointer events):
swiper.on('pointerDown', handler);   // instead of touchStart
swiper.on('pointerMove', handler);   // instead of touchMove
swiper.on('pointerUp', handler);     // instead of touchEnd
// Or listen to native DOM events instead of Swiper events
```

### 2. Autoplay module fully reworked

```javascript
// OLD (v8):
const swiper = new Swiper('.swiper', {
  autoplay: {
    delay: 3000,
    stopOnLastSlide: true,      // RENAMED
    disableOnInteraction: false,
    reverseDirection: false,    // NEW in v9
    waitForTransition: true,
  },
});

// v8 events:
swiper.on('autoplayStart', () => {});
swiper.on('autoplayStop', () => {});

// NEW (v9):
const swiper = new Swiper('.swiper', {
  autoplay: {
    delay: 3000,
    stopOnLastSlide: false,      // Unchanged
    disableOnInteraction: false, // Unchanged
    reverseDirection: false,
    waitForTransition: true,
  },
});

// v9 events (new names):
swiper.on('autoplayStart', () => {});     // Unchanged
swiper.on('autoplayStop', () => {});      // Unchanged
swiper.on('autoplayTimeLeft', (s, time, progress) => {}); // NEW
```

### 3. Loop mode reimplemented

```javascript
// OLD (v8 — loop via duplicated slides):
const swiper = new Swiper('.swiper', {
  loop: true,
  loopedSlides: 3,     // Number of slides to duplicate
  loopAdditionalSlides: 0,
});

// NEW (v9 — loop without duplicates, dynamic reordering):
const swiper = new Swiper('.swiper', {
  loop: true,
  // loopedSlides: 3,  // Different semantics now!
  // Requirement: slides.length >= slidesPerView * 2
});
```

### 4. Lazy loading moved into the core

```javascript
// OLD (v8 — separate Lazy module):
import Swiper, { Lazy } from 'swiper';
const swiper = new Swiper('.swiper', {
  modules: [Lazy],
  lazy: {
    loadPrevNext: true,
  },
  preloadImages: false,
});

// NEW (v9 — lazy in the core, no module import):
const swiper = new Swiper('.swiper', {
  lazy: true,
  // OR:
  lazy: {
    loadPrevNext: true,
    loadPrevNextAmount: 2,
  },
});
```

The HTML attribute for lazy images stays the same:
```html
<!-- Lazy-loaded image: -->
<img data-src="path/to/image.jpg" class="swiper-lazy" />
```

### 5. Dom7 removed

```javascript
// OLD (v8 — Dom7 available):
import { $ } from 'swiper/dom7';
import { $ } from 'swiper/utils/dom7';

// NEW (v9 — Dom7 removed, use vanilla JS):
// The import is no longer possible
// Instead of: swiper.$el.addClass('active')
// Now: swiper.el.classList.add('active')
```

### 6. Framework adapters removed

```javascript
// OLD (v8):
import { SwiperModule } from 'swiper/angular';
import { Swiper, SwiperSlide } from 'swiper/svelte';
import { Swiper, SwiperSlide } from 'swiper/solid';

// NEW (v9): framework adapters REMOVED
// Solution: use the Swiper element (web component)
import { register } from 'swiper/element/bundle';
register();
// <swiper-container>/<swiper-slide> as custom elements

// React and Vue are retained:
import { Swiper, SwiperSlide } from 'swiper/react'; // Still fine
import { Swiper, SwiperSlide } from 'swiper/vue';   // Still fine
```

### 7. Removed parameters (v9)

| Removed parameter | Alternative |
|---|---|
| `swipeHandler` | Removed, no replacement |
| `iOSEdgeSwipeDetection` | Removed |
| `iOSEdgeSwipeThreshold` | Removed |
| `passiveListeners` | Always passive in v9 |
| `uniqueNavElements` | Removed |
| `preloadImages` | Removed (lazy in the core) |
| `watchSlidesVisibility` | Renamed to `watchSlidesProgress` |

---

## Breaking changes overview

| Version | Biggest changes |
|---|---|
| v11 | `loopedSlides` removed, element events prefixed with `swiper` by default |
| v10 | Module imports move to `swiper/modules`, element DOM structure, CSS paths |
| v9 | Touch→pointer events, lazy in the core, Dom7 removed, Angular/Svelte/Solid adapters removed, new loop |

---

## Quick checklist for upgrading to v11

```text
[ ] loopedSlides → loopAdditionalSlides
[ ] Swiper element events: "slidechange" → "swiperslidechange"
[ ] Check container overflow (if clip behavior is required)
```

## Quick checklist for upgrading to v10

```text
[ ] import { Navigation } from 'swiper' → from 'swiper/modules'
[ ] Adjust CSS imports: 'swiper/css/swiper.css' → 'swiper/css'
[ ] Swiper element shadow DOM adjustments (if you access the DOM directly)
[ ] Swiper element global styles → injectStyles
```

## Quick checklist for upgrading to v9

```text
[ ] Angular/Svelte/Solid adapters → Swiper element
[ ] Touch events → pointer events
[ ] Lazy module → no module import anymore
[ ] Dom7 → vanilla JS
[ ] Loop: make sure slides.length >= slidesPerView * 2
[ ] Review the autoplay API (new parameters/events)
```

---

*Sources:*
- *https://swiperjs.com/migration-guide-v11*
- *https://swiperjs.com/migration-guide-v10*
- *https://swiperjs.com/migration-guide-v9*
- *Swiper v12.2.0*
