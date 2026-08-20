# Sprachpaket (Language pack) – multilingualism for admin & storefront

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/sprachpaket  
**Availability**: Free in the Shopware Store  
**Important**: No longer supported from Shopware 6.8!

## Overview

The **Sprachpaket** lets you run Shopware 6 in up to 29 languages –
for the administration as well as for the storefront.

---

## IMPORTANT: deprecation from version 6.8

> **The Sprachpaket is no longer supported from Shopware 6.8.**
> From Shopware 6.7.3.0 a **native language management system** is available.
> → Migration to the native system is recommended for new installations.

---

## Supported languages (29)

| Language | Language | Language |
|---|---|---|
| Bosnian | Bulgarian | Chinese (simplified) |
| Chinese (traditional) | Danish | English (USA) |
| Finnish | French | Greek |
| Hebrew | Hindi | Indonesian |
| Italian | Japanese | Korean |
| Croatian | Dutch | Norwegian |
| Persian | Polish | Portuguese |
| Russian | Swedish | Serbian |
| Slovak | Spanish | Czech |
| Turkish | Ukrainian | Hungarian |
| Vietnamese | | |

(English and German are included in Shopware by default)

---

## Installation

### Option 1: first-run setup assistant
- In the wizard step "Erweiterungen" (Extensions), search for and install the Sprachpaket

### Option 2: Shopware Store
1. https://store.shopware.com → search for "Sprachpaket Shopware 6"
2. Activate the free licence
3. In the admin: **Erweiterungen > Meine Erweiterungen** (My extensions) → install + activate

---

## Configuration

### For the administration (admin interface)
After installation and activation:
1. **Profil** (Profile, bottom left) → select the language
2. Reload the page → admin in the new language

### For the storefront
Storefront languages have to be enabled explicitly:
1. **Verkaufskanäle** (Sales channels) → open the storefront
2. Section "Sprachen" (Languages) → add the desired language
3. Set it as the default language or as an additional language

---

## Translation workflow

Once a language has been added to the sales channel:

1. Translate **Produkte** (Products): Katalog > Produkte > [product] → switch language at the top right
2. Translate **Kategorien** (Categories): Katalog > Kategorien → switch language
3. Translate **E-Mail-Templates**: Einstellungen (Settings) > E-Mail-Templates → switch language
4. Translate **Erlebniswelten** (Shopping Experiences): Content > Erlebniswelten → switch language

### Inheritance model
- Fields without a translation inherit from the **default/fallback language**
- Inheritance is indicated by the green padlock icon
- Opening the padlock = the field can be overwritten

---

## Migration to the native language system (from 6.7.3.0)

From Shopware 6.7.3.0 the Sprachpaket is no longer necessary:
- Manage languages directly in the shop settings
- No separate extension download needed
- **Einstellungen > Sprachen** in the admin

For existing installations with the Sprachpaket:
1. Configure the native languages in the admin
2. Deactivate the Sprachpaket (after verifying that all translations are present)
3. Uninstall the Sprachpaket
