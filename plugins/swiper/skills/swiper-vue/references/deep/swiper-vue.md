# Swiper Vue — Vollständige Referenz

Swiper Vue-Komponenten sind offiziell unterstützt und in `swiper/vue` enthalten.
Kompatibel mit Vue 3 (Composition API).

---

## Installation

```bash
npm install swiper
```

---

## Basis-Import

```javascript
import { Swiper, SwiperSlide } from 'swiper/vue';

// Core-CSS (immer nötig)
import 'swiper/css';

// Modul-spezifische CSS
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

// Oder alles auf einmal
import 'swiper/css/bundle';
```

---

## Minimales Beispiel (Composition API)

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

## Options API Beispiel

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

## `<Swiper>` — Props

Alle [Swiper API-Parameter](https://swiperjs.com/swiper-api#parameters) sind als Props verfügbar (camelCase oder kebab-case in Templates).

### Zusätzliche Vue-spezifische Props

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML-Element des Containers |
| `wrapperTag` | `string` | `'div'` | HTML-Element des Wrappers |
| `modules` | `SwiperModule[]` | — | Einzubindende Module |

### Häufige Parameter-Beispiele

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

Der `@swiper`-Event liefert die Swiper-Instanz nach der Initialisierung.
Alle weiteren Swiper-Events werden direkt als Vue-Events gefeuert:

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
  console.log('Swiper-Instanz:', swiper);
  // swiper.slideNext(), swiper.slidePrev(), etc.
};

const onSlideChange = (swiper) => {
  console.log('Aktiver Index:', swiper.activeIndex);
  console.log('Realer Index:', swiper.realIndex);
};

const onProgress = (swiper, progress) => {
  console.log('Fortschritt:', progress); // 0 bis 1
};

const onAutoplayTimeLeft = (swiper, time, progress) => {
  // time: verbleibende Zeit in ms
  // progress: 0 bis 1
};
```

---

## `<SwiperSlide>` — Props

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML-Element des Slides |
| `zoom` | `boolean` | `false` | Zoom-Wrapper aktivieren |
| `virtualIndex` | `number` | — | Index für Virtual Slides (Pflicht bei virtual) |

---

## `v-slot` — Slide-Render-Props

```vue
<swiper-slide v-slot="{ isActive, isPrev, isNext, isVisible, isDuplicate }">
  <div :class="{ 'slide--active': isActive, 'slide--prev': isPrev }">
    <span v-if="isActive">Dieser Slide ist aktiv</span>
    <span v-if="isPrev">Vorheriger Slide</span>
    <span v-if="isNext">Nächster Slide</span>
  </div>
</swiper-slide>
```

| Variable | Bedeutung |
|---|---|
| `isActive` | Slide ist aktiv |
| `isPrev` | Vorheriger Slide |
| `isNext` | Nächster Slide |
| `isVisible` | Slide ist sichtbar (benötigt `watchSlidesProgress`) |
| `isDuplicate` | Duplikat im Loop-Modus |

---

## Composables

### `useSwiper`

Zugriff auf Swiper-Instanz innerhalb von Kindkomponenten:

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
    <button @click="goPrev">Zurück</button>
    <button @click="goNext">Vor</button>
  </div>
</template>
```

Innerhalb von `<Swiper>` platzieren:
```vue
<swiper>
  <swiper-slide>Slide 1</swiper-slide>
  <slide-navigation /> <!-- Komponente mit useSwiper -->
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
    Slide-Inhalt
  </div>
</template>
```

---

## Slots (Content-Injection)

```vue
<swiper>
  <template #container-start>
    <div>Vor dem swiper-wrapper</div>
  </template>

  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <template #container-end>
    <div>Nach dem swiper-wrapper</div>
  </template>

  <template #wrapper-start>
    <div>Im Wrapper, vor Slides</div>
  </template>

  <template #wrapper-end>
    <div>Im Wrapper, nach Slides</div>
  </template>
</swiper>
```

---

## Module einbinden

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

## Controller (synchronisierte Swiper)

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

## Thumbs (Vorschaubilder)

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
  <!-- Haupt-Swiper -->
  <swiper
    :modules="[Thumbs]"
    :thumbs="{ swiper: thumbsSwiper }"
    :space-between="10"
  >
    <swiper-slide><img src="img1.jpg" /></swiper-slide>
    <swiper-slide><img src="img2.jpg" /></swiper-slide>
  </swiper>

  <!-- Thumbs-Swiper -->
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

## Effekte

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

Alle Effekte: `"slide"` | `"fade"` | `"cube"` | `"coverflow"` | `"flip"` | `"cards"` | `"creative"`

---

## CSS-Imports Referenz

```javascript
import 'swiper/css';                   // Core (immer)
import 'swiper/css/bundle';            // Alles (alternativ zu einzelnen)
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

*Quelle: https://swiperjs.com/vue — Swiper v12.2.0*
