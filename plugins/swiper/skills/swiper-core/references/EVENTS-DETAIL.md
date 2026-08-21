# Swiper — Complete event reference (v11/12)

Register events with `swiper.on(event, handler)`, `swiper.once(event, handler)`, or directly in the constructor via `on: { eventName: handler }`.

```js
// In the constructor
const swiper = new Swiper('.swiper', {
  on: {
    init(swiper) { /* ... */ },
    slideChange(swiper) { /* ... */ },
  }
});

// After initialization
swiper.on('slideChange', (swiper) => console.log(swiper.activeIndex));
swiper.once('transitionEnd', (swiper) => console.log('only once'));
swiper.onAny((eventName, ...args) => console.log(eventName, args));
```

---

## Contents

- [1. Core events](#1-core-events)
- [2. Navigation events](#2-navigation-events)
- [3. Pagination events](#3-pagination-events)
- [4. Scrollbar events](#4-scrollbar-events)
- [5. Autoplay events](#5-autoplay-events)
- [6. Keyboard events](#6-keyboard-events)
- [7. Mousewheel events](#7-mousewheel-events)
- [8. Zoom events](#8-zoom-events)
- [Event usage examples](#event-usage-examples)

## 1. Core events

| Event | Arguments | Description |
|---|---|---|
| `activeIndexChange` | `(swiper)` | The active index changed. |
| `afterInit` | `(swiper)` | Right after initialization. |
| `beforeDestroy` | `(swiper)` | Right before Swiper is destroyed. |
| `beforeInit` | `(swiper)` | Right before initialization. |
| `beforeLoopFix` | `(swiper)` | Right before the loop fix. |
| `beforeResize` | `(swiper)` | Before the resize handler. |
| `beforeSlideChangeStart` | `(swiper)` | Before the slide-change transition starts. |
| `beforeTransitionStart` | `(swiper, speed, internal)` | Before a transition starts. `speed`: transition duration, `internal`: internal call. |
| `breakpoint` | `(swiper, breakpointParams)` | The breakpoint changed. `breakpointParams`: new parameters. |
| `changeDirection` | `(swiper)` | The direction changed. |
| `click` | `(swiper, event)` | The user clicks/taps Swiper. `event`: PointerEvent. |
| `destroy` | `(swiper)` | Swiper is destroyed. |
| `doubleClick` | `(swiper, event)` | Double click on Swiper. `event`: PointerEvent. |
| `doubleTap` | `(swiper, event)` | Double tap on the container. `event`: PointerEvent. |
| `fromEdge` | `(swiper)` | Swiper leaves an edge position. |
| `init` | `(swiper)` | Right after initialization (after `afterInit`). |
| `lock` | `(swiper)` | Swiper is locked (too few slides). |
| `loopFix` | `(swiper)` | After the loop fix. |
| `momentumBounce` | `(swiper)` | Momentum bounce triggered. |
| `observerUpdate` | `(swiper)` | The observer detected DOM mutations. |
| `orientationchange` | `(swiper)` | The device orientation changed. |
| `progress` | `(swiper, progress)` | The wrapper progress changed. `progress`: current progress (0–1). |
| `reachBeginning` | `(swiper)` | Swiper reached the beginning. |
| `reachEnd` | `(swiper)` | Swiper reached the last slide. |
| `realIndexChange` | `(swiper)` | The real index changed. |
| `resize` | `(swiper)` | The window size changed. |
| `setTransition` | `(swiper, transition)` | A Swiper animation starts. `transition`: transition duration. |
| `setTranslate` | `(swiper, translate)` | The wrapper changes its position. `translate`: current translate value. |
| `slideChange` | `(swiper)` | The active slide changed. |
| `slideChangeTransitionEnd` | `(swiper)` | The animation after a slide change finished. |
| `slideChangeTransitionStart` | `(swiper)` | The animation for a slide change begins. |
| `slideNextTransitionEnd` | `(swiper)` | Like `slideChangeTransitionEnd`, forward direction only. |
| `slideNextTransitionStart` | `(swiper)` | Like `slideChangeTransitionStart`, forward direction only. |
| `slidePrevTransitionEnd` | `(swiper)` | Like `slideChangeTransitionEnd`, backward direction only. |
| `slidePrevTransitionStart` | `(swiper)` | Like `slideChangeTransitionStart`, backward direction only. |
| `slideResetTransitionEnd` | `(swiper)` | The reset animation finished. |
| `slideResetTransitionStart` | `(swiper)` | The reset animation begins. |
| `sliderFirstMove` | `(swiper, event)` | First touch/drag movement. `event`: PointerEvent. |
| `sliderMove` | `(swiper, event)` | The user touches and moves the finger. `event`: PointerEvent. |
| `slidesGridLengthChange` | `(swiper)` | The slides grid changed. |
| `slidesLengthChange` | `(swiper)` | The number of slides changed. |
| `slidesUpdated` | `(swiper)` | Slides were calculated and updated. |
| `snapGridLengthChange` | `(swiper)` | The snap grid changed. |
| `snapIndexChange` | `(swiper)` | The snap index changed. |
| `tap` | `(swiper, event)` | The user taps Swiper (not a double tap). `event`: PointerEvent. |
| `toEdge` | `(swiper)` | Swiper reaches an edge position. |
| `touchEnd` | `(swiper, event)` | The user releases Swiper. `event`: PointerEvent. |
| `touchMove` | `(swiper, event)` | The user touches and moves the finger. `event`: PointerEvent. |
| `touchMoveOpposite` | `(swiper, event)` | Movement against the slider direction. `event`: PointerEvent. |
| `touchStart` | `(swiper, event)` | The user touches Swiper. `event`: PointerEvent. |
| `transitionEnd` | `(swiper)` | The transition finished. |
| `transitionStart` | `(swiper)` | The transition begins. |
| `unlock` | `(swiper)` | Swiper is unlocked. |
| `update` | `(swiper)` | `swiper.update()` was called. |

---

## 2. Navigation events

| Event | Arguments | Description |
|---|---|---|
| `navigationHide` | `(swiper)` | The navigation is hidden. |
| `navigationNext` | `(swiper)` | The next button was clicked. |
| `navigationPrev` | `(swiper)` | The previous button was clicked. |
| `navigationShow` | `(swiper)` | The navigation is shown. |

---

## 3. Pagination events

| Event | Arguments | Description |
|---|---|---|
| `paginationHide` | `(swiper)` | The pagination is hidden. |
| `paginationRender` | `(swiper, paginationEl)` | The pagination was rendered. `paginationEl`: HTMLElement. |
| `paginationShow` | `(swiper)` | The pagination is shown. |
| `paginationUpdate` | `(swiper, paginationEl)` | The pagination was updated. `paginationEl`: HTMLElement. |

---

## 4. Scrollbar events

| Event | Arguments | Description |
|---|---|---|
| `scrollbarDragEnd` | `(swiper, event)` | Scrollbar drag ended. `event`: PointerEvent. |
| `scrollbarDragMove` | `(swiper, event)` | The scrollbar is being dragged. `event`: PointerEvent. |
| `scrollbarDragStart` | `(swiper, event)` | Scrollbar drag started. `event`: PointerEvent. |

---

## 5. Autoplay events

| Event | Arguments | Description |
|---|---|---|
| `autoplay` | `(swiper)` | Autoplay changed the slide. |
| `autoplayPause` | `(swiper)` | Autoplay was paused. |
| `autoplayResume` | `(swiper)` | Autoplay was resumed. |
| `autoplayStart` | `(swiper)` | Autoplay was started. |
| `autoplayStop` | `(swiper)` | Autoplay was stopped. |
| `autoplayTimeLeft` | `(swiper, timeLeft, percentage)` | Fires during the autoplay countdown. `timeLeft`: ms until the next slide, `percentage`: 0–1 progress. |

```js
// Autoplay progress indicator
swiper.on('autoplayTimeLeft', (s, timeLeft, percentage) => {
  progressCircle.style.setProperty('--progress', 1 - percentage);
  progressContent.textContent = `${Math.ceil(timeLeft / 1000)}s`;
});
```

---

## 6. Keyboard events

| Event | Arguments | Description |
|---|---|---|
| `keyPress` | `(swiper, keyCode)` | A key was pressed. `keyCode`: KeyboardEvent.keyCode. |

---

## 7. Mousewheel events

| Event | Arguments | Description |
|---|---|---|
| `scroll` | `(swiper, event)` | A mouse wheel scroll event fired. `event`: WheelEvent. |

---

## 8. Zoom events

| Event | Arguments | Description |
|---|---|---|
| `zoomChange` | `(swiper, scale, imageEl, slideEl)` | The zoom level changed. `scale`: current zoom factor, `imageEl`: image element, `slideEl`: slide element. |

---

## Event usage examples

```js
// Lifecycle tracking
const swiper = new Swiper('.swiper', {
  on: {
    beforeInit(s) {
      console.log('before init');
    },
    init(s) {
      console.log('initialized, activeIndex:', s.activeIndex);
    },
    afterInit(s) {
      console.log('after init');
    },
  }
});

// Slide change
swiper.on('slideChange', (s) => {
  console.log('active slide:', s.activeIndex, 'realIndex:', s.realIndex);
});

// Edge detection
swiper.on('reachBeginning', () => console.log('first slide'));
swiper.on('reachEnd', () => console.log('last slide'));
swiper.on('toEdge', () => console.log('edge reached'));
swiper.on('fromEdge', () => console.log('edge left'));

// Touch events
swiper.on('touchStart', (s, event) => console.log('touch start', event.touches[0]));
swiper.on('touchMove', (s, event) => console.log('touch move'));
swiper.on('touchEnd', (s, event) => console.log('touch end'));

// Transition
swiper.on('transitionStart', () => console.log('transition start'));
swiper.on('transitionEnd', () => console.log('transition end'));
swiper.on('slideChangeTransitionStart', () => console.log('slide change start'));
swiper.on('slideChangeTransitionEnd', () => console.log('slide change end'));

// Progress
swiper.on('progress', (s, progress) => {
  console.log('progress:', Math.round(progress * 100), '%');
});

// Breakpoint
swiper.on('breakpoint', (s, params) => {
  console.log('new breakpoint, params:', params);
});

// Lazy loading
swiper.on('lazyImageReady', (s, slideEl, imageEl) => {
  console.log('image loaded:', imageEl.src);
});

// Resize
swiper.on('resize', (s) => {
  console.log('container size changed, width:', s.width);
});

// Observer
swiper.on('observerUpdate', (s) => {
  console.log('DOM mutation detected');
});
```

---

*Source: https://swiperjs.com/swiper-api*
