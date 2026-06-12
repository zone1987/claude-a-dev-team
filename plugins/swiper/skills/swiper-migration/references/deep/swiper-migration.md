# Swiper Migration Guide — v9, v10, v11

Alle Breaking Changes je Hauptversion mit Vorher/Nachher-Codebeispielen.

---

## Migration auf Swiper v11

Offizielle Seite: https://swiperjs.com/migration-guide-v11

### 1. `loopedSlides`-Parameter entfernt

Der Parameter `loopedSlides` wurde entfernt.

```javascript
// ALT (v10):
const swiper = new Swiper('.swiper', {
  loop: true,
  loopedSlides: 5, // ENTFERNT
});

// NEU (v11):
const swiper = new Swiper('.swiper', {
  loop: true,
  loopAdditionalSlides: 5, // Neuer Parameter (wenn nötig)
});
```

### 2. Element Events Präfix (BREAKING: Standard geändert)

Ab v11 haben alle Swiper-Element-Events standardmäßig den Präfix `swiper`.

```javascript
// ALT (v10 — kein Präfix):
swiperEl.addEventListener('slidechange', handler);
swiperEl.addEventListener('progress', handler);
swiperEl.addEventListener('reachend', handler);

// NEU (v11 — Präfix "swiper" by default):
swiperEl.addEventListener('swiperslidechange', handler);
swiperEl.addEventListener('swiperprogress', handler);
swiperEl.addEventListener('swiperreachend', handler);
```

Altes Verhalten beibehalten (kein Präfix):
```html
<swiper-container events-prefix="">
  <!-- Events: "slidechange", "progress" wie in v10 -->
</swiper-container>
```

```javascript
Object.assign(swiperEl, {
  eventsPrefix: '', // Kein Präfix
});
```

### 3. Container `overflow` CSS-Standard

Der Container hat jetzt `overflow: hidden` als Standard.

```css
/* Falls alte Layouts brechen — eigene Überschreibung: */
.swiper {
  overflow: clip; /* oder: overflow: visible */
}
```

---

## Migration auf Swiper v10

Offizielle Seite: https://swiperjs.com/migration-guide-v10

### 1. Modul-Imports (MAJOR BREAKING CHANGE)

```javascript
// ALT (v9):
import Swiper, { Navigation, Pagination, Autoplay } from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/react';

// NEU (v10):
import Swiper from 'swiper';
import { Navigation, Pagination, Autoplay } from 'swiper/modules'; // NEUER PFAD
import { Swiper, SwiperSlide } from 'swiper/react'; // Gleich
```

### 2. Swiper Element DOM-Struktur geändert

v10 fügte eine zusätzliche `.swiper`-Wrapper-Div ein:

**v9 Shadow DOM-Struktur:**
```html
<swiper-container>
  #shadow-root
    <div class="swiper-wrapper">
      <slot />   ← Slides landen hier direkt
    </div>
</swiper-container>
```

**v10 Shadow DOM-Struktur:**
```html
<swiper-container>
  #shadow-root
    <div class="swiper">          ← NEU: Extra Wrapper
      <div class="swiper-wrapper">
        <slot />
      </div>
    </div>
</swiper-container>
```

Code, der direkt auf Shadow-DOM-Internals zugreift, muss angepasst werden.

### 3. Swiper Element injiziert keine globalen Styles mehr

```javascript
// ALT (v9 — Swiper Element injizierte Styles global):
// Keine zusätzliche Aktion nötig

// NEU (v10 — Styles nur noch im Shadow DOM):
// Eigene Navigation/Pagination/Scrollbar-Elemente brauchen eigene Styles:
Object.assign(swiperEl, {
  injectStyles: [`
    .swiper-button-next,
    .swiper-button-prev {
      /* Eigene Styles */
    }
  `],
});
```

### 4. Paketstruktur geändert

```javascript
// ALT (v9 — direkte Dateipfade):
import Swiper from 'swiper/swiper.esm.js';
import 'swiper/swiper.min.css';

// NEU (v10 — neue Pfade):
import Swiper from 'swiper';                    // Paket-Root
import 'swiper/css';                            // Core CSS
import { Navigation } from 'swiper/modules';   // Module
```

- `.esm.js` → `.mjs` (Extension geändert)
- `.browser.esm.js` → `.mjs` (vereinheitlicht)
- Alle Module-Dateien wurden verschoben

### 5. CSS-Import-Pfade

```javascript
// ALT (v9):
import 'swiper/css/swiper.css';
import 'swiper/swiper-bundle.css';

// NEU (v10):
import 'swiper/css';
import 'swiper/css/bundle';     // Bundle (alle Module)
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-fade';
// etc.
```

---

## Migration auf Swiper v9

Offizielle Seite: https://swiperjs.com/migration-guide-v9

### 1. Touch Events entfernt — nur noch Pointer Events

```javascript
// ALT (v8 — Touch Events):
swiper.on('touchStart', handler);
swiper.on('touchMove', handler);
swiper.on('touchEnd', handler);

// NEU (v9 — Pointer Events):
swiper.on('pointerDown', handler);   // statt touchStart
swiper.on('pointerMove', handler);   // statt touchMove
swiper.on('pointerUp', handler);     // statt touchEnd
// Oder auf nativen DOM-Events lauschen statt Swiper-Events
```

### 2. Autoplay-Modul komplett überarbeitet

