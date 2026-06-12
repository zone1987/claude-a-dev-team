# flatpickr — Plugins (vollständige Referenz, v4.6.13)

Quelle: `src/plugins/*` (8 Plugins, Stand v4.6.13).

## Plugin-Konzept

Plugins sind Funktionen, die eine optionale Konfiguration und die flatpickr-Instanz erhalten
und ein Objekt mit Hook-Funktionen zurückgeben. Sie werden im `plugins`-Array übergeben.

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

Zeigt einen Bestätigungs-Button nachdem der Nutzer Datum+Zeit oder mehrere Daten ausgewählt hat.
Verhindert ungewolltes Schließen des Kalenders.

### Import

```js
// ES Module
import confirmDatePlugin from "flatpickr/dist/plugins/confirmDate/confirmDate.js";
import "flatpickr/dist/plugins/confirmDate/confirmDate.css";

// Browser
// <script src="https://npmcdn.com/flatpickr/dist/plugins/confirmDate/confirmDate.js"></script>
// <link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/plugins/confirmDate/confirmDate.css">
```

### Config-Interface (`src/plugins/confirmDate/confirmDate.ts`)

```typescript
interface Config {
  confirmIcon?: string;   // Default: SVG-Häkchen
  confirmText?: string;   // Default: "OK "
  showAlways?: boolean;   // Default: false
  theme?: string;         // Default: "light"
}
```

### Konfigurationsoptionen

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `confirmIcon` | `String` | SVG-Häkchen | HTML für das Bestätigungs-Icon |
| `confirmText` | `String` | `"OK "` | Text des Bestätigungs-Buttons |
| `showAlways` | `Boolean` | `false` | Button immer sichtbar (nicht nur nach Auswahl) |
| `theme` | `String` | `"light"` | CSS-Theme: `"light"` oder `"dark"` |

### Verwendung

```js
flatpickr("#date", {
  enableTime: true,
  plugins: [confirmDatePlugin({
    confirmIcon: "<i class='fa fa-check'></i>",
    confirmText: "Bestätigen",
    showAlways: false,
    theme: "light"
  })]
});

// Einfachste Form
flatpickr("#date", {
  enableTime: true,
  plugins: [confirmDatePlugin({})]
});

// Mit Multiple-Modus
flatpickr("#date", {
  mode: "multiple",
  plugins: [confirmDatePlugin({ confirmText: "OK" })]
});
```

### Verhalten

- Taucht nach Auswahl von Datum+Zeit auf, im `multiple`-Modus oder bei `monthSelect`-Plugin
- Bei `showAlways: true` immer sichtbar
- Tab vom letzten Zeit-Element springt zum Bestätigungs-Button
- Enter auf dem Button schließt den Kalender
- Nicht aktiv bei `noCalendar: true` oder im mobilen Modus

---

## 2. rangePlugin (Beta)

Ermöglicht Datumsbereich-Auswahl mit **zwei separaten Input-Feldern** (statt einem kombinierten).

### Import

```js
import rangePlugin from "flatpickr/dist/plugins/rangePlugin.js";
```

### Config-Interface (`src/plugins/rangePlugin.ts`)

```typescript
interface Config {
  input?: string | HTMLInputElement;  // Selektor oder Element für zweites Input
  position?: "left";                  // Positionierung des Pickers
}
```

### Konfigurationsoptionen

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `input` | `String\|HTMLInputElement` | — | CSS-Selektor oder Element für das zweite Input-Feld; fehlt es, wird ein geklontes Input eingefügt |
| `position` | `String` | — | `"left"`: Picker öffnet sich relativ zum ersten Input auch wenn zweites fokussiert ist |

### Verwendung

```html
<input id="rangeStart" type="text" placeholder="Von">
<input id="rangeEnd" type="text" placeholder="Bis">
```

```js
flatpickr("#rangeStart", {
  plugins: [rangePlugin({ input: "#rangeEnd" })]
});
```

### Verhalten

- Das erste Input enthält das Start-Datum, das zweite das End-Datum
- Klick auf das zweite Input öffnet den Picker und springt zum bereits gewählten End-Datum
- Setzt `fp.config.mode = "range"` automatisch
- Kompatibler mit Formularen als `mode: "range"` (zwei separate Werte)
- Unterstützt `allowInput: true`

---

## 3. weekSelect

Ermöglicht die Auswahl einer ganzen Woche. Keine Konfigurationsparameter.

### Import

```js
import weekSelectPlugin from "flatpickr/dist/plugins/weekSelect/weekSelect.js";
```

### Config-Interface

Kein Config-Interface — das Plugin nimmt keine Parameter.

### Verwendung

