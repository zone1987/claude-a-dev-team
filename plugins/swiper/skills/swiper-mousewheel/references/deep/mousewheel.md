# Swiper Mousewheel-Modul — Vollständige Referenz

## Import & Aktivierung

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

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Mausrad-Steuerung aktivieren |
| `eventsTarget` | `HTMLElement \| string` | `'container'` | Element das Mausrad-Events empfängt; `'container'` = Swiper-Container |
| `invert` | `boolean` | `false` | Scroll-Richtung umkehren |
| `forceToAxis` | `boolean` | `false` | Scroll auf die Swiper-Achse beschränken (verhindert diagonales Scrollen) |
| `releaseOnEdges` | `boolean` | `false` | Seiten-Scrollen erlauben wenn Swiper am ersten/letzten Slide ist |
| `sensitivity` | `number` | `1` | Multiplikator für Scroll-Delta (> 1 = empfindlicher) |
| `thresholdDelta` | `number \| null` | `null` | Mindest-Scroll-Delta zum Auslösen einer Transition |
| `thresholdTime` | `number \| null` | `null` | Mindest-Zeit in ms zwischen Scroll-Events |
| `noMousewheelClass` | `string` | `'swiper-no-mousewheel'` | CSS-Klasse auf Kindelementen um Mausrad dort zu deaktivieren |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.mousewheel.enabled` | `boolean` | Gibt an ob Mausrad-Steuerung aktiv ist |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.mousewheel.enable()` | Mausrad-Steuerung aktivieren |
| `swiper.mousewheel.disable()` | Mausrad-Steuerung deaktivieren |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `scroll` | `(swiper, event)` | Wird bei Mausrad-Scroll ausgelöst |

## noMousewheelClass — Scroll in Kindelementen deaktivieren

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <!-- Dieses Element scrollt normal, löst keinen Slide-Wechsel aus -->
      <div class="swiper-no-mousewheel" style="overflow-y: scroll; height: 200px;">
        Langer Text der gescrollt werden kann...
      </div>
    </div>
  </div>
</div>
```

## Vollständige Beispiele

### Vollbild-Vertikalscroller

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

### Mit Body als Event-Target

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
Quelle: https://swiperjs.com/swiper-api#mousewheel-control
