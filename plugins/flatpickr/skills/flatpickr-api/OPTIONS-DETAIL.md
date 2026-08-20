# flatpickr — Complete options reference (v4.6.13)

All options are passed as the second argument to `flatpickr(element, options)`.
Source: `src/types/options.ts` + `src/types/options.ts#defaults` (authoritative, as of v4.6.13).

## Contents

- [Complete options table](#complete-options-table)
- [Hook signature (type `Hook`)](#hook-signature-type-hook)
- [Options in detail](#options-in-detail)

## Complete options table

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `allowInput` | `Boolean` | `false` | Lets the user type the date directly into the input field |
| `allowInvalidPreload` | `Boolean` | `false` | Allows preloading an invalid date; when `false`, the field is cleared if the supplied date is invalid |
| `altFormat` | `String` | `"F j, Y"` | Display format for the `altInput` field (same tokens as `dateFormat`) |
| `altInput` | `Boolean` | `false` | Shows the user a readable date (per `altFormat`) but sends the `dateFormat` value to the server |
| `altInputClass` | `String` | `"form-control input"` | CSS classes for the input element created by `altInput` (it already inherits the original input's classes) |
| `animate` | `Boolean` | `true` (except IE) | Enables month transition animations (automatically `false` in IE) |
| `appendTo` | `HTMLElement` | `undefined` | Appends the calendar to the given DOM element instead of `document.body` |
| `ariaDateFormat` | `String` | `"F j, Y"` | Defines the date format in the `aria-label` of the calendar days (for screen readers) |
| `autoFillDefaultTime` | `Boolean` | `true` | Whether the default time is filled in automatically when the input is empty and gains or loses focus |
| `clickOpens` | `Boolean` | `true` | Opens the picker when the input element is clicked; `false` for purely programmatic opening |
| `closeOnSelect` | `Boolean` | `true` | Close the calendar automatically after a date is selected |
| `conjunction` | `String` | `", "` | Separator between dates in `multiple` mode (e.g. `" :: "`) |
| `dateFormat` | `String` | `"Y-m-d"` | Format of the date in the input element (the value sent to the backend) |
| `defaultDate` | `String\|Date\|Array` | `undefined` | Preselected date / preselected dates on initialization |
| `defaultHour` | `Number` | `12` | Default hour in the time picker when no date is selected |
| `defaultMinute` | `Number` | `0` | Default minute in the time picker when no date is selected |
| `defaultSeconds` | `Number` | `0` | Default second in the time picker when no date is selected |
| `disable` | `Array` | `[]` | Array of dates, date ranges or functions that define the dates to be blocked |
| `disableMobile` | `Boolean` | `false` | Forces the flatpickr picker on mobile devices too (no native picker) |
| `enable` | `Array` | `undefined` | Array of dates/ranges/functions — when set, ONLY these dates are selectable |
| `enableSeconds` | `Boolean` | `false` | Enable second selection in the time picker |
| `enableTime` | `Boolean` | `false` | Enable the time picker |
| `errorHandler` | `Function` | `console.warn` | Error handling function `(err: Error) => void` for invalid dates |
| `formatDate` | `Function` | `undefined` | Custom formatting function `(date, format, locale) => string`; replaces the built-in one |
| `getWeek` | `Function` | ISO-8601 calculation | Function `(date: Date) => string\|number` for week number calculation (with `weekNumbers: true`) |
| `hourIncrement` | `Integer` | `1` | Step size for hours (also via the scroll wheel) |
| `ignoredFocusElements` | `HTMLElement[]` | `[]` | Elements that can be clicked without closing the calendar |
| `inline` | `Boolean` | `false` | Displays the calendar permanently (not as a dropdown) |
| `locale` | `String\|Object` | `"default"` | Localization: language code (`"de"`, `"ru"`) or locale object (partial or complete) |
| `maxDate` | `String\|Date\|Number` | `undefined` | Latest selectable date (inclusive) |
| `maxTime` | `String\|Date\|Number` | `undefined` | Latest selectable time |
| `minDate` | `String\|Date\|Number` | `undefined` | Earliest selectable date (inclusive) |
| `minTime` | `String\|Date\|Number` | `undefined` | Earliest selectable time |
| `minuteIncrement` | `Integer` | `5` | Step size for minutes (also via the scroll wheel) |
| `mode` | `String` | `"single"` | Selection mode: `"single"`, `"multiple"`, `"range"`, `"time"` |
| `monthSelectorType` | `String` | `"dropdown"` | Month display in the header: `"dropdown"` or `"static"` |
| `nextArrow` | `String` | SVG arrow | HTML content for the arrow to the next month |
| `noCalendar` | `Boolean` | `false` | Hides the calendar — time picker only (with `enableTime: true`) |
| `now` | `String\|Date\|Number` | `new Date()` | Overrides "today" for all date calculations (useful for tests) |
| `onChange` | `Function\|Array` | `[]` | Hook: fires when the date/time is changed |
| `onClose` | `Function\|Array` | `[]` | Hook: fires when the calendar closes |
| `onDayCreate` | `Function\|Array` | `[]` | Hook: for every day DOM element while rendering (4th param is `dayElem`) |
| `onDestroy` | `Function\|Array` | `[]` | Hook: fires before the instance is destroyed (`destroy()`) |
| `onKeyDown` | `Function\|Array` | `[]` | Hook: fires on valid keyboard input |
| `onMonthChange` | `Function\|Array` | `[]` | Hook: fires when the month changes |
| `onOpen` | `Function\|Array` | `[]` | Hook: fires when the calendar opens |
| `onParseConfig` | `Function\|Array` | `[]` | Hook: fires after config parsing; allows manipulation of the ParsedOptions |
| `onPreCalendarPosition` | `Function\|Array` | `[]` | Hook: fires before the calendar is positioned |
| `onReady` | `Function\|Array` | `[]` | Hook: fires once when the calendar is fully ready |
| `onValueUpdate` | `Function\|Array` | `[]` | Hook: fires when the input value is updated (more often than `onChange`) |
| `onYearChange` | `Function\|Array` | `[]` | Hook: fires when the year changes |
| `parseDate` | `Function` | `undefined` | Custom parse function `(dateString, format) => Date` |
| `plugins` | `Array` | `[]` | Array of plugin instances (each plugin is a function that returns options) |
| `position` | `String\|Function` | `"auto"` | Calendar position relative to the input: `"auto"`, `"above"`, `"below"`, `"auto left"`, `"auto center"`, `"auto right"`, `"above left"`, `"above center"`, `"above right"`, `"below left"`, `"below center"`, `"below right"` or `(self, el) => void` |
| `positionElement` | `Element` | `undefined` | Reference element for positioning the calendar (instead of the input) |
| `prevArrow` | `String` | SVG arrow | HTML content for the arrow to the previous month |
| `shorthandCurrentMonth` | `Boolean` | `false` | Shows month names in short form (Sep instead of September) |
| `showMonths` | `Integer` | `1` | Number of calendar months visible at the same time |
| `static` | `Boolean` | `false` | Positions the calendar directly next to the input (inside a wrapper element); for scrollable containers |
| `time_24hr` | `Boolean` | `false` | 24-hour format in the time picker (no AM/PM) |
| `weekNumbers` | `Boolean` | `false` | Shows week numbers on the left of the calendar |
| `wrap` | `Boolean` | `false` | Enables custom elements (buttons, toggle, clear) with `data-input`, `data-toggle`, `data-clear` attributes |

## Hook signature (type `Hook`)

```typescript
type Hook = (
  dates: Date[],       // Array of the selected dates
  currentDateString: string,  // Formatted date string
  self: Instance,      // The flatpickr instance
  data?: any           // Optional extra data (e.g. for onDayCreate: dayElem)
) => void;
```

All hooks can also be passed as an array:

```js
onChange: [handler1, handler2, handler3]
```

## Options in detail

### `altInput` + `altFormat`

```js
flatpickr("#date", {
  altInput: true,
  altFormat: "F j, Y",     // "January 15, 2024" — visible to the user
  dateFormat: "Y-m-d",     // "2024-01-15" — sent to the backend
  altInputClass: "my-visible-input",
});
```

The original input is hidden and a new visible input using `altFormat` is created.

### `animate`

```js
// Disable animations (e.g. for tests or accessibility)
flatpickr("#date", { animate: false });
```

### `autoFillDefaultTime`

```js
// Prevents the default time being inserted when focus is lost without a date selection
flatpickr("#date", {
  enableTime: true,
  autoFillDefaultTime: false,
});
```

### `closeOnSelect`

```js
// Keep the calendar open after a date is selected (useful with the time picker)
flatpickr("#date", {
  enableTime: true,
  closeOnSelect: false,
});
```

### `disable` — the various forms

```js
// Individual dates
disable: ["2024-01-01", "2024-12-25", new Date(2024, 5, 15)]

// Date ranges
disable: [
  { from: "2024-04-01", to: "2024-04-30" },
  { from: "2024-08-01", to: "2024-08-31" }
]

// Function (true = blocked)
disable: [
  function(date) {
    return date.getDay() === 0 || date.getDay() === 6; // weekends
  }
]
```

### `enable`

Only the given dates are selectable — all others are blocked.

```js
enable: [
  "2024-06-01",
  { from: "2024-07-01", to: "2024-07-31" },
  function(date) { return date.getDate() === 15; } // every 15th
]
```

### `errorHandler`

```js
flatpickr("#date", {
  errorHandler: (err) => {
    // Your own error reporting instead of console.warn
    myErrorTracker.log(err.message);
  }
});
```

### `getWeek`

```js
// Default: ISO-8601 calculation (the Thursday in the week decides the year)
// Override it for your own logic:
flatpickr("#date", {
  weekNumbers: true,
  getWeek: (date) => {
    return `KW ${/* your own calculation */}`;
  }
});
```

### `ignoredFocusElements`

```js
const myButton = document.getElementById("extraButton");
flatpickr("#date", {
  ignoredFocusElements: [myButton], // clicking myButton does not close the calendar
});
```

### `mode`

```js
// Single selection (default)
mode: "single"

// Multiple selection (separated by conjunction in the input)
mode: "multiple"
conjunction: " :: "  // customize the separator (default: ", ")

// Date range
mode: "range"

// Time only (no calendar — equivalent to noCalendar + enableTime)
mode: "time"
```

### `now`

```js
// Override "today" (useful for tests)
flatpickr("#date", {
  now: new Date("2024-06-01"),
});
```

### `onDestroy`

```js
flatpickr("#date", {
  onDestroy: function(selectedDates, dateStr, instance) {
    // Clean up before the destroy
    console.log("Picker is being removed");
  }
});
```

### `onKeyDown`

```js
flatpickr("#date", {
  onKeyDown: function(selectedDates, dateStr, instance, event) {
    // Intercept keyboard input
    if (event.key === "Escape") {
      instance.close();
    }
  }
});
```

### `onPreCalendarPosition`

```js
flatpickr("#date", {
  onPreCalendarPosition: function(selectedDates, dateStr, instance) {
    // Before the calendar is positioned
  }
});
```

### `plugins`

```js
import confirmDatePlugin from "flatpickr/dist/plugins/confirmDate/confirmDate.js";
import scrollPlugin from "flatpickr/dist/plugins/scrollPlugin.js";

flatpickr("#date", {
  enableTime: true,
  plugins: [
    confirmDatePlugin({ confirmText: "OK" }),
    scrollPlugin(),
  ]
});
```

### `position`

```js
// String variants
position: "auto"           // automatic (default)
position: "above"          // always above
position: "below"          // always below
position: "auto left"      // left aligned
position: "auto center"    // centered
position: "auto right"     // right aligned
position: "above left"
position: "above center"
position: "above right"
position: "below left"
position: "below center"
position: "below right"

// Function (for fully custom positioning)
position: function(self, customElement) {
  // customElement is positionElement or undefined
  self.calendarContainer.style.top = "100px";
  self.calendarContainer.style.left = "200px";
}
```

### `parseDate` + `formatDate` (moment.js example)

```js
import moment from "moment";

flatpickr("#date", {
  altInput: true,
  dateFormat: "YYYY-MM-DD",
  altFormat: "DD.MM.YYYY",
  allowInput: true,
  parseDate: (datestr, format) => {
    return moment(datestr, format, true).toDate();
  },
  formatDate: (date, format, locale) => {
    return moment(date).format(format);
  }
});
```

### `showMonths`

```js
// Show two months side by side
flatpickr("#date", { showMonths: 2 });
```

### `static`

```js
// For scrollable containers: the calendar position is calculated relative to the wrapper
flatpickr("#date", { static: true });
```

The HTML must contain a wrapper:

```html
<div class="flatpickr-wrapper">
  <input id="date" type="text">
</div>
```

### `wrap` — input groups with buttons

```html
<div class="flatpickr">
  <input type="text" placeholder="Choose a date" data-input>
  <button type="button" data-toggle>Calendar</button>
  <button type="button" data-clear>X</button>
</div>
```

```js
flatpickr(".flatpickr", { wrap: true });
```

### `inline`

```js
// Calendar always visible (no dropdown)
flatpickr("#container", { inline: true });
```

---

Source: `src/types/options.ts` (v4.6.13) | https://flatpickr.js.org/options/
