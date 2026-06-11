# sw-sales-channel-switch

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| abortChangeFunction | `any` | — | no |  |
| saveChangesFunction | `any` | — | no |  |
| label | `any` | `''` | no |  |
| salesChannelCriteria | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-sales-channel-id | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `checkAbort` | |
| `emitChange` | |
| `onCloseChangesModal` | |
| `onClickSaveChanges` | |
| `onClickRevertUnsavedChanges` | |
| `changeToNewSalesChannel` | |

## Examples

### Example 1
Source: `sw-settings/component/sw-system-config/sw-system-config.html.twig`
```twig
    <sw-sales-channel-switch
        :label="$tc('sw-settings.system-config.labelSalesChannelSelect')"
        @change-sales-channel-id="onSalesChannelChanged"
    />
</div>

{% block sw_system_config_content_card %}
<mt-card
    v-for="card, index in config"
    :key="index"
    position-identifier="sw-system-config-content"
    :class="`sw-system-config__card--${index}`"
    :is-loading="isLoading"
    :title="getInlineSnippet(card.title)"
>
```

### Example 2
Source: `sw-settings-seo/component/sw-seo-url-template-card/sw-seo-url-template-card.html.twig`
```twig
    <sw-sales-channel-switch
        :label="$tc('sw-seo-url-template-card.general.labelSalesChannelSelect')"
        @change-sales-channel-id="onSalesChannelChanged"
    />
</template>

{% block sw_seo_url_template_card_info_box %}
<mt-banner
    variant="info"
    :title="$tc('sw-seo-url-template-card.general.headlineInfoMessageBoxEmptyProperties')"
>
    <span>{{ $tc('sw-seo-url-template-card.general.textInfoMessageBoxEmptyProperties') }}</span>
</mt-banner>
{% endblock %}

```

### Example 3
Source: `sw-settings-seo/component/sw-seo-url/sw-seo-url.html.twig`
```twig
            <sw-sales-channel-switch
                ref="salesChannelSwitch"
                :disabled="disabled || undefined"
                :label="$tc('sw-seo-url.labelSalesChannelSelect')"
                @change-sales-channel-id="onSalesChannelChanged"
            />
        </template>
        {% endblock %}

        <div
            v-if="hasAdditionalSeoSlot"
            class="sw-seo-url__card-seo-additional"
        >
            <slot
                name="seo-additional"
```
