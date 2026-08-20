# Swiper Manipulation module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Methods](#methods)
- [Complete example (dynamic gallery)](#complete-example-dynamic-gallery)
- [Notes on framework integration](#notes-on-framework-integration)

## Concept

The Manipulation module provides methods to add, insert, and remove slides dynamically in the DOM. After every manipulation, Swiper updates its internal state automatically.

**Important:** This module is intended for Swiper Core (vanilla JS). In React/Vue, the slides state should be driven by the framework state.

## Import and activation

```js
import Swiper from 'swiper';
import { Manipulation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Manipulation],
  slidesPerView: 3,
  spaceBetween: 10,
});
```

## Methods

### appendSlide(slides)

Appends one or more slides at the end.

**Signature:** `appendSlide(slides: HTMLElement | string | (HTMLElement | string)[]) => void`

```js
// Single slide (HTML string)
swiper.appendSlide('<div class="swiper-slide">New slide at the end</div>');

// Single slide (HTMLElement)
const slideEl = document.createElement('div');
slideEl.className = 'swiper-slide';
slideEl.textContent = 'Dynamic slide';
swiper.appendSlide(slideEl);

// Several slides at once
swiper.appendSlide([
  '<div class="swiper-slide">Slide A</div>',
  '<div class="swiper-slide">Slide B</div>',
  '<div class="swiper-slide">Slide C</div>',
]);
```

### prependSlide(slides)

Inserts one or more slides at the beginning.

**Signature:** `prependSlide(slides: HTMLElement | string | (HTMLElement | string)[]) => void`

```js
// Single slide
swiper.prependSlide('<div class="swiper-slide">First slide</div>');

// Several slides
swiper.prependSlide([
  '<div class="swiper-slide">New-1</div>',
  '<div class="swiper-slide">New-2</div>',
]);
```

### addSlide(index, slides)

Inserts slides at a specific position.

**Signature:** `addSlide(index: number, slides: HTMLElement | string | (HTMLElement | string)[]) => void`

```js
// Insert at position 2 (zero-based)
swiper.addSlide(2, '<div class="swiper-slide">Slide at position 2</div>');

// Insert several slides starting at position 1
swiper.addSlide(1, [
  '<div class="swiper-slide">New at position 1</div>',
  '<div class="swiper-slide">New at position 2</div>',
]);
```

### removeSlide(slideIndex)

Removes one or more slides by index.

**Signature:** `removeSlide(slideIndex: number | number[]) => void`

```js
// Remove the first slide
swiper.removeSlide(0);

// Remove several slides
swiper.removeSlide([0, 2, 4]);  // slides at index 0, 2, and 4
```

### removeAllSlides()

Removes all slides.

**Signature:** `removeAllSlides() => void`

```js
swiper.removeAllSlides();
```

## Complete example (dynamic gallery)

```js
import Swiper from 'swiper';
import { Manipulation, Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Manipulation, Navigation, Pagination],
  slidesPerView: 1,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    type: 'fraction',
  },
});

// Load slides and append them
async function loadMoreSlides(page) {
  const response = await fetch(`/api/slides?page=${page}`);
  const slides = await response.json();

  const html = slides.map(slide =>
    `<div class="swiper-slide">
      <img src="${slide.image}" alt="${slide.title}" />
      <h3>${slide.title}</h3>
    </div>`
  );

  swiper.appendSlide(html);
}

// Button: add a slide
document.querySelector('#add-slide').addEventListener('click', () => {
  const index = swiper.slides.length;
  swiper.appendSlide(
    `<div class="swiper-slide">Slide ${index + 1}</div>`
  );
  swiper.slideTo(index); // navigate to the new slide
});

// Button: remove the current slide
document.querySelector('#remove-current').addEventListener('click', () => {
  swiper.removeSlide(swiper.activeIndex);
});

// Clear everything and reload
document.querySelector('#reset').addEventListener('click', () => {
  swiper.removeAllSlides();
  loadMoreSlides(1);
});
```

## Notes on framework integration

In React/Vue/Angular, slides are not managed through the Manipulation module but through reactive state updates:

```jsx
// React: manage slides via state
const [slides, setSlides] = useState(['Slide 1', 'Slide 2']);

const addSlide = () => {
  setSlides(prev => [...prev, `Slide ${prev.length + 1}`]);
};

// Swiper updates itself automatically when the slides change
```

---
Source: https://swiperjs.com/swiper-api#manipulation
