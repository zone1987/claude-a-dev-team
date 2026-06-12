# flatpickr — Events & Hooks (vollständige Referenz, v4.6.13)

Quelle: `src/types/options.ts` (Typ `HookKey`, Konstante `HOOKS`, Stand v4.6.13).

## Grundprinzip

Hooks werden als Options-Properties übergeben. Jeder Hook kann eine einzelne Funktion
oder ein Array von Funktionen sein.

```js
flatpickr("#date", {
  onChange: function(selectedDates, dateStr, instance) {
    console.log("Ausgewählt:", dateStr);
    console.log("Als Date-Objekt:", selectedDates[0]);
  },
  onClose: [
    function(selectedDates, dateStr, instance) { /* fn1 */ },
    function(selectedDates, dateStr, instance) { /* fn2 */ }
  ],
});
```

## Alle Hook-Keys

Vollständige Liste laut `src/types/options.ts`:

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

## Standard-Hook Signatur (Typ `Hook`)

Alle Hooks erhalten dieselbe Signatur:

```typescript
type Hook = (
  dates: Date[],              // Array der ausgewählten Daten
  currentDateString: string,  // Formatierter Datumsstring (gem. dateFormat)
  self: Instance,             // Die flatpickr-Instanz
  data?: any                  // Optionale Zusatzdaten
) => void;
```

| Parameter | Typ | Beschreibung |
|-----------|-----|-------------|
| `selectedDates` | `Date[]` | Array der ausgewählten Date-Objekte |
| `dateStr` | `String` | String-Repräsentation des zuletzt ausgewählten Datums (gem. `dateFormat`) |
| `instance` | `Instance` | Die flatpickr-Instanz mit allen Methoden und Properties |
| `data` | `any` | Optionale Zusatzdaten (bei `onDayCreate`: das HTML-Element) |

## Hooks im Detail

### `onChange`

Wird ausgelöst wenn der Nutzer ein Datum auswählt, abwählt oder die Zeit bei einem ausgewählten Datum ändert. Auch bei programmatischen Änderungen wenn `triggerChange: true`.

```js
flatpickr("#date", {
  onChange: function(selectedDates, dateStr, instance) {
    console.log("Neues Datum:", dateStr);
    console.log("Als Date:", selectedDates[0]);

    // Zweite Instanz aktualisieren (z.B. für "bis"-Datum)
    toDatePicker.set("minDate", selectedDates[0]);
  }
});
```

Bei `mode: "range"`:

```js
onChange: function(selectedDates) {
  if (selectedDates.length === 2) {
    const [from, to] = selectedDates;
    console.log("Von:", from, "Bis:", to);
  }
}
```

---

### `onOpen`

Wird ausgelöst wenn der Kalender geöffnet wird (durch Nutzer-Interaktion oder `fp.open()`).

```js
flatpickr("#date", {
  onOpen: function(selectedDates, dateStr, instance) {
    console.log("Kalender geöffnet");
    // Zum heutigen Monat springen
    instance.jumpToDate(new Date());
  }
});
```

---

### `onClose`

Wird ausgelöst wenn der Kalender geschlossen wird (durch Nutzer-Interaktion oder `fp.close()`).

```js
flatpickr("#date", {
  onClose: function(selectedDates, dateStr, instance) {
    console.log("Kalender geschlossen, Wert:", dateStr);
    // Validierung beim Schließen
    if (!dateStr) {
      instance.setDate(new Date());
    }
  }
});
```

---

### `onReady`

Wird **einmalig** ausgelöst wenn der Kalender vollständig initialisiert ist (nach allen Plugin-`onReady`-Hooks).

```js
flatpickr("#date", {
  onReady: function(selectedDates, dateStr, instance) {
    console.log("flatpickr initialisiert:", instance);
    // Externe Referenz setzen
    window.myPicker = instance;
  }
});
```

---

### `onValueUpdate`

Wird ausgelöst wenn der Input-Wert mit einem neuen Datumsstring aktualisiert wird.
Kann häufiger als `onChange` ausgelöst werden (auch bei Hover, partiellem Input, etc.).

```js
flatpickr("#date", {
  onValueUpdate: function(selectedDates, dateStr, instance) {
    // Wird auch bei programmatischer Änderung ausgelöst
    document.getElementById("display").textContent = dateStr;
  }
});
```

---

### `onMonthChange`

Wird ausgelöst wenn der angezeigte Monat wechselt (durch Nutzer oder programmatisch via `changeMonth()`).

