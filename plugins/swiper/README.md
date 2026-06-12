# swiper

> Vollständige Dokumentation des modernen Touch-Sliders Swiper (v11/v12) — komplette API + alle Module.

`swiper` ist die vollständige Wissens-Bibliothek zum modernen, abhängigkeitsfreien Touch-Slider/Carousel **Swiper** (v11/v12), destilliert aus swiperjs.com. Sie deckt die komplette API und alle Module bis ins kleinste Detail ab.

**Core-API:** Einbindung (npm/CDN, CSS-Imports, HTML-Struktur, Modul-Registrierung), die **vollständige Parameter-Referenz** (236 Parameter mit Typ/Default), **alle Methoden** (68), **alle Events** (74) und **Properties** (45).

**Alle Module** (je eigenes Skill mit Parametern/Methoden/Events/CSS): Navigation, Pagination, Scrollbar, Autoplay, **Effekte** (fade/cube/coverflow/flip/cards/creative), Virtual, Keyboard, Mousewheel, Zoom, FreeMode, Grid, Thumbs, Controller, A11y, History, HashNavigation, Parallax, Manipulation, Lazy.

**Einbindungsvarianten:** die **Swiper-Element**-Web-Component (`<swiper-container>`) sowie **React/Vue** (eigene Komponenten) und **Angular/Svelte/Solid** (über das Element, da seit v9 ohne eigene Adapter). Dazu **Migration** (v9/v10/v11), eigene **Plugins** (Plugin-API) und der **Swiper-MCP**-Server.

