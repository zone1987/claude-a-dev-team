# flatpickr — Lokalisierung (vollständige Referenz, v4.6.13)

Quelle: `src/types/locale.ts` + `src/l10n/*.ts` (67 Locale-Dateien, Stand v4.6.13).

## Locale per Instanz setzen

### ES Modules / TypeScript

```js
import flatpickr from "flatpickr";
import { German } from "flatpickr/dist/l10n/de.js";
import { Russian } from "flatpickr/dist/l10n/ru.js";

flatpickr("#date", { locale: German });
flatpickr("#dateRu", { locale: Russian });
```

### CommonJS

```js
const flatpickr = require("flatpickr");
const German = require("flatpickr/dist/l10n/de.js").default.de;

flatpickr("#date", { locale: German });
```

### Browser / CDN (Script-Tags)

```html
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://npmcdn.com/flatpickr/dist/l10n/de.js"></script>
```

```js
flatpickr("#date", { locale: "de" });
// oder: flatpickr.l10ns.de nach Script-Load direkt verfügbar
```

## Globale Lokalisierung

Alle flatpickr-Instanzen auf einmal lokalisieren:

### ES Modules

```js
import { German } from "flatpickr/dist/l10n/de.js";
flatpickr.localize(German);

flatpickr("#date"); // Verwendet automatisch Deutsch
flatpickr("#date2", { locale: "ru" }); // Überschreibt nur für diese Instanz
```

### Browser

```js
flatpickr.localize(flatpickr.l10ns.de);
flatpickr("#date"); // Deutsch
```

## Einzelne Locale-Werte überschreiben

```js
// Ersten Wochentag global auf Montag setzen
flatpickr.l10ns.default.firstDayOfWeek = 1;

// Per Instanz ohne vollständige Locale
flatpickr("#date", {
  locale: {
    firstDayOfWeek: 1  // 0 = Sonntag, 1 = Montag, 6 = Samstag
  }
});
```

## Vollständige Locale-Typ-Definition

Aus `src/types/locale.ts`:

```typescript
type Locale = {
  weekdays: {
    shorthand: [string, string, string, string, string, string, string]; // 7 Wochentage
    longhand:  [string, string, string, string, string, string, string];
  };
  months: {
    shorthand: [string, string, string, string, string, string, string, string, string, string, string, string]; // 12 Monate
    longhand:  [string, string, string, string, string, string, string, string, string, string, string, string];
  };
  daysInMonth: [number, number, number, number, number, number, number, number, number, number, number, number];
  firstDayOfWeek: number;       // 0 = Sonntag, 1 = Montag, ..., 6 = Samstag
  ordinal: (nth: number) => string;
  rangeSeparator: string;       // Standard: " to "
  weekAbbreviation: string;     // Standard: "Wk"
  scrollTitle: string;          // Tooltip für Scroll-Aktion
  toggleTitle: string;          // Tooltip für AM/PM-Toggle
  amPM: [string, string];       // Standard: ["AM", "PM"]
  yearAriaLabel: string;
  monthAriaLabel: string;
  hourAriaLabel: string;
  minuteAriaLabel: string;
  time_24hr: boolean;
};
```

## CustomLocale-Typ (für partielle Locale-Überschreibung)

```typescript
type CustomLocale = {
  weekdays: {
    shorthand: [string, string, string, string, string, string, string]; // Pflichtfeld
    longhand:  [string, string, string, string, string, string, string]; // Pflichtfeld
  };
  months: {
    shorthand: [string, string, string, string, string, string, string, string, string, string, string, string]; // Pflichtfeld
    longhand:  [string, string, string, string, string, string, string, string, string, string, string, string]; // Pflichtfeld
  };
  // Alle folgenden Felder sind optional:
  daysInMonth?: [number, number, number, number, number, number, number, number, number, number, number, number];
  firstDayOfWeek?: number;
  ordinal?: (nth: number) => string;
  rangeSeparator?: string;
  weekAbbreviation?: string;
  scrollTitle?: string;
  toggleTitle?: string;
  amPM?: [string, string];
  yearAriaLabel?: string;
  monthAriaLabel?: string;
  hourAriaLabel?: string;
  minuteAriaLabel?: string;
  time_24hr?: boolean;
};
```

## Benutzerdefinierte Locale (Custom Locale) — vollständiges Beispiel

```js
flatpickr("#date", {
  locale: {
    weekdays: {
      shorthand: ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"],
      longhand: ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
    },
    months: {
      shorthand: ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
      longhand: ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    },
    daysInMonth: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    firstDayOfWeek: 1,
    ordinal: (nth) => ".",
    rangeSeparator: " bis ",
    weekAbbreviation: "KW",
    scrollTitle: "Zum Ändern scrollen",
    toggleTitle: "Klicken zum Umschalten",
    amPM: ["AM", "PM"],
    yearAriaLabel: "Jahr",
    monthAriaLabel: "Monat",
    hourAriaLabel: "Stunde",
    minuteAriaLabel: "Minute",
    time_24hr: true,
  }
});
```

