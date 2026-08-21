# Swiper Scrollbar module — Complete reference

## Contents

- [Import and activation](#import-and-activation)
- [HTML structure](#html-structure)
- [Parameters](#parameters)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [CSS Custom Properties](#css-custom-properties)
- [Complete example (vertical with snap)](#complete-example-vertical-with-snap)

## Import and activation

```js
import Swiper from 'swiper';
import { Scrollbar } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/scrollbar';

const swiper = new Swiper('.swiper', {
  modules: [Scrollbar],
  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true,
    snapOnRelease: true,
  },
});
```

## HTML structure

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
  </div>
  <div class="swiper-scrollbar"></div>
</div>
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `el` | `HTMLElement \| CSSSelector \| null` | `null` | Scrollbar container element or selector |
| `draggable` | `boolean` | `false` | Allow dragging the scrollbar to navigate slides |
| `dragClass` | `string` | `'swiper-scrollbar-drag'` | CSS class for the drag handle element |
| `dragSize` | `number \| 'auto'` | `'auto'` | Size of the drag handle in px; `'auto'` = proportional |
| `hide` | `boolean` | `true` | Hide the scrollbar automatically after interaction |
| `snapOnRelease` | `boolean` | `false` | Snap to the nearest slide when the handle is released |
| `enabled` | `boolean` | — | Enable/disable the scrollbar for specific breakpoints |
| `horizontalClass` | `string` | `'swiper-scrollbar-horizontal'` | Class for horizontal orientation |
| `verticalClass` | `string` | `'swiper-scrollbar-vertical'` | Class for vertical orientation |
| `lockClass` | `string` | `'swiper-scrollbar-lock'` | Class when the scrollbar is locked |
| `scrollbarDisabledClass` | `string` | `'swiper-scrollbar-disabled'` | Class on the container when disabled by a breakpoint |

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.scrollbar.el` | `HTMLElement` | Scrollbar container element |
| `swiper.scrollbar.dragEl` | `HTMLElement` | Drag handle element |

## Methods

| Method | Description |
|---------|--------------|
| `swiper.scrollbar.init()` | Initialize the scrollbar |
| `swiper.scrollbar.destroy()` | Remove the scrollbar |
| `swiper.scrollbar.setTranslate()` | Synchronize the scrollbar position |
| `swiper.scrollbar.updateSize()` | Recalculate the track and handle sizes |

## Events

| Event | Arguments | Description |
|-------|-----------|--------------|
| `scrollbarDragStart` | `(swiper, event)` | Dragging of the handle begins |
| `scrollbarDragMove` | `(swiper, event)` | The handle is being dragged |
| `scrollbarDragEnd` | `(swiper, event)` | Dragging of the handle ends |

```js
swiper.on('scrollbarDragEnd', (swiper, event) => {
  console.log('Drag finished, active slide:', swiper.activeIndex);
});
```

## CSS Custom Properties

```css
:root {
  --swiper-scrollbar-border-radius: 10px;
  --swiper-scrollbar-top: auto;
  --swiper-scrollbar-bottom: 4px;
  --swiper-scrollbar-left: auto;
  --swiper-scrollbar-right: 4px;
  --swiper-scrollbar-sides-offset: 1%;
  --swiper-scrollbar-bg-color: rgba(0, 0, 0, 0.1);
  --swiper-scrollbar-drag-bg-color: rgba(0, 0, 0, 0.5);
  --swiper-scrollbar-size: 4px;
}
```

## Complete example (vertical with snap)

```js
const swiper = new Swiper('.swiper', {
  modules: [Scrollbar],
  direction: 'vertical',
  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true,
    snapOnRelease: true,
    dragSize: 30,
    hide: false,
  },
});
```

---
Source: https://swiperjs.com/swiper-api#scrollbar
