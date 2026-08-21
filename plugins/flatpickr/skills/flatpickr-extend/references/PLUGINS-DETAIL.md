# flatpickr — Plugins (complete reference, v4.6.13)

Source: `src/plugins/*` (8 plugins, as of v4.6.13).

## Contents

- [Plugin concept](#plugin-concept)
- [1. confirmDatePlugin](#1-confirmdateplugin)
- [2. rangePlugin (beta)](#2-rangeplugin-beta)
- [3. weekSelect](#3-weekselect)
- [4. monthSelectPlugin](#4-monthselectplugin)
- [5. minMaxTimePlugin (beta)](#5-minmaxtimeplugin-beta)
- [6. scrollPlugin](#6-scrollplugin)
- [7. momentPlugin](#7-momentplugin)
- [8. labelPlugin](#8-labelplugin)
- [Writing your own plugin](#writing-your-own-plugin)

## Plugin concept

Plugins are functions that receive an optional configuration and the flatpickr instance
and return an object of hook functions. They are passed in the `plugins` array.

```typescript
type Plugin<E = {}> = (fp: Instance & E) => Options;
```

```js
flatpickr("#date", {
  plugins: [pluginA(configA), pluginB()]
});
```

---

## 1. confirmDatePlugin

Shows a confirmation button after the user has selected date+time or multiple dates.
Prevents the calendar from closing unintentionally.

### Import

```js
// ES module
import confirmDatePlugin from "flatpickr/dist/plugins/confirmDate/confirmDate.js";
import "flatpickr/dist/plugins/confirmDate/confirmDate.css";

// Browser
// <script src="https://npmcdn.com/flatpickr/dist/plugins/confirmDate/confirmDate.js"></script>
// <link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/plugins/confirmDate/confirmDate.css">
```

### Config interface (`src/plugins/confirmDate/confirmDate.ts`)

```typescript
interface Config {
  confirmIcon?: string;   // default: SVG check mark
  confirmText?: string;   // default: "OK "
  showAlways?: boolean;   // default: false
  theme?: string;         // default: "light"
}
```

### Configuration options

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `confirmIcon` | `String` | SVG check mark | HTML for the confirmation icon |
| `confirmText` | `String` | `"OK "` | text of the confirmation button |
| `showAlways` | `Boolean` | `false` | keep the button always visible (not only after a selection) |
| `theme` | `String` | `"light"` | CSS theme: `"light"` or `"dark"` |

### Usage

```js
flatpickr("#date", {
  enableTime: true,
  plugins: [confirmDatePlugin({
    confirmIcon: "<i class='fa fa-check'></i>",
    confirmText: "Confirm",
    showAlways: false,
    theme: "light"
  })]
});

// simplest form
flatpickr("#date", {
  enableTime: true,
  plugins: [confirmDatePlugin({})]
});

// with multiple mode
flatpickr("#date", {
  mode: "multiple",
  plugins: [confirmDatePlugin({ confirmText: "OK" })]
});
```

### Behavior

- Appears after date+time selection, in `multiple` mode or with the `monthSelect` plugin
- Always visible with `showAlways: true`
- Tab from the last time element jumps to the confirmation button
- Enter on the button closes the calendar
- Inactive with `noCalendar: true` or in mobile mode

---

## 2. rangePlugin (beta)

Enables date range selection with **two separate input fields** (instead of one combined field).

### Import

```js
import rangePlugin from "flatpickr/dist/plugins/rangePlugin.js";
```

### Config interface (`src/plugins/rangePlugin.ts`)

```typescript
interface Config {
  input?: string | HTMLInputElement;  // selector or element for the second input
  position?: "left";                  // positioning of the picker
}
```

### Configuration options

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `input` | `String\|HTMLInputElement` | — | CSS selector or element for the second input field; if missing, a cloned input is inserted |
| `position` | `String` | — | `"left"`: the picker opens relative to the first input even when the second one has focus |

### Usage

```html
<input id="rangeStart" type="text" placeholder="From">
<input id="rangeEnd" type="text" placeholder="To">
```

```js
flatpickr("#rangeStart", {
  plugins: [rangePlugin({ input: "#rangeEnd" })]
});
```

### Behavior

- The first input holds the start date, the second one the end date
- Clicking the second input opens the picker and jumps to the end date already selected
- Sets `fp.config.mode = "range"` automatically
- More form-friendly than `mode: "range"` (two separate values)
- Supports `allowInput: true`

---

## 3. weekSelect

Enables the selection of a whole week. No configuration parameters.

### Import

```js
import weekSelectPlugin from "flatpickr/dist/plugins/weekSelect/weekSelect.js";
```

### Config interface

No config interface — the plugin takes no parameters.

### Usage

```js
flatpickr("#date", {
  plugins: [weekSelectPlugin()],
  onChange: function() {
    const weekNumber = this.selectedDates[0]
      ? this.config.getWeek(this.selectedDates[0])
      : null;
    console.log("Selected week:", weekNumber);
  }
});
```

### Instance extensions (PlusWeeks)

```typescript
type PlusWeeks = {
  weekStartDay: Date;  // first day of the selected week
  weekEndDay: Date;    // last day of the selected week
};
```

```js
console.log(fp.weekStartDay); // Monday of the selected week
console.log(fp.weekEndDay);   // Sunday of the selected week
```

### Behavior

- Hovering a day highlights the whole week (`inRange` class)
- A click selects all 7 days of the week
- Sets `fp.config.mode = "single"` and `fp.config.enableTime = false` automatically
- `dateFormat` default: `"\\W\\e\\e\\k #W, Y"` (e.g. "Week #24, 2024")

---

## 4. monthSelectPlugin

Shows a month selection — no day selection.

### Import

```js
import monthSelectPlugin from "flatpickr/dist/plugins/monthSelect/index.js";
import "flatpickr/dist/plugins/monthSelect/style.css";
```

### Config interface (`src/plugins/monthSelect/index.ts`)

```typescript
interface Config {
  shorthand: boolean;    // default: false
  dateFormat: string;    // default: "F Y"
  altFormat: string;     // default: "F Y"
  theme: string;         // default: "light"
}
```

### Configuration options

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `shorthand` | `Boolean` | `false` | month names in short form (`Jan` instead of `January`) |
| `dateFormat` | `String` | `"F Y"` | format of the value in the input |
| `altFormat` | `String` | `"F Y"` | display format (when `altInput: true`) |
| `theme` | `String` | `"light"` | CSS theme: `"light"` or `"dark"` |

### Usage

```js
flatpickr("#month", {
  plugins: [
    monthSelectPlugin({
      shorthand: true,        // "Jan 2024" instead of "January 2024"
      dateFormat: "m.y",      // "01.24"
      altFormat: "F Y",       // "January 2024"
      theme: "dark"
    })
  ]
});

// simplest form
flatpickr("#month", {
  plugins: [monthSelectPlugin()]
});
```

### Behavior

- Shows an overview of the 12 months (no calendar with individual days)
- Always selects the first day of the selected month
- Sets `fp.config.enableTime = false` automatically
- The arrows in the header navigate through the years
- Compatible with `altInput: true`, `mode: "range"`, `mode: "multiple"`
- CSS class: `flatpickr-monthSelect-theme-${theme}` on `calendarContainer`

---

## 5. minMaxTimePlugin (beta)

Allows individual time limits per date — different min/max times for different days.

### Import

```js
import minMaxTimePlugin from "flatpickr/dist/plugins/minMaxTimePlugin.js";
```

### Config interface (`src/plugins/minMaxTimePlugin.ts`)

```typescript
interface MinMaxTime {
  minTime?: string;
  maxTime?: string;
}

interface Config {
  table?: Record<string, MinMaxTime>;        // static table: date key → time limits
  getTimeLimits?: (date: Date) => MinMaxTime; // dynamic function
  tableDateFormat?: string;                  // default: "Y-m-d"
}
```

### Configuration options

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `table` | `Object` | — | object with date strings as keys and `{minTime, maxTime}` as values |
| `getTimeLimits` | `Function` | — | function `(date: Date) => {minTime, maxTime}` for dynamic limits |
| `tableDateFormat` | `String` | `"Y-m-d"` | format of the date keys in the `table` object |

### Usage

```js
// with a static table
flatpickr("#date", {
  enableTime: true,
  plugins: [
    minMaxTimePlugin({
      table: {
        "2025-01-10": { minTime: "16:00", maxTime: "22:00" },
        "2025-01-15": { minTime: "09:00", maxTime: "12:00" },
        "2025-01-20": { minTime: "00:00", maxTime: "23:59" }
      }
    })
  ]
});

// with a dynamic function
flatpickr("#date", {
  enableTime: true,
  plugins: [
    minMaxTimePlugin({
      getTimeLimits: function(date) {
        // different times on weekdays than on the weekend
        if (date.getDay() === 0 || date.getDay() === 6) {
          return { minTime: "10:00", maxTime: "18:00" };
        }
        return { minTime: "09:00", maxTime: "20:00" };
      }
    })
  ]
});
```

### Behavior

- Use either `table` OR `getTimeLimits` (not both)
- When no entry exists for a selected date, the instance's global `minTime`/`maxTime` are used
- Time limits may also cross midnight (`minTime > maxTime`)

---

## 6. scrollPlugin

Enables mouse wheel navigation for time and month elements. No configuration parameters.

### Import

```js
import scrollPlugin from "flatpickr/dist/plugins/scrollPlugin.js";
```

### Config interface

No config interface — the plugin takes no parameters.

### Usage

```js
flatpickr("#date", {
  enableTime: true,
  plugins: [scrollPlugin()]
});
```

### Behavior

- Scrolling over the hour/minute/second inputs changes the value via an `increment` CustomEvent
- Scrolling over the month name in the header switches the month
- Scrolling over the year input changes the year
- An IE9 polyfill for `CustomEvent` is built in

---

## 7. momentPlugin

Integration with [moment.js](https://momentjs.com) for parsing/formatting.
Allows the use of moment format strings instead of flatpickr tokens.

### Import

```js
import momentPlugin from "flatpickr/dist/plugins/momentPlugin.js";
import moment from "moment";
```

### Config interface (`src/plugins/momentPlugin.ts`)

```typescript
interface Config {
  moment: Function;  // the moment function (required)
}
```

### Usage

```js
flatpickr("#date", {
  plugins: [momentPlugin({ moment: moment })],
  dateFormat: "YYYY-MM-DD",  // moment format strings
  altFormat: "DD.MM.YYYY",
  altInput: true,
  locale: "de",  // the moment locale is applied automatically
});
```

### Behavior

- Replaces the instance's `parseDate` and `formatDate` with moment implementations
- `parseDate(datestr, format)` uses `moment(datestr, format, true).toDate()` (strict mode)
- `formatDate(date, format)` uses `momentDate.format(format)` with an optional locale
- Supports `increment` events for the hour/minute/second inputs (moment-based increment)
- With the `locale` option given as a string, the moment locale is set

**Alternative without the plugin** (direct approach without a moment dependency in the plugin):

```js
flatpickr("#date", {
  altInput: true,
  dateFormat: "YYYY-MM-DD",
  altFormat: "DD-MM-YYYY",
  allowInput: true,
  parseDate: (datestr, format) => {
    return moment(datestr, format, true).toDate();
  },
  formatDate: (date, format, locale) => {
    return moment(date).format(format);
  }
});
```

---

## 8. labelPlugin

Fixes an accessibility problem: when `altInput: true` or mobile mode is active,
the `id` of the original input is transferred to the visible element.
This makes `<label for="...">` work correctly.
No configuration parameters.

### Import

```js
import labelPlugin from "flatpickr/dist/plugins/labelPlugin/labelPlugin.js";
```

### Config interface

No config interface — the plugin takes no parameters.

### Usage

```html
<label for="myDate">Date:</label>
<input id="myDate" type="text">
```

```js
flatpickr("#myDate", {
  altInput: true,
  plugins: [labelPlugin()]
});
// the altInput receives id="myDate", the original input loses the id
// → clicking the label opens the picker correctly
```

### Behavior

- With `altInput: true`: the original input loses the `id`, `altInput` receives it
- In mobile mode: the original input loses the `id`, `mobileInput` receives it
- When no `id` is present, the plugin does nothing

---

## Writing your own plugin

```typescript
import { Plugin } from "flatpickr/dist/types/options";

interface MyConfig {
  option?: string;
}

function myPlugin(config: MyConfig = {}): Plugin {
  return function(fp) {
    return {
      onReady() {
        console.log("plugin ready:", fp);
        fp.loadedPlugins.push("myPlugin"); // convention: register the plugin name
      },
      onChange(selectedDates, dateStr) {
        console.log("onChange:", dateStr);
      },
      onDestroy() {
        // remove event listeners, clean up
      }
    };
  };
}

flatpickr("#date", {
  plugins: [myPlugin({ option: "value" })]
});
```

### Hooks in plugins

For each hook, a plugin may also return an array of functions:

```js
return {
  onReady: [fn1, fn2, fn3],
  onDestroy: [cleanup1, cleanup2],
};
```

---

Source: `src/plugins/*` (v4.6.13) | https://flatpickr.js.org/plugins/
