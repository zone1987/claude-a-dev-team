# Swiper Parallax module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Data attributes](#data-attributes)
- [Values explained](#values-explained)
- [Complete HTML example](#complete-html-example)
- [Configuration examples](#configuration-examples)

## Concept

The Parallax module enables parallax scroll effects on any HTML element inside the Swiper. Elements move at a different speed relative to the slide transition. Two scoping levels:

- **Direct Swiper children** (backgrounds, for example): parallax is based on the overall progress of the Swiper
- **Slide children** (text, icons): parallax is based on the progress of the individual slide

## Import and activation

```js
import Swiper from 'swiper';
import { Parallax } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  parallax: true,    // or: parallax: { enabled: true }
  speed: 600,        // parallax timing follows the transition speed
});
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Enable the Parallax module |

**Note:** The module has only this single parameter. All parallax values are driven by HTML data attributes.

## Data attributes

| Attribute | Type | Description |
|----------|-----|--------------|
| `data-swiper-parallax` | `number` (px) or `string` (%) | Translate offset along the slide movement axis |
| `data-swiper-parallax-x` | `number` (px) or `string` (%) | Horizontal parallax offset |
| `data-swiper-parallax-y` | `number` (px) or `string` (%) | Vertical parallax offset |
| `data-swiper-parallax-scale` | `number` | Scale factor while the slide is inactive (1 = original size) |
| `data-swiper-parallax-opacity` | `number` (0–1) | Opacity while the slide is inactive |
| `data-swiper-parallax-duration` | `number` (ms) | Individual transition duration for this element |

## Values explained

- **Positive value:** the element moves slower than the slide (classic parallax)
- **Negative value:** the element moves faster than the slide (inverse parallax)
- **Percentage values:** relative to the Swiper container width/height
- **`data-swiper-parallax="-23%"`** on a direct child: moves 23% less than the Swiper scrolls

## Complete HTML example

```html
<div class="swiper">
  <!-- Parallax background (direct child = based on overall progress) -->
  <div
    class="parallax-bg"
    style="background-image: url(background.jpg); position: absolute; width: 130%; height: 100%; left: -15%;"
    data-swiper-parallax="-23%"
  ></div>

  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <!-- Slide children: parallax is based on this slide's progress -->

      <!-- Strong offset (moves faster) -->
      <div class="slide-icon"
           data-swiper-parallax="-200"
           data-swiper-parallax-opacity="0">
        🎯
      </div>

      <!-- Medium offset -->
      <h2 class="slide-title" data-swiper-parallax="-100">
        Slide title
      </h2>

      <!-- Slight offset with its own timing -->
      <p class="slide-text"
         data-swiper-parallax="-50"
         data-swiper-parallax-duration="800">
        Description text
      </p>

      <!-- Scaling only -->
      <div class="slide-badge"
           data-swiper-parallax-scale="0.5">
        New
      </div>

      <!-- X and Y separately -->
      <div class="slide-element"
           data-swiper-parallax-x="-100"
           data-swiper-parallax-y="-50">
        Diagonal parallax
      </div>
    </div>
  </div>
</div>
```

## Configuration examples

### Simple text animation

```js
const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  parallax: true,
  speed: 800,
});
```

```html
<div class="swiper-slide">
  <h1 data-swiper-parallax="-300">Large title</h1>
  <p data-swiper-parallax="-150">Subtitle with half the offset</p>
</div>
```

### With different axes (vertical slider)

```js
const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  direction: 'vertical',
  parallax: true,
});
```

```html
<!-- On a vertical slider: data-swiper-parallax acts on the Y axis -->
<div class="swiper-slide">
  <div data-swiper-parallax="-200">Parallax up/down</div>
  <div data-swiper-parallax-x="-100">Horizontal parallax accent</div>
</div>
```

### Background and content combined

```js
const swiper = new Swiper('.swiper', {
  modules: [Parallax, Autoplay],
  parallax: true,
  speed: 1000,
  autoplay: { delay: 4000 },
});
```

---
Source: https://swiperjs.com/swiper-api#parallax
