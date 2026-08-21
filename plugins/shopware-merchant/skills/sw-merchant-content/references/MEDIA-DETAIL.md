# Shopware 6 – Medien (Media): full documentation

**Source:** https://docs.shopware.com/de/shopware-6-de/Inhalte/medien  
**Version:** from 6.7.0.0

---

## Contents

- [Screenshots](#screenshots)
- [Overview](#overview)
- [Supported file types](#supported-file-types)
- [Uploading files](#uploading-files)
- [Media configuration (single file)](#media-configuration-single-file)
- [Folder management](#folder-management)
- [Deleting unused media](#deleting-unused-media)
- [AI Copilot: image generation](#ai-copilot-image-generation)
- [3D models (GLB format)](#3d-models-glb-format)
- [Best practices](#best-practices)
- [CLI commands (console)](#cli-commands-console)

## Screenshots

| File | Content |
|---|---|
| `../../assets/medien-uebersicht.png` | Medien overview |
| `../../assets/medien-ersetzen.png` | Actions toolbar (replace, download, etc.) |
| `../../assets/medien-metadaten.png` | Metadata editing area |
| `../../assets/medien-verwendung.png` | "Wird verwendet in" (Used in) area |
| `../../assets/ordner.png` | Folder structure view |
| `../../assets/folder-actions.png` | Folder context menu |
| `../../assets/ordner-einstellungen.png` | Folder settings dialogue |
| `../../assets/thumbnails.png` | Thumbnail configuration |
| `../../assets/bild-generierung.jpg` | AI image generation interface |
| `../../assets/bild-generiert.jpg` | Generated image result |
| `../../assets/model-viewer.png` | 3D model viewer in the sidebar |
| `../../assets/model-editor.png` | 3D model editor, full screen |

---

## Overview

Path: **Inhalte** (Content) **> Medien**

Media management is the central library for all files in the shop.
All areas (Erlebniswelten (Shopping Experiences), Produkte (Products), Kategorien (Categories), Themes) access
this library.

### Interface elements of the overview

| Element | Function |
|---|---|
| Search field (top) | Search media by name |
| "Dateien hochladen" (Upload files) | Open the upload dialogue |
| URL upload | Upload a file via URL |
| Display options | List or tile view |
| Sorting options | Sort by name, date, type |
| "Bildgenerierung" (Image generation) | AI image generation (commercial) |
| "Neuen Ordner hinzufügen" (Add new folder) | Create a new folder |

---

## Supported file types

### Images
jpg, jpeg, png, webp, gif, svg, bmp, tiff, eps

### Video
webm, mkv, flv, ogv, ogg, mov, mp4, avi, wmv

### Documents
pdf, txt, doc

### Audio
aac, mp3, wav, flac, oga, wma

### 3D models
glb (GL Binary – for the model viewer and 3D blocks in Erlebniswelten)

---

## Uploading files

### Method 1: direct upload
1. Click "Dateien hochladen"
2. Select files from the file system
3. Several files at once are possible

### Method 2: URL upload
1. Click the URL upload icon
2. Enter the direct URL to the file
3. Shopware downloads the file automatically and stores it

### Duplicate handling

If a file with the same name already exists, a pop-up appears:

| Option | Behaviour |
|---|---|
| Hochladen und ersetzen (Upload and replace) | The existing file is overwritten |
| Hochladen und umbenennen (Upload and rename) | The new file automatically gets a changed name |
| Vorhandene Datei verwenden (Use existing file) | Cancel the upload, use the existing file |
| Datei überspringen (Skip file) | Skip the upload for this file |

---

## Media configuration (single file)

Clicking a medium opens the detail panel on the right.

### Preview
- Image preview or file icon
- For 3D models: interactive model viewer

### Metadata (editable)

| Field | Beschreibung (Description) |
|---|---|
| Name | Display name of the file (not the file name) |
| Alt-Text (Alt text) | Accessibility text for images (important for SEO) |
| Meta-Titel (Meta title) | Title for search engines |

### Tags
- Keywords for better findability
- Several tags possible

### Actions (toolbar)

| Action | Beschreibung |
|---|---|
| Ersetzen (Replace) | Swap the file for a new version (the URL stays the same) |
| Download | Download the file |
| Verschieben (Move) | Move to another folder |
| Link kopieren (Copy link) | Direct URL of the file to the clipboard |
| Löschen (Delete) | Remove the file permanently |

### "Wird verwendet in" (Used in)
- Shows every place where the medium is used
- With direct links to the respective page/product/category
- Important: check before deleting!

---

## Folder management

### Creating a folder
"Neuen Ordner hinzufügen" → enter a name → confirm

### Folder navigation
- Clicking a folder opens its content
- Navigate back via the arrow icon or the breadcrumb

### Folder actions (context menu)

| Action | Beschreibung |
|---|---|
| Verschieben (Move) | Move the folder into the parent folder |
| Einstellungen (Settings) | Open the folder configuration |
| Auflösen (Dissolve) | Remove the folder; move the content into the parent folder |
| Löschen (Delete) | Delete the folder and all of its content permanently |

**Caution**: "Löschen" removes all files it contains irretrievably.

### Folder settings

**"Allgemein" (General) tab:**
- Change the name
- Define the default storage location for certain media types
  (e.g. "all product images automatically end up in this folder")

**"Thumbnails" tab:**

| Setting | Beschreibung |
|---|---|
| Einstellungen vom übergeordneten Ordner übernehmen (Adopt settings from the parent folder) | Inherit thumbnails from the parent folder |
| Thumbnails generieren (Generate thumbnails) | Enable thumbnail generation for this folder |
| Seitenverhältnis beibehalten (Keep aspect ratio) | Keep the proportions when scaling |
| Thumbnail-Qualität (Thumbnail quality) | Value 1–100 (compression quality) |
| Thumbnail-Größen (Thumbnail sizes) | List of generated sizes |

**Default thumbnail sizes:** 400×400, 800×800, 1920×1920

### Regenerating thumbnails

Via the console (SSH/CLI):
```bash
bin/console media:generate-thumbnails
```

---

## Deleting unused media

### Via the console (recommended for large amounts)

```bash
bin/console media:delete-unused
```

Optional parameters:
```bash
# Preview only (dry run)
bin/console media:delete-unused --dry-run

# Check a specific folder
bin/console media:delete-unused --folder-id=<ID>
```

**Note**: create a backup before running it. The action cannot be reversed.

---

## AI Copilot: image generation

**Availability:** Shopware Rise plan or higher + Shopware Commercial extension installed

### Usage

1. Inhalte > Medien > "Bildgenerierung" button
2. Enter a description of the desired image (prompt)
3. Click "Bild generieren" (Generate image)
4. Check the generated image:
   - "Speichern" (Save) → the image is stored in the "AI-generated" folder
   - "Neu generieren" (Regenerate) → create a new image with the same prompt

### Technical details

- **AI model:** Google Nano Banana 2
- **Images per request:** 1 image
- **Daily limit:** limited number of requests per day
- **Post-processing:** not possible; if unsatisfied: regenerate
- **Storage location:** automatically in the "AI-generated" folder

### Supported aspect ratios

1:1 | 2:3 | 3:2 | 3:4 | 4:3 | 9:16 | 16:9 | 21:9

### Supported resolutions

- 1K (default)
- 2K

**Default values:** 16:9 aspect ratio, 1K resolution

### Prompt tips for better results

- **Be concrete**: "product lifestyle image of a sneaker on a wooden floor, natural light, horizontal"
- **Quality hints**: use adjectives such as "high-quality", "professional", "clean"
- **State the orientation**: name landscape/portrait explicitly
- **Dimensions optional**: the aspect ratio can be named in the prompt

### Automatic detection from the prompt

The system analyses the prompt and automatically detects:
- Format (landscape/portrait/square)
- Aspect ratio
- Desired resolution

---

## 3D models (GLB format)

### Prerequisites
- File in .glb format (GL Binary)
- For 3D blocks in Erlebniswelten: Shopware Rise plan

### Model viewer (preview)

Automatically active when a GLB file is selected:

| Control | Action |
|---|---|
| Left mouse button + drag | Rotate the model |
| Right mouse button + drag | Move the camera (pan) |
| Scroll wheel | Zoom in/out |
| Expand button | Open the model editor as a modal |

### Model editor (editing)

Opens via the expand button of the model viewer.

#### Tools

**Move tool (Verschieben-Werkzeug):**
- Blue arrow: Z axis (depth)
- Green arrow: Y axis (height)
- Red arrow: X axis (width)
- Coloured squares: combined planes (XY, XZ, YZ)

**Rotate tool (Drehen-Werkzeug):**
- Red ring: tilt forwards/backwards (pitch)
- Blue ring: tilt left/right (yaw)
- Green ring: rotation around its own axis (roll)
- Yellow outer ring: change the camera perspective

**Scale tool:**
- Default: proportional scaling (all axes at once)
- Optional: scale individual axes
  - Green: height (Y)
  - Red: width (X)
  - Blue: depth (Z)

#### Persistence
All changes in the model editor are saved to the database automatically.
No manual saving required.

---

## Best practices

### File organisation
- Set up the folder structure from the start (e.g. by category or campaign)
- Configure default storage locations for common media types
- Tidy up unused media regularly (`media:delete-unused`)

### Image optimisation
- Prefer the webp format (better compression than JPG/PNG)
- Enable thumbnails for product images
- Always maintain alt texts (SEO and accessibility)

### Performance
- Compress images before uploading
- Mind the maximum file size (depending on the server configuration)
- Use thumbnails instead of delivering the original size

---

## CLI commands (console)

```bash
# Delete unused media
bin/console media:delete-unused

# Regenerate thumbnails
bin/console media:generate-thumbnails

# Thumbnails for a specific folder
bin/console media:generate-thumbnails --folder-id=<ID>
```

Further CLI documentation: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shopware-cli#media
