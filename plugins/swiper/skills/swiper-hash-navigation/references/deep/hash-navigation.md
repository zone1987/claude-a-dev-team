# Swiper Hash Navigation-Modul — Vollständige Referenz

## Konzept

Das Hash Navigation-Modul aktualisiert den URL-Hash beim Slide-Wechsel und navigiert umgekehrt bei Hash-Änderungen (z.B. Browser-Back, direkter Link mit Hash). Einfacher als History-Modul — erfordert keine Server-Konfiguration.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { HashNavigation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [HashNavigation],
  hashNavigation: {
    enabled: true,
    replaceState: false,
    watchState: true,
  },
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `true` | Hash Navigation aktivieren |
| `replaceState` | `boolean` | `false` | `history.replaceState` für Hash-Updates verwenden (kein Verlaufseintrag) |
| `watchState` | `boolean` | `false` | Externe Hash-Änderungen (Browser-Back, direkte URL) beobachten und reagieren |

## data-hash-Attribut

Jeder Slide bekommt ein `data-hash`-Attribut:

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <!-- URL-Hash wird zu: #slide-1 -->
    <div class="swiper-slide" data-hash="slide-1">Slide 1</div>
    <!-- URL-Hash wird zu: #slide-2 -->
    <div class="swiper-slide" data-hash="slide-2">Slide 2</div>
    <!-- URL-Hash wird zu: #slide-3 -->
    <div class="swiper-slide" data-hash="slide-3">Slide 3</div>
  </div>
</div>
```

## URL-Format

| Aktiver Slide | URL |
|---------------|-----|
| `data-hash="intro"` | `https://example.com/#intro` |
| `data-hash="gallery"` | `https://example.com/#gallery` |
| `data-hash="contact"` | `https://example.com/#contact` |

## watchState — Externe Hash-Navigierung

Mit `watchState: true` reagiert Swiper auf externe Hash-Änderungen:

```js
// Nutzer navigiert mit Browser-Back/Forward
// oder öffnet https://example.com/#slide-3 direkt
// → Swiper springt zum Slide mit data-hash="slide-3"
const swiper = new Swiper('.swiper', {
  modules: [HashNavigation],
  hashNavigation: {
    watchState: true,
  },
});
```

## Vollständige Beispiele

### Einzel-Seite mit verankerbaren Sektionen

```js
import Swiper from 'swiper';
import { HashNavigation, Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [HashNavigation, Navigation, Pagination],
  direction: 'vertical',
  hashNavigation: {
    enabled: true,
    watchState: true,
    replaceState: false,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});
```

HTML:
```html
<div class="swiper-slide" data-hash="home">Home</div>
<div class="swiper-slide" data-hash="ueber-uns">Über uns</div>
<div class="swiper-slide" data-hash="leistungen">Leistungen</div>
<div class="swiper-slide" data-hash="kontakt">Kontakt</div>
```

### Externer Link zum Slide

```html
<!-- Direkter Link zum Kontakt-Slide -->
<a href="/page#kontakt">Kontakt öffnen</a>
```

## Unterschied zu History-Modul

| Feature | Hash Navigation | History-Modul |
|---------|-----------------|---------------|
| URL-Format | `/#slide-name` | `/slides/slide-name` |
| Server-Rewrite | Nicht nötig | Erforderlich für direkte Links |
| Attribut | `data-hash` | `data-history` |
| Parameter-Key | — | `key` (URL-Präfix) |

---
Quelle: https://swiperjs.com/swiper-api#hash-navigation
