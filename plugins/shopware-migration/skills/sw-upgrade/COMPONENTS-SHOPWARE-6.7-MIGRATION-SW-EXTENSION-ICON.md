# sw-extension-icon

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| src | `any` | — | yes |  |
| alt | `any` | `''` | no |  |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```twig
    <sw-extension-icon
        class="sw-extension-config__extension-icon"
        :src="image"
        :alt="$tc('sw-extension-store.component.sw-extension-config.imageDescription', { extensionName: extensionLabel}, 0)"
    />
</template>

<template #smart-bar-header>
    {{ extensionLabel }}
</template>

<template
    v-if="extension"
    #smart-bar-header-meta
>
```

### Example 2
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-icon :src="image" />
```

### Example 3
Source: `sw-first-run-wizard/component/sw-plugin-card/sw-plugin-card.html.twig`
```twig
<sw-extension-icon
    :src="plugin.iconPath"
/>

<div class="sw-plugin-card__info">
    <div class="sw-plugin-card__label">
        {{ plugin.label }}
    </div>

    <div class="sw-plugin-card__manufacturer">
        {{ plugin.manufacturer }}
    </div>

    <div
        v-if="showDescription"
```

### Example 4
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<sw-extension-icon
    class="sw-settings-services-service-card__icon"
    :src="icon"
    :alt="`Icon for ${service.name}`"
/>

<div>
    <h4>{{ service.label }}</h4>
    <sw-status
        :color="serviceStatus"
    >
        {{ $t(statusText) }}
    </sw-status>
</div>

```
