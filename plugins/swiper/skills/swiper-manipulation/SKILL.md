---
name: swiper-manipulation
description: >
  Vollständige Referenz des Swiper Manipulation-Moduls: appendSlide, prependSlide,
  addSlide(index), removeSlide, removeAllSlides — dynamisches Hinzufügen/Entfernen von Slides.
  Trigger: "swiper manipulation", "swiper add slide", "swiper remove slide",
  "swiper appendSlide", "swiper prependSlide", "swiper addSlide",
  "swiper removeSlide", "swiper removeAllSlides", "swiper dynamic slides",
  "swiper manipulation module", "swiper insert slide".
---

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
- [references/deep/manipulation.md](references/deep/manipulation.md) — alle Methoden-Signaturen, Parametertypen, Framework-Hinweise
