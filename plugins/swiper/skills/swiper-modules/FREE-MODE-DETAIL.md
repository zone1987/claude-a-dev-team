# Swiper Free Mode module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Relationship to other parameters](#relationship-to-other-parameters)
- [Configuration examples](#configuration-examples)

## Concept

Free Mode disables snapping to fixed slide positions. The slider scrolls freely and — depending on the configuration — can keep rolling with physical momentum (inertia).

## Import and activation

```js
import Swiper from 'swiper';
import { FreeMode } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: {
    enabled: true,
    momentum: true,
  },
});
```

**Shorthand** (default configuration):
```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: true,
});
```

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `boolean` | `false` | Enable Free Mode |
| `momentum` | `boolean` | `true` | Slides keep rolling after release |
| `momentumRatio` | `number` | `1` | Multiplier for the momentum distance (> 1 = further) |
| `momentumVelocityRatio` | `number` | `1` | Multiplier for the momentum velocity |
| `momentumBounce` | `boolean` | `true` | Enable the bounce effect at the edges |
| `momentumBounceRatio` | `number` | `1` | Strength of the bounce effect (> 1 = stronger) |
| `minimumVelocity` | `number` | `0.02` | Minimum swipe velocity required to trigger momentum |
| `sticky` | `boolean` | `false` | Snap to the nearest slide after release |

## Relationship to other parameters

Free Mode can be combined with the following core parameters:

```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  slidesPerView: 'auto',    // slides at their original size
  spaceBetween: 16,
  freeMode: {
    enabled: true,
    momentum: true,
    momentumRatio: 0.5,     // slower coast-out
  },
});
```

## Configuration examples

### Simple tag cloud slider (horizontal, no momentum)

```js
const swiper = new Swiper('.tags-swiper', {
  modules: [FreeMode],
  slidesPerView: 'auto',
  spaceBetween: 8,
  freeMode: {
    enabled: true,
    momentum: false,
  },
});
```

### Momentum scrolling with sticky snap

```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  slidesPerView: 2.5,
  spaceBetween: 20,
  freeMode: {
    enabled: true,
    sticky: true,         // snaps after release
    momentum: true,
    momentumRatio: 0.8,
    momentumBounce: true,
    momentumBounceRatio: 0.5,
  },
});
```

### High sensitivity without bounce

```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: {
    enabled: true,
    momentum: true,
    momentumRatio: 1.5,
    momentumVelocityRatio: 1.5,
    momentumBounce: false,
    minimumVelocity: 0.05,
  },
});
```

---
Source: https://swiperjs.com/swiper-api#free-mode
