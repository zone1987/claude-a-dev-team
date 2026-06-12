# Swiper Element — Vollständige Referenz (Web Component)

Swiper Element sind native Custom Elements (registriert via `customElements.define`).
Verfügbar seit Swiper v9. Ersetzt die entfernten Framework-Adapter für Angular, Svelte und Solid.

---

## Installation & Registrierung

### NPM
```bash
npm install swiper
```

```javascript
// Bundle (alle Module enthalten, auto-styles)
import { register } from 'swiper/element/bundle';
register();

// Core only (leichtgewichtig, Module manuell einbinden)
import { register } from 'swiper/element';
register();
```

### CDN (auto-registriert, kein `register()` nötig)
```html
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-element-bundle.min.js"></script>
```

---

## Die zwei Custom Elements

| Element | Zweck |
|---|---|
| `<swiper-container>` | Haupt-Slider-Container mit allen Swiper-Parametern |
| `<swiper-slide>` | Einzelne Folie |

---

## Parameter als HTML-Attribute (kebab-case)

Alle Swiper-API-Parameter können als kebab-case-Attribute auf `<swiper-container>` gesetzt werden.

```html
<swiper-container
  slides-per-view="3"
  space-between="30"
  speed="500"
  loop="true"
  css-mode="true"
  centered-slides="true"
  navigation="true"
  pagination="true"
  scrollbar="true"
>
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <swiper-slide>Slide 3</swiper-slide>
</swiper-container>
```

### Verschachtelte Objekt-Parameter (Bracket-Notation im Attribut)

```html
<swiper-container
  grid-rows="3"
  mousewheel-force-to-axis="true"
  autoplay-delay="2500"
  autoplay-disable-on-interaction="false"
  pagination-clickable="true"
  navigation-next-el=".my-button-next"
  navigation-prev-el=".my-button-prev"
>
```

### Boolean-Attribute

Boolean-Parameter als String `"true"` oder `"false"` übergeben:
```html
<swiper-container loop="true" autoplay="true"></swiper-container>
```

---

## Komplexe Parameter via JavaScript-Properties

Für Parameter wie `breakpoints`, `pagination.renderBullet`, Arrays etc. direkt als JS-Properties setzen:

```javascript
const swiperEl = document.querySelector('swiper-container');

const params = {
  slidesPerView: 1,
  spaceBetween: 10,
  loop: true,
  // Komplexe Parameter — nur via Property möglich
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
    init() { console.log('initialized'); },
  },
};

Object.assign(swiperEl, params);
swiperEl.initialize();
```

**Wichtig:** Wenn `init="false"` nicht gesetzt ist, initialisiert sich `<swiper-container>` beim DOM-Ready automatisch. Für Property-Binding vor der Initialisierung:

```html
<swiper-container init="false">
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

```javascript
const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, { slidesPerView: 3, breakpoints: { ... } });
swiperEl.initialize(); // Manuell initialisieren
```

---

## Parameter nach Initialisierung aktualisieren

```javascript
const swiperEl = document.querySelector('swiper-container');

// Via Attribut (camelCase-Params → kebab-case-Attributname)
swiperEl.setAttribute('slides-per-view', '3');
swiperEl.setAttribute('space-between', '20');

// Via Property (camelCase direkt)
swiperEl.slidesPerView = 3;
swiperEl.spaceBetween = 20;
```

---

## Event System

### Standard-Events (v11+: Prefix `swiper` by default)

Alle Swiper-Events werden als DOM Custom Events gefeuert. Ab v11 sind Events standardmäßig mit dem Präfix `swiper` versehen:

| Swiper-API-Event | DOM-Event-Name (v11 default) |
|---|---|
| `slideChange` | `swiperslidechange` |
| `progress` | `swiperprogress` |
| `reachEnd` | `swiperreachend` |
| `reachBeginning` | `swiperreachbeginning` |
| `click` | `swiperclick` |
| `tap` | `swipetap` |
| `init` | `swiperinit` |
| `destroy` | `swiperdestroy` |
| `transitionStart` | `swipetransitionstart` |
| `transitionEnd` | `swipetransitionend` |
| `slideNextTransitionStart` | `swiperslideNextTransitionstart` |

Event-Argumente werden via `event.detail` übergeben (Array):

```javascript
const swiperEl = document.querySelector('swiper-container');

