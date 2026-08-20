# flatpickr — Getting Started (complete reference, v4.6.13)

## Contents

- [Version](#version)
- [Installation](#installation)
- [Module import](#module-import)
- [Initialization — all variants](#initialization--all-variants)
- [Configuration parameters](#configuration-parameters)
- [Supported input types](#supported-input-types)
- [Return value](#return-value)
- [TypeScript](#typescript)
- [Browser compatibility](#browser-compatibility)

## Version

**flatpickr v4.6.13** (current stable version)

## Installation

### npm

```bash
npm i flatpickr --save
# Installs v4.6.13 (current stable)
```

### CDN (jsDelivr)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
```

### CDN (npmcdn / unpkg)

```html
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/flatpickr.min.css">
<script src="https://npmcdn.com/flatpickr"></script>
```

## Module import

```js
// ES Modules (recommended for TypeScript / Webpack / Vite)
import flatpickr from "flatpickr";

// CommonJS (Node / older bundlers)
const flatpickr = require("flatpickr");
```

**CSS in Webpack/bundlers:**

```js
import "flatpickr/dist/flatpickr.min.css";
// or for a theme:
import "flatpickr/dist/themes/dark.css";
```

## Initialization — all variants

### 1. ID selector (string)

```js
flatpickr("#myID", {});
```

### 2. CSS class selector — several instances at once

```js
flatpickr(".datepicker", {});
// Returns an array of flatpickr instances
```

### 3. Pass a DOM element directly (recommended for frameworks)

```js
const el = document.getElementById("myDate");
flatpickr(el, { enableTime: true });
```

### 4. NodeList

```js
const inputs = document.querySelectorAll(".date-input");
flatpickr(inputs, { dateFormat: "d.m.Y" });
```

### 5. jQuery plugin

```js
$(".selector").flatpickr({ /* options */ });
```

> Note: with framework integrations (React, Vue, Angular) always pass the DOM element directly, not a string selector.

## Configuration parameters

All options are optional. The second argument `{}` can be omitted entirely:

```js
flatpickr("#date");                      // no options
flatpickr("#date", { inline: true });   // with options
```

The complete options reference: see [flatpickr-options](OPTIONS.md).

## Supported input types

flatpickr works with all standard HTML inputs and also with non-input elements:

```html
<!-- Standard text input -->
<input type="text" id="date1" placeholder="Choose a date">

<!-- Value already prefilled -->
<input type="text" id="date2" value="2024-01-15">

<!-- Inline on a div -->
<div id="inline-calendar"></div>
```

```js
flatpickr("#date1", {});
flatpickr("#date2", { dateFormat: "Y-m-d" });
flatpickr("#inline-calendar", { inline: true });
```

## Return value

`flatpickr()` returns a flatpickr instance (or an array of them for a multi-element selection):

```js
const fp = flatpickr("#myDate", { enableTime: true });

// Later:
fp.open();
fp.setDate("2024-06-15");
fp.destroy();
```

## TypeScript

flatpickr ships its own type declarations (no `@types` needed):

```ts
import flatpickr from "flatpickr";
import { Instance } from "flatpickr/dist/types/instance";
import { Options } from "flatpickr/dist/types/options";

const opts: Options = {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
};

const fp: Instance = flatpickr("#myDate", opts) as Instance;
```

## Browser compatibility

| Browser | Supported |
|---------|------------|
| Chrome | yes |
| Firefox | yes |
| Safari 6+ | yes |
| IE 10+ | yes |
| IE 9 | with polyfill (classList) |

For IE9 details: see [flatpickr-migration](MIGRATION.md).

---

Source: `package.json` v4.6.13 | https://flatpickr.js.org/getting-started/ | https://flatpickr.js.org/
