# Shopware 6 – Media management: Complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/inhalte/medien  
> Applies from: Shopware 6.0.0+

---

## Contents

- [1. Overview](#1-overview)
- [2. Supported file types](#2-supported-file-types)
- [3. Uploading files](#3-uploading-files)
- [4. Media actions](#4-media-actions)
- [5. Editing metadata](#5-editing-metadata)
- [6. Folder management](#6-folder-management)
- [7. Thumbnail configuration](#7-thumbnail-configuration)
- [8. 3D functions](#8-3d-functions)
- [9. Adjusting presentation and sorting](#9-adjusting-presentation-and-sorting)
- [10. AI features](#10-ai-features)
- [11. Maintenance and cleanup](#11-maintenance-and-cleanup)
- [12. Recommendations for product images](#12-recommendations-for-product-images)
- [13. Recommendations for product videos](#13-recommendations-for-product-videos)

## 1. Overview

Media management is the central repository for all files in Shopware 6. From here, product images, category images, documents, videos and 3D models are managed and made available to the shop.

Path: **Inhalte** (Content) > **Medien** (Media)

---

## 2. Supported file types

| Category | Formats |
|---|---|
| **Images** | jpg, jpeg, png, webp, gif, svg, bmp, tiff, eps |
| **Videos** | webm, mkv, flv, ogv, ogg, mov, mp4, avi, wmv |
| **Audio** | aac, mp3, wav, flac |
| **Documents** | pdf, txt, doc |
| **3D models** | glb |

---

## 3. Uploading files

### 3.1 Upload methods

| Method | Description |
|---|---|
| **File upload** | Upload a local file from the computer (click the upload button or drag & drop) |
| **URL upload** | Import a publicly reachable file via URL |

### 3.2 Upload process

1. Inhalte > Medien
2. Select the desired folder (or the root directory)
3. **"Datei hochladen"** (Upload file) or enter a URL
4. For duplicates: Shopware asks whether the existing file should be replaced

### 3.3 Duplicate handling

If a file with an identical name already exists, Shopware offers to:
- **ersetzen** (replace) the file (the file is overwritten, the URL stays the same)
- **umbenennen** (rename) the file (the new file is stored under a changed name)

---

## 4. Media actions

### 4.1 Single file

The following are available via the context menu or the file detail view:

| Action | Description |
|---|---|
| **Ersetzen** (Replace) | Replace the existing file with a new version; the URL is retained |
| **Herunterladen** (Download) | Download the file to the local computer |
| **Verschieben** (Move) | Move it to another folder |
| **Link kopieren** (Copy link) | Copy the file's direct URL to the clipboard |
| **Löschen** (Delete) | Remove the file from the system |

> **Note**: Deleting a file that is still used in products, categories etc. can lead to missing images in the shop!

---

## 5. Editing metadata

Every file has editable metadata:

| Field | Description |
|---|---|
| **Dateiname** (File name) | Name without file extension; determines the file's URL |
| **Alt-Text** (Alt text) | Accessibility and SEO; appears when the image cannot be loaded |
| **Meta-Titel** (Meta title) | Title for SEO purposes |
| **Tags** | Keywords for better findability in media management |
| **Wird verwendet in** (Used in) | Shows all entities (products, categories etc.) that use this file |

### Editing metadata

1. Click the file in media management
2. The right sidebar opens the detail view
3. Edit the fields
4. Save (automatically or via button)

---

## 6. Folder management

### 6.1 Creating a folder

- Button **"Ordner hinzufügen"** (Add folder) or via the context menu
- Nesting of any depth is possible
- Folder names should be chosen meaningfully (e.g. "Produkte", "Banner", "Hersteller")

### 6.2 Folder actions

| Action | Description |
|---|---|
| **Verschieben** (Move) | Move the folder into another folder |
| **Umbenennen** (Rename) | Change the folder label |
| **Auflösen** (Dissolve) | Move the folder's content into the parent folder, then delete the folder |
| **Löschen** (Delete) | Delete the folder and its content |

### 6.3 Default folder structure

Shopware automatically creates default folders for various entities, e.g.:
- `Produkte` – product images
- `Kategorien` – category images  
- `Hersteller` – manufacturer logos
- `Medienverwaltung` – general files

---

## 7. Thumbnail configuration

Thumbnails are automatically generated versions of images in defined sizes.

### 7.1 Default thumbnail sizes

| Size | Usage |
|---|---|
| 400×400 px | Product listing (preview images) |
| 800×800 px | Product detail page (medium quality) |
| 1920×1920 px | Zoom view / high resolution |

### 7.2 Thumbnail settings (configurable per folder)

| Setting | Description |
|---|---|
| **Größen** (Sizes) | Which thumbnail sizes should be generated |
| **Qualität** (Quality) | Compression level (1–100); 80 is a good default value |
| **Seitenverhältnis** (Aspect ratio) | Cropping behaviour (proportional / fill / stretch) |
| **Automatische Generierung** (Automatic generation) | Thumbnails are created automatically on upload |

### 7.3 Generating thumbnails manually (CLI)

```bash
bin/console media:generate-thumbnails
```

Useful after changes to the thumbnail configuration or when thumbnails are missing.

---

## 8. 3D functions

### 8.1 Model Viewer

- Allows GLB files to be viewed directly in the administration
- The 3D model can be rotated, zoomed and explored
- Preview before embedding it in products

### 8.2 Model Editor

- Editing of position, rotation and scaling of the 3D model
- Visual real-time preview of the changes
- Settings are saved automatically

### 8.3 AR (Augmented Reality)

Prerequisites:
- iOS 12+ (Apple ARKit)
- Android 8.0+ with ARCore 1.9
- GLB format of the 3D file
- AR activation in the product settings

---

## 9. Adjusting presentation and sorting

### 9.1 View options

- **Rasteransicht** (Grid view): tiles with preview images
- **Listenansicht** (List view): tabular presentation
- Switchable via dropdown

### 9.2 Sorting options

- Name (A–Z / Z–A)
- Upload date (newest/oldest first)
- File size
- File type

---

## 10. AI features

### 10.1 AI image generation (from Shopware Rise)

- **"AI Copilot Bildgenerierung"** (AI Copilot image generation) directly in media management
- Generate images from a natural-language description
- Generated images are stored directly in media management
- Suitable for mood images, banners, placeholder images

**Usage:**
1. Inhalte > Medien
2. Button **"KI-Bild generieren"** (Generate AI image) (or similar)
3. Enter a description in natural language
4. Have the image generated
5. Save it in the desired folder

---

## 11. Maintenance and cleanup

### 11.1 Identifying unused media

The **"Wird verwendet in"** field shows for each file where it is used.
If the field is empty: the file is not used anywhere.

### 11.2 Deleting unused media (CLI)

```bash
bin/console media:delete-unused
```

Deletes all media files that are no longer referenced in any Shopware entity.

> **Caution**: Before running it, check whether external systems (import tools, exports) reference files that Shopware does not know as "used"!

---

## 12. Recommendations for product images

| Property | Recommendation |
|---|---|
| Format | JPG (photos) or PNG (with transparency) or WebP |
| Aspect ratio | **Square** (1:1) for a consistent presentation |
| Minimum size | 600×600 px |
| Optimal size | 1920×1920 px (covers all thumbnail sizes) |
| File name | Descriptive and SEO-friendly (e.g. `blaues-t-shirt-vorne.jpg`) |
| Alt text | Always fill in for accessibility and SEO |

---

## 13. Recommendations for product videos

| Property | Recommendation |
|---|---|
| Format | **MP4** (best browser compatibility) |
| Codecs | H.264 video, AAC audio |
| Alternative | WebM as fallback |
| Resolution | At least 720p (1280×720) |
| File size | Under 100 MB (performance) |

---

*Source: https://docs.shopware.com/de/shopware-6-de/inhalte/medien*
