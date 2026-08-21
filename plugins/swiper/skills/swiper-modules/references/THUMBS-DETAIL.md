# Swiper Thumbs module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Properties](#properties)
- [Methods](#methods)
- [HTML structure](#html-structure)
- [CSS for the active thumbnail](#css-for-the-active-thumbnail)
- [Thumbs via configuration object (without a separate instance)](#thumbs-via-configuration-object-without-a-separate-instance)
- [Complete gallery example](#complete-gallery-example)

## Concept

The Thumbs module synchronizes a thumbnail Swiper with a main Swiper. The thumbnail Swiper shows small preview images; activating a thumbnail switches the main slider.

## Import and activation

```js
import Swiper from 'swiper';
import { Thumbs, Navigation } from 'swiper/modules';

// Create the thumbs Swiper first
const thumbsSwiper = new Swiper('.swiper-thumbs', {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,  // Important for correct synchronization!
});

// Then the main Swiper with the thumbs configuration
const mainSwiper = new Swiper('.swiper-main', {
  modules: [Thumbs, Navigation],
  spaceBetween: 10,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  thumbs: {
    swiper: thumbsSwiper,
    multipleActiveThumbs: false,
    autoScrollOffset: 0,
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `swiper` | `Swiper \| SwiperOptions \| null` | `null` | Thumbs Swiper instance or configuration object |
| `multipleActiveThumbs` | `boolean` | `true` | Mark multiple thumbnails as active at once (when `slidesPerView > 1`) |
| `autoScrollOffset` | `number` | `0` | How many slides from the edge the active thumbnail is automatically scrolled into the visible area |
| `slideThumbActiveClass` | `string` | `'swiper-slide-thumb-active'` | CSS class for the active thumbnail slide |
| `thumbsContainerClass` | `string` | `'swiper-thumbs'` | CSS class for the thumbs container |

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.thumbs.swiper` | `Swiper` | Reference to the thumbs Swiper instance |

## Methods

| Method | Signature | Description |
|---------|---------|--------------|
| `swiper.thumbs.init()` | `() => void` | Initialize the Thumbs module |
| `swiper.thumbs.update(initial?, position?)` | `(initial?: boolean, position?: string) => void` | Update the thumbs state |

## HTML structure

```html
<!-- Main Swiper -->
<div class="swiper-main">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <img src="image1-full.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image2-full.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image3-full.jpg" />
    </div>
  </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>

<!-- Thumbs Swiper -->
<div class="swiper-thumbs">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <img src="image1-thumb.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image2-thumb.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image3-thumb.jpg" />
    </div>
  </div>
</div>
```

## CSS for the active thumbnail

```css
.swiper-thumbs .swiper-slide {
  opacity: 0.4;
  cursor: pointer;
  transition: opacity 0.3s;
}

.swiper-thumbs .swiper-slide-thumb-active {
  opacity: 1;
}
```

## Thumbs via configuration object (without a separate instance)

```js
const mainSwiper = new Swiper('.swiper-main', {
  modules: [Thumbs],
  thumbs: {
    swiper: {
      el: '.swiper-thumbs',
      spaceBetween: 10,
      slidesPerView: 4,
      watchSlidesProgress: true,
    },
  },
});
```

## Complete gallery example

```js
import Swiper from 'swiper';
import { Thumbs, Navigation, Keyboard } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';

const thumbsSwiper = new Swiper('.gallery-thumbs', {
  slidesPerView: 'auto',
  spaceBetween: 8,
  centeredSlides: true,
  slideToClickedSlide: true,
  watchSlidesProgress: true,
});

const gallerySwiper = new Swiper('.gallery-main', {
  modules: [Thumbs, Navigation, Keyboard],
  spaceBetween: 16,
  keyboard: { enabled: true },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  thumbs: {
    swiper: thumbsSwiper,
    multipleActiveThumbs: false,
    autoScrollOffset: 2,
  },
});
```

---
Source: https://swiperjs.com/swiper-api#thumbs
