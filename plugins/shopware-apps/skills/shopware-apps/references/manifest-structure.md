---
title: Manifest XML Structure
impact: CRITICAL
impactDescription: The manifest.xml is the entry point for every Shopware app
tags: manifest, xml, structure, sections, app
---

## Manifest XML Structure

The `manifest.xml` is the central configuration file for every Shopware app. It defines meta information, setup, permissions, webhooks, admin modules, payment methods, and more. It uses the XSD schema `manifest-3.0.xsd`.

**Incorrect (missing required meta fields):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Manifest/Schema/manifest-3.0.xsd">
    <meta>
        <name>MyApp</name>
    </meta>
</manifest>
```

**Correct (all required meta fields present):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Manifest/Schema/manifest-3.0.xsd">
    <meta>
        <name>MyApp</name>
        <label>My App</label>
        <label lang="de-DE">Meine App</label>
        <description>A useful Shopware app</description>
        <description lang="de-DE">Eine nützliche Shopware-App</description>
        <author>Your Company</author>
        <copyright>(c) Your Company</copyright>
        <version>1.0.0</version>
        <icon>Resources/config/plugin.png</icon>
        <license>MIT</license>
    </meta>
</manifest>
```

### Available Top-Level Sections

All sections except `<meta>` are optional:

| Section | Purpose |
|---------|---------|
| `<meta>` | App name, label, version, author, license (required) |
| `<setup>` | Registration URL and secret for app server communication |
| `<admin>` | Admin modules, action buttons, base-app-url, main-module |
| `<storefront>` | Template load priority |
| `<permissions>` | Entity read/create/update/delete/crud permissions |
| `<allowed-hosts>` | External hosts the app communicates with |
| `<custom-fields>` | Custom field set definitions |
| `<webhooks>` | Webhook event subscriptions |
| `<cookies>` | Cookie consent definitions |
| `<payments>` | Payment method definitions |
| `<shipping-methods>` | Shipping method definitions |
| `<rule-conditions>` | Custom rule condition definitions |
| `<tax>` | Tax provider definitions |
| `<gateways>` | Checkout, context, and IAP gateway URLs |

### App Directory Structure

```
custom/apps/
└── MyApp/
    ├── manifest.xml                    (required)
    ├── Resources/
    │   ├── config/
    │   │   ├── config.xml              (app configuration)
    │   │   └── plugin.png              (app icon)
    │   ├── entities.xml                (custom entities)
    │   ├── flow.xml                    (flow actions/triggers)
    │   ├── cms.xml                     (CMS blocks)
    │   ├── views/storefront/           (Twig templates)
    │   ├── app/
    │   │   ├── storefront/src/         (JS + SCSS)
    │   │   └── administration/snippet/ (admin snippets)
    │   ├── scripts/                    (app scripts)
    │   │   ├── cart/
    │   │   ├── product-page-loaded/
    │   │   └── rule-conditions/
    │   └── public/                     (public assets)
    └── theme.json                      (optional, makes app a theme)
```

### Installation

```bash
bin/console app:install --activate MyApp
bin/console cache:clear
```

The folder name **must** match the `<name>` element in manifest.xml.
