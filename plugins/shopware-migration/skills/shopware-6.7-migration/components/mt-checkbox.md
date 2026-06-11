# mt-checkbox

> Checkbox input with label, indeterminate state, and inheritance support.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| label | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |
| update:checked | — | |
| change | — | |

## Examples

### Example 1
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

### Example 2
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

### Example 3
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

### Example 4
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

### Example 5
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
