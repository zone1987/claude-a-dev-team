# Contao 5.x — Dateiverwaltung (File Management)

Sources:
- https://docs.contao.org/5.x/manual/en/file-manager/
- https://docs.contao.org/5.x/manual/en/file-manager/file-manager/
- https://docs.contao.org/5.x/manual/en/file-manager/meta-data/
- https://docs.contao.org/5.x/manual/en/file-manager/control-downloads/

---

## Contents

- [Overview](#overview)
- [1. Managing files and folders](#1-managing-files-and-folders)
- [2. Metadata](#2-metadata)
- [3. Controlling downloads](#3-controlling-downloads)
- [Practical tips](#practical-tips)

## Overview

With the Dateiverwaltung (File Management, also "file manager") you can manage files and folders on the server. All user files are stored in the `files/` directory by default.

Contao stores all file information in the database and assigns every entry a unique **UUID** (universally unique identifier). This ID is unique system-wide and allows files to be referenced in content elements even after being renamed or moved.

The Dateiverwaltung presents the directory structure as a **hierarchical tree**. Folders can be expanded and collapsed via the plus/minus icon.

---

## 1. Managing files and folders

### Navigation icons

| Icon | Function | Description |
|------|----------|-------------|
| Pen | Edit | Rename + manage metadata |
| Copy | Duplicate | Copy a file or folder |
| Arrow | Move | Relocate to another position |
| Bin | Delete | Remove permanently |
| i | Information | Detail view (UUID, size, path) |
| Arrow up | Upload | Load files into this folder |
| Pencil | Edit file | Text editor for compatible file types |
| Handle | Drag & drop | Intuitive moving with the mouse |

### Creating new folders

Via the **"Neuer Ordner"** (New folder) button with two options:
- **Öffentlich** (Public): folder reachable via HTTP (symlink in `web/files/`)
- **Nicht synchronisieren** (Do not synchronise): prevents database reconciliation

#### Creating nested folders

By entering a path such as `OrdnerA/OrdnerB`, subfolders can be created directly.

**Important**: with nested folders that have public access, only the **last** (innermost) folder receives the public status.

### Uploading files

**Default limits:**
- File size: up to 2 MB
- Image size: up to 3000 × 3000 pixels
- Images are automatically scaled down when the limit is exceeded

**DropZone**: can be enabled in the system settings for convenient drag & drop during upload.

**Uploading a file with the same name**: the existing file is updated, the **UUID is retained** — all references in content elements remain valid.

### FTP upload and synchronisation

For FTP uploads the file names must be **ASCII-compliant**. Special characters can cause problems.

| Problematic | Optimal |
|--------------|---------|
| `Wies'n-Festzug München.jpg` | `Wiesn-Festzug-Muenchen.jpg` |
| `Foto 2024 (1).png` | `foto-2024-1.png` |

After an FTP upload the database must be synchronised:
- Via the **synchronisation button** in the Dateiverwaltung, or
- Via CLI: `vendor/bin/contao-console contao:automator generateSymlinks`

---

## 2. Metadata

Metadata can be recorded for **all file types**. It is primarily used in image galleries and download elements.

### Supported metadata

| Field | Description |
|------|-------------|
| **Titel** (Title) | File title (e.g. for image captions) |
| **Alternativer Text** (Alternative text) | Alt attribute for images (accessibility) |
| **Link** | Link to an external URL or page |
| **Bildunterschrift** (Image caption) | Caption below images |
| **Lizenz-URL** (Licence URL) | Licence note (output as a JSON-LD schema) |

### Multilingual metadata

In multilingual projects, **separate metadata** can be created for each language. Contao automatically chooses the appropriate language for the visitor.

### HTML output example (image content element)

```html
<div class="ce_image first block">
  <figure class="image_container">
    <a href="https://contao.org/de/" title="Contao CMS">
      <img src="…" width="…" height="…" alt="Contao CMS" itemprop="image">
    </a>
    <figcaption class="caption">Contao CMS</figcaption>
  </figure>
</div>
```

### Licence URL (JSON-LD)

The Lizenz-URL is output as `schema.org/ImageObject` in JSON-LD format:

```json
{
  "@type": "ImageObject",
  "contentUrl": "…",
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
```

---

## 3. Controlling downloads

### Directory protection

New folders are **public** by default (reachable via HTTP). Deactivate the **"Öffentlich"** option when creating a folder in order to protect it.

**Important**: if a parent folder is public, the subfolders and files it contains **cannot** be protected separately.

#### Technical background

Public folders are created as **symlinks** under `web/files/`. Without a symlink, files are not reachable for browsers.

Non-public folders are **not directly accessible** via a browser, but can still be delivered through Contao content elements (Download, Downloads).

### Protecting a download element

Access to download elements is restricted via **protected pages** or **protected content elements**:

1. Restrict the protecting content element / page to certain member groups
2. Downloads are accessible exclusively via these content elements
3. Only authorised members can download the files

### HTML output of the download element

```html
<ul class="download_list">
  <li>
    <a href="?file=files/dokument.pdf" title="Herunterladen">
      dokument.pdf <span class="size">(124 KiB)</span>
    </a>
  </li>
</ul>
```

The path `?file=files/…` is processed by Contao and outputs the file only when the appropriate rights are present.

---

## Practical tips

### Finding a file UUID

The UUID is shown in the information dialog of a file (i icon). It can be used in development scenarios for direct database queries.

### Image not visible in the frontend?

Common cause: the folder is **not** marked as public. Solution:
1. Edit the folder (pen icon)
2. Enable the "Öffentlich" option
3. The symlink is created automatically

### Hiding the search

To hide the search area in the Dateiverwaltung, a DCA entry can be used:

```php
// contao/dca/tl_files.php
$GLOBALS['TL_DCA']['tl_files']['config']['notSearchable'] = true;
```
