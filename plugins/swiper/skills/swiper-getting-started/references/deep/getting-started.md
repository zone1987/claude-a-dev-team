# Swiper — Getting Started (vollständige Referenz, v11/12)

## Version

**Swiper v11/12** (aktuelle Stable-Serie). CDN-Beispiele verwenden `@12`.

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

## Import-Varianten

### 1. Core only (kleinste Bundle-Größe)

```js
import Swiper from 'swiper';
import 'swiper/css';

const swiper = new Swiper('.swiper', { loop: true });
```

### 2. Core + ausgewählte Module (empfohlen)

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

### 3. Bundle (alle Module, einfachster Import)

```js
import Swiper from 'swiper/bundle';
import 'swiper/css/bundle';

const swiper = new Swiper('.swiper', { loop: true });
```

### 4. CommonJS (ältere Bundler / Node)

```js
const Swiper = require('swiper');
require('swiper/css');
```

---

## CSS-Import-Pfade (vollständig)

| Import-Pfad | Inhalt |
|---|---|
| `swiper/css` | Core-CSS (Basis, immer nötig) |
| `swiper/css/bundle` | Alle CSS-Module in einem File |
| `swiper/css/navigation` | Navigations-Pfeil-Styles |
| `swiper/css/pagination` | Pagination-Styles (Bullets etc.) |
| `swiper/css/scrollbar` | Scrollbar-Styles |
| `swiper/css/autoplay` | Autoplay-spezifische Styles |
| `swiper/css/effect-fade` | Fade-Effekt-CSS |
| `swiper/css/effect-cube` | Cube-Effekt-CSS |
| `swiper/css/effect-flip` | Flip-Effekt-CSS |
| `swiper/css/effect-coverflow` | Coverflow-Effekt-CSS |
| `swiper/css/effect-creative` | Creative-Effekt-CSS |
| `swiper/css/effect-cards` | Cards-Effekt-CSS |
| `swiper/css/grid` | Grid/Multirow-CSS |
| `swiper/css/thumbs` | Thumbs-CSS |
| `swiper/css/zoom` | Zoom-CSS |
| `swiper/css/free-mode` | Free-Mode-CSS |
| `swiper/css/hash-navigation` | Hash-Navigation-CSS |
| `swiper/css/history` | History-Navigation-CSS |
| `swiper/css/keyboard` | Keyboard-CSS |
| `swiper/css/mousewheel` | Mousewheel-CSS |
| `swiper/css/parallax` | Parallax-CSS |
| `swiper/css/virtual` | Virtual-Slides-CSS |
| `swiper/css/a11y` | Accessibility-CSS |

---

## Module-Import-Pfade

```js
import {
  // Navigation & UI
  Navigation,
  Pagination,
  Scrollbar,

  // Autoplay
  Autoplay,

  // Effekte
  EffectFade,
  EffectCube,
  EffectFlip,
  EffectCoverflow,
  EffectCreative,
  EffectCards,

  // Fortgeschritten
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

### Bundle (einfachste Option)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>

<script>
  const swiper = new Swiper('.swiper', { loop: true });
</script>
```

### ES-Module via CDN

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

## HTML-Struktur (Pflicht)

```html
<!-- Minimale Struktur -->
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
    <div class="swiper-slide">Slide 3</div>
  </div>
</div>
```

```html
<!-- Mit allen optionalen UI-Elementen -->
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
/* CSS-Sizing ist erforderlich */
.swiper {
  width: 100%;
  height: 300px;
}
```

---

## Erste Instanz

```js
// Selector-String
const swiper = new Swiper('.swiper', { /* options */ });

// HTMLElement direkt
const el = document.querySelector('.swiper');
const swiper = new Swiper(el, { /* options */ });
```

---

## Vollständiges Beispiel (npm + Module)

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
<!-- Kein JS nötig, custom element -->
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

## Framework-Integration

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
// app.module.ts / app.config.ts: importiere SwiperModule aus swiper/angular
import { SwiperModule } from 'swiper/angular';
```

---

## Globale Module-Registrierung (Legacy-API, v7 und älter)

```js
// Nicht mehr empfohlen ab v8 — stattdessen modules: [...] im Konstruktor
import Swiper, { Navigation, Pagination } from 'swiper';
Swiper.use([Navigation, Pagination]);
```

---

*Quelle: https://swiperjs.com/get-started | https://swiperjs.com/swiper-api*
