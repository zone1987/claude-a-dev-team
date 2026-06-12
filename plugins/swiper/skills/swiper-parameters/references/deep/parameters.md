# Swiper — Vollständige Parameter-Referenz (v11/12)

Alle Parameter werden als zweites Argument an `new Swiper(el, options)` übergeben.

---

## 1. Core-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `a11y` | `boolean \| A11yOptions` | — | Barrierefreiheit (ARIA-Labels). `true` = Defaults. |
| `allowSlideNext` | `boolean` | `true` | `false` = Swipen zur nächsten Folie deaktiviert. |
| `allowSlidePrev` | `boolean` | `true` | `false` = Swipen zur vorherigen Folie deaktiviert. |
| `allowTouchMove` | `boolean` | `true` | `false` = Wischen deaktiviert; nur API-Steuerung. |
| `autoHeight` | `boolean` | `false` | Wrapper passt seine Höhe an die aktive Folie an. |
| `autoplay` | `boolean \| AutoplayOptions` | — | Autoplay aktivieren. Siehe Autoplay-Parameter. |
| `breakpoints` | `object` | — | Breakpoint-spezifische Parameter (responsive). |
| `breakpointsBase` | `'container' \| CSSSelector \| 'window'` | `'window'` | Basis für Breakpoints: `'window'` oder `'container'` (Beta). |
| `cardsEffect` | `CardsEffectOptions` | — | Cards-Effekt-Parameter. Siehe Cards-Effekt. |
| `centerInsufficientSlides` | `boolean` | `false` | Zentriert Folien, wenn weniger als `slidesPerView` vorhanden. |
| `centeredSlides` | `boolean` | `false` | `true` = Aktive Folie wird zentriert (nicht immer links). |
| `centeredSlidesBounds` | `boolean` | `false` | Zentriert aktive Folie ohne Lücken an den Rändern. |
| `containerModifierClass` | `string` | `'swiper-'` | Präfix der CSS-Modifier-Klasse für den Container. |
| `controller` | `boolean \| ControllerOptions` | — | Zwei Swiper koppeln (synchron steuern). |
| `coverflowEffect` | `CoverflowEffectOptions` | — | Coverflow-Effekt-Parameter. |
| `createElements` | `boolean` | `false` | Swiper umschließt Folien automatisch mit einem Wrapper. |
| `creativeEffect` | `CreativeEffectOptions` | — | Creative-Effekt-Parameter. |
| `cssMode` | `boolean` | `false` | Nutzt modernes CSS Scroll Snap API. |
| `cubeEffect` | `CubeEffectOptions` | — | Cube-Effekt-Parameter. |
| `direction` | `'horizontal' \| 'vertical'` | `'horizontal'` | Slider-Richtung. |
| `edgeSwipeDetection` | `string \| boolean` | `false` | Gibt Swiper-Events frei für Swipe-Back in Apps. |
| `edgeSwipeThreshold` | `number` | `20` | Bereich in px vom linken Bildschirmrand für Touch-Event-Freigabe. |
| `effect` | `'slide' \| 'fade' \| 'cube' \| 'coverflow' \| 'flip' \| 'creative' \| 'cards'` | `'slide'` | Übergangseffekt. |
| `enabled` | `boolean` | `true` | `false` = Swiper initial deaktiviert. |
| `eventsPrefix` | `string` | `'swiper'` | Event-Name-Präfix für alle DOM-Events (Swiper Element). |
| `fadeEffect` | `FadeEffectOptions` | — | Fade-Effekt-Parameter. |
| `flipEffect` | `FlipEffectOptions` | — | Flip-Effekt-Parameter. |
| `focusableElements` | `string` | `'input, select, option, textarea, button, video, label'` | CSS-Selektor für fokussierbare Elemente (Touch-Unterbrechung). |
| `followFinger` | `boolean` | `true` | `false` = Slider animiert erst beim Loslassen. |
| `freeMode` | `boolean \| FreeModeOptions` | — | Free-Mode (kein Einrasten). Siehe FreeMode-Parameter. |
| `grabCursor` | `boolean` | `false` | `true` = Grab-Cursor beim Hover. |
| `grid` | `GridOptions` | — | Multirow-Layout. Siehe Grid-Parameter. |
| `hashNavigation` | `boolean \| HashNavigationOptions` | — | URL-Hash-Navigation pro Folie. |
| `height` | `number \| null` | `null` | Swiper-Höhe in px erzwingen. |
| `history` | `boolean \| HistoryOptions` | — | History-pushState-Navigation. |
| `init` | `boolean` | `true` | `false` = Swiper nicht automatisch initialisieren. |
| `initialSlide` | `number` | `0` | Index der initialen Folie. |
| `injectStyles` | `string[]` | — | Text-Styles in den Shadow DOM injizieren (Swiper Element). |
| `injectStylesUrls` | `string[]` | — | `<link>`-Styles in den Shadow DOM injizieren (Swiper Element). |
| `keyboard` | `boolean \| KeyboardOptions` | — | Tastaturnavigation. Siehe Keyboard-Parameter. |
| `lazyPreloadPrevNext` | `number` | `0` | Anzahl der vorab geladenen Folien vor/nach der aktiven. |
| `lazyPreloaderClass` | `string` | `'swiper-lazy-preloader'` | CSS-Klasse des Lazy-Preloaders. |
| `longSwipes` | `boolean` | `true` | `false` = Lange Wischgesten deaktiviert. |
| `longSwipesMs` | `number` | `300` | Minimale Dauer (ms) für langen Wisch. |
| `longSwipesRatio` | `number` | `0.5` | Verhältnis für langen Wisch zur nächsten/vorherigen Folie. |
| `loop` | `boolean` | `false` | `true` = Endlos-Loop-Modus. |
| `loopAddBlankSlides` | `boolean` | `true` | Fügt automatisch leere Folien bei Grid / `slidesPerGroup` hinzu. |
| `loopAdditionalSlides` | `number` | `0` | Anzahl zusätzlicher geklonter Folien im Loop. |
| `loopPreventsSliding` | `boolean` | `true` | `slideNext`/`Prev` tun nichts während der Loop-Animation. |
| `maxBackfaceHiddenSlides` | `number` | `10` | Bei weniger Slides als dieser Wert wird `backface-visibility` aktiviert. |
| `modules` | `SwiperModule[]` | — | Array der zu verwendenden Swiper-Module. |
| `mousewheel` | `boolean \| MousewheelOptions` | — | Mausrad-Navigation. Siehe Mousewheel-Parameter. |
| `navigation` | `boolean \| NavigationOptions` | — | Navigations-Pfeile. Siehe Navigation-Parameter. |
| `nested` | `boolean` | `false` | `true` für korrekte Touch-Interception bei verschachtelten Swipern. |
| `noSwiping` | `boolean` | `true` | Swipen auf Elementen mit `noSwipingClass` deaktivieren. |
| `noSwipingClass` | `string` | `'swiper-no-swiping'` | CSS-Klasse für Elemente ohne Swipen. |
| `noSwipingSelector` | `string` | — | CSS-Selektor statt `noSwipingClass`. |
| `normalizeSlideIndex` | `boolean` | `true` | Folien-Index normalisieren. |
| `observeParents` | `boolean` | `false` | MutationObserver auch auf Eltern-Elemente. |
| `observeSlideChildren` | `boolean` | `false` | MutationObserver auf Kind-Elemente der Folien. |
| `observer` | `boolean` | `false` | MutationObserver auf dem Swiper aktivieren. |
| `on` | `object` | — | Event-Handler direkt im Konstruktor registrieren. |
| `onAny` | `function(handler)` | — | Listener der bei jedem Event feuert. |
| `oneWayMovement` | `boolean` | `false` | Nur Vorwärts-Swipen möglich. |
| `pagination` | `boolean \| PaginationOptions` | — | Pagination. Siehe Pagination-Parameter. |
| `parallax` | `boolean \| ParallaxOptions` | — | Parallax-Effekte. |
| `passiveListeners` | `boolean` | `true` | Passive Event-Listener für bessere Scroll-Performance. |
| `preventClicks` | `boolean` | `true` | Verhindert unbeabsichtigte Klicks auf Links während Swipe. |
| `preventClicksPropagation` | `boolean` | `true` | Stoppt Click-Event-Propagation auf Links. |
| `preventInteractionOnTransition` | `boolean` | `false` | Keine Folien-Wechsel während der Transition möglich. |
| `resistance` | `boolean` | `true` | `false` = Kein Widerstand an den Rändern. |
| `resistanceRatio` | `number` | `0.85` | Widerstandsstärke an den Rändern (0–1). |
| `resizeObserver` | `boolean` | `true` | ResizeObserver für Container-Größenänderungen nutzen. |
| `rewind` | `boolean` | `false` | Am Ende zur ersten Folie zurückspringen (kein Loop). |
| `roundLengths` | `boolean` | `false` | Breite/Höhe der Folien runden. |
| `runCallbacksOnInit` | `boolean` | `true` | Events bei Initialisierung feuern. |
| `scrollbar` | `boolean \| ScrollbarOptions` | — | Scrollbar. Siehe Scrollbar-Parameter. |
| `setWrapperSize` | `boolean` | `false` | Wrapper-Breite/-Höhe auf Gesamtgröße setzen. |
| `shortSwipes` | `boolean` | `true` | `false` = Kurze Wischgesten deaktiviert. |
| `simulateTouch` | `boolean` | `true` | `true` = Swiper reagiert auf Maus-Events wie Touch-Events. |
| `slideActiveClass` | `string` | `'swiper-slide-active'` | CSS-Klasse der aktiven Folie. |
| `slideBlankClass` | `string` | `'swiper-slide-blank'` | CSS-Klasse leerer Folien (Loop-Modus). |
| `slideClass` | `string` | `'swiper-slide'` | CSS-Klasse der Folien. |
| `slideFullyVisibleClass` | `string` | `'swiper-slide-fully-visible'` | CSS-Klasse vollständig sichtbarer Folien. |
| `slideNextClass` | `string` | `'swiper-slide-next'` | CSS-Klasse der Folie nach der aktiven. |
| `slidePrevClass` | `string` | `'swiper-slide-prev'` | CSS-Klasse der Folie vor der aktiven. |
| `slideToClickedSlide` | `boolean` | `false` | Klick auf Folie erzeugt Transition zu ihr. |
| `slideVisibleClass` | `string` | `'swiper-slide-visible'` | CSS-Klasse teilweise sichtbarer Folien. |
| `slidesOffsetAfter` | `number` | `0` | Zusätzlicher Offset (px) am Ende des Wrappers. |
| `slidesOffsetBefore` | `number` | `0` | Zusätzlicher Offset (px) am Anfang des Wrappers. |
| `slidesPerGroup` | `number` | `1` | Anzahl Folien pro Gruppe beim Wischen. |
| `slidesPerGroupAuto` | `boolean` | `false` | Nur bei `slidesPerView: 'auto'` + `slidesPerGroup: 1`. |
| `slidesPerGroupSkip` | `number` | `0` | Erste X Folien einzeln, Rest nach `slidesPerGroup`. |
| `slidesPerView` | `number \| 'auto'` | `1` | Anzahl sichtbarer Folien gleichzeitig. |
| `snapToSlideEdge` | `boolean` | `false` | Einrasten an Folienkanten statt berechneten Positionen. |
| `spaceBetween` | `string \| number` | `0` | Abstand zwischen Folien in px. |
| `speed` | `number` | `300` | Transition-Dauer in ms. |
| `swipeHandler` | `HTMLElement \| CSSSelector \| null` | `null` | Container der als Swipe-Handler dient. |
| `swiperElementNodeName` | `string` | `'SWIPER-CONTAINER'` | Node-Name des Swiper-Elements. |
| `threshold` | `number` | `5` | Mindest-Bewegung in px um Swipe auszulösen. |
| `thumbs` | `ThumbsOptions` | — | Thumbs-Komponente. Siehe Thumbs-Parameter. |
| `touchAngle` | `number` | `45` | Maximalwinkel (Grad) für Touch-Move-Auslösung. |
| `touchEventsTarget` | `'container' \| 'wrapper'` | `'wrapper'` | Element auf dem Touch-Events registriert werden. |
| `touchMoveStopPropagation` | `boolean` | `false` | Stoppt `touchmove`-Event-Propagation. |
| `touchRatio` | `number` | `1` | Touch-Ratio (Multiplikator für Touch-Bewegung). |
| `touchReleaseOnEdges` | `boolean` | `false` | Touch-Events an Rändern freigeben (für Scroll). |
| `touchStartForcePreventDefault` | `boolean` | `false` | `touchstart` immer `preventDefault()` aufrufen. |
| `touchStartPreventDefault` | `boolean` | `true` | `false` = `pointerdown` nicht prevented. |
| `uniqueNavElements` | `boolean` | `true` | Navigation-Elemente nur in Child-Elementen suchen. |
| `updateOnWindowResize` | `boolean` | `true` | Neu berechnen bei Fenstergrößenänderung. |
| `url` | `string \| null` | `null` | URL für aktive Folie bei Server-Side Rendering. |
| `userAgent` | `string \| null` | `null` | UserAgent-String für Server-Side Rendering. |
| `virtual` | `boolean \| VirtualOptions` | — | Virtuelle Folien. Siehe Virtual-Parameter. |
| `virtualTranslate` | `boolean` | `false` | Swiper funktioniert normal, bewegt sich aber nicht physisch. |
| `watchOverflow` | `boolean` | `true` | Navigation/Scrollbar ausblenden wenn zu wenige Folien. |
| `watchSlidesProgress` | `boolean` | `false` | Progress und Sichtbarkeit jeder Folie berechnen. |
| `width` | `number \| null` | `null` | Swiper-Breite in px erzwingen. |
| `wrapperClass` | `string` | `'swiper-wrapper'` | CSS-Klasse des Wrappers. |
| `zoom` | `boolean \| ZoomOptions` | — | Zoom-Funktion. Siehe Zoom-Parameter. |

