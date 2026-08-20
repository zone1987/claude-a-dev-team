# Swiper — Complete parameter reference (v11/12)

All parameters are passed as the second argument to `new Swiper(el, options)`.

---

## Contents

- [1. Core parameters](#1-core-parameters)
- [2. Breakpoints](#2-breakpoints)
- [3. Navigation parameters](#3-navigation-parameters)
- [4. Pagination parameters](#4-pagination-parameters)
- [5. Scrollbar parameters](#5-scrollbar-parameters)
- [6. Autoplay parameters](#6-autoplay-parameters)
- [7. FreeMode parameters](#7-freemode-parameters)
- [8. Grid parameters (multirow)](#8-grid-parameters-multirow)
- [9. Fade effect parameters](#9-fade-effect-parameters)
- [10. Coverflow effect parameters](#10-coverflow-effect-parameters)
- [11. Flip effect parameters](#11-flip-effect-parameters)
- [12. Cube effect parameters](#12-cube-effect-parameters)
- [13. Cards effect parameters](#13-cards-effect-parameters)
- [14. Creative effect parameters](#14-creative-effect-parameters)
- [15. Thumbs parameters](#15-thumbs-parameters)
- [16. Zoom parameters](#16-zoom-parameters)
- [17. Keyboard parameters](#17-keyboard-parameters)
- [18. Mousewheel parameters](#18-mousewheel-parameters)
- [19. Virtual Slides parameters](#19-virtual-slides-parameters)

## 1. Core parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `a11y` | `boolean \| A11yOptions` | — | Accessibility (ARIA labels). `true` = defaults. |
| `allowSlideNext` | `boolean` | `true` | `false` = swiping to the next slide disabled. |
| `allowSlidePrev` | `boolean` | `true` | `false` = swiping to the previous slide disabled. |
| `allowTouchMove` | `boolean` | `true` | `false` = swiping disabled; API control only. |
| `autoHeight` | `boolean` | `false` | Wrapper adjusts its height to the active slide. |
| `autoplay` | `boolean \| AutoplayOptions` | — | Enable autoplay. See Autoplay parameters. |
| `breakpoints` | `object` | — | Breakpoint-specific parameters (responsive). |
| `breakpointsBase` | `'container' \| CSSSelector \| 'window'` | `'window'` | Base for breakpoints: `'window'` or `'container'` (beta). |
| `cardsEffect` | `CardsEffectOptions` | — | Cards effect parameters. See Cards effect. |
| `centerInsufficientSlides` | `boolean` | `false` | Centers slides when fewer than `slidesPerView` are present. |
| `centeredSlides` | `boolean` | `false` | `true` = active slide is centered (not always left). |
| `centeredSlidesBounds` | `boolean` | `false` | Centers the active slide without gaps at the edges. |
| `containerModifierClass` | `string` | `'swiper-'` | Prefix of the CSS modifier class for the container. |
| `controller` | `boolean \| ControllerOptions` | — | Couple two Swipers (control them in sync). |
| `coverflowEffect` | `CoverflowEffectOptions` | — | Coverflow effect parameters. |
| `createElements` | `boolean` | `false` | Swiper wraps slides automatically in a wrapper. |
| `creativeEffect` | `CreativeEffectOptions` | — | Creative effect parameters. |
| `cssMode` | `boolean` | `false` | Uses the modern CSS Scroll Snap API. |
| `cubeEffect` | `CubeEffectOptions` | — | Cube effect parameters. |
| `direction` | `'horizontal' \| 'vertical'` | `'horizontal'` | Slider direction. |
| `edgeSwipeDetection` | `string \| boolean` | `false` | Releases Swiper events for swipe-back in apps. |
| `edgeSwipeThreshold` | `number` | `20` | Area in px from the left screen edge for touch event release. |
| `effect` | `'slide' \| 'fade' \| 'cube' \| 'coverflow' \| 'flip' \| 'creative' \| 'cards'` | `'slide'` | Transition effect. |
| `enabled` | `boolean` | `true` | `false` = Swiper initially disabled. |
| `eventsPrefix` | `string` | `'swiper'` | Event name prefix for all DOM events (Swiper Element). |
| `fadeEffect` | `FadeEffectOptions` | — | Fade effect parameters. |
| `flipEffect` | `FlipEffectOptions` | — | Flip effect parameters. |
| `focusableElements` | `string` | `'input, select, option, textarea, button, video, label'` | CSS selector for focusable elements (touch interruption). |
| `followFinger` | `boolean` | `true` | `false` = slider only animates on release. |
| `freeMode` | `boolean \| FreeModeOptions` | — | Free mode (no snapping). See FreeMode parameters. |
| `grabCursor` | `boolean` | `false` | `true` = grab cursor on hover. |
| `grid` | `GridOptions` | — | Multirow layout. See Grid parameters. |
| `hashNavigation` | `boolean \| HashNavigationOptions` | — | URL hash navigation per slide. |
| `height` | `number \| null` | `null` | Force Swiper height in px. |
| `history` | `boolean \| HistoryOptions` | — | History pushState navigation. |
| `init` | `boolean` | `true` | `false` = do not initialize Swiper automatically. |
| `initialSlide` | `number` | `0` | Index of the initial slide. |
| `injectStyles` | `string[]` | — | Inject text styles into the shadow DOM (Swiper Element). |
| `injectStylesUrls` | `string[]` | — | Inject `<link>` styles into the shadow DOM (Swiper Element). |
| `keyboard` | `boolean \| KeyboardOptions` | — | Keyboard navigation. See Keyboard parameters. |
| `lazyPreloadPrevNext` | `number` | `0` | Number of preloaded slides before/after the active one. |
| `lazyPreloaderClass` | `string` | `'swiper-lazy-preloader'` | CSS class of the lazy preloader. |
| `longSwipes` | `boolean` | `true` | `false` = long swipe gestures disabled. |
| `longSwipesMs` | `number` | `300` | Minimum duration (ms) for a long swipe. |
| `longSwipesRatio` | `number` | `0.5` | Ratio for a long swipe to the next/previous slide. |
| `loop` | `boolean` | `false` | `true` = endless loop mode. |
| `loopAddBlankSlides` | `boolean` | `true` | Automatically adds blank slides with grid / `slidesPerGroup`. |
| `loopAdditionalSlides` | `number` | `0` | Number of additional cloned slides in loop mode. |
| `loopPreventsSliding` | `boolean` | `true` | `slideNext`/`Prev` do nothing during the loop animation. |
| `maxBackfaceHiddenSlides` | `number` | `10` | With fewer slides than this value, `backface-visibility` is enabled. |
| `modules` | `SwiperModule[]` | — | Array of the Swiper modules to use. |
| `mousewheel` | `boolean \| MousewheelOptions` | — | Mouse wheel navigation. See Mousewheel parameters. |
| `navigation` | `boolean \| NavigationOptions` | — | Navigation arrows. See Navigation parameters. |
| `nested` | `boolean` | `false` | `true` for correct touch interception with nested Swipers. |
| `noSwiping` | `boolean` | `true` | Disable swiping on elements with `noSwipingClass`. |
| `noSwipingClass` | `string` | `'swiper-no-swiping'` | CSS class for elements without swiping. |
| `noSwipingSelector` | `string` | — | CSS selector instead of `noSwipingClass`. |
| `normalizeSlideIndex` | `boolean` | `true` | Normalize the slide index. |
| `observeParents` | `boolean` | `false` | MutationObserver on parent elements as well. |
| `observeSlideChildren` | `boolean` | `false` | MutationObserver on the child elements of the slides. |
| `observer` | `boolean` | `false` | Enable MutationObserver on the Swiper. |
| `on` | `object` | — | Register event handlers directly in the constructor. |
| `onAny` | `function(handler)` | — | Listener that fires on every event. |
| `oneWayMovement` | `boolean` | `false` | Only forward swiping possible. |
| `pagination` | `boolean \| PaginationOptions` | — | Pagination. See Pagination parameters. |
| `parallax` | `boolean \| ParallaxOptions` | — | Parallax effects. |
| `passiveListeners` | `boolean` | `true` | Passive event listeners for better scroll performance. |
| `preventClicks` | `boolean` | `true` | Prevents unintended clicks on links during a swipe. |
| `preventClicksPropagation` | `boolean` | `true` | Stops click event propagation on links. |
| `preventInteractionOnTransition` | `boolean` | `false` | No slide changes possible during the transition. |
| `resistance` | `boolean` | `true` | `false` = no resistance at the edges. |
| `resistanceRatio` | `number` | `0.85` | Resistance strength at the edges (0–1). |
| `resizeObserver` | `boolean` | `true` | Use ResizeObserver for container size changes. |
| `rewind` | `boolean` | `false` | Jump back to the first slide at the end (no loop). |
| `roundLengths` | `boolean` | `false` | Round the width/height of the slides. |
| `runCallbacksOnInit` | `boolean` | `true` | Fire events on initialization. |
| `scrollbar` | `boolean \| ScrollbarOptions` | — | Scrollbar. See Scrollbar parameters. |
| `setWrapperSize` | `boolean` | `false` | Set the wrapper width/height to the total size. |
| `shortSwipes` | `boolean` | `true` | `false` = short swipe gestures disabled. |
| `simulateTouch` | `boolean` | `true` | `true` = Swiper reacts to mouse events like touch events. |
| `slideActiveClass` | `string` | `'swiper-slide-active'` | CSS class of the active slide. |
| `slideBlankClass` | `string` | `'swiper-slide-blank'` | CSS class of blank slides (loop mode). |
| `slideClass` | `string` | `'swiper-slide'` | CSS class of the slides. |
| `slideFullyVisibleClass` | `string` | `'swiper-slide-fully-visible'` | CSS class of fully visible slides. |
| `slideNextClass` | `string` | `'swiper-slide-next'` | CSS class of the slide after the active one. |
| `slidePrevClass` | `string` | `'swiper-slide-prev'` | CSS class of the slide before the active one. |
| `slideToClickedSlide` | `boolean` | `false` | Clicking a slide triggers a transition to it. |
| `slideVisibleClass` | `string` | `'swiper-slide-visible'` | CSS class of partially visible slides. |
| `slidesOffsetAfter` | `number` | `0` | Additional offset (px) at the end of the wrapper. |
| `slidesOffsetBefore` | `number` | `0` | Additional offset (px) at the start of the wrapper. |
| `slidesPerGroup` | `number` | `1` | Number of slides per group when swiping. |
| `slidesPerGroupAuto` | `boolean` | `false` | Only with `slidesPerView: 'auto'` + `slidesPerGroup: 1`. |
| `slidesPerGroupSkip` | `number` | `0` | First X slides individually, the rest per `slidesPerGroup`. |
| `slidesPerView` | `number \| 'auto'` | `1` | Number of slides visible at the same time. |
| `snapToSlideEdge` | `boolean` | `false` | Snap to slide edges instead of calculated positions. |
| `spaceBetween` | `string \| number` | `0` | Spacing between slides in px. |
| `speed` | `number` | `300` | Transition duration in ms. |
| `swipeHandler` | `HTMLElement \| CSSSelector \| null` | `null` | Container that serves as the swipe handler. |
| `swiperElementNodeName` | `string` | `'SWIPER-CONTAINER'` | Node name of the Swiper element. |
| `threshold` | `number` | `5` | Minimum movement in px to trigger a swipe. |
| `thumbs` | `ThumbsOptions` | — | Thumbs component. See Thumbs parameters. |
| `touchAngle` | `number` | `45` | Maximum angle (degrees) for touch move triggering. |
| `touchEventsTarget` | `'container' \| 'wrapper'` | `'wrapper'` | Element on which touch events are registered. |
| `touchMoveStopPropagation` | `boolean` | `false` | Stops `touchmove` event propagation. |
| `touchRatio` | `number` | `1` | Touch ratio (multiplier for touch movement). |
| `touchReleaseOnEdges` | `boolean` | `false` | Release touch events at the edges (for scrolling). |
| `touchStartForcePreventDefault` | `boolean` | `false` | Always call `preventDefault()` on `touchstart`. |
| `touchStartPreventDefault` | `boolean` | `true` | `false` = `pointerdown` not prevented. |
| `uniqueNavElements` | `boolean` | `true` | Look for navigation elements only in child elements. |
| `updateOnWindowResize` | `boolean` | `true` | Recalculate on window resize. |
| `url` | `string \| null` | `null` | URL for the active slide in server-side rendering. |
| `userAgent` | `string \| null` | `null` | UserAgent string for server-side rendering. |
| `virtual` | `boolean \| VirtualOptions` | — | Virtual slides. See Virtual parameters. |
| `virtualTranslate` | `boolean` | `false` | Swiper works normally but does not move physically. |
| `watchOverflow` | `boolean` | `true` | Hide navigation/scrollbar when there are too few slides. |
| `watchSlidesProgress` | `boolean` | `false` | Calculate progress and visibility of every slide. |
| `width` | `number \| null` | `null` | Force Swiper width in px. |
| `wrapperClass` | `string` | `'swiper-wrapper'` | CSS class of the wrapper. |
| `zoom` | `boolean \| ZoomOptions` | — | Zoom function. See Zoom parameters. |

---

## 2. Breakpoints

```js
const swiper = new Swiper('.swiper', {
  slidesPerView: 1,
  spaceBetween: 10,
  breakpoints: {
    // from 640px
    640: { slidesPerView: 2, spaceBetween: 20 },
    // from 768px
    768: { slidesPerView: 3, spaceBetween: 30 },
    // from 1024px
    1024: { slidesPerView: 4, spaceBetween: 40 },
  },
});
```

---

## 3. Navigation parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `navigation.addIcons` | `boolean` | `true` | Add SVG icons to navigation buttons automatically. |
| `navigation.disabledClass` | `string` | `'swiper-button-disabled'` | CSS class when the button is disabled. |
| `navigation.enabled` | `boolean` | — | For breakpoints: enable/disable navigation. |
| `navigation.hiddenClass` | `string` | `'swiper-button-hidden'` | CSS class when the button is hidden. |
| `navigation.hideOnClick` | `boolean` | `false` | Hide/show navigation after a click on the slider. |
| `navigation.lockClass` | `string` | `'swiper-button-lock'` | CSS class when navigation is locked. |
| `navigation.navigationDisabledClass` | `string` | `'swiper-navigation-disabled'` | Container class when navigation is disabled. |
| `navigation.nextEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS selector or HTMLElement for the next button. |
| `navigation.prevEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS selector or HTMLElement for the previous button. |

---

## 4. Pagination parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `pagination.bulletActiveClass` | `string` | `'swiper-pagination-bullet-active'` | CSS class of the active bullet. |
| `pagination.bulletClass` | `string` | `'swiper-pagination-bullet'` | CSS class of a bullet. |
| `pagination.bulletElement` | `string` | `'span'` | HTML tag for bullets. |
| `pagination.clickable` | `boolean` | `false` | Clicking a bullet navigates to the slide. |
| `pagination.clickableClass` | `string` | `'swiper-pagination-clickable'` | Class when the pagination is clickable. |
| `pagination.currentClass` | `string` | `'swiper-pagination-current'` | Class of the current fraction element. |
| `pagination.dynamicBullets` | `boolean` | `false` | Only a few bullets visible with many slides. |
| `pagination.dynamicMainBullets` | `number` | `1` | Number of visible main bullets with `dynamicBullets`. |
| `pagination.el` | `HTMLElement \| CSSSelector \| null` | `null` | CSS selector or HTMLElement of the pagination. |
| `pagination.enabled` | `boolean` | — | For breakpoints. |
| `pagination.formatFractionCurrent` | `function(number)` | — | Format the fraction counter. |
| `pagination.formatFractionTotal` | `function(number)` | — | Format the fraction total. |
| `pagination.hiddenClass` | `string` | `'swiper-pagination-hidden'` | Class when the pagination is inactive. |
| `pagination.hideOnClick` | `boolean` | `true` | Hide the pagination after a click on the slider. |
| `pagination.horizontalClass` | `string` | `'swiper-pagination-horizontal'` | Class with a horizontal Swiper. |
| `pagination.lockClass` | `string` | `'swiper-pagination-lock'` | Class when the pagination is disabled. |
| `pagination.modifierClass` | `string` | `'swiper-pagination-'` | Prefix of the modifier CSS class. |
| `pagination.paginationDisabledClass` | `string` | `'swiper-pagination-disabled'` | Container class when the pagination is disabled. |
| `pagination.progressbarFillClass` | `string` | `'swiper-pagination-progressbar-fill'` | CSS class of the progress bar fill element. |
| `pagination.progressbarOpposite` | `boolean` | `false` | Progress bar opposite to the slider direction. |
| `pagination.progressbarOppositeClass` | `string` | `'swiper-pagination-progressbar-opposite'` | Class of the opposite progress bar. |
| `pagination.renderBullet` | `function(index, className)` | `null` | Render bullets individually. |
| `pagination.renderCustom` | `function(swiper, current, total)` | `null` | Required with `type: 'custom'`. |
| `pagination.renderFraction` | `function(currentClass, totalClass)` | `null` | Render fraction pagination individually. |
| `pagination.renderProgressbar` | `function(progressbarFillClass)` | `null` | Render the progress bar individually. |
| `pagination.totalClass` | `string` | `'swiper-pagination-total'` | Class of the total count element. |
| `pagination.type` | `'bullets' \| 'fraction' \| 'progressbar' \| 'custom'` | `'bullets'` | Pagination type. |
| `pagination.verticalClass` | `string` | `'swiper-pagination-vertical'` | Class with a vertical Swiper. |

---

## 5. Scrollbar parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `scrollbar.dragClass` | `string` | `'swiper-scrollbar-drag'` | CSS class of the scrollbar drag element. |
| `scrollbar.dragSize` | `number \| 'auto'` | `'auto'` | Size of the drag element in px. |
| `scrollbar.draggable` | `boolean` | `false` | The scrollbar is draggable. |
| `scrollbar.el` | `HTMLElement \| CSSSelector \| null` | `null` | CSS selector or HTMLElement of the scrollbar. |
| `scrollbar.enabled` | `boolean` | — | For breakpoints. |
| `scrollbar.hide` | `boolean` | `true` | Hide the scrollbar automatically after interaction. |
| `scrollbar.horizontalClass` | `string` | `'swiper-scrollbar-horizontal'` | Class with a horizontal Swiper. |
| `scrollbar.lockClass` | `string` | `'swiper-scrollbar-lock'` | Class when the scrollbar is disabled. |
| `scrollbar.scrollbarDisabledClass` | `string` | `'swiper-scrollbar-disabled'` | Container class when the scrollbar is disabled. |
| `scrollbar.snapOnRelease` | `boolean` | `false` | Snap to a slide on release. |
| `scrollbar.verticalClass` | `string` | `'swiper-scrollbar-vertical'` | Class with a vertical Swiper. |

---

## 6. Autoplay parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `autoplay.delay` | `number` | `3000` | Pause between transitions in ms. |
| `autoplay.disableOnInteraction` | `boolean` | `true` | `false` = autoplay continues after user interaction. |
| `autoplay.pauseOnMouseEnter` | `boolean` | `false` | Autoplay pauses on hover. |
| `autoplay.reverseDirection` | `boolean` | `false` | Autoplay in reverse direction. |
| `autoplay.stopOnLastSlide` | `boolean` | `false` | Autoplay stops at the last slide. |
| `autoplay.waitForTransition` | `boolean` | `true` | Autoplay waits for the wrapper transition. |

---

## 7. FreeMode parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `freeMode.enabled` | `boolean` | `false` | Enable free mode. |
| `freeMode.minimumVelocity` | `number` | `0.02` | Minimum swipe speed for momentum. |
| `freeMode.momentum` | `boolean` | `true` | The slide keeps gliding after release. |
| `freeMode.momentumBounce` | `boolean` | `true` | `false` = no bounce at the edge. |
| `freeMode.momentumBounceRatio` | `number` | `1` | Bounce strength. |
| `freeMode.momentumRatio` | `number` | `1` | Momentum distance multiplier. |
| `freeMode.momentumVelocityRatio` | `number` | `1` | Momentum speed multiplier. |
| `freeMode.sticky` | `boolean` | `false` | Snap to slide positions (free mode + snap). |

---

## 8. Grid parameters (multirow)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `grid.fill` | `'row' \| 'column'` | `'column'` | Fill direction: by column or by row. |
| `grid.rows` | `number` | `1` | Number of rows. |

```js
// Example: 2 rows, 3 columns
const swiper = new Swiper('.swiper', {
  modules: [Grid],
  grid: { rows: 2, fill: 'row' },
  slidesPerView: 3,
  spaceBetween: 20,
});
```

---

## 9. Fade effect parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `fadeEffect.crossFade` | `boolean` | `false` | Enable cross fade (fade out + fade in at the same time). |

---

## 10. Coverflow effect parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `coverflowEffect.depth` | `number` | `100` | Depth offset in px (Z axis). |
| `coverflowEffect.modifier` | `number` | `1` | Effect multiplier. |
| `coverflowEffect.rotate` | `number` | `50` | Rotation in degrees. |
| `coverflowEffect.scale` | `number` | `1` | Scaling effect. |
| `coverflowEffect.slideShadows` | `boolean` | `true` | Enable slide shadows. |
| `coverflowEffect.stretch` | `number` | `0` | Additional space between slides. |

---

## 11. Flip effect parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `flipEffect.limitRotation` | `boolean` | `true` | Limit the rotation of the edge slides. |
| `flipEffect.slideShadows` | `boolean` | `true` | Enable slide shadows. |

---

## 12. Cube effect parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `cubeEffect.shadow` | `boolean` | `true` | Main slider shadow. |
| `cubeEffect.shadowOffset` | `number` | `20` | Shadow offset in px. |
| `cubeEffect.shadowScale` | `number` | `0.94` | Shadow scale ratio. |
| `cubeEffect.slideShadows` | `boolean` | `true` | Enable slide shadows. |

---

## 13. Cards effect parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `cardsEffect.perSlideOffset` | `number` | `8` | Offset per slide in px. |
| `cardsEffect.perSlideRotate` | `number` | `2` | Rotation per slide in degrees. |
| `cardsEffect.rotate` | `boolean` | `true` | Enable cards rotation. |
| `cardsEffect.slideShadows` | `boolean` | `true` | Enable slide shadows. |

---

## 14. Creative effect parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `creativeEffect.limitProgress` | `number` | `1` | Limit progress/offset on the side slides. |
| `creativeEffect.next` | `CreativeEffectTransform` | — | Transforms of the next slide. |
| `creativeEffect.perspective` | `boolean` | `true` | Enable 3D transforms. |
| `creativeEffect.prev` | `CreativeEffectTransform` | — | Transforms of the previous slide. |
| `creativeEffect.progressMultiplier` | `number` | `1` | Transform and opacity multiplier. |
| `creativeEffect.shadowPerProgress` | `boolean` | `false` | Split shadow opacity per slide. |

---

## 15. Thumbs parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `thumbs.autoScrollOffset` | `number` | `0` | How many slides from the edge the active thumb is scrolled at. |
| `thumbs.multipleActiveThumbs` | `boolean` | `true` | Several thumbs can be active at the same time. |
| `thumbs.slideThumbActiveClass` | `string` | `'swiper-slide-thumb-active'` | Class of the active thumb slide. |
| `thumbs.swiper` | `string \| Swiper \| null` | `null` | Swiper instance or CSS selector of the thumbs Swiper. |
| `thumbs.thumbsContainerClass` | `string` | `'swiper-thumbs'` | Class of the thumbs container. |

---

## 16. Zoom parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `zoom.containerClass` | `string` | `'swiper-zoom-container'` | CSS class of the zoom container. |
| `zoom.limitToOriginalSize` | `boolean` | `false` | Do not scale the image beyond 100%. |
| `zoom.maxRatio` | `number` | `3` | Maximum zoom factor. |
| `zoom.minRatio` | `number` | `1` | Minimum zoom factor. |
| `zoom.panOnMouseMove` | `boolean` | `false` | The zoomed image follows the mouse movement. |
| `zoom.toggle` | `boolean` | `true` | Enable double tap to zoom. |
| `zoom.zoomedSlideClass` | `string` | `'swiper-slide-zoomed'` | Class of the zoomed slide. |

---

## 17. Keyboard parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `keyboard.enabled` | `boolean` | `false` | Enable keyboard control. |
| `keyboard.onlyInViewport` | `boolean` | `true` | Only control when the Swiper is visible in the viewport. |
| `keyboard.pageUpDown` | `boolean` | `true` | Enable the Page Up/Down keys. |
| `keyboard.speed` | `number` | `undefined` | Speed of the keyboard navigation in ms. |

---

## 18. Mousewheel parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `mousewheel.enabled` | `boolean` | `false` | Enable mouse wheel control. |
| `mousewheel.eventsTarget` | `HTMLElement \| 'container' \| 'wrapper' \| CSSSelector` | `'container'` | Element that receives mouse wheel events. |
| `mousewheel.forceToAxis` | `boolean` | `false` | Force mouse wheel movement onto the slider axis. |
| `mousewheel.invert` | `boolean` | `false` | Invert the direction. |
| `mousewheel.noMousewheelClass` | `string` | `'swiper-no-mousewheel'` | Elements with this class ignore the mouse wheel. |
| `mousewheel.releaseOnEdges` | `boolean` | `false` | Release the mouse wheel at the edges (page scroll). |
| `mousewheel.sensitivity` | `number` | `1` | Mouse wheel sensitivity multiplier. |
| `mousewheel.thresholdDelta` | `number \| null` | `null` | Minimum scroll delta value for a slide change. |
| `mousewheel.thresholdTime` | `number \| null` | `null` | Minimum time delta (ms) for a slide change. |

---

## 19. Virtual Slides parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `virtual.addSlidesAfter` | `number` | `0` | Additional pre-rendered slides after the active one. |
| `virtual.addSlidesBefore` | `number` | `0` | Additional pre-rendered slides before the active one. |
| `virtual.cache` | `boolean` | `true` | DOM cache of the rendered slides. |
| `virtual.enabled` | `boolean` | `false` | Enable virtual slides. |
| `virtual.renderExternal` | `function(VirtualData)` | `null` | External rendering (e.g. React/Vue). |

```js
// Virtual slides example
const swiper = new Swiper('.swiper', {
  modules: [Virtual],
  virtual: {
    enabled: true,
    slides: Array.from({ length: 1000 }, (_, i) => `Slide ${i + 1}`),
    renderSlide(slide, index) {
      return `<div class="swiper-slide">${slide}</div>`;
    },
  },
});
```

---

*Source: https://swiperjs.com/swiper-api*
