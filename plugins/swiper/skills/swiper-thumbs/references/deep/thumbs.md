# Swiper Thumbs-Modul — Vollständige Referenz

## Konzept

Das Thumbs-Modul synchronisiert einen Thumbnail-Swiper mit einem Haupt-Swiper. Der Thumbnail-Swiper zeigt kleine Vorschaubilder; das Aktivieren eines Thumbnails wechselt den Haupt-Slider.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Thumbs, Navigation } from 'swiper/modules';

// Zuerst den Thumbs-Swiper erstellen
const thumbsSwiper = new Swiper('.swiper-thumbs', {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,  // Wichtig für korrekte Synchronisierung!
});

// Dann den Haupt-Swiper mit thumbs-Konfiguration
const mainSwiper = new Swiper('.swiper-main', {
  modules: [Thumbs, Navigation],
  spaceBetween: 10,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  thumbs: {
    swiper: thumbsSwiper,
    multipleActiveThumbs: false,
    autoScrollOffset: 0,
  },
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `swiper` | `Swiper \| SwiperOptions \| null` | `null` | Thumbs-Swiper-Instanz oder Konfigurationsobjekt |
| `multipleActiveThumbs` | `boolean` | `true` | Mehrere Thumbnails gleichzeitig als aktiv markieren (wenn `slidesPerView > 1`) |
| `autoScrollOffset` | `number` | `0` | Ab wie vielen Slides vom Rand der aktive Thumbnail automatisch in den sichtbaren Bereich gescrollt wird |
| `slideThumbActiveClass` | `string` | `'swiper-slide-thumb-active'` | CSS-Klasse für den aktiven Thumbnail-Slide |
| `thumbsContainerClass` | `string` | `'swiper-thumbs'` | CSS-Klasse für den Thumbs-Container |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.thumbs.swiper` | `Swiper` | Referenz auf die Thumbs-Swiper-Instanz |

## Methoden

| Methode | Signatur | Beschreibung |
|---------|---------|--------------|
| `swiper.thumbs.init()` | `() => void` | Thumbs-Modul initialisieren |
| `swiper.thumbs.update(initial?, position?)` | `(initial?: boolean, position?: string) => void` | Thumbs-Status aktualisieren |

## HTML-Struktur

```html
<!-- Haupt-Swiper -->
<div class="swiper-main">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <img src="image1-full.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image2-full.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image3-full.jpg" />
    </div>
  </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>

<!-- Thumbs-Swiper -->
<div class="swiper-thumbs">
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <img src="image1-thumb.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image2-thumb.jpg" />
    </div>
    <div class="swiper-slide">
      <img src="image3-thumb.jpg" />
    </div>
  </div>
</div>
```

## CSS für aktiven Thumbnail

```css
.swiper-thumbs .swiper-slide {
  opacity: 0.4;
  cursor: pointer;
  transition: opacity 0.3s;
}

.swiper-thumbs .swiper-slide-thumb-active {
  opacity: 1;
}
```

## Thumbs via Konfigurationsobjekt (ohne separate Instanz)

```js
const mainSwiper = new Swiper('.swiper-main', {
  modules: [Thumbs],
  thumbs: {
    swiper: {
      el: '.swiper-thumbs',
      spaceBetween: 10,
      slidesPerView: 4,
      watchSlidesProgress: true,
    },
  },
});
```

## Vollständiges Galerie-Beispiel

```js
import Swiper from 'swiper';
import { Thumbs, Navigation, Keyboard } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';

const thumbsSwiper = new Swiper('.gallery-thumbs', {
  slidesPerView: 'auto',
  spaceBetween: 8,
  centeredSlides: true,
  slideToClickedSlide: true,
  watchSlidesProgress: true,
});

const gallerySwiper = new Swiper('.gallery-main', {
  modules: [Thumbs, Navigation, Keyboard],
  spaceBetween: 16,
  keyboard: { enabled: true },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  thumbs: {
    swiper: thumbsSwiper,
    multipleActiveThumbs: false,
    autoScrollOffset: 2,
  },
});
```

---
Quelle: https://swiperjs.com/swiper-api#thumbs