## Alle verfügbaren Locales (67 Dateien)

Locale-Dateien liegen unter `flatpickr/dist/l10n/<code>.js`.
Locale-Keys laut `src/types/locale.ts` (`type key`):

| Code | Sprache | Datei |
|------|---------|-------|
| `ar` | Arabisch | `ar.js` |
| `ar-dz` | Arabisch (Algerien) | `ar-dz.js` |
| `at` | Österreichisches Deutsch | `at.js` |
| `az` | Aserbaidschanisch | `az.js` |
| `be` | Belarussisch | `be.js` |
| `bg` | Bulgarisch | `bg.js` |
| `bn` | Bangla / Bengali | `bn.js` |
| `bs` | Bosnisch | `bs.js` |
| `ca` / `cat` | Katalanisch | `cat.js` |
| `ckb` | Kurdisch (Sorani) | `ckb.js` |
| `cs` | Tschechisch | `cs.js` |
| `cy` | Walisisch | `cy.js` |
| `da` | Dänisch | `da.js` |
| `de` | Deutsch | `de.js` |
| `default` / `en` | Englisch (Standard) | `default.js` |
| `eo` | Esperanto | `eo.js` |
| `es` | Spanisch | `es.js` |
| `et` | Estnisch | `et.js` |
| `fa` | Persisch / Farsi | `fa.js` |
| `fi` | Finnisch | `fi.js` |
| `fo` | Färöisch | `fo.js` |
| `fr` | Französisch | `fr.js` |
| `ga` | Irisch / Gälisch | `ga.js` |
| `gr` | Griechisch | `gr.js` |
| `he` | Hebräisch | `he.js` |
| `hi` | Hindi | `hi.js` |
| `hr` | Kroatisch | `hr.js` |
| `hu` | Ungarisch | `hu.js` |
| `hy` | Armenisch | `hy.js` |
| `id` | Indonesisch | `id.js` |
| `is` | Isländisch | `is.js` |
| `it` | Italienisch | `it.js` |
| `ja` | Japanisch | `ja.js` |
| `ka` | Georgisch | `ka.js` |
| `km` | Khmer | `km.js` |
| `ko` | Koreanisch | `ko.js` |
| `kz` | Kasachisch | `kz.js` |
| `lt` | Litauisch | `lt.js` |
| `lv` | Lettisch | `lv.js` |
| `mk` | Mazedonisch | `mk.js` |
| `mn` | Mongolisch | `mn.js` |
| `ms` | Malaiisch | `ms.js` |
| `my` | Burmesisch | `my.js` |
| `nl` | Niederländisch | `nl.js` |
| `nn` | Norwegisch Nynorsk | `nn.js` |
| `no` | Norwegisch Bokmål | `no.js` |
| `pa` | Punjabi | `pa.js` |
| `pl` | Polnisch | `pl.js` |
| `pt` | Portugiesisch | `pt.js` |
| `ro` | Rumänisch | `ro.js` |
| `ru` | Russisch | `ru.js` |
| `si` | Singhalesisch | `si.js` |
| `sk` | Slowakisch | `sk.js` |
| `sl` | Slowenisch | `sl.js` |
| `sq` | Albanisch | `sq.js` |
| `sr` | Serbisch (Lateinisch) | `sr.js` |
| `sr-cyr` | Serbisch (Kyrillisch) | `sr-cyr.js` |
| `sv` | Schwedisch | `sv.js` |
| `th` | Thailändisch | `th.js` |
| `tr` | Türkisch | `tr.js` |
| `uk` | Ukrainisch | `uk.js` |
| `uz` | Usbekisch (Kyrillisch) | `uz.js` |
| `uz_latn` | Usbekisch (Lateinisch) | `uz_latn.js` |
| `vn` | Vietnamesisch | `vn.js` |
| `zh` | Chinesisch (Vereinfacht) | `zh.js` |
| `zh_tw` | Chinesisch (Traditionell) | `zh_tw.js` |

**Hinweis:** Der Locale-Key `"ca"` ist ein Alias für `"cat"` (Katalanisch).
Der Key `"en"` ist ein Alias für `"default"` (Englisch).
Die Datei `ar-dz.js` muss mit dem String-Key `"ar-dz"` referenziert werden (kein Punkt-Zugriff).

---

Quelle: `src/types/locale.ts` + `src/l10n/index.ts` (v4.6.13) | https://flatpickr.js.org/localization/
