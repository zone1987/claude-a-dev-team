# sw-system-config

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| domain | `any` | — | yes |  |
| salesChannelId | `any` | `null` | no |  |
| salesChannelSwitchable | `any` | `false` | no |  |
| inherit | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| beforeElements | — | |
| card-element | — | |
| card-element-last | — | |
| afterElements | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-changed | — | |
| config-changed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getFieldError` | |
| `createdComponent` | |
| `readConfig` | |
| `readAll` | |
| `loadCurrentSalesChannelConfig` | |
| `saveAll` | |
| `createErrorNotification` | |
| `onSalesChannelChanged` | |
| `hasMapInheritanceSupport` | |
| `getElementBind` | |
| `getInheritWrapperBind` | |
| `getInheritedValue` | |
| `emitConfig` | |
| `kebabCase` | |
| `isMeteorComponent` | |
| `getMeteorElementBind` | |
| `getMeteorElementEventsHandler` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isNotDefaultSalesChannel` | |
| `typesWithMapInheritanceSupport` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```twig
        <sw-system-config
            ref="systemConfig"
            :domain="domain"
            sales-channel-switchable
            :sales-channel-id="salesChannelId"
        />
    </template>
</sw-meteor-page>
{% endblock %}

```

### Example 2
Source: `sw-settings-newsletter/page/sw-settings-newsletter/sw-settings-newsletter.html.twig`
```twig
            <sw-system-config
                ref="systemConfig"
                sales-channel-switchable
                domain="core.newsletter"
                @loading-changed="onLoadingChanged"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 3
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-system-config
    ref="systemConfig"
    sales-channel-switchable
    domain="core.listing"
    @loading-changed="onLoadingChanged"
>

    <template #afterElements="{ config, index, isNotDefaultSalesChannel, inheritance }">
        {% block sw_settings_listing_content_card_view_system_config_default_sorting_select %}
        <sw-inherit-wrapper
            v-if="config && index === 0"
            v-model:value="config['core.listing.defaultSorting']"
            :label="$tc('sw-settings-listing.general.labelDefaultSorting')"
            :has-parent="isNotDefaultSalesChannel"
            :inherited-value="inheritance['core.listing.defaultSorting']"
```

### Example 4
Source: `sw-settings-basic-information/page/sw-settings-basic-information/sw-settings-basic-information.html.twig`
```twig
            <sw-system-config
                v-show="!isLoading"
                ref="systemConfig"
                sales-channel-switchable
                domain="core.basicInformation"
                @loading-changed="onLoadingChanged"
            />
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 5
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-index/sw-settings-shopware-updates-index.html.twig`
```twig
<sw-system-config
    v-show="!isLoading"
    ref="systemConfig"
    domain="core.update"
    @loading-changed="onLoadingChanged"
>
    <template #card-element-last>
        <div class="sw-settings-shopware-updates-index__check-for-updates-btn">
            <mt-button
                ghost
                :is-loading="isSearchingForUpdates"
                variant="secondary"
                @click="searchForUpdates"
            >
                {{ $t('sw-settings-shopware-updates.general.checkForUpdates') }}
```