// Einfaches Event
swiperEl.addEventListener('swiperslidechange', (event) => {
  console.log('Slide changed');
  console.log(event.detail[0]); // Swiper-Instanz
});

// Event mit mehreren Parametern
swiperEl.addEventListener('swiperprogress', (event) => {
  const [swiper, progress] = event.detail;
  console.log(`Progress: ${progress}`);
});

swiperEl.addEventListener('swipetap', (event) => {
  const [swiper, pointerEvent] = event.detail;
});
```

### Event-Präfix anpassen

```html
<!-- Kein Präfix (Verhalten vor v11) -->
<swiper-container events-prefix="">
  <!-- Events: "slidechange", "progress", etc. -->
</swiper-container>

<!-- Benutzerdefinierter Präfix -->
<swiper-container events-prefix="swiper-">
  <!-- Events: "swiper-slidechange", "swiper-progress", etc. -->
</swiper-container>
```

---

## Swiper-Instanz & Methoden

```javascript
const swiperEl = document.querySelector('swiper-container');

// Nach Initialisierung: Swiper-Instanz via .swiper Property
const swiper = swiperEl.swiper;

// Alle Swiper-Methoden verfügbar
swiper.slideNext();
swiper.slidePrev();
swiper.slideTo(3);
swiper.slideToLoop(3);
swiper.update();
swiper.destroy();
swiper.autoplay.start();
swiper.autoplay.stop();
swiper.pagination.render();
swiper.pagination.update();

// Eigenschaften
console.log(swiper.activeIndex);
console.log(swiper.realIndex);
console.log(swiper.slides);
console.log(swiper.isBeginning);
console.log(swiper.isEnd);
```

---

## Slots

Inhalt innerhalb `<swiper-container>` positionieren (außerhalb des `.swiper-wrapper`):

```html
<swiper-container>
  <!-- Vor dem swiper-wrapper -->
  <div slot="container-start">Dieser Inhalt kommt vor den Slides</div>

  <!-- Normale Slides (kein slot-Attribut) -->
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>

  <!-- Nach dem swiper-wrapper -->
  <div slot="container-end">Dieser Inhalt kommt nach den Slides</div>

  <!-- Vor dem swiper-wrapper (innerhalb wrapper) -->
  <div slot="wrapper-start">Im Wrapper, vor Slides</div>

  <!-- Nach dem swiper-wrapper (innerhalb wrapper) -->
  <div slot="wrapper-end">Im Wrapper, nach Slides</div>
</swiper-container>
```

---

## CSS & Shadow DOM

### CSS Parts (Shadow DOM Styling ohne `::slotted`)

```css
/* Container */
swiper-container::part(container) { }

/* Wrapper */
swiper-container::part(wrapper) { }

/* Navigation */
swiper-container::part(button-prev) { background-color: blue; }
swiper-container::part(button-next) { background-color: blue; }

/* Pagination */
swiper-container::part(pagination) { }
swiper-container::part(bullet) { background-color: grey; }
swiper-container::part(bullet-active) { background-color: red; }

/* Scrollbar */
swiper-container::part(scrollbar) { }
swiper-container::part(scrollbar-drag) { }
```

### Styles in Shadow DOM injizieren (`injectStyles`)

CSS-Strings direkt in den Shadow DOM scope injizieren:

```javascript
const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, {
  injectStyles: [
    `
    :host(.red) .swiper-wrapper {
      background-color: red;
    }
    .swiper-button-next,
    .swiper-button-prev {
      color: white;
      background: rgba(0,0,0,0.3);
      padding: 8px;
      border-radius: 50%;
    }
    `,
  ],
  injectStylesUrls: [
    'path/to/custom-navigation.css',
    'path/to/custom-pagination.css',
  ],
});
swiperEl.initialize();
```

---

## Auto-Render Navigation/Pagination/Scrollbar

```html
<!-- Automatisch generierte UI-Elemente -->
<swiper-container
  navigation="true"
  pagination="true"
  scrollbar="true"
