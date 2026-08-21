# Swiper Plugins & Custom Module — Complete reference

---

## Contents

- [Premium Plugins](#premium-plugins)
- [Writing your own Swiper modules / plugins](#writing-your-own-swiper-modules--plugins)
- [All Swiper lifecycle events (for plugin hooks)](#all-swiper-lifecycle-events-for-plugin-hooks)
- [Plugin with external state management](#plugin-with-external-state-management)
- [Swiper instance properties in the plugin context](#swiper-instance-properties-in-the-plugin-context)

## Premium Plugins

Swiper offers premium plugins through two providers:

### UI Initiative (uiinitiative.com)

Premium Swiper plugins as ready-made, high-quality slider experiences:

| Plugin name | Description |
|---|---|
| **Super Flow** | Advanced flow slider |
| **Expo Slider** | Exhibition/gallery slider |
| **Cards Stack Slider** | Stacked cards animation |
| **Material You Slider** | Material Design 3 slider |
| **Tinder Slider** | Swipe-left/right interaction |
| **Shaders Slider** | WebGL shader transitions |
| **Slicer Slider** | Slice/split transitions |
| **Shutters Slider** | Blind-style transitions |
| **Stories Slider** | Social media stories format |
| **Spring Slider** | Spring-based physics animations |
| **Panorama Slider** | 360° panorama presentation |
| **Fashion Slider** | Fashion/editorial slider |
| **Carousel Slider** | Classic carousel (extended) |
| **Triple Slider** | Three-slide presentation |
| **Travel Slider** | Travel/magazine slider |
| **Expanding Collection** | Expanding cards collection |
| **Posters Slider** | Poster/fullscreen format |
| **Paper Onboarding** | Onboarding flow with a paper effect |

### Swiper Studio (studio.swiperjs.com)

| Plugin name | Description |
|---|---|
| **Swiper 3D Slicer** | 3D slice transition |
| **Swiper 3D Pagination** | 3D pagination elements |

---

## Writing your own Swiper modules / plugins

Swiper supports a plugin API for custom modules. Modules extend Swiper's functionality by hooking into the Swiper lifecycle.

### Basic structure of a Swiper module

```javascript
const MyPlugin = {
  // Name of the plugin (becomes available as a Swiper property)
  name: 'myPlugin',

  // Params: default parameters of the plugin
  params: {
    myPlugin: {
      enabled: true,
      speed: 300,
      customOption: 'default',
    },
  },

  // create: called when a new Swiper instance is created
  create(swiper) {
    // Extend the Swiper instance here
    swiper.myPlugin = {
      doSomething() {
        console.log('Plugin action on', swiper.activeIndex);
      },
      state: 'idle',
    };
  },

  // on: lifecycle hook registrations
  on: {
    // On initialization
    init(swiper) {
      console.log('MyPlugin: Swiper initialized');
      // Access the plugin params:
      const { enabled, speed } = swiper.params.myPlugin;
      if (!enabled) return;

      // Setup code here
    },

    // After destruction
    destroy(swiper) {
      console.log('MyPlugin: Swiper destroyed');
      // Cleanup here
    },

    // On every slide change
    slideChange(swiper) {
      console.log('MyPlugin: Slide changed to', swiper.activeIndex);
    },

    // On progress (throttled)
    progress(swiper, progress) {
      // progress: 0 to 1
    },

    // On transition start
    transitionStart(swiper) {},

    // On transition end
    transitionEnd(swiper) {},

    // When slides are set anew
    slidesUpdated(swiper) {},

    // On update
    update(swiper) {},

    // On resize
    resize(swiper) {},

    // Before destruction
    beforeDestroy(swiper) {},

    // On touch/pointer down
    touchStart(swiper, event) {},

    // On touch/pointer move
    touchMove(swiper, event) {},

    // On touch/pointer end
    touchEnd(swiper, event) {},

    // On click
    click(swiper, event) {},
  },
};
```

### Plugin with custom CSS (via injectStyles)

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
        // For Swiper Element: inject styles into the shadow DOM
        // (passed via the element's injectStyles param)
      } else {
        // For Swiper Core: inject styles into the document
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

### Registering and using the plugin

```javascript
import Swiper from 'swiper';
import { Navigation } from 'swiper/modules';

// Include the plugin
const swiper = new Swiper('.swiper', {
  modules: [Navigation, MyPlugin],
  navigation: true,
  myPlugin: {
    enabled: true,
    customOption: 'value',
  },
});

// Use the plugin methods
swiper.myPlugin.doSomething();
```

### Plugin for Swiper Element

```javascript
import { register } from 'swiper/element/bundle';

register();

// Register custom params for element attributes
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

## All Swiper lifecycle events (for plugin hooks)

| Event | When |
|---|---|
| `beforeInit` | Before initialization |
| `init` | After initialization |
| `afterInit` | After `init` |
| `beforeDestroy` | Before destruction |
| `destroy` | On destruction |
| `slideChange` | When the active slide changes |
| `slideChangeTransitionStart` | Start of the slide transition |
| `slideChangeTransitionEnd` | End of the slide transition |
| `slideNextTransitionStart` | Start on forward navigation |
| `slideNextTransitionEnd` | End on forward navigation |
| `slidePrevTransitionStart` | Start on backward navigation |
| `slidePrevTransitionEnd` | End on backward navigation |
| `transitionStart` | Transition start (general) |
| `transitionEnd` | Transition end (general) |
| `touchStart` | Pointer/touch pressed |
| `touchMove` | Pointer/touch moved |
| `touchEnd` | Pointer/touch released |
| `click` | Click on a slide |
| `tap` | Tap on a slide |
| `doubleTap` | Double tap |
| `progress` | Progress update |
| `reachBeginning` | First slide reached |
| `reachEnd` | Last slide reached |
| `fromEdge` | Moved away from the beginning/end |
| `setTranslate` | Translate was set |
| `setTransition` | Transition was set |
| `resize` | Resize event |
| `observerUpdate` | The DOM observer reports a change |
| `update` | After `swiper.update()` |
| `lock` | Swiper locked |
| `unlock` | Swiper unlocked |
| `slideResetTransitionStart` | Reset transition start |
| `slideResetTransitionEnd` | Reset transition end |
| `slidesUpdated` | Slides DOM updated |
| `snapGridLengthChange` | Snap grid change |
| `slidesGridLengthChange` | Slides grid change |
| `snapIndexChange` | Snap index changed |
| `activeIndexChange` | Active index changed |
| `realIndexChange` | Real index changed |

---

## Plugin with external state management

```javascript
const StatePlugin = {
  name: 'statePlugin',
  params: {
    statePlugin: {
      onStateChange: null, // callback function
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

// Usage:
const swiper = new Swiper('.swiper', {
  modules: [StatePlugin],
  statePlugin: {
    onStateChange: (state) => {
      console.log('State:', state);
      // Update React, Vue, etc. state
    },
  },
});
```

---

## Swiper instance properties in the plugin context

Swiper properties available in the plugin's `create(swiper)` and `on` hooks:

```javascript
create(swiper) {
  swiper.el           // Container DOM element
  swiper.wrapperEl    // Wrapper DOM element
  swiper.slides       // Array of all slide elements
  swiper.activeIndex  // Current slide index
  swiper.realIndex    // Real index (with loop)
  swiper.isBeginning  // At the beginning?
  swiper.isEnd        // At the end?
  swiper.params       // All Swiper parameters (incl. plugin params)
  swiper.isElement    // Is it a Swiper Element (web component)?
  swiper.translate    // Current translate value
  swiper.progress     // Progress (0-1)

  // Methods:
  swiper.slideNext()
  swiper.slidePrev()
  swiper.slideTo(index)
  swiper.update()
  swiper.emit('eventName', ...args)  // Emit your own events
  swiper.on('eventName', handler)    // Listen to an event
  swiper.off('eventName', handler)   // Remove an event
}
```

---

*Sources:*
- *https://swiperjs.com/plugins*
- *https://swiperjs.com/swiper-api*
- *Swiper v12.2.0*
