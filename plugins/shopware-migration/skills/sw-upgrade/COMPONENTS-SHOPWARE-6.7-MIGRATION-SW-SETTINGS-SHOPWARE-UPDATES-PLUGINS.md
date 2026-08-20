# sw-settings-shopware-updates-plugins

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | no |  |
| plugins | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `openMyExtensions` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `columns` | |

## Examples

### Example 1
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
    <sw-settings-shopware-updates-plugins
        :plugins="plugins"
        :is-loading="isLoading"
    />
</sw-card-view>

<mt-empty-state
    v-if="!isLoading && !updateInfo.version"
    :centered="true"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-settings-shopware-updates.general.emptyState')"
/>

<sw-modal
    v-if="updaterIsRunning"
```
