# Swiper Autoplay-Modul — Vollständige Referenz

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Autoplay } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [Autoplay],
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
  },
});
```

## Parameter

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `delay` | `number` | `3000` | Pause zwischen Slide-Transitionen in Millisekunden |
| `disableOnInteraction` | `boolean` | `true` | `false` = Autoplay nach Benutzerinteraktion neu starten (nicht stoppen) |
| `pauseOnMouseEnter` | `boolean` | `false` | Autoplay pausieren wenn Zeiger den Container betritt |
| `reverseDirection` | `boolean` | `false` | Autoplay in umgekehrter Richtung abspielen |
| `stopOnLastSlide` | `boolean` | `false` | Autoplay am letzten Slide stoppen (kein Effekt im Loop-Modus) |
| `waitForTransition` | `boolean` | `true` | Warten bis die Wrapper-Transition abgeschlossen ist |

## Per-Slide-Override

Einzelner Slide kann eigenes Delay erhalten:

```html
<div class="swiper-slide" data-swiper-autoplay="5000">
  Dieser Slide bleibt 5 Sekunden stehen
</div>
```

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.autoplay.running` | `boolean` | Autoplay läuft gerade |
| `swiper.autoplay.paused` | `boolean` | Autoplay ist pausiert |
| `swiper.autoplay.timeLeft` | `number` | Verbleibende Zeit in ms bis zur nächsten Transition |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.autoplay.start()` | Autoplay starten |
| `swiper.autoplay.stop()` | Autoplay vollständig stoppen |
| `swiper.autoplay.pause()` | Autoplay pausieren (kann fortgesetzt werden) |
| `swiper.autoplay.resume()` | Pausiertes Autoplay fortsetzen |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `autoplay` | `(swiper)` | Wird ausgelöst wenn Autoplay einen Slide-Wechsel triggert |
| `autoplayStart` | `(swiper)` | Autoplay wurde gestartet |
| `autoplayStop` | `(swiper)` | Autoplay wurde gestoppt |
| `autoplayPause` | `(swiper)` | Autoplay wurde pausiert |
| `autoplayResume` | `(swiper)` | Autoplay wurde fortgesetzt |
| `autoplayTimeLeft` | `(swiper, timeLeft, percentage)` | Kontinuierliches Event mit verbleibender Zeit und Prozent (0..1) |

### autoplayTimeLeft für Fortschrittsanzeige

```js
swiper.on('autoplayTimeLeft', (swiper, timeLeft, percentage) => {
  // timeLeft: ms bis zur nächsten Transition
  // percentage: 0 = Anfang, 1 = Ende des Delays
  progressBar.style.setProperty('--progress', 1 - percentage);
});
```

## Vollständiges Beispiel

```js
const swiper = new Swiper('.swiper', {
  modules: [Autoplay],
  loop: true,
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
    reverseDirection: false,
    waitForTransition: true,
  },
  on: {
    autoplayStart: () => console.log('gestartet'),
    autoplayStop: () => console.log('gestoppt'),
    autoplayTimeLeft: (s, time, progress) => {
      document.querySelector('.timer').textContent =
        Math.ceil(time / 1000) + 's';
    },
  },
});

// Externe Steuerung
document.querySelector('#pause-btn').addEventListener('click', () => {
  swiper.autoplay.pause();
});
document.querySelector('#play-btn').addEventListener('click', () => {
  swiper.autoplay.resume();
});
```

---
Quelle: https://swiperjs.com/swiper-api#autoplay
