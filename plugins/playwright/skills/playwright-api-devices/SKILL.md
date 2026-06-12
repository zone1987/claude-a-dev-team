---
name: playwright-api-devices
description: >
  EXPERIMENTELLE Playwright-APIs fuer Geraete- und Desktop-Automatisierung:
  Android (ADB) und Electron. Vollstaendige API-Referenz fuer alle Klassen
  mit allen Methoden, Properties, Events und Parametern.
  Android, AndroidDevice, AndroidInput, AndroidSocket, AndroidWebView,
  Electron, ElectronApplication, experimental device testing,
  Playwright Android ADB automation, Electron desktop app testing.
triggers:
  - Playwright Android
  - playwright android testing
  - AndroidDevice
  - AndroidInput
  - AndroidSocket
  - AndroidWebView
  - android.devices
  - android.connect
  - android.launchServer
  - androidDevice.launchBrowser
  - androidDevice.webView
  - androidDevice.shell
  - androidDevice.tap
  - androidDevice.swipe
  - androidDevice.fill
  - androidDevice.installApk
  - AndroidSelector
  - AndroidKey
  - Playwright Electron
  - Electron testing
  - ElectronApplication
  - electron.launch
  - electronApplication.evaluate
  - electronApplication.firstWindow
  - electronApplication.browserWindow
  - electronApplication.waitForEvent
  - electronApplication.context
  - Electron desktop test
  - Playwright experimentell
  - experimental playwright
---

> WARNUNG: Alle Klassen in diesem Skill sind EXPERIMENTELL. Die APIs koennen sich ohne
> Vorankuendigung aendern. Android-Support erfordert ADB (Android Debug Bridge) und
> Playwright-Treiber auf dem Geraet. Electron-Support erfordert Electron v12.2.0+,
> v13.4.0+, oder v14+.

## Android-Klassen (ADB)

- `references/deep/class-android.md`
  Entry Point: `playwright.android` — `devices()`, `connect()`, `launchServer()`, `setDefaultTimeout()`.
  4 Methoden, 0 Properties, 0 Events.

- `references/deep/class-androiddevice.md`
  Kern-Automatisierung: UI-Gesten (tap, swipe, fling, drag, pinch), Shell, APK-Install,
  WebView-Zugriff, Browser-Launch. 25 Methoden, 1 Property (`input`), 2 Events (`close`, `webview`).

- `references/deep/class-androidinput.md`
  Koordinatenbasierte Low-Level-Eingaben: `tap`, `drag`, `swipe`, `press`, `type`.
  5 Methoden, 0 Properties, 0 Events.

- `references/deep/class-androidsocket.md`
  Bidirektionale Prozesskommunikation via `open()`: `write`, `close`, Events `data`/`close`.
  2 Methoden, 0 Properties, 2 Events.

- `references/deep/class-androidwebview.md`
  Brucke zur Playwright Page API: `page()`, `pid()`, `pkg()`. 1 Event (`close`).
  3 Methoden, 0 Properties, 1 Event.

## Electron-Klassen

- `references/deep/class-electron.md`
  Entry Point: `playwright.electron` — einzige Methode: `launch()` mit allen Optionen.
  1 Methode, 0 Properties, 0 Events.

- `references/deep/class-electronapplication.md`
  Laufende Electron-App: `evaluate()` / `evaluateHandle()` im Main Process,
  `firstWindow()`, `browserWindow()`, `context()`, `process()`, `waitForEvent()`, `windows()`.
  8 Methoden, 0 Properties, 3 Events (`close`, `console`, `window`).
