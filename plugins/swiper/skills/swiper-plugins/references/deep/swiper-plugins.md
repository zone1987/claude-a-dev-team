# Swiper Plugins & Custom Module — Vollständige Referenz

---

## Premium Plugins

Swiper bietet Premium-Plugins über zwei Anbieter an:

### UI Initiative (uiinitiative.com)

Premium Swiper-Plugins als fertige, hochwertige Slider-Experiences:

| Plugin-Name | Beschreibung |
|---|---|
| **Super Flow** | Fortgeschrittener Flow-Slider |
| **Expo Slider** | Ausstellungs-/Galerie-Slider |
| **Cards Stack Slider** | Gestapelte Karten-Animation |
| **Material You Slider** | Material Design 3 Slider |
| **Tinder Slider** | Swipe-left/right Interaction |
| **Shaders Slider** | WebGL-Shader-Übergänge |
| **Slicer Slider** | Slice/Split-Transitions |
| **Shutters Slider** | Jalousie-artige Transitions |
| **Stories Slider** | Social-Media-Stories-Format |
| **Spring Slider** | Federbasierte Physik-Animationen |
| **Panorama Slider** | 360°-Panorama-Darstellung |
| **Fashion Slider** | Mode/Editorial-Slider |
| **Carousel Slider** | Klassisches Karussell (erweitert) |
| **Triple Slider** | Drei-Slide-Darstellung |
| **Travel Slider** | Reise/Magazin-Slider |
| **Expanding Collection** | Expanding Cards Collection |
| **Posters Slider** | Poster/Fullscreen-Format |
| **Paper Onboarding** | Onboarding-Flow mit Papier-Effekt |

### Swiper Studio (studio.swiperjs.com)

| Plugin-Name | Beschreibung |
|---|---|
| **Swiper 3D Slicer** | 3D-Schnitt-Transition |
| **Swiper 3D Pagination** | 3D-Pagination-Elemente |

---

## Eigene Swiper-Module / Plugins schreiben

Swiper unterstützt eine Plugin-API für eigene Module. Module erweitern die Swiper-Funktionalität durch Hooks in den Swiper-Lifecycle.

### Grundstruktur eines Swiper-Moduls

```javascript
const MyPlugin = {
  // Name des Plugins (wird als Swiper-Property verfügbar)
  name: 'myPlugin',

  // Params: Standard-Parameter des Plugins
  params: {
    myPlugin: {
      enabled: true,
      speed: 300,
      customOption: 'default',
    },
  },

  // create: wird aufgerufen wenn eine neue Swiper-Instanz erstellt wird
  create(swiper) {
    // Hier Swiper-Instanz erweitern
    swiper.myPlugin = {
      doSomething() {
        console.log('Plugin action on', swiper.activeIndex);
      },
      state: 'idle',
    };
  },

  // on: Lifecycle-Hook-Registrierungen
  on: {
    // Beim Initialisieren
    init(swiper) {
      console.log('MyPlugin: Swiper initialized');
      // Zugriff auf Plugin-Params:
      const { enabled, speed } = swiper.params.myPlugin;
      if (!enabled) return;

      // Setup-Code hier
    },

    // Nach dem Löschen
    destroy(swiper) {
      console.log('MyPlugin: Swiper destroyed');
      // Cleanup hier
    },

    // Bei jedem Slide-Wechsel
    slideChange(swiper) {
      console.log('MyPlugin: Slide changed to', swiper.activeIndex);
    },

    // Bei Fortschritt (throttled)
    progress(swiper, progress) {
      // progress: 0 bis 1
    },

    // Bei Transition-Start
    transitionStart(swiper) {},

    // Bei Transition-Ende
    transitionEnd(swiper) {},

    // Wenn Slides neu gesetzt werden
    slidesUpdated(swiper) {},

    // Bei Update
    update(swiper) {},

    // Bei Resize
    resize(swiper) {},

    // Vor dem Zerstören
    beforeDestroy(swiper) {},

    // Bei Touch/Pointer-Down
    touchStart(swiper, event) {},

    // Bei Touch/Pointer-Move
    touchMove(swiper, event) {},

    // Bei Touch/Pointer-End
    touchEnd(swiper, event) {},

    // Beim Click
    click(swiper, event) {},
  },
};
```

### Plugin mit Custom CSS (über injectStyles)

```javascript
const MyPlugin = {
  name: 'myPlugin',
  params: {
    myPlugin: { enabled: true },
  },
  create(swiper) {
    swiper.myPlugin = {};
  },
  on: {
    init(swiper) {
      if (swiper.isElement) {
        // Für Swiper Element: Styles in Shadow DOM injizieren
        // (wird via injectStyles-Param des Elements übergeben)
      } else {
        // Für Swiper Core: Styles ins Document injizieren
        const style = document.createElement('style');
        style.textContent = `
          .swiper-my-plugin-active {
            opacity: 1;
          }
        `;
        document.head.appendChild(style);
        swiper.myPlugin.style = style;
      }
    },
    beforeDestroy(swiper) {
      swiper.myPlugin.style?.remove();
    },
  },
};
```

### Plugin registrieren und verwenden

```javascript
import Swiper from 'swiper';
import { Navigation } from 'swiper/modules';

// Plugin einbinden
const swiper = new Swiper('.swiper', {
  modules: [Navigation, MyPlugin],
  navigation: true,
  myPlugin: {
    enabled: true,
    customOption: 'value',
  },
});

// Plugin-Methoden nutzen
swiper.myPlugin.doSomething();
```