```js
flatpickr("#date", {
  plugins: [weekSelectPlugin()],
  onChange: function() {
    const weekNumber = this.selectedDates[0]
      ? this.config.getWeek(this.selectedDates[0])
      : null;
    console.log("Ausgewählte Woche:", weekNumber);
  }
});
```

### Instanz-Erweiterungen (PlusWeeks)

```typescript
type PlusWeeks = {
  weekStartDay: Date;  // Erster Tag der gewählten Woche
  weekEndDay: Date;    // Letzter Tag der gewählten Woche
};
```

```js
console.log(fp.weekStartDay); // Montag der gewählten Woche
console.log(fp.weekEndDay);   // Sonntag der gewählten Woche
```

### Verhalten

- Hover über einen Tag markiert die gesamte Woche (`inRange`-Klasse)
- Klick wählt alle 7 Tage der Woche aus
- Setzt `fp.config.mode = "single"` und `fp.config.enableTime = false` automatisch
- `dateFormat` default: `"\\W\\e\\e\\k #W, Y"` (z.B. "Week #24, 2024")

---

## 4. monthSelectPlugin

Zeigt eine Monatsauswahl — keine Tagesauswahl.

### Import

```js
import monthSelectPlugin from "flatpickr/dist/plugins/monthSelect/index.js";
import "flatpickr/dist/plugins/monthSelect/style.css";
```

### Config-Interface (`src/plugins/monthSelect/index.ts`)

```typescript
interface Config {
  shorthand: boolean;    // Default: false
  dateFormat: string;    // Default: "F Y"
  altFormat: string;     // Default: "F Y"
  theme: string;         // Default: "light"
}
```

### Konfigurationsoptionen

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `shorthand` | `Boolean` | `false` | Monatsnamen in Kurzform (`Jan` statt `January`) |
| `dateFormat` | `String` | `"F Y"` | Format des Werts im Input |
| `altFormat` | `String` | `"F Y"` | Anzeigeformat (wenn `altInput: true`) |
| `theme` | `String` | `"light"` | CSS-Theme: `"light"` oder `"dark"` |

### Verwendung

```js
flatpickr("#month", {
  plugins: [
    monthSelectPlugin({
      shorthand: true,        // "Jan 2024" statt "January 2024"
      dateFormat: "m.y",      // "01.24"
      altFormat: "F Y",       // "January 2024"
      theme: "dark"
    })
  ]
});

// Einfachste Form
flatpickr("#month", {
  plugins: [monthSelectPlugin()]
});
```

### Verhalten

- Zeigt eine Übersicht der 12 Monate (kein Kalender mit einzelnen Tagen)
- Wählt immer den ersten Tag des gewählten Monats
- Setzt `fp.config.enableTime = false` automatisch
- Pfeile im Header navigieren durch die Jahre
- Kompatibel mit `altInput: true`, `mode: "range"`, `mode: "multiple"`
- CSS-Klasse: `flatpickr-monthSelect-theme-${theme}` auf `calendarContainer`

---

## 5. minMaxTimePlugin (Beta)

Erlaubt individuelle Zeitgrenzen pro Datum — verschiedene Min/Max-Zeiten für verschiedene Tage.

### Import

```js
import minMaxTimePlugin from "flatpickr/dist/plugins/minMaxTimePlugin.js";
```

### Config-Interface (`src/plugins/minMaxTimePlugin.ts`)

```typescript
interface MinMaxTime {
  minTime?: string;
  maxTime?: string;
}

interface Config {
  table?: Record<string, MinMaxTime>;        // Statische Tabelle: Datum-Key → Zeitgrenzen
  getTimeLimits?: (date: Date) => MinMaxTime; // Dynamische Funktion
  tableDateFormat?: string;                  // Default: "Y-m-d"
}
```

### Konfigurationsoptionen

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `table` | `Object` | — | Objekt mit Datum-Strings als Keys und `{minTime, maxTime}` als Values |
| `getTimeLimits` | `Function` | — | Funktion `(date: Date) => {minTime, maxTime}` für dynamische Grenzen |
| `tableDateFormat` | `String` | `"Y-m-d"` | Format der Datum-Keys im `table`-Objekt |

### Verwendung

```js
// Mit statischer Tabelle
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

// Mit dynamischer Funktion
flatpickr("#date", {
  enableTime: true,
  plugins: [
    minMaxTimePlugin({
      getTimeLimits: function(date) {
        // Wochentags andere Zeiten als am Wochenende
        if (date.getDay() === 0 || date.getDay() === 6) {
          return { minTime: "10:00", maxTime: "18:00" };
        }
        return { minTime: "09:00", maxTime: "20:00" };
      }
    })
  ]
});
```

### Verhalten

