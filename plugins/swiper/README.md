# swiper

> Complete documentation of the modern touch slider Swiper (v11/v12) — the full API plus every module.

`swiper` is the complete knowledge library for the modern, dependency-free touch slider/carousel **Swiper** (v11/v12), distilled from swiperjs.com. It covers the entire API and every module down to the smallest detail.

**Core API:** integration (npm/CDN, CSS imports, HTML structure, module registration), the **complete parameter reference** (236 parameters with type/default), **all methods** (68), **all events** (74) and **properties** (45).

**All modules** (each with its parameters/methods/events/CSS): Navigation, Pagination, Scrollbar, Autoplay, **effects** (fade/cube/coverflow/flip/cards/creative), Virtual, Keyboard, Mousewheel, Zoom, FreeMode, Grid, Thumbs, Controller, A11y, History, HashNavigation, Parallax, Manipulation, Lazy.

**Integration variants:** the **Swiper Element** web component (`<swiper-container>`) as well as **React/Vue** (dedicated components) and **Angular/Svelte/Solid** (via the element, since v9 ships without dedicated adapters). Plus **migration** (v9/v10/v11), custom **plugins** (plugin API) and the **Swiper MCP** server.

Specialist: **`swiper-expert`**; scaffolder **`/swiper-init`** (variant + HTML + CSS imports + module registration + init). **When to use:** for any slider/carousel in the frontend — including Shopware storefront/admin or Contao projects.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. Knowledge distilled from swiperjs.com and embedded; each skill keeps a lean `SKILL.md` and loads its depth from flat SCREAMING-CASE.md reference files next to it.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install swiper@claude-a-dev-team
```

## Skills (4)

| Skill | Description |
|---|---|
| `swiper-core` | Swiper core API: getting started (npm, CDN, CSS imports, HTML structure, first instance, module registration), the exhaustive reference of all configuration parameters, all instance methods (slideNext, slidePrev, slideTo, update, destroy, on/off/once, navigation/pagination/scrollbar/autoplay/zoom/manipulation methods), all events (init, slideChange, transitionStart/End, touchStart/Move/End, reachBeginning, reachEnd, progress, autoplay, pagination, navigation, zoom and more), all properties (activeIndex, realIndex, previousIndex, slides, translate, progress, isBeginning, isEnd, params, el, wrapperEl, snapGrid, slidesGrid plus module properties), the Swiper Element web component (`<swiper-container>`/`<swiper-slide>` registration, parameters as kebab-case attributes, JSON attributes, property binding, slots, lowercase events, methods, shadow-DOM CSS) and migration across major versions (v9/v10/v11 breaking changes: CSS imports, module imports, lazy loading, element structure, removed parameters, framework adapter removal, touch events, Dom7). |
| `swiper-modules` | Swiper modules with their parameters, methods, events and CSS: Navigation (nextEl/prevEl, disabledClass, hiddenClass, lockClass, addIcons, hideOnClick, CSS variables), Pagination (bullets/fraction/progressbar/custom, clickable, dynamicBullets, renderBullet/Fraction/Custom/Progressbar, CSS variables), Scrollbar (el, draggable, dragSize, hide, snapOnRelease, CSS variables, scrollbarDragStart/Move/End), Autoplay (delay, disableOnInteraction, pauseOnMouseEnter, reverseDirection, stopOnLastSlide, waitForTransition, start/stop/pause/resume, autoplayTimeLeft), effects (fade, cube, coverflow, flip, cards, creative — each with its full parameter object: fadeEffect, cubeEffect, coverflowEffect, flipEffect, cardsEffect, creativeEffect), Virtual (slides array, renderSlide, renderExternal, cache, addSlidesBefore/After for performant DOM rendering of large slide sets), Zoom (maxRatio, minRatio, toggle, limitToOriginalSize, panOnMouseMove, containerClass, zoom.in/out/toggle, zoomChange, per-slide `data-swiper-zoom`), Thumbs (linking a swiper instance, multipleActiveThumbs, autoScrollOffset, slideThumbActiveClass, thumbsContainerClass, init/update), Grid (rows, fill column/row for multi-row slide layouts), FreeMode (momentum, momentumRatio, momentumVelocityRatio, momentumBounce, minimumVelocity, sticky — free scrolling without snap points, with momentum physics), Keyboard (enabled, onlyInViewport, pageUpDown, enable/disable, keyPress), Mousewheel (enabled, invert, forceToAxis, releaseOnEdges, sensitivity, thresholdDelta, thresholdTime, eventsTarget, noMousewheelClass, enable/disable, scroll) and A11y (ARIA attributes, prevSlideMessage, nextSlideMessage, firstSlideMessage, lastSlideMessage, paginationBulletMessage, notificationClass — screen reader support). |
| `swiper-advanced` | Swiper advanced features: Controller (control, inverse, by slide/progress — synchronizing multiple Swiper instances, bidirectional control), History (key, replaceState, keepQuery, root — browser history integration with a per-slide `data-history` attribute), Hash Navigation (enabled, replaceState, watchState — URL-hash-based slide navigation with the `data-hash` attribute), Parallax (`data-swiper-parallax`, `data-swiper-parallax-x/y`, `data-swiper-parallax-scale`, `data-swiper-parallax-opacity`, `data-swiper-parallax-duration` — parallax effects for backgrounds and slide content), Lazy loading (native `loading="lazy"` browser integration, lazyPreloadPrevNext, lazyPreloaderClass, the `swiper-lazy-preloader` HTML element), Manipulation (appendSlide, prependSlide, addSlide(index), removeSlide, removeAllSlides — adding and removing slides dynamically), custom plugins (premium plugins from UI Initiative and Swiper Studio, plus the plugin API structure for writing your own Swiper modules) and the Swiper MCP server (HTTP endpoint for programmatic access to the Swiper documentation, 8 tools: search-api, get-option, get-method, get-event, get-module-options, list-demos, get-demo, get-premium-recommendations, plus setup for Claude Code). |
| `swiper-frameworks` | Swiper framework bindings: React (`<Swiper>`/`<SwiperSlide>`, all props = API parameters, the modules prop, events as `onXxx` props, the `useSwiper`/`useSwiperSlide` hooks, slots, virtual slides, controller), Vue (`<Swiper>`/`<SwiperSlide>`, props, events, `v-slot` render props, the `useSwiper`/`useSwiperSlide` composables, modules, virtual slides, controller, thumbs), Angular (since v9 via Swiper Element `<swiper-container>`/`<swiper-slide>`, CUSTOM_ELEMENTS_SCHEMA, property binding, events, ViewChild access), Svelte/SvelteKit (since v9 via Swiper Element, `register()`, property binding with `bind:this`, events with `on:swiper*`) and SolidJS (since v9 via Swiper Element, `register()`, property binding, events). |

## Agents (1)

| Agent | Description |
|---|---|
| `swiper-expert` | Specialist for Swiper (modern touch slider/carousel, v11/v12). |

## Commands (1)

| Command | Description |
|---|---|
| `/swiper-init` | Scaffolds a Swiper integration — variant (Core/Element/React/Vue), HTML structure, CSS imports, module registration (Navigation/Pagination/Autoplay/effects/…) and init code with the desired parameters. |
