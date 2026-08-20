# Swiper Vue — Complete reference

The Swiper Vue components are officially supported and shipped in `swiper/vue`.
Compatible with Vue 3 (Composition API).

---

## Contents

- [Installation](#installation)
- [Base import](#base-import)
- [Minimal example (Composition API)](#minimal-example-composition-api)
- [Options API example](#options-api-example)
- [`<Swiper>` — props](#swiper-props)
- [Events](#events)
- [`<SwiperSlide>` — props](#swiperslide-props)
- [`v-slot` — slide render props](#v-slot-slide-render-props)
- [Composables](#composables)
- [Slots (content injection)](#slots-content-injection)
- [Including modules](#including-modules)
- [Virtual Slides](#virtual-slides)
- [Controller (synchronized Swipers)](#controller-synchronized-swipers)
- [Thumbs (thumbnails)](#thumbs-thumbnails)
- [Effects](#effects)
- [CSS import reference](#css-import-reference)

## Installation

```bash
npm install swiper
```

---

## Base import

```javascript
import { Swiper, SwiperSlide } from 'swiper/vue';

// Core CSS (always required)
import 'swiper/css';

// Module-specific CSS
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-fade';
import 'swiper/css/effect-cube';
import 'swiper/css/effect-coverflow';
import 'swiper/css/effect-flip';
import 'swiper/css/effect-cards';
import 'swiper/css/effect-creative';
import 'swiper/css/thumbs';
import 'swiper/css/free-mode';
import 'swiper/css/grid';
import 'swiper/css/zoom';

// Or everything at once
import 'swiper/css/bundle';
```

---

## Minimal example (Composition API)

```vue
<template>
  <swiper
    :slides-per-view="3"
    :space-between="50"
    @swiper="onSwiper"
    @slideChange="onSlideChange"
  >
    <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide>
    <swiper-slide>Slide 3</swiper-slide>
  </swiper>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';

const onSwiper = (swiper) => {
  console.log('Swiper instance:', swiper);
};
const onSlideChange = () => {
  console.log('Slide changed');
};
</script>
```

---

## Options API example

```vue
<template>
  <swiper
    :slides-per-view="3"
    :space-between="50"
    @swiper="onSwiper"
    @slideChange="onSlideChange"
  >
    <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide>
  </swiper>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';

export default {
  components: { Swiper, SwiperSlide },
  setup() {
    const onSwiper = (swiper) => console.log(swiper);
    const onSlideChange = () => console.log('slide change');
    return { onSwiper, onSlideChange };
  },
};
</script>
```

---

## `<Swiper>` — props

All [Swiper API parameters](https://swiperjs.com/swiper-api#parameters) are available as props (camelCase or kebab-case in templates).

### Additional Vue-specific props

| Prop | Type | Default | Description |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML element of the container |
| `wrapperTag` | `string` | `'div'` | HTML element of the wrapper |
| `modules` | `SwiperModule[]` | — | Modules to include |

### Common parameter examples

```vue
<swiper
  :slides-per-view="1"
  :space-between="10"
  :speed="400"
  :loop="true"
  :centered-slides="true"
  direction="horizontal"
  :breakpoints="{
    640: { slidesPerView: 2, spaceBetween: 20 },
    768: { slidesPerView: 3, spaceBetween: 30 },
    1024: { slidesPerView: 4, spaceBetween: 40 },
  }"
  :autoplay="{ delay: 2500, disableOnInteraction: false }"
  :navigation="true"
  :pagination="{ clickable: true }"
  :scrollbar="{ draggable: true }"
  :free-mode="true"
  :grid="{ rows: 2 }"
  effect="fade"
  :fade-effect="{ crossFade: true }"
  :keyboard="{ enabled: true }"
  :mousewheel="true"
  :lazy="true"
>
```

---

## Events

The `@swiper` event provides the Swiper instance after initialization.
All other Swiper events are fired directly as Vue events:

```vue
<swiper
  @swiper="onSwiper"
  @slideChange="onSlideChange"
  @progress="onProgress"
  @reachEnd="onReachEnd"
  @reachBeginning="onReachBeginning"
  @autoplayTimeLeft="onAutoplayTimeLeft"
  @click="onClick"
  @tap="onTap"
  @init="onInit"
  @destroy="onDestroy"
  @transitionStart="onTransitionStart"
  @transitionEnd="onTransitionEnd"
  @slideChangeTransitionStart="onSlideChangeTransitionStart"
  @slideChangeTransitionEnd="onSlideChangeTransitionEnd"
  @activeIndexChange="onActiveIndexChange"
  @realIndexChange="onRealIndexChange"
  @snapIndexChange="onSnapIndexChange"
  @zoomChange="onZoomChange"
>
```

```javascript
const onSwiper = (swiper) => {
  console.log('Swiper instance:', swiper);
  // swiper.slideNext(), swiper.slidePrev(), etc.
};

const onSlideChange = (swiper) => {
  console.log('Active index:', swiper.activeIndex);
  console.log('Real index:', swiper.realIndex);
};

const onProgress = (swiper, progress) => {
  console.log('Progress:', progress); // 0 to 1
};

const onAutoplayTimeLeft = (swiper, time, progress) => {
  // time: remaining time in ms
  // progress: 0 to 1
};
```

---

## `<SwiperSlide>` — props

| Prop | Type | Default | Description |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML element of the slide |
| `zoom` | `boolean` | `false` | Enable the zoom wrapper |
| `virtualIndex` | `number` | — | Index for Virtual Slides (required with virtual) |

---

## `v-slot` — slide render props

```vue
<swiper-slide v-slot="{ isActive, isPrev, isNext, isVisible, isDuplicate }">
  <div :class="{ 'slide--active': isActive, 'slide--prev': isPrev }">
    <span v-if="isActive">This slide is active</span>
    <span v-if="isPrev">Previous slide</span>
    <span v-if="isNext">Next slide</span>
  </div>
</swiper-slide>
```

| Variable | Meaning |
|---|---|
| `isActive` | The slide is active |
| `isPrev` | Previous slide |
| `isNext` | Next slide |
| `isVisible` | The slide is visible (requires `watchSlidesProgress`) |
| `isDuplicate` | Duplicate in loop mode |

---

## Composables

### `useSwiper`

Access the Swiper instance inside child components:

```vue
<script setup>
import { useSwiper } from 'swiper/vue';

const swiper = useSwiper();

function goNext() {
  swiper.value.slideNext();
}
function goPrev() {
  swiper.value.slidePrev();
}
function goTo(index) {
  swiper.value.slideTo(index);
}
</script>

<template>
  <div>
    <button @click="goPrev">Back</button>
    <button @click="goNext">Forward</button>
  </div>
</template>
```

Place inside `<Swiper>`:
```vue
<swiper>
  <swiper-slide>Slide 1</swiper-slide>
  <slide-navigation /> <!-- Component using useSwiper -->
</swiper>
```

### `useSwiperSlide`

```vue
<script setup>
import { useSwiperSlide } from 'swiper/vue';

const swiperSlide = useSwiperSlide();
// swiperSlide.value.isActive
// swiperSlide.value.isPrev
// swiperSlide.value.isNext
// swiperSlide.value.isVisible
// swiperSlide.value.isDuplicate
</script>

<template>
  <div :class="{ active: swiperSlide.isActive }">
    Slide content
  </div>
</template>
```

---

## Slots (content injection)

```vue
<swiper>
  <template #container-start>
    <div>Before the swiper-wrapper</div>
  </template>

  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <template #container-end>
    <div>After the swiper-wrapper</div>
  </template>

  <template #wrapper-start>
    <div>In the wrapper, before the slides</div>
  </template>

  <template #wrapper-end>
    <div>In the wrapper, after the slides</div>
  </template>
</swiper>
```

---

## Including modules

```vue
<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import {
  Navigation,
  Pagination,
  Scrollbar,
  Autoplay,
  EffectFade,
  Thumbs,
  FreeMode,
  Virtual,
  Controller,
  Zoom,
  Grid,
  Keyboard,
  Mousewheel,
  Parallax,
  A11y,
} from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/effect-fade';
</script>

<template>
  <swiper
    :modules="[Navigation, Pagination, Autoplay, EffectFade]"
    :navigation="true"
    :pagination="{ clickable: true }"
    :autoplay="{ delay: 3000 }"
    effect="fade"
  >
    <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide>
  </swiper>
</template>
```

---

## Virtual Slides

```vue
<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Virtual } from 'swiper/modules';

const slides = Array.from({ length: 1000 }, (_, i) => `Slide ${i + 1}`);
</script>

<template>
  <swiper :modules="[Virtual]" :virtual="true" :slides-per-view="3">
    <swiper-slide
      v-for="(slide, index) in slides"
      :key="slide"
      :virtual-index="index"
    >
      {{ slide }}
    </swiper-slide>
  </swiper>
</template>
```

---

## Controller (synchronized Swipers)

```vue
<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Controller } from 'swiper/modules';
import { ref } from 'vue';

const firstSwiper = ref(null);
const secondSwiper = ref(null);
</script>

<template>
  <swiper
    :modules="[Controller]"
    :controller="{ control: secondSwiper }"
    @swiper="(s) => (firstSwiper = s)"
  >
    <swiper-slide>Slide 1A</swiper-slide>
    <swiper-slide>Slide 2A</swiper-slide>
  </swiper>

  <swiper
    :modules="[Controller]"
    :controller="{ control: firstSwiper }"
    @swiper="(s) => (secondSwiper = s)"
  >
    <swiper-slide>Slide 1B</swiper-slide>
    <swiper-slide>Slide 2B</swiper-slide>
  </swiper>
</template>
```

---

## Thumbs (thumbnails)

```vue
<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Thumbs, FreeMode } from 'swiper/modules';
import { ref } from 'vue';
import 'swiper/css/thumbs';
import 'swiper/css/free-mode';

const thumbsSwiper = ref(null);
</script>

<template>
  <!-- Main Swiper -->
  <swiper
    :modules="[Thumbs]"
    :thumbs="{ swiper: thumbsSwiper }"
    :space-between="10"
  >
    <swiper-slide><img src="img1.jpg" /></swiper-slide>
    <swiper-slide><img src="img2.jpg" /></swiper-slide>
  </swiper>

  <!-- Thumbs Swiper -->
  <swiper
    :modules="[FreeMode, Thumbs]"
    :watch-slides-progress="true"
    :free-mode="true"
    :slides-per-view="4"
    :space-between="10"
    @swiper="(s) => (thumbsSwiper = s)"
  >
    <swiper-slide><img src="img1.jpg" /></swiper-slide>
    <swiper-slide><img src="img2.jpg" /></swiper-slide>
  </swiper>
</template>
```

---

## Effects

```vue
<script setup>
import { EffectCards } from 'swiper/modules';
import 'swiper/css/effect-cards';
</script>

<template>
  <swiper :modules="[EffectCards]" effect="cards" :grab-cursor="true">
    <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide>
  </swiper>
</template>
```

All effects: `"slide"` | `"fade"` | `"cube"` | `"coverflow"` | `"flip"` | `"cards"` | `"creative"`

---

## CSS import reference

```javascript
import 'swiper/css';                   // Core (always)
import 'swiper/css/bundle';            // Everything (alternative to individual)
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/autoplay';
import 'swiper/css/effect-fade';
import 'swiper/css/effect-cube';
import 'swiper/css/effect-flip';
import 'swiper/css/effect-coverflow';
import 'swiper/css/effect-cards';
import 'swiper/css/effect-creative';
import 'swiper/css/thumbs';
import 'swiper/css/free-mode';
import 'swiper/css/grid';
import 'swiper/css/zoom';
import 'swiper/css/keyboard';
import 'swiper/css/virtual';
```

---

*Source: https://swiperjs.com/vue — Swiper v12.2.0*
