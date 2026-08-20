# mt-url-field

> URL input field with protocol prefix.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| omitUrlHash | `boolean` | — | no | |
| omitUrlSearch | `boolean` | — | no | |
| copyable | `boolean` | — | no | |
| error | `{` | — | no | |
| detail | `string` | — | yes | |
| label | `string` | — | no | |
| required | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| isInherited | `boolean` | — | no | |
| helpText | `string` | — | no | |
| disabled | `boolean` | — | no | |
| placeholder | `string` | — | no | |
| name | `string` | — | no | |
| size | `"small" | "default"` | — | no | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-remove | — | |
| inheritance-restore | — | |
| change | — | |

## Examples

### Example 1
Source: `sw-cms/elements/image-slider/config/sw-cms-el-config-image-slider.html.twig`
```twig
        <mt-url-field
            v-model="sliderItem.url"
            class="sw-cms-el-config-image-slider__settings-link-input"
            :name="sliderItem.mediaUrl"
            :placeholder="$t('sw-cms.elements.image.config.placeholder.enterUrl')"
            :label="$t('sw-cms.elements.image.config.label.linkTo')"
        />
    </sw-container>
    {% endblock %}

    {% block sw_cms_element_image_slider_config_settings_link_aria_label %}
    <mt-text-field
        v-model="sliderItem.ariaLabel"
        class="sw-cms-el-config-image-slider__settings-link-aria-label"
        :name="sliderItem.ariaLabel"
```

### Example 2
Source: `sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig`
```twig
    <mt-url-field
        v-model="currentDomain.url"
        type="text"
        omit-url-hash
        omit-url-search
        :label="$tc('sw-sales-channel.detail.labelInputUrl')"
        :error="error"
        @update:model-value="onInput"
    />
    {% endblock %}

    {% block sw_sales_channel_detail_domains_input_language %}
    <sw-single-select
        v-model:value="currentDomain.languageId"
        class="sw-sales-channel-detail-domains__domain-language-select"
```
