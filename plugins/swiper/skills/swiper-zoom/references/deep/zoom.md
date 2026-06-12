# Swiper Zoom-Modul — Vollständige Referenz

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Zoom } from 'swiper/modules';
import 'swiper/css/zoom';

const swiper = new Swiper('.swiper', {
  modules: [Zoom],
  zoom: {
    maxRatio: 3,
    minRatio: 1,
    toggle: true,
  },
});
```

## HTML-Struktur

Alle zoom-fähigen Bilder müssen in `.swiper-zoom-container` eingewickelt werden:

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <!-- Standard-Zoom -->
    <div class="swiper-slide">
      <div class="swiper-zoom-container">
        <img src="image1.jpg" />
      </div>
    </div>

    <!-- Per-Slide maxRatio überschreiben -->
    <div class="swiper-slide">
      <div class="swiper-zoom-container" data-swiper-zoom="5">
        <img src="image2.jpg" />
      </div>
    </div>

    <!-- Benutzerdefiniertes Zoom-Target (nicht img) -->
    <div class="swiper-slide">
      <div class="swiper-zoom-container">
        <div class="swiper-zoom-target">
          Zoomfähiger Inhalt
        </div>
      </div>
    </div>
  </div>
</div>
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Zoom-Modul aktivieren |
| `maxRatio` | `number` | `3` | Maximaler Zoom-Faktor (3 = 300%) |
| `minRatio` | `number` | `1` | Minimaler Zoom-Faktor (1 = Originalgröße) |
| `toggle` | `boolean` | `true` | Zoom per Doppeltipp ein-/ausschalten |
| `containerClass` | `string` | `'swiper-zoom-container'` | CSS-Klasse für Zoom-Container-Elemente |
| `zoomedSlideClass` | `string` | `'swiper-slide-zoomed'` | CSS-Klasse für den aktuell gezoomten Slide |
| `limitToOriginalSize` | `boolean` | `false` | Bild nie über 100% seiner Originalgröße zoomen |
| `panOnMouseMove` | `boolean` | `false` | Gezoomtes Bild beim Mausbewegen automatisch verschieben |

## Data-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `data-swiper-zoom` | `number` | Per-Slide `maxRatio` überschreiben |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.zoom.enabled` | `boolean` | Zoom-Modul aktiv? |
| `swiper.zoom.scale` | `number` | Aktueller Zoom-Faktor des aktiven Slides |

## Methoden

| Methode | Signatur | Beschreibung |
|---------|---------|--------------|
| `swiper.zoom.enable()` | `() => void` | Zoom-Modul aktivieren |
| `swiper.zoom.disable()` | `() => void` | Zoom-Modul deaktivieren |
| `swiper.zoom.in(ratio?)` | `(ratio?: number) => void` | Aktiven Slide hereinzoomen; optionaler Ziel-Faktor |
| `swiper.zoom.out()` | `() => void` | Aktiven Slide auf `minRatio` zurückzoomen |
| `swiper.zoom.toggle(event?)` | `(event?: Event) => void` | Zoom-Status des aktiven Slides umschalten |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `zoomChange` | `(swiper, scale, imageEl, slideEl)` | Wird ausgelöst wenn sich der Zoom-Faktor ändert |

```js
swiper.on('zoomChange', (swiper, scale, imageEl, slideEl) => {
  console.log('Aktueller Zoom:', scale);
  if (scale > 1) {
    slideEl.classList.add('is-zoomed');
  } else {
    slideEl.classList.remove('is-zoomed');
  }
});
```

## Programmatische Steuerung

```js
// Auf 2x zoomen
swiper.zoom.in(2);

// Zurück auf Originalgröße
swiper.zoom.out();

// Toggle
document.querySelector('#zoom-btn').addEventListener('click', () => {
  swiper.zoom.toggle();
});

// Zoom anzeigen
document.querySelector('#scale').textContent = swiper.zoom.scale + 'x';
```

## Vollständiges Beispiel (Foto-Galerie)

```js
import Swiper from 'swiper';
import { Zoom, Navigation, Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/zoom';
import 'swiper/css/navigation';

const swiper = new Swiper('.gallery-swiper', {
  modules: [Zoom, Navigation, Pagination],
  zoom: {
    maxRatio: 5,
    minRatio: 1,
    toggle: true,
    limitToOriginalSize: false,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
  },
  on: {
    zoomChange: (swiper, scale) => {
      // Navigation bei gezoomtem Bild ausblenden
      document.querySelector('.swiper-button-next').style.opacity =
        scale > 1 ? '0' : '1';
    },
  },
});
```

---
Quelle: https://swiperjs.com/swiper-api#zoom
