# Swiper — Vollständige Event-Referenz (v11/12)

Events werden per `swiper.on(event, handler)`, `swiper.once(event, handler)`, oder direkt im Konstruktor via `on: { eventName: handler }` registriert.

```js
// Im Konstruktor
const swiper = new Swiper('.swiper', {
  on: {
    init(swiper) { /* ... */ },
    slideChange(swiper) { /* ... */ },
  }
});

// Nach der Initialisierung
swiper.on('slideChange', (swiper) => console.log(swiper.activeIndex));
swiper.once('transitionEnd', (swiper) => console.log('einmalig'));
swiper.onAny((eventName, ...args) => console.log(eventName, args));
```

---

## 1. Core-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `activeIndexChange` | `(swiper)` | Aktiver Index hat sich geändert. |
| `afterInit` | `(swiper)` | Direkt nach der Initialisierung. |
| `beforeDestroy` | `(swiper)` | Direkt bevor Swiper zerstört wird. |
| `beforeInit` | `(swiper)` | Direkt vor der Initialisierung. |
| `beforeLoopFix` | `(swiper)` | Direkt vor dem Loop-Fix. |
| `beforeResize` | `(swiper)` | Vor dem Resize-Handler. |
| `beforeSlideChangeStart` | `(swiper)` | Vor dem Start der Folien-Wechsel-Transition. |
| `beforeTransitionStart` | `(swiper, speed, internal)` | Vor dem Start einer Transition. `speed`: Transitions-Dauer, `internal`: interner Aufruf. |
| `breakpoint` | `(swiper, breakpointParams)` | Breakpoint hat sich geändert. `breakpointParams`: neue Parameter. |
| `changeDirection` | `(swiper)` | Richtung hat sich geändert. |
| `click` | `(swiper, event)` | Benutzer klickt/tippt auf Swiper. `event`: PointerEvent. |
| `destroy` | `(swiper)` | Swiper wird zerstört. |
| `doubleClick` | `(swiper, event)` | Doppelklick auf Swiper. `event`: PointerEvent. |
| `doubleTap` | `(swiper, event)` | Doppeltippen auf Container. `event`: PointerEvent. |
| `fromEdge` | `(swiper)` | Swiper verlässt eine Randposition. |
| `init` | `(swiper)` | Direkt nach der Initialisierung (nach `afterInit`). |
| `lock` | `(swiper)` | Swiper wird gesperrt (zu wenige Folien). |
| `loopFix` | `(swiper)` | Nach dem Loop-Fix. |
| `momentumBounce` | `(swiper)` | Momentum-Bounce ausgelöst. |
| `observerUpdate` | `(swiper)` | Observer hat DOM-Mutationen erkannt. |
| `orientationchange` | `(swiper)` | Geräteausrichtung hat sich geändert. |
| `progress` | `(swiper, progress)` | Wrapper-Fortschritt hat sich geändert. `progress`: aktueller Fortschritt (0–1). |
| `reachBeginning` | `(swiper)` | Swiper hat den Anfang erreicht. |
| `reachEnd` | `(swiper)` | Swiper hat die letzte Folie erreicht. |
| `realIndexChange` | `(swiper)` | Realer Index hat sich geändert. |
| `resize` | `(swiper)` | Fenster-Größe hat sich geändert. |
| `setTransition` | `(swiper, transition)` | Swiper-Animation startet. `transition`: Transitions-Dauer. |
| `setTranslate` | `(swiper, translate)` | Wrapper ändert seine Position. `translate`: aktueller Translate-Wert. |
| `slideChange` | `(swiper)` | Aktive Folie hat sich geändert. |
| `slideChangeTransitionEnd` | `(swiper)` | Animation nach Folienwechsel abgeschlossen. |
| `slideChangeTransitionStart` | `(swiper)` | Animation für Folienwechsel beginnt. |
| `slideNextTransitionEnd` | `(swiper)` | Wie `slideChangeTransitionEnd`, nur Vorwärts-Richtung. |
| `slideNextTransitionStart` | `(swiper)` | Wie `slideChangeTransitionStart`, nur Vorwärts-Richtung. |
| `slidePrevTransitionEnd` | `(swiper)` | Wie `slideChangeTransitionEnd`, nur Rückwärts-Richtung. |
| `slidePrevTransitionStart` | `(swiper)` | Wie `slideChangeTransitionStart`, nur Rückwärts-Richtung. |
| `slideResetTransitionEnd` | `(swiper)` | Reset-Animation abgeschlossen. |
| `slideResetTransitionStart` | `(swiper)` | Reset-Animation beginnt. |
| `sliderFirstMove` | `(swiper, event)` | Erste Touch-/Drag-Bewegung. `event`: PointerEvent. |
| `sliderMove` | `(swiper, event)` | Benutzer berührt und bewegt Finger. `event`: PointerEvent. |
| `slidesGridLengthChange` | `(swiper)` | Slides-Grid hat sich geändert. |
| `slidesLengthChange` | `(swiper)` | Anzahl der Folien hat sich geändert. |
| `slidesUpdated` | `(swiper)` | Folien wurden berechnet und aktualisiert. |
| `snapGridLengthChange` | `(swiper)` | Snap-Grid hat sich geändert. |
| `snapIndexChange` | `(swiper)` | Snap-Index hat sich geändert. |
| `tap` | `(swiper, event)` | Benutzer tippt auf Swiper (kein Doppeltippen). `event`: PointerEvent. |
| `toEdge` | `(swiper)` | Swiper erreicht eine Randposition. |
| `touchEnd` | `(swiper, event)` | Benutzer lässt Swiper los. `event`: PointerEvent. |
| `touchMove` | `(swiper, event)` | Benutzer berührt und bewegt Finger. `event`: PointerEvent. |
| `touchMoveOpposite` | `(swiper, event)` | Bewegung entgegen der Slider-Richtung. `event`: PointerEvent. |
| `touchStart` | `(swiper, event)` | Benutzer berührt Swiper. `event`: PointerEvent. |
| `transitionEnd` | `(swiper)` | Transition abgeschlossen. |
| `transitionStart` | `(swiper)` | Transition beginnt. |
| `unlock` | `(swiper)` | Swiper wird entsperrt. |
| `update` | `(swiper)` | `swiper.update()` wurde aufgerufen. |

