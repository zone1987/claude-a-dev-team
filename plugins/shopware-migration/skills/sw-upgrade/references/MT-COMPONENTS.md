# Meteor (mt-*) components

> **`size="default"` on every `mt-button` you write.** The component defaults to
> `size="small"` — 32 pixels against the 40 of every core control beside it. Examples below
> that are quoted from Shopware's own source keep the core's spelling; **a plugin's own
> template sets the size explicitly.**
> → `shopware-admin` → `sw-meteor` → `COMPONENTS.md`

58 components, each with its props, slots, events and examples exactly as the generator extracted them. One file per component cost 1044 unreachable references; grouped, every component stays one direct link from SKILL.md.

## Contents

- [`mt-avatar`](#mt-avatar)
- [`mt-badge`](#mt-badge)
- [`mt-banner`](#mt-banner)
- [`mt-button`](#mt-button)
- [`mt-card`](#mt-card)
- [`mt-chart`](#mt-chart)
- [`mt-checkbox`](#mt-checkbox)
- [`mt-color-badge`](#mt-color-badge)
- [`mt-colorpicker`](#mt-colorpicker)
- [`mt-context-button`](#mt-context-button)
- [`mt-context-menu-divider`](#mt-context-menu-divider)
- [`mt-context-menu-item`](#mt-context-menu-item)
- [`mt-data-table-badge-renderer`](#mt-data-table-badge-renderer)
- [`mt-data-table-number-renderer`](#mt-data-table-number-renderer)
- [`mt-data-table-price-renderer`](#mt-data-table-price-renderer)
- [`mt-data-table-text-renderer`](#mt-data-table-text-renderer)
- [`mt-data-table`](#mt-data-table)
- [`mt-datepicker`](#mt-datepicker)
- [`mt-email-field`](#mt-email-field)
- [`mt-empty-state`](#mt-empty-state)
- [`mt-entity-data-table`](#mt-entity-data-table)
- [`mt-entity-select`](#mt-entity-select)
- [`mt-help-text`](#mt-help-text)
- [`mt-icon`](#mt-icon)
- [`mt-inset`](#mt-inset)
- [`mt-link`](#mt-link)
- [`mt-loader`](#mt-loader)
- [`mt-modal-action`](#mt-modal-action)
- [`mt-modal-close`](#mt-modal-close)
- [`mt-modal-root`](#mt-modal-root)
- [`mt-modal-trigger`](#mt-modal-trigger)
- [`mt-modal`](#mt-modal)
- [`mt-number-field`](#mt-number-field)
- [`mt-pagination`](#mt-pagination)
- [`mt-password-field`](#mt-password-field)
- [`mt-popover-item-result`](#mt-popover-item-result)
- [`mt-popover-item`](#mt-popover-item)
- [`mt-popover`](#mt-popover)
- [`mt-progress-bar`](#mt-progress-bar)
- [`mt-promo-badge`](#mt-promo-badge)
- [`mt-search`](#mt-search)
- [`mt-segmented-control`](#mt-segmented-control)
- [`mt-select`](#mt-select)
- [`mt-skeleton-bar`](#mt-skeleton-bar)
- [`mt-slider`](#mt-slider)
- [`mt-snackbar`](#mt-snackbar)
- [`mt-switch`](#mt-switch)
- [`mt-tabs`](#mt-tabs)
- [`mt-text-editor`](#mt-text-editor)
- [`mt-text-field`](#mt-text-field)
- [`mt-text`](#mt-text)
- [`mt-textarea`](#mt-textarea)
- [`mt-theme-provider`](#mt-theme-provider)
- [`mt-toast-notification`](#mt-toast-notification)
- [`mt-toast`](#mt-toast)
- [`mt-tooltip`](#mt-tooltip)
- [`mt-unit-field`](#mt-unit-field)
- [`mt-url-field`](#mt-url-field)

## mt-avatar

> Avatar component displaying user initials or images.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `"2xs" | "xs" | "s" | "m" | "l"` | — | no | |
| firstName | `string` | — | no | |
| lastName | `string` | — | no | |
| imageUrl | `string` | — | no | |
| variant | `"circle" | "square"` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```vue
<mt-avatar
>
    <!-- content -->
</mt-avatar>
```

## mt-badge

> Small status badge for labeling and categorizing items.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `"neutral" | "info" | "attention" | "critical" | "positive"` | — | no | |
| icon | `string` | — | no | |
| size | `"s" | "m" | "l"` | — | no | |
| statusIndicator | `boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```vue
<mt-badge
>
    <!-- content -->
</mt-badge>
```

## mt-banner

> Notification banner for displaying info, success, warning, error, or attention messages.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `"neutral" | "info" | "attention" | "critical" | "positive" | "inherited"` | — | no | |
| title | `string` | — | no | |
| hideIcon | `boolean` | — | no | |
| closable | `boolean` | — | no | |
| bannerIndex | `string` | — | no | |
| icon | `string` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| customIcon | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<mt-banner
    v-if="isRebuildInProgress"
    class="sw-settings-search__search-index-warning-text"
    variant="attention"
>

    {% block sw_settings_search_search_index_warning_top %}
    <p class="sw-settings-search__search-index-warning-top">
        {{ $tc('sw-settings-search.generalTab.textWarningOpenTab') }}
    </p>
    {% endblock %}

    {% block sw_settings_search_search_index_warning_bottom %}
    <p>{{ $tc('sw-settings-search.generalTab.textRebuildSearchIndexDescription') }}</p>
    {% endblock %}
```

#### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<mt-banner variant="inherited">
    {{ $tc('sw-bulk-edit.product.alertInheritance.message') }}
</mt-banner>
```

#### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<mt-banner
    :title="$tc('sw-bulk-edit.product.alertRestrictedFields.title')"
    variant="attention"
>
    <span v-html="$tc('sw-bulk-edit.product.alertRestrictedFields.message')"></span>
    <ul>
        <li
            v-for="(restrictedField, index) in restrictedFields"
            :key="index"
        >
            {{ $tc(`sw-bulk-edit.product.alertRestrictedFields.${restrictedField}`) }}
        </li>
    </ul>
</mt-banner>
```

#### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
<mt-banner
    :title="$tc('sw-bulk-edit.order.alertRestrictedFields.title')"
    variant="attention"
>
    <span v-html="$tc('sw-bulk-edit.order.alertRestrictedFields.message')"></span>
    <ul>
        <li
            v-for="(restrictedField, index) in restrictedFields"
            :key="index"
        >
            {{ $tc(`sw-bulk-edit.order.alertRestrictedFields.${restrictedField}`) }}
        </li>
    </ul>
</mt-banner>
```

#### Example 5
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-confirm/sw-bulk-edit-save-modal-confirm.html.twig`
```twig
<mt-banner
    v-show="isFlowTriggered"
    class="sw-bulk-edit-save-modal-confirm__trigger-flows-alert"
>
    <p>{{ $tc('sw-bulk-edit.modal.confirm.alertTitle') }}</p>
    <span>{{ triggeredFlows.join(', ') }}</span>
</mt-banner>
```

## mt-button

> Primary interactive button component with variants, sizes, loading states, and icon slots.

- [Slots](#slots)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| is | `Component | string` | — | no | |
| disabled | `boolean` | — | no | |
| variant | `"primary" | "secondary" | "tertiary" | "critical" | actionVariant` | — | no | |
| ghost | `boolean` | — | no | |
| size | `"x-small" | "small" | "default" | "large"` | — | no | |
| square | `boolean` | — | no | |
| block | `boolean` | — | no | |
| link | `string` | — | no | |
| isLoading | `boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| iconFront | — | |
| iconBack | — | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<mt-button
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('country.creator'),
        showOnDisabledElements: true
    }"
    class="sw-settings-country-list__button-create"
    variant="primary"
    :disabled="!acl.can('country.creator') || undefined"
    size="default"
    @click="$router.push({ name: 'sw.settings.country.create' })"
>
    {{ $tc('sw-settings-country.list.buttonAddCountry') }}
</mt-button>
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<mt-button
    size="small"
    variant="secondary"
    @click="onCloseDeleteModal"
>
    {{ $tc('global.default.cancel') }}
</mt-button>
```

#### Example 3
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<mt-button
    v-tooltip.bottom="{
        message: 'ESC',
        appearance: 'light'
    }"
    :disabled="isLoading"
    variant="secondary"
    size="default"
    @click="onCancel"
>
    {{ $tc('global.default.cancel') }}
</mt-button>
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
<mt-button
    class="sw-settings-country-currency-hamburger-menu__button"
    size="x-small"
    square
    variant="secondary"
>

    {% block sw_country_currency_hamburger_menu_icon %}
    <mt-icon
        name="regular-bars-s"
        size="16px"
    />
    {% endblock %}

</mt-button>
```

#### Example 5
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-button
    class="sw-settings-country-address-handling__button-reset"
    variant="critical"
    ghost
    @click="resetMarkup"
>
    {{ $tc('sw-settings-country.detail.buttonResetMarkup') }}
</mt-button>
```

## mt-card

> Card container for grouping related content with optional title, subtitle, hero, and toolbar.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `string` | — | no | |
| subtitle | `string` | — | no | |
| isLoading | `boolean` | — | no | |
| large | `boolean` | — | no | |
| inheritance | `boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| subtitle | — | |
| avatar | — | |
| grid | — | |
| footer | — | |
| default | — | |
| toolbar | — | |
| tabs | — | |
| headerRight | — | |
| before-card | — | |
| context-actions | — | |
| after-card | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:inheritance | value: boolean | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<mt-card
    v-if="isLoading || country"
    position-identifier="sw-settings-country-list"
>
    {% block sw_settings_country_list_grid %}
    <template #grid>
        {% block sw_settings_country_list_grid_inner %}
        <sw-entity-listing
            ref="swSettingsCountryGrid"
            class="sw-settings-country-list-grid"
            :data-source="country"
            :columns="getCountryColumns()"
            :repository="countryRepository"
            :full-page="false"
            detail-route="sw.settings.country.detail"
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<mt-card
    v-if="showCustomFields"
    position-identifier="sw-settings-country-detail-custom-field-sets"
    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
    :is-loading="isLoading"
>
    <sw-custom-field-set-renderer
        :entity="country"
        :disabled="!acl.can('country.editor')"
        :sets="customFieldSets"
    />
</mt-card>
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-card
    position-identifier="sw-settings-country-address-handling-options"
    :title="$tc('sw-settings-country.detail.titleOptions')"
    :is-loading="isLoading"
>
    <sw-container class="sw-settings-country-address-handling__options-container">

        <mt-switch
            :model-value="country.forceStateInRegistration"
            class="sw-settings-country-address-handling__option-items"
            bordered
            :disabled="!acl.can('country.editor') || undefined"
            :label="$tc('sw-settings-country.detail.labelForceStateInRegistration')"
            @update:model-value="updateCountry('forceStateInRegistration', $event)"
        />
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-card
    position-identifier="sw-settings-country-address-handling-formatting"
    :title="$tc('sw-settings-country.detail.titleFormatting')"
    :is-loading="isLoading"
>
    <sw-container class="sw-settings-country-address-handling__options-container">
        <div class="sw-settings-country-address-handling__address-markup">
            <sw-multi-snippet-drag-and-drop
                v-for="(snippet, index) in addressFormat"
                :key="index"
                v-droppable="{ data: { snippet, index }, dragGroup: 'sw-multi-snippet' }"
                v-draggable="{ ...dragConf, data: { snippet, index }}"
                :value="snippet"
                :line-position="index"
                :get-label-property="getLabelProperty"
```

#### Example 5
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-card
    position-identifier="sw-settings-country-detail-general"
    :title="$tc('sw-settings-country.detail.titleCard')"
    :is-loading="isLoading"
>
    <sw-container
        columns="repeat(auto-fit, minmax(250px, 1fr))"
        gap="0px 30px"
    >

        <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks, vue/attributes-order -->
        {% block sw_settings_country_general_content_field_name %}

        <mt-text-field
            v-model="country.name"
```

## mt-chart

> Chart component for data visualization (bar, line, pie charts).

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| series | `any[]` | — | yes | |
| options | `ChartOptions` | `'() => ({'` | no | |
| type | `ApexChart["type"]` | — | no | |
| width | `string | number` | — | no | |
| height | `string | number` | — | no | |

### Examples

#### Basic Usage
```vue
<mt-chart
    series="..."
>
</mt-chart>
```

## mt-checkbox

> Checkbox input with label, indeterminate state, and inheritance support.

- [Events / Emits](#events-emits)
- [Examples](#examples)

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| label | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |
| update:checked | — | |
| change | — | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
        <mt-checkbox
            v-model:checked="item.active"
        />
        {% endblock %}
    </template>
    <template v-else>
        {% block sw_settings_country_list_columns_active_label %}
        <mt-icon
            v-if="item.active"
            name="regular-checkmark-xs"
            size="16px"
            class="is--active"
        />
        <mt-icon
            v-else
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
            <mt-checkbox
                v-model:checked="item.checked"
                :label="item.name"
                :disabled="(item.disabled || !acl.can('country.editor')) || undefined"
                @update:checked="onCheckCurrency(item.id, item.checked)"
            />
            {% endblock %}

        </div>
        {% endblock %}

    </div>
    {% endblock %}

    {% block sw_settings_country_currency_hamburger_menu_loader %}
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
        <mt-checkbox
            v-model:checked="item.searchable"
        />
        {% endblock %}
    </template>

    <template v-else>
        {% block sw_settings_search_searchable_content_general_searchable_label %}
        <sw-data-grid-column-boolean v-model:value="item.searchable" />
        {% endblock %}
    </template>
</template>
{% endblock %}

{% block sw_settings_search_searchable_content_general_tokenize %}
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
        <mt-checkbox
            v-model:checked="item.searchable"
        />
        {% endblock %}
    </template>

    <template v-else>
        {% block sw_settings_search_searchable_content_customfields_searchable_label %}
        <mt-icon
            v-if="item.searchable"
            class="is--active"
            name="regular-checkmark-xs"
            size="16px"
        />
        <mt-icon
```

#### Example 5
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
    <mt-checkbox
        v-model:checked="bulkEditData[formField.name].isChanged"
        class="sw-bulk-edit-change-field__change"
        :label="!formField.config.changeLabel ? $tc('sw-bulk-edit.general.defaultChangeLabel') : formField.config.changeLabel"
        :help-text="formField.labelHelpText"
        :disabled="!!bulkEditData[formField.name].disabled"
        @update:checked="onChangeToggle($event, formField.name)"
    />
    {% endblock %}

    {% block sw_bulk_edit_change_type_field_renderer_change_field_subtitle %}
    <span v-if="formField.config.changeSubLabel">
        {{ formField.config.changeSubLabel }}
    </span>
    {% endblock %}
```

## mt-color-badge

> Color swatch badge displaying a specific color value.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```vue
<mt-color-badge
>
    <!-- content -->
</mt-color-badge>
```

## mt-colorpicker

> Color picker with hex input, alpha channel, and visual color selection.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |

### Examples

#### Example 1
Source: `sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig`
```twig
<mt-colorpicker
    v-model="colorHexCode"
    name="sw-field--currentOption-colorHexCode"
    :disabled="!allowEdit"
    :label="$tc('sw-property.detail.labelOptionColor')"
    :z-index="1000"
/>
{% endblock %}

{% block sw_property_option_detail_media %}
<sw-upload-listener
    :upload-tag="currentOption.id"
    auto-upload
    @media-upload-finish="successfulUpload"
/>
```

#### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
<mt-colorpicker
    v-model="section.backgroundColor"
    :label="$tc('sw-cms.detail.label.backgroundColorLabel')"
    :placeholder="$tc('sw-cms.detail.label.backgroundColorField')"
/>
{% endblock %}

{% block sw_cms_section_config_background_image_field %}
<sw-media-compact-upload-v2
    :source="section && section.backgroundMedia && section.backgroundMedia.id ? section.backgroundMedia : null"
    :upload-tag="uploadTag"
    :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
    :default-folder="cmsPageState.pageEntityName"
    :allow-multi-select="false"
    @media-upload-remove-image="removeMedia"
```

#### Example 3
Source: `sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig`
```twig
<mt-colorpicker
    v-model="block.backgroundColor"
    :label="$tc('sw-cms.detail.label.backgroundColorLabel')"
    :placeholder="$tc('sw-cms.detail.label.backgroundColorField')"
/>
{% endblock %}

{% block sw_cms_block_config_background_image_field %}
<sw-media-compact-upload-v2
    :source="block && block.backgroundMedia && block.backgroundMedia.id ? block.backgroundMedia : null"
    :upload-tag="uploadTag"
    :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
    :default-folder="cmsPageState.pageEntityName"
    :allow-multi-select="false"
    @media-upload-remove-image="removeMedia"
```

#### Example 4
Source: `sw-cms/elements/vimeo-video/config/sw-cms-el-config-vimeo-video.html.twig`
```twig
        <mt-colorpicker
            v-model="element.config.color.value"
            class="sw-cms-el-config-vimeo-video__color"
            :z-index="1001"
            :alpha="false"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
{% endblock %}

{% block sw_cms_element_vimeo_video_config_player_controls %}
<div class="sw-cms-el-config-vimeo-video__player-controls">
    <sw-cms-inherit-wrapper
        field="autoplay"
```

## mt-context-button

> Button that triggers a context menu dropdown.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| menuWidth | `number` | — | no | |
| menuHorizontalAlign | `"right" | "left"` | — | no | |
| menuVerticalAlign | `"bottom" | "top"` | — | no | |
| icon | `string` | — | no | |
| disabled | `boolean` | — | no | |
| hasError | `boolean` | — | no | |
| autoClose | `boolean` | — | no | |
| title | `string` | — | no | |
| childViews | `View[]` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| button | — | |
| button-text | — | |

### Examples

#### Basic Usage
```vue
<mt-context-button
>
    <!-- content -->
</mt-context-button>
```

## mt-context-menu-divider

> Visual separator between context menu groups.

### Examples

#### Basic Usage
```vue
<mt-context-menu-divider
>
</mt-context-menu-divider>
```

## mt-context-menu-item

> Individual item in a context menu.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Examples

#### Basic Usage
```vue
<mt-context-menu-item
>
</mt-context-menu-item>
```

## mt-data-table-badge-renderer

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Examples

#### Basic Usage
```vue
<mt-data-table-badge-renderer
>
</mt-data-table-badge-renderer>
```

## mt-data-table-number-renderer

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Examples

#### Basic Usage
```vue
<mt-data-table-number-renderer
>
</mt-data-table-number-renderer>
```

## mt-data-table-price-renderer

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Examples

#### Basic Usage
```vue
<mt-data-table-price-renderer
>
</mt-data-table-price-renderer>
```

## mt-data-table-text-renderer

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Examples

#### Basic Usage
```vue
<mt-data-table-text-renderer
>
</mt-data-table-text-renderer>
```

## mt-data-table

> Advanced data table with sorting, filtering, pagination, and column configuration.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:appliedFilters | — | |
| change-show-outlines | — | |
| change-show-stripes | — | |
| change-outline-framing | — | |
| change-enable-row-numbering | — | |
| open-details | — | |
| context-select | — | |
| item-delete | — | |
| reload | — | |
| pagination-limit-change | — | |
| pagination-current-page-change | — | |
| search-value-change | — | |
| sort-change | — | |
| selection-change | — | |
| multiple-selection-change | — | |
| bulk-edit | — | |
| bulk-delete | — | |

### Examples

#### Basic Usage
```vue
<mt-data-table
>
</mt-data-table>
```

## mt-datepicker

> Date/time picker with calendar and various date format support.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | — | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-invoice/sw-bulk-edit-order-documents-generate-invoice.html.twig`
```twig
    <mt-datepicker
        v-model="generateData.documentDate"
        class="sw-bulk-edit-order-documents-generate-invoice__item"
        hide-hint
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelDatePicker')"
        :placeholder="$tc('sw-datepicker.date.placeholder')"
    />
    {% endblock %}

    {% block sw_bulk_edit_order_documents_generate_invoice_textarea %}
    <mt-textarea
        v-model="generateData.documentComment"
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelTextarea')"
        :placeholder="$tc('sw-bulk-edit.order.documents.generateInvoice.placeholderTextarea')"
    />
```

#### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-delivery-note/sw-bulk-edit-order-documents-generate-delivery-note.html.twig`
```twig
    <mt-datepicker
        v-model="generateData.custom.deliveryDate"
        class="sw-bulk-edit-order-documents-generate-invoice__item"
        hide-hint
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelDatePicker')"
        :placeholder="$tc('sw-datepicker.date.placeholder')"
    />
    <mt-datepicker
        v-model="generateData.custom.deliveryNoteDate"
        class="sw-bulk-edit-order-documents-generate-invoice__item"
        hide-hint
        :label="$tc('sw-bulk-edit.order.documents.generateDeliveryNote.labelDeliveryDatePicker')"
        :placeholder="$tc('sw-datepicker.date.placeholder')"
    />
</template>
```

#### Example 3
Source: `sw-settings-tax/component/sw-settings-tax-rule-modal/sw-settings-tax-rule-modal.html.twig`
```twig
    <mt-datepicker
        v-model="taxRule.activeFrom"
        date-type="datetime"
        :error="taxRuleActiveFromError"
        :label="$tc('sw-settings-tax.taxRuleCard.labelActiveFrom')"
        :placeholder="$tc('sw-datepicker.datetime.placeholder')"
    />
    {% endblock %}
</sw-container>
{% endblock %}

{% block sw_settings_tax_rule_modal_form_footer %}
<template #modal-footer>
    {% block sw_settings_tax_rule_modal_form_footer_cancel %}
    <mt-button
```

#### Example 4
Source: `sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig`
```twig
    <mt-datepicker
        v-model="promotion.validFrom"
        class="sw-promotion-v2-detail-base__field-valid-from"
        date-type="datetime"
        :label="$tc('sw-promotion-v2.detail.base.general.validFromLabel')"
        :placeholder="$tc('sw-promotion-v2.detail.base.general.validFromPlaceholder')"
        :disabled="!acl.can('promotion.editor')"
    />
    {% endblock %}

    {% block sw_promotion_v2_detail_base_general_valid_until %}
    <mt-datepicker
        v-model="promotion.validUntil"
        class="sw-promotion-v2-detail-base__field-valid-until"
        date-type="datetime"
```

#### Example 5
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
<mt-datepicker
    v-else-if="type === 'date'"
    class="sw-custom-entity-input-field__date"
    hide-hint
    :model-value="currentValue"
    :label="label"
    :placeholder="placeholder"
    :help-text="helpText"
    @update:model-value="onChange"
/>

<!-- ToDo NEXT-22874 - Implement email-field verification to entity_schema
<sw-email-field
    v-else-if="type === 'email'"
    class="sw-custom-entity-input-field__email"
```

## mt-email-field

> Email input field with built-in validation.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `boolean` | — | no | |
| required | `boolean` | — | no | |
| modelValue | `string` | — | no | |
| name | `string` | — | no | |
| label | `string` | — | no | |
| error | `{` | — | no | |
| detail | `string` | — | yes | |
| helpText | `string` | — | no | |
| copyable | `boolean` | — | no | |
| copyableTooltip | `boolean` | — | no | |
| placeholder | `string` | — | no | |
| small | `boolean` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| prefix | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| blur | — | |
| focus | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Examples

#### Example 1
Source: `sw-customer/component/sw-customer-base-form/sw-customer-base-form.html.twig`
```twig
<mt-email-field
    v-model="customer.email"
    name="sw-field--customer-email"
    required
    :label="$tc('sw-customer.baseForm.labelEmail')"
    :placeholder="$tc('sw-customer.baseForm.placeholderEmail')"
    :error="customerEmailError"
/>
{% endblock %}

{% block sw_customer_base_form_password_field %}
<mt-password-field
    v-model="customer.password"
    name="sw-field--customer-password"
    autocomplete="new-password"
```

#### Example 2
Source: `sw-customer/component/sw-customer-card/sw-customer-card.html.twig`
```twig
<mt-email-field
    v-else
    v-model="customer.email"
    name="sw-field--customer-email"
    validation="required"
    required
    :label="$tc('sw-customer.card.labelEmail')"
    :placeholder="$tc('sw-customer.card.placeholderEmail')"
    :error="customerEmailError"
/>
{% endblock %}
{% endblock %}

{% block sw_customer_card_password %}
<mt-password-field
```

## mt-empty-state

> Empty state display with icon, title, and description for zero-data scenarios.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| headline | `string` | — | yes | |
| description | `string` | — | yes | |
| icon | `string` | — | yes | |
| linkHref | `string` | — | no | |
| linkText | `string` | — | no | |
| linkType | `"external" | "internal"` | — | no | |
| buttonText | `string` | — | no | |
| centered | `boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| button | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| button-click | — | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
        <mt-empty-state
            v-if="showEmptyState"
            :icon="$route.meta.$module.icon"
            :headline="$tc('sw-country-state-detail.emptyTitle')"
            :description="$tc('sw-country-state-detail.emptySubline')"
        />
        {% endblock %}
    </template>
    {% block sw_settings_country_state_detail %}
    <sw-country-state-detail
        v-if="currentCountryState"
        :country-state="currentCountryState"
        @attribute-edit-save="onSaveCountryState"
        @attribute-edit-cancel="onCancelCountryState"
    />
```

#### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <mt-empty-state
            v-if="!isLoading && selectedIds.length == 0"
            :icon="$route.meta.$module.icon"
            :headline="$tc('sw-bulk-edit.product.messageEmptyTitle')"
            :description="$tc('sw-bulk-edit.product.messageEmptySubline')"
        />

        {% block sw_bulk_edit_product_save_modal %}
        <router-view
            v-slot="{ Component }"
        >
            <component
                :is="Component"
                :item-total="selectedIds.length"
                :is-loading="isLoading"
```

#### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <mt-empty-state
            v-if="selectedIds.length <= 0 && !isLoading"
            :icon="$route.meta.$module.icon"
            :headline="$tc('sw-bulk-edit.order.messageEmptyTitle')"
            :description="$tc('sw-bulk-edit.order.messageEmptySubline')"
        />
        {% endblock %}

        {% block sw_bulk_edit_order_save_modal %}
        <router-view
            v-slot="{ Component }"
        >
            <component
                :is="Component"
                :item-total="selectedIds.length"
```

#### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
        <mt-empty-state
            v-if="selectedIds.length <= 0 && !isLoading"
            icon="solid-users"
            :headline="$tc('sw-bulk-edit.customer.messageEmptyTitle')"
            :description="$tc('sw-bulk-edit.customer.messageEmptySubline')"
        />
        {% endblock %}

        {% block sw_bulk_edit_customer_save_modal %}
        <router-view
            v-slot="{ Component }"
        >
            <component
                :is="Component"
                :item-total="selectedIds.length"
```

#### Example 5
Source: `sw-settings-units/page/sw-settings-units-list/sw-settings-units.html.twig`
```twig
<mt-empty-state
    v-if="!isLoading && isEmpty"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-settings-units.empty-state.title')"
    :description="$tc('sw-settings-units.empty-state.subline')"
/>

<template #grid>
    <sw-data-grid
        v-show="isLoading || !isEmpty"
        ref="swDataGrid"
        class="sw-settings-units-grid"
        :is-loading="isLoading"
        :data-source="unitList"
        :columns="unitColumns()"
```

## mt-entity-data-table

> Data table with integrated Shopware entity data source.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `keyof EntitySchema.Entities` | — | yes | |
| repository | `typeof Repository` | — | no | |
| forceRealModal | `boolean` | — | no | |
| columns | `ColumnDefinition[]` | — | yes | |
| columnChanges | `Record<string, ColumnChanges>` | — | no | |
| title | `string` | — | no | |
| subtitle | `string` | — | no | |
| layout | `"default" | "full"` | — | no | |
| allowBulkDelete | `boolean` | — | no | |
| allowBulkEdit | `boolean` | — | no | |
| allowRowSelection | `boolean` | — | no | |
| bulkEditMoreActions | `{` | — | no | |
| id | `string` | — | yes | |
| label | `string` | — | yes | |
| onClick | `() => void` | — | yes | |
| icon | `"default" | "critical" | "active" | string` | — | no | |
| type | `"default" | "active" | "critical"` | — | no | |
| metaCopy | `string` | — | no | |
| contextualDetail | `string` | — | no | |
| disableDelete | `boolean` | — | no | |
| disableEdit | `boolean` | — | no | |
| disableSearch | `boolean` | — | no | |
| disableSettingsTable | `boolean` | — | no | |
| additionalContextButtons | `{` | — | no | |
| key | `string` | — | yes | |
| caption | `string` | — | no | |
| paginationOptions | `number[]` | — | no | |
| availableFilters | `AvailableFilter[]` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| bulk-delete | rowIds: string[] | |
| bulk-edit | rowIds: string[] | |
| open-details | — | |

### Examples

#### Basic Usage
```vue
<mt-entity-data-table
    entity="..."
    columns="..."
    id="..."
>
    <!-- content -->
</mt-entity-data-table>
```

## mt-entity-select

> Entity select dropdown with Shopware API data source.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | value: any | |

### Examples

#### Basic Usage
```vue
<mt-entity-select
>
    <!-- content -->
</mt-entity-select>
```

## mt-help-text

> Help icon with tooltip popover showing explanatory text.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `string` | — | yes | |
| width | `number` | — | no | |
| showDelay | `number` | — | no | |
| hideDelay | `number` | — | no | |
| placement | `Placement` | — | no | |

### Examples

#### Basic Usage
```vue
<mt-help-text
    text="..."
>
</mt-help-text>
```

## mt-icon

> SVG icon component rendering icons from the Shopware icon set.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `string` | — | yes | |
| color | `string` | — | no | |
| decorative | `boolean` | — | no | |
| size | `string` | — | no | |
| mode | `"solid" | "regular"` | — | no | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
        <mt-icon
            name="regular-chevron-right-xs"
            size="12px"
        /> {{ $tc('sw-settings-country.list.textHeadline') }}
        {% endblock %}

        {% block sw_settings_country_list_smart_bar_header_amount %}
        <span
            v-if="!isLoading"
            class="sw-page__smart-bar-amount"
        >
            ({{ total }})
        </span>
        {% endblock %}
    </h2>
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
        <mt-icon
            v-if="item.active"
            name="regular-checkmark-xs"
            size="16px"
            class="is--active"
        />
        <mt-icon
            v-else
            name="regular-times-s"
            size="16px"
            class="is--inactive"
        />
        {% endblock %}
    </template>
</template>
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
        <mt-icon
            name="regular-bars-s"
            size="16px"
        />
        {% endblock %}

    </mt-button>
    {% endblock %}

</template>

{% block sw_country_currency_hamburger_menu_list %}
<div class="sw-settings-country-currency-hamburger-menu__wrapper">

    {% block sw_country_currency_hamburger_menu_item %}
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
            <mt-icon
                name="regular-long-arrow-right"
                size="16px"
            />
        </a>
    </sw-container>
    {% endblock %}

</sw-container>

{% block sw_settings_country_general_content_field_tax_free_companies %}

<mt-switch
    v-model="country.companyTax.enabled"
    name="sw-field--country-companyTax-enabled"
```

#### Example 5
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
            <mt-icon
                name="regular-long-arrow-right"
                size="16px"
            />
        </a>
    </sw-container>
    {% endblock %}
</sw-container>

{% block sw_settings_country_general_content_show_currency_dependent_modal %}
<sw-settings-country-currency-dependent-modal
    v-if="showCurrencyModal"
    :currency-depends-value="currencyDependsValue"
    :country-id="countryId"
    :is-loading="isLoading"
```

## mt-inset

> Layout component providing consistent inset padding.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```vue
<mt-inset
>
    <!-- content -->
</mt-inset>
```

## mt-link

> Styled link component for navigation with external/internal variants.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| to | `string` | — | no | |
| as | `string` | — | no | |
| variant | `"primary" | "critical"` | — | no | |
| disabled | `boolean` | — | no | |
| type | `"external" | "internal"` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | event: MouseEvent | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<mt-link
    type="external"
    href="https://developer.shopware.com/docs/guides/hosting/installation-updates/extension-managment.html"
>
    {{ $tc('sw-app.component.sw-app-wrong-app-url-modal.labelLearnMoreButton') }}
</mt-link>
```

#### Example 2
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
<mt-link
    class="sw-extension-permissions-modal__detail-link"
    as="button"
    type="internal"
    @click="openDetailsModal(key)"
>
    {{ $tc('sw-extension-store.component.sw-extension-permissions-modal.textEntities') }}
</mt-link>
```

#### Example 3
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
<mt-link
    class="sw-extension-permissions-modal__detail-link"
    as="button"
    type="internal"
    @click="toggleDomainsModal(true)"
>
    {{ $tc('sw-extension-store.component.sw-extension-permissions-modal.showDomains') }}
</mt-link>
```

#### Example 4
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
<mt-link
    v-if="salesChannel.length > 0"
    class="sw-settings-listing-default-sales-channel__quick-link"
    as="button"
    type="internal"
    variant="primary"
    @click="displayAdvancedVisibility"
    @keydown.enter="displayAdvancedVisibility"
>
    {{ $tc('sw-settings-listing.index.defaultSalesChannel.linkAdvancedVisibility') }}
</mt-link>
```

#### Example 5
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
<mt-link
    as="button"
    class="sw-import-export-exporter__link"
    @click="setExportModalProfile('product_configurator_setting')"
>
    {{ $tc('sw-import-export.exporter.directExportVariantsLabel') }}
</mt-link>
```

## mt-loader

> Loading spinner indicator for async operations.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | ``${string}px`` | — | no | |

### Examples

#### Example 1
Source: `sw-sso-error/page/index/sw-sso-error-index.html.twig`
```twig
<mt-loader />
```

#### Example 2
Source: `sw-login/page/index/sw-login.html.twig`
```twig
<mt-loader v-if="isLoading" />
```

#### Example 3
Source: `sw-login/view/sw-login-recovery-recovery/sw-login-recovery-recovery.html.twig`
```twig
<mt-loader />
```

#### Example 4
Source: `sw-login/view/sw-login-login/sw-login-login.html.twig`
```twig
<mt-loader />
```

#### Example 5
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/subcomponents/sw-settings-usage-data-store-data-consent-card/sw-settings-usage-data-store-data-consent-card.html.twig`
```twig
<mt-loader v-if="isLoading" />
```

## mt-modal-action

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| as | `Component | string` | — | yes | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Examples

#### Example 1
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="primary"
    @click="savePreferences"
>
    {{ $t('sw-settings-usage-data.consent-modal.actions.save-preferences') }}
</mt-modal-action>
```

#### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="primary"
    @click="shareNothing"
>
    <template #iconFront="{ size }">
        <mt-icon
            name="solid-times"
            :size="size"
        />
    </template>
    {{ $t('sw-settings-usage-data.consent-modal.actions.share-nothing') }}
</mt-modal-action>
```

#### Example 3
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="critical"
    :is-loading="isLoading"
    @click="revokePermissions"
>
    {{ $t('sw-settings-services.revoke-permissions-modal.label-button-revoke-permissions') }}
</mt-modal-action>
```

#### Example 4
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="secondary"
    @click="showDeactivateModal = false"
>
    {{ $t('global.default.cancel') }}
</mt-modal-action>
```

#### Example 5
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-action
    as="mt-button"
    variant="critical"
    :is-loading="isLoading"
    @click="setActive(false, () => { showDeactivateModal = false })"
>
    {{ $t('sw-settings-services.general.deactivate') }}
</mt-modal-action>
```

## mt-modal-close

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| as | `Component | string` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Example 1
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-close
    as="mt-button"
    variant="secondary"
>
    {{ $t('global.default.cancel') }}
</mt-modal-close>
```

#### Example 2
Source: `sw-settings-services/component/sw-settings-services-deactivate-modal/sw-settings-services-deactivate-modal.html.twig`
```twig
<mt-modal-close
    as="mt-button"
    variant="secondary"
>
    {{ $t('global.default.cancel') }}
</mt-modal-close>
```

#### Example 3
Source: `sw-settings-services/component/sw-settings-services-grant-permissions-modal/sw-settings-services-grant-permissions-modal.html.twig`
```twig
<mt-modal-close
    as="mt-button"
    variant="secondary"
    size="small"
>
    {{ $t('global.default.cancel') }}
</mt-modal-close>
```

## mt-modal-root

> Meteor component from the `@shopware-ag/meteor-component-library` package.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isOpen | `boolean; closable?: boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
<mt-modal-root
    :is-open="isOpen"
    @change="onModalRootChange"
>
    <mt-modal
        ref="swMediaModal"
        class="sw-media-modal-v2"
        width="full"
        :title="$tc('sw-media.sw-media-modal-v2.titleModal')"
    >

        {% block sw_media_modal_v2_content %}
        <div class="sw-media-modal-v2__content">

            {% block sw_media_modal_v2_tabs %}
```

#### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-root
    :is-open="showConsentModal"
    :closable="false"
>
    <mt-modal
        width="s"
        :title="$t('sw-settings-usage-data.consent-modal.title')"
        :closable="false"
        hide-header
    >
        <template #default>
            <div class="sw-settings-usage-data-consent-modal__content">
                <img
                    class="sw-setting-usage-data-consent-modal__icon-union"
                    :src="unionPath"
```

#### Example 3
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-root>
    <mt-modal :title="$t('sw-settings-services.revoke-permissions-modal.title')">
        <div class="sw-settings-services-revoke-permissions-modal__content">
            <p>{{ $t('sw-settings-services.revoke-permissions-modal.p-1') }}</p>

            <p>{{ $t('sw-settings-services.revoke-permissions-modal.p-2') }}</p>
        </div>

        <template #footer>
            <div class="sw-settings-services-revoke-permissions-modal__footer">
                <mt-modal-close
                    as="mt-button"
                    variant="secondary"
                >
                    {{ $t('global.default.cancel') }}
```

#### Example 4
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-root
    :is-open="showDeactivateModal"
    @change="showDeactivateModal = $event"
>
    <mt-modal :title="$t('sw-settings-services.general.deactivate')">
        <div class="sw-settings-services-service-card__deactivate-modal-content">
            <p>{{ $t('sw-settings-services.service-card.deactivate-modal.warning', { serviceName: service.label }) }}</p>

            <p>{{ $t('sw-settings-services.service-card.deactivate-modal.consequences') }}</p>
        </div>

        <template #footer>
            <div class="sw-settings-services-service-card__deactivate-modal-footer">
                <mt-modal-action
                    as="mt-button"
```

#### Example 5
Source: `sw-settings-services/component/sw-settings-services-deactivate-modal/sw-settings-services-deactivate-modal.html.twig`
```twig
<mt-modal-root>
    <mt-modal :title="$t('sw-settings-services.deactivate-modal.title')">
        <div class="sw-settings-services-deactivate-modal__content">
            <p>{{ $t('sw-settings-services.deactivate-modal.p-1') }}</p>

            <p>{{ $t('sw-settings-services.deactivate-modal.p-2') }}</p>

            <mt-link
                type="external"
                as="a"
                target="_blank"
                :href="feedbackLink"
            >
                {{ $t('sw-settings-services.deactivate-modal.label-feedback-link') }}
            </mt-link>
```

## mt-modal-trigger

> Meteor component from the `@shopware-ag/meteor-component-library` package.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| as | `Component` | — | yes | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Example 1
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-trigger as="button">
    {{ $t('sw-settings-services.revoke-permissions-modal.label-button-revoke-permissions') }}
</mt-modal-trigger>
```

#### Example 2
Source: `sw-settings-services/component/sw-settings-services-deactivate-modal/sw-settings-services-deactivate-modal.html.twig`
```twig
<mt-modal-trigger as="button">
    {{ $t('sw-settings-services.general.deactivate') }}
</mt-modal-trigger>
```

## mt-modal

> Modal dialog with title, content area, actions, and close functionality.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header-left | — | |
| title-after | — | |
| header-right | — | |
| default | — | |
| footer | — | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
<mt-modal-root
    :is-open="isOpen"
    @change="onModalRootChange"
>
    <mt-modal
        ref="swMediaModal"
        class="sw-media-modal-v2"
        width="full"
        :title="$tc('sw-media.sw-media-modal-v2.titleModal')"
    >

        {% block sw_media_modal_v2_content %}
        <div class="sw-media-modal-v2__content">

            {% block sw_media_modal_v2_tabs %}
```

#### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-root
    :is-open="showConsentModal"
    :closable="false"
>
    <mt-modal
        width="s"
        :title="$t('sw-settings-usage-data.consent-modal.title')"
        :closable="false"
        hide-header
    >
        <template #default>
            <div class="sw-settings-usage-data-consent-modal__content">
                <img
                    class="sw-setting-usage-data-consent-modal__icon-union"
                    :src="unionPath"
```

#### Example 3
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
    <mt-modal-action
        as="mt-button"
        variant="primary"
        @click="savePreferences"
    >
        {{ $t('sw-settings-usage-data.consent-modal.actions.save-preferences') }}
    </mt-modal-action>
</template>
<template v-else>
    <mt-modal-action
        as="mt-button"
        variant="primary"
        @click="shareNothing"
    >
        <template #iconFront="{ size }">
```

#### Example 4
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-root>
    <mt-modal :title="$t('sw-settings-services.revoke-permissions-modal.title')">
        <div class="sw-settings-services-revoke-permissions-modal__content">
            <p>{{ $t('sw-settings-services.revoke-permissions-modal.p-1') }}</p>

            <p>{{ $t('sw-settings-services.revoke-permissions-modal.p-2') }}</p>
        </div>

        <template #footer>
            <div class="sw-settings-services-revoke-permissions-modal__footer">
                <mt-modal-close
                    as="mt-button"
                    variant="secondary"
                >
                    {{ $t('global.default.cancel') }}
```

#### Example 5
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-root
    :is-open="showDeactivateModal"
    @change="showDeactivateModal = $event"
>
    <mt-modal :title="$t('sw-settings-services.general.deactivate')">
        <div class="sw-settings-services-service-card__deactivate-modal-content">
            <p>{{ $t('sw-settings-services.service-card.deactivate-modal.warning', { serviceName: service.label }) }}</p>

            <p>{{ $t('sw-settings-services.service-card.deactivate-modal.consequences') }}</p>
        </div>

        <template #footer>
            <div class="sw-settings-services-service-card__deactivate-modal-footer">
                <mt-modal-action
                    as="mt-button"
```

## mt-number-field

> Number input with step, min/max, digits control, and increase/decrease buttons.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |
| change | — | |
| input-change | — | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-number-field
    v-model="country.position"
    name="sw-field--country-position"
    number-type="int"
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelPosition')"
    :placeholder="placeholder(country, 'position', $tc('sw-settings-country.detail.placeholderPosition'))"
/>
{% endblock %}

{% block sw_settings_country_general_content_field_iso %}

<mt-text-field
    v-model="country.iso"
    name="sw-field--country-iso"
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-number-field
    v-model="country.customerTax.amount"
    name="sw-field--country-customerTax-amount"
    class="sw-settings-country-general__input-amount customer-tax-amount"
    :min="0"
    :label="$tc('sw-settings-country.detail.taxFreeFrom')"
    :help-text="$tc('sw-settings-country.detail.taxFreeFromHelpText')"
    :disabled="!acl.can('country.editor') || undefined"
>
    <template #suffix>
        <sw-entity-single-select
            v-model:value="country.customerTax.currencyId"
            name="sw-field--country-customerTax-currencyId"
            class="sw-settings-country-general__customer-select-currency sw-settings-country-general__select"
            entity="currency"
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
    <mt-number-field
        v-model="item.amount"
        class="sw-settings-country-currency-dependent-modal__input"
        :min="0"
        :disabled="(!item.enabled || !acl.can('country.editor')) || undefined"
        @update:model-value="reCalculatorInherited(item)"
    />
</template>
{% endblock %}

{% block sw_settings_country_currency_dependent_grid_column_is_base_currency %}
<template #column-enabled="{ item }">
    <sw-radio-field
        :value="checkBox"
        :name="radioButtonName"
```

#### Example 4
Source: `sw-settings-country/component/sw-country-state-detail/sw-country-state-detail.html.twig`
```twig
    <mt-number-field
        v-model="countryState.position"
        name="sw-field--countryState-position"
        :disabled="!acl.can('country.editor') || undefined"
        :tooltip-text="$tc('sw-country-state-detail.tooltipPosition')"
        number-type="int"
        :label="$tc('sw-country-state-detail.labelPosition')"
    />
    {% endblock %}
</sw-container>

{% block sw_country_state_detail_modal_footer %}
<template #modal-footer>
    {% block sw_country_state_detail_modal_footer_cancel %}
    <mt-button
```

#### Example 5
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
        <mt-number-field
            v-model="item.ranking"
            number-type="int"
            size="small"
        />
        {% endblock %}
    </template>
</template>
{% endblock %}

{% block sw_settings_search_searchable_content_general_searchable %}
<template #column-searchable="{ item, isInlineEdit }">
    <template v-if="isInlineEdit">
        {% block sw_settings_search_searchable_content_general_searchable_editor %}
        <mt-checkbox
```

## mt-pagination

> Pagination control with page navigation and items-per-page selector.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentPage | `number` | — | yes | |
| limit | `number` | — | yes | |
| totalItems | `number` | — | yes | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-current-page | value: number | |

### Examples

#### Basic Usage
```vue
<mt-pagination
    currentPage="..."
    limit="..."
    totalItems="..."
>
</mt-pagination>
```

## mt-password-field

> Password input with show/hide toggle.

- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `string | null` | — | no | |
| placeholder | `string` | — | no | |
| disabled | `boolean` | — | no | |
| error | `{ code: number; detail: string } | null` | — | no | |
| hint | `string | null` | — | no | |
| toggable | `boolean` | — | no | |
| name | `string | undefined` | — | no | |
| required | `boolean` | — | no | |
| helpText | `string` | — | no | |
| size | `"small" | "default"` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| disableInheritanceToggle | `boolean` | — | no | |
| idSuffix | `string` | — | no | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | value: string | undefined | |
| submit | — | |
| inheritance-restore | value: unknown | |
| inheritance-remove | value: unknown | |
| update:modelValue | value: string | undefined | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-account/sw-extension-my-extensions-account.html.twig`
```twig
            <mt-password-field
                v-model="form.password"
                class="sw-extension-my-extensions-account__password-field"
                :label="$tc('sw-extension.my-extensions.account.passwordLabel')"
                :placeholder="$tc('sw-extension.my-extensions.account.passwordPlaceholder')"
                @keyup.enter="login"
            />
        </div>

        <div class="sw-extension-my-extensions-account__wrapper-content-login-footer">
            <a
                :href="$tc('sw-extension.my-extensions.account.recoveryUrl')"
                target="_blank"
                rel="noopener"
            >
```

#### Example 2
Source: `sw-integration/page/sw-integration-list/sw-integration-list.html.twig`
```twig
    <mt-password-field
        v-if="secretAccessKeyFieldTypeIsPassword"
        v-model="currentIntegration.secretAccessKey"
        name="sw-field--currentIntegration-secretAccessKey"
        :label="$tc('sw-integration.detail.secretFieldLabel')"
        :disabled="true"
        :password-toggle-able="false"
        :copyable="showSecretAccessKey"
        :copyable-tooltip="true"
    />
</template>

<mt-button
    v-if="!showSecretAccessKey"
    variant="critical"
```

#### Example 3
Source: `sw-inactivity-login/page/index/sw-inactivity-login.html.twig`
```twig
<mt-password-field
    v-model="password"
    v-autofocus
    :label="$tc('sw-login.index.labelPassword')"
    :disabled="isLoading"
    :error="passwordError"
    @keydown.enter="loginUserWithPassword"
/>

<mt-checkbox
    v-model:checked="rememberMe"
    :label="$tc('sw-login.index.labelKeepLoggedIn')"
/>

<template #modal-footer>
```

#### Example 4
Source: `sw-login/view/sw-login-recovery-recovery/sw-login-recovery-recovery.html.twig`
```twig
        <mt-password-field
            ref="swLoginRecoveryRecoveryNewPasswordField"
            v-model="newPassword"
            :label="$tc('sw-login.recovery.recovery.newPasswordField.label')"
            :error="userPasswordError"
        />
        {% endblock %}

        {% block sw_login_recovery_recovery_form_password_confirm_field %}
        <mt-password-field
            v-model="newPasswordConfirm"
            :label="$tc('sw-login.recovery.recovery.passwordConfirmField.label')"
        />
        {% endblock %}

```

#### Example 5
Source: `sw-login/view/sw-login-login/sw-login-login.html.twig`
```twig
<mt-password-field
    v-model="password"
    name="sw-field--password"
    :label="$tc('sw-login.index.labelPassword')"
    :placeholder="$tc('sw-login.index.placeholderPassword')"
    :disabled="showLoginAlert"
    required
/>
{% endblock %}

{% block sw_login_login_submit %}
<div class="sw-login__submit">
    {% block sw_login_login_submit_button %}
    <mt-button
        :disabled="password.length <= 0 || username.length <= 0 || showLoginAlert"
```

## mt-popover-item-result

> Result item within a popover search results list.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| search | — | |
| click-group-action | — | |
| click-option | — | |
| change-checkbox | — | |
| change-visibility | — | |
| change-order | — | |

### Examples

#### Basic Usage
```vue
<mt-popover-item-result
>
</mt-popover-item-result>
```

## mt-popover-item

> Menu item within a popover menu.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| extension-logo | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-checkbox | — | |
| change-switch | — | |
| change-visibility | — | |
| click-options | — | |

### Examples

#### Example 1
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
            <mt-popover-item
                v-if="!service.active"
                :label="$t('sw-settings-services.general.activate')"
                :disabled="isLoading"
                :on-label-click="() => setActive(true, toggleFloatingUi)"
            />

            <mt-popover-item
                v-if="service.active"
                :label="$t('sw-settings-services.general.deactivate')"
                :disabled="isLoading"
                :on-label-click="() => openDeactivateModal(toggleFloatingUi)"
            />

            <mt-popover-item
```

## mt-popover

> Popover overlay positioned relative to a trigger element.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| trigger | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:isOpened | — | |

### Examples

#### Example 1
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-popover
    :child-views="[{ name: 'base' }]"
>
    <template
        #trigger="{ toggleFloatingUi }"
    >
        <mt-button
            variant="secondary"
            square
            @click="toggleFloatingUi"
        >
            <mt-icon name="solid-ellipsis-h-s" />
        </mt-button>
    </template>

```

#### Example 2
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
        <mt-popover-item
            :label="$t('sw-settings-services.service-card.permissions')"
            :on-label-click="() => openPermissionsModal(toggleFloatingUi)"
        />
    </template>
</mt-popover>
```

## mt-progress-bar

> Progress bar indicator for showing completion status.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `string` | — | yes | |
| maxValue | `number` | — | yes | |
| error | `{ detail: string; code: number } | null` | — | no | |
| progressLabelType | `string` | — | no | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<mt-progress-bar
    :model-value="progressBarValue"
    :max-value="100"
>
    {{ $tc('sw-settings-search.generalTab.textRebuildingSearchIndex') }}
</mt-progress-bar>
```

#### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-summary/sw-extension-ratings-summary.html.twig`
```twig
                    <mt-progress-bar
                        :model-value="ratingGroup.count"
                        :max-value="maxProgressValue"
                    />
                    {% endblock %}
                </template>
            </div>
            {% endblock %}
        </div>
        {% endblock %}
    </div>
    {% endblock %}
</div>
{% endblock %}

```

#### Example 3
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
        <mt-progress-bar
            :model-value="progressbarValue"
            :max-value="100"
        />
        <span class="progress-title">
            <p v-if="step === 'download'">{{ $t('sw-settings-shopware-updates.infos.progress.download') }}</p>
            <p v-if="step === 'unpack'">{{ $t('sw-settings-shopware-updates.infos.progress.unpack') }}</p>
            <p v-if="step === 'deactivate'">{{ $t('sw-settings-shopware-updates.infos.progress.deactivate') }}</p>
        </span>
    </div>
</sw-modal>

<sw-modal
    v-if="updateModalShown"
    class="sw-settings-shopware-updates-check__start-update"
```

#### Example 4
Source: `sw-product/component/sw-product-clone-modal/sw-product-clone-modal.html.twig`
```twig
    <mt-progress-bar
        class="clone-variant-progress-bar"
        :max-value="cloneMaxProgress"
        :model-value="cloneProgress"
    />
    {% endblock %}

    {% block sw_product_clone_modal_progress_bar_description %}
    <div class="clone-variant-progress-bar__description">
        {{ cloneProgress }} {{ $tc('sw-product.variations.progressTypeOf') }} {{ cloneMaxProgress }} {{ $tc('sw-product.general.cloneSuffix') }}
    </div>
    {% endblock %}
</sw-modal>
{% endblock %}

```

#### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
                <mt-progress-bar
                    class="generate-variant-progress-bar"
                    :model-value="actualProgress"
                    :max-value="maxProgress"
                />

                <span class="generate-variant-progress-bar__description">
                    {{ actualProgress }} {{ $tc('sw-product.variations.progressTypeOf') }} {{ maxProgress }} {{ $tc('sw-product.variations.progressTypeVariation') }} {{ progressMessage }}
                </span>
            </div>
        </transition>
    </template>
</sw-modal>
{% endblock %}

```

## mt-promo-badge

> Promotional badge for highlighting features or status.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `"new" | "beta" | "shopware-ai"` | — | no | |
| size | `"s" | "m" | "l"` | — | no | |

### Examples

#### Basic Usage
```vue
<mt-promo-badge
>
</mt-promo-badge>
```

## mt-search

> Search input field with debounced search event.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `string` | — | no | |
| placeholder | `string` | — | no | |
| size | `"small" | "default"` | — | no | |
| disabled | `boolean` | — | no | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | value: string | |
| update:modelValue | value: string | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-mapping/sw-import-export-edit-profile-modal-mapping.html.twig`
```twig
    <mt-search
        v-model="searchTerm"
        class="sw-import-export-view-profiles__search"
        size="small"
        :disabled="!mappingsExist"
        @change="onSearch"
    />
    {% endblock %}

    {% block sw_import_export_edit_profile_modal_mapping_toolbar_add_mapping %}
    <mt-button
        v-tooltip="{
            message: $tc('sw-import-export.profile.addMappingTooltipText'),
            disabled: addMappingEnabled,
            showOnDisabledElements: true
```

#### Example 2
Source: `sw-import-export/view/sw-import-export-view-profiles/sw-import-export-view-profiles.html.twig`
```twig
    <mt-search
        v-model="searchTerm"
        class="sw-import-export-view-profiles__search"
        size="small"
        @change="onSearch"
    />
    {% endblock %}

    {% block sw_import_export_view_profile_profiles_toolbar_add_new_profile %}
    <mt-button
        v-tooltip="createTooltip"
        class="sw-import-export-view-profiles__create-action"
        ghost
        :disabled="isLoading || isNotSystemLanguage"
        size="small"
```

#### Example 3
Source: `sw-settings/page/sw-settings-index/sw-settings-index.html.twig`
```twig
    <mt-search
        v-model="searchQuery"
        class="sw-settings__content-header-search"
        :placeholder="$t('sw-settings.index.search.placeholder')"
        size="small"
    />
</div>
{% endblock %}

{# @deprecated tag:v6.8.0 - will be removed without replacement #}
<mt-banner
    v-if="!feature.isActive('v6.8.0.0') && !hideSettingRenameBanner"
    class="sw-settings__content-rename-banner"
    variant="info"
    closable
```

## mt-segmented-control

> Segmented toggle control for switching between options.

### Examples

#### Basic Usage
```vue
<mt-segmented-control
>
</mt-segmented-control>
```

## mt-select

> Dropdown select with single/multi selection, search, and custom rendering.

- [Events / Emits](#events-emits)
- [Examples](#examples)

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| prefix | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| paginate | — | |
| update:modelValue | — | |
| change | — | |
| item-add | — | |
| item-remove | — | |
| display-values-expand | — | |
| search-term-change | — | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
    <mt-select
        v-model="productSortingKey"
        class="sw-settings-search-live-search__sorting-select"
        value-property="key"
        label-property="translated.label"
        :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSorting')"
        :options="productSortings"
        :disabled="!isSearchEnable || undefined"
        @update:model-value="searchOnStorefront"
    />
</sw-container>
{% endblock %}

{% block sw_settings_search_view_live_search_results %}
<div class="sw-settings-search-live-search__search-results">
```

#### Example 2
Source: `sw-extension/component/sw-extension-my-extensions-listing-controls/sw-extension-my-extensions-listing-controls.html.twig`
```twig
    <mt-select
        v-model="selectedSortingOption"
        class="sw-extension-my-extensions-listing-controls__sorting-dropdown"
        small
        :options="sortingOptions"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 3
Source: `sw-property/component/sw-property-detail-base/sw-property-detail-base.html.twig`
```twig
<mt-select
    v-model="propertyGroup.displayType"
    name="sw-field--propertyGroup-displayType"
    validation="required"
    required
    :label="$tc('sw-property.detail.labelDisplayType')"
    :disabled="!allowEdit"
    :options="displayTypeOptions"
/>
{% endblock %}

{% block sw_property_detail_sorting_type %}
<mt-select
    v-model="propertyGroup.sortingType"
    name="sw-field--propertyGroup-sortingType"
```

#### Example 4
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
<mt-select
    v-model="section.sizingMode"
    :label="$tc('sw-cms.detail.label.sizingField')"
    :options="sizingModeOptions"
/>
{% endblock %}

{% block sw_cms_sidebar_section_config_sidebar_mobile %}
<mt-select
    v-if="section.type === 'sidebar'"
    v-model="section.mobileBehavior"
    :label="$tc('sw-cms.detail.sidebar.mobile')"
    :options="mobileBehaviorOptions"
/>
{% endblock %}
```

#### Example 5
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
        <mt-select
            v-model="section.backgroundMediaMode"
            :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
            :disabled="!section.backgroundMediaId"
            :options="backgroundMediaModeOptions"
        />
        {% endblock %}
        {% endblock %}
    </div>
    {% endblock %}
</div>
{% endblock %}

```

## mt-skeleton-bar

> Skeleton loading placeholder for content that is being loaded.

### Examples

#### Basic Usage
```vue
<mt-skeleton-bar
>
</mt-skeleton-bar>
```

## mt-slider

> Slider input for selecting a value within a range.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |

### Examples

#### Basic Usage
```vue
<mt-slider
>
</mt-slider>
```

## mt-snackbar

> Temporary notification snackbar appearing at the bottom of the screen.

### Examples

#### Basic Usage
```vue
<mt-snackbar
>
</mt-snackbar>
```

## mt-switch

> Toggle switch input with label and optional bordered appearance.

- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `boolean` | — | no | |
| label | `string` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| inheritedValue | `boolean` | — | no | |
| required | `boolean` | — | no | |
| disabled | `boolean` | — | no | |
| checked | `boolean` | — | no | |
| bordered | `boolean` | — | no | |
| helpText | `string` | — | no | |
| error | `{ detail: string }` | — | no | |
| removeTopMargin | `boolean` | — | no | |
| name | `string` | — | no | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| update:modelValue | — | |
| inheritance-remove | — | |
| inheritance-restore | — | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-switch
    :model-value="country.forceStateInRegistration"
    class="sw-settings-country-address-handling__option-items"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelForceStateInRegistration')"
    @update:model-value="updateCountry('forceStateInRegistration', $event)"
/>

<mt-switch
    :model-value="country.postalCodeRequired"
    class="sw-settings-country-address-handling__option-items"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelPostalCodeRequired')"
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
            <mt-switch
                :model-value="country.checkAdvancedPostalCodePattern"
                class="sw-settings-country-address-handling__option-items"
                :disabled="!acl.can('country.editor') || disabledAdvancedPostalCodePattern || undefined"
                :label="$tc('sw-settings-country.detail.labelCheckAdvancedPostalCodePattern')"
                :help-text="$tc('sw-settings-country.detail.helpTextAdvancedPostalCodePattern', {5: '{5}', 4: '{4}', 2: '{2}'}, 0)"
                @update:model-value="updateCountry('checkAdvancedPostalCodePattern', $event)"
            />

            <mt-text-field
                :model-value="country.advancedPostalCodePattern"
                class="sw-settings-country-address-handling__text-field"
                :class="{'is--disabled': !country.checkAdvancedPostalCodePattern}"
                :disabled="!acl.can('country.editor') || undefined"
                :placeholder="$tc('sw-settings-country.detail.placeholderAdvancedPostalCodePattern')"
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-switch
    v-model="country.active"
    name="sw-field--country-active"
    class="sw-settings-country-general__option-items"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelActive')"
/>
{% endblock %}

{% block sw_settings_country_general_content_field_shipping_available %}

<mt-switch
    v-model="country.shippingAvailable"
    name="sw-field--country-shippingAvailable"
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-switch
    v-model="country.companyTax.enabled"
    name="sw-field--country-companyTax-enabled"
    class="sw-settings-country-general__option-items switch-field-company-tax-free"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelCompanyTaxFree')"
    :help-text="$tc('sw-settings-country.detail.helpTextCompanyTaxFree')"
/>
{% endblock %}

<sw-container
    v-if="country.companyTax.enabled"
    class="sw-settings-country-general-company-tax"
>
```

#### Example 5
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-invoice/sw-bulk-edit-order-documents-generate-invoice.html.twig`
```twig
    <mt-switch
        v-model="generateData.forceDocumentCreation"
        :label="$tc('sw-bulk-edit.order.documents.forceDocumentCreation')"
        :help-text="$tc('sw-bulk-edit.order.documents.forceDocumentCreationHelpText')"
    />
    {% endblock %}

    {% block sw_bulk_edit_order_documents_generate_invoice_placeholder %}
    {% endblock %}
</div>
{% endblock %}

```

## mt-tabs

> Tab navigation with support for items array and content slot.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-item-active | — | |

### Examples

#### Basic Usage
```vue
<mt-tabs
>
</mt-tabs>
```

## mt-text-editor

> Rich text editor with formatting toolbar (bold, italic, lists, links, etc.).

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | — | |
| update:codeMode | — | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
    <mt-text-editor
        v-else
        :key="category.id + 'description-meteor'"
        v-model="category.description"
        class="sw-category-detail-base__description"
        type="textarea"
        :disabled="!acl.can('category.editor')"
        sanitize-input
        sanitize-field-name="category_translation.description"
        :label="$tc('sw-category.base.menu.descriptionLabel')"
        :placeholder="$tc('sw-category.base.menu.descriptionPlaceholder')"
    />
    {% endblock %}
</mt-card>
{% endblock %}
```

#### Example 2
Source: `sw-cms/elements/text/config/sw-cms-el-config-text.html.twig`
```twig
                <mt-text-editor
                    v-else
                    :key="isInherited + '-meteor'"
                    :disabled="isInherited"
                    :model-value="element.config.content.value"
                    :custom-buttons="customTextEditorButtons"
                    @update:model-value="onInput"
                />

                <template #preview="{ demoValue }">
                    <div class="sw-cms-el-config-text__mapping-preview">
                        <div v-html="$sanitize(demoValue)"></div>
                    </div>
                </template>
            </sw-cms-mapping-field>
```

#### Example 3
Source: `sw-cms/elements/text/component/sw-cms-el-text.html.twig`
```twig
    <mt-text-editor
        v-else
        :model-value="element.config.content.value"
        :custom-buttons="customTextEditorButtons"
        is-inline-edit
        @update:model-value="onInput"
    />
</div>
{% endblock %}

```

#### Example 4
Source: `sw-product/component/sw-product-basic-form/sw-product-basic-form.html.twig`
```twig
        <mt-text-editor
            v-else
            :key="'meteor-' + isInherited"
            :placeholder="placeholder(product, 'description', $tc('sw-product.basicForm.placeholderDescriptionLong'))"
            :error="productDescriptionError"
            :disabled="isInherited || !allowEdit"
            :model-value="currentValue"
            sanitize-input
            sanitize-field-name="product_translation.description"
            @update:model-value="updateCurrentValue"
        />
    </template>
</sw-inherit-wrapper>
{% endblock %}

```

#### Example 5
Source: `sw-manufacturer/page/sw-manufacturer-detail/sw-manufacturer-detail.html.twig`
```twig
    <mt-text-editor
        v-else
        v-model="manufacturer.description"
        :label="$tc('sw-manufacturer.detail.labelDescription')"
        :placeholder="placeholder(manufacturer, 'description', $tc('sw-manufacturer.detail.placeholderDescription'))"
        name="description"
        sanitize-input
        sanitize-field-name="product_manufacturer_translation.description"
        :error="manufacturerDescriptionError"
        :disabled="!acl.can('product_manufacturer.editor') || undefined"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```

## mt-text-field

> Text input field with label, placeholder, help text, prefix, suffix, and error state.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| change | — | |
| update:modelValue | — | |
| focus | — | |
| blur | — | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
            <mt-text-field
                :model-value="country.advancedPostalCodePattern"
                class="sw-settings-country-address-handling__text-field"
                :class="{'is--disabled': !country.checkAdvancedPostalCodePattern}"
                :disabled="!acl.can('country.editor') || undefined"
                :placeholder="$tc('sw-settings-country.detail.placeholderAdvancedPostalCodePattern')"
                @update:model-value="updateCountry('advancedPostalCodePattern', $event)"
            />
        </div>
    </sw-container>
</mt-card>
{% endblock %}

{% block sw_settings_country_address_handling_formatting %}
<mt-card
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-text-field
    v-model="country.name"
    name="sw-field--country-name"
    required
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelName')"
    :placeholder="placeholder(country, 'name', $tc('sw-settings-country.detail.placeholderName'))"
    :error="countryNameError"
/>
{% endblock %}

{% block sw_settings_country_general_content_field_position %}
<mt-number-field
    v-model="country.position"
    name="sw-field--country-position"
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
        <mt-text-field
            v-model="country.iso3"
            name="sw-field--country-iso3"
            :disabled="!acl.can('country.editor') || undefined"
            :label="$tc('sw-settings-country.detail.labelIso3')"
            :placeholder="placeholder(country, 'iso3', $tc('sw-settings-country.detail.placeholderIso3'))"
        />
        {% endblock %}
    </sw-container>
</mt-card>
{% endblock %}

{% block sw_settings_country_general_options_card %}
<mt-card
    position-identifier="sw-settings-country-general"
```

#### Example 4
Source: `sw-settings-country/component/sw-country-state-detail/sw-country-state-detail.html.twig`
```twig
    <mt-text-field
        v-model="countryState.name"
        name="sw-field--countryState-name"
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-country-state-detail.labelName')"
        :placeholder="placeholder(countryState, 'name')"
    />
    {% endblock %}

    {% block sw_country_state_detail_modal_shortcode %}

    <mt-text-field
        v-model="countryState.shortCode"
        name="sw-field--countryState-shortCode"
        :disabled="!acl.can('country.editor') || undefined"
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<mt-text-field
    v-model="salutation.salutationKey"
    name="sw-field--salutation-salutationKey"
    class="sw-settings-salutation-detail__salutation_key"
    :label="$tc('sw-settings-salutation.detail.fieldSalutationKeyLabel')"
    :placeholder="$tc('sw-settings-salutation.detail.fieldSalutationKeyPlaceholder')"
    :help-text="$tc('sw-settings-salutation.detail.fieldSalutationKeyTooltip')"
    :error="salutationSalutationKeyError"
    validation="required"
    required
    :disabled="!acl.can('salutation.editor') || undefined"
    @update:model-value="onChange"
/>
{% endblock %}

```

## mt-text

> Typography component for consistent text rendering.

- [Slots](#slots)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `"2xs" | "xs" | "s" | "m" | "l" | "xl" | "2xl" | "3xl"` | — | no | |
| weight | `"bold" | "semibold" | "medium" | "regular"` | — | no | |
| as | `string | Component` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
            <mt-text-field
                :model-value="country.advancedPostalCodePattern"
                class="sw-settings-country-address-handling__text-field"
                :class="{'is--disabled': !country.checkAdvancedPostalCodePattern}"
                :disabled="!acl.can('country.editor') || undefined"
                :placeholder="$tc('sw-settings-country.detail.placeholderAdvancedPostalCodePattern')"
                @update:model-value="updateCountry('advancedPostalCodePattern', $event)"
            />
        </div>
    </sw-container>
</mt-card>
{% endblock %}

{% block sw_settings_country_address_handling_formatting %}
<mt-card
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-text-field
    v-model="country.name"
    name="sw-field--country-name"
    required
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelName')"
    :placeholder="placeholder(country, 'name', $tc('sw-settings-country.detail.placeholderName'))"
    :error="countryNameError"
/>
{% endblock %}

{% block sw_settings_country_general_content_field_position %}
<mt-number-field
    v-model="country.position"
    name="sw-field--country-position"
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
        <mt-text-field
            v-model="country.iso3"
            name="sw-field--country-iso3"
            :disabled="!acl.can('country.editor') || undefined"
            :label="$tc('sw-settings-country.detail.labelIso3')"
            :placeholder="placeholder(country, 'iso3', $tc('sw-settings-country.detail.placeholderIso3'))"
        />
        {% endblock %}
    </sw-container>
</mt-card>
{% endblock %}

{% block sw_settings_country_general_options_card %}
<mt-card
    position-identifier="sw-settings-country-general"
```

#### Example 4
Source: `sw-settings-country/component/sw-country-state-detail/sw-country-state-detail.html.twig`
```twig
    <mt-text-field
        v-model="countryState.name"
        name="sw-field--countryState-name"
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-country-state-detail.labelName')"
        :placeholder="placeholder(countryState, 'name')"
    />
    {% endblock %}

    {% block sw_country_state_detail_modal_shortcode %}

    <mt-text-field
        v-model="countryState.shortCode"
        name="sw-field--countryState-shortCode"
        :disabled="!acl.can('country.editor') || undefined"
```

#### Example 5
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
            <mt-textarea
                v-if="activeTab === 'raw'"
                :model-value="displayString"
            />
            {% endblock %}
            {% endblock %}
        </template>

    </sw-tabs>
    {% endblock %}

    {% block sw_settings_logging_entry_info_footer %}
    <template #modal-footer>
        {% block sw_settings_logging_entry_info_close_button %}
        <mt-button
```

## mt-textarea

> Multi-line text input with label and error handling.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| required | `boolean` | — | no | |
| disabled | `boolean` | — | no | |
| name | `string` | — | no | |
| label | `string` | — | no | |
| placeholder | `string` | — | no | |
| error | `{` | — | no | |
| detail | `string` | — | yes | |
| helpText | `string` | — | no | |
| maxLength | `number` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-remove | — | |
| inheritance-restore | — | |
| change | — | |
| focus | — | |
| blur | — | |

### Examples

#### Example 1
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
            <mt-textarea
                v-if="activeTab === 'raw'"
                :model-value="displayString"
            />
            {% endblock %}
            {% endblock %}
        </template>

    </sw-tabs>
    {% endblock %}

    {% block sw_settings_logging_entry_info_footer %}
    <template #modal-footer>
        {% block sw_settings_logging_entry_info_close_button %}
        <mt-button
```

#### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-invoice/sw-bulk-edit-order-documents-generate-invoice.html.twig`
```twig
    <mt-textarea
        v-model="generateData.documentComment"
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelTextarea')"
        :placeholder="$tc('sw-bulk-edit.order.documents.generateInvoice.placeholderTextarea')"
    />
    {% endblock %}

    {% block sw_bulk_edit_order_documents_generate_invoice_toggle_skip %}

    <mt-switch
        v-model="generateData.forceDocumentCreation"
        :label="$tc('sw-bulk-edit.order.documents.forceDocumentCreation')"
        :help-text="$tc('sw-bulk-edit.order.documents.forceDocumentCreationHelpText')"
    />
    {% endblock %}
```

#### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation-inputs/sw-extension-review-creation-inputs.html.twig`
```twig
    <mt-textarea
        v-model="text"
        :label="$tc('sw-extension-store.component.sw-extension-ratings.sw-extension-review-creation-inputs.labelText')"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 4
Source: `sw-settings-product-feature-sets/page/sw-settings-product-feature-sets-detail/sw-settings-product-feature-sets-detail.html.twig`
```twig
                    <mt-textarea
                        v-model="productFeatureSet.description"
                        :label="$tc('sw-settings-product-feature-sets.detail.labelDescription')"
                        class="sw-settings-product-feature-sets-detail__description"
                        :error="productFeatureSetDescriptionError"
                        :disabled="!acl.can('product_feature_sets.editor')"
                        :placeholder="placeholder(productFeatureSet, 'description', $tc('sw-settings-product-feature-sets.detail.placeholderDescription'))"
                    />
                    {% endblock %}

                </mt-card>
                {% endblock %}

                {% block sw_settings_product_feature_set_detail_content_values_card %}
                <sw-settings-product-feature-sets-values-card
```

#### Example 5
Source: `sw-property/component/sw-property-detail-base/sw-property-detail-base.html.twig`
```twig
<mt-textarea
    v-model="propertyGroup.description"
    name="sw-field--propertyGroup-description"
    :label="$tc('sw-property.detail.labelDescription')"
    :placeholder="placeholder(propertyGroup, 'description', $tc('sw-property.detail.placeholderDescription'))"
    :disabled="!allowEdit"
/>
{% endblock %}

{% block sw_property_detail_filter_visible_container %}
<sw-container
    columns="repeat(2, 1fr)"
    gap="0px 30px"
>
    {% block sw_property_detail_base_filterable %}
```

## mt-theme-provider

> Theme provider component that wraps children with CSS custom properties.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| future | `FutureFlags` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```vue
<mt-theme-provider
>
    <!-- content -->
</mt-theme-provider>
```

## mt-toast-notification

> Individual toast notification with auto-dismiss and action support.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| remove-toast | — | |

### Examples

#### Basic Usage
```vue
<mt-toast-notification
>
</mt-toast-notification>
```

## mt-toast

> Toast notification manager for stacking multiple toast messages.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| remove-toast | — | |

### Examples

#### Basic Usage
```vue
<mt-toast
>
</mt-toast>
```

## mt-tooltip

> Tooltip overlay showing help text on hover.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| content | `string` | — | yes | |
| delayDurationInMs | `number` | — | no | |
| hideDelayDurationInMs | `number` | — | no | |
| placement | `Placement` | — | no | |
| maxWidth | `number` | — | no | |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```vue
<mt-tooltip
    content="..."
>
    <!-- content -->
</mt-tooltip>
```

## mt-unit-field

> Number input with a unit selector dropdown (e.g., px, em, %).

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| defaultUnit | `Unit` | — | yes | |
| measurementType | `"length" | "mass"` | — | no | |
| modelValue | `number | undefined` | — | no | |
| placeholder | `string` | — | no | |
| numberType | `"float" | "int"` | — | no | |
| step | `number` | — | no | |
| min | `number` | — | no | |
| max | `number` | — | no | |
| digits | `number` | — | no | |
| fillDigits | `boolean` | — | no | |
| allowEmpty | `boolean` | — | no | |
| numberAlignEnd | `boolean` | — | no | |
| label | `string` | — | no | |
| error | `object` | — | no | |
| disabled | `boolean` | — | no | |
| required | `boolean` | — | no | |
| name | `string` | — | no | |
| size | `string` | — | no | |
| helpText | `string` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| disableInheritanceToggle | `boolean` | — | no | |
| copyable | `boolean` | — | no | |
| copyableTooltip | `boolean` | — | no | |
| zIndex | `number | null` | — | no | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | value: number | undefined | |
| update:defaultUnit | value: Unit | |
| update:measurementType | value: "length" | "mass" | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-measurement-form/sw-product-measurement-form.html.twig`
```twig
        <mt-unit-field
            measurement-type="length"
            :model-value="props.currentValue"
            :default-unit="lengthUnit"
            :label="$t('sw-product.settingsForm.labelWidth')"
            :is-inheritance-field="props.isInheritField"
            :is-inherited="props.isInherited"
            :placeholder="$t('sw-product.settingsForm.placeholderWidth')"
            :min="0"
            :step="1"
            :digits="3"
            :error="productWidthError"
            :disabled="props.isInherited || !allowEdit"
            :allow-empty="true"
            @update:model-value="props.updateCurrentValue"
```

#### Example 2
Source: `sw-product/component/sw-product-measurement-form/sw-product-measurement-form.html.twig`
```twig
            <mt-unit-field
                measurement-type="length"
                :model-value="props.currentValue"
                :default-unit="lengthUnit"
                :label="$t('sw-product.settingsForm.labelHeight')"
                :is-inheritance-field="props.isInheritField"
                :is-inherited="props.isInherited"
                :placeholder="$t('sw-product.settingsForm.placeholderHeight')"
                :min="0"
                :step="1"
                :digits="3"
                :error="productHeightError"
                :disabled="props.isInherited || !allowEdit"
                :allow-empty="true"
                @update:model-value="props.updateCurrentValue"
```

## mt-url-field

> URL input field with protocol prefix.

### Props

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

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-remove | — | |
| inheritance-restore | — | |
| change | — | |

### Examples

#### Example 1
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

#### Example 2
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
