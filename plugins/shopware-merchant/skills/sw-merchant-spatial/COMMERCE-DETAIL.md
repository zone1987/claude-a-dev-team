# Shopware 6 – Spatial Commerce: full reference

> Source: https://docs.shopware.com/de/shopware-6-de/spatial-commerce
> Applies from: Shopware 6.6.8.1+ (Scene Editor), 6.7.9.0+ (Bundles)

---

## Contents

- [1. Spatial Commerce overview](#1-spatial-commerce-overview)
- [2. 3D product models & augmented reality](#2-3d-product-models-augmented-reality)
- [3. 3D viewer block for the Erlebniswelten](#3-3d-viewer-block-for-the-erlebniswelten)
- [4. Immersive Elements app](#4-immersive-elements-app)
- [5. Scene Editor](#5-scene-editor)
- [Source](#source)

## 1. Spatial Commerce overview

Under **Spatial Commerce** Shopware bundles all functions for three-dimensional and
immersive product presentation. The goal is to offer customers a more realistic shopping
experience that goes beyond classic 2D product photos.

### Included functions

1. **3D product models** – upload 3D files (.glb) to products and have them displayed in the
   storefront as a 3D viewer as well as via augmented reality (AR).
2. **3D viewer block for the Erlebniswelten** – a standalone CMS block that presents 3D models
   in any layout (drag & drop).
3. **Immersive Elements** – an app in cooperation with Instorier (Norwegian experts for
   digital storytelling); offers six specialised 3D blocks for the Erlebniswelten.
4. **Scene Editor** – a tool for creating 3D scenes, placing products and making
   unlimited image exports (beta from 6.6.8.1).

### Plan requirements

| Function | Minimum plan |
|---|---|
| 3D models on products | Rise |
| 3D viewer block | Rise |
| Immersive Elements | Rise (or €49/month in the Store) |
| Scene Editor | Rise (from 6.6.8.1) |

---

## 2. 3D product models & augmented reality

Path: **Kataloge > Produkte** (Catalogues > Products) → tab **Allgemein** (General) → section **Medien** (Media)

### 2.1 File format

- Only `.glb` (GL Transmission Format Binary) is supported
- GLB is a binary format based on the widely used glTF standard
- 3D files are **not optimised automatically** – already optimised files
  should be uploaded in order to avoid performance problems
- **Important limitation**: a 3D model can **not** be used as the cover image of a
  product or directly within the Erlebniswelten

### 2.2 Uploading a 3D model

1. **Kataloge > Produkte** → open the product
2. Tab **Allgemein** → section **Medien**
3. Upload the 3D file (.glb) (like normal media)
4. The model appears in the media gallery of the product

### 2.3 Configuring the AR view

1. **Inhalte > Medien** (Content > Media) → click the uploaded 3D file
2. Section **Konfiguration** (Configuration) → enable the **AR-Ansicht** (AR view) toggle
3. **Set the product size**: since Shopware does not normalise the size, the
   real product size has to be specified manually
   > ⚠ Without a correct size specification the product appears in AR with wrong dimensions

### 2.4 Storefront presentation

- The 3D icon appears **at the bottom right** of the product image on the detail page
- Clicking the icon opens the 3D viewer (ThreeJS-based)
- **AR view**: a click generates a QR code → the customer scans it with a mobile device → the AR view starts
- AR runs in the browser (no app download needed)

### 2.5 AR device compatibility

| Operating system | Browser | Minimum version |
|---|---|---|
| iOS | Safari | iOS 12+ |
| Android | Chrome | Android 8.0+ with ARCore 1.9+ |

Older browser versions can show performance limitations.

### 2.6 The ThreeJS library

Shopware uses the open source library **ThreeJS** for the 3D rendering in the browser.

---

## 3. 3D viewer block for the Erlebniswelten

Path: **Inhalte > Erlebniswelten** (Content > Shopping Experiences) → edit the layout → add a block

### 3.1 Function

The **3D-Modell** (3D model) block allows 3D models to be integrated into any
Erlebniswelten layout. Customers can:

- view the product from various angles
- zoom (mouse wheel or pinch gesture)
- rotate (mouse drag or touch gesture)

This improves the understanding of the product with regard to **structure, surface and shape**
compared with classic 2D photos.

### 3.2 Availability

- Available from the commercial **Rise** plan
- File format: exclusively `.glb`

### 3.3 Adding the block

1. Open the Erlebniswelten layout
2. Drag the block out of the block library via **drag & drop**
3. In the block: upload the `.glb` file or select it from the media library
4. Configure the presentation settings

---

## 4. Immersive Elements app

See the detail skill: `sw-merchant-spatial-immersive-elements`

Short overview of the six elements:

| Element | Function | Price |
|---|---|---|
| Cylinder Gallery | 360° image slider with mouse control | Included |
| Depth Gallery | Parallax effect (mouse + scrolling) | Included |
| Exploded View | Interactive breakdown of the product into individual parts | €49/month add-on |
| 3D Model Journey | Animated 360° product tour with hotspots + audio | Included |
| Slide Behind Gallery | Horizontal content change (deeper than a slider) | Included |
| VR Cinema | 3D/VR experience (webp video format) | Included |

---

## 5. Scene Editor

See the detail skill: `sw-merchant-spatial-scene-editor`

Short overview:
- Path: **Inhalte > Scene Editor**
- Status: **Beta** (Rise plan, from 6.6.8.1)
- Function: create 3D scenes, place products, export images

---

## Source
https://docs.shopware.com/de/shopware-6-de/spatial-commerce
