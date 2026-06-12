---
name: flatpickr-instance
description: >
  flatpickr Instanz-API: alle Methoden, Properties und DOM-Elemente.
  Trigger: "flatpickr instanz", "flatpickr instance", "flatpickr methoden", "flatpickr methods",
  "flatpickr setDate", "flatpickr open close", "flatpickr destroy", "flatpickr set option",
  "flatpickr selectedDates", "flatpickr changeMonth", "flatpickr clear", "flatpickr toggle".
---

# flatpickr — Instanz-API

```js
const fp = flatpickr("#date", { enableTime: true });

fp.open();                        // Kalender öffnen
fp.setDate("2024-06-15");         // Datum programmatisch setzen
fp.set("minDate", "today");       // Option dynamisch ändern
fp.destroy();                     // Instanz entfernen
```

## Wichtigste Methoden

| Methode | Beschreibung |
|---------|-------------|
| `open()` | Kalender öffnen |
| `close()` | Kalender schließen |
| `toggle()` | Kalender öffnen/schließen |
| `clear()` | Auswahl und Input leeren |
| `destroy()` | Instanz komplett entfernen |
| `setDate(date, triggerChange?)` | Datum setzen |
| `set(option, value)` | Config-Option ändern |
| `changeMonth(n, isOffset?)` | Monat wechseln |
| `jumpToDate(date)` | Zu Datum springen |

## Wichtigste Properties

| Property | Typ | Beschreibung |
|----------|-----|-------------|
| `selectedDates` | `Date[]` | Aktuell gewählte Daten |
| `currentYear` | `number` | Angezeigtes Jahr |
| `currentMonth` | `number` | Angezeigter Monat (0–11) |
| `config` | `object` | Aktive Konfiguration |

## Vertiefung
- [references/deep/instance.md](references/deep/instance.md) — vollständige Methoden, Properties, DOM-Elemente, statische Hilfsfunktionen
