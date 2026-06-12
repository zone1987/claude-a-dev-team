# Swiper Svelte — Vollständige Referenz (via Swiper Element)

**Wichtig:** Die separaten Svelte-Komponenten (`swiper/svelte`) wurden in Swiper v9 entfernt.
Der offizielle Weg ist seither die Integration via **Swiper Element** (Web Component).

Archiv für v8 (alte Svelte-Komponenten): https://v8.swiperjs.com/svelte

---

## Installation

```bash
npm install swiper
```

---

## Registrierung (einmalig)

```javascript
// src/app.js, src/main.js oder src/routes/+layout.svelte
import { register } from 'swiper/element/bundle';
register();
```

Oder lazy im Component:
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

## CSS importieren

```javascript
// In src/app.css oder global CSS:
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

// Oder Bundle:
import 'swiper/css/bundle';
```

---

## Minimales Beispiel

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

## Parameter als Attribute

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

## Property-Binding via `bind:this` und `onMount`

Für komplexe Parameter (Breakpoints, Render-Funktionen etc.):

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

Ab Swiper v11: Events haben standardmäßig den Präfix `swiper`:

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

Präfix anpassen:
```svelte
<swiper-container events-prefix="">
  <!-- Events: "slidechange", "progress" (kein Prefix) -->
</swiper-container>
```

---

## Swiper-Methoden aufrufen

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

<button on:click={prev}>Zurück</button>
<button on:click={next}>Vor</button>
```

---

## Reaktive Parameter (Svelte Stores / Reactive)

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
  <div slot="container-start">Vor den Slides</div>

  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <div slot="container-end">Nach den Slides</div>
</swiper-container>
```

---

## #each-Loop mit Slides

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

## Thumbs-Integration

```svelte
<script>
  import { onMount } from 'svelte';
  import { register } from 'swiper/element/bundle';
  register();

  let mainSwiperEl;
  let thumbsSwiperEl;

  onMount(() => {
    // Thumbs-Swiper zuerst initialisieren
    Object.assign(thumbsSwiperEl, {
      slidesPerView: 4,
      spaceBetween: 10,
      watchSlidesProgress: true,
      freeMode: true,
    });
    thumbsSwiperEl.initialize();

    // Dann Haupt-Swiper mit Thumbs-Referenz
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

## SvelteKit-Integration

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

## Häufige Probleme & Lösungen

| Problem | Lösung |
|---|---|
| `swiper-container` wird nicht erkannt | `register()` aufrufen (und SSR-Check bei SvelteKit) |
| Slides erscheinen nicht | CSS importieren: `import 'swiper/css'` |
| Events werden nicht gefeuert | Event-Namen prüfen: v11+ Prefix `swiper` |
| SSR-Fehler in SvelteKit | `if (browser)` prüfen oder `onMount` nutzen (client-only) |
| Komplexe Parameter ignoriert | `init="false"` + `Object.assign` + `initialize()` verwenden |

---

*Quelle: https://swiperjs.com/svelte + https://swiperjs.com/element — Swiper v12.2.0*
