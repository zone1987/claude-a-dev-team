# flatpickr — Complete formatting reference (v4.6.13)

Tokens are used in `dateFormat`, `altFormat`, `ariaDateFormat`.
Source: `src/utils/formatting.ts` (authoritative, as of v4.6.13).

## Contents

- [All tokens](#all-tokens)
- [Complete token list (type `token`)](#complete-token-list-type-token)
- [Common format combinations](#common-format-combinations)
- [altInput pattern](#altinput-pattern)
- [Escaping special characters](#escaping-special-characters)
- [Custom parsing/formatting](#custom-parsingformatting)
- [Static helpers](#static-helpers)
- [Token regex patterns (for your own parsers)](#token-regex-patterns-for-your-own-parsers)

## All tokens

### Day

| Token | Description | Example | Source |
|-------|-------------|---------|--------|
| `d` | Day of the month, 2-digit with leading zero | `01` to `31` | `formats.d` |
| `D` | Weekday, short form (localized) | `Mon` to `Sun` | `formats.D` |
| `l` | Weekday, long form (localized) | `Monday` to `Sunday` | `formats.l` |
| `j` | Day of the month, without leading zero | `1` to `31` | `formats.j` |
| `J` | Day of the month without leading zero + ordinal suffix | `1st`, `2nd`, ..., `31st` | `formats.J` |
| `w` | Numeric weekday | `0` (Sun) to `6` (Sat) | `formats.w` |
| `W` | ISO week number of the year | `0` to `52` | `formats.W` |

### Month

| Token | Description | Example | Source |
|-------|-------------|---------|--------|
| `F` | Month name, long form (localized) | `January` to `December` | `formats.F` |
| `m` | Month number, 2-digit with leading zero | `01` to `12` | `formats.m` |
| `n` | Month number, without leading zero | `1` to `12` | `formats.n` |
| `M` | Month name, short form (localized) | `Jan` to `Dec` | `formats.M` |

### Year

| Token | Description | Example | Source |
|-------|-------------|---------|--------|
| `Y` | Year, 4-digit | `1999`, `2024` | `formats.Y` |
| `y` | Year, 2-digit | `99`, `24` | `formats.y` |

### Time

| Token | Description | Example | Source |
|-------|-------------|---------|--------|
| `H` | Hours, 24-hour format, 2-digit | `00` to `23` | `formats.H` |
| `h` | Hours, 12-hour format, without leading zero | `1` to `12` | `formats.h` |
| `G` | Hours, 12-hour format, 2-digit with leading zero | `01` to `12` | `formats.G` |
| `i` | Minutes, 2-digit with leading zero | `00` to `59` | `formats.i` |
| `S` | Seconds, 2-digit with leading zero | `00` to `59` | `formats.S` |
| `s` | Seconds, without leading zero | `0` to `59` | `formats.s` |
| `K` | AM/PM (localized) | `AM` or `PM` | `formats.K` |

### Miscellaneous

| Token | Description | Example | Source |
|-------|-------------|---------|--------|
| `U` | Unix timestamp in seconds (since epoch) | `1413704993` | `formats.U` |
| `u` | Unix timestamp in milliseconds | `1413704993000` | `formats.u` |
| `Z` | ISO 8601 date with UTC timezone (`.toISOString()`) | `2017-03-04T01:23:43.000Z` | `formats.Z` |

**Note:** `u` (milliseconds) only exists in `formats` and is parsed correctly by `revFormat` (`new Date(parseFloat(unixMillSeconds))`). `U` (seconds) is often preferred.

## Complete token list (type `token`)

```typescript
type token =
  | "D" | "F" | "G" | "H" | "J" | "K" | "M" | "S" | "U" | "W" | "Y" | "Z"
  | "d" | "h" | "i" | "j" | "l" | "m" | "n" | "s" | "u" | "w" | "y";
```

## Common format combinations

```js
// German format
dateFormat: "d.m.Y"            // 31.12.2024

// ISO format (API/backend)
dateFormat: "Y-m-d"            // 2024-12-31

// With time (24h)
dateFormat: "Y-m-d H:i"        // 2024-12-31 14:30
dateFormat: "Y-m-d H:i:S"      // 2024-12-31 14:30:45

// 12-hour with AM/PM
dateFormat: "Y-m-d h:i K"      // 2024-12-31 02:30 PM

// Human-readable (English)
altFormat: "F j, Y"            // December 31, 2024
altFormat: "j. F Y"            // 31. December 2024

// Unix timestamp (seconds)
dateFormat: "U"                // 1735689000

// Unix timestamp (milliseconds)
dateFormat: "u"                // 1735689000000

// ISO with timezone (recommended for UTC transfer)
dateFormat: "Z"                // 2024-12-31T14:30:00.000Z

// Week number
dateFormat: "\\Woche W, Y"    // "Woche 52, 2024"
```

## altInput pattern

With `altInput: true` two fields are used:
- `dateFormat` → the value actually sent to the server (e.g. `"Y-m-d"`)
- `altFormat` → the format visible to the user (e.g. `"F j, Y"`)

```js
flatpickr("#date", {
  altInput: true,
  altFormat: "F j, Y",       // "December 31, 2024" (visible)
  dateFormat: "Y-m-d",       // "2024-12-31" (in the hidden input)
});
```

## Escaping special characters

To use a token character literally, escape it with `\\`:

```js
dateFormat: "\\W\\e\\e\\k #W, Y"   // "Week #52, 2024" (W as token, rest literal)
dateFormat: "Y-m-d\\TH:i:S"        // "2024-12-31T14:30:45" (T literal, not a token)
dateFormat: "d.m.Y \\u\\h\\r H:i"  // "31.12.2024 uhr 14:30" (uhr literal)
```

## Custom parsing/formatting

```js
flatpickr("#date", {
  parseDate: (datestr, format) => {
    // Custom parse logic, returns a Date
    // Example: German format dd.mm.yyyy
    const parts = datestr.split(".");
    return new Date(+parts[2], +parts[1] - 1, +parts[0]);
  },
  formatDate: (date, format, locale) => {
    // Custom format logic, returns a string
    return date.toLocaleDateString("de-DE");
  }
});
```

## Static helpers

```js
// Format without an instance
flatpickr.formatDate(new Date(), "Y-m-d H:i");  // "2024-12-31 14:30"

// Parse without an instance
flatpickr.parseDate("2024-12-31", "Y-m-d");     // Date Object
```

## Token regex patterns (for your own parsers)

Some tokens are locale-dependent and are set at runtime:

| Token | Regex pattern |
|-------|--------------|
| `D` | Weekday short forms (locale) |
| `F` | Month long forms (locale) |
| `K` | AM/PM values (locale) |
| `M` | Month short forms (locale) |
| `l` | Weekday long forms (locale) |
| `G`, `H`, `h` | `(\d\d|\d)` |
| `Y` | `(\d{4})` |
| `y` | `(\d{2})` |
| `Z`, `U`, `u` | `(.+)` |

---

Source: `src/utils/formatting.ts` (v4.6.13) | https://flatpickr.js.org/formatting/
