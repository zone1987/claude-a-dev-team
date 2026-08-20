# playwright-api-devices

> WARNUNG: Alle Klassen in diesem Skill sind EXPERIMENTELL. Die APIs koennen sich ohne
> Vorankuendigung aendern. Android-Support erfordert ADB (Android Debug Bridge) und
> Playwright-Treiber auf dem Geraet. Electron-Support erfordert Electron v12.2.0+,
> v13.4.0+, oder v14+.

## Android-Klassen (ADB)

- `API-DEVICES-CLASS-ANDROID.md`
  Entry Point: `playwright.android` — `devices()`, `connect()`, `launchServer()`, `setDefaultTimeout()`.
  4 Methoden, 0 Properties, 0 Events.

- `API-DEVICES-CLASS-ANDROIDDEVICE.md`
  Kern-Automatisierung: UI-Gesten (tap, swipe, fling, drag, pinch), Shell, APK-Install,
  WebView-Zugriff, Browser-Launch. 25 Methoden, 1 Property (`input`), 2 Events (`close`, `webview`).

- `API-DEVICES-CLASS-ANDROIDINPUT.md`
  Koordinatenbasierte Low-Level-Eingaben: `tap`, `drag`, `swipe`, `press`, `type`.
  5 Methoden, 0 Properties, 0 Events.

- `API-DEVICES-CLASS-ANDROIDSOCKET.md`
  Bidirektionale Prozesskommunikation via `open()`: `write`, `close`, Events `data`/`close`.
  2 Methoden, 0 Properties, 2 Events.

- `API-DEVICES-CLASS-ANDROIDWEBVIEW.md`
  Brucke zur Playwright Page API: `page()`, `pid()`, `pkg()`. 1 Event (`close`).
  3 Methoden, 0 Properties, 1 Event.

## Electron-Klassen

- `API-DEVICES-CLASS-ELECTRON.md`
  Entry Point: `playwright.electron` — einzige Methode: `launch()` mit allen Optionen.
  1 Methode, 0 Properties, 0 Events.

- `API-DEVICES-CLASS-ELECTRONAPPLICATION.md`
  Laufende Electron-App: `evaluate()` / `evaluateHandle()` im Main Process,
  `firstWindow()`, `browserWindow()`, `context()`, `process()`, `waitForEvent()`, `windows()`.
  8 Methoden, 0 Properties, 3 Events (`close`, `console`, `window`).