- Nur `table` ODER `getTimeLimits` nutzen (nicht beide)
- Wenn für ein gewähltes Datum kein Eintrag vorhanden, werden die globalen `minTime`/`maxTime` der Instanz verwendet
- Zeitgrenzen können auch über Mitternacht gehen (`minTime > maxTime`)

---

## 6. scrollPlugin

Aktiviert Mausrad-Navigation für Zeit- und Monatselemente. Keine Konfigurationsparameter.

### Import

```js
import scrollPlugin from "flatpickr/dist/plugins/scrollPlugin.js";
```

### Config-Interface

Kein Config-Interface — das Plugin nimmt keine Parameter.

### Verwendung

```js
flatpickr("#date", {
  enableTime: true,
  plugins: [scrollPlugin()]
});
```

### Verhalten

- Scrollen über Stunden/Minuten/Sekunden-Inputs ändert den Wert per `increment`-CustomEvent
- Scrollen über den Monatsnamen im Header wechselt den Monat
- Scrollen über das Jahr-Input ändert das Jahr
- IE9-Polyfill für `CustomEvent` ist eingebaut

---

## 7. momentPlugin

Integration mit [moment.js](https://momentjs.com) für Parsing/Formatierung.
Ermöglicht die Verwendung von moment-Format-Strings statt flatpickr-Tokens.

### Import

```js
import momentPlugin from "flatpickr/dist/plugins/momentPlugin.js";
import moment from "moment";
```

### Config-Interface (`src/plugins/momentPlugin.ts`)

```typescript
interface Config {
  moment: Function;  // Die moment-Funktion (Pflichtfeld)
}
```

### Verwendung

```js
flatpickr("#date", {
  plugins: [momentPlugin({ moment: moment })],
  dateFormat: "YYYY-MM-DD",  // moment-Format-Strings
  altFormat: "DD.MM.YYYY",
  altInput: true,
  locale: "de",  // moment-Locale wird automatisch übernommen
});
```

### Verhalten

- Ersetzt `parseDate` und `formatDate` der Instanz durch moment-Implementierungen
- `parseDate(datestr, format)` nutzt `moment(datestr, format, true).toDate()` (strict mode)
- `formatDate(date, format)` nutzt `momentDate.format(format)` mit optionalem locale
- Unterstützt `increment`-Events für Stunden/Minuten/Sekunden-Inputs (moment-basiertes Inkrement)
- Bei `locale`-Option als String wird moment-Locale gesetzt

**Alternativ ohne Plugin** (direkter Ansatz ohne moment-Abhängigkeit im Plugin):

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

Behebt ein Zugänglichkeitsproblem: Wenn `altInput: true` oder mobiler Modus aktiv ist,
wird die `id` des originalen Inputs auf das sichtbare Element übertragen.
Dadurch funktioniert `<label for="...">` korrekt.
Keine Konfigurationsparameter.

### Import

```js
import labelPlugin from "flatpickr/dist/plugins/labelPlugin/labelPlugin.js";
```

### Config-Interface

Kein Config-Interface — das Plugin nimmt keine Parameter.

### Verwendung

```html
<label for="myDate">Datum:</label>
<input id="myDate" type="text">
```

```js
flatpickr("#myDate", {
  altInput: true,
  plugins: [labelPlugin()]
});
// Das altInput erhält id="myDate", das original-Input verliert die id
// → Klick auf das Label öffnet korrekt den Picker
```

### Verhalten

- Bei `altInput: true`: originales Input verliert die `id`, `altInput` erhält sie
- Bei mobilem Modus: originales Input verliert die `id`, `mobileInput` erhält sie
- Wenn kein `id` vorhanden, tut das Plugin nichts

---

## Eigenes Plugin schreiben

```typescript
import { Plugin } from "flatpickr/dist/types/options";

interface MyConfig {
  option?: string;
}

function myPlugin(config: MyConfig = {}): Plugin {
  return function(fp) {
    return {
      onReady() {
        console.log("Plugin bereit:", fp);
        fp.loadedPlugins.push("myPlugin"); // Konvention: Plugin-Namen registrieren
      },
      onChange(selectedDates, dateStr) {
        console.log("onChange:", dateStr);
      },
      onDestroy() {
        // Event-Listener entfernen, aufräumen
      }
    };
  };
}

flatpickr("#date", {
  plugins: [myPlugin({ option: "value" })]
});
```

### Hooks in Plugins

Ein Plugin kann für jeden Hook auch ein Array von Funktionen zurückgeben:

```js
return {
  onReady: [fn1, fn2, fn3],
  onDestroy: [cleanup1, cleanup2],
};
```

---

Quelle: `src/plugins/*` (v4.6.13) | https://flatpickr.js.org/plugins/
