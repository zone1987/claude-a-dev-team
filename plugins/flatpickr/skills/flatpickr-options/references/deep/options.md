# flatpickr — Vollständige Options-Referenz (v4.6.13)

Alle Optionen werden als zweites Argument an `flatpickr(element, options)` übergeben.
Quelle: `src/types/options.ts` + `src/types/options.ts#defaults` (autoritativ, Stand v4.6.13).

## Vollständige Options-Tabelle

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|-------------|
| `allowInput` | `Boolean` | `false` | Erlaubt dem Nutzer, Datum direkt in das Input-Feld einzutippen |
| `allowInvalidPreload` | `Boolean` | `false` | Erlaubt das Vorladen eines ungültigen Datums; wenn `false`, wird das Feld geleert wenn das angegebene Datum ungültig ist |
| `altFormat` | `String` | `"F j, Y"` | Anzeigeformat für das `altInput`-Feld (gleiche Tokens wie `dateFormat`) |
| `altInput` | `Boolean` | `false` | Zeigt dem Nutzer ein lesbares Datum (gemäß `altFormat`), sendet aber den `dateFormat`-Wert an den Server |
| `altInputClass` | `String` | `"form-control input"` | CSS-Klassen für das durch `altInput` erzeugte Input-Element (erbt bereits die Klassen des Original-Inputs) |
| `animate` | `Boolean` | `true` (außer IE) | Monat-Transitions-Animationen aktivieren (automatisch `false` im IE) |
| `appendTo` | `HTMLElement` | `undefined` | Hängt den Kalender an das angegebene DOM-Element statt an `document.body` |
| `ariaDateFormat` | `String` | `"F j, Y"` | Definiert das Datumsformat im `aria-label` der Kalendertage (für Screen Reader) |
| `autoFillDefaultTime` | `Boolean` | `true` | Ob die Standard-Zeit automatisch befüllt wird, wenn das Input leer ist und Fokus erhält oder verliert |
| `clickOpens` | `Boolean` | `true` | Öffnet den Picker beim Klick auf das Input-Element; `false` für rein programmatisches Öffnen |
| `closeOnSelect` | `Boolean` | `true` | Kalender automatisch schließen nach Datum-Auswahl |
| `conjunction` | `String` | `", "` | Trennzeichen zwischen Daten im `multiple`-Modus (z.B. `" :: "`) |
| `dateFormat` | `String` | `"Y-m-d"` | Format des Datums im Input-Element (Wert der ans Backend gesendet wird) |
| `defaultDate` | `String\|Date\|Array` | `undefined` | Vorausgewähltes Datum / vorausgewählte Daten bei Initialisierung |
| `defaultHour` | `Number` | `12` | Standardstunde im Zeitpicker wenn kein Datum gewählt ist |
| `defaultMinute` | `Number` | `0` | Standardminute im Zeitpicker wenn kein Datum gewählt ist |
| `defaultSeconds` | `Number` | `0` | Standardsekunde im Zeitpicker wenn kein Datum gewählt ist |
| `disable` | `Array` | `[]` | Array von Daten, Datumsbereichen oder Funktionen, die zu sperrende Daten definieren |
| `disableMobile` | `Boolean` | `false` | Erzwingt den flatpickr-Picker auch auf mobilen Geräten (kein nativer Picker) |
| `enable` | `Array` | `undefined` | Array von Daten/Ranges/Funktionen — wenn gesetzt, sind NUR diese Daten wählbar |
| `enableSeconds` | `Boolean` | `false` | Sekundenauswahl im Zeitpicker aktivieren |
| `enableTime` | `Boolean` | `false` | Zeitpicker aktivieren |
| `errorHandler` | `Function` | `console.warn` | Fehlerbehandlungs-Funktion `(err: Error) => void` bei ungültigen Daten |
| `formatDate` | `Function` | `undefined` | Benutzerdefinierte Formatierungsfunktion `(date, format, locale) => string`; ersetzt die eingebaute |
| `getWeek` | `Function` | ISO-8601-Berechnung | Funktion `(date: Date) => string\|number` für Wochennummer-Berechnung (bei `weekNumbers: true`) |
| `hourIncrement` | `Integer` | `1` | Schrittweite für Stunden (auch per Scrollrad) |
| `ignoredFocusElements` | `HTMLElement[]` | `[]` | Elemente, auf die geklickt werden kann ohne den Kalender zu schließen |
| `inline` | `Boolean` | `false` | Zeigt den Kalender dauerhaft (nicht als Dropdown) |
| `locale` | `String\|Object` | `"default"` | Lokalisierung: Sprachcode (`"de"`, `"ru"`) oder Locale-Objekt (partiell oder vollständig) |
| `maxDate` | `String\|Date\|Number` | `undefined` | Spätestes wählbares Datum (inklusiv) |
| `maxTime` | `String\|Date\|Number` | `undefined` | Späteste wählbare Uhrzeit |
| `minDate` | `String\|Date\|Number` | `undefined` | Frühestes wählbares Datum (inklusiv) |
| `minTime` | `String\|Date\|Number` | `undefined` | Früheste wählbare Uhrzeit |
| `minuteIncrement` | `Integer` | `5` | Schrittweite für Minuten (auch per Scrollrad) |
| `mode` | `String` | `"single"` | Auswahlmodus: `"single"`, `"multiple"`, `"range"`, `"time"` |
| `monthSelectorType` | `String` | `"dropdown"` | Monats-Anzeige im Header: `"dropdown"` oder `"static"` |
| `nextArrow` | `String` | SVG-Pfeil | HTML-Inhalt für den Pfeil zum nächsten Monat |
| `noCalendar` | `Boolean` | `false` | Blendet den Kalender aus — nur Zeitpicker (mit `enableTime: true`) |
| `now` | `String\|Date\|Number` | `new Date()` | Überschreibt "heute" für alle Datumsberechnungen (nützlich für Tests) |
| `onChange` | `Function\|Array` | `[]` | Hook: wird ausgelöst wenn Datum/Zeit geändert wird |
| `onClose` | `Function\|Array` | `[]` | Hook: wird ausgelöst wenn Kalender schließt |
| `onDayCreate` | `Function\|Array` | `[]` | Hook: für jedes Tages-DOM-Element beim Rendern (4. Param ist `dayElem`) |
| `onDestroy` | `Function\|Array` | `[]` | Hook: wird ausgelöst bevor die Instanz zerstört wird (`destroy()`) |
| `onKeyDown` | `Function\|Array` | `[]` | Hook: wird bei gültigen Tastatureingaben ausgelöst |
| `onMonthChange` | `Function\|Array` | `[]` | Hook: wird ausgelöst wenn Monat wechselt |
| `onOpen` | `Function\|Array` | `[]` | Hook: wird ausgelöst wenn Kalender öffnet |
| `onParseConfig` | `Function\|Array` | `[]` | Hook: wird nach dem Konfig-Parsen ausgelöst; erlaubt Manipulation der ParsedOptions |
| `onPreCalendarPosition` | `Function\|Array` | `[]` | Hook: wird vor der Kalender-Positionierung ausgelöst |
| `onReady` | `Function\|Array` | `[]` | Hook: wird einmalig ausgelöst wenn Kalender vollständig bereit ist |
| `onValueUpdate` | `Function\|Array` | `[]` | Hook: wird ausgelöst wenn Input-Wert aktualisiert wird (häufiger als `onChange`) |
| `onYearChange` | `Function\|Array` | `[]` | Hook: wird ausgelöst wenn Jahr wechselt |
| `parseDate` | `Function` | `undefined` | Benutzerdefinierte Parse-Funktion `(dateString, format) => Date` |
| `plugins` | `Array` | `[]` | Array von Plugin-Instanzen (jedes Plugin ist eine Funktion, die Options zurückgibt) |
| `position` | `String\|Function` | `"auto"` | Kalenderposition relativ zum Input: `"auto"`, `"above"`, `"below"`, `"auto left"`, `"auto center"`, `"auto right"`, `"above left"`, `"above center"`, `"above right"`, `"below left"`, `"below center"`, `"below right"` oder `(self, el) => void` |
| `positionElement` | `Element` | `undefined` | Referenz-Element für die Kalender-Positionierung (statt des Inputs) |
| `prevArrow` | `String` | SVG-Pfeil | HTML-Inhalt für den Pfeil zum vorherigen Monat |
| `shorthandCurrentMonth` | `Boolean` | `false` | Zeigt Monatsnamen in Kurzform (Sep statt September) |
| `showMonths` | `Integer` | `1` | Anzahl der gleichzeitig sichtbaren Kalender-Monate |
| `static` | `Boolean` | `false` | Positioniert den Kalender direkt neben dem Input (innerhalb eines Wrapper-Elements); für scrollbare Container |
| `time_24hr` | `Boolean` | `false` | 24-Stunden-Format im Zeitpicker (kein AM/PM) |
| `weekNumbers` | `Boolean` | `false` | Zeigt Wochennummern links im Kalender |
| `wrap` | `Boolean` | `false` | Aktiviert benutzerdefinierte Elemente (Buttons, Toggle, Clear) mit `data-input`, `data-toggle`, `data-clear` Attributen |

