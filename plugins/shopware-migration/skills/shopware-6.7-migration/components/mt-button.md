# mt-button

> Primary interactive button component with variants, sizes, loading states, and icon slots.

## Props

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

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| iconFront | — | |
| iconBack | — | |

## Examples

### Example 1
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

### Example 2
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

### Example 3
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

### Example 4
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

### Example 5
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
