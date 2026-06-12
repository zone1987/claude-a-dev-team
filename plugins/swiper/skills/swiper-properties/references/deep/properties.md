# Swiper — Vollständige Properties-Referenz (v11/12)

Alle Properties sind auf der Swiper-Instanz verfügbar. Die meisten sind read-only; `allowSlideNext`, `allowSlidePrev`, `allowTouchMove` sind read-write.

```js
const swiper = new Swiper('.swiper', { ... });
console.log(swiper.activeIndex);  // aktueller Folien-Index
```

---

## 1. Core-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `activeIndex` | `number` | Index der aktuell aktiven Folie. Im Loop-Modus enthält er den Index inklusive der geklonten Folien; für den "echten" Index `realIndex` nutzen. |
| `allowSlideNext` | `boolean` | Steuert ob zur nächsten Folie gewechselt werden kann. Lese-/Schreibbar: `swiper.allowSlideNext = false`. |
| `allowSlidePrev` | `boolean` | Steuert ob zur vorherigen Folie gewechselt werden kann. Lese-/Schreibbar. |
| `allowTouchMove` | `boolean` | Steuert ob Touch/Maus-Wischgesten möglich sind. Lese-/Schreibbar. |
| `animating` | `boolean` | `true` wenn Swiper gerade in einer Transition ist. |
| `clickedIndex` | `number` | Index der zuletzt geklickten Folie. |
| `clickedSlide` | `HTMLElement` | HTMLElement der zuletzt geklickten Folie. |
| `defaults` | `SwiperOptions` | Globale Standard-Optionen (statisch). |
| `el` | `HTMLElement` | Container-HTMLElement des Sliders. |
| `enabled` | `boolean` | `true` wenn Swiper aktiviert ist. |
| `extendedDefaults` | `SwiperOptions` | Objekt mit global erweiterten Swiper-Optionen. |
| `height` | `number` | Aktuelle Höhe des Containers in px. |
| `isBeginning` | `boolean` | `true` wenn Swiper ganz links/oben ist. |
| `isEnd` | `boolean` | `true` wenn Swiper ganz rechts/unten ist. |
| `isLocked` | `boolean` | `true` wenn Swiper gesperrt ist (zu wenige Folien für `slidesPerView`). |
| `originalParams` | `SwiperOptions` | Ursprüngliche Initialisierungsparameter (unverändertes Objekt). |
| `params` | `SwiperOptions` | Aktive Konfiguration (kann durch Breakpoints abweichen). |
| `previousIndex` | `number` | Index der zuletzt aktiven Folie. |
| `progress` | `number` | Fortschritt des Wrapper-Translates von 0 (Anfang) bis 1 (Ende). |
| `realIndex` | `number` | Index der aktiven Folie bereinigt um geklonte Loop-Folien. Im nicht-Loop-Modus identisch mit `activeIndex`. |
| `slides` | `HTMLElement[]` | Array aller Folien-HTMLElements. |
| `slidesEl` | `HTMLElement` | Wrapper-HTMLElement (identisch mit `wrapperEl`). |
| `slidesGrid` | `number[]` | Array der berechneten Positionen jeder Folie. |
| `slidesSizesGrid` | `number[]` | Array der Breiten (horizontal) oder Höhen (vertikal) jeder Folie in px. |
| `snapGrid` | `number[]` | Snap-Punkte des Sliders. |
| `snapIndex` | `number` | Index des aktuellen Snap-Punktes in `snapGrid`. |
| `swipeDirection` | `'next' \| 'prev' \| undefined` | Aktuelle Wisch-Richtung. |
| `touches` | `object` | Objekt mit Touch-Event-Werten: `startX`, `startY`, `currentX`, `currentY`, `diff`. |
| `translate` | `number` | Aktueller Translate-Wert des Wrappers in px (negativ bei normalem Schieben nach links). |
| `width` | `number` | Aktuelle Breite des Containers in px. |
| `wrapperEl` | `HTMLElement` | Wrapper-HTMLElement (das Element mit `swiper-wrapper`-Klasse). |

---

