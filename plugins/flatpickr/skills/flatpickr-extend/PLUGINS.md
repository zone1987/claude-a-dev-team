# flatpickr — Plugins

Plugins are activated via `plugins: [new PluginName(config)]`.

```js
flatpickr("#date", {
  enableTime: true,
  plugins: [new confirmDatePlugin({ confirmText: "OK" })]
});
```

## Official plugins

| Plugin | Function |
|--------|---------|
| `confirmDatePlugin` | Confirmation button after selection |
| `rangePlugin` | Date range with two separate inputs |
| `weekSelect` | Select a whole week |
| `monthSelectPlugin` | Select a month only (no day) |
| `minMaxTimePlugin` | Time limits per individual date |
| `scrollPlugin` | Mouse wheel navigation |
| `momentPlugin` | moment.js integration |

## Further reading
- [PLUGINS-DETAIL.md](PLUGINS-DETAIL.md) — complete plugin reference with all options, signatures and code examples
