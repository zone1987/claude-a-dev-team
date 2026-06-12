# Swiper — Vollständige Methoden-Referenz (v11/12)

Alle Methoden werden auf der Swiper-Instanz aufgerufen: `const swiper = new Swiper(...)`.

---

## 1. Core-Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `attachEvents()` | — | `void` | Alle Event-Listener erneut hinzufügen. |
| `changeDirection(direction?, needUpdate?)` | `direction: 'horizontal' \| 'vertical'` (optional), `needUpdate: boolean` (default `true`) | `Swiper` | Slider-Richtung von horizontal zu vertikal oder umgekehrt ändern. |
| `changeLanguageDirection(direction)` | `direction: 'rtl' \| 'ltr'` | `void` | Sprachrichtung des Sliders ändern. |
| `destroy(deleteInstance?, cleanStyles?)` | `deleteInstance: boolean` (default `true`), `cleanStyles: boolean` (default `true`) | `void` | Swiper-Instanz zerstören und alle Event-Listener entfernen. |
| `detachEvents()` | — | `void` | Alle Event-Listener entfernen. |
| `disable()` | — | `void` | Swiper deaktivieren (wenn er aktiviert war). |
| `emit(event, ...args)` | `event: string`, `args: any` | `void` | Event auf der Instanz manuell auslösen. |
| `enable()` | — | `void` | Swiper aktivieren (wenn er deaktiviert war). |
| `extendDefaults(options)` | `options: SwiperOptions` | `void` | Globale Swiper-Standardwerte erweitern (statisch). |
| `getTranslate()` | — | `number` | Aktuellen CSS3-Transform-Translate-Wert des Wrappers zurückgeben. |
| `init(el?)` | `el: HTMLElement` | `Swiper` | Slider initialisieren (wenn `init: false` gesetzt). |
| `maxTranslate()` | — | `number` | Maximalen Translate-Wert zurückgeben. |
| `minTranslate()` | — | `number` | Minimalen Translate-Wert zurückgeben. |
| `off(event, handler)` | `event: string`, `handler: function` | `Swiper` | Event-Handler entfernen. |
| `offAny(handler)` | `handler: function` | `Swiper` | Listener für alle Events entfernen. |
| `on(event, handler)` | `event: string`, `handler: function` | `Swiper` | Event-Handler hinzufügen. |
| `onAny(handler)` | `handler: function` | `Swiper` | Listener der bei jedem Event feuert hinzufügen. |
| `once(event, handler)` | `event: string`, `handler: function` | `Swiper` | Event-Handler hinzufügen der nach einmaligem Auslösen entfernt wird. |
| `setGrabCursor()` | — | `void` | Grab-Cursor setzen. |
| `setProgress(progress, speed?)` | `progress: number` (0–1), `speed: number` (ms) | `void` | Swiper-Translate-Fortschritt setzen. |
| `setTranslate(translate)` | `translate: number` | `void` | Eigenen CSS3-Transform-Translate-Wert setzen. |
| `slideNext(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Zur nächsten Folie wechseln. |
| `slidePrev(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Zur vorherigen Folie wechseln. |
| `slideReset(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Zur aktuell aktiven Folie zurücksetzen. |
| `slideTo(index, speed?, runCallbacks?)` | `index: number`, `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Zu Folie mit dem angegebenen Index wechseln. |
| `slideToClosest(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Zur nächstgelegenen Folie / zum nächsten Snap-Punkt. |
| `slideToLoop(index, speed?, runCallbacks?)` | `index: number`, `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Im Loop-Modus zu `realIndex === index` wechseln. |
| `slidesPerViewDynamic()` | — | `number` | Dynamisch berechnete Anzahl sichtbarer Folien zurückgeben. |
| `translateTo(translate, speed, runCallbacks?, translateBounds?)` | `translate: number` (px), `speed: number` (ms), `runCallbacks: boolean` (default `true`), `translateBounds: boolean` (default `true`) | `void` | Eigenen CSS3-Transform-Translate-Wert animieren. |
| `unsetGrabCursor()` | — | `void` | Grab-Cursor entfernen. |
| `update()` | — | `void` | Nach Hinzufügen/Entfernen/Ausblenden von Folien aufrufen. Führt `updateSize`, `updateSlides`, `updateProgress`, `updateSlidesClasses` aus. |
| `updateAutoHeight(speed?)` | `speed: number` (ms) | `void` | Höhe erzwingen aktualisieren wenn `autoHeight: true`. |
| `updateProgress()` | — | `void` | Fortschritt des Wrappers neu berechnen. |
| `updateSize()` | — | `void` | Container-Größe neu berechnen. |
| `updateSlides()` | — | `void` | Anzahl der Folien und Offsets neu berechnen. |
| `updateSlidesClasses()` | — | `void` | Aktive/Prev/Next-Klassen auf Folien und Bullets aktualisieren. |
| `use(modules)` | `modules: SwiperModule[]` | `void` | Module zur Laufzeit installieren (statische Methode). |

---

### Nutzungsbeispiele Core-Methoden

```js
const swiper = new Swiper('.swiper', { loop: true });

// Navigation
swiper.slideNext();
swiper.slidePrev();
swiper.slideTo(5);              // Index 5, Standard-Speed
swiper.slideTo(5, 1000);        // Index 5, 1000 ms
swiper.slideTo(5, 1000, false); // Kein Callback

// Loop-Modus: realIndex ansprechen
swiper.slideToLoop(3);

// Fortschritt setzen (0 = Anfang, 1 = Ende)
swiper.setProgress(0.5, 300);

// Event-Handling
const handler = (s) => console.log(s.activeIndex);
swiper.on('slideChange', handler);
swiper.off('slideChange', handler);
swiper.once('transitionEnd', (s) => console.log('einmalig'));
swiper.onAny((name, ...args) => console.log('event:', name));

// Richtung ändern
swiper.changeDirection('vertical');

// Nach DOM-Manipulation
swiper.update();

// Deaktivieren/Aktivieren
swiper.disable();
swiper.enable();

// Translate
const t = swiper.getTranslate(); // aktueller Wert
swiper.setTranslate(-300);        // direkt setzen
swiper.translateTo(-300, 500);    // animiert

// Zerstören
swiper.destroy();       // Instanz löschen, Styles bereinigen
swiper.destroy(false);  // Styles behalten
```

---

## 2. Navigation-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.navigation.destroy()` | — | Navigation zerstören. |
| `swiper.navigation.init()` | — | Navigation initialisieren. |
| `swiper.navigation.update()` | — | Navigations-Buttons-Zustand aktualisieren (aktiviert/deaktiviert). |

---

## 3. Pagination-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.pagination.destroy()` | — | Pagination zerstören. |
| `swiper.pagination.init()` | — | Pagination initialisieren. |
| `swiper.pagination.render()` | — | Pagination-Layout rendern. |
| `swiper.pagination.update()` | — | Pagination-Zustand aktualisieren (aktiviert/deaktiviert/aktiv). |

---

## 4. Scrollbar-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.scrollbar.destroy()` | — | Scrollbar zerstören. |
| `swiper.scrollbar.init()` | — | Scrollbar initialisieren. |
| `swiper.scrollbar.setTranslate()` | — | Scrollbar-Translate aktualisieren. |
| `swiper.scrollbar.updateSize()` | — | Scrollbar-Track und Handler-Größen aktualisieren. |

---

## 5. Autoplay-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.autoplay.pause()` | — | Autoplay pausieren. |
| `swiper.autoplay.resume()` | — | Autoplay fortsetzen. |
| `swiper.autoplay.start()` | — | Autoplay starten. |
| `swiper.autoplay.stop()` | — | Autoplay stoppen. |

```js
// Autoplay-Steuerung
document.querySelector('#pause').addEventListener('click', () => swiper.autoplay.pause());
document.querySelector('#play').addEventListener('click', () => swiper.autoplay.resume());
```

---

## 6. Manipulation-Methoden (Modul: Manipulation)

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.addSlide(index, slides)` | `index: number`, `slides: HTMLElement \| string \| array` | Neue Folie(n) an einem bestimmten Index einfügen. |
| `swiper.appendSlide(slides)` | `slides: HTMLElement \| string \| array` | Neue Folie(n) am Ende hinzufügen. |
| `swiper.prependSlide(slides)` | `slides: HTMLElement \| string \| array` | Neue Folie(n) am Anfang hinzufügen. |
| `swiper.removeAllSlides()` | — | Alle Folien entfernen. |
| `swiper.removeSlide(slideIndex)` | `slideIndex: number \| number[]` | Folie(n) am angegebenen Index entfernen. |

```js
import { Manipulation } from 'swiper/modules';
const swiper = new Swiper('.swiper', { modules: [Manipulation] });

// Folie hinzufügen
swiper.appendSlide('<div class="swiper-slide">Neue Folie</div>');
swiper.prependSlide('<div class="swiper-slide">Erste Folie</div>');
swiper.addSlide(2, '<div class="swiper-slide">Folie 3</div>');

// Folien entfernen
swiper.removeSlide(0);
swiper.removeSlide([0, 1, 2]);
swiper.removeAllSlides();
```

---

## 7. Thumbs-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.thumbs.init()` | — | Thumbs initialisieren. |
| `swiper.thumbs.update(initial, p)` | `initial: boolean`, `p: any` | Thumbs aktualisieren. |

---

## 8. Zoom-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.zoom.disable()` | — | Zoom-Modul deaktivieren. |
| `swiper.zoom.enable()` | — | Zoom-Modul aktivieren. |
| `swiper.zoom.in(ratio?)` | `ratio: number` (optional) | Aktive Folie einzoomen. |
| `swiper.zoom.out()` | — | Aktive Folie auszoomen. |
| `swiper.zoom.toggle(event)` | `event: PointerEvent` | Zoom der aktiven Folie umschalten. |

---

## 9. Keyboard-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.keyboard.disable()` | — | Tastatursteuerung deaktivieren. |
| `swiper.keyboard.enable()` | — | Tastatursteuerung aktivieren. |

---

## 10. Mousewheel-Methoden

| Methode | Parameter | Beschreibung |
|---|---|---|
| `swiper.mousewheel.disable()` | — | Mausrad-Steuerung deaktivieren. |
| `swiper.mousewheel.enable()` | — | Mausrad-Steuerung aktivieren. |

---

*Quelle: https://swiperjs.com/swiper-api*
