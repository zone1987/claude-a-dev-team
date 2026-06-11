# sw-color-badge

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'default'` | no |  |
| color | `any` | `''` | no |  |
| rounded | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `colorStyle` | |
| `variantClass` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-color-badge
        v-if="item.state === 'failed'"
        variant="error"
        rounded
    />

    <sw-color-badge
        v-else-if="item.state === 'succeeded'"
        variant="success"
        rounded
    />

    <sw-color-badge
        v-else
        rounded
```

### Example 2
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
        <sw-color-badge
            v-if="logEntity.state === 'failed'"
            class="sw-import-export-activity-result-modal__color-badge"
            variant="error"
            rounded
        />

        <sw-color-badge
            v-else-if="logEntity.state === 'succeeded'"
            class="sw-import-export-activity-result-modal__color-badge"
            variant="success"
            rounded
        />

        <sw-color-badge
```

### Example 3
Source: `sw-import-export/component/sw-import-export-activity-log-info-modal/sw-import-export-activity-log-info-modal.html.twig`
```twig
        <sw-color-badge
            v-if="logEntity.state === 'failed'"
            class="sw-import-export-activity-log-info-modal__color-badge"
            variant="error"
            rounded
        />

        <sw-color-badge
            v-else-if="logEntity.state === 'succeeded'"
            class="sw-import-export-activity-log-info-modal__color-badge"
            variant="success"
            rounded
        />

        <sw-color-badge
```

### Example 4
Source: `sw-settings-shopware-updates/view/sw-settings-shopware-updates-plugins/sw-shopware-updates-plugins.html.twig`
```twig
    <sw-color-badge
        v-if="item.statusVariant"
        :variant="item.statusVariant"
        :rounded="true"
    />
    <sw-color-badge
        v-else
        :color="item.statusColor"
        :rounded="true"
    />&nbsp;

    <template v-if="item.statusMessage === 'notCompatible'">
        {{ item.statusMessage }} {{ $t('sw-settings-shopware-updates.plugins.pluginWillBeDeactivatedHint') }}
    </template>
    <template v-else-if="item.statusMessage">
```

### Example 5
Source: `sw-settings-shopware-updates/view/sw-settings-shopware-updates-requirements/sw-shopware-updates-requirements.html.twig`
```twig
                    <sw-color-badge
                        variant="success"
                        :rounded="true"
                    />&nbsp;
                    {{ $t('sw-settings-shopware-updates.requirements.ready') }}
                </template>

                <template v-else>
                    <sw-color-badge
                        variant="error"
                        :rounded="true"
                    />&nbsp;
                    {{ $t('sw-settings-shopware-updates.requirements.notReady') }}
                </template>
            </template>
```