## Hook-Signatur (Typ `Hook`)

```typescript
type Hook = (
  dates: Date[],       // Array der ausgewählten Daten
  currentDateString: string,  // Formatierter Datumsstring
  self: Instance,      // Die flatpickr-Instanz
  data?: any           // Optionale Zusatzdaten (z.B. bei onDayCreate: dayElem)
) => void;
```

Alle Hooks können auch als Array übergeben werden:

```js
onChange: [handler1, handler2, handler3]
```

## Optionen im Detail

### `altInput` + `altFormat`

```js
flatpickr("#date", {
  altInput: true,
  altFormat: "F j, Y",     // "January 15, 2024" — für den Nutzer sichtbar
  dateFormat: "Y-m-d",     // "2024-01-15" — ans Backend gesendet
  altInputClass: "my-visible-input",
});
```

Das Original-Input wird versteckt, ein neues sichtbares Input mit `altFormat` angelegt.

### `animate`

```js
// Animationen deaktivieren (z.B. für Tests oder Barrierefreiheit)
flatpickr("#date", { animate: false });
```

### `autoFillDefaultTime`

```js
// Verhindert, dass beim Focusverlust ohne Datum-Auswahl die Standardzeit eingesetzt wird
flatpickr("#date", {
  enableTime: true,
  autoFillDefaultTime: false,
});
```

