---
name: sw-merchant-catalog-media
description: >
  Shopware Medien verwalten, Bild hochladen, Medienverwaltung, Media Manager, Ordner erstellen,
  Thumbnail Shopware, Alt-Text Bild, Medien löschen, URL Upload Shopware, Medien Metadaten,
  Shopware Bilder, 3D Modell Shopware, Medien Shopware 6, Bild ersetzen, ungenutzte Medien löschen,
  AI Bildgenerierung Shopware
---

# Shopware 6 – Medien

Die Medienverwaltung ist unter **Inhalte > Medien** erreichbar.
Hier werden alle Dateien zentral verwaltet, die im Shop verwendet werden.

## Datei hochladen

1. Inhalte > Medien
2. **„Datei hochladen"** (lokale Datei) oder **URL-Upload** (öffentliche URL)
3. Datei wird im aktuellen Ordner abgelegt

## Unterstützte Dateitypen

| Kategorie | Formate |
|---|---|
| Bilder | jpg, jpeg, png, webp, gif, svg, bmp, tiff, eps |
| Videos | webm, mkv, flv, ogv, mov, mp4, avi, wmv |
| Audio | aac, mp3, wav, flac |
| Dokumente | pdf, txt, doc |
| 3D-Modelle | glb |

## Medien-Aktionen

- Ersetzen (gleiche Datei neu hochladen)
- Herunterladen
- In Ordner verschieben
- Link kopieren
- Löschen

## Metadaten bearbeiten

- Dateiname, Alt-Text, Meta-Titel, Tags
- „Wird verwendet in" (Nutzungsübersicht)

## Thumbnails

Standard-Größen: 400×400, 800×800, 1920×1920 px.
Konfigurierbar: Qualität (1–100), Seitenverhältnis, Auto-Generierung.
CLI-Befehl: `media:generate-thumbnails`

## Ungenutzte Medien bereinigen

CLI-Befehl: `media:delete-unused`

Siehe `references/deep/media.md` für vollständige Konfigurationsdetails.

## Quelle
https://docs.shopware.com/de/shopware-6-de/inhalte/medien