>
  <swiper-slide>Slide 1</swiper-slide>
</swiper-container>
```

---

## Thumbs-Integration (CSS-Selektor)

```html
<!-- Thumbs-Swiper (kein JS nötig bei einfacher Konfiguration) -->
<swiper-container
  thumbs-swiper=".my-thumbs"
  loop="true"
  space-between="10"
>
  <swiper-slide><img src="img1.jpg" /></swiper-slide>
  <swiper-slide><img src="img2.jpg" /></swiper-slide>
</swiper-container>

<swiper-container
  class="my-thumbs"
  slides-per-view="4"
  space-between="10"
  watch-slides-progress="true"
>
  <swiper-slide><img src="img1.jpg" /></swiper-slide>
  <swiper-slide><img src="img2.jpg" /></swiper-slide>
</swiper-container>
```

---

## Virtual Slides

```html
<swiper-container virtual="true" slides-per-view="3">
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <!-- Weitere Slides -->
</swiper-container>
```

---

## Lazy Loading

```html
<swiper-container>
  <swiper-slide lazy="true">
    <img src="image.jpg" loading="lazy" />
  </swiper-slide>
</swiper-container>
```

---

## Core vs. Bundle

### Bundle (empfohlen für die meisten Fälle)
```javascript
import { register } from 'swiper/element/bundle';
register();
// Alle Module + Styles enthalten
```

### Core (minimales Bundle, Module manuell)
```javascript
import { register } from 'swiper/element';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';
register();

const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, {
  modules: [Navigation, Pagination, Autoplay],
  injectStylesUrls: [
    'swiper/css/navigation',
    'swiper/css/pagination',
  ],
  navigation: true,
  pagination: { clickable: true },
});
swiperEl.initialize();
```

---

## Custom Plugin-Parameter registrieren (v9.1.0+)

```javascript
// Eigene Plugin-Parameter bekannt machen, damit sie als Attribute erkannt werden
window.SwiperElementRegisterParams(['myParam', 'anotherParam']);

const swiperEl = document.querySelector('swiper-container');
// Jetzt als Attribut nutzbar:
swiperEl.setAttribute('my-param', 'value');
```

---

## Framework-Integration Übersicht

| Framework | Empfehlung | Hinweis |
|---|---|---|
| Angular | Swiper Element | `CUSTOM_ELEMENTS_SCHEMA` im Modul/Component |
| Svelte | Swiper Element | `bind:this`, Events mit `on:swiper*` |
| Solid | Swiper Element | `ref`, `addEventListener` |
| React | Swiper React-Komponenten ODER Element | Element in React mit `useRef` + `addEventListener` |
| Vue | Swiper Vue-Komponenten ODER Element | Element in Vue mit `:` und `@` nativ |

---

## Vergleich: Swiper Element vs. Swiper Core (Klasse)

| Merkmal | Swiper Element | Swiper Core |
|---|---|---|
| Initialisierung | HTML-Tag + auto/`initialize()` | `new Swiper('.selector', options)` |
| Parameter | HTML-Attribute (kebab) + JS-Properties | JS-Objekt im Konstruktor |
| Events | DOM Custom Events (lowercase + prefix) | `.on('eventName', fn)` |
| Zugriff | `.swiper`-Property des Elements | Direkte Instanz-Variable |
| Shadow DOM | Ja (CSS Parts, injectStyles) | Nein |
| Framework-Neutral | Ja | Nein (JS-only) |
| Bundle-Größe | Etwas größer | Kleiner (Core-only möglich) |

---

*Quelle: https://swiperjs.com/element — Swiper v12.2.0*
