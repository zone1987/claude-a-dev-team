# flatpickr — Vollständige Formatierungs-Referenz (v4.6.13)

Tokens werden in `dateFormat`, `altFormat`, `ariaDateFormat` verwendet.
Quelle: `src/utils/formatting.ts` (autoritativ, Stand v4.6.13).

## Alle Tokens

### Tag

| Token | Beschreibung | Beispiel | Quelle |
|-------|-------------|---------|--------|
| `d` | Tag des Monats, 2-stellig mit führender Null | `01` bis `31` | `formats.d` |
| `D` | Wochentag, Kurzform (lokalisiert) | `Mon` bis `Sun` | `formats.D` |
| `l` | Wochentag, Langform (lokalisiert) | `Monday` bis `Sunday` | `formats.l` |
| `j` | Tag des Monats, ohne führende Null | `1` bis `31` | `formats.j` |
| `J` | Tag des Monats ohne führende Null + Ordinalzahl | `1st`, `2nd`, ..., `31st` | `formats.J` |
| `w` | Numerischer Wochentag | `0` (So) bis `6` (Sa) | `formats.w` |
| `W` | ISO-Wochennummer des Jahres | `0` bis `52` | `formats.W` |

### Monat

| Token | Beschreibung | Beispiel | Quelle |
|-------|-------------|---------|--------|
| `F` | Monatsname, Langform (lokalisiert) | `January` bis `December` | `formats.F` |
| `m` | Monatsnummer, 2-stellig mit führender Null | `01` bis `12` | `formats.m` |
| `n` | Monatsnummer, ohne führende Null | `1` bis `12` | `formats.n` |
| `M` | Monatsname, Kurzform (lokalisiert) | `Jan` bis `Dec` | `formats.M` |

### Jahr

| Token | Beschreibung | Beispiel | Quelle |
|-------|-------------|---------|--------|
| `Y` | Jahr, 4-stellig | `1999`, `2024` | `formats.Y` |
| `y` | Jahr, 2-stellig | `99`, `24` | `formats.y` |

### Zeit

| Token | Beschreibung | Beispiel | Quelle |
|-------|-------------|---------|--------|
| `H` | Stunden, 24-Stunden-Format, 2-stellig | `00` bis `23` | `formats.H` |
| `h` | Stunden, 12-Stunden-Format, ohne führende Null | `1` bis `12` | `formats.h` |
| `G` | Stunden, 12-Stunden-Format, 2-stellig mit führender Null | `01` bis `12` | `formats.G` |
| `i` | Minuten, 2-stellig mit führender Null | `00` bis `59` | `formats.i` |
| `S` | Sekunden, 2-stellig mit führender Null | `00` bis `59` | `formats.S` |
| `s` | Sekunden, ohne führende Null | `0` bis `59` | `formats.s` |
| `K` | AM/PM (lokalisiert) | `AM` oder `PM` | `formats.K` |

### Sonstige

| Token | Beschreibung | Beispiel | Quelle |
|-------|-------------|---------|--------|
| `U` | Unix-Timestamp in Sekunden (seit Epoch) | `1413704993` | `formats.U` |
| `u` | Unix-Timestamp in Millisekunden | `1413704993000` | `formats.u` |
| `Z` | ISO 8601 Datum mit UTC-Zeitzone (`.toISOString()`) | `2017-03-04T01:23:43.000Z` | `formats.Z` |

**Hinweis:** `u` (Millisekunden) ist nur in `formats` vorhanden und wird von `revFormat` korrekt geparst (`new Date(parseFloat(unixMillSeconds))`). Oft wird `U` (Sekunden) bevorzugt.

## Vollständige Token-Liste (Typ `token`)

```typescript
type token =
  | "D" | "F" | "G" | "H" | "J" | "K" | "M" | "S" | "U" | "W" | "Y" | "Z"
  | "d" | "h" | "i" | "j" | "l" | "m" | "n" | "s" | "u" | "w" | "y";
```

