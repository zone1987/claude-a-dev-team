---
name: swiper-parallax
description: >
  Vollständige Referenz des Swiper Parallax-Moduls: data-swiper-parallax,
  data-swiper-parallax-x/y, data-swiper-parallax-scale, data-swiper-parallax-opacity,
  data-swiper-parallax-duration — Parallax-Effekte für Hintergründe und Slide-Inhalte.
  Trigger: "swiper parallax", "swiper parallax module", "swiper parallax effect",
  "swiper data-swiper-parallax", "swiper parallax background", "swiper parallax text",
  "swiper parallax scale opacity", "swiper parallax parameters", "swiper parallax enabled".
---

# Swiper — Parallax-Modul

Parallax-Effekte auf Hintergründe und Slide-Elemente via Data-Attribute.

```js
import Swiper from 'swiper';
import { Parallax } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  parallax: true,
  speed: 600,
});
```

HTML:
```html
<div class="swiper">
  <!-- Hintergrund: bewegt sich mit Swiper-Gesamtfortschritt -->
  <div class="parallax-bg" style="background-image:url(bg.jpg)"
       data-swiper-parallax="-23%"></div>

  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <div class="title" data-swiper-parallax="-100">Titel</div>
      <div class="subtitle" data-swiper-parallax="-200" data-swiper-parallax-opacity="0.5">
        Untertitel
      </div>
      <div class="text" data-swiper-parallax="-300" data-swiper-parallax-duration="600">
        Text mit eigenem Timing
      </div>
    </div>
  </div>
</div>
```

## Vertiefung
- [references/deep/parallax.md](references/deep/parallax.md) — alle Data-Attribute mit Typ/Beschreibung, Scoping-Regeln
