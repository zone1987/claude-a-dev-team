---
name: gotenberg-deploy
description: Scaffold eines Gotenberg-Deployments — docker run / docker-compose / Kubernetes / Cloud Run mit Health-Check, Ports, Ressourcen und den passenden CLI-Flags/Env-Vars (api-*, chromium-*, libreoffice-*, webhook-*, log-*, Outbound-Filtering).
argument-hint: <ziel> docker|compose|k8s|cloudrun [--auth basic] [--webhook] [--prometheus]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /gotenberg-deploy

Erzeuge eine einsatzfertige Gotenberg-Betriebskonfiguration. Skills: `gotenberg-installation`, `gotenberg-configuration`,
`gotenberg-system` (Health/Metrics), `gotenberg-outbound-filtering`, ggf. `gotenberg-webhook`, `gotenberg-telemetry`.

## Ablauf
1. **Zielplattform** aus `$ARGUMENTS` (docker run, docker-compose, K8s-Manifest, Cloud Run).
2. **Basis** erzeugen: offizielles Image `gotenberg/gotenberg:<tag>`, Port `3000`, Health-Check gegen `/health`
   (`gotenberg-system`), sinnvolle Ressourcen-Limits (Chromium/LibreOffice sind speicherhungrig).
3. **Flags/Env-Vars** NUR dokumentierte ergänzen (Quelle: `gotenberg-configuration`), z.B. `--api-timeout`,
   `--api-port`, `--chromium-disable-javascript`, `--libreoffice-restart-after`, `--log-level`, `--api-enable-basic-auth`
   (mit `GOTENBERG_API_BASIC_AUTH_USERNAME/PASSWORD` als **Platzhalter**, niemals echte Werte).
4. **Optionen**: `--auth basic` → Basic-Auth; `--webhook` → Hinweise/Whitelist (`gotenberg-webhook`); `--prometheus` →
   Metrics-Endpoint aktiv lassen (`gotenberg-system`). SSRF-Schutz via Outbound-Filtering empfehlen.
5. Kurzer Betriebs-Hinweis: Stateless → horizontal skalierbar; keine Persistenz nötig.

Flags/Defaults nie raten — gegen `gotenberg-configuration`/`-installation` prüfen. Keine echten Credentials ins Manifest.
