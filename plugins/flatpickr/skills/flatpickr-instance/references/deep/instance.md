# flatpickr — Instanz-API (vollständige Referenz, v4.6.13)

Quelle: `src/types/instance.ts` (autoritativ, Stand v4.6.13).

```js
const fp = flatpickr("#date", { enableTime: true });
```

---

## Methoden

### `open(e?, positionElement?)`

Öffnet den Kalender.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `e` | `FocusEvent\|MouseEvent` | Optionales Event (wird meist weggelassen) |
| `positionElement` | `HTMLElement` | Optionales Element für die Positionierung |

```js
fp.open();
```

---

### `close()`

Schließt den Kalender.

```js
fp.close();
```

---

### `toggle()`

Öffnet den Kalender wenn geschlossen, schließt ihn wenn geöffnet.

```js
fp.toggle();
```

---

### `clear(emitChangeEvent?, toInitial?)`

Setzt die Auswahl zurück und leert das Input-Feld.

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|-------------|
| `emitChangeEvent` | `Boolean` | `true` | Ob `onChange` ausgelöst werden soll |
| `toInitial` | `Boolean` | `false` | Auf den Initialzustand zurücksetzen |

```js
fp.clear();
fp.clear(false); // kein onChange-Event
```

---

### `destroy()`

Entfernt die flatpickr-Instanz vollständig: entfernt Event-Listener, stellt das Original-Input
wieder her. Nach `destroy()` ist die Instanz nicht mehr verwendbar.

```js
fp.destroy();
```

---

### `changeMonth(value, isOffset?, fromKeyboard?)`

Wechselt den angezeigten Monat.

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|-------------|
| `value` | `Number` | — | Monatswert |
| `isOffset` | `Boolean` | `true` | `true`: Monatszahl als Offset; `false`: absoluter Monat (0–11) |
| `fromKeyboard` | `Boolean` | `false` | Gibt an ob die Aktion per Tastatur ausgelöst wurde |

```js
fp.changeMonth(1);         // einen Monat vorwärts
fp.changeMonth(-2);        // zwei Monate rückwärts
fp.changeMonth(0, false);  // zu Januar springen (absolut)
fp.changeMonth(11, false); // zu Dezember springen (absolut)
```

---

### `changeYear(year)`

Wechselt das angezeigte Jahr direkt auf den angegebenen Wert.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `year` | `Number` | Das Zieljahr (4-stellig) |

```js
fp.changeYear(2025);
```

---

### `formatDate(dateObj, formatStr)`

Gibt einen formatierten Datumsstring zurück.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `dateObj` | `Date` | Das zu formatierende Date-Objekt |
| `formatStr` | `String` | Format-Pattern (gleiche Tokens wie `dateFormat`) |

**Rückgabe:** `String`

```js
fp.formatDate(new Date(), "Y-m-d");       // "2024-12-31"
fp.formatDate(new Date(), "d.m.Y H:i");  // "31.12.2024 14:30"
```

---

### `isEnabled(date, timeless?)`

Prüft ob ein bestimmtes Datum wählbar ist (nicht durch `disable`/`enable` oder `minDate`/`maxDate` gesperrt).

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|-------------|
| `date` | `String\|Date\|Number` | — | Das zu prüfende Datum |
| `timeless` | `Boolean` | `true` | Uhrzeit bei der Prüfung ignorieren |

**Rückgabe:** `Boolean`

```js
fp.isEnabled("2024-12-25"); // false wenn gesperrt
fp.isEnabled(new Date());   // true wenn heute wählbar
```

---

### `jumpToDate(date?, triggerChange?)`

Setzt die Kalenderansicht auf Jahr und Monat des angegebenen Datums. Wählt das Datum
nicht aus — nur Navigation.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `date` | `String\|Date\|undefined` | Zieldatum; `undefined` → springt zum letzten gewählten Datum, `minDate` oder heute |
| `triggerChange` | `Boolean` | Ob Monat/Jahr-Change-Hooks ausgelöst werden sollen |

