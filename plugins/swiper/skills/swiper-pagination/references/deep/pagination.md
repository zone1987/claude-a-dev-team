# Swiper Pagination-Modul — Vollständige Referenz

## Import & Aktivierung

```js
import Swiper from 'swiper';
import { Pagination } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';

const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
  },
});
```

## HTML-Struktur

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
  </div>
  <div class="swiper-pagination"></div>
</div>
```

## Parameter (vollständig)

| Name | Typ | Default | Beschreibung |
|------|-----|---------|--------------|
| `el` | `HTMLElement \| CSSSelector \| null` | `null` | Container-Element oder Selektor |
| `type` | `string` | `'bullets'` | Pagination-Typ: `'bullets'`, `'fraction'`, `'progressbar'`, `'custom'` |
| `clickable` | `boolean` | `false` | Slides per Klick auf Bullets wechseln (nur bullets-Typ) |
| `dynamicBullets` | `boolean` | `false` | Nur begrenzte Bullets zeigen bei vielen Slides |
| `dynamicMainBullets` | `number` | `1` | Anzahl sichtbarer Haupt-Bullets im dynamischen Modus |
| `hideOnClick` | `boolean` | `true` | Pagination beim Klick auf Container ein-/ausblenden |
| `enabled` | `boolean` | — | Pagination für bestimmte Breakpoints aktivieren/deaktivieren |
| `bulletClass` | `string` | `'swiper-pagination-bullet'` | CSS-Klasse für einzelne Bullets |
| `bulletActiveClass` | `string` | `'swiper-pagination-bullet-active'` | CSS-Klasse für den aktiven Bullet |
| `bulletElement` | `string` | `'span'` | HTML-Tag für Bullets |
| `clickableClass` | `string` | `'swiper-pagination-clickable'` | Klasse wenn Pagination anklickbar |
| `currentClass` | `string` | `'swiper-pagination-current'` | Klasse für aktuellen Index (fraction) |
| `totalClass` | `string` | `'swiper-pagination-total'` | Klasse für Gesamtanzahl (fraction) |
| `hiddenClass` | `string` | `'swiper-pagination-hidden'` | Klasse wenn Pagination versteckt |
| `horizontalClass` | `string` | `'swiper-pagination-horizontal'` | Klasse bei horizontaler Ausrichtung |
| `verticalClass` | `string` | `'swiper-pagination-vertical'` | Klasse bei vertikaler Ausrichtung |
| `lockClass` | `string` | `'swiper-pagination-lock'` | Klasse wenn Pagination gesperrt |
| `modifierClass` | `string` | `'swiper-pagination-'` | CSS-Klassen-Präfix |
| `paginationDisabledClass` | `string` | `'swiper-pagination-disabled'` | Klasse am Container wenn deaktiviert |
| `progressbarFillClass` | `string` | `'swiper-pagination-progressbar-fill'` | Klasse für Progressbar-Füllbalken |
| `progressbarOpposite` | `boolean` | `false` | Progressbar-Richtung umkehren |
| `progressbarOppositeClass` | `string` | `'swiper-pagination-progressbar-opposite'` | Klasse für Gegenrichtungs-Progressbar |
| `renderBullet` | `function(index, className)` | `null` | Benutzerdefiniertes Bullet-Rendering |
| `renderFraction` | `function(currentClass, totalClass)` | `null` | Benutzerdefiniertes Fraction-Rendering |
| `renderProgressbar` | `function(progressbarFillClass)` | `null` | Benutzerdefiniertes Progressbar-Rendering |
| `renderCustom` | `function(swiper, current, total)` | `null` | Pflicht bei `type: 'custom'` |
| `formatFractionCurrent` | `function(number)` | — | Aktuellen Index formatieren |
| `formatFractionTotal` | `function(number)` | — | Gesamtanzahl formatieren |

## Render-Funktions-Signaturen

### renderBullet
```js
pagination: {
  renderBullet: function (index, className) {
    // index: 0-basierter Slide-Index
    // className: 'swiper-pagination-bullet' (+ aktiv-Klasse automatisch)
    return '<span class="' + className + '">' + (index + 1) + '</span>';
  },
}
```

### renderFraction
```js
pagination: {
  type: 'fraction',
  renderFraction: function (currentClass, totalClass) {
    return '<span class="' + currentClass + '"></span>' +
           ' / ' +
           '<span class="' + totalClass + '"></span>';
  },
}
```

### renderProgressbar
```js
pagination: {
  type: 'progressbar',
  renderProgressbar: function (progressbarFillClass) {
    return '<span class="' + progressbarFillClass + '"></span>';
  },
}
```

### renderCustom
```js
pagination: {
  type: 'custom',
  renderCustom: function (swiper, current, total) {
    return current + ' von ' + total;
  },
}
```

### formatFractionCurrent / formatFractionTotal
```js
pagination: {
  type: 'fraction',
  formatFractionCurrent: (number) => String(number).padStart(2, '0'),
  formatFractionTotal: (number) => String(number).padStart(2, '0'),
}
```

## Properties

| Property | Typ | Beschreibung |
|----------|-----|--------------|
| `swiper.pagination.el` | `HTMLElement` | Container-Element |
| `swiper.pagination.bullets` | `HTMLElement[]` | Array aller Bullet-Elemente |

## Methoden

| Methode | Beschreibung |
|---------|--------------|
| `swiper.pagination.init()` | Pagination initialisieren |
| `swiper.pagination.destroy()` | Pagination entfernen |
| `swiper.pagination.render()` | Pagination-Layout neu rendern |
| `swiper.pagination.update()` | Pagination-Status aktualisieren |

## Events

| Event | Argumente | Beschreibung |
|-------|-----------|--------------|
| `paginationRender` | `(swiper, paginationEl)` | Nach dem Rendern |
| `paginationUpdate` | `(swiper, paginationEl)` | Nach dem Aktualisieren |
| `paginationShow` | `(swiper)` | Pagination eingeblendet |
| `paginationHide` | `(swiper)` | Pagination ausgeblendet |

## CSS Custom Properties

```css
:root {
  --swiper-pagination-color: var(--swiper-theme-color);
  --swiper-pagination-left: auto;
  --swiper-pagination-right: 8px;
  --swiper-pagination-bottom: 8px;
  --swiper-pagination-top: auto;
  --swiper-pagination-fraction-color: inherit;
  --swiper-pagination-progressbar-bg-color: rgba(0, 0, 0, 0.25);
  --swiper-pagination-progressbar-size: 4px;
  --swiper-pagination-bullet-size: 8px;
  --swiper-pagination-bullet-width: 8px;
  --swiper-pagination-bullet-height: 8px;
  --swiper-pagination-bullet-inactive-color: #000;
  --swiper-pagination-bullet-inactive-opacity: 0.2;
  --swiper-pagination-bullet-opacity: 1;
  --swiper-pagination-bullet-horizontal-gap: 4px;
  --swiper-pagination-bullet-vertical-gap: 6px;
}
```

## Komplettbeispiele

### Fraction-Pagination mit Null-Padding
```js
const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    type: 'fraction',
    formatFractionCurrent: (n) => String(n).padStart(2, '0'),
    formatFractionTotal: (n) => String(n).padStart(2, '0'),
  },
});
```

### Nummerierte Bullets
```js
const swiper = new Swiper('.swiper', {
  modules: [Pagination],
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    renderBullet: (index, className) =>
      `<span class="${className}">${index + 1}</span>`,
  },
});
```

---
Quelle: https://swiperjs.com/swiper-api#pagination
