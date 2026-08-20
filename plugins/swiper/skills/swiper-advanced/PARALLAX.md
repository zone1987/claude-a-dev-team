# Swiper — Parallax module

Parallax effects on backgrounds and slide elements via data attributes.

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
  <!-- Background: moves with the overall Swiper progress -->
  <div class="parallax-bg" style="background-image:url(bg.jpg)"
       data-swiper-parallax="-23%"></div>

  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <div class="title" data-swiper-parallax="-100">Title</div>
      <div class="subtitle" data-swiper-parallax="-200" data-swiper-parallax-opacity="0.5">
        Subtitle
      </div>
      <div class="text" data-swiper-parallax="-300" data-swiper-parallax-duration="600">
        Text with its own timing
      </div>
    </div>
  </div>
</div>
```

## Further reading
- [PARALLAX-DETAIL.md](PARALLAX-DETAIL.md) — all data attributes with type/description, scoping rules
