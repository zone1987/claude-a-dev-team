# Swiper Free Mode-Modul — Vollständige Referenz

## Konzept

Free Mode deaktiviert das Snapping zu festen Slide-Positionen. Der Slider scrollt frei und kann — je nach Konfiguration — mit physikalischem Momentum (Trägheit) weiterrollen.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { FreeMode } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: {
    enabled: true,
    momentum: true,
  },
});
```

**Kurzform** (Standard-Konfiguration):
```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: true,
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Free Mode aktivieren |
| `momentum` | `boolean` | `true` | Slides rollen nach dem Loslassen noch weiter |
| `momentumRatio` | `number` | `1` | Multiplikator für die Momentum-Entfernung (> 1 = weiter) |
| `momentumVelocityRatio` | `number` | `1` | Multiplikator für die Momentum-Geschwindigkeit |
| `momentumBounce` | `boolean` | `true` | Bounce-Effekt an den Rändern aktivieren |
| `momentumBounceRatio` | `number` | `1` | Stärke des Bounce-Effekts (> 1 = stärker) |
| `minimumVelocity` | `number` | `0.02` | Mindest-Swipe-Geschwindigkeit um Momentum auszulösen |
| `sticky` | `boolean` | `false` | Nach dem Loslassen zum nächsten Slide snappen |

## Verhältnis zu anderen Parametern

Free Mode kann mit folgenden Core-Parametern kombiniert werden:

```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  slidesPerView: 'auto',    // Slides in Originalgröße
  spaceBetween: 16,
  freeMode: {
    enabled: true,
    momentum: true,
    momentumRatio: 0.5,     // langsameres Auslaufen
  },
});
```

## Konfigurationsbeispiele

### Einfacher Tag-Cloud-Slider (horizontal, kein Momentum)

```js
const swiper = new Swiper('.tags-swiper', {
  modules: [FreeMode],
  slidesPerView: 'auto',
  spaceBetween: 8,
  freeMode: {
    enabled: true,
    momentum: false,
  },
});
```

### Momentum-Scroll mit Sticky-Snap

```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  slidesPerView: 2.5,
  spaceBetween: 20,
  freeMode: {
    enabled: true,
    sticky: true,         // snapped nach dem Loslassen
    momentum: true,
    momentumRatio: 0.8,
    momentumBounce: true,
    momentumBounceRatio: 0.5,
  },
});
```

### Hohe Sensitivität ohne Bounce

```js
const swiper = new Swiper('.swiper', {
  modules: [FreeMode],
  freeMode: {
    enabled: true,
    momentum: true,
    momentumRatio: 1.5,
    momentumVelocityRatio: 1.5,
    momentumBounce: false,
    minimumVelocity: 0.05,
  },
});
```

---
Quelle: https://swiperjs.com/swiper-api#free-mode