```javascript
// ALT (v8):
const swiper = new Swiper('.swiper', {
  autoplay: {
    delay: 3000,
    stopOnLastSlide: true,      // UMBENANNT
    disableOnInteraction: false,
    reverseDirection: false,    // NEU in v9
    waitForTransition: true,
  },
});

// v8 Events:
swiper.on('autoplayStart', () => {});
swiper.on('autoplayStop', () => {});

// NEU (v9):
const swiper = new Swiper('.swiper', {
  autoplay: {
    delay: 3000,
    stopOnLastSlide: false,      // Gleich
    disableOnInteraction: false, // Gleich
    reverseDirection: false,
    waitForTransition: true,
  },
});

// v9 Events (neue Namen):
swiper.on('autoplayStart', () => {});     // Gleich
swiper.on('autoplayStop', () => {});      // Gleich
swiper.on('autoplayTimeLeft', (s, time, progress) => {}); // NEU
```

### 3. Loop-Modus neu implementiert

```javascript
// ALT (v8 — Loop via Slide-Duplikate):
const swiper = new Swiper('.swiper', {
  loop: true,
  loopedSlides: 3,     // Anzahl zu duplizierender Slides
  loopAdditionalSlides: 0,
});

// NEU (v9 — Loop ohne Duplikate, dynamische Umsortierung):
const swiper = new Swiper('.swiper', {
  loop: true,
  // loopedSlides: 3,  // Andere Semantik jetzt!
  // Bedingung: slides.length >= slidesPerView * 2
});
```

### 4. Lazy Loading ins Core integriert

```javascript
// ALT (v8 — eigenes Lazy-Modul):
import Swiper, { Lazy } from 'swiper';
const swiper = new Swiper('.swiper', {
  modules: [Lazy],
  lazy: {
    loadPrevNext: true,
  },
  preloadImages: false,
});

// NEU (v9 — Lazy im Core, kein Modul-Import):
const swiper = new Swiper('.swiper', {
  lazy: true,
  // ODER:
  lazy: {
    loadPrevNext: true,
    loadPrevNextAmount: 2,
  },
});
```

HTML-Attribut für Lazy-Bilder bleibt gleich:
```html
<!-- Lazy-Loading-Bild: -->
<img data-src="path/to/image.jpg" class="swiper-lazy" />
```

### 5. Dom7 entfernt

```javascript
// ALT (v8 — Dom7 verfügbar):
import { $ } from 'swiper/dom7';
import { $ } from 'swiper/utils/dom7';

// NEU (v9 — Dom7 entfernt, Vanilla JS verwenden):
// Kein Import mehr möglich
// Statt: swiper.$el.addClass('active')
// Jetzt: swiper.el.classList.add('active')
```

### 6. Framework-Adapter entfernt

```javascript
// ALT (v8):
import { SwiperModule } from 'swiper/angular';
import { Swiper, SwiperSlide } from 'swiper/svelte';
import { Swiper, SwiperSlide } from 'swiper/solid';

// NEU (v9): Framework-Adapter ENTFERNT
// Lösung: Swiper Element (Web Component) verwenden
import { register } from 'swiper/element/bundle';
register();
// <swiper-container>/<swiper-slide> als Custom Elements

// React und Vue bleiben erhalten:
import { Swiper, SwiperSlide } from 'swiper/react'; // Weiterhin OK
import { Swiper, SwiperSlide } from 'swiper/vue';   // Weiterhin OK
```

### 7. Entfernte Parameter (v9)

| Entfernter Parameter | Alternative |
|---|---|
| `swipeHandler` | Entfernt, kein Ersatz |
| `iOSEdgeSwipeDetection` | Entfernt |
| `iOSEdgeSwipeThreshold` | Entfernt |
| `passiveListeners` | Immer passiv in v9 |
| `uniqueNavElements` | Entfernt |
| `preloadImages` | Entfernt (Lazy im Core) |
| `watchSlidesVisibility` | Umbenannt zu `watchSlidesProgress` |

---

## Gesamtübersicht Breaking Changes

| Version | Größte Änderungen |
|---|---|
| v11 | `loopedSlides` entfernt, Element-Events Präfix `swiper` als Standard |
| v10 | Module-Imports auf `swiper/modules`, Element DOM-Struktur, CSS-Pfade |
| v9 | Touch→Pointer Events, Lazy ins Core, Dom7 entfernt, Angular/Svelte/Solid Adapter entfernt, Loop neu |

---

## Schnell-Checkliste für Upgrade auf v11

```text
[ ] loopedSlides → loopAdditionalSlides
[ ] Swiper Element Events: "slidechange" → "swiperslidechange"
[ ] Container-Overflow prüfen (falls clip-Verhalten nötig)
```

## Schnell-Checkliste für Upgrade auf v10

```text
[ ] import { Navigation } from 'swiper' → from 'swiper/modules'
[ ] CSS-Imports anpassen: 'swiper/css/swiper.css' → 'swiper/css'
[ ] Swiper Element Shadow DOM Anpassungen (falls direkte DOM-Zugriffe)
[ ] Swiper Element globale Styles → injectStyles
```

## Schnell-Checkliste für Upgrade auf v9

```text
[ ] Angular/Svelte/Solid Adapter → Swiper Element
[ ] Touch Events → Pointer Events
[ ] Lazy Modul → Kein Modul-Import mehr
[ ] Dom7 → Vanilla JS
[ ] Loop: slides.length >= slidesPerView * 2 sicherstellen
[ ] Autoplay API prüfen (neue Parameter/Events)
```

---

*Quellen:*
- *https://swiperjs.com/migration-guide-v11*
- *https://swiperjs.com/migration-guide-v10*
- *https://swiperjs.com/migration-guide-v9*
- *Swiper v12.2.0*