```js
fp.jumpToDate("2025-06-01");
fp.jumpToDate(new Date(), true);
fp.jumpToDate(); // springt zum aktuell gewählten oder heutigem Datum
```

---

### `parseDate(date, givenFormat?, timeless?)`

Konvertiert einen Datumsstring oder Timestamp in ein Date-Objekt.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `date` | `Date\|String\|Number` | Datumsstring, Timestamp oder Date-Objekt |
| `givenFormat` | `String` | Erwartetes Format (optional) |
| `timeless` | `Boolean` | Zeit-Anteil ignorieren |

**Rückgabe:** `Date | undefined`

```js
fp.parseDate("31.12.2024", "d.m.Y"); // → Date Object
fp.parseDate("2024-12-31", "Y-m-d"); // → Date Object
```

---

### `redraw()`

Zeichnet den Kalender neu. Notwendig z.B. nach DOM-Manipulation am Kalender.

```js
fp.redraw();
```

---

### `set(option, value?)`

Aktualisiert eine Konfig-Option und zeichnet den Kalender bei Bedarf neu.
Kann auch ein Objekt mit mehreren Optionen übergeben werden.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `option` | `String\|Object` | Name der Konfig-Property oder Objekt mit mehreren Optionen |
| `value` | `*` | Neuer Wert (wenn `option` ein String ist) |

```js
fp.set("minDate", "today");
fp.set("maxDate", new Date().fp_incr(14)); // 14 Tage ab heute
fp.set("dateFormat", "d.m.Y");
fp.set("disable", [function(date) { return date.getDay() === 0; }]);
fp.set("onChange", newHandler);

// Mehrere Optionen auf einmal
fp.set({ minDate: "2024-01-01", maxDate: "2024-12-31" });
```

---

### `setDate(date, triggerChange?, format?)`

Setzt das ausgewählte Datum programmatisch.

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `date` | `String\|Date\|Number\|Array` | Datum oder Daten-Array |
| `triggerChange` | `Boolean` | Ob `onChange`-Hooks ausgelöst werden |
| `format` | `String` | Format des Datumsstrings (wenn von `dateFormat` abweichend) |

```js
fp.setDate("2024-06-15");                          // mit dateFormat
fp.setDate(new Date());                            // heute
fp.setDate("15.06.2024", true, "d.m.Y");          // anderes Format
fp.setDate(["2024-06-01", "2024-06-30"]);          // Range oder Multiple
fp.setDate(["2024-06-01", "2024-06-30"], true);    // mit onChange-Trigger
```

---

### `updateValue(triggerChange?)`

Aktualisiert den Wert des Input-Feldes basierend auf den aktuell gewählten Daten.

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|-------------|
| `triggerChange` | `Boolean` | `true` | Ob `onChange`-Hooks ausgelöst werden sollen |

```js
fp.updateValue();
fp.updateValue(false); // ohne Event
```

---

### `pad(num)`

Hilfsfunktion: gibt eine auf 2 Stellen aufgefüllte Zahl zurück.

```js
fp.pad(5);  // "05"
fp.pad(12); // "12"
```

---

## Properties

### `selectedDates`

- **Typ:** `Date[]`
- Array der aktuell ausgewählten Date-Objekte (leer wenn nichts ausgewählt)

```js
const dates = fp.selectedDates;
if (dates.length > 0) {
  console.log("Erstes Datum:", dates[0]);
}
// Range: dates[0] = Start, dates[1] = Ende
```

### `currentYear`

- **Typ:** `Number`
- Das im Kalender angezeigte Jahr

```js
console.log(fp.currentYear); // z.B. 2024
```

### `currentMonth`

- **Typ:** `Number` (0–11)
- Der im Kalender angezeigte Monat (0 = Januar, 11 = Dezember)

```js
console.log(fp.currentMonth); // 0–11
const monthName = ["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"][fp.currentMonth];
```

### `config`

- **Typ:** `ParsedOptions`
- Die aktive Konfiguration (Defaults + User-Optionen, vollständig geparst)
- Hooks sind als Arrays zugänglich und können manipuliert werden