### Plugin für Swiper Element

```javascript
import { register } from 'swiper/element/bundle';

register();

// Custom Params für Element-Attribute registrieren
window.SwiperElementRegisterParams(['myPlugin', 'myPluginEnabled']);

const swiperEl = document.querySelector('swiper-container');
Object.assign(swiperEl, {
  modules: [MyPlugin],
  myPlugin: {
    enabled: true,
  },
});
swiperEl.initialize();
```

---

## Alle Swiper Lifecycle-Events (für Plugin-Hooks)

| Event | Wann |
|---|---|
| `beforeInit` | Vor der Initialisierung |
| `init` | Nach der Initialisierung |
| `afterInit` | Nach `init` |
| `beforeDestroy` | Vor dem Löschen |
| `destroy` | Beim Löschen |
| `slideChange` | Wenn aktiver Slide wechselt |
| `slideChangeTransitionStart` | Start der Slide-Transition |
| `slideChangeTransitionEnd` | Ende der Slide-Transition |
| `slideNextTransitionStart` | Start bei Vorwärts-Navigation |
| `slideNextTransitionEnd` | Ende bei Vorwärts-Navigation |
| `slidePrevTransitionStart` | Start bei Rückwärts-Navigation |
| `slidePrevTransitionEnd` | Ende bei Rückwärts-Navigation |
| `transitionStart` | Transition-Start (allgemein) |
| `transitionEnd` | Transition-Ende (allgemein) |
| `touchStart` | Pointer/Touch gedrückt |
| `touchMove` | Pointer/Touch bewegt |
| `touchEnd` | Pointer/Touch losgelassen |
| `click` | Click auf Slide |
| `tap` | Tap auf Slide |
| `doubleTap` | Doppel-Tap |
| `progress` | Fortschritts-Update |
| `reachBeginning` | Erster Slide erreicht |
| `reachEnd` | Letzter Slide erreicht |
| `fromEdge` | Von Anfang/Ende weggewechselt |
| `setTranslate` | Translate gesetzt |
| `setTransition` | Transition gesetzt |
| `resize` | Resize-Event |
| `observerUpdate` | DOM-Observer meldet Änderung |
| `update` | Nach `swiper.update()` |
| `lock` | Swiper gelockt |
| `unlock` | Swiper entsperrt |
| `slideResetTransitionStart` | Reset-Transition Start |
| `slideResetTransitionEnd` | Reset-Transition Ende |
| `slidesUpdated` | Slides DOM aktualisiert |
| `snapGridLengthChange` | Snap-Grid-Änderung |
| `slidesGridLengthChange` | Slides-Grid-Änderung |
| `snapIndexChange` | Snap-Index geändert |
| `activeIndexChange` | Aktiver Index geändert |
| `realIndexChange` | Realer Index geändert |

---

## Plugin mit externem State-Management

```javascript
const StatePlugin = {
  name: 'statePlugin',
  params: {
    statePlugin: {
      onStateChange: null, // Callback-Funktion
    },
  },
  create(swiper) {
    swiper.statePlugin = {
      _state: {
        activeIndex: 0,
        isBeginning: true,
        isEnd: false,
      },
      getState() {
        return { ...this._state };
      },
    };
  },
  on: {
    init(swiper) {
      swiper.statePlugin._state = {
        activeIndex: swiper.activeIndex,
        isBeginning: swiper.isBeginning,
        isEnd: swiper.isEnd,
      };
    },
    slideChange(swiper) {
      swiper.statePlugin._state = {
        activeIndex: swiper.activeIndex,
        isBeginning: swiper.isBeginning,
        isEnd: swiper.isEnd,
      };

      const callback = swiper.params.statePlugin?.onStateChange;
      if (typeof callback === 'function') {
        callback(swiper.statePlugin._state);
      }
    },
  },
};

// Verwendung:
const swiper = new Swiper('.swiper', {
  modules: [StatePlugin],
  statePlugin: {
    onStateChange: (state) => {
      console.log('State:', state);
      // React, Vue, etc. State updaten
    },
  },
});
```

---

## Swiper-Instanz-Eigenschaften im Plugin-Kontext

Im Plugin `create(swiper)` und `on`-Hooks verfügbare Swiper-Properties:

```javascript
create(swiper) {
  swiper.el           // Container DOM-Element
  swiper.wrapperEl    // Wrapper DOM-Element
  swiper.slides       // Array aller Slide-Elemente
  swiper.activeIndex  // Aktueller Slide-Index
  swiper.realIndex    // Realer Index (bei Loop)
  swiper.isBeginning  // Am Anfang?
  swiper.isEnd        // Am Ende?
  swiper.params       // Alle Swiper-Parameter (inkl. Plugin-Params)
  swiper.isElement    // Ist Swiper Element (Web Component)?
  swiper.translate    // Aktueller Translate-Wert
  swiper.progress     // Fortschritt (0-1)

  // Methoden:
  swiper.slideNext()
  swiper.slidePrev()
  swiper.slideTo(index)
  swiper.update()
  swiper.emit('eventName', ...args)  // Eigene Events auslösen
  swiper.on('eventName', handler)    // Event lauschen
  swiper.off('eventName', handler)   // Event entfernen
}
```

---

*Quellen:*
- *https://swiperjs.com/plugins*
- *https://swiperjs.com/swiper-api*
- *Swiper v12.2.0*
