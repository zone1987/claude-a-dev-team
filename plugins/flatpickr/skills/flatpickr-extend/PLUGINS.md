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
- [PLUGINS-DETAIL.md](PLUGINS-DETAIL.md) — vollständige Plugin-Referenz mit allen Optionen, Signaturen und Codebeispielen
