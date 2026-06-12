# Swiper Manipulation-Modul — Vollständige Referenz

## Konzept

Das Manipulation-Modul stellt Methoden bereit um Slides dynamisch im DOM hinzuzufügen, einzufügen und zu entfernen. Nach jeder Manipulation aktualisiert Swiper automatisch seinen internen State.

**Wichtig:** Dieses Modul ist für Swiper Core (Vanilla JS) gedacht. In React/Vue sollte der Slides-State über den Framework-State gesteuert werden.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Manipulation } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Manipulation],
  slidesPerView: 3,
  spaceBetween: 10,
});
```

## Methoden

### appendSlide(slides)

Fügt einen oder mehrere Slides ans Ende an.

**Signatur:** `appendSlide(slides: HTMLElement | string | (HTMLElement | string)[]) => void`

```js
// Einzelner Slide (HTML-String)
swiper.appendSlide('<div class="swiper-slide">Neuer Slide am Ende</div>');

// Einzelner Slide (HTMLElement)
const slideEl = document.createElement('div');
slideEl.className = 'swiper-slide';
slideEl.textContent = 'Dynamischer Slide';
swiper.appendSlide(slideEl);

// Mehrere Slides auf einmal
swiper.appendSlide([
  '<div class="swiper-slide">Slide A</div>',
  '<div class="swiper-slide">Slide B</div>',
  '<div class="swiper-slide">Slide C</div>',
]);
```

### prependSlide(slides)

Fügt einen oder mehrere Slides am Anfang ein.

**Signatur:** `prependSlide(slides: HTMLElement | string | (HTMLElement | string)[]) => void`

```js
// Einzelner Slide
swiper.prependSlide('<div class="swiper-slide">Erster Slide</div>');

// Mehrere Slides
swiper.prependSlide([
  '<div class="swiper-slide">Neu-1</div>',
  '<div class="swiper-slide">Neu-2</div>',
]);
```

### addSlide(index, slides)

Fügt Slides an einer bestimmten Position ein.

**Signatur:** `addSlide(index: number, slides: HTMLElement | string | (HTMLElement | string)[]) => void`

```js
// An Position 2 einfügen (0-basiert)
swiper.addSlide(2, '<div class="swiper-slide">Slide an Position 2</div>');

// Mehrere Slides ab Position 1 einfügen
swiper.addSlide(1, [
  '<div class="swiper-slide">Neu an Position 1</div>',
  '<div class="swiper-slide">Neu an Position 2</div>',
]);
```

### removeSlide(slideIndex)

Entfernt einen oder mehrere Slides per Index.

**Signatur:** `removeSlide(slideIndex: number | number[]) => void`

```js
// Ersten Slide entfernen
swiper.removeSlide(0);

// Mehrere Slides entfernen
swiper.removeSlide([0, 2, 4]);  // Slides an Index 0, 2 und 4
```

### removeAllSlides()

Entfernt alle Slides.

**Signatur:** `removeAllSlides() => void`

```js
swiper.removeAllSlides();
```

## Vollständiges Beispiel (dynamische Galerie)

```js
import Swiper from 'swiper';
import { Manipulation, Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Manipulation, Navigation, Pagination],
  slidesPerView: 1,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    type: 'fraction',
  },
});

// Slide laden und anhängen
async function loadMoreSlides(page) {
  const response = await fetch(`/api/slides?page=${page}`);
  const slides = await response.json();

  const html = slides.map(slide =>
    `<div class="swiper-slide">
      <img src="${slide.image}" alt="${slide.title}" />
      <h3>${slide.title}</h3>
    </div>`
  );

  swiper.appendSlide(html);
}

// Schaltfläche: Slide hinzufügen
document.querySelector('#add-slide').addEventListener('click', () => {
  const index = swiper.slides.length;
  swiper.appendSlide(
    `<div class="swiper-slide">Slide ${index + 1}</div>`
  );
  swiper.slideTo(index); // Zum neuen Slide navigieren
});

// Schaltfläche: Aktuellen Slide entfernen
document.querySelector('#remove-current').addEventListener('click', () => {
  swiper.removeSlide(swiper.activeIndex);
});

// Alle leeren und neu laden
document.querySelector('#reset').addEventListener('click', () => {
  swiper.removeAllSlides();
  loadMoreSlides(1);
});
```

## Hinweise zur Framework-Integration

In React/Vue/Angular werden Slides nicht per Manipulation-Modul verwaltet, sondern durch reaktive State-Updates:

```jsx
// React: Slides über State verwalten
const [slides, setSlides] = useState(['Slide 1', 'Slide 2']);

const addSlide = () => {
  setSlides(prev => [...prev, `Slide ${prev.length + 1}`]);
};

// Swiper aktualisiert sich automatisch wenn sich die Slides ändern
```

---
Quelle: https://swiperjs.com/swiper-api#manipulation
