# sw-settings-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | — | yes |  |
| to | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| icon | — | |
| label | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |

## Examples

### Example 1
Source: `sw-settings/page/sw-settings-index/sw-settings-index.html.twig`
```twig
<sw-settings-item
    v-for="settingsItem in settingsItems"
    :id="settingsItem.id"
    :key="settingsItem.name"
    :label="getLabel(settingsItem)"
    :to="getRouteConfig(settingsItem)"
>
    <template #icon>
        <component
            :is="settingsItem.iconComponent"
            v-if="settingsItem.iconComponent"
        />

        <mt-icon
            v-else
```
