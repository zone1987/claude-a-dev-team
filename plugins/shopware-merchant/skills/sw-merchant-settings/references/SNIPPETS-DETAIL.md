# Shopware 6 – Textbausteine (Snippets) – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/Textbausteine

---

## Contents

- [Overview](#overview)
- [Default snippet sets](#default-snippet-sets)
- [Management functions (overview)](#management-functions-overview)
- [Editing a snippet](#editing-a-snippet)
- [Reset dialog](#reset-dialog)
- [Filter options](#filter-options)
- [Creating a new snippet](#creating-a-new-snippet)
- [Creating a new snippet set](#creating-a-new-snippet-set)
- [Tips & tricks](#tips--tricks)

## Overview

**Path:** Einstellungen (Settings) > Shop > Textbausteine  
Snippets are used to translate and adapt texts in the storefront or in documents.

---

## Default snippet sets

- `BASE de-DE` — default German translations
- `BASE en-GB` — default English translations

> The base JSON files (`messages.de.base.json`, `storefront.de.json`) should **not be edited manually**, as they are needed for resetting.

---

## Management functions (overview)

| Function | Description |
|---|---|
| Mehrfachänderung (Bulk edit) | Edit several sets at the same time |
| Textbaustein-Set hinzufügen (Add snippet set) | Create a new set based on the base files |
| Kontextmenü (Context menu) | Edit, duplicate or delete sets |
| Inline-Bearbeitung (Inline editing) | Double-click enables direct changes |

---

## Editing a snippet

### Access paths
1. Click the set name directly
2. Select sets via checkbox → "Mehrfachänderung"
3. Use the context menu

### List functions
- Name column: snippet key
- Separate input fields per set
- Refresh button: refresh the view
- Filter options available

### Detail page
By clicking a key or "Bearbeiten" (Edit), translations can be edited **across sets**.

---

## Reset dialog

- Selection via checkboxes: which sets should be reset
- Display of the current and the original translation
- "Für alle Textbaustein-Sets zurücksetzen" (Reset for all snippet sets): global reset

---

## Filter options

| Filter | Description |
|---|---|
| Nur leere Textbausteine (Empty snippets only) | Entries without content |
| Nur angepasste Textbausteine (Customised snippets only) | Manually edited texts |
| Nur hinzugefügte Textbausteine (Added snippets only) | Texts created by admins |
| Autor (Author) | Filters by creator (default: "Shopware") |
| Bereich/Funktion (Area/function) | e.g. `_checkout_` |

---

## Creating a new snippet

**Global creation** — no separate creation per set is needed.

### Requirements
- Unique name/key (no spaces or special characters)
- A descriptive name is recommended (e.g. `checkout.headline`)
- Separate input fields per available set

---

## Creating a new snippet set

### Method 1: adding via button
1. Inline editing with the form activated
2. Enter a name
3. Define the **Locale** (e.g. `en-GB`, `de-DE` or a two-letter ISO 639-1 code)
4. Select the **Basisdatei** (Base file) (fallback)
5. Save

> The locale follows the **BCP 47 standard** and is limited to ISO 639-1 language codes.

### Method 2: duplicating
1. Context menu of an existing set
2. The copy receives the suffix `_Kopie`
3. Rename via double-click in the overview (not on the detail page)

---

## Tips & tricks

### Embedding links in snippets
```html
<a href="https://example.com">Angezeigter Text</a>
```

### Editing the service hotline
- Snippet key: `footer.serviceHotline`
- Displayed in the storefront footer
- Reachable via Einstellungen > Shop > Textbausteine

### Inserting line breaks
```html
After the comma,<br> a line break follows.
```
