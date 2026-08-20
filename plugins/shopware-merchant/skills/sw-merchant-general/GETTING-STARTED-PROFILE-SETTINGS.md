# Profileinstellungen (Profile settings)

**Source**: https://docs.shopware.com/de/shopware-6-de/einstellungen/Profileinstellungen  
**Applies from**: Shopware 6.4.8.0

## Overview

The profile settings allow every admin user to configure their **personal** display
and preferences in the administration.

**Access**: bottom left in the administration → click the profile picture/name

---

## Profile area

### Personal information
| Field | Description | Changeable here? |
|---|---|---|
| First name | Display name in the administration | No¹ |
| Last name | Display name in the administration | No¹ |
| User name | Login name | No¹ |
| Email address | Login & notifications | Yes |
| Profile picture | Upload your own image (JPG, PNG) | Yes |
| Administration language | German, English, more with installed language packs | Yes |

> ¹ Core profile information (name, user name) can only be changed under:
> **Einstellungen** (Settings) **> System > Benutzer & Rechte** (Users & permissions) **>** edit user [name]

---

## Changing the password

1. In the profile area, navigate to **Passwort** (Password)
2. Enter the current password
3. Enter the new password (twice for confirmation)
4. Save

---

## Search settings

Every user can configure individually **which entities** the administration search
should index and search:

- **Alle auswählen** (Select all) – activate all available entities
- **Alle abwählen** (Deselect all) – deactivate all entities
- **Standard wiederherstellen** (Restore default) – back to the Shopware default

### Searchable entities (default)
- Produkte (Products)
- Bestellungen (Orders)
- Kunden (Customers)
- Kategorien (Categories)
- Medien (Media)
- Hersteller (Manufacturers)
- Eigenschaften (Properties)

---

## Keyboard shortcut overview

The profile has a **Tastenkürzel** (Keyboard shortcuts) section with all available shortcuts:

| Shortcut | Action |
|---|---|
| `Strg/Cmd + F` | Open the quick search |
| `#` in the search | Open the module filter |
| `Strg/Cmd + S` | Save (in forms) |
| `Esc` | Close a modal / overlay |

---

## Administration language

- **Switching**: Profil (Profile) > Sprache (Language) > selection → reload the page
- **Important**: this only changes the **administration language**, not the storefront language
- For new languages: install the Sprachpaket extension
  → See `../../../sw-merchant-extensions/references/deep/sprachpaket.md`
