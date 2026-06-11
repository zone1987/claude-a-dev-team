# mt-banner

> Notification banner for displaying info, success, warning, error, or attention messages.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `"neutral" | "info" | "attention" | "critical" | "positive" | "inherited"` | — | no | |
| title | `string` | — | no | |
| hideIcon | `boolean` | — | no | |
| closable | `boolean` | — | no | |
| bannerIndex | `string` | — | no | |
| icon | `string` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| customIcon | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

## Examples

### Example 1
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

### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<mt-banner variant="inherited">
    {{ $tc('sw-bulk-edit.product.alertInheritance.message') }}
</mt-banner>
```

### Example 3
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

### Example 4
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

### Example 5
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
