# sw-settings-listing-visibility-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| config | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onPageChange` | |
| `changeVisibilityValue` | |
| `fetchSalesChannels` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `truncateFilter` | |

## Examples

### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
            <sw-settings-listing-visibility-detail
                ref="visibilityConfig"
                :config="visibilityConfig"
            />

            <template #modal-footer>
                <mt-button
                    variant="primary"
                    size="small"
                    @click="closeAdvancedVisibility"
                >
                    {{ $tc('global.default.apply') }}
                </mt-button>
            </template>
        </sw-modal>
```
