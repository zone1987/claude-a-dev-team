# Plugin Configuration

## Overview

Plugin configuration is defined in `src/Resources/config/config.xml` and managed via `SystemConfigService`. Configuration values are accessible in the Administration under Extensions > My extensions > [Plugin] > Configure.

## config.xml Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/System/SystemConfig/Schema/config.xsd">

    <card>
        <title>General Settings</title>
        <title lang="de-DE">Allgemeine Einstellungen</title>

        <input-field type="text">
            <name>apiKey</name>
            <label>API Key</label>
            <label lang="de-DE">API-Schlüssel</label>
            <placeholder>Enter your API key...</placeholder>
            <placeholder lang="de-DE">API-Schlüssel eingeben...</placeholder>
            <helpText>Your API key from the provider dashboard</helpText>
            <helpText lang="de-DE">Ihr API-Schlüssel aus dem Anbieter-Dashboard</helpText>
        </input-field>

        <input-field type="bool">
            <name>active</name>
            <label>Enable Plugin</label>
            <label lang="de-DE">Plugin aktivieren</label>
            <defaultValue>false</defaultValue>
        </input-field>
    </card>
</config>
```

## Available Field Types

| Type | Element | Description |
|------|---------|-------------|
| `text` | `<input-field type="text">` | Single-line text |
| `textarea` | `<input-field type="textarea">` | Multi-line text |
| `bool` | `<input-field type="bool">` | Toggle switch |
| `checkbox` | `<input-field type="checkbox">` | Checkbox |
| `int` | `<input-field type="int">` | Integer number |
| `float` | `<input-field type="float">` | Decimal number |
| `password` | `<input-field type="password">` | Password (masked) |
| `single-select` | `<input-field type="single-select">` | Dropdown |
| `multi-select` | `<input-field type="multi-select">` | Multi-select dropdown |
| `colorpicker` | `<input-field type="colorpicker">` | Color picker |
| `date` | `<input-field type="date">` | Date picker |
| `datetime` | `<input-field type="datetime">` | Date+time picker |
| `url` | `<input-field type="url">` | URL input |
| `html` | `<input-field type="html">` | HTML editor |

## Select Fields with Options

```xml
<input-field type="single-select">
    <name>displayMode</name>
    <label>Display Mode</label>
    <label lang="de-DE">Anzeigemodus</label>
    <options>
        <option>
            <id>default</id>
            <name>Default</name>
            <name lang="de-DE">Standard</name>
        </option>
        <option>
            <id>compact</id>
            <name>Compact</name>
            <name lang="de-DE">Kompakt</name>
        </option>
        <option>
            <id>extended</id>
            <name>Extended</name>
            <name lang="de-DE">Erweitert</name>
        </option>
    </options>
    <defaultValue>default</defaultValue>
</input-field>
```

## Reading Configuration in PHP

Use `SystemConfigService` to read plugin configuration values:

```php
use Shopware\Core\System\SystemConfig\SystemConfigService;

class MyService
{
    public function __construct(
        private readonly SystemConfigService $systemConfigService,
    ) {}

    public function getApiKey(?string $salesChannelId = null): ?string
    {
        // Key pattern: {PluginName}.config.{fieldName}
        return $this->systemConfigService->getString(
            'FfContentPlus.config.apiKey',
            $salesChannelId
        );
    }

    public function isActive(?string $salesChannelId = null): bool
    {
        return $this->systemConfigService->getBool(
            'FfContentPlus.config.active',
            $salesChannelId
        );
    }
}
```

## Configuration Key Pattern

```
{PluginName}.config.{fieldName}
```

Examples:
- `FfContentPlus.config.apiKey`
- `FfContentPlus.config.active`
- `FfContentPlus.config.displayMode`

## Sales Channel-Specific Configuration

Configuration can be set per sales channel. When reading, pass the `$salesChannelId`:

```php
// Global value (fallback)
$value = $systemConfigService->get('FfContentPlus.config.apiKey');

// Sales channel-specific value
$value = $systemConfigService->get('FfContentPlus.config.apiKey', $salesChannelId);
```

## SystemConfigService Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `get(string $key, ?string $salesChannelId = null)` | `mixed` | Get raw value |
| `getString(string $key, ?string $salesChannelId = null)` | `string` | Get as string |
| `getInt(string $key, ?string $salesChannelId = null)` | `int` | Get as integer |
| `getFloat(string $key, ?string $salesChannelId = null)` | `float` | Get as float |
| `getBool(string $key, ?string $salesChannelId = null)` | `bool` | Get as boolean |
| `set(string $key, mixed $value, ?string $salesChannelId = null)` | `void` | Set a value |
| `delete(string $key, ?string $salesChannelId = null)` | `void` | Delete a value |

## Advanced: Component Override

Replace the default input component for a field:

```xml
<input-field type="text">
    <name>entitySelect</name>
    <label>Select a product</label>
    <componentName>sw-entity-single-select</componentName>
</input-field>
```
