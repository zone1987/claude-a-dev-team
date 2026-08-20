# Swiper Controller module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [Bidirectional synchronization](#bidirectional-synchronization)
- [Multiple controlled Swipers](#multiple-controlled-swipers)
- [Inverse control](#inverse-control)
- [Complete example (linked sliders)](#complete-example-linked-sliders)

## Concept

The Controller module synchronizes two or more Swiper instances with each other. When one is navigated, the other follows. Supports unidirectional and bidirectional control.

## Import and activation

```js
import Swiper from 'swiper';
import { Controller } from 'swiper/modules';

const swiper1 = new Swiper('.swiper-1', {
  modules: [Controller],
});

const swiper2 = new Swiper('.swiper-2', {
  modules: [Controller],
  controller: {
    control: swiper1,
    inverse: false,
    by: 'slide',
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `control` | `Swiper \| Swiper[] \| null` | `null` | Controlled Swiper instance(s) |
| `inverse` | `boolean` | `false` | Opposite direction: with `true`, forward control moves the other one backward |
| `by` | `'slide' \| 'container'` | `'slide'` | Sync by slide index (`'slide'`) or by translate progress (`'container'`) |

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.controller.control` | `Swiper \| Swiper[]` | Reference to the controlled instance(s) — can be set afterwards |

## Methods

| Method | Signature | Description |
|---------|---------|--------------|
| `swiper.controller.setTranslate(translate, byController)` | `(translate: number, byController: Swiper) => void` | Synchronize the translate value |
| `swiper.controller.setTransition(transition, byController)` | `(transition: number, byController: Swiper) => void` | Synchronize the transition duration |

## Events

| Event | Arguments | Description |
|-------|-----------|--------------|
| `controllerUpdate` | `(swiper)` | Controller synchronization was updated |

## Bidirectional synchronization

```js
import Swiper from 'swiper';
import { Controller } from 'swiper/modules';

const swiperA = new Swiper('.swiper-a', {
  modules: [Controller],
  slidesPerView: 1,
});

const swiperB = new Swiper('.swiper-b', {
  modules: [Controller],
  slidesPerView: 1,
});

// Connect bidirectionally after creation
swiperA.controller.control = swiperB;
swiperB.controller.control = swiperA;
```

## Multiple controlled Swipers

```js
const master = new Swiper('.master', {
  modules: [Controller],
});

const slave1 = new Swiper('.slave-1', { modules: [Controller] });
const slave2 = new Swiper('.slave-2', { modules: [Controller] });

// Master controls both slaves
master.controller.control = [slave1, slave2];
```

## Inverse control

```js
// Gallery forward -> thumbs scroll backward
const gallery = new Swiper('.gallery', {
  modules: [Controller],
  controller: {
    control: thumbs,
    inverse: true,
  },
});
```

## Complete example (linked sliders)

```js
import Swiper from 'swiper';
import { Controller, Pagination } from 'swiper/modules';

const textSwiper = new Swiper('.text-swiper', {
  modules: [Controller, Pagination],
  slidesPerView: 1,
  spaceBetween: 0,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  on: {
    controllerUpdate: (swiper) => {
      console.log('Sync updated');
    },
  },
});

const imageSwiper = new Swiper('.image-swiper', {
  modules: [Controller],
  slidesPerView: 1,
  effect: 'fade',
  speed: 800,
});

// Connect bidirectionally
textSwiper.controller.control = imageSwiper;
imageSwiper.controller.control = textSwiper;
```

---
Source: https://swiperjs.com/swiper-api#controller
