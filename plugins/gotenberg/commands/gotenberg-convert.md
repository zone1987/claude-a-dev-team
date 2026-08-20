---
name: gotenberg-convert
description: Scaffold a Gotenberg request — picks the route (Chromium HTML/URL/Markdown, LibreOffice, PDF engines merge/split/convert/…), builds the multipart/form-data curl call with the desired form fields, optionally as a gotenberg-php snippet or async via webhook.
argument-hint: <what> e.g. "html→pdf A4 landscape with header" | "merge a.pdf b.pdf" | "docx→pdf/a-2b" [--client curl|php] [--async]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /gotenberg-convert

Produce a ready-to-run Gotenberg call. Skills: `gotenberg-convert` plus the matching topic skill(s)
(`gotenberg-chromium-*`, `gotenberg-convert`, `gotenberg-pdf-*`), client examples from `gotenberg-operations`,
async from `gotenberg-operations`.

## Procedure
1. **Determine target + route** from `$ARGUMENTS`:
   - HTML/Markdown/URL → PDF → `/forms/chromium/convert/{html|markdown|url}`
   - Screenshot → `/forms/chromium/screenshot/{html|markdown|url}`
   - Office → PDF → `/forms/libreoffice/convert`
   - merge/split/convert/flatten/encrypt/metadata/bookmarks/embed/factur-x/rotate/stamp/watermark → `/forms/pdfengines/<op>`
2. **Input files** as `-F "files=@..."` (mind the order for merge; HTML needs `index.html` + assets).
3. **Add form fields** — ONLY documented fields with the correct name/type (source: the respective skill), e.g.
   `paperWidth/paperHeight`, `marginTop…`, `landscape`, `nativePageRanges`, `printBackground`, `waitDelay`,
   `pdfa`, `pdfua`, `metadata`, header/footer files.
4. **Output/tracing**: `-H "Gotenberg-Output-Filename: …"`, optionally `-H "Gotenberg-Trace: …"`.
5. **Variant**: `--client php` → `gotenberg-php` snippet; `--async` → webhook headers
   (`Gotenberg-Webhook-Url`, `-Webhook-Error-Url`, and if needed `-Webhook-Method`/`-Webhook-Extra-Http-Headers`).

Never guess routes/field names/defaults — check them against the `gotenberg-*` skills. No real credentials/tokens in examples.
Point out interactions (e.g. PDF/A ↔ encryption).
