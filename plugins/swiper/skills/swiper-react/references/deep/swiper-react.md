# Swiper React — Vollständige Referenz

Swiper React-Komponenten sind offiziell unterstützt und in `swiper/react` enthalten.
Kompatibel mit React 18+.

---

## Installation

```bash
npm install swiper
```

---

## Basis-Import

```jsx
import { Swiper, SwiperSlide } from 'swiper/react';

// Core-CSS (immer nötig)
import 'swiper/css';

// Modul-spezifische CSS-Dateien
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

// Oder alles auf einmal (Bundle)
import 'swiper/css/bundle';
```

---

## Minimales Beispiel

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

## `<Swiper>` — Props

Alle [Swiper API-Parameter](https://swiperjs.com/swiper-api#parameters) sind als Props verfügbar (camelCase).

### Zusätzliche React-spezifische Props

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML-Element des Containers |
| `wrapperTag` | `string` | `'div'` | HTML-Element des Wrappers |
| `onSwiper` | `(swiper: Swiper) => void` | — | Callback mit Swiper-Instanz nach Init |
| `modules` | `SwiperModule[]` | — | Array der einzubindenden Module |

### Häufige Parameter als Props

```jsx
<Swiper
  // Allgemein
  slidesPerView={1}
  spaceBetween={10}
  speed={400}
  loop={true}
  centeredSlides={true}
  direction="horizontal" // oder "vertical"
  
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
  
  // Freier Modus
  freeMode={true}
  
  // Grid
  grid={{ rows: 2 }}
  
  // Effekte
  effect="fade" // "slide"|"fade"|"cube"|"coverflow"|"flip"|"cards"|"creative"
  fadeEffect={{ crossFade: true }}
  
  // Keyboard
  keyboard={{ enabled: true }}
  
  // Mousewheel
  mousewheel={true}
  
  // Lazy Loading
  lazy={true}
>
```

---

## Events als `onXxx`-Props

Jeder Swiper-API-Event ist als Prop verfügbar (Format: `on` + EventName mit Großbuchstabe):

| Swiper-Event | React-Prop |
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

## `<SwiperSlide>` — Props

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `tag` | `string` | `'div'` | HTML-Element des Slides |
| `zoom` | `boolean` | `false` | Zoom-Wrapper aktivieren |
| `virtualIndex` | `number` | — | Index für Virtual Slides (Pflicht) |

---

## Render-Funktion (Slide State)

`SwiperSlide` akzeptiert eine Render-Funktion, die Zustandsvariablen bereitstellt:

```jsx
<SwiperSlide>
  {({ isActive, isPrev, isNext, isVisible, isDuplicate }) => (
    <div className={isActive ? 'slide active' : 'slide'}>
      {isActive && <span>Aktuell aktiv</span>}
      {isNext && <span>Nächster Slide</span>}
      {isPrev && <span>Vorheriger Slide</span>}
    </div>
  )}
</SwiperSlide>
```

| Variable | Bedeutung |
|---|---|
| `isActive` | Dieser Slide ist aktiv |
| `isPrev` | Vorheriger Slide |
| `isNext` | Nächster Slide |
| `isVisible` | Sichtbar (benötigt `watchSlidesProgress`) |
| `isDuplicate` | Duplikat im Loop-Modus |

---

## Hooks

### `useSwiper`

Zugriff auf Swiper-Instanz innerhalb von Kindkomponenten:

```jsx
import { useSwiper } from 'swiper/react';

function SlideNavigation() {
  const swiper = useSwiper();

  return (
    <div>
      <button onClick={() => swiper.slidePrev()}>Zurück</button>
      <button onClick={() => swiper.slideNext()}>Vor</button>
      <button onClick={() => swiper.slideTo(0)}>Anfang</button>
    </div>
  );
}

// Innerhalb von <Swiper> verwenden:
<Swiper>
  <SwiperSlide>Slide 1</SwiperSlide>
  <SlideNavigation />
</Swiper>
```

### `useSwiperSlide`

Slide-Zustand innerhalb einer Slide-Kindkomponente:

```jsx
import { useSwiperSlide } from 'swiper/react';

function SlideContent() {
  const swiperSlide = useSwiperSlide();
  // swiperSlide.isActive, .isPrev, .isNext, .isVisible, .isDuplicate

  return (
    <div>
      {swiperSlide.isActive ? 'Aktiver Slide' : 'Inaktiver Slide'}
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

## Slots (Content-Injection)

Spezielle Slots für Inhalt außerhalb des Wrappers:

```jsx
<Swiper>
  {/* container-start: vor dem swiper-wrapper */}
  <div slot="container-start">Oben</div>

  <SwiperSlide>Slide 1</SwiperSlide>
  <SwiperSlide>Slide 2</SwiperSlide>

  {/* container-end: nach dem swiper-wrapper */}
  <div slot="container-end">Unten</div>

  {/* wrapper-start / wrapper-end: innerhalb des Wrappers */}
  <div slot="wrapper-start">Wrapper Start</div>
  <div slot="wrapper-end">Wrapper End</div>
</Swiper>
```

---

## Module einbinden

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

### Alle verfügbaren Module

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

## Controller (synchronisierte Swiper)

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

## Thumbs (Vorschaubilder)

```jsx
import { Thumbs, FreeMode } from 'swiper/modules';
import { useState } from 'react';
import 'swiper/css/thumbs';
import 'swiper/css/free-mode';

function ThumbsSwiper() {
  const [thumbsSwiper, setThumbsSwiper] = useState(null);

  return (
    <>
      {/* Haupt-Swiper */}
      <Swiper
        modules={[Thumbs]}
        thumbs={{ swiper: thumbsSwiper }}
        spaceBetween={10}
      >
        <SwiperSlide><img src="img1.jpg" /></SwiperSlide>
        <SwiperSlide><img src="img2.jpg" /></SwiperSlide>
      </Swiper>

      {/* Thumbs-Swiper */}
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

## Effekte

```jsx
import { EffectCards } from 'swiper/modules';
import 'swiper/css/effect-cards';

<Swiper modules={[EffectCards]} effect="cards" grabCursor>
  <SwiperSlide>Slide 1</SwiperSlide>
  <SwiperSlide>Slide 2</SwiperSlide>
</Swiper>
```

Alle Effekte: `"slide"` | `"fade"` | `"cube"` | `"coverflow"` | `"flip"` | `"cards"` | `"creative"`

---

## Swiper-Instanz via Ref (alternative zu `onSwiper`)

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

*Quelle: https://swiperjs.com/react — Swiper v12.2.0*
