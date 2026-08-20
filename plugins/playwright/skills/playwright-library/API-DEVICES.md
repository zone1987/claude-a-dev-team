# playwright-api-devices

> WARNING: All classes in this skill are EXPERIMENTAL. The APIs may change without
> prior notice. Android support requires ADB (Android Debug Bridge) and
> Playwright drivers on the device. Electron support requires Electron v12.2.0+,
> v13.4.0+, or v14+.

## Android Classes (ADB)

- `API-DEVICES-CLASS-ANDROID.md`
  Entry Point: `playwright.android` — `devices()`, `connect()`, `launchServer()`, `setDefaultTimeout()`.
  4 methods, 0 properties, 0 events.

- `API-DEVICES-CLASS-ANDROIDDEVICE.md`
  Core automation: UI gestures (tap, swipe, fling, drag, pinch), shell, APK install,
  WebView access, browser launch. 25 methods, 1 property (`input`), 2 events (`close`, `webview`).

- `API-DEVICES-CLASS-ANDROIDINPUT.md`
  Coordinate-based low-level input: `tap`, `drag`, `swipe`, `press`, `type`.
  5 methods, 0 properties, 0 events.

- `API-DEVICES-CLASS-ANDROIDSOCKET.md`
  Bidirectional process communication via `open()`: `write`, `close`, events `data`/`close`.
  2 methods, 0 properties, 2 events.

- `API-DEVICES-CLASS-ANDROIDWEBVIEW.md`
  Bridge to the Playwright Page API: `page()`, `pid()`, `pkg()`. 1 event (`close`).
  3 methods, 0 properties, 1 event.

## Electron Classes

- `API-DEVICES-CLASS-ELECTRON.md`
  Entry Point: `playwright.electron` — only method: `launch()` with all options.
  1 method, 0 properties, 0 events.

- `API-DEVICES-CLASS-ELECTRONAPPLICATION.md`
  Running Electron app: `evaluate()` / `evaluateHandle()` in the main process,
  `firstWindow()`, `browserWindow()`, `context()`, `process()`, `waitForEvent()`, `windows()`.
  8 methods, 0 properties, 3 events (`close`, `console`, `window`).
