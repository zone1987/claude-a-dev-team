# Swiper Keyboard-Modul — Vollständige Referenz

## Import & Aktivierung

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

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Tastaturnavigation aktivieren |
| `onlyInViewport` | `boolean` | `true` | Nur steuern wenn Swiper sichtbar im Viewport ist |
| `pageUpDown` | `boolean` | `true` | Navigation per Page Up / Page Down aktivieren |
| `speed` | `number` | `undefined` | Transitions-Dauer bei Tastendruck in ms (überschreibt globalen `speed`) |

## Unterstützte Tasten

| Taste | Aktion |
|-------|--------|
| `ArrowRight` / `ArrowDown` | Nächster Slide |
| `ArrowLeft` / `ArrowUp` | Vorheriger Slide |
| `Page Down` | Nächster Slide (wenn `pageUpDown: true`) |
| `Page Up` | Vorheriger Slide (wenn `pageUpDown: true`) |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.keyboard.enabled` | `boolean` | Gibt an ob Tastatursteuerung aktiv ist |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.keyboard.enable()` | Tastaturnavigation aktivieren |
| `swiper.keyboard.disable()` | Tastaturnavigation deaktivieren |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `keyPress` | `(swiper, keyCode)` | Wird bei jedem Tastendruck ausgelöst (keyCode = numerischer Key-Code) |

```js
swiper.on('keyPress', (swiper, keyCode) => {
  console.log('Taste gedrückt:', keyCode);
  // 37 = ArrowLeft, 38 = ArrowUp, 39 = ArrowRight, 40 = ArrowDown
  // 33 = Page Up, 34 = Page Down
});
```

## Vollständiges Beispiel

```js
const swiper = new Swiper('.swiper', {
  modules: [Keyboard],
  keyboard: {
    enabled: true,
    onlyInViewport: false, // immer reagieren, auch wenn außerhalb
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

// Dynamisch umschalten
document.querySelector('#toggle-keyboard').addEventListener('click', () => {
  if (swiper.keyboard.enabled) {
    swiper.keyboard.disable();
  } else {
    swiper.keyboard.enable();
  }
});
```

---
Quelle: https://swiperjs.com/swiper-api#keyboard-control
