# Swiper Keyboard module — Complete reference

## Import and activation

```js
import Swiper from 'swiper';
import { Keyboard } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Keyboard],
  keyboard: {
    enabled: true,
    onlyInViewport: true,
    pageUpDown: true,
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Enable keyboard navigation |
| `onlyInViewport` | `boolean` | `true` | Only control when the Swiper is visible in the viewport |
| `pageUpDown` | `boolean` | `true` | Enable navigation via Page Up / Page Down |
| `speed` | `number` | `undefined` | Transition duration on key press in ms (overrides the global `speed`) |

## Supported keys

| Key | Action |
|-------|--------|
| `ArrowRight` / `ArrowDown` | Next slide |
| `ArrowLeft` / `ArrowUp` | Previous slide |
| `Page Down` | Next slide (when `pageUpDown: true`) |
| `Page Up` | Previous slide (when `pageUpDown: true`) |

## Properties

| Property | Type | Description |
|----------|-----|--------------|
| `swiper.keyboard.enabled` | `boolean` | Indicates whether keyboard control is active |

## Methods

| Method | Description |
|---------|--------------|
| `swiper.keyboard.enable()` | Enable keyboard navigation |
| `swiper.keyboard.disable()` | Disable keyboard navigation |

## Events

| Event | Arguments | Description |
|-------|-----------|--------------|
| `keyPress` | `(swiper, keyCode)` | Fires on every key press (keyCode = numeric key code) |

```js
swiper.on('keyPress', (swiper, keyCode) => {
  console.log('Key pressed:', keyCode);
  // 37 = ArrowLeft, 38 = ArrowUp, 39 = ArrowRight, 40 = ArrowDown
  // 33 = Page Up, 34 = Page Down
});
```

## Complete example

```js
const swiper = new Swiper('.swiper', {
  modules: [Keyboard],
  keyboard: {
    enabled: true,
    onlyInViewport: false, // always react, even when outside
    pageUpDown: true,
    speed: 400,
  },
  on: {
    keyPress: (swiper, keyCode) => {
      if (keyCode === 27) { // Escape
        swiper.slideTo(0);
      }
    },
  },
});

// Toggle dynamically
document.querySelector('#toggle-keyboard').addEventListener('click', () => {
  if (swiper.keyboard.enabled) {
    swiper.keyboard.disable();
  } else {
    swiper.keyboard.enable();
  }
});
```

---
Source: https://swiperjs.com/swiper-api#keyboard-control
