# sw-settings-shopware-updates-requirements

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| updateInfo | `any` | — | yes |  |
| requirements | `any` | — | yes |  |
| isLoading | `any` | — | no |  |

## Examples

### Example 1
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
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

<mt-empty-state
    v-if="!isLoading && !updateInfo.version"
    :centered="true"
    :icon="$route.meta.$module.icon"
```