---

## 2. Navigation-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `navigationHide` | `(swiper)` | Navigation wird ausgeblendet. |
| `navigationNext` | `(swiper)` | Weiter-Button wurde geklickt. |
| `navigationPrev` | `(swiper)` | Zurück-Button wurde geklickt. |
| `navigationShow` | `(swiper)` | Navigation wird eingeblendet. |

---

## 3. Pagination-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `paginationHide` | `(swiper)` | Pagination wird ausgeblendet. |
| `paginationRender` | `(swiper, paginationEl)` | Pagination wurde gerendert. `paginationEl`: HTMLElement. |
| `paginationShow` | `(swiper)` | Pagination wird eingeblendet. |
| `paginationUpdate` | `(swiper, paginationEl)` | Pagination wurde aktualisiert. `paginationEl`: HTMLElement. |

---

## 4. Scrollbar-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `scrollbarDragEnd` | `(swiper, event)` | Scrollbar-Drag beendet. `event`: PointerEvent. |
| `scrollbarDragMove` | `(swiper, event)` | Scrollbar wird gezogen. `event`: PointerEvent. |
| `scrollbarDragStart` | `(swiper, event)` | Scrollbar-Drag gestartet. `event`: PointerEvent. |

---

## 5. Autoplay-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `autoplay` | `(swiper)` | Folie wurde durch Autoplay gewechselt. |
| `autoplayPause` | `(swiper)` | Autoplay wurde pausiert. |
| `autoplayResume` | `(swiper)` | Autoplay wurde fortgesetzt. |
| `autoplayStart` | `(swiper)` | Autoplay wurde gestartet. |
| `autoplayStop` | `(swiper)` | Autoplay wurde gestoppt. |
| `autoplayTimeLeft` | `(swiper, timeLeft, percentage)` | Wird während des Autoplay-Countdowns ausgelöst. `timeLeft`: ms bis nächste Folie, `percentage`: 0–1 Fortschritt. |

```js
// Autoplay-Progress-Anzeige
swiper.on('autoplayTimeLeft', (s, timeLeft, percentage) => {
  progressCircle.style.setProperty('--progress', 1 - percentage);
  progressContent.textContent = `${Math.ceil(timeLeft / 1000)}s`;
});
```

---

## 6. Keyboard-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `keyPress` | `(swiper, keyCode)` | Taste wurde gedrückt. `keyCode`: KeyboardEvent.keyCode. |

---

## 7. Mousewheel-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `scroll` | `(swiper, event)` | Mausrad-Scroll-Event ausgelöst. `event`: WheelEvent. |

---

## 8. Zoom-Events

| Event | Argumente | Beschreibung |
|---|---|---|
| `zoomChange` | `(swiper, scale, imageEl, slideEl)` | Zoom-Level hat sich geändert. `scale`: aktueller Zoom-Faktor, `imageEl`: Bild-Element, `slideEl`: Folien-Element. |

---

## Event-Nutzungs-Beispiele

```js
// Lifecycle-Tracking
const swiper = new Swiper('.swiper', {
  on: {
    beforeInit(s) {
      console.log('vor Init');
    },
    init(s) {
      console.log('initialisiert, activeIndex:', s.activeIndex);
    },
    afterInit(s) {
      console.log('nach Init');
    },
  }
});

// Slide-Wechsel
swiper.on('slideChange', (s) => {
  console.log('aktive Folie:', s.activeIndex, 'realIndex:', s.realIndex);
});

// Rand-Erkennung
swiper.on('reachBeginning', () => console.log('erste Folie'));
swiper.on('reachEnd', () => console.log('letzte Folie'));
swiper.on('toEdge', () => console.log('Rand erreicht'));
swiper.on('fromEdge', () => console.log('Rand verlassen'));

// Touch-Events
swiper.on('touchStart', (s, event) => console.log('touch start', event.touches[0]));
swiper.on('touchMove', (s, event) => console.log('touch move'));
swiper.on('touchEnd', (s, event) => console.log('touch end'));

// Transition
swiper.on('transitionStart', () => console.log('transition start'));
swiper.on('transitionEnd', () => console.log('transition end'));
swiper.on('slideChangeTransitionStart', () => console.log('slide change start'));
swiper.on('slideChangeTransitionEnd', () => console.log('slide change end'));

// Fortschritt
swiper.on('progress', (s, progress) => {
  console.log('Fortschritt:', Math.round(progress * 100), '%');
});

// Breakpoint
swiper.on('breakpoint', (s, params) => {
  console.log('neuer Breakpoint, params:', params);
});

// Lazy Loading
swiper.on('lazyImageReady', (s, slideEl, imageEl) => {
  console.log('Bild geladen:', imageEl.src);
});

// Resize
swiper.on('resize', (s) => {
  console.log('Container-Größe geändert, Breite:', s.width);
});

// Observer
swiper.on('observerUpdate', (s) => {
  console.log('DOM-Mutation erkannt');
});
```

---

*Quelle: https://swiperjs.com/swiper-api*
