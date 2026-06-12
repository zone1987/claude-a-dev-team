# Swiper Virtual Slides-Modul — Vollständige Referenz

## Konzept

Virtual Slides hält nur die für die Anzeige erforderlichen Slides im DOM. Bei hunderten oder tausenden Slides drastisch bessere Performance gegenüber vollständigem DOM-Rendering.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Virtual } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Virtual],
  virtual: {
    slides: ['Slide 1', 'Slide 2', 'Slide 3', /* ... */],
  },
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `enabled` | `boolean` | `false` | Virtual Slides aktivieren |
| `slides` | `array` | `[]` | Datenquelle — Array aus beliebigen Werten (String, Objekt, etc.) |
| `cache` | `boolean` | `true` | Gerenderte Slide-HTML-Elemente im Cache halten |
| `addSlidesBefore` | `number` | `0` | Zusätzliche Slides vor dem aktiven vorrendern |
| `addSlidesAfter` | `number` | `0` | Zusätzliche Slides nach dem aktiven vorrendern |
| `renderSlide` | `function(slide, index)` | `null` | Eigene Render-Funktion für einzelne Slides; muss HTML-String zurückgeben |
| `renderExternal` | `function(data)` | `null` | Rendering an externe Bibliothek (React/Vue) delegieren |
| `renderExternalUpdate` | `function(data)` | `null` | Callback nach Update bei `renderExternal` |

## renderSlide-Funktion

```js
virtual: {
  slides: myDataArray,
  renderSlide: (slide, index) => {
    // slide = Eintrag aus slides-Array
    // index = Position im Array
    return `
      <div class="swiper-slide" data-index="${index}">
        <img src="${slide.image}" alt="${slide.title}" />
        <h3>${slide.title}</h3>
      </div>
    `;
  },
}
```

## renderExternal für React

```jsx
// React-Integration mit renderExternal
const [virtualData, setVirtualData] = useState({ slides: [], offset: 0 });

const swiper = new Swiper('.swiper', {
  modules: [Virtual],
  virtual: {
    slides: mySlides,
    renderExternal: (data) => {
      setVirtualData(data);
    },
  },
});

// JSX
<div className="swiper-wrapper" style={{ paddingLeft: virtualData.offset + 'px' }}>
  {virtualData.slides.map((slide, index) => (
    <div className="swiper-slide" key={index}>{slide}</div>
  ))}
</div>
```

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.virtual.slides` | `array` | Aktuell im DOM gerenderte Slides |
| `swiper.virtual.cache` | `object` | Gecachte Slide-Elemente (key = Index) |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.virtual.update(force?)` | Virtual Slides aktualisieren; `force: true` = Cache leeren |
| `swiper.virtual.appendSlide(slides)` | Slides ans Ende anhängen |
| `swiper.virtual.prependSlide(slides)` | Slides am Anfang einfügen |

## Einschränkungen

- **Nicht kompatibel** mit dem Grid-Modul
- **Nicht kompatibel** mit `slidesPerView: 'auto'`
- Für Loop-Modus müssen genügend Slides vorhanden sein

## Vollständiges Beispiel mit 1000 Slides

```js
import Swiper from 'swiper';
import { Virtual, Navigation, Pagination } from 'swiper/modules';

const slides = Array.from({ length: 1000 }, (_, i) => ({
  id: i,
  title: `Slide ${i + 1}`,
  image: `https://picsum.photos/800/400?random=${i}`,
}));

const swiper = new Swiper('.swiper', {
  modules: [Virtual, Navigation, Pagination],
  slidesPerView: 1,
  virtual: {
    slides,
    cache: true,
    addSlidesBefore: 2,
    addSlidesAfter: 2,
    renderSlide: (slide, index) => `
      <div class="swiper-slide">
        <img src="${slide.image}" loading="lazy" />
        <p>${slide.title}</p>
      </div>
    `,
  },
  navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
  pagination: { el: '.swiper-pagination', type: 'fraction' },
});
```

---
Quelle: https://swiperjs.com/swiper-api#virtual-slides
