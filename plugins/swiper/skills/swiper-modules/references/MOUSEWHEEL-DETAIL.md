# Swiper Mousewheel module — Complete reference

## Import and activation

```js
import Swiper from 'swiper';
import { Mousewheel } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Mousewheel],
  mousewheel: {
    enabled: true,
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `boolean` | `false` | Enable mouse wheel control |
| `eventsTarget` | `HTMLElement \| string` | `'container'` | Element that receives wheel events; `'container'` = the Swiper container |
| `invert` | `boolean` | `false` | Invert the scroll direction |
| `forceToAxis` | `boolean` | `false` | Restrict scrolling to the Swiper axis (prevents diagonal scrolling) |
| `releaseOnEdges` | `boolean` | `false` | Allow page scrolling when Swiper is on the first/last slide |
| `sensitivity` | `number` | `1` | Multiplier for the scroll delta (> 1 = more sensitive) |
| `thresholdDelta` | `number \| null` | `null` | Minimum scroll delta needed to trigger a transition |
| `thresholdTime` | `number \| null` | `null` | Minimum time in ms between scroll events |
| `noMousewheelClass` | `string` | `'swiper-no-mousewheel'` | CSS class on child elements to disable the mouse wheel there |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `swiper.mousewheel.enabled` | `boolean` | Indicates whether mouse wheel control is active |

## Methods

| Method | Description |
|--------|-------------|
| `swiper.mousewheel.enable()` | Enable mouse wheel control |
| `swiper.mousewheel.disable()` | Disable mouse wheel control |

## Events

| Event | Arguments | Description |
|-------|-----------|-------------|
| `scroll` | `(swiper, event)` | Fires on mouse wheel scroll |

## noMousewheelClass — disable scrolling inside child elements

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <!-- This element scrolls normally and does not trigger a slide change -->
      <div class="swiper-no-mousewheel" style="overflow-y: scroll; height: 200px;">
        Long text that can be scrolled...
      </div>
    </div>
  </div>
</div>
```

## Complete examples

### Full-screen vertical scroller

```js
const swiper = new Swiper('.swiper', {
  modules: [Mousewheel],
  direction: 'vertical',
  slidesPerView: 1,
  spaceBetween: 0,
  mousewheel: {
    enabled: true,
    releaseOnEdges: true,
    thresholdDelta: 30,
    thresholdTime: 800,
  },
  speed: 800,
});
```

### With body as the event target

```js
const swiper = new Swiper('.swiper', {
  modules: [Mousewheel],
  mousewheel: {
    enabled: true,
    eventsTarget: document.body,
    forceToAxis: true,
  },
});
```

---
Source: https://swiperjs.com/swiper-api#mousewheel-control
