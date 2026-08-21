# flatpickr — Localization (complete reference, v4.6.13)

Source: `src/types/locale.ts` + `src/l10n/*.ts` (67 locale files, as of v4.6.13).

## Contents

- [Setting the locale per instance](#setting-the-locale-per-instance)
- [Global localization](#global-localization)
- [Overriding individual locale values](#overriding-individual-locale-values)
- [Complete locale type definition](#complete-locale-type-definition)
- [CustomLocale type (for partial locale overrides)](#customlocale-type-for-partial-locale-overrides)
- [Custom locale — complete example](#custom-locale--complete-example)
- [All available locales (67 files)](#all-available-locales-67-files)

## Setting the locale per instance

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

### Browser / CDN (script tags)

```html
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://npmcdn.com/flatpickr/dist/l10n/de.js"></script>
```

```js
flatpickr("#date", { locale: "de" });
// or: flatpickr.l10ns.de is directly available once the script has loaded
```

## Global localization

Localize all flatpickr instances at once:

### ES Modules

```js
import { German } from "flatpickr/dist/l10n/de.js";
flatpickr.localize(German);

flatpickr("#date"); // uses German automatically
flatpickr("#date2", { locale: "ru" }); // overrides it for this instance only
```

### Browser

```js
flatpickr.localize(flatpickr.l10ns.de);
flatpickr("#date"); // German
```

## Overriding individual locale values

```js
// set the first weekday globally to Monday
flatpickr.l10ns.default.firstDayOfWeek = 1;

// per instance without a full locale
flatpickr("#date", {
  locale: {
    firstDayOfWeek: 1  // 0 = Sunday, 1 = Monday, 6 = Saturday
  }
});
```

## Complete locale type definition

From `src/types/locale.ts`:

```typescript
type Locale = {
  weekdays: {
    shorthand: [string, string, string, string, string, string, string]; // 7 weekdays
    longhand:  [string, string, string, string, string, string, string];
  };
  months: {
    shorthand: [string, string, string, string, string, string, string, string, string, string, string, string]; // 12 months
    longhand:  [string, string, string, string, string, string, string, string, string, string, string, string];
  };
  daysInMonth: [number, number, number, number, number, number, number, number, number, number, number, number];
  firstDayOfWeek: number;       // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
  ordinal: (nth: number) => string;
  rangeSeparator: string;       // default: " to "
  weekAbbreviation: string;     // default: "Wk"
  scrollTitle: string;          // tooltip for the scroll action
  toggleTitle: string;          // tooltip for the AM/PM toggle
  amPM: [string, string];       // default: ["AM", "PM"]
  yearAriaLabel: string;
  monthAriaLabel: string;
  hourAriaLabel: string;
  minuteAriaLabel: string;
  time_24hr: boolean;
};
```

## CustomLocale type (for partial locale overrides)

```typescript
type CustomLocale = {
  weekdays: {
    shorthand: [string, string, string, string, string, string, string]; // required
    longhand:  [string, string, string, string, string, string, string]; // required
  };
  months: {
    shorthand: [string, string, string, string, string, string, string, string, string, string, string, string]; // required
    longhand:  [string, string, string, string, string, string, string, string, string, string, string, string]; // required
  };
  // all of the following fields are optional:
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

## Custom locale — complete example

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

## All available locales (67 files)

Locale files live under `flatpickr/dist/l10n/<code>.js`.
Locale keys according to `src/types/locale.ts` (`type key`):

| Code | Language | File |
|------|---------|-------|
| `ar` | Arabic | `ar.js` |
| `ar-dz` | Arabic (Algeria) | `ar-dz.js` |
| `at` | Austrian German | `at.js` |
| `az` | Azerbaijani | `az.js` |
| `be` | Belarusian | `be.js` |
| `bg` | Bulgarian | `bg.js` |
| `bn` | Bangla / Bengali | `bn.js` |
| `bs` | Bosnian | `bs.js` |
| `ca` / `cat` | Catalan | `cat.js` |
| `ckb` | Kurdish (Sorani) | `ckb.js` |
| `cs` | Czech | `cs.js` |
| `cy` | Welsh | `cy.js` |
| `da` | Danish | `da.js` |
| `de` | German | `de.js` |
| `default` / `en` | English (default) | `default.js` |
| `eo` | Esperanto | `eo.js` |
| `es` | Spanish | `es.js` |
| `et` | Estonian | `et.js` |
| `fa` | Persian / Farsi | `fa.js` |
| `fi` | Finnish | `fi.js` |
| `fo` | Faroese | `fo.js` |
| `fr` | French | `fr.js` |
| `ga` | Irish / Gaelic | `ga.js` |
| `gr` | Greek | `gr.js` |
| `he` | Hebrew | `he.js` |
| `hi` | Hindi | `hi.js` |
| `hr` | Croatian | `hr.js` |
| `hu` | Hungarian | `hu.js` |
| `hy` | Armenian | `hy.js` |
| `id` | Indonesian | `id.js` |
| `is` | Icelandic | `is.js` |
| `it` | Italian | `it.js` |
| `ja` | Japanese | `ja.js` |
| `ka` | Georgian | `ka.js` |
| `km` | Khmer | `km.js` |
| `ko` | Korean | `ko.js` |
| `kz` | Kazakh | `kz.js` |
| `lt` | Lithuanian | `lt.js` |
| `lv` | Latvian | `lv.js` |
| `mk` | Macedonian | `mk.js` |
| `mn` | Mongolian | `mn.js` |
| `ms` | Malay | `ms.js` |
| `my` | Burmese | `my.js` |
| `nl` | Dutch | `nl.js` |
| `nn` | Norwegian Nynorsk | `nn.js` |
| `no` | Norwegian Bokmål | `no.js` |
| `pa` | Punjabi | `pa.js` |
| `pl` | Polish | `pl.js` |
| `pt` | Portuguese | `pt.js` |
| `ro` | Romanian | `ro.js` |
| `ru` | Russian | `ru.js` |
| `si` | Sinhala | `si.js` |
| `sk` | Slovak | `sk.js` |
| `sl` | Slovenian | `sl.js` |
| `sq` | Albanian | `sq.js` |
| `sr` | Serbian (Latin) | `sr.js` |
| `sr-cyr` | Serbian (Cyrillic) | `sr-cyr.js` |
| `sv` | Swedish | `sv.js` |
| `th` | Thai | `th.js` |
| `tr` | Turkish | `tr.js` |
| `uk` | Ukrainian | `uk.js` |
| `uz` | Uzbek (Cyrillic) | `uz.js` |
| `uz_latn` | Uzbek (Latin) | `uz_latn.js` |
| `vn` | Vietnamese | `vn.js` |
| `zh` | Chinese (Simplified) | `zh.js` |
| `zh_tw` | Chinese (Traditional) | `zh_tw.js` |

**Note:** The locale key `"ca"` is an alias for `"cat"` (Catalan).
The key `"en"` is an alias for `"default"` (English).
The file `ar-dz.js` must be referenced with the string key `"ar-dz"` (no dot access).

---

Source: `src/types/locale.ts` + `src/l10n/index.ts` (v4.6.13) | https://flatpickr.js.org/localization/
