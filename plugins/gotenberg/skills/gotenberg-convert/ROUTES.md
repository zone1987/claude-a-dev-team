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

Vollstaendige Routentabelle: `ROUTES-DETAIL.md`
