# Swiper SolidJS — Vollständige Referenz (via Swiper Element)

**Wichtig:** Die separaten SolidJS-Komponenten (`swiper/solid`) wurden in Swiper v9 entfernt.
Der offizielle Weg ist seither die Integration via **Swiper Element** (Web Component).

Archiv für v8 (alte SolidJS-Komponenten): https://v8.swiperjs.com/solid

---

## Installation

```bash
npm install swiper
```

---

## Registrierung (einmalig)

```javascript
// src/index.jsx oder src/root.jsx
import { register } from 'swiper/element/bundle';
register();
```

---

## CSS importieren

```javascript
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
// Oder:
import 'swiper/css/bundle';
```

---

## Minimales Beispiel

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

## Property-Binding via `ref` und `onMount`

Für komplexe Parameter (Breakpoints, Render-Funktionen etc.):

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

Ab Swiper v11: Events haben standardmäßig den Präfix `swiper`:

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

**Hinweis:** SolidJS nutzt `on:eventname` für native DOM-Events.

Präfix anpassen:
```jsx
<swiper-container events-prefix="">
  {/* Events: "slidechange", "progress" (kein Prefix) */}
</swiper-container>
```

---

## Swiper-Methoden aufrufen

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
      <button onClick={prev}>Zurück</button>
      <button onClick={next}>Vor</button>
    </div>
  );
}
```

---

## Reaktive Parameter mit Signals

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

## Slides aus Array rendern (For)

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
  <div slot="container-start">Vor den Slides</div>

  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <div slot="container-end">Nach den Slides</div>
</swiper-container>
```

---

## Lazy Initialization (SolidStart / SSR)

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

## Thumbs-Integration

```jsx
import { onMount } from 'solid-js';
import { register } from 'swiper/element/bundle';
register();

function ThumbsExample() {
  let mainRef;
  let thumbsRef;

  onMount(() => {
    // Thumbs zuerst
    Object.assign(thumbsRef, {
      slidesPerView: 4,
      spaceBetween: 10,
      watchSlidesProgress: true,
      freeMode: true,
    });
    thumbsRef.initialize();

    // Dann Haupt-Swiper
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

## SolidJS-spezifische JSX-Hinweise

SolidJS kompiliert JSX direkt zu DOM-Operationen (kein Virtual DOM). Wichtig:

- `ref={refVar}` für Elementen-Referenz (kein Callback-Ref wie React)
- `on:eventname` für native Custom Events (lowercase)
- Attribute werden als echte DOM-Attribute gesetzt

```jsx
// SolidJS-spezifische Event-Syntax:
<swiper-container
  on:swiperslidechange={handler}  // Native Custom Event
  onClick={handler}               // Synthetischer Click-Event
/>
```

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
|---|---|
| `swiper-container` unbekannt | `register()` aufrufen, idealerweise einmalig in `index.jsx` |
| Styles fehlen | `import 'swiper/css'` sicherstellen |
| Events werden nicht gefeuert | SolidJS nutzt `on:eventname` für native DOM-Events |
| SSR-Fehler | Lazy import in `onMount` verwenden |
| Komplexe Params nicht übernommen | `init="false"` + `Object.assign` + `initialize()` |

---

*Quelle: https://swiperjs.com/solid + https://swiperjs.com/element — Swiper v12.2.0*
