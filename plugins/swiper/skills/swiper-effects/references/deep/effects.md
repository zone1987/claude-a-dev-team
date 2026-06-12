# Swiper Übergangseffekte — Vollständige Referenz

Swiper unterstützt sechs Übergangseffekte. Jeder Effekt wird als separates Modul importiert.

## Übersicht der Import-Namen

| Effekt | `effect`-Wert | Modul-Import |
|--------|---------------|--------------|
| Überblendung | `'fade'` | `EffectFade` |
| Würfel | `'cube'` | `EffectCube` |
| Coverflow | `'coverflow'` | `EffectCoverflow` |
| Flip | `'flip'` | `EffectFlip` |
| Karten | `'cards'` | `EffectCards` |
| Kreativ | `'creative'` | `EffectCreative` |

---

## 1. Fade Effect — `fadeEffect`

**Importname:** `EffectFade`

```js
import Swiper from 'swiper';
import { EffectFade } from 'swiper/modules';
import 'swiper/css/effect-fade';

const swiper = new Swiper('.swiper', {
  modules: [EffectFade],
  effect: 'fade',
  fadeEffect: {
    crossFade: true,
  },
});
```

### Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `crossFade` | `boolean` | `false` | Cross-Fade aktivieren: beide Slides gleichzeitig ein-/ausblenden. `false` = nur Einblenden des aktiven Slides. |

**Hinweis:** Bei `crossFade: false` bleibt der vorherige Slide unter dem neuen sichtbar, bis der neue vollständig eingeblendet ist.

---

## 2. Cube Effect — `cubeEffect`

**Importname:** `EffectCube`

```js
import Swiper from 'swiper';
import { EffectCube } from 'swiper/modules';
import 'swiper/css/effect-cube';

const swiper = new Swiper('.swiper', {
  modules: [EffectCube],
  effect: 'cube',
  cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
  },
});
```

### Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `shadow` | `boolean` | `true` | Hauptschatten unter dem Würfel anzeigen |
| `shadowOffset` | `number` | `20` | Versatz des Hauptschattens in px |
| `shadowScale` | `number` | `0.94` | Skalierungsfaktor des Hauptschattens |
| `slideShadows` | `boolean` | `true` | Schatten auf den Würfelflächen (Slides) anzeigen |

---

## 3. Coverflow Effect — `coverflowEffect`

**Importname:** `EffectCoverflow`

```js
import Swiper from 'swiper';
import { EffectCoverflow } from 'swiper/modules';
import 'swiper/css/effect-coverflow';

const swiper = new Swiper('.swiper', {
  modules: [EffectCoverflow],
  effect: 'coverflow',
  centeredSlides: true,
  slidesPerView: 'auto',
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 1,
    scale: 1,
    slideShadows: true,
  },
});
```

### Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `rotate` | `number` | `50` | Rotationswinkel der Neben-Slides in Grad |
| `stretch` | `number \| string` | `0` | Zusätzlicher Abstand zwischen Slides in px oder % |
| `depth` | `number` | `100` | Z-Versatz der Neben-Slides in px |
| `modifier` | `number` | `1` | Verstärkungs-/Dämpfungsfaktor für alle Effekte |
| `scale` | `number` | `1` | Skalierungsfaktor der Neben-Slides (< 1 = kleiner) |
| `slideShadows` | `boolean` | `true` | Schatten auf Slides anzeigen |

---

## 4. Flip Effect — `flipEffect`

**Importname:** `EffectFlip`

```js
import Swiper from 'swiper';
import { EffectFlip } from 'swiper/modules';
import 'swiper/css/effect-flip';

const swiper = new Swiper('.swiper', {
  modules: [EffectFlip],
  effect: 'flip',
  flipEffect: {
    slideShadows: true,
    limitRotation: true,
  },
});
```

### Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `slideShadows` | `boolean` | `true` | Schatten auf Slides während des Flip-Effekts |
| `limitRotation` | `boolean` | `true` | Rotation am ersten und letzten Slide begrenzen |

---

## 5. Cards Effect — `cardsEffect`

**Importname:** `EffectCards`

```js
import Swiper from 'swiper';
import { EffectCards } from 'swiper/modules';
import 'swiper/css/effect-cards';

const swiper = new Swiper('.swiper', {
  modules: [EffectCards],
  effect: 'cards',
  cardsEffect: {
    rotate: true,
    perSlideRotate: 2,
    perSlideOffset: 8,
    slideShadows: true,
  },
});
```

### Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `rotate` | `boolean` | `true` | Karten-Rotation aktivieren |
| `perSlideRotate` | `number` | `2` | Rotationswinkel pro Slide-Stufe in Grad |
| `perSlideOffset` | `number` | `8` | Versatz pro Slide-Stufe in px |
| `slideShadows` | `boolean` | `true` | Schatten auf Karten anzeigen |

---

## 6. Creative Effect — `creativeEffect`

**Importname:** `EffectCreative`

Ermöglicht vollständig benutzerdefinierte 3D-Transformationen je Slide-Position.

```js
import Swiper from 'swiper';
import { EffectCreative } from 'swiper/modules';
import 'swiper/css/effect-creative';

const swiper = new Swiper('.swiper', {
  modules: [EffectCreative],
  effect: 'creative',
  creativeEffect: {
    prev: {
      // Vorherige Slides
      shadow: true,
      translate: ['-20%', 0, -1],
    },
    next: {
      // Nächste Slides
      translate: ['100%', 0, 0],
    },
  },
});
```

### Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `prev` | `CreativeEffectTransform` | — | Transform-Objekt für Slides vor dem aktiven |
| `next` | `CreativeEffectTransform` | — | Transform-Objekt für Slides nach dem aktiven |
| `perspective` | `boolean` | `true` | 3D-Perspektive aktivieren (erforderlich für 3D-Transforms) |
| `progressMultiplier` | `number` | `1` | Verstärkungsfaktor für Transformations-Intensität |
| `limitProgress` | `number` | `1` | Anzahl der Slides die Transforms erhalten (über aktive hinaus) |
| `shadowPerProgress` | `boolean` | `false` | Schatten-Opazität über mehrere Slides verteilen |

### Transform-Objekt Schema (`CreativeEffectTransform`)

```ts
interface CreativeEffectTransform {
  translate: [x: string | number, y: string | number, z: string | number];
  rotate?: [x: number, y: number, z: number]; // in Grad
  opacity?: number;   // 0..1
  scale?: number;     // 1 = Originalgröße
  shadow?: boolean;   // Schatten anzeigen
  origin?: string;    // CSS transform-origin, z.B. 'left bottom'
}
```

### Beispiele für kreative Effekte

```js
// Slide-herein-Effekt (Classic)
creativeEffect: {
  prev: { translate: [0, 0, -400] },
  next: { translate: ['100%', 0, 0] },
}

// Überblendung mit Skalierung
creativeEffect: {
  prev: {
    shadow: true,
    translate: ['-125%', 0, -800],
    rotate: [0, 0, -90],
  },
  next: {
    translate: ['125%', 0, -800],
    rotate: [0, 0, 90],
  },
}

// Von oben nach unten
creativeEffect: {
  prev: {
    shadow: true,
    translate: [0, '-120%', 0],
  },
  next: {
    translate: [0, '120%', 0],
  },
}
```

---
Quelle: https://swiperjs.com/swiper-api#fade-effect
