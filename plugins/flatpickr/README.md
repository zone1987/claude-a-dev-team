# flatpickr

> Vollständige Dokumentation des leichtgewichtigen JS-Datetime-Pickers flatpickr (v4.6.x).

`flatpickr` ist die vollständige Wissens-Bibliothek zum gleichnamigen **leichtgewichtigen, abhängigkeitsfreien JavaScript-Datetime-Picker** (v4.6.x). Sie ist aus der offiziellen Doku (flatpickr.js.org) **und dem npm-Quellcode** destilliert — letzterer ist maßgeblich, da die Website einige Optionen/Plugins nicht listet.

Abgedeckt: **Einbindung** (npm/CDN inkl. CSS, Init), die **komplette Optionen-Referenz** (62 Optionen mit Typ/Default — inkl. quell-exklusiver wie `animate`, `closeOnSelect`, `autoFillDefaultTime`), alle **Formatierungs-Tokens** (23, inkl. `u`), **Events/Hooks** (12: onChange/onOpen/onClose/onReady/onValueUpdate/onMonth-/YearChange/onDayCreate/onKeyDown/onDestroy/onPreCalendarPosition/onParseConfig), die **Instanz-API** (Methoden/Properties/DOM-Elemente), die **Lokalisierung** (alle 67 Locales + CustomLocale-Struktur), **Themes**, **alle 8 offiziellen Plugins** (range, confirmDate, weekSelect, monthSelect, minMaxTime, **label**, scroll, moment), **Beispiele**, **Mobile-Support** und die **Migration** (v2 / IE9).

Spezialist: **`flatpickr-expert`**; Scaffolder **`/flatpickr-init`** (npm/CDN + CSS + Init + Hooks + optional Plugin, Vanilla/React/Vue). **Wann nutzen:** für jede Datums-/Zeit-Auswahl im Frontend — auch in Shopware-Storefront-/Admin- oder Contao-Projekten. Hinweis: flatpickrs „Hooks" sind seine Event-Callbacks (siehe `flatpickr-events`), nicht zu verwechseln mit Claude-Code-Hooks.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen aus flatpickr.js.org + npm-Quellcode destilliert und eingebettet; Skills laden Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install flatpickr@claude-a-dev-team
```

## Skills (11)

| Skill | Beschreibung |
|---|---|
| `flatpickr-getting-started` | flatpickr installieren und initialisieren: npm, CDN, CSS, Basis-Init, Selektoren, jQuery |
| `flatpickr-events` | Alle flatpickr Hooks und Events: onChange, onOpen, onClose, onReady, onValueUpdate, onMonthChange, onYearChange, onDayCreate, onKeyDown, onParseConfig — Signaturen und Beispiele |
| `flatpickr-examples` | flatpickr Beispiele und Patterns: DateTime, Range, Multiple, Time-only, Inline, Disable, altInput, Preloading, Wrap/Input-Groups, Custom Parsing/Formatting |
| `flatpickr-formatting` | Alle flatpickr Datum/Zeit-Formatierungstokens: Zeichen, Beschreibung, Beispielwerte |
| `flatpickr-instance` | flatpickr Instanz-API: alle Methoden, Properties und DOM-Elemente |
| `flatpickr-localization` | flatpickr Lokalisierung: Locale setzen, importieren, eigene Locale, firstDayOfWeek |
| `flatpickr-migration` | flatpickr Migration von v2 auf v3+: Breaking Changes, IE9-Polyfill, utc-Option entfernt |
| `flatpickr-mobile` | flatpickr Mobile-Support: natives Datetime-Input, automatische Erkennung, disableMobile |
| `flatpickr-options` | Vollständige Referenz aller flatpickr-Konfigurationsoptionen: Typ, Default, Beschreibung |
| `flatpickr-plugins` | Alle offiziellen flatpickr Plugins: rangePlugin, confirmDatePlugin, weekSelect, monthSelectPlugin, minMaxTimePlugin, scrollPlugin, labelPlugin, momentPlugin |
| `flatpickr-themes` | Alle flatpickr Themes: dark, airbnb, confetti, material_blue, material_green, material_orange, material_red, light — einbinden und wechseln |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `flatpickr-expert` | Spezialist für flatpickr (leichtgewichtiger, abhängigkeitsfreier JS-Datetime-Picker, v4.6.x) |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/flatpickr-init` | Scaffold einer flatpickr-Einbindung — npm/CDN-Setup inkl. CSS, Init-Code mit gewünschten Optionen (Range/Zeit/inline/Locale), Events/Hooks und optional einem offiziellen Plugin |