```js
console.log(fp.config.dateFormat);
fp.config.onChange.push(additionalHandler);
```

### `isOpen`

- **Typ:** `Boolean`
- `true` wenn der Kalender aktuell geöffnet ist

```js
if (!fp.isOpen) fp.open();
```

### `isMobile`

- **Typ:** `Boolean`
- `true` wenn flatpickr im mobilen Modus läuft (nativer Picker)

```js
if (!fp.isMobile) {
  fp.calendarContainer.classList.add("custom-class");
}
```

### `latestSelectedDateObj`

- **Typ:** `Date | undefined`
- Das zuletzt gewählte Date-Objekt (auch bei Range-Auswahl: das zuletzt angeklickte Ende)

```js
console.log(fp.latestSelectedDateObj);
```

### `now`

- **Typ:** `Date`
- Das "Heute"-Datum (kann mit Option `now` überschrieben sein)

```js
console.log(fp.now); // aktuelles Datum
```

### `l10n`

- **Typ:** `Locale`
- Das aktive Locale-Objekt

```js
console.log(fp.l10n.months.longhand[fp.currentMonth]);
```

### `loadedPlugins`

- **Typ:** `string[]`
- Namen der geladenen Plugins (Plugins fügen sich selbst per `fp.loadedPlugins.push("name")` ein)

```js
console.log(fp.loadedPlugins); // z.B. ["confirmDate", "scroll"]
```

---

## DOM-Elemente

### `element`

- **Typ:** `HTMLElement`
- Das ursprüngliche Element auf dem flatpickr initialisiert wurde

### `input`

- **Typ:** `HTMLInputElement`
- Das aktive Input-Element (bei `altInput: true`: das altInput-Element intern; `_input` ist das Original)

```js
fp.input.setAttribute("placeholder", "Datum wählen");
```

### `_input`

- **Typ:** `HTMLInputElement`
- Das originale Input-Element (vor altInput-Ersatz)

### `altInput`

- **Typ:** `HTMLInputElement | undefined`
- Das durch `altInput: true` erzeugte sichtbare Input-Element

```js
if (fp.altInput) {
  fp.altInput.classList.add("my-visible-input");
}
```

### `mobileInput`

- **Typ:** `HTMLInputElement | undefined`
- Das native Input-Element im mobilen Modus

### `calendarContainer`

- **Typ:** `HTMLDivElement` (`div.flatpickr-calendar`)
- Der Kalender-Container selbst

```js
fp.calendarContainer.classList.add("my-custom-class");
```

### `days`

- **Typ:** `HTMLDivElement`
- Container-Element für alle Tages-Zellen im Kalender

### `daysContainer`

- **Typ:** `HTMLDivElement | undefined`
- Äußerer Container der Tages-Elemente

### `monthNav`

- **Typ:** `HTMLDivElement`
- Der Monatsnavigations-Container (enthält Pfeile, Monat, Jahr)

### `prevMonthNav`

- **Typ:** `HTMLElement`
- Der "Zurück"-Pfeil für die Monatsnavigation

### `nextMonthNav`

- **Typ:** `HTMLElement`
- Der "Vorwärts"-Pfeil für die Monatsnavigation

### `currentMonthElement`

- **Typ:** `HTMLSpanElement`
- Das `<span>` mit dem aktuellen Monatsnamen (erstes Monat-Element)

### `currentYearElement`

- **Typ:** `HTMLInputElement`
- Das `<input>` mit dem aktuellen Jahr (erstes Jahr-Element)

### `monthElements`

- **Typ:** `HTMLSpanElement[]`
- Array aller Monats-Elemente (bei `showMonths > 1` mehrere)

### `yearElements`

- **Typ:** `HTMLInputElement[]`
- Array aller Jahr-Elemente (bei `showMonths > 1` mehrere)

### `monthsDropdownContainer`

- **Typ:** `HTMLSelectElement`
- Das `<select>` Element für die Monats-Dropdown-Navigation (`monthSelectorType: "dropdown"`)

### `weekdayContainer`

