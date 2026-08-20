# gotenberg

Comprehensive library for **[Gotenberg](https://gotenberg.dev)** — the Docker-based, **stateless** developer API for **PDF generation and manipulation**. Gotenberg bundles **Chromium** (HTML/Markdown/URL → PDF plus screenshots), **LibreOffice** (Office documents → PDF) and **PDF engines** (pdfcpu/QPDF/PDFtk: merge/split/convert/flatten/encrypt/metadata/bookmarks/embed/Factur-X/rotate/stamp/watermark) behind a single HTTP interface: every route is a `POST` with `multipart/form-data`, inputs go in as `files`, options as identically named form fields, and the response is the finished file.

This plugin documents **every route, every form field, every CLI flag and env var and every header** — distilled from the official documentation (gotenberg.dev) and embedded in the skills (no external runtime dependencies). Each skill keeps a lean `SKILL.md` and loads its depth from flat SCREAMING-CASE.md reference files next to it. It also covers operations (health/metrics/debug/telemetry/logging), security (outbound URL filtering against SSRF, basic auth), asynchronous processing (webhook) and the client libraries (PHP `gotenberg-php`, Go, JS, Python).

Part of the marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install gotenberg@claude-a-dev-team
```

## Usage

- **Skills** load automatically in matching context (for example "HTML to PDF", "merge PDF", "docx→pdf/a", "ZUGFeRD/Factur-X").
- **Agent `gotenberg-expert`** for conversion/manipulation, **`gotenberg-ops`** for provisioning and operations.
- **Commands** `/gotenberg-convert` (request scaffold) and `/gotenberg-deploy` (deployment scaffold).
- **Hook** reminds you, when editing Gotenberg calls, to verify routes and fields, to consider output filename/async and to keep credentials clean.

## Skills (3)

| Skill | Description |
|---|---|
| `gotenberg-convert` | Conversion with Gotenberg: an overview of what Gotenberg is, which capabilities it has and when to use it; the route overview — all endpoints, `multipart/form-data`, response headers, `Gotenberg-Output-Filename`, `Gotenberg-Trace`, basic auth, shared fields; HTML → PDF with all form fields, header/footer, assets, wait mechanisms, PDF/A, metadata, page size; URL → PDF with all form fields, cookies, headers, wait mechanisms, JS SPAs; Markdown → PDF with the `index.html` template, `.md` files, MathJax, assets; screenshots — capturing HTML, URL and Markdown as PNG/JPEG/WebP; and LibreOffice — converting Office documents (100+ formats) to PDF. |
| `gotenberg-pdf` | PDF manipulation with Gotenberg: merging PDFs (`POST /forms/pdfengines/merge`), splitting PDFs with `splitMode` pages/intervals (`POST /forms/pdfengines/split`), converting PDFs to PDF/A or PDF/UA (`POST /forms/pdfengines/convert`), flattening PDF form fields (`POST /forms/pdfengines/flatten`), encrypting PDFs with a password and permissions (`POST /forms/pdfengines/encrypt`), reading and writing PDF metadata (XMP/Exif), reading and writing PDF bookmarks / the document outline, embedding file attachments in PDFs (`POST /forms/pdfengines/embed`), generating Factur-X / ZUGFeRD e-invoices (`POST /forms/pdfengines/factur-x`), rotating PDF pages (`POST /forms/pdfengines/rotate`), stamping PDFs with text/image/PDF overlays (`POST /forms/pdfengines/stamp`) and placing text/image/PDF watermarks behind the content (`POST /forms/pdfengines/watermark`). |
| `gotenberg-operations` | Running Gotenberg: installation — Docker, Docker Compose, Kubernetes, Cloud Run, AWS Lambda; configuration — all CLI flags and env vars for API, Chromium, LibreOffice, PDF engines, webhook, logging; client libraries — the PHP SDK (`gotenberg-php`), community clients, a custom HTTP integration; asynchronous webhook callbacks and remote file download; configuring outbound URL filtering / SSRF protection; the system endpoints — health check, version, Prometheus metrics, debug; configuring OpenTelemetry tracing, metrics and logging; and troubleshooting — empty PDFs, font problems, timeouts, LibreOffice errors. |

## Agents

| Agent | Description |
|---|---|
| `gotenberg-expert` | Specialist for conversion and PDF manipulation: routes, all form fields, Chromium/LibreOffice/PDF engines, webhook, clients. |
| `gotenberg-ops` | Operations/DevOps specialist: installation, configuration (all flags/env vars), health/metrics/debug, telemetry, SSRF protection, scaling, troubleshooting. |

## Commands

| Command | Description |
|---|---|
| `/gotenberg-convert` | Scaffolds a Gotenberg request — picks the route (Chromium/LibreOffice/PDF engines) and builds the `multipart/form-data` curl call with the desired form fields, optionally as a `gotenberg-php` snippet or async via webhook. |
| `/gotenberg-deploy` | Scaffolds a deployment — `docker run` / docker-compose / Kubernetes / Cloud Run with health check, ports, resources and the matching CLI flags/env vars. |

## Hooks

| Hook | Description |
|---|---|
| `gotenberg-reminder.py` (PostToolUse) | Fires when editing files that contain Gotenberg calls: reminds you to verify route and field names, to consider `Gotenberg-Output-Filename`/async and warns about plaintext credentials. |

## License & author

proprietary — Andreas Gerhardt, A-Dev-Team. Source: the official Gotenberg documentation (https://gotenberg.dev).
