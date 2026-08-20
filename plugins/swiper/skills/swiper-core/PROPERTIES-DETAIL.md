# Swiper — Complete properties reference (v11/12)

All properties are available on the Swiper instance. Most are read-only; `allowSlideNext`, `allowSlidePrev` and `allowTouchMove` are read-write.

```js
const swiper = new Swiper('.swiper', { ... });
console.log(swiper.activeIndex);  // current slide index
```

---

## Contents

- [1. Core properties](#1-core-properties)
- [2. Navigation properties](#2-navigation-properties)
- [3. Pagination properties](#3-pagination-properties)
- [4. Scrollbar properties](#4-scrollbar-properties)
- [5. Autoplay properties](#5-autoplay-properties)
- [6. Thumbs properties](#6-thumbs-properties)
- [7. Zoom properties](#7-zoom-properties)
- [8. Keyboard properties](#8-keyboard-properties)
- [9. Mousewheel properties](#9-mousewheel-properties)
- [Usage examples](#usage-examples)

## 1. Core properties

| Property | Type | Description |
|---|---|---|
| `activeIndex` | `number` | Index of the currently active slide. In loop mode it includes the cloned slides; use `realIndex` for the "real" index. |
| `allowSlideNext` | `boolean` | Controls whether moving to the next slide is possible. Read-write: `swiper.allowSlideNext = false`. |
| `allowSlidePrev` | `boolean` | Controls whether moving to the previous slide is possible. Read-write. |
| `allowTouchMove` | `boolean` | Controls whether touch/mouse swipe gestures are possible. Read-write. |
| `animating` | `boolean` | `true` while Swiper is in a transition. |
| `clickedIndex` | `number` | Index of the last clicked slide. |
| `clickedSlide` | `HTMLElement` | HTMLElement of the last clicked slide. |
| `defaults` | `SwiperOptions` | Global default options (static). |
| `el` | `HTMLElement` | Container HTMLElement of the slider. |
| `enabled` | `boolean` | `true` when Swiper is enabled. |
| `extendedDefaults` | `SwiperOptions` | Object with the globally extended Swiper options. |
| `height` | `number` | Current height of the container in px. |
| `isBeginning` | `boolean` | `true` when Swiper is at the far left/top. |
| `isEnd` | `boolean` | `true` when Swiper is at the far right/bottom. |
| `isLocked` | `boolean` | `true` when Swiper is locked (too few slides for `slidesPerView`). |
| `originalParams` | `SwiperOptions` | Original initialization parameters (unmodified object). |
| `params` | `SwiperOptions` | Active configuration (may differ due to breakpoints). |
| `previousIndex` | `number` | Index of the previously active slide. |
| `progress` | `number` | Progress of the wrapper translate, from 0 (beginning) to 1 (end). |
| `realIndex` | `number` | Index of the active slide with cloned loop slides discounted. Identical to `activeIndex` outside loop mode. |
| `slides` | `HTMLElement[]` | Array of all slide HTMLElements. |
| `slidesEl` | `HTMLElement` | Wrapper HTMLElement (identical to `wrapperEl`). |
| `slidesGrid` | `number[]` | Array of the calculated positions of every slide. |
| `slidesSizesGrid` | `number[]` | Array of the widths (horizontal) or heights (vertical) of every slide in px. |
| `snapGrid` | `number[]` | Snap points of the slider. |
| `snapIndex` | `number` | Index of the current snap point in `snapGrid`. |
| `swipeDirection` | `'next' \| 'prev' \| undefined` | Current swipe direction. |
| `touches` | `object` | Object with touch event values: `startX`, `startY`, `currentX`, `currentY`, `diff`. |
| `translate` | `number` | Current translate value of the wrapper in px (negative when sliding left normally). |
| `width` | `number` | Current width of the container in px. |
| `wrapperEl` | `HTMLElement` | Wrapper HTMLElement (the element with the `swiper-wrapper` class). |

---

## 2. Navigation properties

| Property | Type | Description |
|---|---|---|
| `swiper.navigation.nextEl` | `HTMLElement` | HTMLElement of the next button. |
| `swiper.navigation.prevEl` | `HTMLElement` | HTMLElement of the previous button. |

---

## 3. Pagination properties

| Property | Type | Description |
|---|---|---|
| `swiper.pagination.bullets` | `HTMLElement[]` | Array of all pagination bullet HTMLElements. |
| `swiper.pagination.el` | `HTMLElement` | HTMLElement of the pagination container. |

---

## 4. Scrollbar properties

| Property | Type | Description |
|---|---|---|
| `swiper.scrollbar.dragEl` | `HTMLElement` | HTMLElement of the draggable scrollbar handle. |
| `swiper.scrollbar.el` | `HTMLElement` | HTMLElement of the scrollbar container. |

---

## 5. Autoplay properties

| Property | Type | Description |
|---|---|---|
| `swiper.autoplay.paused` | `boolean` | `true` when autoplay is paused. |
| `swiper.autoplay.running` | `boolean` | `true` when autoplay is enabled and running. |
| `swiper.autoplay.timeLeft` | `number` | When paused: remaining time in ms until the next transition. |

---

## 6. Thumbs properties

| Property | Type | Description |
|---|---|---|
| `swiper.thumbs.swiper` | `Swiper` | Swiper instance of the thumbs Swiper. |

---

## 7. Zoom properties

| Property | Type | Description |
|---|---|---|
| `swiper.zoom.enabled` | `boolean` | `true` when the Zoom module is enabled. |
| `swiper.zoom.scale` | `number` | Current zoom factor of the image. |

---

## 8. Keyboard properties

| Property | Type | Description |
|---|---|---|
| `swiper.keyboard.enabled` | `boolean` | `true` when keyboard control is enabled. |

---

## 9. Mousewheel properties

| Property | Type | Description |
|---|---|---|
| `swiper.mousewheel.enabled` | `boolean` | `true` when mouse wheel control is enabled. |

---

## Usage examples

```js
const swiper = new Swiper('.swiper', { loop: true });

// Indices
console.log(swiper.activeIndex);    // e.g. 3 (including cloned loop slides)
console.log(swiper.realIndex);      // e.g. 1 (real index without clones)
console.log(swiper.previousIndex);  // last active index

// Boundary checks
if (swiper.isBeginning) console.log('First slide');
if (swiper.isEnd) console.log('Last slide');
if (swiper.isLocked) console.log('Not enough slides to swipe');

// Geometry
console.log(swiper.width, swiper.height);       // container dimensions
console.log(swiper.translate);                   // current wrapper offset
console.log(swiper.progress);                    // 0..1
console.log(swiper.slides.length);               // number of slides (incl. clones)

// DOM access
swiper.el.classList.add('active');
swiper.wrapperEl.style.transitionDuration = '0ms';
swiper.slides[swiper.activeIndex].style.opacity = '1';

// Grid data
console.log(swiper.slidesGrid);      // [0, 320, 640, ...]
console.log(swiper.slidesSizesGrid); // [310, 310, 310, ...]
console.log(swiper.snapGrid);        // snap points

// Touch data
swiper.on('touchMove', (s, e) => {
  console.log('touchStart X:', s.touches.startX);
  console.log('current X:',    s.touches.currentX);
  console.log('diff:',         s.touches.diff);
});

// Determine direction
swiper.on('sliderMove', (s) => {
  console.log('swiping:', s.swipeDirection); // 'next' or 'prev'
});

// Dynamic control
swiper.allowSlideNext = false;  // lock forward
swiper.allowSlidePrev = false;  // lock backward
swiper.allowTouchMove = false;  // disable touch

// Autoplay state
if (swiper.autoplay.running) {
  console.log('running, next slide in', swiper.autoplay.timeLeft, 'ms');
}

// Zoom
console.log('zoom factor:', swiper.zoom.scale);

// Active parameters (possibly changed by breakpoints)
console.log('slidesPerView:', swiper.params.slidesPerView);
```

---

*Source: https://swiperjs.com/swiper-api*
