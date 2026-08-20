# mt-text-field

> Text input field with label, placeholder, help text, prefix, suffix, and error state.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| change | — | |
| update:modelValue | — | |
| focus | — | |
| blur | — | |

## Examples

### Example 1
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

### Example 2
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

### Example 3
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

### Example 4
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

### Example 5
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
