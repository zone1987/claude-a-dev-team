# Swiper Element — Complete reference (Web Component)

Swiper Element are native custom elements (registered via `customElements.define`).
Available since Swiper v9. Replaces the removed framework adapters for Angular, Svelte and Solid.

---

## Contents

- [Installation & registration](#installation-registration)
- [The two custom elements](#the-two-custom-elements)
- [Parameters as HTML attributes (kebab-case)](#parameters-as-html-attributes-kebab-case)
- [Complex parameters via JavaScript properties](#complex-parameters-via-javascript-properties)
- [Updating parameters after initialization](#updating-parameters-after-initialization)
- [Event system](#event-system)
- [Swiper instance & methods](#swiper-instance-methods)
- [Slots](#slots)
- [CSS & Shadow DOM](#css-shadow-dom)
- [Auto-render Navigation/Pagination/Scrollbar](#auto-render-navigationpaginationscrollbar)
- [Thumbs integration (CSS selector)](#thumbs-integration-css-selector)
- [Virtual Slides](#virtual-slides)
- [Lazy Loading](#lazy-loading)
- [Core vs. Bundle](#core-vs-bundle)
- [Registering custom plugin parameters (v9.1.0+)](#registering-custom-plugin-parameters-v910)
- [Framework integration overview](#framework-integration-overview)
- [Comparison: Swiper Element vs. Swiper Core (class)](#comparison-swiper-element-vs-swiper-core-class)

## Installation & registration

### NPM
```bash
npm install swiper
```

```javascript
// Bundle (all modules included, auto-styles)
import { register } from 'swiper/element/bundle';
register();

// Core only (lightweight, include modules manually)
import { register } from 'swiper/element';
register();
```

### CDN (auto-registered, no `register()` needed)
```html
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-element-bundle.min.js"></script>
```

---

## The two custom elements

| Element | Purpose |
|---|---|
| `<swiper-container>` | Main slider container with all Swiper parameters |
| `<swiper-slide>` | A single slide |

---

## Parameters as HTML attributes (kebab-case)

Every Swiper API parameter can be set as a kebab-case attribute on `<swiper-container>`.

```html
<swiper-container
  slides-per-view="3"
  space-between="30"
  speed="500"
  loop="true"
  css-mode="true"
  centered-slides="true"
  navigation="true"
  pagination="true"
  scrollbar="true"
>
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <swiper-slide>Slide 3</swiper-slide>
</swiper-container>
```

### Nested object parameters (bracket notation in the attribute)

```html
<swiper-container
  grid-rows="3"
  mousewheel-force-to-axis="true"
  autoplay-delay="2500"
  autoplay-disable-on-interaction="false"
  pagination-clickable="true"
  navigation-next-el=".my-button-next"
  navigation-prev-el=".my-button-prev"
>
```

### Boolean attributes

Pass boolean parameters as the string `"true"` or `"false"`:
```html
<swiper-container loop="true" autoplay="true"></swiper-container>
```

---

## Complex parameters via JavaScript properties

For parameters such as `breakpoints`, `pagination.renderBullet`, arrays etc., set them directly as JS properties:

```javascript
const swiperEl = document.querySelector('swiper-container');

const params = {
  slidesPerView: 1,
  spaceBetween: 10,
  loop: true,
  // Complex parameters — only possible via property
  breakpoints: {
    640: { slidesPerView: 2, spaceBetween: 20 },
    768: { slidesPerView: 3, spaceBetween: 30 },
    1024: { slidesPerView: 4, spaceBetween: 40 },
  },
  pagination: {
    clickable: true,
    renderBullet: (index, className) =>
      `<span class="${className}">${index + 1}</span>`,
  },
  on: {
    init() { console.log('initialized'); },
  },
};

Object.assign(swiperEl, params);
swiperEl.initialize();
```

**Important:** unless `init="false"` is set, `<swiper-container>` initializes itself automatically on DOM ready. For property binding before initialization:

```html
<swiper-container init="false">
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

```javascript
const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, { slidesPerView: 3, breakpoints: { ... } });
swiperEl.initialize(); // Initialize manually
```

---

## Updating parameters after initialization

```javascript
const swiperEl = document.querySelector('swiper-container');

// Via attribute (camelCase params → kebab-case attribute name)
swiperEl.setAttribute('slides-per-view', '3');
swiperEl.setAttribute('space-between', '20');

// Via property (camelCase directly)
swiperEl.slidesPerView = 3;
swiperEl.spaceBetween = 20;
```

---

## Event system

### Standard events (v11+: prefix `swiper` by default)

All Swiper events are fired as DOM custom events. As of v11, events carry the prefix `swiper` by default:

| Swiper API event | DOM event name (v11 default) |
|---|---|
| `slideChange` | `swiperslidechange` |
| `progress` | `swiperprogress` |
| `reachEnd` | `swiperreachend` |
| `reachBeginning` | `swiperreachbeginning` |
| `click` | `swiperclick` |
| `tap` | `swipetap` |
| `init` | `swiperinit` |
| `destroy` | `swiperdestroy` |
| `transitionStart` | `swipetransitionstart` |
| `transitionEnd` | `swipetransitionend` |
| `slideNextTransitionStart` | `swiperslideNextTransitionstart` |

Event arguments are passed via `event.detail` (array):

```javascript
const swiperEl = document.querySelector('swiper-container');

// Simple event
swiperEl.addEventListener('swiperslidechange', (event) => {
  console.log('Slide changed');
  console.log(event.detail[0]); // Swiper instance
});

// Event with several parameters
swiperEl.addEventListener('swiperprogress', (event) => {
  const [swiper, progress] = event.detail;
  console.log(`Progress: ${progress}`);
});

swiperEl.addEventListener('swipetap', (event) => {
  const [swiper, pointerEvent] = event.detail;
});
```

### Customizing the event prefix

```html
<!-- No prefix (behavior before v11) -->
<swiper-container events-prefix="">
  <!-- Events: "slidechange", "progress", etc. -->
</swiper-container>

<!-- Custom prefix -->
<swiper-container events-prefix="swiper-">
  <!-- Events: "swiper-slidechange", "swiper-progress", etc. -->
</swiper-container>
```

---

## Swiper instance & methods

```javascript
const swiperEl = document.querySelector('swiper-container');

// After initialization: Swiper instance via the .swiper property
const swiper = swiperEl.swiper;

// All Swiper methods available
swiper.slideNext();
swiper.slidePrev();
swiper.slideTo(3);
swiper.slideToLoop(3);
swiper.update();
swiper.destroy();
swiper.autoplay.start();
swiper.autoplay.stop();
swiper.pagination.render();
swiper.pagination.update();

// Properties
console.log(swiper.activeIndex);
console.log(swiper.realIndex);
console.log(swiper.slides);
console.log(swiper.isBeginning);
console.log(swiper.isEnd);
```

---

## Slots

Position content inside `<swiper-container>` (outside the `.swiper-wrapper`):

```html
<swiper-container>
  <!-- Before the swiper-wrapper -->
  <div slot="container-start">This content comes before the slides</div>

  <!-- Normal slides (no slot attribute) -->
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <!-- After the swiper-wrapper -->
  <div slot="container-end">This content comes after the slides</div>

  <!-- Before the swiper-wrapper (inside the wrapper) -->
  <div slot="wrapper-start">In the wrapper, before the slides</div>

  <!-- After the swiper-wrapper (inside the wrapper) -->
  <div slot="wrapper-end">In the wrapper, after the slides</div>
</swiper-container>
```

---

## CSS & Shadow DOM

### CSS parts (shadow DOM styling without `::slotted`)

```css
/* Container */
swiper-container::part(container) { }

/* Wrapper */
swiper-container::part(wrapper) { }

/* Navigation */
swiper-container::part(button-prev) { background-color: blue; }
swiper-container::part(button-next) { background-color: blue; }

/* Pagination */
swiper-container::part(pagination) { }
swiper-container::part(bullet) { background-color: grey; }
swiper-container::part(bullet-active) { background-color: red; }

/* Scrollbar */
swiper-container::part(scrollbar) { }
swiper-container::part(scrollbar-drag) { }
```

### Injecting styles into the shadow DOM (`injectStyles`)

Inject CSS strings directly into the shadow DOM scope:

```javascript
const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, {
  injectStyles: [
    `
    :host(.red) .swiper-wrapper {
      background-color: red;
    }
    .swiper-button-next,
    .swiper-button-prev {
      color: white;
      background: rgba(0,0,0,0.3);
      padding: 8px;
      border-radius: 50%;
    }
    `,
  ],
  injectStylesUrls: [
    'path/to/custom-navigation.css',
    'path/to/custom-pagination.css',
  ],
});
swiperEl.initialize();
```

---

## Auto-render Navigation/Pagination/Scrollbar

```html
<!-- Automatically generated UI elements -->
<swiper-container
  navigation="true"
  pagination="true"
  scrollbar="true"
>
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

---

## Thumbs integration (CSS selector)

```html
<!-- Thumbs Swiper (no JS needed for a simple configuration) -->
<swiper-container
  thumbs-swiper=".my-thumbs"
  loop="true"
  space-between="10"
>
  <swiper-slide><img src="img1.jpg" /></swiper-slide>
  <swiper-slide><img src="img2.jpg" /></swiper-slide>
</swiper-container>

<swiper-container
  class="my-thumbs"
  slides-per-view="4"
  space-between="10"
  watch-slides-progress="true"
>
  <swiper-slide><img src="img1.jpg" /></swiper-slide>
  <swiper-slide><img src="img2.jpg" /></swiper-slide>
</swiper-container>
```

---

## Virtual Slides

```html
<swiper-container virtual="true" slides-per-view="3">
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <!-- More slides -->
</swiper-container>
```

---

## Lazy Loading

```html
<swiper-container>
  <swiper-slide lazy="true">
    <img src="image.jpg" loading="lazy" />
  </swiper-slide>
</swiper-container>
```

---

## Core vs. Bundle

### Bundle (recommended for most cases)
```javascript
import { register } from 'swiper/element/bundle';
register();
// All modules + styles included
```

### Core (minimal bundle, modules manual)
```javascript
import { register } from 'swiper/element';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';
register();

const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, {
  modules: [Navigation, Pagination, Autoplay],
  injectStylesUrls: [
    'swiper/css/navigation',
    'swiper/css/pagination',
  ],
  navigation: true,
  pagination: { clickable: true },
});
swiperEl.initialize();
```

---

## Registering custom plugin parameters (v9.1.0+)

```javascript
// Make your own plugin parameters known so they are recognized as attributes
window.SwiperElementRegisterParams(['myParam', 'anotherParam']);

const swiperEl = document.querySelector('swiper-container');
// Now usable as an attribute:
swiperEl.setAttribute('my-param', 'value');
```

---

## Framework integration overview

| Framework | Recommendation | Note |
|---|---|---|
| Angular | Swiper Element | `CUSTOM_ELEMENTS_SCHEMA` in the module/component |
| Svelte | Swiper Element | `bind:this`, events with `on:swiper*` |
| Solid | Swiper Element | `ref`, `addEventListener` |
| React | Swiper React components OR Element | Element in React with `useRef` + `addEventListener` |
| Vue | Swiper Vue components OR Element | Element in Vue with `:` and `@` natively |

---

## Comparison: Swiper Element vs. Swiper Core (class)

| Feature | Swiper Element | Swiper Core |
|---|---|---|
| Initialization | HTML tag + auto/`initialize()` | `new Swiper('.selector', options)` |
| Parameters | HTML attributes (kebab) + JS properties | JS object in the constructor |
| Events | DOM custom events (lowercase + prefix) | `.on('eventName', fn)` |
| Access | `.swiper` property of the element | Direct instance variable |
| Shadow DOM | Yes (CSS parts, injectStyles) | No |
| Framework-neutral | Yes | No (JS-only) |
| Bundle size | Slightly larger | Smaller (core-only possible) |

---

*Source: https://swiperjs.com/element — Swiper v12.2.0*
