---
title: Manifest Meta Section
impact: CRITICAL
impactDescription: The meta section contains required app identity information
tags: manifest, meta, name, label, version, author, license
---

## Manifest Meta Section

The `<meta>` section is the only required section in manifest.xml. It defines the app's identity, version, and display information.

### Required Elements

| Element | Description |
|---------|-------------|
| `<name>` | Technical name (must match folder name, UpperCamelCase) |
| `<label>` | Display name shown in admin (translatable) |
| `<author>` | Developer/company name |
| `<copyright>` | Copyright notice |
| `<version>` | Semantic version (e.g., 1.0.0) |
| `<license>` | License identifier (e.g., MIT) |

### Optional Elements

| Element | Description |
|---------|-------------|
| `<description>` | App description (translatable) |
| `<icon>` | Path to app icon relative to manifest |
| `<privacy>` | URL to privacy policy |
| `<privacyPolicyExtensions>` | Privacy policy changes the shop owner must make (translatable) |
| `<compatibility>` | Version compatibility string |

**Incorrect (name doesn't match folder):**

```xml
<!-- Folder: custom/apps/MyShopApp/ -->
<meta>
    <name>MyApp</name> <!-- WRONG: doesn't match folder name -->
    <label>My App</label>
    <author>Dev</author>
    <copyright>(c) Dev</copyright>
    <version>1.0.0</version>
    <license>MIT</license>
</meta>
```

**Correct (name matches folder, with translations):**

```xml
<!-- Folder: custom/apps/MyShopApp/ -->
<meta>
    <name>MyShopApp</name>
    <label>My Shop App</label>
    <label lang="de-DE">Meine Shop App</label>
    <description>Extends the shop with great features</description>
    <description lang="de-DE">Erweitert den Shop um tolle Funktionen</description>
    <author>Your Company Ltd.</author>
    <copyright>(c) by Your Company Ltd.</copyright>
    <version>1.0.0</version>
    <icon>Resources/config/plugin.png</icon>
    <license>MIT</license>
    <privacy>https://example.com/privacy</privacy>
</meta>
```

### Translation Pattern

Translatable elements use the `lang` attribute with BCP 47 locale codes. Default is `en-GB`:

```xml
<label>English label</label>
<label lang="de-DE">German label</label>
<label lang="fr-FR">French label</label>
```
