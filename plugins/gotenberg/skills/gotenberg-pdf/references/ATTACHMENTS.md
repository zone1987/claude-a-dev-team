# Gotenberg — PDF attachments

Embeds external files (XML, images etc.) as attachments in the PDF container.
Includes per-attachment metadata (mimeType, AFRelationship).
Reference: `ATTACHMENTS-DETAIL.md`

Route: `POST /forms/pdfengines/embed`
Returns: PDF (200) | ZIP (multiple inputs) | 400 | 503
