# Swiper Navigation module — Complete reference

## Contents

- [Import and activation](#import-and-activation)
- [HTML structure](#html-structure)
- [Parameters](#parameters)
- [Properties](#properties)
- [Methods](#methods)
- [Events](#events)
- [CSS Custom Properties](#css-custom-properties)
- [Breakpoint-specific navigation](#breakpoint-specific-navigation)
- [External buttons (outside the Swiper container)](#external-buttons-outside-the-swiper-container)

## Import and activation

```js
import Swiper from 'swiper';
import { Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';

const swiper = new Swiper('.swiper', {
  modules: [Navigation],
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
```

## HTML structure

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
    <div class="swiper-slide">Slide 3</div>
  </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>
```

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `nextEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS selector or element for the "next" button |
| `prevEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS selector or element for the "previous" button |
| `hideOnClick` | `boolean` | `false` | Toggle the navigation when clicking the slider container |
| `disabledClass` | `string` | `'swiper-button-disabled'` | CSS class when the button is inactive (first/last slide without loop) |
| `hiddenClass` | `string` | `'swiper-button-hidden'` | CSS class when the button is hidden |
| `lockClass` | `string` | `'swiper-button-lock'` | CSS class when navigation is disabled by a breakpoint |
| `navigationDisabledClass` | `string` | `'swiper-navigation-disabled'` | Class on the container element when navigation is disabled by a breakpoint |
| `addIcons` | `boolean` | `true` | Insert SVG icons into the buttons automatically |
| `enabled` | `boolean` | — | Enable/disable navigation for specific breakpoints |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `swiper.navigation.nextEl` | `HTMLElement` | Reference to the next button |
| `swiper.navigation.prevEl` | `HTMLElement` | Reference to the prev button |

## Methods

| Method | Description |
|--------|-------------|
| `swiper.navigation.init()` | Initialize navigation |
| `swiper.navigation.destroy()` | Remove navigation and clean up |
| `swiper.navigation.update()` | Update the enabled/disabled state of the buttons |

## Events

| Event | Arguments | Description |
|-------|-----------|-------------|
| `navigationHide` | `(swiper)` | The buttons are being hidden |
| `navigationShow` | `(swiper)` | The buttons are being shown |
| `navigationPrev` | `(swiper)` | The prev button was clicked |
| `navigationNext` | `(swiper)` | The next button was clicked |

```js
swiper.on('navigationNext', (swiper) => {
  console.log('Next clicked, active index:', swiper.activeIndex);
});
```

## CSS Custom Properties

```css
:root {
  --swiper-navigation-size: 44px;
  --swiper-navigation-top-offset: 50%;
  --swiper-navigation-sides-offset: 10px;
  --swiper-navigation-color: var(--swiper-theme-color);
}
```

## Breakpoint-specific navigation

```js
const swiper = new Swiper('.swiper', {
  modules: [Navigation],
  breakpoints: {
    640: {
      navigation: {
        enabled: false,
      },
    },
    1024: {
      navigation: {
        enabled: true,
      },
    },
  },
});
```

## External buttons (outside the Swiper container)

```js
const swiper = new Swiper('.swiper', {
  modules: [Navigation],
  navigation: {
    nextEl: '#my-custom-next',
    prevEl: '#my-custom-prev',
  },
});
```

---
Source: https://swiperjs.com/swiper-api#navigation
