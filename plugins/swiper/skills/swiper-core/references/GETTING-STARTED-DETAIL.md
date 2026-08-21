# Swiper — Getting Started (complete reference, v11/12)

## Contents

- [Version](#version)
- [Installation](#installation)
- [Import variants](#import-variants)
- [CSS import paths (complete)](#css-import-paths-complete)
- [Module import paths](#module-import-paths)
- [CDN — jsDelivr](#cdn-jsdelivr)
- [HTML structure (required)](#html-structure-required)
- [First instance](#first-instance)
- [Complete example (npm + modules)](#complete-example-npm-modules)
- [Swiper Element (Web Component)](#swiper-element-web-component)
- [Framework integration](#framework-integration)
- [Global module registration (legacy API, v7 and older)](#global-module-registration-legacy-api-v7-and-older)

## Version

**Swiper v11/12** (current stable series). CDN examples use `@12`.

---

## Installation

### npm

```bash
npm install swiper
```

### yarn / pnpm / bun

```bash
yarn add swiper
pnpm add swiper
bun add swiper
```

---

## Import variants

### 1. Core only (smallest bundle size)

```js
import Swiper from 'swiper';
import 'swiper/css';

const swiper = new Swiper('.swiper', { loop: true });
```

### 2. Core + selected modules (recommended)

```js
import Swiper from 'swiper';
import { Navigation, Pagination, Autoplay, Scrollbar, EffectFade } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-fade';

const swiper = new Swiper('.swiper', {
  modules: [Navigation, Pagination, Autoplay, Scrollbar, EffectFade],
  navigation: true,
  pagination: { el: '.swiper-pagination', clickable: true },
});
```

### 3. Bundle (all modules, simplest import)

```js
import Swiper from 'swiper/bundle';
import 'swiper/css/bundle';

const swiper = new Swiper('.swiper', { loop: true });
```

### 4. CommonJS (older bundlers / Node)

```js
const Swiper = require('swiper');
require('swiper/css');
```

---

## CSS import paths (complete)

| Import path | Contents |
|---|---|
| `swiper/css` | Core CSS (base, always required) |
| `swiper/css/bundle` | All CSS modules in one file |
| `swiper/css/navigation` | Navigation arrow styles |
| `swiper/css/pagination` | Pagination styles (bullets etc.) |
| `swiper/css/scrollbar` | Scrollbar styles |
| `swiper/css/autoplay` | Autoplay-specific styles |
| `swiper/css/effect-fade` | Fade effect CSS |
| `swiper/css/effect-cube` | Cube effect CSS |
| `swiper/css/effect-flip` | Flip effect CSS |
| `swiper/css/effect-coverflow` | Coverflow effect CSS |
| `swiper/css/effect-creative` | Creative effect CSS |
| `swiper/css/effect-cards` | Cards effect CSS |
| `swiper/css/grid` | Grid/multirow CSS |
| `swiper/css/thumbs` | Thumbs CSS |
| `swiper/css/zoom` | Zoom CSS |
| `swiper/css/free-mode` | Free mode CSS |
| `swiper/css/hash-navigation` | Hash navigation CSS |
| `swiper/css/history` | History navigation CSS |
| `swiper/css/keyboard` | Keyboard CSS |
| `swiper/css/mousewheel` | Mousewheel CSS |
| `swiper/css/parallax` | Parallax CSS |
| `swiper/css/virtual` | Virtual slides CSS |
| `swiper/css/a11y` | Accessibility CSS |

---

## Module import paths

```js
import {
  // Navigation & UI
  Navigation,
  Pagination,
  Scrollbar,

  // Autoplay
  Autoplay,

  // Effects
  EffectFade,
  EffectCube,
  EffectFlip,
  EffectCoverflow,
  EffectCreative,
  EffectCards,

  // Advanced
  FreeMode,
  Grid,
  Thumbs,
  Zoom,
  Virtual,
  Keyboard,
  Mousewheel,
  Parallax,
  HashNavigation,
  History,
  A11y,
  Manipulation,
} from 'swiper/modules';
```

---

## CDN — jsDelivr

### Bundle (simplest option)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>

<script>
  const swiper = new Swiper('.swiper', { loop: true });
</script>
```

### ES modules via CDN

```html
<script type="module">
  import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.mjs';
  const swiper = new Swiper('.swiper', { loop: true });
</script>
```

### Unpkg

```html
<link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css">
<script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
```

---

## HTML structure (required)

```html
<!-- Minimal structure -->
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
    <div class="swiper-slide">Slide 3</div>
  </div>
</div>
```

```html
<!-- With all optional UI elements -->
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
    <div class="swiper-slide">Slide 3</div>
  </div>

  <!-- Pagination -->
  <div class="swiper-pagination"></div>

  <!-- Navigation -->
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>

  <!-- Scrollbar -->
  <div class="swiper-scrollbar"></div>
</div>
```

```css
/* CSS sizing is required */
.swiper {
  width: 100%;
  height: 300px;
}
```

---

## First instance

```js
// Selector string
const swiper = new Swiper('.swiper', { /* options */ });

// HTMLElement directly
const el = document.querySelector('.swiper');
const swiper = new Swiper(el, { /* options */ });
```

---

## Complete example (npm + modules)

```js
import Swiper from 'swiper';
import { Navigation, Pagination, Autoplay, EffectFade } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/effect-fade';

const swiper = new Swiper('.swiper', {
  modules: [Navigation, Pagination, Autoplay, EffectFade],
  direction: 'horizontal',
  loop: true,
  effect: 'fade',
  speed: 600,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
```

---

## Swiper Element (Web Component)

```html
<!-- No JS needed, custom element -->
<script type="module">
  import { register } from 'swiper/element/bundle';
  register();
</script>

<swiper-container slides-per-view="3" space-between="30" loop="true">
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <swiper-slide>Slide 3</swiper-slide>
</swiper-container>
```

---

## Framework integration

### React

```jsx
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';

export default function MySwiper() {
  return (
    <Swiper modules={[Navigation]} navigation slidesPerView={3} spaceBetween={20}>
      <SwiperSlide>Slide 1</SwiperSlide>
      <SwiperSlide>Slide 2</SwiperSlide>
    </Swiper>
  );
}
```

### Vue 3

```vue
<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
</script>

<template>
  <Swiper :modules="[Navigation]" :slides-per-view="3" :space-between="20" navigation>
    <SwiperSlide>Slide 1</SwiperSlide>
    <SwiperSlide>Slide 2</SwiperSlide>
  </Swiper>
</template>
```

### Angular

```ts
// app.module.ts / app.config.ts: import SwiperModule from swiper/angular
import { SwiperModule } from 'swiper/angular';
```

---

## Global module registration (legacy API, v7 and older)

```js
// No longer recommended from v8 on — use modules: [...] in the constructor instead
import Swiper, { Navigation, Pagination } from 'swiper';
Swiper.use([Navigation, Pagination]);
```

---

*Source: https://swiperjs.com/get-started | https://swiperjs.com/swiper-api*
