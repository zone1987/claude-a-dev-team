---
name: gotenberg-routes
description: >
  Gotenberg Routen-Uebersicht — alle Endpunkte, multipart/form-data, Response-Header,
  Gotenberg-Output-Filename, Gotenberg-Trace, Basic-Auth, gemeinsame Felder.
  Trigger: "Gotenberg Routen", "Gotenberg Endpunkte", "Gotenberg API Uebersicht",
  "Gotenberg multipart", "Gotenberg Output-Header", "Gotenberg routes overview",
  "Gotenberg-Trace", "Gotenberg-Output-Filename", "Gotenberg Auth".
---

# Gotenberg — Routen-Uebersicht

Jede Route akzeptiert einen `multipart/form-data` POST-Request und gibt eine Datei zurueck.

## Gemeinsame Request-Header

| Header | Typ | Beschreibung |
|--------|-----|-------------|
| `Gotenberg-Output-Filename` | string | Dateiname der Antwort (ohne Extension). Default: zufaellige UUID. |
| `Gotenberg-Trace` | string | Eigene Request-ID fuer Logs. Ersetzt Standard-UUID. |

## Authentifizierung

Basic Auth per CLI-Flag `--api-enable-basic-auth`. Credentials per Env-Var
`GOTENBERG_API_BASIC_AUTH_USERNAME` / `GOTENBERG_API_BASIC_AUTH_PASSWORD`.

Vollstaendige Routentabelle: `references/deep/routes.md`