## Häufige Format-Kombinationen

```js
// Deutsches Format
dateFormat: "d.m.Y"            // 31.12.2024

// ISO-Format (API/Backend)
dateFormat: "Y-m-d"            // 2024-12-31

// Mit Uhrzeit (24h)
dateFormat: "Y-m-d H:i"        // 2024-12-31 14:30
dateFormat: "Y-m-d H:i:S"      // 2024-12-31 14:30:45

// 12-Stunden mit AM/PM
dateFormat: "Y-m-d h:i K"      // 2024-12-31 02:30 PM

// Menschenlesbar (Englisch)
altFormat: "F j, Y"            // December 31, 2024
altFormat: "j. F Y"            // 31. December 2024

// Unix-Timestamp (Sekunden)
dateFormat: "U"                // 1735689000

// Unix-Timestamp (Millisekunden)
dateFormat: "u"                // 1735689000000

// ISO mit Timezone (empfohlen für UTC-Übertragung)
dateFormat: "Z"                // 2024-12-31T14:30:00.000Z

// Wochennummer
dateFormat: "\\Woche W, Y"    // "Woche 52, 2024"
```

## altInput Pattern

Mit `altInput: true` werden zwei Felder verwendet:
- `dateFormat` → Wert der tatsächlich an den Server gesendet wird (z.B. `"Y-m-d"`)
- `altFormat` → Für den Nutzer sichtbares Format (z.B. `"F j, Y"`)

```js
flatpickr("#date", {
  altInput: true,
  altFormat: "F j, Y",       // "December 31, 2024" (sichtbar)
  dateFormat: "Y-m-d",       // "2024-12-31" (im versteckten Input)
});
```

## Sonderzeichen escapen

Wenn ein Token-Zeichen literell verwendet werden soll, mit `\\` escapen:

```js
dateFormat: "\\W\\e\\e\\k #W, Y"   // "Week #52, 2024" (W als Token, rest literal)
dateFormat: "Y-m-d\\TH:i:S"        // "2024-12-31T14:30:45" (T literal, kein Token)
dateFormat: "d.m.Y \\u\\h\\r H:i"  // "31.12.2024 uhr 14:30" (uhr literal)
```

## Benutzerdefiniertes Parsen/Formatieren

```js
flatpickr("#date", {
  parseDate: (datestr, format) => {
    // Eigene Parse-Logik, gibt Date zurück
    // Beispiel: deutsches Format dd.mm.yyyy
    const parts = datestr.split(".");
    return new Date(+parts[2], +parts[1] - 1, +parts[0]);
  },
  formatDate: (date, format, locale) => {
    // Eigene Format-Logik, gibt String zurück
    return date.toLocaleDateString("de-DE");
  }
});
```

## Statische Hilfsfunktionen

```js
// Formatieren ohne Instanz
flatpickr.formatDate(new Date(), "Y-m-d H:i");  // "2024-12-31 14:30"

// Parsen ohne Instanz
flatpickr.parseDate("2024-12-31", "Y-m-d");     // Date Object
```

## Token-Regex-Muster (für eigene Parser)

Einige Tokens sind locale-abhängig und werden zur Laufzeit gesetzt:

| Token | Regex-Pattern |
|-------|--------------|
| `D` | Wochentag-Kurzformen (locale) |
| `F` | Monatslangformen (locale) |
| `K` | AM/PM-Werte (locale) |
| `M` | Monats-Kurzformen (locale) |
| `l` | Wochentag-Langformen (locale) |
| `G`, `H`, `h` | `(\d\d|\d)` |
| `Y` | `(\d{4})` |
| `y` | `(\d{2})` |
| `Z`, `U`, `u` | `(.+)` |

---

Quelle: `src/utils/formatting.ts` (v4.6.13) | https://flatpickr.js.org/formatting/
