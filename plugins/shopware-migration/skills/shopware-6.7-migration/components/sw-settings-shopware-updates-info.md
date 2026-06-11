# sw-settings-shopware-updates-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| changelog | `any` | — | yes |  |
| isLoading | `any` | — | no |  |

## Examples

### Example 1
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
    <sw-settings-shopware-updates-info
        v-if="updateInfo"
        :is-loading="isLoading"
        :changelog="updateInfo.body"
    />
    <sw-settings-shopware-updates-requirements
        :is-loading="isLoading"
        :update-info="updateInfo"
        :requirements="requirements"
    />
    <sw-settings-shopware-updates-plugins
        :plugins="plugins"
        :is-loading="isLoading"
    />
</sw-card-view>
```
