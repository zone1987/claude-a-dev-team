# Swiper Parallax-Modul — Vollständige Referenz

## Konzept

Das Parallax-Modul ermöglicht Parallax-Scroll-Effekte auf beliebigen HTML-Elementen innerhalb des Swipers. Elemente bewegen sich mit unterschiedlicher Geschwindigkeit relativ zum Slide-Übergang. Zwei Scoping-Bereiche:

- **Direkte Swiper-Kinder** (z.B. Hintergründe): Parallax basiert auf dem Gesamtfortschritt des Swipers
- **Slide-Kinder** (Texte, Icons): Parallax basiert auf dem Fortschritt des einzelnen Slides

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Parallax } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  parallax: true,    // oder: parallax: { enabled: true }
  speed: 600,        // Parallax-Timing folgt dem Transition-Speed
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Parallax-Modul aktivieren |

**Hinweis:** Das Modul hat nur diesen einen Parameter. Alle Parallax-Werte werden über HTML-Data-Attribute gesteuert.

## Data-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `data-swiper-parallax` | `number` (px) oder `string` (%) | Translate-Versatz auf der Slide-Bewegungsachse |
| `data-swiper-parallax-x` | `number` (px) oder `string` (%) | Horizontaler Parallax-Versatz |
| `data-swiper-parallax-y` | `number` (px) oder `string` (%) | Vertikaler Parallax-Versatz |
| `data-swiper-parallax-scale` | `number` | Skalierungsfaktor wenn Slide inaktiv (1 = Originalgröße) |
| `data-swiper-parallax-opacity` | `number` (0–1) | Opazität wenn Slide inaktiv |
| `data-swiper-parallax-duration` | `number` (ms) | Eigene Transition-Dauer für dieses Element |

## Werte erklärt

- **Positiver Wert:** Element bewegt sich langsamer als der Slide (klassischer Parallax)
- **Negativer Wert:** Element bewegt sich schneller als der Slide (inverser Parallax)
- **Prozent-Werte:** Relativ zur Swiper-Container-Breite/-Höhe
- **`data-swiper-parallax="-23%"`** auf einem direkten Kind: bewegt sich 23% weniger als der Swiper scrollt

## Vollständiges HTML-Beispiel

```html
<div class="swiper">
  <!-- Parallax-Hintergrund (direktes Kind = basiert auf Gesamt-Progress) -->
  <div
    class="parallax-bg"
    style="background-image: url(background.jpg); position: absolute; width: 130%; height: 100%; left: -15%;"
    data-swiper-parallax="-23%"
  ></div>

  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <!-- Slide-Kinder: Parallax basiert auf diesem Slide's Progress -->

      <!-- Starker Versatz (bewegt sich schneller) -->
      <div class="slide-icon"
           data-swiper-parallax="-200"
           data-swiper-parallax-opacity="0">
        🎯
      </div>

      <!-- Mittlerer Versatz -->
      <h2 class="slide-title" data-swiper-parallax="-100">
        Slide-Titel
      </h2>

      <!-- Leichter Versatz mit eigenem Timing -->
      <p class="slide-text"
         data-swiper-parallax="-50"
         data-swiper-parallax-duration="800">
        Beschreibungstext
      </p>

      <!-- Nur Skalierung -->
      <div class="slide-badge"
           data-swiper-parallax-scale="0.5">
        Neu
      </div>

      <!-- X und Y separat -->
      <div class="slide-element"
           data-swiper-parallax-x="-100"
           data-swiper-parallax-y="-50">
        Diagonaler Parallax
      </div>
    </div>
  </div>
</div>
```

## Konfigurationsbeispiele

### Einfache Text-Animation

```js
const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  parallax: true,
  speed: 800,
});
```

```html
<div class="swiper-slide">
  <h1 data-swiper-parallax="-300">Großer Titel</h1>
  <p data-swiper-parallax="-150">Untertitel mit halbem Versatz</p>
</div>
```

### Mit verschiedenen Achsen (vertikaler Slider)

```js
const swiper = new Swiper('.swiper', {
  modules: [Parallax],
  direction: 'vertical',
  parallax: true,
});
```

```html
<!-- Bei vertikalem Slider: data-swiper-parallax wirkt auf Y-Achse -->
<div class="swiper-slide">
  <div data-swiper-parallax="-200">Parallax nach oben/unten</div>
  <div data-swiper-parallax-x="-100">Horizontaler Parallax-Akzent</div>
</div>
```

### Hintergrund + Inhalt kombiniert

```js
const swiper = new Swiper('.swiper', {
  modules: [Parallax, Autoplay],
  parallax: true,
  speed: 1000,
  autoplay: { delay: 4000 },
});
```

---
Quelle: https://swiperjs.com/swiper-api#parallax
