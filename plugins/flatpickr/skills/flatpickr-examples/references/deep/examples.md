# flatpickr — Beispiele & Patterns (vollständige Referenz)

## 1. Basic (kein Config)

```js
flatpickr("#date");
// Oder:
flatpickr("#date", {});
```

---

## 2. DateTime-Picker

```js
flatpickr("#datetime", {
  enableTime: true,
  dateFormat: "Y-m-d H:i"
});
```

---

## 3. Menschenlesbares Datum (altInput)

altInput versteckt das Original-Input und erzeugt ein neues sichtbares Feld.
Der Backend-Wert bleibt in `dateFormat`, der Anzeige-Wert in `altFormat`.

```js
flatpickr("#date", {
  altInput: true,
  altFormat: "F j, Y",       // "December 31, 2024" (für Nutzer)
  dateFormat: "Y-m-d"        // "2024-12-31" (ans Backend)
});

// Deutsch
flatpickr("#date", {
  altInput: true,
  altFormat: "j. F Y",       // "31. Dezember 2024"
  dateFormat: "Y-m-d",
  locale: "de"
});
```

---

## 4. Datumsformate für defaultDate

```js
// Date-Objekt
flatpickr("#date", { defaultDate: new Date(2024, 0, 15) });

// Unix-Timestamp
flatpickr("#date", { defaultDate: 1705276800000 });

// ISO-String
flatpickr("#date", { defaultDate: "2024-01-15T00:00:00.000Z" });

// Datumsstring (gemäß dateFormat)
flatpickr("#date", { defaultDate: "2024-01-15" });

// Shortcut
flatpickr("#date", { defaultDate: "today" });
```

---

## 5. Datum vorladen

Aus dem Input-Value:

```html
<input type="text" id="date" value="2024-01-15">
```

```js
flatpickr("#date", { dateFormat: "Y-m-d" });
// Wert wird automatisch gelesen und vorgeladen
```

Über `defaultDate`:

```js
flatpickr("#date", {
  defaultDate: "2024-01-15",
  dateFormat: "Y-m-d"
});
```

---

## 6. minDate / maxDate

```js
// Nur zukünftige Daten
flatpickr("#date", { minDate: "today" });

// Fixer Bereich
flatpickr("#date", { minDate: "2024-01-01", maxDate: "2024-12-31" });

// 2 Wochen ab heute
flatpickr("#date", {
  minDate: "today",
  maxDate: new Date().fp_incr(14)
});

// Deutsches Format
flatpickr("#date", {
  dateFormat: "d.m.Y",
  maxDate: "31.12.2024"
});
```

---

## 7. Daten sperren (disable)

### Einzelne Daten

```js
flatpickr("#date", {
  disable: ["2024-01-01", "2024-12-25", new Date(2024, 4, 1)]
});
```

### Datumsbereiche

```js
flatpickr("#date", {
  dateFormat: "Y-m-d",
  disable: [
    { from: "2024-04-01", to: "2024-04-30" },  // April gesperrt
    { from: "2024-08-01", to: "2024-08-31" }   // August gesperrt
  ]
});
```

### Per Funktion (true = gesperrt)

```js
// Wochenenden sperren
flatpickr("#date", {
  disable: [
    function(date) {
      return date.getDay() === 0 || date.getDay() === 6;
    }
  ],
  locale: { firstDayOfWeek: 1 }
});

// Jeden 13. sperren
flatpickr("#date", {
  disable: [date => date.getDate() === 13]
});
```

### Kombiniert

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

## 8. Nur bestimmte Daten erlauben (enable)

```js
// Nur diese Daten wählbar
flatpickr("#date", {
  enable: ["2024-03-30", "2024-05-21", new Date(2024, 8, 9)]
});

// Nur bestimmte Bereiche
flatpickr("#date", {
  enable: [
    { from: "2024-04-01", to: "2024-05-01" },
    { from: "2024-09-01", to: "2024-12-01" }
  ]
});

// Per Funktion (true = erlaubt)
flatpickr("#date", {
  enable: [
    function(date) {
      // Nur gerade Monate, erste Monatshälfte
      return date.getMonth() % 2 === 0 && date.getDate() < 15;
    }
  ]
});
```

---

## 9. Mehrfachauswahl (multiple)

```js
flatpickr("#date", {
  mode: "multiple",
  dateFormat: "Y-m-d"
});

// Vorladen
flatpickr("#date", {
  mode: "multiple",
  dateFormat: "Y-m-d",
  defaultDate: ["2024-06-01", "2024-06-15", "2024-06-30"]
});

// Trennzeichen anpassen
flatpickr("#date", {
  mode: "multiple",
  conjunction: " :: "   // Standard: Komma
});
```

---

## 10. Datumsbereich (range)

```js
// Einfach
flatpickr("#date", { mode: "range" });

// Mit Constraints
flatpickr("#date", {
  mode: "range",
  minDate: "today",
  dateFormat: "Y-m-d",
  disable: [function(date) { return !(date.getDate() % 8); }]
});

// Vorladen
flatpickr("#date", {
  mode: "range",
  dateFormat: "Y-m-d",
  defaultDate: ["2024-06-01", "2024-06-30"]
});

// Auswertung
flatpickr("#date", {
  mode: "range",
  onChange: function(selectedDates) {
    if (selectedDates.length === 2) {
      const [start, end] = selectedDates;
      const days = Math.round((end - start) / (1000 * 60 * 60 * 24));
      console.log("Ausgewählt:", days, "Tage");
    }
  }
});
```

---

## 11. Zeit-Picker (ohne Kalender)

```js
// 12-Stunden mit AM/PM
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "h:i K"
});

// 24-Stunden
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  time_24hr: true
});

// Mit Sekunden
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  enableSeconds: true,
  dateFormat: "H:i:S",
  time_24hr: true
});

// Mit Zeitgrenzen
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  minTime: "09:00",
  maxTime: "17:00"
});

// Vorausfüllen
flatpickr("#time", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  defaultDate: "13:45"
});
```

---

## 12. DateTime mit Zeitbegrenzung

```js
flatpickr("#date", {
  enableTime: true,
  minTime: "09:00",
  maxTime: "17:00"
});
```

---

## 13. Inline-Kalender (immer sichtbar)

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

## 14. Wochennummern

```js
flatpickr("#date", {
  weekNumbers: true,
  // Eigene Berechnung (optional)
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

## 15. Input-Gruppe mit Buttons (wrap)

```html
<!-- Bootstrap Input-Group Beispiel -->
<div class="flatpickr input-group">
  <input type="text" placeholder="Datum wählen" data-input class="form-control">
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

**Datenattribute:**

| Attribut | Funktion |
|---------|---------|
| `data-input` | Das eigentliche Input-Feld |
| `data-toggle` | Klick öffnet/schließt Kalender |
| `data-clear` | Klick leert Auswahl |
| `data-open` | Klick öffnet Kalender |
| `data-close` | Klick schließt Kalender |

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

## 17. Zwei verknüpfte Datepicker (Von/Bis)

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

## 18. Dynamische Datumsdeaktivierung via API

```js
const fp = flatpickr("#date", {});

// Daten aus Backend laden und sperren
fetch("/api/blocked-dates")
  .then(r => r.json())
  .then(dates => {
    fp.set("disable", dates); // ["2024-06-15", "2024-06-20"]
  });
```

---

Quelle: https://flatpickr.js.org/examples/
