# flatpickr — Themes (vollständige Referenz)

## Verfügbare Themes

| Theme-Name | CSS-Datei | Beschreibung |
|-----------|-----------|-------------|
| Default | `flatpickr.min.css` | Standardtheme (weiß/blau) |
| Dark | `themes/dark.css` | Dunkles Theme |
| Airbnb | `themes/airbnb.css` | Airbnb-Stil (rosa Akzente) |
| Confetti | `themes/confetti.css` | Farbenfrohes Theme |
| Material Blue | `themes/material_blue.css` | Material Design, blau |
| Material Green | `themes/material_green.css` | Material Design, grün |
| Material Orange | `themes/material_orange.css` | Material Design, orange |
| Material Red | `themes/material_red.css` | Material Design, rot |
| Light | `themes/light.css` | Helles Theme |

## Theme einbinden

### Webpack / Bundler

```js
// Standard-Theme (wird oft bereits durch flatpickr-Import geladen)
import "flatpickr/dist/flatpickr.min.css";

// Alternatives Theme (ersetzt das Standard-CSS)
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
<!-- Standard -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">

<!-- Dark Theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/dark.css">

<!-- Airbnb Theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/airbnb.css">

<!-- Confetti Theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/confetti.css">

<!-- Material Blue -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_blue.css">

<!-- Material Green -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_green.css">

<!-- Material Orange -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_orange.css">

<!-- Material Red -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/material_red.css">

<!-- Light Theme -->
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/themes/light.css">
```

Hinweis: Nur **ein** Theme-CSS laden (nicht mehrere gleichzeitig).

## Plugin-spezifische Themes

Manche Plugins (z.B. `confirmDatePlugin`, `monthSelectPlugin`) unterstützen eine eigene
`theme`-Option:

```js
flatpickr("#date", {
  plugins: [new confirmDatePlugin({ theme: "dark" })]
});

flatpickr("#month", {
  plugins: [new monthSelectPlugin({ theme: "dark" })]
});
```

## Custom Styling / CSS-Klassen

Die wichtigsten CSS-Klassen für eigene Anpassungen:

```css
/* Kalender-Container */
.flatpickr-calendar { }

/* Header-Bereich */
.flatpickr-months { }
.flatpickr-month { }
.flatpickr-prev-month { }
.flatpickr-next-month { }
.cur-month { }          /* Monatsname */
.cur-year { }           /* Jahres-Input */

/* Wochentage-Zeile */
.flatpickr-weekdays { }
.flatpickr-weekday { }

/* Tage */
.flatpickr-days { }
.flatpickr-day { }
.flatpickr-day.today { }        /* Heutiger Tag */
.flatpickr-day.selected { }     /* Ausgewählter Tag */
.flatpickr-day.inRange { }      /* Tag im Bereich */
.flatpickr-day.startRange { }   /* Bereichs-Start */
.flatpickr-day.endRange { }     /* Bereichs-Ende */
.flatpickr-day.disabled { }     /* Gesperrter Tag */
.flatpickr-day.prevMonthDay { } /* Tag des Vormonats */
.flatpickr-day.nextMonthDay { } /* Tag des Folgemonats */
.flatpickr-day.flatpickr-disabled { } /* Vollständig deaktiviert */

/* Zeitpicker */
.flatpickr-time { }
.flatpickr-hour { }
.flatpickr-minute { }
.flatpickr-second { }
.flatpickr-am-pm { }

/* Wochennummern */
.flatpickr-weeknumber { }
```

## Eigenes Theme erstellen

Eigene Styles nach dem Standard-CSS laden:

```css
/* my-theme.css — nach flatpickr.min.css laden */
.flatpickr-calendar {
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  border: none;
}

.flatpickr-day.selected,
.flatpickr-day.startRange,
.flatpickr-day.endRange {
  background: #6366f1;   /* Indigo */
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

Quelle: https://flatpickr.js.org/themes/ | https://cdn.jsdelivr.net/npm/flatpickr/dist/themes/
