# flatpickr — Themes (complete reference)

## Contents

- [Available themes](#available-themes)
- [Including a theme](#including-a-theme)
- [Plugin-specific themes](#plugin-specific-themes)
- [Custom styling / CSS classes](#custom-styling--css-classes)
- [Creating your own theme](#creating-your-own-theme)

## Available themes

| Theme name | CSS file | Description |
|-----------|-----------|-------------|
| Default | `flatpickr.min.css` | default theme (white/blue) |
| Dark | `themes/dark.css` | dark theme |
| Airbnb | `themes/airbnb.css` | Airbnb style (pink accents) |
| Confetti | `themes/confetti.css` | colorful theme |
| Material Blue | `themes/material_blue.css` | Material Design, blue |
| Material Green | `themes/material_green.css` | Material Design, green |
| Material Orange | `themes/material_orange.css` | Material Design, orange |
| Material Red | `themes/material_red.css` | Material Design, red |
| Light | `themes/light.css` | light theme |

## Including a theme

### Webpack / bundler

```js
// default theme (often already loaded by the flatpickr import)
import "flatpickr/dist/flatpickr.min.css";

// alternative theme (replaces the default CSS)
import "flatpickr/dist/themes/dark.css";
import "flatpickr/dist/themes/airbnb.css";
import "flatpickr/dist/themes/confetti.css";
import "flatpickr/dist/themes/material_blue.css";
import "flatpickr/dist/themes/material_green.css";
import "flatpickr/dist/themes/material_orange.css";
import "flatpickr/dist/themes/material_red.css";
import "flatpickr/dist/themes/light.css";

// CommonJS
require("flatpickr/dist/themes/dark.css");
```

### Browser / CDN

```html
<!-- default -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">

<!-- Dark theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/dark.css">

<!-- Airbnb theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/airbnb.css">

<!-- Confetti theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/confetti.css">

<!-- Material Blue -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_blue.css">

<!-- Material Green -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_green.css">

<!-- Material Orange -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_orange.css">

<!-- Material Red -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_red.css">

<!-- Light theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/light.css">
```

Note: Load only **one** theme CSS (not several at the same time).

## Plugin-specific themes

Some plugins (e.g. `confirmDatePlugin`, `monthSelectPlugin`) support their own
`theme` option:

```js
flatpickr("#date", {
  plugins: [new confirmDatePlugin({ theme: "dark" })]
});

flatpickr("#month", {
  plugins: [new monthSelectPlugin({ theme: "dark" })]
});
```

## Custom styling / CSS classes

The most important CSS classes for your own adjustments:

```css
/* calendar container */
.flatpickr-calendar { }

/* header area */
.flatpickr-months { }
.flatpickr-month { }
.flatpickr-prev-month { }
.flatpickr-next-month { }
.cur-month { }          /* month name */
.cur-year { }           /* year input */

/* weekday row */
.flatpickr-weekdays { }
.flatpickr-weekday { }

/* days */
.flatpickr-days { }
.flatpickr-day { }
.flatpickr-day.today { }        /* today */
.flatpickr-day.selected { }     /* selected day */
.flatpickr-day.inRange { }      /* day inside the range */
.flatpickr-day.startRange { }   /* range start */
.flatpickr-day.endRange { }     /* range end */
.flatpickr-day.disabled { }     /* blocked day */
.flatpickr-day.prevMonthDay { } /* day of the previous month */
.flatpickr-day.nextMonthDay { } /* day of the next month */
.flatpickr-day.flatpickr-disabled { } /* fully disabled */

/* time picker */
.flatpickr-time { }
.flatpickr-hour { }
.flatpickr-minute { }
.flatpickr-second { }
.flatpickr-am-pm { }

/* week numbers */
.flatpickr-weeknumber { }
```

## Creating your own theme

Load your own styles after the default CSS:

```css
/* my-theme.css — load after flatpickr.min.css */
.flatpickr-calendar {
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  border: none;
}

.flatpickr-day.selected,
.flatpickr-day.startRange,
.flatpickr-day.endRange {
  background: #6366f1;   /* indigo */
  border-color: #6366f1;
}

.flatpickr-day.inRange {
  background: #e0e7ff;
  border-color: #e0e7ff;
  box-shadow: -5px 0 0 #e0e7ff, 5px 0 0 #e0e7ff;
}

.flatpickr-day.today {
  border-color: #6366f1;
}

.flatpickr-month {
  background: #6366f1;
  color: white;
}

.flatpickr-prev-month,
.flatpickr-next-month {
  fill: white;
}
```

---

Source: https://flatpickr.js.org/themes/ | https://cdn.jsdelivr.net/npm/flatpickr/dist/themes/
