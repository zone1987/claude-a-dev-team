# Swiper SolidJS — Complete reference (via Swiper Element)

**Important:** The separate SolidJS components (`swiper/solid`) were removed in Swiper v9.
Since then, the official approach is integration via **Swiper Element** (Web Component).

Archive for v8 (the old SolidJS components): https://v8.swiperjs.com/solid

---

## Contents

- [Installation](#installation)
- [Registration (once)](#registration-once)
- [Import the CSS](#import-the-css)
- [Minimal example](#minimal-example)
- [Property binding via `ref` and `onMount`](#property-binding-via-ref-and-onmount)
- [Events](#events)
- [Calling Swiper methods](#calling-swiper-methods)
- [Reactive parameters with signals](#reactive-parameters-with-signals)
- [Rendering slides from an array (For)](#rendering-slides-from-an-array-for)
- [Slots](#slots)
- [Lazy initialization (SolidStart / SSR)](#lazy-initialization-solidstart-ssr)
- [Thumbs integration](#thumbs-integration)
- [SolidJS-specific JSX notes](#solidjs-specific-jsx-notes)
- [Common problems and solutions](#common-problems-and-solutions)

## Installation

```bash
npm install swiper
```

---

## Registration (once)

```javascript
// src/index.jsx or src/root.jsx
import { register } from 'swiper/element/bundle';
register();
```

---

## Import the CSS

```javascript
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
// Or:
import 'swiper/css/bundle';
```

---

## Minimal example

```jsx
import { register } from 'swiper/element/bundle';
import 'swiper/css';

register();

function App() {
  return (
    <swiper-container
      slides-per-view="3"
      space-between="30"
      navigation="true"
      pagination="true"
    >
      <swiper-slide>Slide 1</swiper-slide>
      <swiper-slide>Slide 2</swiper-slide>
      <swiper-slide>Slide 3</swiper-slide>
    </swiper-container>
  );
}
```

---

## Property binding via `ref` and `onMount`

For complex parameters (breakpoints, render functions, etc.):

```jsx
import { onMount, createSignal } from 'solid-js';
import { register } from 'swiper/element/bundle';

register();

function MySwiper() {
  let swiperRef;

  onMount(() => {
    const params = {
      slidesPerView: 1,
      spaceBetween: 10,
      breakpoints: {
        640: { slidesPerView: 2, spaceBetween: 20 },
        768: { slidesPerView: 3, spaceBetween: 30 },
        1024: { slidesPerView: 4, spaceBetween: 40 },
      },
      pagination: {
        clickable: true,
      },
      navigation: true,
      on: {
        init(swiper) {
          console.log('Swiper initialized', swiper);
        },
      },
    };

    Object.assign(swiperRef, params);
    swiperRef.initialize();
  });

  return (
    <swiper-container ref={swiperRef} init="false">
      <swiper-slide>Slide 1</swiper-slide>
      <swiper-slide>Slide 2</swiper-slide>
    </swiper-container>
  );
}
```

---

## Events

As of Swiper v11, events carry the prefix `swiper` by default:

```jsx
function MySwiper() {
  function handleSlideChange(event) {
    const [swiper] = event.detail;
    console.log('Active index:', swiper.activeIndex);
  }

  function handleProgress(event) {
    const [swiper, progress] = event.detail;
    console.log('Progress:', progress);
  }

  function handleInit(event) {
    const [swiper] = event.detail;
    console.log('Initialized', swiper);
  }

  return (
    <swiper-container
      on:swiperslidechange={handleSlideChange}
      on:swiperprogress={handleProgress}
      on:swiperinit={handleInit}
      on:swiperreachend={() => console.log('End reached')}
      on:swipertransitionstart={() => console.log('Transition start')}
    >
      <swiper-slide>Slide 1</swiper-slide>
    </swiper-container>
  );
}
```

**Note:** SolidJS uses `on:eventname` for native DOM events.

Change the prefix:
```jsx
<swiper-container events-prefix="">
  {/* Events: "slidechange", "progress" (no prefix) */}
</swiper-container>
```

---

## Calling Swiper methods

```jsx
function MySwiper() {
  let swiperRef;

  function next() {
    swiperRef.swiper.slideNext();
  }

  function prev() {
    swiperRef.swiper.slidePrev();
  }

  function slideTo(index) {
    swiperRef.swiper.slideTo(index);
  }

  return (
    <div>
      <swiper-container ref={swiperRef} navigation="true">
        <swiper-slide>Slide 1</swiper-slide>
        <swiper-slide>Slide 2</swiper-slide>
      </swiper-container>
      <button onClick={prev}>Back</button>
      <button onClick={next}>Forward</button>
    </div>
  );
}
```

---

## Reactive parameters with signals

```jsx
import { createSignal, createEffect } from 'solid-js';

function ReactiveSwiper() {
  let swiperRef;
  const [slidesPerView, setSlidesPerView] = createSignal(3);

  createEffect(() => {
    if (swiperRef?.swiper) {
      swiperRef.swiper.params.slidesPerView = slidesPerView();
      swiperRef.swiper.update();
    }
  });

  return (
    <div>
      <input
        type="range"
        min="1"
        max="5"
        value={slidesPerView()}
        onInput={(e) => setSlidesPerView(Number(e.target.value))}
      />
      <swiper-container
        ref={swiperRef}
        slides-per-view={slidesPerView()}
      >
        <swiper-slide>Slide 1</swiper-slide>
        <swiper-slide>Slide 2</swiper-slide>
      </swiper-container>
    </div>
  );
}
```

---

## Rendering slides from an array (For)

```jsx
import { For } from 'solid-js';

const items = [
  { id: 1, title: 'Item 1', img: 'img1.jpg' },
  { id: 2, title: 'Item 2', img: 'img2.jpg' },
  { id: 3, title: 'Item 3', img: 'img3.jpg' },
];

function ListSwiper() {
  return (
    <swiper-container slides-per-view="3" space-between="20">
      <For each={items}>
        {(item) => (
          <swiper-slide>
            <img src={item.img} alt={item.title} />
            <p>{item.title}</p>
          </swiper-slide>
        )}
      </For>
    </swiper-container>
  );
}
```

---

## Slots

```jsx
<swiper-container>
  <div slot="container-start">Before the slides</div>

  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <div slot="container-end">After the slides</div>
</swiper-container>
```

---

## Lazy initialization (SolidStart / SSR)

```jsx
import { onMount, Show } from 'solid-js';
import { createSignal } from 'solid-js';

function LazySwiper() {
  const [mounted, setMounted] = createSignal(false);
  let swiperRef;

  onMount(() => {
    import('swiper/element/bundle').then(({ register }) => {
      register();
      setMounted(true);
    });
  });

  return (
    <Show when={mounted()}>
      <swiper-container
        ref={swiperRef}
        slides-per-view="3"
        navigation="true"
      >
        <swiper-slide>Slide 1</swiper-slide>
        <swiper-slide>Slide 2</swiper-slide>
      </swiper-container>
    </Show>
  );
}
```

---

## Thumbs integration

```jsx
import { onMount } from 'solid-js';
import { register } from 'swiper/element/bundle';
register();

function ThumbsExample() {
  let mainRef;
  let thumbsRef;

  onMount(() => {
    // Thumbs first
    Object.assign(thumbsRef, {
      slidesPerView: 4,
      spaceBetween: 10,
      watchSlidesProgress: true,
      freeMode: true,
    });
    thumbsRef.initialize();

    // Then the main Swiper
    Object.assign(mainRef, {
      spaceBetween: 10,
      thumbs: { swiper: thumbsRef.swiper },
    });
    mainRef.initialize();
  });

  return (
    <div>
      <swiper-container ref={mainRef} init="false">
        <swiper-slide><img src="img1.jpg" /></swiper-slide>
        <swiper-slide><img src="img2.jpg" /></swiper-slide>
      </swiper-container>
      <swiper-container ref={thumbsRef} init="false">
        <swiper-slide><img src="img1.jpg" /></swiper-slide>
        <swiper-slide><img src="img2.jpg" /></swiper-slide>
      </swiper-container>
    </div>
  );
}
```

---

## SolidJS-specific JSX notes

SolidJS compiles JSX straight to DOM operations (no virtual DOM). Key points:

- `ref={refVar}` for the element reference (not a callback ref as in React)
- `on:eventname` for native custom events (lowercase)
- Attributes are set as real DOM attributes

```jsx
// SolidJS-specific event syntax:
<swiper-container
  on:swiperslidechange={handler}  // Native custom event
  onClick={handler}               // Synthetic click event
/>
```

---

## Common problems and solutions

| Problem | Solution |
|---|---|
| `swiper-container` unknown | Call `register()`, ideally once in `index.jsx` |
| Styles missing | Make sure `import 'swiper/css'` is present |
| Events are not fired | SolidJS uses `on:eventname` for native DOM events |
| SSR error | Use a lazy import inside `onMount` |
| Complex params not applied | `init="false"` + `Object.assign` + `initialize()` |

---

*Source: https://swiperjs.com/solid + https://swiperjs.com/element — Swiper v12.2.0*
