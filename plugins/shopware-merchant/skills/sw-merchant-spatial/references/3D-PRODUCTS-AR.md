# Shopware 6 – 3D product models & augmented reality: full reference

> Source: https://docs.shopware.com/de/shopware-6-de/kataloge/produkte
> Source (media/AR): https://docs.shopware.com/de/shopware-6-de/Inhalte/medien
> Plan: Rise (or higher)

---

## Contents

- [1. Prerequisites](#1-prerequisites)
- [2. Uploading a 3D model to a product](#2-uploading-a-3d-model-to-a-product)
- [3. Configuring the AR view](#3-configuring-the-ar-view)
- [4. Storefront presentation](#4-storefront-presentation)
- [5. Device compatibility](#5-device-compatibility)
- [6. 3D viewer block in the Erlebniswelten](#6-3d-viewer-block-in-the-erlebniswelten)
- [7. Technical background: GLB / glTF](#7-technical-background-glb-gltf)
- [Source](#source)

## 1. Prerequisites

- **Shopware plan**: Rise or higher
- **File format**: exclusively `.glb` (GL Transmission Format Binary)
  - GLB is a binary format based on the widely used **glTF standard**
  - A frequently used format for exchanging 3D models between applications
- **3D rendering library**: ThreeJS (open source, browser-based)

---

## 2. Uploading a 3D model to a product

### 2.1 Path

**Kataloge > Produkte** (Catalogues > Products) → open a product or create a new one → tab **Allgemein** (General) → section **Medien** (Media)

### 2.2 Steps

1. In the **Medien** section click the button for adding media
2. Select the `.glb` file or drag and drop it into the media gallery
3. The 3D model appears in the media overview of the product

### 2.3 Important limitations

| Limitation | Detail |
|---|---|
| No cover image | A 3D model can **not** be used as the product cover image |
| No Erlebniswelten | 3D models from the product tab can **not** be used directly in the Erlebniswelten |
| No automatic optimisation | 3D files are stored in their original quality and size |
| Performance | Large, unoptimised files can increase the storefront loading time |

> ⚠ **Recommendation**: upload only already optimised 3D files in order to avoid performance problems.

---

## 3. Configuring the AR view

### 3.1 Path

**Inhalte > Medien** (Content > Media) → click the uploaded 3D file → area **Konfiguration** (Configuration)

### 3.2 Enabling AR

1. Find and click the file in the media library under **Inhalte > Medien**
2. In the detail area under **Konfiguration** enable the **AR-Ansicht** (AR view) toggle
3. **Set the product size** (mandatory):
   - Shopware does not normalise the size of the 3D model automatically
   - The real dimension of the product has to be entered manually
   - Without a correct size specification the product appears in AR with wrong dimensions

### 3.3 Why the size specification matters

> "The size of the product in AR has to be set beforehand, because the size of the product
> is not normalised in Shopware."

An incorrectly dimensioned AR object (too large or too small) can make the AR experience
useless for customers.

---

## 4. Storefront presentation

### 4.1 3D viewer on the product detail page

- A **3D icon** appears **at the bottom right** of the product image on the detail page
- Clicking the icon opens the integrated 3D viewer (ThreeJS-based)
- Customers can:
  - rotate the product freely (mouse drag / touch gesture)
  - zoom (mouse wheel / pinch gesture)
  - view it from any angle

### 4.2 AR experience via QR code

1. The customer clicks the 3D icon on the product detail page
2. A **QR code** is generated and displayed
3. The customer scans the QR code with their mobile device
4. The AR view starts in the browser of the mobile device (no app download required)
5. The 3D model appears in the customer's real environment in the defined dimensions

---

## 5. Device compatibility

### 5.1 Supported systems for AR

| Operating system | Browser | Minimum version | Additional requirement |
|---|---|---|---|
| iOS | Safari | iOS 12+ | — |
| Android | Chrome | Android 8.0+ | ARCore 1.9+ |

> ⚠ Older browser versions can experience performance limitations.
> Not all devices support ARCore – this is the responsibility of the device manufacturer.

---

## 6. 3D viewer block in the Erlebniswelten

> For direct integration into Erlebniswelten layouts a dedicated **3D-Modell** (3D model) block is available.
> It is independent of the product media.

### 6.1 Availability

- From the commercial **Rise** plan
- File format: exclusively `.glb`

### 6.2 Adding the block

1. **Inhalte > Erlebniswelten** (Content > Shopping Experiences) → open the desired layout
2. Open the block library → drag and drop the **3D-Modell** block into the layout
3. Upload the `.glb` file in that block or select it from the media library
4. Adjust the presentation options as needed

### 6.3 Interaction options for customers

- View the product from various angles
- Zoom and rotate
- Improved perception of structure, surface and shape

---

## 7. Technical background: GLB / glTF

- **glTF** (GL Transmission Format) is an open standard of the Khronos Consortium
- **GLB** is the binary variant of glTF (everything bundled in one file)
- Advantages: small file format, wide compatibility, usable natively in WebGL
- Shopware uses **ThreeJS** as the JavaScript library for rendering

---

## Source
https://docs.shopware.com/de/shopware-6-de/kataloge/produkte
https://docs.shopware.com/de/shopware-6-de/Inhalte/Erlebniswelten
https://docs.shopware.com/de/shopware-6-de/spatial-commerce
