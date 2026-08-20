# Gotenberg — PDF Metadata (Reading & Writing)

Reads XMP/Exif metadata via ExifTool (JSON response) and writes new XMP tags.
Reference: `METADATA-DETAIL.md`

Routes:
- `POST /forms/pdfengines/metadata/read` → JSON response
- `POST /forms/pdfengines/metadata/write` → PDF/ZIP
