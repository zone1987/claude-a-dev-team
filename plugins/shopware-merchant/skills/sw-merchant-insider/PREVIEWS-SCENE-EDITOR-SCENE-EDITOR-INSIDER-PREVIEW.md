# Shopware 6 – Scene Editor (Beta): full reference

> Source: https://docs.shopware.com/de/shopware-6-de/commercial-features/scene-editor
> Insider Previews: https://docs.shopware.com/de/shopware-6-de/insider-previews
> Plan: Rise or higher | Minimum version: 6.6.8.1 | Status: Beta

---

## Contents

- [1. Overview](#1-overview)
- [2. Activation (Insider Previews)](#2-activation-insider-previews)
- [3. Plan requirements](#3-plan-requirements)
- [4. Beta status – notes](#4-beta-status-notes)
- [5. Scene overview](#5-scene-overview)
- [6. Creating a new scene](#6-creating-a-new-scene)
- [7. Area: 3D objects](#7-area-3d-objects)
- [8. Area: scene (global settings)](#8-area-scene-global-settings)
- [9. Exporting an image – complete process](#9-exporting-an-image-complete-process)
- [10. Shapes (primitives)](#10-shapes-primitives)
- [11. Community Hub](#11-community-hub)
- [Source](#source)

## 1. Overview

The **Scene Editor** offers the possibility to use the full potential of 3D models
for creating product images. The core functions:

- Build a wide variety of **3D scenes**
- **Place and arrange** products in the scene
- Generate **unlimited images** from the scenes
- Exported images are perfectly matched to your own products

**Path in the admin**: **Inhalte** (Content) > Scene Editor

---

## 2. Activation (Insider Previews)

### Versions 6.6.8.1 – 6.6.10.5

In these versions the Scene Editor is an **insider preview feature** and must
first be enabled explicitly:

1. Open the **Insider Previews** module in the admin
2. Find the **Scene Editor** in the list of available preview features
3. **Enable** the feature
4. The Scene Editor is then reachable under **Inhalte > Scene Editor**

### From version 6.6.10.6

The Scene Editor is available directly, without an activation step.

---

## 3. Plan requirements

| Plan | Scene Editor available |
|---|---|
| Starter | No |
| Basics | No |
| Rise | Yes (from 6.6.8.1) |
| Evolve | Yes |
| Beyond | Yes |

---

## 4. Beta status – notes

> ⚠ **This feature is currently in beta status.** The feature scope is
> still limited in this version and may be expanded further in future updates.
> Its behaviour and scope may still change.

Shopware welcomes feedback in order to develop the feature in a targeted way.
Feedback can be submitted via the linked feedback forum.

---

## 5. Scene overview

The Scene Editor start page lists all scenes that have been created.

### Controls

| Element | No. | Function |
|---|---|---|
| **Listenansicht** (List view) | (1) | Switch between tile and list view |
| **Sortieren nach** (Sort by) | (2) | Sorting: creation date, modification date, name |
| **Kontextmenü** (Context menu) | (3) | Delete, duplicate, edit |
| **Neue Szene erstellen** (Create new scene) | (4) | Open the creation dialog |

Opening directly: clicking a scene entry opens editing immediately.

---

## 6. Creating a new scene

1. Click **"Neue Szene erstellen"**
2. Assign a scene name (the only mandatory field)
3. Automatic redirection into the editing view

---

## 7. Area: 3D objects

### 7.1 Main elements

| Element | No. | Description |
|---|---|---|
| Object in the workspace | (1) | Main window; freely rotatable grid; shows the selected 3D object |
| **3D-Objekt hinzufügen** (Add 3D object) | (2) | Dropdown menu with various object types |
| **Gruppe hinzufügen** (Add group) | (3) | Combine several objects into one group |
| **Ansichtsauswahl** (View selection) | (4) | Camera/perspective switch (e.g. "Freie Ansicht" – free view) |
| **Verschieben-Werkzeug** (Move tool) | (5) | Activate the move tool |
| **Drehen-Werkzeug** (Rotate tool) | (6) | Activate the rotate tool |
| **Skalieren-Werkzeug** (Scale tool) | (7) | Activate the scale tool |
| Light Settings | (8) | Configure the lighting |
| **Bild exportieren** (Export image) | (9) | Export the scene as an image file |
| **Szene speichern** (Save scene) | (10) | Save the complete scene persistently |

---

### 7.2 Move tool – detail

**Colour coding of the axis arrows**:

| Colour | Axis | Direction |
|---|---|---|
| Blue | Z axis | Forward / backward |
| Green | Y axis | Up / down |
| Red | X axis | Left / right |

**Coloured squares**: movement along combined planes
**Centre square**: free movement in all directions

---

### 7.3 Rotate tool – detail

**Colour coding of the rotation rings**:

| Colour | Rotation |
|---|---|
| Red | Tilt forward/backward (pitch) |
| Blue | Tilt left/right (roll) |
| Green | Rotate around its own axis (yaw) |
| Yellow (outer ring) | Rotation from the camera perspective |

---

### 7.4 Scale tool – detail

| Mode | Description |
|---|---|
| **Uniform (default)** | Proportions are preserved; all axes scale simultaneously |
| **Axis-specific** | Disable the option for individual axis scaling |

**Axis-specific squares**:

| Colour | Axis |
|---|---|
| Green | Height |
| Red | Width |
| Blue | Depth |

---

### 7.5 Light Settings – detail

| Parameter | Options |
|---|---|
| **Typ** (Type) | Scene-wide light **or** object-specific light |
| **Einstellungen** (Settings) | Predefined presets **or** custom adjustments |
| **Lichtfarbe** (Light colour) | Enter a colour code (example: `#ffffff` = white light) |
| **Light Intensity** | Slider 0–100 % |

> The view of the light options can differ depending on the selected object.

---

## 8. Area: scene (global settings)

| Setting | No. | Description |
|---|---|---|
| **Szenenname** (Scene name) | (1) | Edit the name of the scene |
| **Hintergrundfarbe** (Background colour) | (2) | Configure the background colour of the scene |
| **Bodenfarbe** (Floor colour) | (3) | Configure the floor colour of the scene |

---

## 9. Exporting an image – complete process

### Step by step

1. Click **"Bild exportieren"** (top right)
2. Select the **Kamera** (Camera) **(1)**: which of the configured cameras should be used for the export?
3. Choose the **Auflösung** (Resolution) **(2)**: template or custom
4. Enter the **Breite** (Width) **(3)** in pixels
5. Enter the **Höhe** (Height) **(4)** in pixels
6. Click **"Bild speichern"** (Save image) **(5)**
7. The image is saved automatically in the media folder **"Scene Editor Media"**

### Using the exported images

Exported images can, directly from the media library:
- Be assigned as a product image
- Be built into **Erlebniswelten** (Shopping Experiences)
- Be used for marketing materials

---

## 10. Shapes (primitives)

Basic geometric shapes as stage elements:

### Adding

1. **"3D-Objekt hinzufügen"** → tab **"Primitive"** in the "Medien auswählen" (Select media) window
2. Select the desired shape and add it

### Configurable

- **Material properties** (surface, gloss, reflection)
- **Colour** of the shape

### Typical use

- Pedestal / platform for the product
- Background wall
- Decorative geometric elements

---

## 11. Community Hub

An interactive learning path for the Scene Editor is available in the **Community Hub**.
There, features can be tried out directly and knowledge expanded in a playful way.

---

## Source
https://docs.shopware.com/de/shopware-6-de/commercial-features/scene-editor
https://docs.shopware.com/de/shopware-6-de/insider-previews
