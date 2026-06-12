# Swiper History-Modul — Vollständige Referenz

## Konzept

Das History-Modul integriert Swiper in den Browser-Verlauf. Jeder Slide erhält eine eigene URL, sodass Nutzer mit den Browser-Back/Forward-Buttons navigieren können und direkte Links zu spezifischen Slides möglich sind.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { History } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [History],
  history: {
    key: 'slides',
    replaceState: false,
    keepQuery: true,
  },
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `true` | History-Modul aktivieren |
| `key` | `string` | `'slides'` | URL-Präfix; erzeugt URLs wie `/slides/slide-name` |
| `replaceState` | `boolean` | `false` | `history.replaceState` statt `pushState` verwenden (kein Eintrag im Verlauf) |
| `keepQuery` | `boolean` | `false` | Query-Parameter der aktuellen URL beibehalten |
| `root` | `string` | `''` | Wurzelpfad für History-URLs |

## data-history-Attribut

Jeder Slide braucht ein `data-history`-Attribut mit dem URL-Segment:

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <!-- URL wird zu: /slides/einfuehrung -->
    <div class="swiper-slide" data-history="einfuehrung">
      Einführung
    </div>
    <!-- URL wird zu: /slides/kapitel-1 -->
    <div class="swiper-slide" data-history="kapitel-1">
      Kapitel 1
    </div>
    <!-- URL wird zu: /slides/fazit -->
    <div class="swiper-slide" data-history="fazit">
      Fazit
    </div>
  </div>
</div>
```

## URL-Schema

Mit `key: 'slides'` und `root: '/'`:

| Aktiver Slide | Resultierende URL |
|---------------|------------------|
| `data-history="intro"` | `/slides/intro` |
| `data-history="chapter-2"` | `/slides/chapter-2` |
| `data-history="end"` | `/slides/end` |

## Vollständige Konfigurationsbeispiele

### Präsentation mit sauberem URL-Schema

```js
import Swiper from 'swiper';
import { History, Keyboard } from 'swiper/modules';

const swiper = new Swiper('.presentation', {
  modules: [History, Keyboard],
  slidesPerView: 1,
  keyboard: { enabled: true },
  history: {
    key: 'folie',
    replaceState: false,
    keepQuery: false,
    root: '/praesentation',
  },
  speed: 600,
});
```

HTML:
```html
<div class="swiper-slide" data-history="einleitung">...</div>
<div class="swiper-slide" data-history="hintergrund">...</div>
<!-- erzeugt: /praesentation/folie/einleitung -->
```

### Mit replaceState (kein Verlauf, aber URL aktualisiert)

```js
const swiper = new Swiper('.swiper', {
  modules: [History],
  history: {
    key: 'tab',
    replaceState: true,  // Kein Verlaufseintrag
    keepQuery: true,     // ?utm_source=... bleibt erhalten
  },
});
```

## Unterschied zu Hash Navigation

| Feature | History-Modul | Hash Navigation-Modul |
|---------|---------------|----------------------|
| URL-Format | `/slides/slide-name` | `#slide-name` |
| Browser-History | `pushState` / `replaceState` | Hash-Änderung |
| Server-Konfiguration | Benötigt Rewrite-Regeln | Keine Serveränderung |
| SEO | Besser (echte URLs) | Eingeschränkt |
| Attribut auf Slide | `data-history` | `data-hash` |

---
Quelle: https://swiperjs.com/swiper-api#history