```js
flatpickr("#date", {
  onMonthChange: function(selectedDates, dateStr, instance) {
    console.log("Monat:", instance.currentMonth, "Jahr:", instance.currentYear);
    // Verfügbare Daten dynamisch nachladen
    loadAvailableDates(instance.currentYear, instance.currentMonth);
  }
});
```

---

### `onYearChange`

Wird ausgelöst wenn das angezeigte Jahr wechselt (durch Nutzer oder programmatisch).

```js
flatpickr("#date", {
  onYearChange: function(selectedDates, dateStr, instance) {
    console.log("Jahr gewechselt:", instance.currentYear);
  }
});
```

---

### `onDayCreate`

Wird für jedes Tages-DOM-Element beim Rendern des Kalenders aufgerufen.
Ermöglicht vollständige Kontrolle über jeden Kalendertag.
Das 4. Argument `data` ist hier das `DayElement` (HTMLSpanElement mit `.dateObj`-Property).

```js
flatpickr("#date", {
  onDayCreate: function(dObj, dStr, fp, dayElem) {
    // dayElem ist ein DayElement (HTMLSpanElement & { dateObj: Date; $i: number })
    
    // Tooltip hinzufügen
    dayElem.title = "Klick für " + dStr;

    // Event-Punkt hinzufügen
    if (hasEvent(dObj)) {
      dayElem.innerHTML += "<span class='event-dot'></span>";
    }

    // Bestimmte Tage markieren
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

Wird nach dem Parsen der Konfiguration ausgelöst. Erlaubt Manipulation der `ParsedOptions`
bevor der Kalender aufgebaut wird. Wird auch von Plugins genutzt (`rangePlugin`, `weekSelect`, `monthSelect`).

```js
flatpickr("#date", {
  onParseConfig: function(selectedDates, dateStr, instance) {
    // Konfig nach dem Parsen anpassen
    // Achtung: instance.config ist zu diesem Zeitpunkt noch im Aufbau
    console.log("Konfig geparsed");
  }
});
```

---

### `onDestroy`

Wird ausgelöst bevor die flatpickr-Instanz zerstört wird (`fp.destroy()`).
Nützlich für Aufräumarbeiten in Plugins und Integrations-Code.

```js
flatpickr("#date", {
  onDestroy: function(selectedDates, dateStr, instance) {
    console.log("Picker wird entfernt");
    // Externe Referenzen freigeben
    window.myPicker = null;
    // Eigene Event-Listener entfernen
    document.removeEventListener("click", myHandler);
  }
});
```

---

### `onKeyDown`

Wird bei gültigen Tastatureingaben im Kalender ausgelöst.
Das 4. Argument `data` ist das `KeyboardEvent`.

```js
flatpickr("#date", {
  onKeyDown: function(selectedDates, dateStr, instance, event) {
    // event ist das KeyboardEvent
    if (event.key === "Enter") {
      console.log("Enter gedrückt");
    }
    if (event.key === "Escape") {
      instance.close();
    }
  }
});
```

---

### `onPreCalendarPosition`

Wird unmittelbar vor der Positionierungsberechnung des Kalenders ausgelöst.
Nützlich für Plugins, die das `positionElement` dynamisch ändern müssen (z.B. `rangePlugin`).

```js
flatpickr("#date", {
  onPreCalendarPosition: function(selectedDates, dateStr, instance) {
    // Vor der Positionierung: kann instance._positionElement überschreiben
    console.log("Kalender wird positioniert");
  }
});
```

---

## Hooks nach Initialisierung manipulieren

```js
const fp = flatpickr("#date", { onChange: originalHandler });

// Weiteren Handler hinzufügen
fp.config.onChange.push(function(selectedDates, dateStr) {
  console.log("Zusätzlicher Handler:", dateStr);
});

// Handler vollständig ersetzen
fp.config.onChange = [newHandler];
```

## Hooks via `set()` dynamisch setzen

```js
const fp = flatpickr("#date", {});

fp.set("onChange", function(selectedDates, dateStr) {
  console.log("Dynamisch gesetzt:", dateStr);
});
```

## Mehrere Hooks gleichzeitig als Array

```js
flatpickr("#date", {
  onReady: [
    function(selectedDates, dateStr, fp) { /* Initialisierung A */ },
    function(selectedDates, dateStr, fp) { /* Initialisierung B */ },
  ],
  onDestroy: [cleanupA, cleanupB],
});
```

---

Quelle: `src/types/options.ts` (v4.6.13) | https://flatpickr.js.org/events/
