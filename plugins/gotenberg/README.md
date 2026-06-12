# gotenberg

Vollumfängliche Bibliothek für **[Gotenberg](https://gotenberg.dev)** — die Docker-basierte, **stateless** Developer-API zur **PDF-Erzeugung und -Manipulation**. Gotenberg bündelt **Chromium** (HTML/Markdown/URL → PDF + Screenshots), **LibreOffice** (Office-Dokumente → PDF) und **PDF-Engines** (pdfcpu/QPDF/PDFtk: merge/split/convert/flatten/encrypt/metadata/bookmarks/embed/Factur-X/rotate/stamp/watermark) hinter einer einheitlichen HTTP-Schnittstelle: jede Route ist ein `POST` mit `multipart/form-data`, Eingaben als `files`, Optionen als gleichnamige Form-Felder, Antwort ist die fertige Datei.

Dieses Plugin dokumentiert **jede Route, jedes Form-Feld, jeden CLI-Flag/jede Env-Var und jeden Header** — destilliert aus der offiziellen Doku (gotenberg.dev) und in die Skills eingebettet (keine externen Laufzeit-Abhängigkeiten). Schlanke `SKILL.md`, Tiefe in `references/deep/`. Es deckt außerdem Betrieb (Health/Metrics/Debug/Telemetry/Logging), Sicherheit (Outbound-URL-Filtering gegen SSRF, Basic-Auth), asynchrone Verarbeitung (Webhook) und die Client-Bibliotheken (PHP `gotenberg-php`, Go, JS, Python) ab.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install gotenberg@claude-a-dev-team
```

## Nutzung

- **Skills** laden automatisch bei passendem Kontext (z.B. „HTML to PDF", „PDF mergen", „docx→pdf/a", „ZUGFeRD/Factur-X").
- **Agent `gotenberg-expert`** für Konvertierung/Manipulation, **`gotenberg-ops`** für Bereitstellung & Betrieb.
- **Commands** `/gotenberg-convert` (Request-Scaffold) und `/gotenberg-deploy` (Deployment-Scaffold).
- **Hook** erinnert beim Bearbeiten von Gotenberg-Aufrufen an Routen-/Feld-Prüfung, Output-Filename/Async und Credential-Hygiene.

## Skills

| Skill | Beschreibung |
|---|---|
| `gotenberg-introduction` | Überblick — was ist Gotenberg, welche Fähigkeiten, wann einsetzen. |
| `gotenberg-installation` | Installieren — Docker, Docker Compose, Kubernetes, Cloud Run, AWS Lambda. |
| `gotenberg-routes` | Routen-Übersicht — alle Endpunkte, multipart/form-data, Response-Header, `Gotenberg-Output-Filename`, `Gotenberg-Trace`, Basic-Auth, gemeinsame Felder. |
| `gotenberg-clients` | Client-Bibliotheken — PHP-SDK (`gotenberg-php`), Community-Clients, eigene HTTP-Integration. |
| `gotenberg-configuration` | Konfiguration — alle CLI-Flags und Env-Vars für API, Chromium, LibreOffice, PDF-Engines, Webhook, Logging. |
| `gotenberg-chromium-html` | HTML → PDF — alle Form-Felder, Header/Footer, Assets, Warte-Mechanismen, PDF/A, Metadaten, Seitengröße. |
| `gotenberg-chromium-url` | URL → PDF — alle Form-Felder, Cookies, Headers, Warte-Mechanismen, JS-SPAs. |
| `gotenberg-chromium-markdown` | Markdown → PDF — `index.html`-Template, `.md`-Dateien, MathJax, Assets. |
| `gotenberg-chromium-screenshots` | Screenshots — HTML, URL und Markdown als PNG/JPEG/WebP erfassen. |
| `gotenberg-libreoffice` | LibreOffice — Office-Dokumente (100+ Formate) zu PDF konvertieren. |
| `gotenberg-pdf-merge` | PDFs zusammenführen (`POST /forms/pdfengines/merge`). |
| `gotenberg-pdf-split` | PDFs aufteilen — `splitMode` pages/intervals (`POST /forms/pdfengines/split`). |
| `gotenberg-pdf-convert` | PDFs nach PDF/A bzw. PDF/UA konvertieren (`POST /forms/pdfengines/convert`). |
| `gotenberg-pdf-flatten` | PDF-Formularfelder flatten (`POST /forms/pdfengines/flatten`). |
| `gotenberg-pdf-encrypt` | PDFs mit Passwort & Berechtigungen verschlüsseln (`POST /forms/pdfengines/encrypt`). |
| `gotenberg-pdf-metadata` | PDF-Metadaten (XMP/Exif) lesen und schreiben. |
| `gotenberg-pdf-bookmarks` | PDF-Lesezeichen / Document-Outline lesen und schreiben. |
| `gotenberg-pdf-attachments` | Datei-Anhänge in PDFs einbetten (`POST /forms/pdfengines/embed`). |
| `gotenberg-pdf-facturx` | Factur-X / ZUGFeRD-E-Rechnungen erzeugen (`POST /forms/pdfengines/factur-x`). |
| `gotenberg-pdf-rotate` | PDF-Seiten rotieren (`POST /forms/pdfengines/rotate`). |
| `gotenberg-pdf-stamp` | PDFs mit Text-/Bild-/PDF-Overlays stempeln (`POST /forms/pdfengines/stamp`). |
| `gotenberg-pdf-watermark` | Text-/Bild-/PDF-Wasserzeichen hinter den Inhalt legen (`POST /forms/pdfengines/watermark`). |
| `gotenberg-webhook` | Asynchrone Webhook-Callbacks und Remote-Datei-Download. |
| `gotenberg-outbound-filtering` | Outbound-URL-Filtering / SSRF-Schutz konfigurieren. |
| `gotenberg-system` | System-Endpunkte: Health-Check, Version, Prometheus-Metrics, Debug. |
| `gotenberg-telemetry` | OpenTelemetry-Tracing, -Metrics und -Logging konfigurieren. |
| `gotenberg-troubleshooting` | Fehlersuche: leere PDFs, Font-Probleme, Timeouts, LibreOffice-Fehler. |

## Agents

| Agent | Beschreibung |
|---|---|
| `gotenberg-expert` | Spezialist für Konvertierung & PDF-Manipulation: Routen, alle Form-Felder, Chromium/LibreOffice/PDF-Engines, Webhook, Clients. |
| `gotenberg-ops` | Betriebs-/DevOps-Spezialist: Installation, Konfiguration (alle Flags/Env-Vars), Health/Metrics/Debug, Telemetry, SSRF-Schutz, Skalierung, Troubleshooting. |

## Commands

| Command | Beschreibung |
|---|---|
| `/gotenberg-convert` | Scaffold eines Gotenberg-Requests — wählt Route (Chromium/LibreOffice/PDF-Engines), baut den `multipart/form-data`-curl-Aufruf mit den gewünschten Form-Feldern, optional als `gotenberg-php`-Snippet oder async via Webhook. |
| `/gotenberg-deploy` | Scaffold eines Deployments — `docker run` / docker-compose / Kubernetes / Cloud Run mit Health-Check, Ports, Ressourcen und den passenden CLI-Flags/Env-Vars. |

## Hooks

| Hook | Beschreibung |
|---|---|
| `gotenberg-reminder.py` (PostToolUse) | Feuert beim Bearbeiten von Dateien mit Gotenberg-Aufrufen: erinnert an Routen-/Feldnamen-Prüfung, `Gotenberg-Output-Filename`/Async und warnt vor Klartext-Credentials. |

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team. Quelle: offizielle Gotenberg-Dokumentation (https://gotenberg.dev).
