---
name: swiper-getting-started
description: >
  Swiper installieren und einbinden: npm, CDN, CSS-Imports, HTML-Struktur, erste Instanz,
  Module registrieren, Core vs. Bundle vs. Element, Framework-Integration.
  Trigger: "swiper installieren", "swiper einbinden", "swiper setup", "swiper init",
  "swiper npm", "swiper CDN", "swiper getting started", "swiper html struktur",
  "swiper module registrieren", "new Swiper", "swiper-wrapper", "swiper-slide",
  "install swiper", "swiper setup guide", "swiper first steps".
---

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
- [references/deep/getting-started.md](references/deep/getting-started.md) — vollständige Installations-, Import- und Init-Referenz mit allen CSS-Pfaden, Modul-Varianten und Framework-Hinweisen