- **Typ:** `HTMLDivElement`
- Container für die Wochentags-Header (Mo, Di, Mi, ...)

### `weekWrapper`

- **Typ:** `HTMLDivElement | undefined`
- Äußerer Wrapper für Wochennummern-Anzeige (nur wenn `weekNumbers: true`)

### `weekNumbers`

- **Typ:** `HTMLDivElement | undefined`
- Container für die Wochennummern-Spalte (nur wenn `weekNumbers: true`)

### `timeContainer`

- **Typ:** `HTMLDivElement | undefined`
- Container für den Zeitpicker (nur wenn `enableTime: true`)

### `hourElement`

- **Typ:** `HTMLInputElement | undefined`
- Das Stunden-Input im Zeitpicker

```js
if (fp.hourElement) {
  console.log("Aktuelle Stunde:", fp.hourElement.value);
}
```

### `minuteElement`

- **Typ:** `HTMLInputElement | undefined`
- Das Minuten-Input im Zeitpicker

### `secondElement`

- **Typ:** `HTMLInputElement | undefined`
- Das Sekunden-Input (nur wenn `enableSeconds: true`)

### `amPM`

- **Typ:** `HTMLSpanElement | undefined`
- Das AM/PM-Toggle-Element (nur wenn `time_24hr: false` und `enableTime: true`)

### `selectedDateElem`

- **Typ:** `DayElement | undefined`
- Das DOM-Element des zuletzt ausgewählten Tages

### `todayDateElem`

- **Typ:** `DayElement | undefined`
- Das DOM-Element des heutigen Tages im Kalender

### `pluginElements`

- **Typ:** `Node[]`
- DOM-Elemente, die von Plugins hinzugefügt wurden

---

## DayElement-Typ

```typescript
type DayElement = HTMLSpanElement & {
  dateObj: Date;  // Das Datum des Tages
  $i: number;     // Index im Kalender-Grid (0–41)
};
```

Wird in `onDayCreate` und `weekSelect`-Plugin verwendet.

---

## Statische Hilfsfunktionen

Verfügbar direkt auf dem `flatpickr`-Objekt (nicht auf der Instanz):

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

Vergleicht zwei Datumsangaben. Gibt negative Zahl, 0 oder positive Zahl zurück.

```js
flatpickr.compareDates(new Date("2024-01-01"), new Date("2024-06-01")); // < 0
flatpickr.compareDates(new Date("2024-06-01"), new Date("2024-06-01")); // 0
```

### `flatpickr.localize(locale)`

Globale Lokalisierung setzen:

```js
import { German } from "flatpickr/dist/l10n/de.js";
flatpickr.localize(German);
// Jetzt verwenden alle neuen flatpickr-Instanzen Deutsch
```

### `flatpickr.setDefaults(config)`

Globale Standard-Optionen setzen (wirkt auf alle neu erstellten Instanzen):

```js
flatpickr.setDefaults({
  dateFormat: "d.m.Y",
  locale: "de",
});
```

### `flatpickr.defaultConfig`

- **Typ:** `Partial<ParsedOptions>`
- Zugriff auf die globale Standard-Konfiguration

```js
console.log(flatpickr.defaultConfig.dateFormat); // "Y-m-d"
```

### `flatpickr.l10ns`

- **Typ:** `{ [k in LocaleKey]?: CustomLocale } & { default: Locale }`
- Alle geladenen Locale-Objekte

```js
flatpickr.l10ns.default.firstDayOfWeek = 1; // Montag als erster Wochentag global
```

---

## `fp_incr` — Datums-Hilfsfunktion

flatpickr ergänzt Date-Objekte um die Methode `fp_incr(n)`:

```js
new Date().fp_incr(7)   // heute + 7 Tage
new Date().fp_incr(-3)  // heute - 3 Tage

// Typischer Anwendungsfall: maxDate auf 2 Wochen ab heute
fp.set("maxDate", new Date().fp_incr(14));
```

---

Quelle: `src/types/instance.ts` (v4.6.13) | https://flatpickr.js.org/instance-methods-properties-elements/
