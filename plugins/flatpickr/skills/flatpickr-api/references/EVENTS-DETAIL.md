# flatpickr — Events and hooks (complete reference, v4.6.13)

Source: `src/types/options.ts` (type `HookKey`, constant `HOOKS`, as of v4.6.13).

## Contents

- [Basic principle](#basic-principle)
- [All hook keys](#all-hook-keys)
- [Standard hook signature (type `Hook`)](#standard-hook-signature-type-hook)
- [Hooks in detail](#hooks-in-detail)
- [Manipulating hooks after initialization](#manipulating-hooks-after-initialization)
- [Setting hooks dynamically via `set()`](#setting-hooks-dynamically-via-set)
- [Several hooks at once as an array](#several-hooks-at-once-as-an-array)

## Basic principle

Hooks are passed as option properties. Every hook can be a single function
or an array of functions.

```js
flatpickr("#date", {
  onChange: function(selectedDates, dateStr, instance) {
    console.log("Selected:", dateStr);
    console.log("As a Date object:", selectedDates[0]);
  },
  onClose: [
    function(selectedDates, dateStr, instance) { /* fn1 */ },
    function(selectedDates, dateStr, instance) { /* fn2 */ }
  ],
});
```

## All hook keys

Complete list according to `src/types/options.ts`:

```typescript
type HookKey =
  | "onChange"
  | "onClose"
  | "onDayCreate"
  | "onDestroy"
  | "onKeyDown"
  | "onMonthChange"
  | "onOpen"
  | "onParseConfig"
  | "onReady"
  | "onValueUpdate"
  | "onYearChange"
  | "onPreCalendarPosition";
```

## Standard hook signature (type `Hook`)

All hooks receive the same signature:

```typescript
type Hook = (
  dates: Date[],              // Array of the selected dates
  currentDateString: string,  // Formatted date string (per dateFormat)
  self: Instance,             // The flatpickr instance
  data?: any                  // Optional extra data
) => void;
```

| Parameter | Type | Description |
|-----------|-----|-------------|
| `selectedDates` | `Date[]` | Array of the selected Date objects |
| `dateStr` | `String` | String representation of the most recently selected date (per `dateFormat`) |
| `instance` | `Instance` | The flatpickr instance with all methods and properties |
| `data` | `any` | Optional extra data (for `onDayCreate`: the HTML element) |

## Hooks in detail

### `onChange`

Fires when the user selects a date, deselects it, or changes the time of a selected date. Also on programmatic changes when `triggerChange: true`.

```js
flatpickr("#date", {
  onChange: function(selectedDates, dateStr, instance) {
    console.log("New date:", dateStr);
    console.log("As a Date:", selectedDates[0]);

    // Update a second instance (e.g. for the "to" date)
    toDatePicker.set("minDate", selectedDates[0]);
  }
});
```

With `mode: "range"`:

```js
onChange: function(selectedDates) {
  if (selectedDates.length === 2) {
    const [from, to] = selectedDates;
    console.log("From:", from, "To:", to);
  }
}
```

---

### `onOpen`

Fires when the calendar opens (through user interaction or `fp.open()`).

```js
flatpickr("#date", {
  onOpen: function(selectedDates, dateStr, instance) {
    console.log("Calendar opened");
    // Jump to the current month
    instance.jumpToDate(new Date());
  }
});
```

---

### `onClose`

Fires when the calendar closes (through user interaction or `fp.close()`).

```js
flatpickr("#date", {
  onClose: function(selectedDates, dateStr, instance) {
    console.log("Calendar closed, value:", dateStr);
    // Validate on close
    if (!dateStr) {
      instance.setDate(new Date());
    }
  }
});
```

---

### `onReady`

Fires **once** when the calendar is fully initialized (after all plugin `onReady` hooks).

```js
flatpickr("#date", {
  onReady: function(selectedDates, dateStr, instance) {
    console.log("flatpickr initialized:", instance);
    // Store an external reference
    window.myPicker = instance;
  }
});
```

---

### `onValueUpdate`

Fires when the input value is updated with a new date string.
Can fire more often than `onChange` (also on hover, partial input, etc.).

```js
flatpickr("#date", {
  onValueUpdate: function(selectedDates, dateStr, instance) {
    // Also fires on programmatic changes
    document.getElementById("display").textContent = dateStr;
  }
});
```

---

### `onMonthChange`

Fires when the displayed month changes (by the user or programmatically via `changeMonth()`).

```js
flatpickr("#date", {
  onMonthChange: function(selectedDates, dateStr, instance) {
    console.log("Month:", instance.currentMonth, "Year:", instance.currentYear);
    // Load available dates dynamically
    loadAvailableDates(instance.currentYear, instance.currentMonth);
  }
});
```

---

### `onYearChange`

Fires when the displayed year changes (by the user or programmatically).

```js
flatpickr("#date", {
  onYearChange: function(selectedDates, dateStr, instance) {
    console.log("Year changed:", instance.currentYear);
  }
});
```

---

### `onDayCreate`

Called for every day DOM element while the calendar renders.
Gives full control over each calendar day.
Here the 4th argument `data` is the `DayElement` (HTMLSpanElement with a `.dateObj` property).

```js
flatpickr("#date", {
  onDayCreate: function(dObj, dStr, fp, dayElem) {
    // dayElem is a DayElement (HTMLSpanElement & { dateObj: Date; $i: number })
    
    // Add a tooltip
    dayElem.title = "Click for " + dStr;

    // Add an event dot
    if (hasEvent(dObj)) {
      dayElem.innerHTML += "<span class='event-dot'></span>";
    }

    // Mark specific days
    if (dObj.getDate() === 15) {
      dayElem.classList.add("pay-day");
    }
  }
});
```

```css
.event-dot {
  position: absolute;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  bottom: 2px;
  left: calc(50% - 2px);
  background: #3d8eb9;
}
.pay-day {
  background: #e8f5e9;
  font-weight: bold;
}
```

---

### `onParseConfig`

Fires after the configuration has been parsed. Allows manipulation of the `ParsedOptions`
before the calendar is built. Also used by plugins (`rangePlugin`, `weekSelect`, `monthSelect`).

```js
flatpickr("#date", {
  onParseConfig: function(selectedDates, dateStr, instance) {
    // Adjust the config after parsing
    // Caution: instance.config is still being built at this point
    console.log("Config parsed");
  }
});
```

---

### `onDestroy`

Fires before the flatpickr instance is destroyed (`fp.destroy()`).
Useful for cleanup work in plugins and integration code.

```js
flatpickr("#date", {
  onDestroy: function(selectedDates, dateStr, instance) {
    console.log("Picker is being removed");
    // Release external references
    window.myPicker = null;
    // Remove your own event listeners
    document.removeEventListener("click", myHandler);
  }
});
```

---

### `onKeyDown`

Fires on valid keyboard input inside the calendar.
Here the 4th argument `data` is the `KeyboardEvent`.

```js
flatpickr("#date", {
  onKeyDown: function(selectedDates, dateStr, instance, event) {
    // event is the KeyboardEvent
    if (event.key === "Enter") {
      console.log("Enter pressed");
    }
    if (event.key === "Escape") {
      instance.close();
    }
  }
});
```

---

### `onPreCalendarPosition`

Fires immediately before the calendar's position is calculated.
Useful for plugins that need to change the `positionElement` dynamically (e.g. `rangePlugin`).

```js
flatpickr("#date", {
  onPreCalendarPosition: function(selectedDates, dateStr, instance) {
    // Before positioning: can overwrite instance._positionElement
    console.log("Calendar is being positioned");
  }
});
```

---

## Manipulating hooks after initialization

```js
const fp = flatpickr("#date", { onChange: originalHandler });

// Add another handler
fp.config.onChange.push(function(selectedDates, dateStr) {
  console.log("Additional handler:", dateStr);
});

// Replace the handlers entirely
fp.config.onChange = [newHandler];
```

## Setting hooks dynamically via `set()`

```js
const fp = flatpickr("#date", {});

fp.set("onChange", function(selectedDates, dateStr) {
  console.log("Set dynamically:", dateStr);
});
```

## Several hooks at once as an array

```js
flatpickr("#date", {
  onReady: [
    function(selectedDates, dateStr, fp) { /* initialization A */ },
    function(selectedDates, dateStr, fp) { /* initialization B */ },
  ],
  onDestroy: [cleanupA, cleanupB],
});
```

---

Source: `src/types/options.ts` (v4.6.13) | https://flatpickr.js.org/events/