Spezialist: **`swiper-expert`**; Scaffolder **`/swiper-init`** (Variante + HTML + CSS-Imports + Modul-Registrierung + Init). **Wann nutzen:** für jeden Slider/Carousel im Frontend — auch in Shopware-Storefront-/Admin- oder Contao-Projekten.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen aus swiperjs.com destilliert und eingebettet; Skills laden Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install swiper@claude-a-dev-team
```

## Skills — Core-API (5)

| Skill | Beschreibung |
|---|---|
| `swiper-getting-started` | Swiper installieren und einbinden: npm, CDN, CSS-Imports, HTML-Struktur, erste Instanz, Module registrieren, Core vs |
| `swiper-events` | Alle Swiper-Events: init, slideChange, transitionStart/End, touchStart/Move/End, reachBeginning, reachEnd, progress, autoplay, pagination, navigation, zoom und mehr |
| `swiper-methods` | Alle Swiper-Instanz-Methoden: slideNext, slidePrev, slideTo, update, destroy, on/off/once, Navigation-, Pagination-, Scrollbar-, Autoplay-, Zoom-, Manipulation-Methoden |
| `swiper-parameters` | Erschöpfende Referenz aller Swiper-Konfigurationsparameter: Core, Navigation, Pagination, Scrollbar, Autoplay, FreeMode, Grid, Effekte, Thumbs, Zoom, Keyboard, Mousewheel, Virtual |
| `swiper-properties` | Alle Swiper-Instanz-Properties: activeIndex, realIndex, previousIndex, slides, translate, progress, isBeginning, isEnd, params, el, wrapperEl, snapGrid, slidesGrid und Modul-Properties |

## Skills — Module (19)

| Skill | Beschreibung |
|---|---|
| `swiper-a11y` | Vollständige Referenz des Swiper A11y (Accessibility)-Moduls: ARIA-Attribute, prevSlideMessage, nextSlideMessage, firstSlideMessage, lastSlideMessage, paginationBulletMessage, notificationClass — Screen-Reader-Unterstützung |
| `swiper-autoplay` | Vollständige Referenz des Swiper Autoplay-Moduls: delay, disableOnInteraction, pauseOnMouseEnter, reverseDirection, stopOnLastSlide, waitForTransition, Methoden start/stop/pause/resume, Events autoplayTimeLeft |
| `swiper-controller` | Vollständige Referenz des Swiper Controller-Moduls: control, inverse, by (slide/progress) — mehrere Swiper-Instanzen synchronisieren, bidirektionale Steuerung |
| `swiper-effects` | Vollständige Referenz aller Swiper-Übergangseffekte: fade, cube, coverflow, flip, cards, creative — je mit vollständigem Parameter-Objekt (fadeEffect, cubeEffect, coverflowEffect, flipEffect, cardsEffect, creativeEffect inkl |
| `swiper-free-mode` | Vollständige Referenz des Swiper Free Mode-Moduls: momentum, momentumRatio, momentumVelocityRatio, momentumBounce, minimumVelocity, sticky — freies Scrollen ohne Snap-Punkte, mit Momentum-Physik |
| `swiper-grid` | Vollständige Referenz des Swiper Grid-Moduls: rows, fill (column/row) — mehrzeilige Slide-Layouts mit Swiper Grid |
| `swiper-hash-navigation` | Vollständige Referenz des Swiper Hash Navigation-Moduls: enabled, replaceState, watchState — URL-Hash-basierte Slide-Navigation mit data-hash-Attribut |
| `swiper-history` | Vollständige Referenz des Swiper History-Moduls: key, replaceState, keepQuery, root — Browser-History-Integration mit data-history-Attribut je Slide |
| `swiper-keyboard` | Vollständige Referenz des Swiper Keyboard-Moduls: enabled, onlyInViewport, pageUpDown, Methoden enable/disable, Event keyPress — Tastaturnavigation für Swiper |
| `swiper-lazy` | Vollständige Referenz des Swiper Lazy Loading: loading="lazy" native Browser-Integration, lazyPreloadPrevNext, lazyPreloaderClass, swiper-lazy-preloader HTML-Element |
| `swiper-manipulation` | Vollständige Referenz des Swiper Manipulation-Moduls: appendSlide, prependSlide, addSlide(index), removeSlide, removeAllSlides — dynamisches Hinzufügen/Entfernen von Slides |
| `swiper-mousewheel` | Vollständige Referenz des Swiper Mousewheel-Moduls: enabled, invert, forceToAxis, releaseOnEdges, sensitivity, thresholdDelta, thresholdTime, eventsTarget, noMousewheelClass, Methoden enable/disable, Event scroll |
| `swiper-navigation` | Vollständige Referenz des Swiper Navigation-Moduls: nextEl/prevEl, disabledClass, hiddenClass, lockClass, addIcons, hideOnClick, CSS-Variablen, Events, Methoden |
| `swiper-pagination` | Vollständige Referenz des Swiper Pagination-Moduls: bullets/fraction/progressbar/custom, clickable, dynamicBullets, renderBullet/Fraction/Custom/Progressbar, CSS-Variablen, Events |
| `swiper-parallax` | Vollständige Referenz des Swiper Parallax-Moduls: data-swiper-parallax, data-swiper-parallax-x/y, data-swiper-parallax-scale, data-swiper-parallax-opacity, data-swiper-parallax-duration — Parallax-Effekte für Hintergründe und Slide-Inhalte |
| `swiper-scrollbar` | Vollständige Referenz des Swiper Scrollbar-Moduls: el, draggable, dragSize, hide, snapOnRelease, CSS-Variablen, Events (scrollbarDragStart/Move/End), Methoden |
| `swiper-thumbs` | Vollständige Referenz des Swiper Thumbs-Moduls: swiper-Instanz verknüpfen, multipleActiveThumbs, autoScrollOffset, slideThumbActiveClass, thumbsContainerClass, Methoden init/update — Thumbnail-Galerie-Navigation |
| `swiper-virtual` | Vollständige Referenz des Swiper Virtual Slides-Moduls: slides-Array, renderSlide, renderExternal, cache, addSlidesBefore/After — performantes DOM-Rendering großer Slide-Mengen |
| `swiper-zoom` | Vollständige Referenz des Swiper Zoom-Moduls: maxRatio, minRatio, toggle, limitToOriginalSize, panOnMouseMove, containerClass, Methoden zoom.in/out/toggle, Event zoomChange, data-swiper-zoom Attribut per Slide |

## Skills — Integration & Migration (9)

| Skill | Beschreibung |
|---|---|
| `swiper-angular` | Swiper in Angular — ab v9 via Swiper Element (`<swiper-container>`/`<swiper-slide>`), CUSTOM_ELEMENTS_SCHEMA, Property-Binding, Events, ViewChild-Zugriff |
| `swiper-element` | Swiper Web Component — `<swiper-container>`/`<swiper-slide>` Registrierung, Parameter als Attribute (kebab-case), JSON-Attribute, Property-Binding, Slots, Events (Lowercase), Methoden, Shadow-DOM-CSS |
| `swiper-mcp` | Swiper MCP-Server — HTTP-Endpunkt für programmatischen Zugriff auf Swiper-Dokumentation, 8 Tools (search-api, get-option, get-method, get-event, get-module-options, list-demos, get-demo, get-premium-recommendations), Setup für Claude Code,  |
| `swiper-migration` | Swiper Breaking Changes für v9, v10 und v11 — CSS-Imports, Modul-Imports, Lazy Loading, Element-Struktur, entfernte Parameter, Framework-Adapter-Entfernung, Touch-Events, Dom7 |
| `swiper-plugins` | Swiper Plugins & Community-Module — Premium-Plugins (UI Initiative, Swiper Studio), Plugin-API-Struktur zum Schreiben eigener Swiper-Module |
| `swiper-react` | Swiper React-Komponenten — `<Swiper>`/`<SwiperSlide>`, alle Props (= API-Parameter), modules-Prop, Events als `onXxx`-Props, `useSwiper`/`useSwiperSlide`-Hooks, Slots, Virtual Slides, Controller |
| `swiper-solid` | Swiper in SolidJS — ab v9 via Swiper Element (`<swiper-container>`/`<swiper-slide>`), `register()`, Property-Binding, Events |
| `swiper-svelte` | Swiper in Svelte/SvelteKit — ab v9 via Swiper Element (`<swiper-container>`/`<swiper-slide>`), `register()`, Property-Binding mit `bind:this`, Events mit `on:swiper*` |
| `swiper-vue` | Swiper Vue-Komponenten — `<Swiper>`/`<SwiperSlide>`, Props, Events, `v-slot`-Render-Props, `useSwiper`/`useSwiperSlide`-Composables, Modules, Virtual Slides, Controller, Thumbs |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `swiper-expert` | Spezialist für Swiper (moderner Touch-Slider/Carousel, v11/v12) |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/swiper-init` | Scaffold einer Swiper-Einbindung — Variante (Core/Element/React/Vue), HTML-Struktur, CSS-Imports, Modul-Registrierung (Navigation/Pagination/Autoplay/Effekte/…) und Init-Code mit den gewünschten Parametern |
