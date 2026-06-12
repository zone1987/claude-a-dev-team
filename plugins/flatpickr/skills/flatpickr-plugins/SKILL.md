---
name: flatpickr-plugins
description: >
  Alle offiziellen flatpickr Plugins: rangePlugin, confirmDatePlugin, weekSelect,
  monthSelectPlugin, minMaxTimePlugin, scrollPlugin, labelPlugin, momentPlugin.
  Trigger: "flatpickr plugins", "flatpickr plugin", "flatpickr range picker", "flatpickr rangePlugin",
  "flatpickr confirmDate", "flatpickr weekSelect", "flatpickr monthSelect",
  "flatpickr minMaxTime", "flatpickr scroll", "flatpickr datumsbereich".
---

# flatpickr — Plugins

Plugins werden via `plugins: [new PluginName(config)]` aktiviert.

```js
flatpickr("#date", {
  enableTime: true,
  plugins: [new confirmDatePlugin({ confirmText: "OK" })]
});
```

## Offizielle Plugins

| Plugin | Funktion |
|--------|---------|
| `confirmDatePlugin` | Bestätigungs-Button nach Auswahl |
| `rangePlugin` | Datumsbereich mit zwei separaten Inputs |
| `weekSelect` | Ganze Woche auswählen |
| `monthSelectPlugin` | Nur Monat auswählen (kein Tag) |
| `minMaxTimePlugin` | Zeitgrenzen je einzelnem Datum |
| `scrollPlugin` | Mausrad-Navigation |
| `momentPlugin` | moment.js Integration |

## Vertiefung
- [references/deep/plugins.md](references/deep/plugins.md) — vollständige Plugin-Referenz mit allen Optionen, Signaturen und Codebeispielen
