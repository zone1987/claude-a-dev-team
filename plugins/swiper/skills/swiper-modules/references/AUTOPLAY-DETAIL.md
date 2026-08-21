# Swiper Autoplay module — Complete reference

## Contents

- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Per-slide override](#per-slide-override)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [Complete example](#complete-example)

## Import and activation

```js
import Swiper from 'swiper';
import { Autoplay } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Autoplay],
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `delay` | `number` | `3000` | Pause between slide transitions in milliseconds |
| `disableOnInteraction` | `boolean` | `true` | `false` = restart autoplay after user interaction instead of stopping it |
| `pauseOnMouseEnter` | `boolean` | `false` | Pause autoplay when the pointer enters the container |
| `reverseDirection` | `boolean` | `false` | Run autoplay in the reverse direction |
| `stopOnLastSlide` | `boolean` | `false` | Stop autoplay on the last slide (no effect in loop mode) |
| `waitForTransition` | `boolean` | `true` | Wait until the wrapper transition has finished |

## Per-slide override

An individual slide can define its own delay:

```html
<div class="swiper-slide" data-swiper-autoplay="5000">
  This slide stays for 5 seconds
</div>
```

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `swiper.autoplay.running` | `boolean` | Autoplay is currently running |
| `swiper.autoplay.paused` | `boolean` | Autoplay is paused |
| `swiper.autoplay.timeLeft` | `number` | Remaining time in ms until the next transition |

## Methods

| Method | Description |
|--------|-------------|
| `swiper.autoplay.start()` | Start autoplay |
| `swiper.autoplay.stop()` | Stop autoplay completely |
| `swiper.autoplay.pause()` | Pause autoplay (can be resumed) |
| `swiper.autoplay.resume()` | Resume paused autoplay |

## Events

| Event | Arguments | Description |
|-------|-----------|-------------|
| `autoplay` | `(swiper)` | Fires when autoplay triggers a slide change |
| `autoplayStart` | `(swiper)` | Autoplay was started |
| `autoplayStop` | `(swiper)` | Autoplay was stopped |
| `autoplayPause` | `(swiper)` | Autoplay was paused |
| `autoplayResume` | `(swiper)` | Autoplay was resumed |
| `autoplayTimeLeft` | `(swiper, timeLeft, percentage)` | Continuous event with the remaining time and percentage (0..1) |

### autoplayTimeLeft for a progress indicator

```js
swiper.on('autoplayTimeLeft', (swiper, timeLeft, percentage) => {
  // timeLeft: ms until the next transition
  // percentage: 0 = start, 1 = end of the delay
  progressBar.style.setProperty('--progress', 1 - percentage);
});
```

## Complete example

```js
const swiper = new Swiper('.swiper', {
  modules: [Autoplay],
  loop: true,
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
    reverseDirection: false,
    waitForTransition: true,
  },
  on: {
    autoplayStart: () => console.log('started'),
    autoplayStop: () => console.log('stopped'),
    autoplayTimeLeft: (s, time, progress) => {
      document.querySelector('.timer').textContent =
        Math.ceil(time / 1000) + 's';
    },
  },
});

// External control
document.querySelector('#pause-btn').addEventListener('click', () => {
  swiper.autoplay.pause();
});
document.querySelector('#play-btn').addEventListener('click', () => {
  swiper.autoplay.resume();
});
```

---
Source: https://swiperjs.com/swiper-api#autoplay
