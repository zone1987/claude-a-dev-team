# flatpickr

> Complete documentation of the lightweight JS datetime picker flatpickr (v4.6.x).

`flatpickr` is the complete knowledge library for the **lightweight, dependency-free JavaScript datetime picker** of the same name (v4.6.x). It is distilled from the official documentation (flatpickr.js.org) **and from the npm source code** — the latter is authoritative, because the website does not list some options and plugins.

Covered: **integration** (npm/CDN including CSS, init), the **complete options reference** (62 options with type/default — including source-exclusive ones such as `animate`, `closeOnSelect`, `autoFillDefaultTime`), all **format tokens** (23, including `u`), **events/hooks** (12: onChange/onOpen/onClose/onReady/onValueUpdate/onMonth-/YearChange/onDayCreate/onKeyDown/onDestroy/onPreCalendarPosition/onParseConfig), the **instance API** (methods/properties/DOM elements), **localization** (all 67 locales + CustomLocale structure), **themes**, **all 8 official plugins** (range, confirmDate, weekSelect, monthSelect, minMaxTime, **label**, scroll, moment), **examples**, **mobile support** and the **migration** (v2 / IE9).

Specialist: **`flatpickr-expert`**; scaffolder **`/flatpickr-init`** (npm/CDN + CSS + init + hooks + optional plugin, Vanilla/React/Vue). **When to use:** for any date/time selection in the frontend — including Shopware storefront/admin or Contao projects. Note: flatpickr's "hooks" are its event callbacks (see `flatpickr-api`), not to be confused with Claude Code hooks.

Part of the marketplace **[claude-a-dev-team](../../README.md)**. Knowledge distilled from flatpickr.js.org + the npm source code and embedded; each skill keeps a lean `SKILL.md` and loads its depth from flat SCREAMING-CASE.md reference files next to it.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install flatpickr@claude-a-dev-team
```

## Skills (2)

| Skill | Description |
|---|---|
| `flatpickr-api` | flatpickr API: installation, all options, instance methods, events and hooks, date format tokens, examples. |
| `flatpickr-extend` | flatpickr extensions: the official plugins (range, confirmDate, weekSelect, monthSelect), 67 locales, themes, mobile. |

## Agents (1)

| Agent | Description |
|---|---|
| `flatpickr-expert` | Specialist for flatpickr (lightweight, dependency-free JS datetime picker, v4.6.x). |

## Commands (1)

| Command | Description |
|---|---|
| `/flatpickr-init` | Scaffolds a flatpickr integration — npm/CDN setup including CSS, init code with the desired options (range/time/inline/locale), events/hooks and optionally one official plugin. |
