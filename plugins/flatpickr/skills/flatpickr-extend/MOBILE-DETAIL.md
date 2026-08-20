# flatpickr — Mobile Support (vollständige Referenz)

## Automatische Erkennung

flatpickr erkennt automatisch mobile Browser und schaltet auf den **nativen Datetime-Picker**
des Betriebssystems um. Dies bietet dem Nutzer die vertraute OS-Erfahrung.

Die Erkennung erfolgt über den Browser-User-Agent. Bei mobilen Geräten (iOS, Android)
wird ein natives `<input type="date">`, `<input type="datetime-local">` oder
`<input type="time">` verwendet.

## Nativ unterstützte Features

Folgende flatpickr-Features werden an den nativen Picker weitergeleitet:

| Feature | Unterstützt |
|---------|------------|
| `defaultDate` | ja |
| `minDate` | ja |
| `maxDate` | ja |
| `onChange`-Callback | ja |
| `disable` (Array/Funktion) | nein* |
| `enableTime` | ja (natives datetime-local) |
| `noCalendar` | ja (natives time) |
| Plugins | nein |

*Wenn Features verwendet werden, die nativ nicht verfügbar sind (z.B. `disable`-Funktionen),
fällt flatpickr automatisch auf den eigenen Picker zurück.

## Fallback-Verhalten

Wenn eine nicht-nativ-unterstützbare Konfiguration erkannt wird, wird der flatpickr-Picker
auch auf Mobilgeräten gezeigt:

```js
// Fällt automatisch auf flatpickr-Picker zurück (kein nativer Picker)
flatpickr("#date", {
  disable: [function(date) { return date.getDay() === 0; }]
});
```

## Nativen Picker deaktivieren

```js
flatpickr("#date", {
  disableMobile: true   // Immer flatpickr-Picker, nie nativer
});
```

**Empfehlung:** Nur verwenden wenn flatpickr-spezifische Features (z.B. Themes, Plugins,
`onDayCreate`) auf Mobilgeräten zwingend benötigt werden. Der native Picker bietet
generell bessere UX auf Mobilgeräten.

## Globale Mobile-Konfiguration

```js
// Alle Instanzen auf nativen Picker verzichten
flatpickr(".datepicker", {
  disableMobile: true
});
```

## Typ-Mapping

| flatpickr-Konfiguration | Nativer Input-Typ |
|------------------------|-------------------|
| Standard (nur Datum) | `type="date"` |
| `enableTime: true` | `type="datetime-local"` |
| `noCalendar: true`, `enableTime: true` | `type="time"` |

## Browser-Kompatibilität

| Browser/OS | Nativer Picker |
|-----------|---------------|
| iOS Safari | ja (nativ) |
| iOS Chrome | ja (nativ) |
| Android Chrome | ja (nativ) |
| Android Firefox | ja (nativ) |
| Desktop Chrome | flatpickr |
| Desktop Firefox | flatpickr |
| Desktop Safari | flatpickr |

---

Quelle: https://flatpickr.js.org/mobile-support/
