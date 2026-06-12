# Swiper Controller-Modul — Vollständige Referenz

## Konzept

Das Controller-Modul synchronisiert zwei oder mehr Swiper-Instanzen miteinander. Wenn einer navigiert wird, folgt der andere. Supports unidirektionale und bidirektionale Steuerung.

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Controller } from 'swiper/modules';

const swiper1 = new Swiper('.swiper-1', {
  modules: [Controller],
});

const swiper2 = new Swiper('.swiper-2', {
  modules: [Controller],
  controller: {
    control: swiper1,
    inverse: false,
    by: 'slide',
  },
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `control` | `Swiper \| Swiper[] \| null` | `null` | Gesteuerte Swiper-Instanz(en) |
| `inverse` | `boolean` | `false` | Gegenrichtung: wenn `true`, steuert vorwärts → rückwärts im anderen |
| `by` | `'slide' \| 'container'` | `'slide'` | Sync per Slide-Index (`'slide'`) oder per Translate-Progress (`'container'`) |

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.controller.control` | `Swiper \| Swiper[]` | Referenz auf gesteuerte Instanz(en) — kann nachträglich gesetzt werden |

## Methoden

| Methode | Signatur | Beschreibung |
|---------|---------|--------------|
| `swiper.controller.setTranslate(translate, byController)` | `(translate: number, byController: Swiper) => void` | Translate-Wert synchronisieren |
| `swiper.controller.setTransition(transition, byController)` | `(transition: number, byController: Swiper) => void` | Transition-Dauer synchronisieren |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `controllerUpdate` | `(swiper)` | Controller-Synchronisierung wurde aktualisiert |

## Bidirektionale Synchronisierung

```js
import Swiper from 'swiper';
import { Controller } from 'swiper/modules';

const swiperA = new Swiper('.swiper-a', {
  modules: [Controller],
  slidesPerView: 1,
});

const swiperB = new Swiper('.swiper-b', {
  modules: [Controller],
  slidesPerView: 1,
});

// Nach Erstellung bidirektional verbinden
swiperA.controller.control = swiperB;
swiperB.controller.control = swiperA;
```

## Mehrere gesteuerte Swipers

```js
const master = new Swiper('.master', {
  modules: [Controller],
});

const slave1 = new Swiper('.slave-1', { modules: [Controller] });
const slave2 = new Swiper('.slave-2', { modules: [Controller] });

// Master steuert beide Slaves
master.controller.control = [slave1, slave2];
```

## Inverse-Steuerung

```js
// Galerie vorwärts → Thumbs rückwärts scrollen
const gallery = new Swiper('.gallery', {
  modules: [Controller],
  controller: {
    control: thumbs,
    inverse: true,
  },
});
```

## Vollständiges Beispiel (Linked Sliders)

```js
import Swiper from 'swiper';
import { Controller, Pagination } from 'swiper/modules';

const textSwiper = new Swiper('.text-swiper', {
  modules: [Controller, Pagination],
  slidesPerView: 1,
  spaceBetween: 0,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  on: {
    controllerUpdate: (swiper) => {
      console.log('Sync aktualisiert');
    },
  },
});

const imageSwiper = new Swiper('.image-swiper', {
  modules: [Controller],
  slidesPerView: 1,
  effect: 'fade',
  speed: 800,
});

// Bidirektional verbinden
textSwiper.controller.control = imageSwiper;
imageSwiper.controller.control = textSwiper;
```

---
Quelle: https://swiperjs.com/swiper-api#controller