### `closeOnSelect`

```js
// Kalender offen lassen nach Datum-Auswahl (z.B. beim Time-Picker sinnvoll)
flatpickr("#date", {
  enableTime: true,
  closeOnSelect: false,
});
```

### `disable` — verschiedene Formen

```js
// Einzelne Daten
disable: ["2024-01-01", "2024-12-25", new Date(2024, 5, 15)]

// Datumsbereiche
disable: [
  { from: "2024-04-01", to: "2024-04-30" },
  { from: "2024-08-01", to: "2024-08-31" }
]

// Funktion (true = gesperrt)
disable: [
  function(date) {
    return date.getDay() === 0 || date.getDay() === 6; // Wochenenden
  }
]
```

### `enable`

Nur angegebene Daten sind wählbar — alle anderen werden gesperrt.

```js
enable: [
  "2024-06-01",
  { from: "2024-07-01", to: "2024-07-31" },
  function(date) { return date.getDate() === 15; } // Jeder 15.
]
```

### `errorHandler`

```js
flatpickr("#date", {
  errorHandler: (err) => {
    // Statt console.warn eigenes Error-Reporting
    myErrorTracker.log(err.message);
  }
});
```

### `getWeek`

```js
// Standard: ISO-8601-Berechnung (Donnerstag in der Woche entscheidet das Jahr)
// Überschreiben für eigene Logik:
flatpickr("#date", {
  weekNumbers: true,
  getWeek: (date) => {
    return `KW ${/* eigene Berechnung */}`;
  }
});
```

### `ignoredFocusElements`

```js
const myButton = document.getElementById("extraButton");
flatpickr("#date", {
  ignoredFocusElements: [myButton], // Klick auf myButton schließt den Kalender nicht
});
```

### `mode`

```js
// Einfachauswahl (Standard)
mode: "single"

// Mehrfachauswahl (durch conjunction getrennt im Input)
mode: "multiple"
conjunction: " :: "  // Trennzeichen anpassen (Default: ", ")

// Datumsbereich
mode: "range"

// Nur Zeit (kein Kalender — entspricht noCalendar + enableTime)
mode: "time"
```

### `now`

```js
// "Heute" überschreiben (nützlich für Tests)
flatpickr("#date", {
  now: new Date("2024-06-01"),
});
```

### `onDestroy`

```js
flatpickr("#date", {
  onDestroy: function(selectedDates, dateStr, instance) {
    // Aufräumen vor dem Destroy
    console.log("Picker wird entfernt");
  }
});
```

### `onKeyDown`

```js
flatpickr("#date", {
  onKeyDown: function(selectedDates, dateStr, instance, event) {
    // Tastatur-Eingaben abfangen
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
    // Vor der Positionierung des Kalenders
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
// String-Varianten
position: "auto"           // automatisch (Standard)
position: "above"          // immer oben
position: "below"          // immer unten
position: "auto left"      // links ausgerichtet
position: "auto center"    // zentriert
position: "auto right"     // rechts ausgerichtet
position: "above left"
position: "above center"
position: "above right"
position: "below left"
position: "below center"
position: "below right"

// Funktion (für vollständig eigene Positionierung)
position: function(self, customElement) {
  // customElement ist positionElement oder undefined
  self.calendarContainer.style.top = "100px";
  self.calendarContainer.style.left = "200px";
}
```

### `parseDate` + `formatDate` (moment.js Beispiel)

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
// Zwei Monate nebeneinander anzeigen
flatpickr("#date", { showMonths: 2 });
```

### `static`

```js
// Für scrollbare Container: Kalender-Position wird relativ zum Wrapper berechnet
flatpickr("#date", { static: true });
```

HTML muss einen Wrapper enthalten:

```html
<div class="flatpickr-wrapper">
  <input id="date" type="text">
</div>
```

### `wrap` — Input-Gruppen mit Buttons

```html
<div class="flatpickr">
  <input type="text" placeholder="Datum wählen" data-input>
  <button type="button" data-toggle>Kalender</button>
  <button type="button" data-clear>X</button>
</div>
```

```js
flatpickr(".flatpickr", { wrap: true });
```

### `inline`

```js
// Kalender immer sichtbar (kein Dropdown)
flatpickr("#container", { inline: true });
```

---

Quelle: `src/types/options.ts` (v4.6.13) | https://flatpickr.js.org/options/
