# Swiper Scrollbar-Modul — Vollständige Referenz

## Import & Aktivierung

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

## HTML-Struktur

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
  </div>
  <div class="swiper-scrollbar"></div>
</div>
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `el` | `HTMLElement \| CSSSelector \| null` | `null` | Scrollbar-Container-Element oder Selektor |
| `draggable` | `boolean` | `false` | Scrollbar-Drag zur Slide-Navigation erlauben |
| `dragClass` | `string` | `'swiper-scrollbar-drag'` | CSS-Klasse für das Drag-Handle-Element |
| `dragSize` | `number \| 'auto'` | `'auto'` | Größe des Drag-Handles in px; `'auto'` = proportional |
| `hide` | `boolean` | `true` | Scrollbar nach Interaktion automatisch ausblenden |
| `snapOnRelease` | `boolean` | `false` | Beim Loslassen des Handles zum nächsten Slide snappen |
| `enabled` | `boolean` | — | Scrollbar für bestimmte Breakpoints aktivieren/deaktivieren |
| `horizontalClass` | `string` | `'swiper-scrollbar-horizontal'` | Klasse bei horizontaler Ausrichtung |
| `verticalClass` | `string` | `'swiper-scrollbar-vertical'` | Klasse bei vertikaler Ausrichtung |
| `lockClass` | `string` | `'swiper-scrollbar-lock'` | Klasse wenn Scrollbar gesperrt |
| `scrollbarDisabledClass` | `string` | `'swiper-scrollbar-disabled'` | Klasse am Container wenn per Breakpoint deaktiviert |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.scrollbar.el` | `HTMLElement` | Scrollbar-Container-Element |
| `swiper.scrollbar.dragEl` | `HTMLElement` | Drag-Handle-Element |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.scrollbar.init()` | Scrollbar initialisieren |
| `swiper.scrollbar.destroy()` | Scrollbar entfernen |
| `swiper.scrollbar.setTranslate()` | Scrollbar-Position synchronisieren |
| `swiper.scrollbar.updateSize()` | Track- und Handle-Größen neu berechnen |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `scrollbarDragStart` | `(swiper, event)` | Drag des Handles beginnt |
| `scrollbarDragMove` | `(swiper, event)` | Handle wird gezogen |
| `scrollbarDragEnd` | `(swiper, event)` | Drag des Handles endet |

```js
swiper.on('scrollbarDragEnd', (swiper, event) => {
  console.log('Drag beendet, aktiver Slide:', swiper.activeIndex);
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

## Vollständiges Beispiel (vertikal mit Snap)

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
Quelle: https://swiperjs.com/swiper-api#scrollbar
