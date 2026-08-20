# Swiper Svelte — Complete reference (via Swiper Element)

**Important:** The separate Svelte components (`swiper/svelte`) were removed in Swiper v9.
Since then, the official approach is integration via **Swiper Element** (Web Component).

Archive for v8 (the old Svelte components): https://v8.swiperjs.com/svelte

---

## Contents

- [Installation](#installation)
- [Registration (once)](#registration-once)
- [Import the CSS](#import-the-css)
- [Minimal example](#minimal-example)
- [Parameters as attributes](#parameters-as-attributes)
- [Property binding via `bind:this` and `onMount`](#property-binding-via-bindthis-and-onmount)
- [Events](#events)
- [Calling Swiper methods](#calling-swiper-methods)
- [Reactive parameters (Svelte stores / reactive)](#reactive-parameters-svelte-stores-reactive)
- [Slots](#slots)
- [#each loop with slides](#each-loop-with-slides)
- [Thumbs integration](#thumbs-integration)
- [SvelteKit integration](#sveltekit-integration)
- [Svelte 5 (Runes)](#svelte-5-runes)
- [Common problems and solutions](#common-problems-and-solutions)

## Installation

```bash
npm install swiper
```

---

## Registration (once)

```javascript
// src/app.js, src/main.js or src/routes/+layout.svelte
import { register } from 'swiper/element/bundle';
register();
```

Or lazily inside the component:
```svelte
<script>
  import { onMount } from 'svelte';
  import { register } from 'swiper/element/bundle';

  onMount(() => {
    register();
  });
</script>
```

---

## Import the CSS

```javascript
// In src/app.css or global CSS:
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

// Or the bundle:
import 'swiper/css/bundle';
```

---

## Minimal example

```svelte
<script>
  import { register } from 'swiper/element/bundle';
  import 'swiper/css';
  register();
</script>

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
```

---

## Parameters as attributes

```svelte
<swiper-container
  slides-per-view="3"
  space-between="30"
  speed="500"
  loop="true"
  centered-slides="true"
  navigation="true"
  pagination="true"
  scrollbar="true"
  autoplay-delay="2500"
  autoplay-disable-on-interaction="false"
  mousewheel-force-to-axis="true"
>
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

---

## Property binding via `bind:this` and `onMount`

For complex parameters (breakpoints, render functions, etc.):

```svelte
<script>
  import { onMount } from 'svelte';
  import { register } from 'swiper/element/bundle';
  register();

  let swiperEl;

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
        renderBullet: (index, className) =>
          `<span class="${className}">${index + 1}</span>`,
      },
      on: {
        init(swiper) {
          console.log('initialized', swiper);
        },
      },
    };

    Object.assign(swiperEl, params);
    swiperEl.initialize();
  });
</script>

<swiper-container bind:this={swiperEl} init="false">
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
</swiper-container>
```

---

## Events

As of Swiper v11, events carry the prefix `swiper` by default:

```svelte
<script>
  function onSlideChange(event) {
    const [swiper] = event.detail;
    console.log('Active index:', swiper.activeIndex);
  }

  function onProgress(event) {
    const [swiper, progress] = event.detail;
    console.log('Progress:', progress);
  }

  function onInit(event) {
    const [swiper] = event.detail;
    console.log('Swiper initialized', swiper);
  }

  function onReachEnd(event) {
    console.log('Reached end');
  }
</script>

<swiper-container
  on:swiperslidechange={onSlideChange}
  on:swiperprogress={onProgress}
  on:swiperinit={onInit}
  on:swiperreachend={onReachEnd}
  on:swipertransitionstart={onTransitionStart}
  on:swipertransitionend={onTransitionEnd}
  on:swiperclick={onClick}
>
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

Change the prefix:
```svelte
<swiper-container events-prefix="">
  <!-- Events: "slidechange", "progress" (no prefix) -->
</swiper-container>
```

---

## Calling Swiper methods

```svelte
<script>
  let swiperEl;

  function next() {
    swiperEl.swiper.slideNext();
  }

  function prev() {
    swiperEl.swiper.slidePrev();
  }

  function slideTo(index) {
    swiperEl.swiper.slideTo(index);
  }

  function toggleAutoplay() {
    const swiper = swiperEl.swiper;
    if (swiper.autoplay.running) {
      swiper.autoplay.stop();
    } else {
      swiper.autoplay.start();
    }
  }
</script>

<swiper-container bind:this={swiperEl} navigation="true">
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
</swiper-container>

<button on:click={prev}>Back</button>
<button on:click={next}>Forward</button>
```

---

## Reactive parameters (Svelte stores / reactive)

```svelte
<script>
  import { onMount } from 'svelte';
  import { register } from 'swiper/element/bundle';
  register();

  let swiperEl;
  let slidesPerView = 3;

  $: if (swiperEl && swiperEl.swiper) {
    swiperEl.swiper.params.slidesPerView = slidesPerView;
    swiperEl.swiper.update();
  }
</script>

<input type="range" min="1" max="5" bind:value={slidesPerView} />

<swiper-container
  bind:this={swiperEl}
  slides-per-view={slidesPerView}
>
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
</swiper-container>
```

---

## Slots

```svelte
<swiper-container>
  <div slot="container-start">Before the slides</div>

  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <div slot="container-end">After the slides</div>
</swiper-container>
```

---

## #each loop with slides

```svelte
<script>
  const items = [
    { id: 1, title: 'Item 1', img: 'img1.jpg' },
    { id: 2, title: 'Item 2', img: 'img2.jpg' },
    { id: 3, title: 'Item 3', img: 'img3.jpg' },
  ];
</script>

<swiper-container slides-per-view="3" space-between="20">
  {#each items as item (item.id)}
    <swiper-slide>
      <img src={item.img} alt={item.title} />
      <p>{item.title}</p>
    </swiper-slide>
  {/each}
</swiper-container>
```

---

## Thumbs integration

```svelte
<script>
  import { onMount } from 'svelte';
  import { register } from 'swiper/element/bundle';
  register();

  let mainSwiperEl;
  let thumbsSwiperEl;

  onMount(() => {
    // Initialize the thumbs Swiper first
    Object.assign(thumbsSwiperEl, {
      slidesPerView: 4,
      spaceBetween: 10,
      watchSlidesProgress: true,
      freeMode: true,
    });
    thumbsSwiperEl.initialize();

    // Then the main Swiper with the thumbs reference
    Object.assign(mainSwiperEl, {
      spaceBetween: 10,
      thumbs: { swiper: thumbsSwiperEl.swiper },
    });
    mainSwiperEl.initialize();
  });
</script>

<swiper-container bind:this={mainSwiperEl} init="false">
  <swiper-slide><img src="img1.jpg" /></swiper-slide>
  <swiper-slide><img src="img2.jpg" /></swiper-slide>
</swiper-container>

<swiper-container bind:this={thumbsSwiperEl} init="false">
  <swiper-slide><img src="img1.jpg" /></swiper-slide>
  <swiper-slide><img src="img2.jpg" /></swiper-slide>
</swiper-container>
```

---

## SvelteKit integration

```svelte
<!-- src/routes/+page.svelte -->
<script>
  import { browser } from '$app/environment';
  import { onMount } from 'svelte';
  import 'swiper/css';

  let swiperEl;

  onMount(async () => {
    if (browser) {
      const { register } = await import('swiper/element/bundle');
      register();
    }
  });
</script>

<swiper-container bind:this={swiperEl} slides-per-view="3">
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
</swiper-container>
```

---

## Svelte 5 (Runes)

```svelte
<script>
  import { onMount } from 'svelte';
  import { register } from 'swiper/element/bundle';

  register();

  let swiperEl = $state(null);

  onMount(() => {
    if (swiperEl) {
      Object.assign(swiperEl, {
        slidesPerView: 3,
        breakpoints: { 768: { slidesPerView: 4 } },
      });
      swiperEl.initialize();
    }
  });
</script>

<swiper-container bind:this={swiperEl} init="false">
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

---

## Common problems and solutions

| Problem | Solution |
|---|---|
| `swiper-container` is not recognized | Call `register()` (and add an SSR check in SvelteKit) |
| Slides do not appear | Import the CSS: `import 'swiper/css'` |
| Events are not fired | Check the event names: v11+ prefix `swiper` |
| SSR error in SvelteKit | Check `if (browser)` or use `onMount` (client-only) |
| Complex parameters ignored | Use `init="false"` + `Object.assign` + `initialize()` |

---

*Source: https://swiperjs.com/svelte + https://swiperjs.com/element — Swiper v12.2.0*
