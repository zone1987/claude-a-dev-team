# flatpickr — Migration and browser compatibility (complete reference)

## Contents

- [Updating from v2 → v3+](#updating-from-v2-v3)
- [IE9 support](#ie9-support)
- [Browser compatibility matrix](#browser-compatibility-matrix)
- [Changelog — important changes](#changelog--important-changes)

## Updating from v2 → v3+

### Breaking change 1: `utc` option removed

**Problem:** The former `utc: true` option produced incorrect timezone data.

**Before (v2):**

```js
flatpickr("#date", { utc: true });
```

**After (v3+):**

```js
// Recommended: ISO format with timezone
flatpickr("#date", {
  dateFormat: "Z",          // ISO 8601: "2024-12-31T14:30:00.000Z"
  altInput: true,
  altFormat: "F j, Y H:i"  // Human-readable for the user
});

// If the old dateFormat option already contained "Z" — escape it:
flatpickr("#date", {
  dateFormat: "dHi\\Z M y"  // "Z" as a literal, not as the ISO token
});
```

**Advantages of the ISO format:**
- Correct timezone information
- Broad database support (MySQL, PostgreSQL, etc.)
- Standards-compliant (ISO 8601)

### Breaking change 2: constructor unified

**Before (v2):**

```js
// Element
new Flatpickr(element, config);

// Configuration
Flatpickr.defaultConfig.dateFormat = "Y-m-d";
```

**After (v3+):**

```js
// For module users (Webpack etc.) — no change needed
flatpickr(element, config);

// For script-tag users — a simple find & replace:
// "Flatpickr" → "flatpickr" (everywhere)
flatpickr.defaultConfig.dateFormat = "Y-m-d";
```

**Migration for script-tag users:**

A simple search & replace: `Flatpickr` → `flatpickr` (case-sensitive)

Affects:
- `new Flatpickr()` → `flatpickr()`
- `Flatpickr.defaultConfig` → `flatpickr.defaultConfig`
- All other `Flatpickr` references

---

## IE9 support

flatpickr runs out of the box in **IE10+, Safari 6+, Firefox and Chrome**.

IE9 support requires two steps:

### Step 1: classList polyfill

```bash
npm install classlist-polyfill
```

```js
// Load it in the entry file (before flatpickr)
import "classlist-polyfill";
import flatpickr from "flatpickr";
```

Or via CDN:

```html
<script src="https://npmcdn.com/classlist-polyfill"></script>
```

### Step 2: IE9-specific CSS

```html
<!--[if IE 9]>
<link rel="stylesheet" type="text/css" href="https://npmcdn.com/flatpickr/dist/ie.css">
<![endif]-->
```

Or via npm:

```css
/* In an IE9-specific build */
@import "flatpickr/dist/ie.css";
```

### Webpack + html-webpack-plugin

For conditional stylesheets with bundlers: [html-webpack-plugin Issue #155](https://github.com/jantimon/html-webpack-plugin/issues/155)

---

## Browser compatibility matrix

| Browser | Version | Supported | Note |
|---------|---------|------------|-----------|
| Chrome | all modern | yes | — |
| Firefox | all modern | yes | — |
| Safari | 6+ | yes | — |
| Edge | all | yes | — |
| IE | 10+ | yes | — |
| IE | 9 | with polyfill | classList polyfill + ie.css |
| IE | < 9 | no | — |
| iOS Safari | all | yes | native picker on touch devices |
| Android Chrome | all | yes | native picker on touch devices |

---

## Changelog — important changes

### v4.x
- `onKeyDown` hook added
- `onParseConfig` hook added
- `showMonths` option for showing several months at once
- `monthSelectorType` option (`dropdown` or `static`)
- Improved accessibility (ARIA)

### v3.0
- `utc` option removed (→ `dateFormat: "Z"`)
- `Flatpickr` → `flatpickr` unified
- Plugin system introduced
- Extended localization

---

Source: https://flatpickr.js.org/updating-from-v2/ | https://flatpickr.js.org/ie9/
