---
name: gotenberg-convert
description: Scaffold eines Gotenberg-Requests — wählt Route (Chromium HTML/URL/Markdown, LibreOffice, PDF-Engines merge/split/convert/…), baut den multipart/form-data-curl-Aufruf mit den gewünschten Form-Feldern, optional als gotenberg-php-Snippet oder async via Webhook.
argument-hint: <was> z.B. "html→pdf A4 quer mit Header" | "merge a.pdf b.pdf" | "docx→pdf/a-2b" [--client curl|php] [--async]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /gotenberg-convert

Erzeuge einen einsatzfertigen Gotenberg-Aufruf. Skills: `gotenberg-routes` + die passende(n) Themen-Skills
(`gotenberg-chromium-*`, `gotenberg-libreoffice`, `gotenberg-pdf-*`), Client-Beispiele aus `gotenberg-clients`,
Async aus `gotenberg-webhook`.

## Ablauf
1. **Ziel + Route** aus `$ARGUMENTS` bestimmen:
   - HTML/Markdown/URL → PDF → `/forms/chromium/convert/{html|markdown|url}`
   - Screenshot → `/forms/chromium/screenshot/{html|markdown|url}`
   - Office → PDF → `/forms/libreoffice/convert`
   - merge/split/convert/flatten/encrypt/metadata/bookmarks/embed/factur-x/rotate/stamp/watermark → `/forms/pdfengines/<op>`
2. **Eingabedateien** als `-F "files=@..."` (Reihenfolge bei merge beachten; HTML braucht `index.html` + Assets).
3. **Form-Felder** ergänzen — NUR dokumentierte Felder mit korrektem Namen/Typ (Quelle: jeweiliges Skill), z.B.
   `paperWidth/paperHeight`, `marginTop…`, `landscape`, `nativePageRanges`, `printBackground`, `waitDelay`,
   `pdfa`, `pdfua`, `metadata`, Header/Footer-Dateien.
4. **Output/Tracing**: `-H "Gotenberg-Output-Filename: …"`, optional `-H "Gotenberg-Trace: …"`.
5. **Variante**: `--client php` → `gotenberg-php`-Snippet; `--async` → Webhook-Header
   (`Gotenberg-Webhook-Url`, `-Webhook-Error-Url`, ggf. `-Webhook-Method`/`-Webhook-Extra-Http-Headers`).

Routen/Feldnamen/Defaults nie raten — gegen die `gotenberg-*`-Skills prüfen. Keine echten Credentials/Tokens in Beispiele.
Auf Wechselwirkungen hinweisen (z.B. PDF/A ↔ Verschlüsselung).
