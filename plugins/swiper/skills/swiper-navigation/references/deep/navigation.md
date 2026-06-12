# Swiper Navigation-Modul — Vollständige Referenz

## Import & Aktivierung

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

## HTML-Struktur

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

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `nextEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS-Selektor oder Element für den "Weiter"-Button |
| `prevEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS-Selektor oder Element für den "Zurück"-Button |
| `hideOnClick` | `boolean` | `false` | Navigation beim Klick auf den Slider-Container ein-/ausblenden |
| `disabledClass` | `string` | `'swiper-button-disabled'` | CSS-Klasse wenn Button inaktiv (erster/letzter Slide ohne Loop) |
| `hiddenClass` | `string` | `'swiper-button-hidden'` | CSS-Klasse wenn Button ausgeblendet |
| `lockClass` | `string` | `'swiper-button-lock'` | CSS-Klasse wenn Navigation per Breakpoint deaktiviert |
| `navigationDisabledClass` | `string` | `'swiper-navigation-disabled'` | Klasse am Container-Element wenn Navigation per Breakpoint deaktiviert |
| `addIcons` | `boolean` | `true` | SVG-Icons automatisch in die Buttons einfügen |
| `enabled` | `boolean` | — | Navigation für bestimmte Breakpoints aktivieren/deaktivieren |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.navigation.nextEl` | `HTMLElement` | Referenz auf den Next-Button |
| `swiper.navigation.prevEl` | `HTMLElement` | Referenz auf den Prev-Button |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.navigation.init()` | Navigation initialisieren |
| `swiper.navigation.destroy()` | Navigation entfernen und aufräumen |
| `swiper.navigation.update()` | Status (enabled/disabled) der Buttons aktualisieren |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `navigationHide` | `(swiper)` | Buttons werden ausgeblendet |
| `navigationShow` | `(swiper)` | Buttons werden eingeblendet |
| `navigationPrev` | `(swiper)` | Prev-Button wurde geklickt |
| `navigationNext` | `(swiper)` | Next-Button wurde geklickt |

```js
swiper.on('navigationNext', (swiper) => {
  console.log('Weiter geklickt, aktiver Index:', swiper.activeIndex);
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

## Breakpoint-spezifische Navigation

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

## Externe Buttons (außerhalb des Swiper-Containers)

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
Quelle: https://swiperjs.com/swiper-api#navigation