## 2. Navigation-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.navigation.nextEl` | `HTMLElement` | HTMLElement des Weiter-Buttons. |
| `swiper.navigation.prevEl` | `HTMLElement` | HTMLElement des Zurück-Buttons. |

---

## 3. Pagination-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.pagination.bullets` | `HTMLElement[]` | Array aller Pagination-Bullet-HTMLElements. |
| `swiper.pagination.el` | `HTMLElement` | HTMLElement des Pagination-Containers. |

---

## 4. Scrollbar-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.scrollbar.dragEl` | `HTMLElement` | HTMLElement des ziehbaren Scrollbar-Handles. |
| `swiper.scrollbar.el` | `HTMLElement` | HTMLElement des Scrollbar-Containers. |

---

## 5. Autoplay-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.autoplay.paused` | `boolean` | `true` wenn Autoplay pausiert ist. |
| `swiper.autoplay.running` | `boolean` | `true` wenn Autoplay aktiviert ist und läuft. |
| `swiper.autoplay.timeLeft` | `number` | Wenn pausiert: verbleibende Zeit in ms bis zur nächsten Transition. |

---

## 6. Thumbs-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.thumbs.swiper` | `Swiper` | Swiper-Instanz des Thumbs-Swipers. |

---

## 7. Zoom-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.zoom.enabled` | `boolean` | `true` wenn das Zoom-Modul aktiviert ist. |
| `swiper.zoom.scale` | `number` | Aktueller Zoom-Faktor des Bildes. |

---

## 8. Keyboard-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.keyboard.enabled` | `boolean` | `true` wenn Tastatursteuerung aktiviert ist. |

---

## 9. Mousewheel-Properties

| Property | Typ | Beschreibung |
|---|---|---|
| `swiper.mousewheel.enabled` | `boolean` | `true` wenn Mausrad-Steuerung aktiviert ist. |

---

## Nutzungsbeispiele

```js
const swiper = new Swiper('.swiper', { loop: true });

// Indices
console.log(swiper.activeIndex);    // z.B. 3 (mit geklonten Loop-Folien)
console.log(swiper.realIndex);      // z.B. 1 (echter Index ohne Klone)
console.log(swiper.previousIndex);  // letzter aktiver Index

// Grenzprüfung
if (swiper.isBeginning) console.log('Erste Folie');
if (swiper.isEnd) console.log('Letzte Folie');
if (swiper.isLocked) console.log('Nicht genug Folien zum Wischen');

// Geometrie
console.log(swiper.width, swiper.height);       // Container-Dimensionen
console.log(swiper.translate);                   // aktueller Wrapper-Offset
console.log(swiper.progress);                    // 0..1
console.log(swiper.slides.length);               // Anzahl Folien (inkl. Klone)

// DOM-Zugriff
swiper.el.classList.add('active');
swiper.wrapperEl.style.transitionDuration = '0ms';
swiper.slides[swiper.activeIndex].style.opacity = '1';

// Grid-Daten
console.log(swiper.slidesGrid);      // [0, 320, 640, ...]
console.log(swiper.slidesSizesGrid); // [310, 310, 310, ...]
console.log(swiper.snapGrid);        // Snap-Punkte

// Touch-Daten
swiper.on('touchMove', (s, e) => {
  console.log('touchStart X:', s.touches.startX);
  console.log('current X:',    s.touches.currentX);
  console.log('diff:',         s.touches.diff);
});

// Richtung ermitteln
swiper.on('sliderMove', (s) => {
  console.log('wische:', s.swipeDirection); // 'next' oder 'prev'
});

// Dynamische Steuerung
swiper.allowSlideNext = false;  // Vorwärts sperren
swiper.allowSlidePrev = false;  // Rückwärts sperren
swiper.allowTouchMove = false;  // Touch deaktivieren

// Autoplay-Zustand
if (swiper.autoplay.running) {
  console.log('läuft, nächste Folie in', swiper.autoplay.timeLeft, 'ms');
}

// Zoom
console.log('Zoom-Faktor:', swiper.zoom.scale);

// Aktive Parameter (u.U. durch Breakpoints geändert)
console.log('slidesPerView:', swiper.params.slidesPerView);
```

---

*Quelle: https://swiperjs.com/swiper-api*
