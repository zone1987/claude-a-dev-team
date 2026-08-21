---
title: Config.xml Field Types and Configuration
impact: HIGH
impactDescription: App configuration fields define the settings UI and must follow strict naming and type rules
tags: config, configuration, fields, settings
---

## Config.xml Field Types and Configuration

App configuration is defined in `Resources/config/config.xml`. Fields are grouped into cards, and each field type maps to a specific input in the admin UI. Config values are stored with the key format `{appName}.config.{fieldName}`.

### Card Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Manifest/Schema/manifest-3.0.xsd">
    <card>
        <title>General Settings</title>
        <title lang="de-DE">Allgemeine Einstellungen</title>

        <input-field type="text">
            <name>apiKey</name>
            <label>API Key</label>
            <label lang="de-DE">API-Schlüssel</label>
            <placeholder>Enter your API key</placeholder>
            <helpText>The API key from your provider dashboard</helpText>
            <required>true</required>
        </input-field>
    </card>
</config>
```

### All Available Field Types

| Type | Description | Value |
|------|-------------|-------|
| `text` | Single-line text input | string |
| `textarea` | Multi-line text input | string |
| `text-editor` | Rich text editor (HTML) | string |
| `url` | URL input with validation | string |
| `password` | Masked password input | string |
| `int` | Integer number input | integer |
| `float` | Decimal number input | float |
| `bool` | Toggle switch | boolean |
| `checkbox` | Checkbox | boolean |
| `datetime` | Date and time picker | string (ISO 8601) |
| `date` | Date picker | string |
| `time` | Time picker | string |
| `colorpicker` | Color picker | string (hex) |
| `single-select` | Dropdown select | string |
| `multi-select` | Multi-select dropdown | array |
| `price` | Price input with currency | object |

### Common Field Properties

All field types support these child elements:

```xml
<input-field type="text">
    <name>fieldName</name>              <!-- required, unique within config -->
    <label>English Label</label>        <!-- required -->
    <label lang="de-DE">German</label>  <!-- translatable -->
    <placeholder>Hint text</placeholder>
    <helpText>Explanation shown below the field</helpText>
    <defaultValue>some default</defaultValue>
    <required>true</required>
    <disabled>false</disabled>
</input-field>
```

### Field Name Rules

Field names **must** match the pattern `[a-zA-Z][a-zA-Z0-9]*`. No hyphens, underscores, or special characters. Must start with a letter.

**Incorrect (invalid field name):**

```xml
<input-field type="text">
    <name>api-key</name>   <!-- WRONG: hyphens not allowed -->
</input-field>

<input-field type="text">
    <name>2ndField</name>  <!-- WRONG: must start with a letter -->
</input-field>
```

**Correct (valid field names):**

```xml
<input-field type="text">
    <name>apiKey</name>
</input-field>

<input-field type="text">
    <name>secondField</name>
</input-field>
```

### Select Options

For `single-select` and `multi-select`, define options with `id` and translatable `name`:

```xml
<input-field type="single-select">
    <name>shippingMode</name>
    <label>Shipping Mode</label>
    <options>
        <option>
            <id>standard</id>
            <name>Standard Shipping</name>
            <name lang="de-DE">Standardversand</name>
        </option>
        <option>
            <id>express</id>
            <name>Express Shipping</name>
            <name lang="de-DE">Expressversand</name>
        </option>
    </options>
    <defaultValue>standard</defaultValue>
</input-field>
```

### Reading Config Values

**In Twig templates (storefront):**

```twig
{% set apiKey = config('MyApp.config.apiKey') %}
{% if config('MyApp.config.isEnabled') %}
    <div>Feature is enabled</div>
{% endif %}
```

**In app scripts:**

```twig
{% set apiKey = services.config.app('apiKey') %}
{% set mode = services.config.app('shippingMode') %}
```

Note: In app scripts, `services.config.app()` only requires the field name without the app name prefix.

### Config Key Format

Config values are stored with the key `{appName}.config.{fieldName}`. For an app named `MyApp` with a field `apiKey`, the full config key is `MyApp.config.apiKey`.
