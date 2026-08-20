# flatpickr — Instance API (complete reference, v4.6.13)

Source: `src/types/instance.ts` (authoritative, as of v4.6.13).

```js
const fp = flatpickr("#date", { enableTime: true });
```

---

## Contents

- [Methods](#methods)
- [Properties](#properties)
- [DOM elements](#dom-elements)
- [DayElement type](#dayelement-type)
- [Static helper functions](#static-helper-functions)
- [`fp_incr` — date helper function](#fp_incr--date-helper-function)

## Methods

### `open(e?, positionElement?)`

Opens the calendar.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `e` | `FocusEvent\|MouseEvent` | Optional event (usually omitted) |
| `positionElement` | `HTMLElement` | Optional element used for positioning |

```js
fp.open();
```

---

### `close()`

Closes the calendar.

```js
fp.close();
```

---

### `toggle()`

Opens the calendar when it is closed, closes it when it is open.

```js
fp.toggle();
```

---

### `clear(emitChangeEvent?, toInitial?)`

Resets the selection and clears the input field.

| Parameter | Type | Default | Description |
|-----------|-----|---------|-------------|
| `emitChangeEvent` | `Boolean` | `true` | Whether `onChange` should be fired |
| `toInitial` | `Boolean` | `false` | Reset to the initial state |

```js
fp.clear();
fp.clear(false); // no onChange event
```

---

### `destroy()`

Removes the flatpickr instance completely: removes event listeners and restores the original
input. After `destroy()` the instance can no longer be used.

```js
fp.destroy();
```

---

### `changeMonth(value, isOffset?, fromKeyboard?)`

Changes the displayed month.

| Parameter | Type | Default | Description |
|-----------|-----|---------|-------------|
| `value` | `Number` | — | Month value |
| `isOffset` | `Boolean` | `true` | `true`: month number as an offset; `false`: absolute month (0–11) |
| `fromKeyboard` | `Boolean` | `false` | Indicates whether the action was triggered by the keyboard |

```js
fp.changeMonth(1);         // one month forward
fp.changeMonth(-2);        // two months back
fp.changeMonth(0, false);  // jump to January (absolute)
fp.changeMonth(11, false); // jump to December (absolute)
```

---

### `changeYear(year)`

Changes the displayed year directly to the given value.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `year` | `Number` | The target year (4 digits) |

```js
fp.changeYear(2025);
```

---

### `formatDate(dateObj, formatStr)`

Returns a formatted date string.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `dateObj` | `Date` | The Date object to format |
| `formatStr` | `String` | Format pattern (same tokens as `dateFormat`) |

**Returns:** `String`

```js
fp.formatDate(new Date(), "Y-m-d");       // "2024-12-31"
fp.formatDate(new Date(), "d.m.Y H:i");  // "31.12.2024 14:30"
```

---

### `isEnabled(date, timeless?)`

Checks whether a given date is selectable (not blocked by `disable`/`enable` or `minDate`/`maxDate`).

| Parameter | Type | Default | Description |
|-----------|-----|---------|-------------|
| `date` | `String\|Date\|Number` | — | The date to check |
| `timeless` | `Boolean` | `true` | Ignore the time when checking |

**Returns:** `Boolean`

```js
fp.isEnabled("2024-12-25"); // false when blocked
fp.isEnabled(new Date());   // true when today is selectable
```

---

### `jumpToDate(date?, triggerChange?)`

Sets the calendar view to the year and month of the given date. Does not select the
date — navigation only.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `date` | `String\|Date\|undefined` | Target date; `undefined` → jumps to the last selected date, `minDate` or today |
| `triggerChange` | `Boolean` | Whether month/year change hooks should be fired |

```js
fp.jumpToDate("2025-06-01");
fp.jumpToDate(new Date(), true);
fp.jumpToDate(); // jumps to the currently selected date or today
```

---

### `parseDate(date, givenFormat?, timeless?)`

Converts a date string or timestamp into a Date object.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `date` | `Date\|String\|Number` | Date string, timestamp or Date object |
| `givenFormat` | `String` | Expected format (optional) |
| `timeless` | `Boolean` | Ignore the time part |

**Returns:** `Date | undefined`

```js
fp.parseDate("31.12.2024", "d.m.Y"); // → Date Object
fp.parseDate("2024-12-31", "Y-m-d"); // → Date Object
```

---

### `redraw()`

Redraws the calendar. Necessary e.g. after DOM manipulation on the calendar.

```js
fp.redraw();
```

---

### `set(option, value?)`

Updates a config option and redraws the calendar when needed.
An object holding several options can also be passed.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `option` | `String\|Object` | Name of the config property or an object with several options |
| `value` | `*` | New value (when `option` is a string) |

```js
fp.set("minDate", "today");
fp.set("maxDate", new Date().fp_incr(14)); // 14 days from today
fp.set("dateFormat", "d.m.Y");
fp.set("disable", [function(date) { return date.getDay() === 0; }]);
fp.set("onChange", newHandler);

// Several options at once
fp.set({ minDate: "2024-01-01", maxDate: "2024-12-31" });
```

---

### `setDate(date, triggerChange?, format?)`

Sets the selected date programmatically.

| Parameter | Type | Description |
|-----------|-----|-------------|
| `date` | `String\|Date\|Number\|Array` | Date or array of dates |
| `triggerChange` | `Boolean` | Whether `onChange` hooks are fired |
| `format` | `String` | Format of the date string (when it differs from `dateFormat`) |

```js
fp.setDate("2024-06-15");                          // using dateFormat
fp.setDate(new Date());                            // today
fp.setDate("15.06.2024", true, "d.m.Y");          // a different format
fp.setDate(["2024-06-01", "2024-06-30"]);          // range or multiple
fp.setDate(["2024-06-01", "2024-06-30"], true);    // with an onChange trigger
```

---

### `updateValue(triggerChange?)`

Updates the value of the input field based on the currently selected dates.

| Parameter | Type | Default | Description |
|-----------|-----|---------|-------------|
| `triggerChange` | `Boolean` | `true` | Whether `onChange` hooks should be fired |

```js
fp.updateValue();
fp.updateValue(false); // without an event
```

---

### `pad(num)`

Helper function: returns a number padded to 2 digits.

```js
fp.pad(5);  // "05"
fp.pad(12); // "12"
```

---

## Properties

### `selectedDates`

- **Type:** `Date[]`
- Array of the currently selected Date objects (empty when nothing is selected)

```js
const dates = fp.selectedDates;
if (dates.length > 0) {
  console.log("First date:", dates[0]);
}
// Range: dates[0] = start, dates[1] = end
```

### `currentYear`

- **Type:** `Number`
- The year displayed in the calendar

```js
console.log(fp.currentYear); // e.g. 2024
```

### `currentMonth`

- **Type:** `Number` (0–11)
- The month displayed in the calendar (0 = January, 11 = December)

```js
console.log(fp.currentMonth); // 0–11
const monthName = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][fp.currentMonth];
```

### `config`

- **Type:** `ParsedOptions`
- The active configuration (defaults + user options, fully parsed)
- Hooks are accessible as arrays and can be manipulated

```js
console.log(fp.config.dateFormat);
fp.config.onChange.push(additionalHandler);
```

### `isOpen`

- **Type:** `Boolean`
- `true` when the calendar is currently open

```js
if (!fp.isOpen) fp.open();
```

### `isMobile`

- **Type:** `Boolean`
- `true` when flatpickr is running in mobile mode (native picker)

```js
if (!fp.isMobile) {
  fp.calendarContainer.classList.add("custom-class");
}
```

### `latestSelectedDateObj`

- **Type:** `Date | undefined`
- The most recently selected Date object (with a range selection too: the end clicked last)

```js
console.log(fp.latestSelectedDateObj);
```

### `now`

- **Type:** `Date`
- The "today" date (can be overridden with the `now` option)

```js
console.log(fp.now); // current date
```

### `l10n`

- **Type:** `Locale`
- The active locale object

```js
console.log(fp.l10n.months.longhand[fp.currentMonth]);
```

### `loadedPlugins`

- **Type:** `string[]`
- Names of the loaded plugins (plugins add themselves via `fp.loadedPlugins.push("name")`)

```js
console.log(fp.loadedPlugins); // e.g. ["confirmDate", "scroll"]
```

---

## DOM elements

### `element`

- **Type:** `HTMLElement`
- The original element flatpickr was initialized on

### `input`

- **Type:** `HTMLInputElement`
- The active input element (with `altInput: true`: the altInput element internally; `_input` is the original)

```js
fp.input.setAttribute("placeholder", "Choose a date");
```

### `_input`

- **Type:** `HTMLInputElement`
- The original input element (before the altInput replacement)

### `altInput`

- **Type:** `HTMLInputElement | undefined`
- The visible input element created by `altInput: true`

```js
if (fp.altInput) {
  fp.altInput.classList.add("my-visible-input");
}
```

### `mobileInput`

- **Type:** `HTMLInputElement | undefined`
- The native input element in mobile mode

### `calendarContainer`

- **Type:** `HTMLDivElement` (`div.flatpickr-calendar`)
- The calendar container itself

```js
fp.calendarContainer.classList.add("my-custom-class");
```

### `days`

- **Type:** `HTMLDivElement`
- Container element for all day cells in the calendar

### `daysContainer`

- **Type:** `HTMLDivElement | undefined`
- Outer container of the day elements

### `monthNav`

- **Type:** `HTMLDivElement`
- The month navigation container (holds arrows, month, year)

### `prevMonthNav`

- **Type:** `HTMLElement`
- The "back" arrow for the month navigation

### `nextMonthNav`

- **Type:** `HTMLElement`
- The "forward" arrow for the month navigation

### `currentMonthElement`

- **Type:** `HTMLSpanElement`
- The `<span>` holding the current month name (first month element)

### `currentYearElement`

- **Type:** `HTMLInputElement`
- The `<input>` holding the current year (first year element)

### `monthElements`

- **Type:** `HTMLSpanElement[]`
- Array of all month elements (several with `showMonths > 1`)

### `yearElements`

- **Type:** `HTMLInputElement[]`
- Array of all year elements (several with `showMonths > 1`)

### `monthsDropdownContainer`

- **Type:** `HTMLSelectElement`
- The `<select>` element for the month dropdown navigation (`monthSelectorType: "dropdown"`)

### `weekdayContainer`

- **Type:** `HTMLDivElement`
- Container for the weekday headers (Mon, Tue, Wed, ...)

### `weekWrapper`

- **Type:** `HTMLDivElement | undefined`
- Outer wrapper for the week number display (only when `weekNumbers: true`)

### `weekNumbers`

- **Type:** `HTMLDivElement | undefined`
- Container for the week number column (only when `weekNumbers: true`)

### `timeContainer`

- **Type:** `HTMLDivElement | undefined`
- Container for the time picker (only when `enableTime: true`)

### `hourElement`

- **Type:** `HTMLInputElement | undefined`
- The hour input in the time picker

```js
if (fp.hourElement) {
  console.log("Current hour:", fp.hourElement.value);
}
```

### `minuteElement`

- **Type:** `HTMLInputElement | undefined`
- The minute input in the time picker

### `secondElement`

- **Type:** `HTMLInputElement | undefined`
- The second input (only when `enableSeconds: true`)

### `amPM`

- **Type:** `HTMLSpanElement | undefined`
- The AM/PM toggle element (only when `time_24hr: false` and `enableTime: true`)

### `selectedDateElem`

- **Type:** `DayElement | undefined`
- The DOM element of the most recently selected day

### `todayDateElem`

- **Type:** `DayElement | undefined`
- The DOM element of today's day in the calendar

### `pluginElements`

- **Type:** `Node[]`
- DOM elements that were added by plugins

---

## DayElement type

```typescript
type DayElement = HTMLSpanElement & {
  dateObj: Date;  // The date of the day
  $i: number;     // Index in the calendar grid (0–41)
};
```

Used in `onDayCreate` and the `weekSelect` plugin.

---

## Static helper functions

Available directly on the `flatpickr` object (not on the instance):

### `flatpickr.parseDate(date, format?, timeless?)`

```js
const date = flatpickr.parseDate("2024-12-31", "Y-m-d");
// → Date Object: Tue Dec 31 2024
```

### `flatpickr.formatDate(date, format)`

```js
const str = flatpickr.formatDate(new Date(), "Y-m-d h:i K");
// → "2024-12-31 02:30 PM"
```

### `flatpickr.compareDates(date1, date2, timeless?)`

Compares two dates. Returns a negative number, 0 or a positive number.

```js
flatpickr.compareDates(new Date("2024-01-01"), new Date("2024-06-01")); // < 0
flatpickr.compareDates(new Date("2024-06-01"), new Date("2024-06-01")); // 0
```

### `flatpickr.localize(locale)`

Set the global localization:

```js
import { German } from "flatpickr/dist/l10n/de.js";
flatpickr.localize(German);
// Now all new flatpickr instances use German
```

### `flatpickr.setDefaults(config)`

Set global default options (affects all newly created instances):

```js
flatpickr.setDefaults({
  dateFormat: "d.m.Y",
  locale: "de",
});
```

### `flatpickr.defaultConfig`

- **Type:** `Partial<ParsedOptions>`
- Access to the global default configuration

```js
console.log(flatpickr.defaultConfig.dateFormat); // "Y-m-d"
```

### `flatpickr.l10ns`

- **Type:** `{ [k in LocaleKey]?: CustomLocale } & { default: Locale }`
- All loaded locale objects

```js
flatpickr.l10ns.default.firstDayOfWeek = 1; // Monday as the first weekday globally
```

---

## `fp_incr` — date helper function

flatpickr extends Date objects with the `fp_incr(n)` method:

```js
new Date().fp_incr(7)   // today + 7 days
new Date().fp_incr(-3)  // today - 3 days

// Typical use case: maxDate two weeks from today
fp.set("maxDate", new Date().fp_incr(14));
```

---

Source: `src/types/instance.ts` (v4.6.13) | https://flatpickr.js.org/instance-methods-properties-elements/
