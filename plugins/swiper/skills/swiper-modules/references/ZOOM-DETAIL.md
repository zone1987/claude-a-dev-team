# Swiper Zoom module — Complete reference

## Contents

- [Import and activation](#import-and-activation)
- [HTML structure](#html-structure)
- [Parameters](#parameters)
- [Data attributes](#data-attributes)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [Programmatic control](#programmatic-control)
- [Complete example (photo gallery)](#complete-example-photo-gallery)

## Import and activation

```js
import Swiper from 'swiper';
import { Zoom } from 'swiper/modules';
import 'swiper/css/zoom';

const swiper = new Swiper('.swiper', {
  modules: [Zoom],
  zoom: {
    maxRatio: 3,
    minRatio: 1,
    toggle: true,
  },
});
```

## HTML structure

All zoomable images must be wrapped in a `.swiper-zoom-container`:

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <!-- Standard zoom -->
    <div class="swiper-slide">
      <div class="swiper-zoom-container">
        <img src="image1.jpg" />
      </div>
    </div>

    <!-- Override maxRatio per slide -->
    <div class="swiper-slide">
      <div class="swiper-zoom-container" data-swiper-zoom="5">
        <img src="image2.jpg" />
      </div>
    </div>

    <!-- Custom zoom target (not an img) -->
    <div class="swiper-slide">
      <div class="swiper-zoom-container">
        <div class="swiper-zoom-target">
          Zoomable content
        </div>
      </div>
    </div>
  </div>
</div>
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Enable the Zoom module |
| `maxRatio` | `number` | `3` | Maximum zoom factor (3 = 300%) |
| `minRatio` | `number` | `1` | Minimum zoom factor (1 = original size) |
| `toggle` | `boolean` | `true` | Toggle zoom with a double tap |
| `containerClass` | `string` | `'swiper-zoom-container'` | CSS class for zoom container elements |
| `zoomedSlideClass` | `string` | `'swiper-slide-zoomed'` | CSS class for the currently zoomed slide |
| `limitToOriginalSize` | `boolean` | `false` | Never zoom an image beyond 100% of its original size |
| `panOnMouseMove` | `boolean` | `false` | Pan the zoomed image automatically as the mouse moves |

## Data attributes

| Attribute | Type | Description |
|----------|-----|--------------|
| `data-swiper-zoom` | `number` | Override `maxRatio` per slide |

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.zoom.enabled` | `boolean` | Is the Zoom module active? |
| `swiper.zoom.scale` | `number` | Current zoom factor of the active slide |

## Methods

| Method | Signature | Description |
|---------|---------|--------------|
| `swiper.zoom.enable()` | `() => void` | Enable the Zoom module |
| `swiper.zoom.disable()` | `() => void` | Disable the Zoom module |
| `swiper.zoom.in(ratio?)` | `(ratio?: number) => void` | Zoom into the active slide; optional target factor |
| `swiper.zoom.out()` | `() => void` | Zoom the active slide back to `minRatio` |
| `swiper.zoom.toggle(event?)` | `(event?: Event) => void` | Toggle the zoom state of the active slide |

## Events

| Event | Arguments | Description |
|-------|-----------|--------------|
| `zoomChange` | `(swiper, scale, imageEl, slideEl)` | Fires when the zoom factor changes |

```js
swiper.on('zoomChange', (swiper, scale, imageEl, slideEl) => {
  console.log('Current zoom:', scale);
  if (scale > 1) {
    slideEl.classList.add('is-zoomed');
  } else {
    slideEl.classList.remove('is-zoomed');
  }
});
```

## Programmatic control

```js
// Zoom to 2x
swiper.zoom.in(2);

// Back to original size
swiper.zoom.out();

// Toggle
document.querySelector('#zoom-btn').addEventListener('click', () => {
  swiper.zoom.toggle();
});

// Display the zoom
document.querySelector('#scale').textContent = swiper.zoom.scale + 'x';
```

## Complete example (photo gallery)

```js
import Swiper from 'swiper';
import { Zoom, Navigation, Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/zoom';
import 'swiper/css/navigation';

const swiper = new Swiper('.gallery-swiper', {
  modules: [Zoom, Navigation, Pagination],
  zoom: {
    maxRatio: 5,
    minRatio: 1,
    toggle: true,
    limitToOriginalSize: false,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
  },
  on: {
    zoomChange: (swiper, scale) => {
      // Hide the navigation while the image is zoomed
      document.querySelector('.swiper-button-next').style.opacity =
        scale > 1 ? '0' : '1';
    },
  },
});
```

---
Source: https://swiperjs.com/swiper-api#zoom
