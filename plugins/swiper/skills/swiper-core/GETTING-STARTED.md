# Swiper — Getting Started

Touch-fähiger Slider/Carousel ohne externe Abhängigkeiten. Unterstützt Mobile, Desktop, moderne Browser.

```bash
npm install swiper
```

```js
// Minimal (Core only)
import Swiper from 'swiper';
import 'swiper/css';
const swiper = new Swiper('.swiper', { loop: true });
```

```html
<!-- CDN (schnellster Einstieg) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
```

```html
<!-- Pflicht-HTML-Struktur -->
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
  </div>
</div>
```

## Vertiefung
- [GETTING-STARTED-DETAIL.md](GETTING-STARTED-DETAIL.md) — vollständige Installations-, Import- und Init-Referenz mit allen CSS-Pfaden, Modul-Varianten und Framework-Hinweisen
