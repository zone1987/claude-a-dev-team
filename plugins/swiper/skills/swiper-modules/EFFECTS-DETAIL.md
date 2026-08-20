# Swiper transition effects — Complete reference

Swiper supports six transition effects. Each effect is imported as a separate module.

## Contents

- [Overview of import names](#overview-of-import-names)
- [1. Fade Effect — `fadeEffect`](#1-fade-effect-fadeeffect)
- [2. Cube Effect — `cubeEffect`](#2-cube-effect-cubeeffect)
- [3. Coverflow Effect — `coverflowEffect`](#3-coverflow-effect-coverfloweffect)
- [4. Flip Effect — `flipEffect`](#4-flip-effect-flipeffect)
- [5. Cards Effect — `cardsEffect`](#5-cards-effect-cardseffect)
- [6. Creative Effect — `creativeEffect`](#6-creative-effect-creativeeffect)

## Overview of import names

| Effect | `effect` value | Module import |
|--------|----------------|---------------|
| Fade | `'fade'` | `EffectFade` |
| Cube | `'cube'` | `EffectCube` |
| Coverflow | `'coverflow'` | `EffectCoverflow` |
| Flip | `'flip'` | `EffectFlip` |
| Cards | `'cards'` | `EffectCards` |
| Creative | `'creative'` | `EffectCreative` |

---

## 1. Fade Effect — `fadeEffect`

**Import name:** `EffectFade`

```js
import Swiper from 'swiper';
import { EffectFade } from 'swiper/modules';
import 'swiper/css/effect-fade';

const swiper = new Swiper('.swiper', {
  modules: [EffectFade],
  effect: 'fade',
  fadeEffect: {
    crossFade: true,
  },
});
```

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `crossFade` | `boolean` | `false` | Enable cross-fade: fade both slides in and out at the same time. `false` = only fade in the active slide. |

**Note:** With `crossFade: false` the previous slide stays visible underneath the new one until the new one has fully faded in.

---

## 2. Cube Effect — `cubeEffect`

**Import name:** `EffectCube`

```js
import Swiper from 'swiper';
import { EffectCube } from 'swiper/modules';
import 'swiper/css/effect-cube';

const swiper = new Swiper('.swiper', {
  modules: [EffectCube],
  effect: 'cube',
  cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
  },
});
```

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `shadow` | `boolean` | `true` | Show the main shadow beneath the cube |
| `shadowOffset` | `number` | `20` | Offset of the main shadow in px |
| `shadowScale` | `number` | `0.94` | Scale factor of the main shadow |
| `slideShadows` | `boolean` | `true` | Show shadows on the cube faces (slides) |

---

## 3. Coverflow Effect — `coverflowEffect`

**Import name:** `EffectCoverflow`

```js
import Swiper from 'swiper';
import { EffectCoverflow } from 'swiper/modules';
import 'swiper/css/effect-coverflow';

const swiper = new Swiper('.swiper', {
  modules: [EffectCoverflow],
  effect: 'coverflow',
  centeredSlides: true,
  slidesPerView: 'auto',
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 1,
    scale: 1,
    slideShadows: true,
  },
});
```

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rotate` | `number` | `50` | Rotation angle of the adjacent slides in degrees |
| `stretch` | `number \| string` | `0` | Additional space between slides in px or % |
| `depth` | `number` | `100` | Z offset of the adjacent slides in px |
| `modifier` | `number` | `1` | Amplification/damping factor for all effects |
| `scale` | `number` | `1` | Scale factor of the adjacent slides (< 1 = smaller) |
| `slideShadows` | `boolean` | `true` | Show shadows on slides |

---

## 4. Flip Effect — `flipEffect`

**Import name:** `EffectFlip`

```js
import Swiper from 'swiper';
import { EffectFlip } from 'swiper/modules';
import 'swiper/css/effect-flip';

const swiper = new Swiper('.swiper', {
  modules: [EffectFlip],
  effect: 'flip',
  flipEffect: {
    slideShadows: true,
    limitRotation: true,
  },
});
```

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `slideShadows` | `boolean` | `true` | Shadows on slides during the flip effect |
| `limitRotation` | `boolean` | `true` | Limit the rotation on the first and last slide |

---

## 5. Cards Effect — `cardsEffect`

**Import name:** `EffectCards`

```js
import Swiper from 'swiper';
import { EffectCards } from 'swiper/modules';
import 'swiper/css/effect-cards';

const swiper = new Swiper('.swiper', {
  modules: [EffectCards],
  effect: 'cards',
  cardsEffect: {
    rotate: true,
    perSlideRotate: 2,
    perSlideOffset: 8,
    slideShadows: true,
  },
});
```

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rotate` | `boolean` | `true` | Enable card rotation |
| `perSlideRotate` | `number` | `2` | Rotation angle per slide step in degrees |
| `perSlideOffset` | `number` | `8` | Offset per slide step in px |
| `slideShadows` | `boolean` | `true` | Show shadows on cards |

---

## 6. Creative Effect — `creativeEffect`

**Import name:** `EffectCreative`

Allows fully custom 3D transformations per slide position.

```js
import Swiper from 'swiper';
import { EffectCreative } from 'swiper/modules';
import 'swiper/css/effect-creative';

const swiper = new Swiper('.swiper', {
  modules: [EffectCreative],
  effect: 'creative',
  creativeEffect: {
    prev: {
      // Previous slides
      shadow: true,
      translate: ['-20%', 0, -1],
    },
    next: {
      // Next slides
      translate: ['100%', 0, 0],
    },
  },
});
```

### Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `prev` | `CreativeEffectTransform` | — | Transform object for slides before the active one |
| `next` | `CreativeEffectTransform` | — | Transform object for slides after the active one |
| `perspective` | `boolean` | `true` | Enable 3D perspective (required for 3D transforms) |
| `progressMultiplier` | `number` | `1` | Amplification factor for the transformation intensity |
| `limitProgress` | `number` | `1` | Number of slides that receive transforms (beyond the active one) |
| `shadowPerProgress` | `boolean` | `false` | Distribute the shadow opacity across multiple slides |

### Transform object schema (`CreativeEffectTransform`)

```ts
interface CreativeEffectTransform {
  translate: [x: string | number, y: string | number, z: string | number];
  rotate?: [x: number, y: number, z: number]; // in degrees
  opacity?: number;   // 0..1
  scale?: number;     // 1 = original size
  shadow?: boolean;   // show shadow
  origin?: string;    // CSS transform-origin, e.g. 'left bottom'
}
```

### Examples of creative effects

```js
// Slide-in effect (classic)
creativeEffect: {
  prev: { translate: [0, 0, -400] },
  next: { translate: ['100%', 0, 0] },
}

// Cross-fade with scaling
creativeEffect: {
  prev: {
    shadow: true,
    translate: ['-125%', 0, -800],
    rotate: [0, 0, -90],
  },
  next: {
    translate: ['125%', 0, -800],
    rotate: [0, 0, 90],
  },
}

// Top to bottom
creativeEffect: {
  prev: {
    shadow: true,
    translate: [0, '-120%', 0],
  },
  next: {
    translate: [0, '120%', 0],
  },
}
```

---
Source: https://swiperjs.com/swiper-api#fade-effect
