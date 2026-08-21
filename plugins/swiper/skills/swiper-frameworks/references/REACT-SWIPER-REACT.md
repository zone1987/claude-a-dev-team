# Swiper React — Complete reference

The Swiper React components are officially supported and shipped in `swiper/react`.
Compatible with React 18+.

---

## Contents

- [Installation](#installation)
- [Base import](#base-import)
- [Minimal example](#minimal-example)
- [`<Swiper>` — props](#swiper-props)
- [Events as `onXxx` props](#events-as-onxxx-props)
- [`<SwiperSlide>` — props](#swiperslide-props)
- [Render function (slide state)](#render-function-slide-state)
- [Hooks](#hooks)
- [Slots (content injection)](#slots-content-injection)
- [Including modules](#including-modules)
- [Virtual Slides](#virtual-slides)
- [Controller (synchronized Swipers)](#controller-synchronized-swipers)
- [Thumbs (thumbnails)](#thumbs-thumbnails)
- [Effects](#effects)
- [Swiper instance via ref (alternative to `onSwiper`)](#swiper-instance-via-ref-alternative-to-onswiper)

## Installation

```bash
npm install swiper
```

---

## Base import

```jsx
import { Swiper, SwiperSlide } from 'swiper/react';

// Core CSS (always required)
import 'swiper/css';

// Module-specific CSS files
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

// Or everything at once (bundle)
import 'swiper/css/bundle';
```

---

## Minimal example

```jsx
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';

export default function MySwiper() {
  return (
    <Swiper
      spaceBetween={50}
      slidesPerView={3}
      onSlideChange={() => console.log('slide change')}
      onSwiper={(swiper) => console.log(swiper)}
    >
      <SwiperSlide>Slide 1</SwiperSlide>
      <SwiperSlide>Slide 2</SwiperSlide>
      <SwiperSlide>Slide 3</SwiperSlide>
    </Swiper>
  );
}
```

---

## `<Swiper>` — props

All [Swiper API parameters](https://swiperjs.com/swiper-api#parameters) are available as props (camelCase).

### Additional React-specific props

| Prop | Type | Default | Description |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML element of the container |
| `wrapperTag` | `string` | `'div'` | HTML element of the wrapper |
| `onSwiper` | `(swiper: Swiper) => void` | — | Callback with the Swiper instance after init |
| `modules` | `SwiperModule[]` | — | Array of the modules to include |

### Common parameters as props

```jsx
<Swiper
  // General
  slidesPerView={1}
  spaceBetween={10}
  speed={400}
  loop={true}
  centeredSlides={true}
  direction="horizontal" // or "vertical"
  
  // Breakpoints
  breakpoints={{
    640: { slidesPerView: 2, spaceBetween: 20 },
    768: { slidesPerView: 3, spaceBetween: 30 },
    1024: { slidesPerView: 4, spaceBetween: 40 },
  }}
  
  // Autoplay
  autoplay={{ delay: 2500, disableOnInteraction: false }}
  
  // Navigation
  navigation={true}
  
  // Pagination
  pagination={{ clickable: true }}
  
  // Scrollbar
  scrollbar={{ draggable: true }}
  
  // Free mode
  freeMode={true}
  
  // Grid
  grid={{ rows: 2 }}
  
  // Effects
  effect="fade" // "slide"|"fade"|"cube"|"coverflow"|"flip"|"cards"|"creative"
  fadeEffect={{ crossFade: true }}
  
  // Keyboard
  keyboard={{ enabled: true }}
  
  // Mousewheel
  mousewheel={true}
  
  // Lazy loading
  lazy={true}
>
```

---

## Events as `onXxx` props

Every Swiper API event is available as a prop (format: `on` + event name with a capital letter):

| Swiper event | React prop |
|---|---|
| `slideChange` | `onSlideChange` |
| `progress` | `onProgress` |
| `reachEnd` | `onReachEnd` |
| `reachBeginning` | `onReachBeginning` |
| `init` | `onInit` |
| `destroy` | `onDestroy` |
| `click` | `onClick` |
| `tap` | `onTap` |
| `doubleTap` | `onDoubleTap` |
| `imagesReady` | `onImagesReady` |
| `transitionStart` | `onTransitionStart` |
| `transitionEnd` | `onTransitionEnd` |
| `slideChangeTransitionStart` | `onSlideChangeTransitionStart` |
| `slideChangeTransitionEnd` | `onSlideChangeTransitionEnd` |
| `slideNextTransitionStart` | `onSlideNextTransitionStart` |
| `slidePrevTransitionStart` | `onSlidePrevTransitionStart` |
| `setTranslate` | `onSetTranslate` |
| `setTransition` | `onSetTransition` |
| `autoplayStart` | `onAutoplayStart` |
| `autoplayStop` | `onAutoplayStop` |
| `autoplayTimeLeft` | `onAutoplayTimeLeft` |
| `lazyImageLoad` | `onLazyImageLoad` |
| `lazyImageReady` | `onLazyImageReady` |
| `activeIndexChange` | `onActiveIndexChange` |
| `snapIndexChange` | `onSnapIndexChange` |
| `realIndexChange` | `onRealIndexChange` |
| `observerUpdate` | `onObserverUpdate` |
| `fromEdge` | `onFromEdge` |
| `zoomChange` | `onZoomChange` |

```jsx
<Swiper
  onSwiper={(swiper) => console.log('Init:', swiper)}
  onSlideChange={(swiper) => console.log('Index:', swiper.activeIndex)}
  onProgress={(swiper, progress) => console.log('Progress:', progress)}
  onReachEnd={(swiper) => console.log('End reached')}
  onAutoplayTimeLeft={(swiper, time, progress) =>
    console.log(`${Math.ceil(time / 1000)}s left`)
  }
>
```

---

## `<SwiperSlide>` — props

| Prop | Type | Default | Description |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML element of the slide |
| `zoom` | `boolean` | `false` | Enable the zoom wrapper |
| `virtualIndex` | `number` | — | Index for Virtual Slides (required) |

---

## Render function (slide state)

`SwiperSlide` accepts a render function that provides state variables:

```jsx
<SwiperSlide>
  {({ isActive, isPrev, isNext, isVisible, isDuplicate }) => (
    <div className={isActive ? 'slide active' : 'slide'}>
      {isActive && <span>Currently active</span>}
      {isNext && <span>Next slide</span>}
      {isPrev && <span>Previous slide</span>}
    </div>
  )}
</SwiperSlide>
```

| Variable | Meaning |
|---|---|
| `isActive` | This slide is active |
| `isPrev` | Previous slide |
| `isNext` | Next slide |
| `isVisible` | Visible (requires `watchSlidesProgress`) |
| `isDuplicate` | Duplicate in loop mode |

---

## Hooks

### `useSwiper`

Access the Swiper instance inside child components:

```jsx
import { useSwiper } from 'swiper/react';

function SlideNavigation() {
  const swiper = useSwiper();

  return (
    <div>
      <button onClick={() => swiper.slidePrev()}>Back</button>
      <button onClick={() => swiper.slideNext()}>Forward</button>
      <button onClick={() => swiper.slideTo(0)}>Beginning</button>
    </div>
  );
}

// Use inside <Swiper>:
<Swiper>
  <SwiperSlide>Slide 1</SwiperSlide>
  <SlideNavigation />
</Swiper>
```

### `useSwiperSlide`

Slide state inside a slide child component:

```jsx
import { useSwiperSlide } from 'swiper/react';

function SlideContent() {
  const swiperSlide = useSwiperSlide();
  // swiperSlide.isActive, .isPrev, .isNext, .isVisible, .isDuplicate

  return (
    <div>
      {swiperSlide.isActive ? 'Active slide' : 'Inactive slide'}
    </div>
  );
}

<Swiper>
  <SwiperSlide>
    <SlideContent />
  </SwiperSlide>
</Swiper>
```

---

## Slots (content injection)

Special slots for content outside the wrapper:

```jsx
<Swiper>
  {/* container-start: before the swiper-wrapper */}
  <div slot="container-start">Top</div>

  <SwiperSlide>Slide 1</SwiperSlide>
  <SwiperSlide>Slide 2</SwiperSlide>

  {/* container-end: after the swiper-wrapper */}
  <div slot="container-end">Bottom</div>

  {/* wrapper-start / wrapper-end: inside the wrapper */}
  <div slot="wrapper-start">Wrapper Start</div>
  <div slot="wrapper-end">Wrapper End</div>
</Swiper>
```

---

## Including modules

```jsx
import { Navigation, Pagination, Scrollbar, Autoplay, EffectFade } from 'swiper/modules';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/autoplay';
import 'swiper/css/effect-fade';

<Swiper
  modules={[Navigation, Pagination, Scrollbar, Autoplay, EffectFade]}
  navigation
  pagination={{ clickable: true }}
  scrollbar={{ draggable: true }}
  autoplay={{ delay: 3000 }}
  effect="fade"
>
```

### All available modules

```javascript
import {
  Virtual,
  Keyboard,
  Mousewheel,
  Navigation,
  Pagination,
  Scrollbar,
  Parallax,
  FreeMode,
  Grid,
  Manipulation,
  Zoom,
  Controller,
  A11y,
  History,
  HashNavigation,
  Autoplay,
  EffectFade,
  EffectCube,
  EffectFlip,
  EffectCoverflow,
  EffectCards,
  EffectCreative,
  Thumbs,
} from 'swiper/modules';
```

---

## Virtual Slides

```jsx
import { Virtual } from 'swiper/modules';

const slides = Array.from({ length: 1000 }, (_, i) => `Slide ${i + 1}`);

<Swiper
  modules={[Virtual]}
  virtual
  slidesPerView={3}
>
  {slides.map((slide, index) => (
    <SwiperSlide key={slide} virtualIndex={index}>
      {slide}
    </SwiperSlide>
  ))}
</Swiper>
```

---

## Controller (synchronized Swipers)

```jsx
import { Controller } from 'swiper/modules';
import { useState } from 'react';

function ControlledSwiper() {
  const [firstSwiper, setFirstSwiper] = useState(null);
  const [secondSwiper, setSecondSwiper] = useState(null);

  return (
    <>
      <Swiper
        modules={[Controller]}
        onSwiper={setFirstSwiper}
        controller={{ control: secondSwiper }}
      >
        <SwiperSlide>Slide 1A</SwiperSlide>
        <SwiperSlide>Slide 2A</SwiperSlide>
      </Swiper>

      <Swiper
        modules={[Controller]}
        onSwiper={setSecondSwiper}
        controller={{ control: firstSwiper }}
      >
        <SwiperSlide>Slide 1B</SwiperSlide>
        <SwiperSlide>Slide 2B</SwiperSlide>
      </Swiper>
    </>
  );
}
```

---

## Thumbs (thumbnails)

```jsx
import { Thumbs, FreeMode } from 'swiper/modules';
import { useState } from 'react';
import 'swiper/css/thumbs';
import 'swiper/css/free-mode';

function ThumbsSwiper() {
  const [thumbsSwiper, setThumbsSwiper] = useState(null);

  return (
    <>
      {/* Main Swiper */}
      <Swiper
        modules={[Thumbs]}
        thumbs={{ swiper: thumbsSwiper }}
        spaceBetween={10}
      >
        <SwiperSlide><img src="img1.jpg" /></SwiperSlide>
        <SwiperSlide><img src="img2.jpg" /></SwiperSlide>
      </Swiper>

      {/* Thumbs Swiper */}
      <Swiper
        modules={[FreeMode, Thumbs]}
        onSwiper={setThumbsSwiper}
        watchSlidesProgress
        freeMode
        slidesPerView={4}
        spaceBetween={10}
      >
        <SwiperSlide><img src="img1.jpg" /></SwiperSlide>
        <SwiperSlide><img src="img2.jpg" /></SwiperSlide>
      </Swiper>
    </>
  );
}
```

---

## Effects

```jsx
import { EffectCards } from 'swiper/modules';
import 'swiper/css/effect-cards';

<Swiper modules={[EffectCards]} effect="cards" grabCursor>
  <SwiperSlide>Slide 1</SwiperSlide>
  <SwiperSlide>Slide 2</SwiperSlide>
</Swiper>
```

All effects: `"slide"` | `"fade"` | `"cube"` | `"coverflow"` | `"flip"` | `"cards"` | `"creative"`

---

## Swiper instance via ref (alternative to `onSwiper`)

```jsx
import { useRef } from 'react';

function MySwiper() {
  const swiperRef = useRef(null);

  return (
    <>
      <Swiper onSwiper={(swiper) => (swiperRef.current = swiper)}>
        <SwiperSlide>Slide 1</SwiperSlide>
      </Swiper>
      <button onClick={() => swiperRef.current?.slideNext()}>
        Next
      </button>
    </>
  );
}
```

---

*Source: https://swiperjs.com/react — Swiper v12.2.0*
