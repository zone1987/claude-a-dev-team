# Swiper — Getting Started

Touch-enabled slider/carousel with no external dependencies. Supports mobile, desktop and modern browsers.

```bash
npm install swiper
```

```js
// Minimal (core only)
import Swiper from 'swiper';
import 'swiper/css';
const swiper = new Swiper('.swiper', { loop: true });
```

```html
<!-- CDN (fastest way to start) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
```

```html
<!-- Required HTML structure -->
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
  </div>
</div>
```

## Further reading
- [GETTING-STARTED-DETAIL.md](GETTING-STARTED-DETAIL.md) — complete installation, import and init reference with all CSS paths, module variants and framework notes
