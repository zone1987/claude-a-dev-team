# Shopware Publisher – draft management for Erlebniswelten

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/ShopwarePublisher  
**Plan**: Shopware Evolve (or higher)

## Overview

The **Shopware Publisher** enables collaborative content management:
create several versions (drafts) of an Erlebniswelt (Shopping Experience) without changing the **active live version**.

Ideal for:
- Preparing seasonal campaigns
- Content reviews before publication
- Team collaboration on landing pages

---

## Installation

1. Open **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions)
2. Log in on the **Shopware Account tab** (licence verification)
3. Install and activate the Publisher (**Apps tab**)

---

## Core features

### 1. Creating a draft

**Normal saving** (without the Publisher): directly into the live version  
**With the Publisher**: the dropdown arrow next to the save button → "Als neuen Entwurf speichern" (Save as a new draft)

Options when saving:
| Option | Description |
|---|---|
| Direkt speichern (Save directly) | Apply it to the live version immediately |
| Als neuen Entwurf speichern | Create a new draft version (live stays unchanged) |

### 2. Managing drafts

In the **Erlebniswelten** overview (Content > Erlebniswelten (Shopping Experiences)):
- Next to each Erlebniswelt: the number of drafts and the live version are visible
- The number of recent changes made by other users

### 3. Activity feed (activity tracking)

An integrated feed shows:
- Which user made changes
- What was changed
- When it was changed

This applies to the live version as well as to the drafts.

### 4. Preview

Drafts can be shown in the **storefront preview** before they are published:
- Open the Erlebniswelt → select the draft → click "Vorschau" (Preview)
- Shows exactly how the draft would look in the frontend

---

## Workflow example: a seasonal campaign

```
1. Current home page (Live)  
   └── Draft: "Weihnachten 2024" (created in parallel)
       ├── Edited by the content team
       ├── Reviewed by the marketing lead
       ├── Check the Vorschau (preview)
       └── On 1 December: publish Draft → Live
```

---

## User permissions for the Publisher

Different user roles can have different Publisher permissions:

| Permission | Description |
|---|---|
| Create drafts | Create a new draft |
| Edit drafts | Change an existing draft |
| Publish drafts | Turn a draft into the live version |
| Delete drafts | Remove drafts |

User permissions: **Einstellungen** (Settings) **> System > Benutzer & Rechte** (Users & permissions) **> Rollen** (Roles)

---

## Difference from the standard Erlebniswelten saving

| Aspect | Without the Publisher | With the Publisher |
|---|---|---|
| Saving = live | Yes, immediately | No – only after publishing |
| Several versions | No | Yes (an unlimited number of drafts) |
| Preview | Yes (but live) | Yes (drafts can be previewed) |
| Change history | No | Yes (activity feed) |
| Rollback | Limited | Yes (activate a draft) |
