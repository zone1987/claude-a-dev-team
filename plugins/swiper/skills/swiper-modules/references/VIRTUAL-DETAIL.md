# Swiper Virtual Slides module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [renderSlide function](#renderslide-function)
- [renderExternal for React](#renderexternal-for-react)
- [Properties](#properties)
- [Methods](#methods)
- [Limitations](#limitations)
- [Complete example with 1000 slides](#complete-example-with-1000-slides)

## Concept

Virtual Slides keeps only the slides required for display in the DOM. With hundreds or thousands of slides this performs dramatically better than rendering the full DOM.

## Import and activation

```js
import Swiper from 'swiper';
import { Virtual } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Virtual],
  virtual: {
    slides: ['Slide 1', 'Slide 2', 'Slide 3', /* ... */],
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Enable Virtual Slides |
| `slides` | `array` | `[]` | Data source — an array of arbitrary values (string, object, etc.) |
| `cache` | `boolean` | `true` | Keep rendered slide HTML elements in the cache |
| `addSlidesBefore` | `number` | `0` | Pre-render additional slides before the active one |
| `addSlidesAfter` | `number` | `0` | Pre-render additional slides after the active one |
| `renderSlide` | `function(slide, index)` | `null` | Custom render function for individual slides; must return an HTML string |
| `renderExternal` | `function(data)` | `null` | Delegate rendering to an external library (React/Vue) |
| `renderExternalUpdate` | `function(data)` | `null` | Callback after an update with `renderExternal` |

## renderSlide function

```js
virtual: {
  slides: myDataArray,
  renderSlide: (slide, index) => {
    // slide = entry from the slides array
    // index = position in the array
    return `
      <div class="swiper-slide" data-index="${index}">
        <img src="${slide.image}" alt="${slide.title}" />
        <h3>${slide.title}</h3>
      </div>
    `;
  },
}
```

## renderExternal for React

```jsx
// React integration with renderExternal
const [virtualData, setVirtualData] = useState({ slides: [], offset: 0 });

const swiper = new Swiper('.swiper', {
  modules: [Virtual],
  virtual: {
    slides: mySlides,
    renderExternal: (data) => {
      setVirtualData(data);
    },
  },
});

// JSX
<div className="swiper-wrapper" style={{ paddingLeft: virtualData.offset + 'px' }}>
  {virtualData.slides.map((slide, index) => (
    <div className="swiper-slide" key={index}>{slide}</div>
  ))}
</div>
```

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.virtual.slides` | `array` | Slides currently rendered in the DOM |
| `swiper.virtual.cache` | `object` | Cached slide elements (key = index) |

## Methods

| Method | Description |
|---------|--------------|
| `swiper.virtual.update(force?)` | Update the Virtual Slides; `force: true` = clear the cache |
| `swiper.virtual.appendSlide(slides)` | Append slides at the end |
| `swiper.virtual.prependSlide(slides)` | Insert slides at the beginning |

## Limitations

- **Not compatible** with the Grid module
- **Not compatible** with `slidesPerView: 'auto'`
- Loop mode requires enough slides to be present

## Complete example with 1000 slides

```js
import Swiper from 'swiper';
import { Virtual, Navigation, Pagination } from 'swiper/modules';

const slides = Array.from({ length: 1000 }, (_, i) => ({
  id: i,
  title: `Slide ${i + 1}`,
  image: `https://picsum.photos/800/400?random=${i}`,
}));

const swiper = new Swiper('.swiper', {
  modules: [Virtual, Navigation, Pagination],
  slidesPerView: 1,
  virtual: {
    slides,
    cache: true,
    addSlidesBefore: 2,
    addSlidesAfter: 2,
    renderSlide: (slide, index) => `
      <div class="swiper-slide">
        <img src="${slide.image}" loading="lazy" />
        <p>${slide.title}</p>
      </div>
    `,
  },
  navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
  pagination: { el: '.swiper-pagination', type: 'fraction' },
});
```

---
Source: https://swiperjs.com/swiper-api#virtual-slides
