# Swiper — Manipulation-Modul

Slides dynamisch im DOM hinzufügen, einfügen und entfernen.

```js
import Swiper from 'swiper';
import { Manipulation } from 'swiper/modules';

const swiper = new Swiper('.swiper', { modules: [Manipulation] });

// Hinzufügen
swiper.appendSlide('<div class="swiper-slide">Neu am Ende</div>');
swiper.prependSlide('<div class="swiper-slide">Neu am Anfang</div>');
swiper.addSlide(2, '<div class="swiper-slide">An Position 2</div>');

// Mehrere auf einmal
swiper.appendSlide([
  '<div class="swiper-slide">A</div>',
  '<div class="swiper-slide">B</div>',
]);

// Entfernen
swiper.removeSlide(0);           // einzeln
swiper.removeSlide([0, 1, 2]);   // mehrere
swiper.removeAllSlides();        // alle
```

**Hinweis:** Dieses Modul ist für Swiper Core gedacht, nicht für React/Vue-Integrationen.

## Vertiefung
- [MANIPULATION-DETAIL.md](MANIPULATION-DETAIL.md) — alle Methoden-Signaturen, Parametertypen, Framework-Hinweise
