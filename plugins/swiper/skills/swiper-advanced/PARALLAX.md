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
- [PARALLAX-DETAIL.md](PARALLAX-DETAIL.md) — alle Data-Attribute mit Typ/Beschreibung, Scoping-Regeln
