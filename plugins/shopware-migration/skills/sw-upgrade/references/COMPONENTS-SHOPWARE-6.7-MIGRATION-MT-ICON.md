# mt-icon

> SVG icon component rendering icons from the Shopware icon set.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `string` | — | yes | |
| color | `string` | — | no | |
| decorative | `boolean` | — | no | |
| size | `string` | — | no | |
| mode | `"solid" | "regular"` | — | no | |

## Examples

### Example 1
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

### Example 2
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

### Example 3
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

### Example 4
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

### Example 5
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
