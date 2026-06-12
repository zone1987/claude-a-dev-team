---
name: panther-config-env
description: >
  Alle PANTHER_*-Umgebungsvariablen vollstaendig: Name, Typ, Default, Wirkung fuer
  Browser-Headless, Sandbox, Web-Server-Dir/Port/Router, externer Server, App-Env,
  Chrome/Firefox-Argumente und Binaries, DevTools, Fenstergroesse, Error-Screenshots,
  Readiness-Path. All PANTHER_* environment variables with type, default and effect:
  headless mode, sandbox, web server dir/port/router, external server, app env,
  Chrome/Firefox arguments and binaries, devtools, window size, error screenshots.
triggers:
  - panther umgebungsvariablen
  - panther environment variables
  - PANTHER_NO_HEADLESS
  - PANTHER_NO_SANDBOX
  - PANTHER_WEB_SERVER_DIR
  - PANTHER_WEB_SERVER_PORT
  - PANTHER_WEB_SERVER_ROUTER
  - PANTHER_EXTERNAL_BASE_URI
  - PANTHER_APP_ENV
  - PANTHER_CHROME_ARGUMENTS
  - PANTHER_CHROME_BINARY
  - PANTHER_FIREFOX_ARGUMENTS
  - PANTHER_FIREFOX_BINARY
  - PANTHER_DEVTOOLS
  - PANTHER_ERROR_SCREENSHOT_DIR
  - PANTHER_ERROR_SCREENSHOT_ATTACH
  - PANTHER_NO_REDUCED_MOTION
  - PANTHER_READINESS_PATH
  - panther konfiguration
  - panther configuration
  - panther env vars
  - panther headless
  - panther fenstergroesse
  - panther window size
  - panther hostname port
---

# panther-config-env

Vollstaendige Referenz aller PANTHER_*-Umgebungsvariablen sowie der programmatischen
Konfigurationsoptionen fuer `createPantherClient()`.

Siehe `references/deep/config-env.md` fuer die komplette Tabelle mit Typ, Default und
Quellenangabe.
