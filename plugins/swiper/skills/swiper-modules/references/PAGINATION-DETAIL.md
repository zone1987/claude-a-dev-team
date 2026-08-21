# Swiper Pagination module — Complete reference

## Contents

- [Import and activation](#import-and-activation)
- [HTML structure](#html-structure)
- [Parameters (complete)](#parameters-complete)
- [Render function signatures](#render-function-signatures)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [CSS Custom Properties](#css-custom-properties)
- [Complete examples](#complete-examples)

## Import and activation

```js
import Swiper from 'swiper';
import { Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';

const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
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
  <div class="swiper-pagination"></div>
</div>
```

## Parameters (complete)

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `el` | `HTMLElement \| CSSSelector \| null` | `null` | Container element or selector |
| `type` | `string` | `'bullets'` | Pagination type: `'bullets'`, `'fraction'`, `'progressbar'`, `'custom'` |
| `clickable` | `boolean` | `false` | Change slides by clicking bullets (bullets type only) |
| `dynamicBullets` | `boolean` | `false` | Show only a limited set of bullets when there are many slides |
| `dynamicMainBullets` | `number` | `1` | Number of visible main bullets in dynamic mode |
| `hideOnClick` | `boolean` | `true` | Show/hide the pagination when clicking the container |
| `enabled` | `boolean` | — | Enable/disable pagination for specific breakpoints |
| `bulletClass` | `string` | `'swiper-pagination-bullet'` | CSS class for individual bullets |
| `bulletActiveClass` | `string` | `'swiper-pagination-bullet-active'` | CSS class for the active bullet |
| `bulletElement` | `string` | `'span'` | HTML tag for bullets |
| `clickableClass` | `string` | `'swiper-pagination-clickable'` | Class when the pagination is clickable |
| `currentClass` | `string` | `'swiper-pagination-current'` | Class for the current index (fraction) |
| `totalClass` | `string` | `'swiper-pagination-total'` | Class for the total count (fraction) |
| `hiddenClass` | `string` | `'swiper-pagination-hidden'` | Class when the pagination is hidden |
| `horizontalClass` | `string` | `'swiper-pagination-horizontal'` | Class for horizontal orientation |
| `verticalClass` | `string` | `'swiper-pagination-vertical'` | Class for vertical orientation |
| `lockClass` | `string` | `'swiper-pagination-lock'` | Class when the pagination is locked |
| `modifierClass` | `string` | `'swiper-pagination-'` | CSS class prefix |
| `paginationDisabledClass` | `string` | `'swiper-pagination-disabled'` | Class on the container when disabled |
| `progressbarFillClass` | `string` | `'swiper-pagination-progressbar-fill'` | Class for the progressbar fill bar |
| `progressbarOpposite` | `boolean` | `false` | Reverse the progressbar direction |
| `progressbarOppositeClass` | `string` | `'swiper-pagination-progressbar-opposite'` | Class for the opposite-direction progressbar |
| `renderBullet` | `function(index, className)` | `null` | Custom bullet rendering |
| `renderFraction` | `function(currentClass, totalClass)` | `null` | Custom fraction rendering |
| `renderProgressbar` | `function(progressbarFillClass)` | `null` | Custom progressbar rendering |
| `renderCustom` | `function(swiper, current, total)` | `null` | Required with `type: 'custom'` |
| `formatFractionCurrent` | `function(number)` | — | Format the current index |
| `formatFractionTotal` | `function(number)` | — | Format the total count |

## Render function signatures

### renderBullet
```js
pagination: {
  renderBullet: function (index, className) {
    // index: 0-based slide index
    // className: 'swiper-pagination-bullet' (+ active class automatically)
    return '<span class="' + className + '">' + (index + 1) + '</span>';
  },
}
```

### renderFraction
```js
pagination: {
  type: 'fraction',
  renderFraction: function (currentClass, totalClass) {
    return '<span class="' + currentClass + '"></span>' +
           ' / ' +
           '<span class="' + totalClass + '"></span>';
  },
}
```

### renderProgressbar
```js
pagination: {
  type: 'progressbar',
  renderProgressbar: function (progressbarFillClass) {
    return '<span class="' + progressbarFillClass + '"></span>';
  },
}
```

### renderCustom
```js
pagination: {
  type: 'custom',
  renderCustom: function (swiper, current, total) {
    return current + ' of ' + total;
  },
}
```

### formatFractionCurrent / formatFractionTotal
```js
pagination: {
  type: 'fraction',
  formatFractionCurrent: (number) => String(number).padStart(2, '0'),
  formatFractionTotal: (number) => String(number).padStart(2, '0'),
}
```

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.pagination.el` | `HTMLElement` | Container element |
| `swiper.pagination.bullets` | `HTMLElement[]` | Array of all bullet elements |

## Methods

| Method | Description |
|---------|--------------|
| `swiper.pagination.init()` | Initialize the pagination |
| `swiper.pagination.destroy()` | Remove the pagination |
| `swiper.pagination.render()` | Re-render the pagination layout |
| `swiper.pagination.update()` | Update the pagination state |

## Events

| Event | Arguments | Description |
|-------|-----------|--------------|
| `paginationRender` | `(swiper, paginationEl)` | After rendering |
| `paginationUpdate` | `(swiper, paginationEl)` | After updating |
| `paginationShow` | `(swiper)` | Pagination was shown |
| `paginationHide` | `(swiper)` | Pagination was hidden |

## CSS Custom Properties

```css
:root {
  --swiper-pagination-color: var(--swiper-theme-color);
  --swiper-pagination-left: auto;
  --swiper-pagination-right: 8px;
  --swiper-pagination-bottom: 8px;
  --swiper-pagination-top: auto;
  --swiper-pagination-fraction-color: inherit;
  --swiper-pagination-progressbar-bg-color: rgba(0, 0, 0, 0.25);
  --swiper-pagination-progressbar-size: 4px;
  --swiper-pagination-bullet-size: 8px;
  --swiper-pagination-bullet-width: 8px;
  --swiper-pagination-bullet-height: 8px;
  --swiper-pagination-bullet-inactive-color: #000;
  --swiper-pagination-bullet-inactive-opacity: 0.2;
  --swiper-pagination-bullet-opacity: 1;
  --swiper-pagination-bullet-horizontal-gap: 4px;
  --swiper-pagination-bullet-vertical-gap: 6px;
}
```

## Complete examples

### Fraction pagination with zero padding
```js
const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    type: 'fraction',
    formatFractionCurrent: (n) => String(n).padStart(2, '0'),
    formatFractionTotal: (n) => String(n).padStart(2, '0'),
  },
});
```

### Numbered bullets
```js
const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    renderBullet: (index, className) =>
      `<span class="${className}">${index + 1}</span>`,
  },
});
```

---
Source: https://swiperjs.com/swiper-api#pagination
