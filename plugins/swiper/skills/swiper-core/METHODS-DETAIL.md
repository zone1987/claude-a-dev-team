# Swiper — Complete method reference (v11/12)

Call all methods on the Swiper instance: `const swiper = new Swiper(...)`.

---

## Contents

- [1. Core methods](#1-core-methods)
- [2. Navigation methods](#2-navigation-methods)
- [3. Pagination methods](#3-pagination-methods)
- [4. Scrollbar methods](#4-scrollbar-methods)
- [5. Autoplay methods](#5-autoplay-methods)
- [6. Manipulation methods (module: Manipulation)](#6-manipulation-methods-module-manipulation)
- [7. Thumbs methods](#7-thumbs-methods)
- [8. Zoom methods](#8-zoom-methods)
- [9. Keyboard methods](#9-keyboard-methods)
- [10. Mousewheel methods](#10-mousewheel-methods)

## 1. Core methods

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `attachEvents()` | — | `void` | Attach all event listeners again. |
| `changeDirection(direction?, needUpdate?)` | `direction: 'horizontal' \| 'vertical'` (optional), `needUpdate: boolean` (default `true`) | `Swiper` | Change the slider direction from horizontal to vertical or vice versa. |
| `changeLanguageDirection(direction)` | `direction: 'rtl' \| 'ltr'` | `void` | Change the language direction of the slider. |
| `destroy(deleteInstance?, cleanStyles?)` | `deleteInstance: boolean` (default `true`), `cleanStyles: boolean` (default `true`) | `void` | Destroy the Swiper instance and remove all event listeners. |
| `detachEvents()` | — | `void` | Remove all event listeners. |
| `disable()` | — | `void` | Disable Swiper (if it was enabled). |
| `emit(event, ...args)` | `event: string`, `args: any` | `void` | Fire an event on the instance manually. |
| `enable()` | — | `void` | Enable Swiper (if it was disabled). |
| `extendDefaults(options)` | `options: SwiperOptions` | `void` | Extend the global Swiper defaults (static). |
| `getTranslate()` | — | `number` | Return the current CSS3 transform translate value of the wrapper. |
| `init(el?)` | `el: HTMLElement` | `Swiper` | Initialize the slider (when `init: false` is set). |
| `maxTranslate()` | — | `number` | Return the maximum translate value. |
| `minTranslate()` | — | `number` | Return the minimum translate value. |
| `off(event, handler)` | `event: string`, `handler: function` | `Swiper` | Remove an event handler. |
| `offAny(handler)` | `handler: function` | `Swiper` | Remove the listener for all events. |
| `on(event, handler)` | `event: string`, `handler: function` | `Swiper` | Add an event handler. |
| `onAny(handler)` | `handler: function` | `Swiper` | Add a listener that fires on every event. |
| `once(event, handler)` | `event: string`, `handler: function` | `Swiper` | Add an event handler that is removed after firing once. |
| `setGrabCursor()` | — | `void` | Set the grab cursor. |
| `setProgress(progress, speed?)` | `progress: number` (0–1), `speed: number` (ms) | `void` | Set the Swiper translate progress. |
| `setTranslate(translate)` | `translate: number` | `void` | Set a custom CSS3 transform translate value. |
| `slideNext(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Move to the next slide. |
| `slidePrev(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Move to the previous slide. |
| `slideReset(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Reset to the currently active slide. |
| `slideTo(index, speed?, runCallbacks?)` | `index: number`, `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Move to the slide with the given index. |
| `slideToClosest(speed?, runCallbacks?)` | `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | Move to the closest slide / snap point. |
| `slideToLoop(index, speed?, runCallbacks?)` | `index: number`, `speed: number` (ms, optional), `runCallbacks: boolean` (default `true`) | `void` | In loop mode, move to `realIndex === index`. |
| `slidesPerViewDynamic()` | — | `number` | Return the dynamically calculated number of visible slides. |
| `translateTo(translate, speed, runCallbacks?, translateBounds?)` | `translate: number` (px), `speed: number` (ms), `runCallbacks: boolean` (default `true`), `translateBounds: boolean` (default `true`) | `void` | Animate to a custom CSS3 transform translate value. |
| `unsetGrabCursor()` | — | `void` | Remove the grab cursor. |
| `update()` | — | `void` | Call after adding/removing/hiding slides. Runs `updateSize`, `updateSlides`, `updateProgress`, `updateSlidesClasses`. |
| `updateAutoHeight(speed?)` | `speed: number` (ms) | `void` | Force a height update when `autoHeight: true`. |
| `updateProgress()` | — | `void` | Recalculate the progress of the wrapper. |
| `updateSize()` | — | `void` | Recalculate the container size. |
| `updateSlides()` | — | `void` | Recalculate the number of slides and their offsets. |
| `updateSlidesClasses()` | — | `void` | Update the active/prev/next classes on slides and bullets. |
| `use(modules)` | `modules: SwiperModule[]` | `void` | Install modules at runtime (static method). |

---

### Core method usage examples

```js
const swiper = new Swiper('.swiper', { loop: true });

// Navigation
swiper.slideNext();
swiper.slidePrev();
swiper.slideTo(5);              // index 5, default speed
swiper.slideTo(5, 1000);        // index 5, 1000 ms
swiper.slideTo(5, 1000, false); // no callback

// Loop mode: address realIndex
swiper.slideToLoop(3);

// Set progress (0 = beginning, 1 = end)
swiper.setProgress(0.5, 300);

// Event handling
const handler = (s) => console.log(s.activeIndex);
swiper.on('slideChange', handler);
swiper.off('slideChange', handler);
swiper.once('transitionEnd', (s) => console.log('only once'));
swiper.onAny((name, ...args) => console.log('event:', name));

// Change direction
swiper.changeDirection('vertical');

// After DOM manipulation
swiper.update();

// Disable/enable
swiper.disable();
swiper.enable();

// Translate
const t = swiper.getTranslate(); // current value
swiper.setTranslate(-300);        // set directly
swiper.translateTo(-300, 500);    // animated

// Destroy
swiper.destroy();       // delete the instance, clean up styles
swiper.destroy(false);  // keep styles
```

---

## 2. Navigation methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.navigation.destroy()` | — | Destroy the navigation. |
| `swiper.navigation.init()` | — | Initialize the navigation. |
| `swiper.navigation.update()` | — | Update the navigation button state (enabled/disabled). |

---

## 3. Pagination methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.pagination.destroy()` | — | Destroy the pagination. |
| `swiper.pagination.init()` | — | Initialize the pagination. |
| `swiper.pagination.render()` | — | Render the pagination layout. |
| `swiper.pagination.update()` | — | Update the pagination state (enabled/disabled/active). |

---

## 4. Scrollbar methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.scrollbar.destroy()` | — | Destroy the scrollbar. |
| `swiper.scrollbar.init()` | — | Initialize the scrollbar. |
| `swiper.scrollbar.setTranslate()` | — | Update the scrollbar translate. |
| `swiper.scrollbar.updateSize()` | — | Update the scrollbar track and handler sizes. |

---

## 5. Autoplay methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.autoplay.pause()` | — | Pause autoplay. |
| `swiper.autoplay.resume()` | — | Resume autoplay. |
| `swiper.autoplay.start()` | — | Start autoplay. |
| `swiper.autoplay.stop()` | — | Stop autoplay. |

```js
// Autoplay control
document.querySelector('#pause').addEventListener('click', () => swiper.autoplay.pause());
document.querySelector('#play').addEventListener('click', () => swiper.autoplay.resume());
```

---

## 6. Manipulation methods (module: Manipulation)

| Method | Parameters | Description |
|---|---|---|
| `swiper.addSlide(index, slides)` | `index: number`, `slides: HTMLElement \| string \| array` | Insert new slide(s) at a specific index. |
| `swiper.appendSlide(slides)` | `slides: HTMLElement \| string \| array` | Append new slide(s) at the end. |
| `swiper.prependSlide(slides)` | `slides: HTMLElement \| string \| array` | Prepend new slide(s) at the beginning. |
| `swiper.removeAllSlides()` | — | Remove all slides. |
| `swiper.removeSlide(slideIndex)` | `slideIndex: number \| number[]` | Remove the slide(s) at the given index. |

```js
import { Manipulation } from 'swiper/modules';
const swiper = new Swiper('.swiper', { modules: [Manipulation] });

// Add slides
swiper.appendSlide('<div class="swiper-slide">New slide</div>');
swiper.prependSlide('<div class="swiper-slide">First slide</div>');
swiper.addSlide(2, '<div class="swiper-slide">Slide 3</div>');

// Remove slides
swiper.removeSlide(0);
swiper.removeSlide([0, 1, 2]);
swiper.removeAllSlides();
```

---

## 7. Thumbs methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.thumbs.init()` | — | Initialize thumbs. |
| `swiper.thumbs.update(initial, p)` | `initial: boolean`, `p: any` | Update thumbs. |

---

## 8. Zoom methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.zoom.disable()` | — | Disable the Zoom module. |
| `swiper.zoom.enable()` | — | Enable the Zoom module. |
| `swiper.zoom.in(ratio?)` | `ratio: number` (optional) | Zoom in on the active slide. |
| `swiper.zoom.out()` | — | Zoom out on the active slide. |
| `swiper.zoom.toggle(event)` | `event: PointerEvent` | Toggle the zoom of the active slide. |

---

## 9. Keyboard methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.keyboard.disable()` | — | Disable keyboard control. |
| `swiper.keyboard.enable()` | — | Enable keyboard control. |

---

## 10. Mousewheel methods

| Method | Parameters | Description |
|---|---|---|
| `swiper.mousewheel.disable()` | — | Disable mouse wheel control. |
| `swiper.mousewheel.enable()` | — | Enable mouse wheel control. |

---

*Source: https://swiperjs.com/swiper-api*