---

## 2. Breakpoints

```js
const swiper = new Swiper('.swiper', {
  slidesPerView: 1,
  spaceBetween: 10,
  breakpoints: {
    // ab 640px
    640: { slidesPerView: 2, spaceBetween: 20 },
    // ab 768px
    768: { slidesPerView: 3, spaceBetween: 30 },
    // ab 1024px
    1024: { slidesPerView: 4, spaceBetween: 40 },
  },
});
```

---

## 3. Navigation-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `navigation.addIcons` | `boolean` | `true` | SVG-Icons automatisch zu Navigations-Buttons hinzufügen. |
| `navigation.disabledClass` | `string` | `'swiper-button-disabled'` | CSS-Klasse wenn Button deaktiviert. |
| `navigation.enabled` | `boolean` | — | Für Breakpoints: Navigation aktivieren/deaktivieren. |
| `navigation.hiddenClass` | `string` | `'swiper-button-hidden'` | CSS-Klasse wenn Button versteckt. |
| `navigation.hideOnClick` | `boolean` | `false` | Navigation nach Klick auf Slider verstecken/zeigen. |
| `navigation.lockClass` | `string` | `'swiper-button-lock'` | CSS-Klasse wenn Navigation gesperrt ist. |
| `navigation.navigationDisabledClass` | `string` | `'swiper-navigation-disabled'` | Container-Klasse wenn Navigation deaktiviert. |
| `navigation.nextEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS-Selektor oder HTMLElement für Weiter-Button. |
| `navigation.prevEl` | `HTMLElement \| CSSSelector \| null` | `null` | CSS-Selektor oder HTMLElement für Zurück-Button. |

---

## 4. Pagination-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `pagination.bulletActiveClass` | `string` | `'swiper-pagination-bullet-active'` | CSS-Klasse des aktiven Bullets. |
| `pagination.bulletClass` | `string` | `'swiper-pagination-bullet'` | CSS-Klasse eines Bullets. |
| `pagination.bulletElement` | `string` | `'span'` | HTML-Tag für Bullets. |
| `pagination.clickable` | `boolean` | `false` | Klick auf Bullet navigiert zur Folie. |
| `pagination.clickableClass` | `string` | `'swiper-pagination-clickable'` | Klasse wenn Pagination klickbar. |
| `pagination.currentClass` | `string` | `'swiper-pagination-current'` | Klasse des aktuellen Fraction-Elements. |
| `pagination.dynamicBullets` | `boolean` | `false` | Nur wenige Bullets sichtbar bei vielen Folien. |
| `pagination.dynamicMainBullets` | `number` | `1` | Anzahl sichtbarer Haupt-Bullets bei `dynamicBullets`. |
| `pagination.el` | `HTMLElement \| CSSSelector \| null` | `null` | CSS-Selektor oder HTMLElement der Pagination. |
| `pagination.enabled` | `boolean` | — | Für Breakpoints. |
| `pagination.formatFractionCurrent` | `function(number)` | — | Fraction-Zähler formatieren. |
| `pagination.formatFractionTotal` | `function(number)` | — | Fraction-Gesamtzahl formatieren. |
| `pagination.hiddenClass` | `string` | `'swiper-pagination-hidden'` | Klasse wenn Pagination inaktiv. |
| `pagination.hideOnClick` | `boolean` | `true` | Pagination nach Klick auf Slider ausblenden. |
| `pagination.horizontalClass` | `string` | `'swiper-pagination-horizontal'` | Klasse bei horizontalem Swiper. |
| `pagination.lockClass` | `string` | `'swiper-pagination-lock'` | Klasse wenn Pagination deaktiviert. |
| `pagination.modifierClass` | `string` | `'swiper-pagination-'` | Präfix der Modifier-CSS-Klasse. |
| `pagination.paginationDisabledClass` | `string` | `'swiper-pagination-disabled'` | Container-Klasse wenn Pagination deaktiviert. |
| `pagination.progressbarFillClass` | `string` | `'swiper-pagination-progressbar-fill'` | CSS-Klasse des Progressbar-Füll-Elements. |
| `pagination.progressbarOpposite` | `boolean` | `false` | Progressbar entgegengesetzt zur Slider-Richtung. |
| `pagination.progressbarOppositeClass` | `string` | `'swiper-pagination-progressbar-opposite'` | Klasse der gegenüberliegenden Progressbar. |
| `pagination.renderBullet` | `function(index, className)` | `null` | Bullets individuell rendern. |
| `pagination.renderCustom` | `function(swiper, current, total)` | `null` | Pflicht bei `type: 'custom'`. |
| `pagination.renderFraction` | `function(currentClass, totalClass)` | `null` | Fraction-Pagination individuell rendern. |
| `pagination.renderProgressbar` | `function(progressbarFillClass)` | `null` | Progressbar individuell rendern. |
| `pagination.totalClass` | `string` | `'swiper-pagination-total'` | Klasse des Gesamt-Anzahl-Elements. |
| `pagination.type` | `'bullets' \| 'fraction' \| 'progressbar' \| 'custom'` | `'bullets'` | Pagination-Typ. |
| `pagination.verticalClass` | `string` | `'swiper-pagination-vertical'` | Klasse bei vertikalem Swiper. |

---

## 5. Scrollbar-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `scrollbar.dragClass` | `string` | `'swiper-scrollbar-drag'` | CSS-Klasse des Scrollbar-Drag-Elements. |
| `scrollbar.dragSize` | `number \| 'auto'` | `'auto'` | Größe des Drag-Elements in px. |
| `scrollbar.draggable` | `boolean` | `false` | Scrollbar ist ziehbar. |
| `scrollbar.el` | `HTMLElement \| CSSSelector \| null` | `null` | CSS-Selektor oder HTMLElement der Scrollbar. |
| `scrollbar.enabled` | `boolean` | — | Für Breakpoints. |
| `scrollbar.hide` | `boolean` | `true` | Scrollbar nach Interaktion automatisch ausblenden. |
| `scrollbar.horizontalClass` | `string` | `'swiper-scrollbar-horizontal'` | Klasse bei horizontalem Swiper. |
| `scrollbar.lockClass` | `string` | `'swiper-scrollbar-lock'` | Klasse wenn Scrollbar deaktiviert. |
| `scrollbar.scrollbarDisabledClass` | `string` | `'swiper-scrollbar-disabled'` | Container-Klasse wenn Scrollbar deaktiviert. |
| `scrollbar.snapOnRelease` | `boolean` | `false` | Einrasten auf Folie beim Loslassen. |
| `scrollbar.verticalClass` | `string` | `'swiper-scrollbar-vertical'` | Klasse bei vertikalem Swiper. |

---

## 6. Autoplay-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `autoplay.delay` | `number` | `3000` | Pause zwischen Transitionen in ms. |
| `autoplay.disableOnInteraction` | `boolean` | `true` | `false` = Autoplay läuft nach Benutzer-Interaktion weiter. |
| `autoplay.pauseOnMouseEnter` | `boolean` | `false` | Autoplay pausiert beim Hover. |
| `autoplay.reverseDirection` | `boolean` | `false` | Autoplay in Rückwärtsrichtung. |
| `autoplay.stopOnLastSlide` | `boolean` | `false` | Autoplay stoppt bei letzter Folie. |
| `autoplay.waitForTransition` | `boolean` | `true` | Autoplay wartet auf Wrapper-Transition. |

---

## 7. FreeMode-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `freeMode.enabled` | `boolean` | `false` | Free-Mode aktivieren. |
| `freeMode.minimumVelocity` | `number` | `0.02` | Mindest-Wisch-Geschwindigkeit für Momentum. |
| `freeMode.momentum` | `boolean` | `true` | Folie gleitet nach dem Loslassen weiter. |
| `freeMode.momentumBounce` | `boolean` | `true` | `false` = Kein Bounce am Rand. |
| `freeMode.momentumBounceRatio` | `number` | `1` | Bounce-Stärke. |
| `freeMode.momentumRatio` | `number` | `1` | Momentum-Distanz-Multiplikator. |
| `freeMode.momentumVelocityRatio` | `number` | `1` | Momentum-Geschwindigkeits-Multiplikator. |
| `freeMode.sticky` | `boolean` | `false` | An Folien-Positionen einrasten (Free-Mode + Snap). |

---

## 8. Grid-Parameter (Multirow)

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `grid.fill` | `'row' \| 'column'` | `'column'` | Befüllungsrichtung: spalten- oder zeilenweise. |
| `grid.rows` | `number` | `1` | Anzahl der Zeilen. |

```js
// Beispiel: 2 Zeilen, 3 Spalten
const swiper = new Swiper('.swiper', {
  modules: [Grid],
  grid: { rows: 2, fill: 'row' },
  slidesPerView: 3,
  spaceBetween: 20,
});
```

---

## 9. Fade-Effekt-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `fadeEffect.crossFade` | `boolean` | `false` | Cross-Fade aktivieren (ausblenden + einblenden gleichzeitig). |

---

## 10. Coverflow-Effekt-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `coverflowEffect.depth` | `number` | `100` | Tiefenversatz in px (Z-Achse). |
| `coverflowEffect.modifier` | `number` | `1` | Effekt-Multiplikator. |
| `coverflowEffect.rotate` | `number` | `50` | Rotation in Grad. |
| `coverflowEffect.scale` | `number` | `1` | Skalierungs-Effekt. |
| `coverflowEffect.slideShadows` | `boolean` | `true` | Folien-Schatten aktivieren. |
| `coverflowEffect.stretch` | `number` | `0` | Zusätzlicher Abstand zwischen Folien. |

---

## 11. Flip-Effekt-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `flipEffect.limitRotation` | `boolean` | `true` | Rotation der Rand-Folien begrenzen. |
| `flipEffect.slideShadows` | `boolean` | `true` | Folien-Schatten aktivieren. |

---

## 12. Cube-Effekt-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `cubeEffect.shadow` | `boolean` | `true` | Haupt-Slider-Schatten. |
| `cubeEffect.shadowOffset` | `number` | `20` | Schatten-Offset in px. |
| `cubeEffect.shadowScale` | `number` | `0.94` | Schatten-Skalierungsverhältnis. |
| `cubeEffect.slideShadows` | `boolean` | `true` | Folien-Schatten aktivieren. |

---

## 13. Cards-Effekt-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `cardsEffect.perSlideOffset` | `number` | `8` | Versatz pro Folie in px. |
| `cardsEffect.perSlideRotate` | `number` | `2` | Rotation pro Folie in Grad. |
| `cardsEffect.rotate` | `boolean` | `true` | Cards-Rotation aktivieren. |
| `cardsEffect.slideShadows` | `boolean` | `true` | Folien-Schatten aktivieren. |

---

## 14. Creative-Effekt-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `creativeEffect.limitProgress` | `number` | `1` | Fortschritt/Offset auf Seiten-Folien begrenzen. |
| `creativeEffect.next` | `CreativeEffectTransform` | — | Transformationen der nächsten Folie. |
| `creativeEffect.perspective` | `boolean` | `true` | 3D-Transformationen aktivieren. |
| `creativeEffect.prev` | `CreativeEffectTransform` | — | Transformationen der vorherigen Folie. |
| `creativeEffect.progressMultiplier` | `number` | `1` | Transformations- und Opacity-Multiplikator. |
| `creativeEffect.shadowPerProgress` | `boolean` | `false` | Schatten-Opacity pro Folie aufteilen. |

---

## 15. Thumbs-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `thumbs.autoScrollOffset` | `number` | `0` | Ab wie vielen Folien vom Rand der aktive Thumb gescrollt wird. |
| `thumbs.multipleActiveThumbs` | `boolean` | `true` | Mehrere Thumbs gleichzeitig aktiv möglich. |
| `thumbs.slideThumbActiveClass` | `string` | `'swiper-slide-thumb-active'` | Klasse des aktiven Thumb-Slides. |
| `thumbs.swiper` | `string \| Swiper \| null` | `null` | Swiper-Instanz oder CSS-Selektor des Thumbs-Swipers. |
| `thumbs.thumbsContainerClass` | `string` | `'swiper-thumbs'` | Klasse des Thumbs-Containers. |

---

## 16. Zoom-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `zoom.containerClass` | `string` | `'swiper-zoom-container'` | CSS-Klasse des Zoom-Containers. |
| `zoom.limitToOriginalSize` | `boolean` | `false` | Bild nicht über 100% skalieren. |
| `zoom.maxRatio` | `number` | `3` | Maximaler Zoom-Faktor. |
| `zoom.minRatio` | `number` | `1` | Minimaler Zoom-Faktor. |
| `zoom.panOnMouseMove` | `boolean` | `false` | Gezoomtes Bild folgt Mausbewegung. |
| `zoom.toggle` | `boolean` | `true` | Doppeltippen zum Zoomen aktivieren. |
| `zoom.zoomedSlideClass` | `string` | `'swiper-slide-zoomed'` | Klasse der gezoomten Folie. |

---

## 17. Keyboard-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `keyboard.enabled` | `boolean` | `false` | Tastatursteuerung aktivieren. |
| `keyboard.onlyInViewport` | `boolean` | `true` | Nur steuern wenn Swiper im Viewport sichtbar. |
| `keyboard.pageUpDown` | `boolean` | `true` | Page-Up/Down-Tasten aktivieren. |
| `keyboard.speed` | `number` | `undefined` | Geschwindigkeit der Tastatur-Navigation in ms. |

---

## 18. Mousewheel-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `mousewheel.enabled` | `boolean` | `false` | Mausrad-Steuerung aktivieren. |
| `mousewheel.eventsTarget` | `HTMLElement \| 'container' \| 'wrapper' \| CSSSelector` | `'container'` | Element das Mausrad-Events empfängt. |
| `mousewheel.forceToAxis` | `boolean` | `false` | Mausrad-Bewegung auf Slider-Achse erzwingen. |
| `mousewheel.invert` | `boolean` | `false` | Richtung invertieren. |
| `mousewheel.noMousewheelClass` | `string` | `'swiper-no-mousewheel'` | Elemente mit dieser Klasse ignorieren Mausrad. |
| `mousewheel.releaseOnEdges` | `boolean` | `false` | Mausrad an Rändern freigeben (Seiten-Scroll). |
| `mousewheel.sensitivity` | `number` | `1` | Mausrad-Sensitivitäts-Multiplikator. |
| `mousewheel.thresholdDelta` | `number \| null` | `null` | Mindestwert des Scroll-Delta für Folienwechsel. |
| `mousewheel.thresholdTime` | `number \| null` | `null` | Mindest-Zeit-Delta (ms) für Folienwechsel. |

---

## 19. Virtual Slides-Parameter

| Parameter | Typ | Default | Beschreibung |
|---|---|---|---|
| `virtual.addSlidesAfter` | `number` | `0` | Zusätzliche vorgerenderte Folien nach aktiver. |
| `virtual.addSlidesBefore` | `number` | `0` | Zusätzliche vorgerenderte Folien vor aktiver. |
| `virtual.cache` | `boolean` | `true` | DOM-Cache der gerenderten Folien. |
| `virtual.enabled` | `boolean` | `false` | Virtuelle Folien aktivieren. |
| `virtual.renderExternal` | `function(VirtualData)` | `null` | Externes Rendering (z.B. React/Vue). |

```js
// Virtual Slides Beispiel
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

*Quelle: https://swiperjs.com/swiper-api*
