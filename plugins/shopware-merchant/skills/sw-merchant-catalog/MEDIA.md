# Shopware 6 – Medien (Media)

Media management is reachable under **Inhalte** (Content) > **Medien** (Media).
All files used in the shop are managed centrally here.

## Uploading a file

1. Inhalte > Medien
2. **"Datei hochladen"** (Upload file) (local file) or **URL upload** (public URL)
3. The file is placed in the current folder

## Supported file types

| Category | Formats |
|---|---|
| Images | jpg, jpeg, png, webp, gif, svg, bmp, tiff, eps |
| Videos | webm, mkv, flv, ogv, mov, mp4, avi, wmv |
| Audio | aac, mp3, wav, flac |
| Documents | pdf, txt, doc |
| 3D models | glb |

## Media actions

- Ersetzen (Replace) (upload the same file again)
- Herunterladen (Download)
- In Ordner verschieben (Move to folder)
- Link kopieren (Copy link)
- Löschen (Delete)

## Editing metadata

- File name, alt text, meta title, tags
- "Wird verwendet in" (Used in) (usage overview)

## Thumbnails

Default sizes: 400×400, 800×800, 1920×1920 px.
Configurable: quality (1–100), aspect ratio, auto-generation.
CLI command: `media:generate-thumbnails`

## Cleaning up unused media

CLI command: `media:delete-unused`

See `MEDIA-DETAIL.md` for full configuration details.

## Source
https://docs.shopware.com/de/shopware-6-de/inhalte/medien
