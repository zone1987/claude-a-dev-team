# flatpickr — Examples & patterns (complete reference)

## Contents

- [1. Basic (no config)](#1-basic-no-config)
- [2. DateTime picker](#2-datetime-picker)
- [3. Human-readable date (altInput)](#3-human-readable-date-altinput)
- [4. Date formats for defaultDate](#4-date-formats-for-defaultdate)
- [5. Preloading a date](#5-preloading-a-date)
- [6. minDate / maxDate](#6-mindate-maxdate)
- [7. Blocking dates (disable)](#7-blocking-dates-disable)
- [8. Allowing only certain dates (enable)](#8-allowing-only-certain-dates-enable)
- [9. Multiple selection (multiple)](#9-multiple-selection-multiple)
- [10. Date range (range)](#10-date-range-range)
- [11. Time picker (without calendar)](#11-time-picker-without-calendar)
- [12. DateTime with time limits](#12-datetime-with-time-limits)
- [13. Inline calendar (always visible)](#13-inline-calendar-always-visible)
- [14. Week numbers](#14-week-numbers)
- [15. Input group with buttons (wrap)](#15-input-group-with-buttons-wrap)
- [16. Custom Parsing & Formatting (moment.js)](#16-custom-parsing-formatting-momentjs)
- [17. Two linked datepickers (from/to)](#17-two-linked-datepickers-fromto)
- [18. Dynamic date deactivation via the API](#18-dynamic-date-deactivation-via-the-api)

## 1. Basic (no config)

```js
flatpickr("#date");
// Or:
flatpickr("#date", {});
```

---

## 2. DateTime picker

```js
flatpickr("#datetime", {
  enableTime: true,
  dateFormat: "Y-m-d H:i"
});
```

---

## 3. Human-readable date (altInput)

altInput hides the original input and creates a new visible field.
The backend value stays in `dateFormat`, the display value in `altFormat`.

```js
flatpickr("#date", {
  altInput: true,
  altFormat: "F j, Y",       // "December 31, 2024" (for the user)
  dateFormat: "Y-m-d"        // "2024-12-31" (to the backend)
});

// German
flatpickr("#date", {
  altInput: true,
  altFormat: "j. F Y",       // "31. Dezember 2024"
  dateFormat: "Y-m-d",
  locale: "de"
});
```

---

## 4. Date formats for defaultDate

```js
// Date object
flatpickr("#date", { defaultDate: new Date(2024, 0, 15) });

// Unix timestamp
flatpickr("#date", { defaultDate: 1705276800000 });

// ISO string
flatpickr("#date", { defaultDate: "2024-01-15T00:00:00.000Z" });

// Date string (per dateFormat)
flatpickr("#date", { defaultDate: "2024-01-15" });

// Shortcut
flatpickr("#date", { defaultDate: "today" });
```

---

## 5. Preloading a date

From the input value:

```html
<input type="text" id="date" value="2024-01-15">
```

```js
flatpickr("#date", { dateFormat: "Y-m-d" });
// The value is read and preloaded automatically
```

Via `defaultDate`:

```js
flatpickr("#date", {
  defaultDate: "2024-01-15",
  dateFormat: "Y-m-d"
});
```

---

## 6. minDate / maxDate

```js
// Future dates only
flatpickr("#date", { minDate: "today" });

// Fixed range
flatpickr("#date", { minDate: "2024-01-01", maxDate: "2024-12-31" });

// 2 weeks from today
flatpickr("#date", {
  minDate: "today",
  maxDate: new Date().fp_incr(14)
});

// German format
flatpickr("#date", {
  dateFormat: "d.m.Y",
  maxDate: "31.12.2024"
});
```

---

## 7. Blocking dates (disable)

### Individual dates

```js
flatpickr("#date", {
  disable: ["2024-01-01", "2024-12-25", new Date(2024, 4, 1)]
});
```

### Date ranges

```js
flatpickr("#date", {
  dateFormat: "Y-m-d",
  disable: [
    { from: "2024-04-01", to: "2024-04-30" },  // April blocked
    { from: "2024-08-01", to: "2024-08-31" }   // August blocked
  ]
});
```

### By function (true = blocked)

```js
// Block weekends
flatpickr("#date", {
  disable: [
    function(date) {
      return date.getDay() === 0 || date.getDay() === 6;
    }
  ],
  locale: { firstDayOfWeek: 1 }
});

// Block every 13th
flatpickr("#date", {
  disable: [date => date.getDate() === 13]
});
```

### Combined

```js
flatpickr("#date", {
  disable: [
    "2024-01-01",
    { from: "2024-04-01", to: "2024-04-07" },
    function(date) { return date.getDay() === 0; }
  ]
});
```

---

## 8. Allowing only certain dates (enable)

```js
// Only these dates are selectable
flatpickr("#date", {
  enable: ["2024-03-30", "2024-05-21", new Date(2024, 8, 9)]
});

// Only certain ranges
flatpickr("#date", {
  enable: [
    { from: "2024-04-01", to: "2024-05-01" },
    { from: "2024-09-01", to: "2024-12-01" }
  ]
});

// By function (true = allowed)
flatpickr("#date", {
  enable: [
    function(date) {
      // Even months only, first half of the month
      return date.getMonth() % 2 === 0 && date.getDate() < 15;
    }
  ]
});
```

---

## 9. Multiple selection (multiple)

```js
flatpickr("#date", {
  mode: "multiple",
  dateFormat: "Y-m-d"
});

// Preloading
flatpickr("#date", {
  mode: "multiple",
  dateFormat: "Y-m-d",
  defaultDate: ["2024-06-01", "2024-06-15", "2024-06-30"]
});

// Customize the separator
flatpickr("#date", {
  mode: "multiple",
  conjunction: " :: "   // default: comma
});
```

---

## 10. Date range (range)

```js
// Simple
flatpickr("#date", { mode: "range" });

// With constraints
flatpickr("#date", {
  mode: "range",
  minDate: "today",
  dateFormat: "Y-m-d",
  disable: [function(date) { return !(date.getDate() % 8); }]
});

// Preloading
flatpickr("#date", {
  mode: "range",
  dateFormat: "Y-m-d",
  defaultDate: ["2024-06-01", "2024-06-30"]
});

// Evaluation
flatpickr("#date", {
  mode: "range",
  onChange: function(selectedDates) {
    if (selectedDates.length === 2) {
      const [start, end] = selectedDates;
      const days = Math.round((end - start) / (1000 * 60 * 60 * 24));
      console.log("Selected:", days, "days");
    }
  }
});
```

---

## 11. Time picker (without calendar)

```js
// 12-hour with AM/PM
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "h:i K"
});

// 24-hour
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  time_24hr: true
});

// With seconds
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  enableSeconds: true,
  dateFormat: "H:i:S",
  time_24hr: true
});

// With time limits
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  minTime: "09:00",
  maxTime: "17:00"
});

// Prefilled
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  defaultDate: "13:45"
});
```

---

## 12. DateTime with time limits

```js
flatpickr("#date", {
  enableTime: true,
  minTime: "09:00",
  maxTime: "17:00"
});
```

---

## 13. Inline calendar (always visible)

```html
<div id="calendar"></div>
```

```js
flatpickr("#calendar", {
  inline: true,
  onChange: function(selectedDates, dateStr) {
    document.getElementById("result").textContent = dateStr;
  }
});
```

---

## 14. Week numbers

```js
flatpickr("#date", {
  weekNumbers: true,
  // Your own calculation (optional)
  getWeek: function(dateObj) {
    const date = new Date(dateObj.valueOf());
    const dayNum = (date.getDay() + 6) % 7;
    date.setDate(date.getDate() - dayNum + 3);
    const firstThursday = date.valueOf();
    date.setMonth(0, 1);
    if (date.getDay() !== 4) {
      date.setMonth(0, 1 + ((4 - date.getDay() + 7) % 7));
    }
    return 1 + Math.ceil((firstThursday - date) / 604800000);
  }
});
```

---

## 15. Input group with buttons (wrap)

```html
<!-- Bootstrap input-group example -->
<div class="flatpickr input-group">
  <input type="text" placeholder="Choose a date" data-input class="form-control">
  <button class="btn btn-outline-secondary" type="button" data-toggle>
    <i class="bi bi-calendar"></i>
  </button>
  <button class="btn btn-outline-secondary" type="button" data-clear>
    <i class="bi bi-x"></i>
  </button>
</div>
```

```js
flatpickr(".flatpickr", { wrap: true });
```

**Data attributes:**

| Attribute | Function |
|---------|---------|
| `data-input` | The actual input field |
| `data-toggle` | Click opens/closes the calendar |
| `data-clear` | Click clears the selection |
| `data-open` | Click opens the calendar |
| `data-close` | Click closes the calendar |

---

## 16. Custom Parsing & Formatting (moment.js)

```js
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

---

## 17. Two linked datepickers (from/to)

```js
const fromPicker = flatpickr("#from", {
  onChange: function(selectedDates) {
    toPicker.set("minDate", selectedDates[0]);
  }
});

const toPicker = flatpickr("#to", {
  onChange: function(selectedDates) {
    fromPicker.set("maxDate", selectedDates[0]);
  }
});
```

---

## 18. Dynamic date deactivation via the API

```js
const fp = flatpickr("#date", {});

// Load dates from the backend and block them
fetch("/api/blocked-dates")
  .then(r => r.json())
  .then(dates => {
    fp.set("disable", dates); // ["2024-06-15", "2024-06-20"]
  });
```

---

Source: https://flatpickr.js.org/examples/
