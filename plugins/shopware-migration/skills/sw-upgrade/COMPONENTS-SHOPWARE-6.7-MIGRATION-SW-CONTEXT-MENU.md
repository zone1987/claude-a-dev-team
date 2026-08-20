# sw-context-menu

> Context menu container with menu items and dividers.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
    <sw-context-menu-item
        :router-link="{ name: 'sw.settings.country.detail', params: { id: item.id, edit: 'edit' }}"
        :disabled="!acl.can('country.editor') && !acl.can('country.viewer') || undefined"
        class="sw-country-list__edit-action"
    >
        {{ detailPageLinkText }}
    </sw-context-menu-item>
    {% endblock %}

    {% block sw_settings_country_list_grid_columns_actions_delete %}
    <sw-context-menu-item
        class="sw-country-list__delete-action"
        variant="danger"
        :disabled="!acl.can('country.deleter') || undefined"
        @click="onDelete(item.id)"
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
        <sw-context-menu-item
            variant="danger"
            :disabled="(item.enabled || !acl.can('country.editor')) || undefined"
            @click="changeCurrencyDependentRow(item.currencyId, false)"
        >
            {{ $tc('global.default.delete') }}
        </sw-context-menu-item>
        {% endblock %}

    </template>
    {% endblock %}

</sw-data-grid>
{% endblock %}

```

### Example 3
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
            <sw-context-menu-item
                v-tooltip.top="{
                    message: $tc('sw-privileges.tooltip.warning'),
                    disabled: acl.can('country.editor'),
                    showOnDisabledElements: true
                }"
                class="sw-settings-country-state__edit-country-state-action"
                :disabled="!acl.can('country.editor') || undefined"
                @click="onClickCountryState(item)"
            >
                {{ $tc('sw-settings-country.detail.editAction') }}
            </sw-context-menu-item>
            {% endblock %}
        </template>
    </sw-one-to-many-grid>
```

### Example 4
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-context-menu-item
    :disabled="isMaxLines"
    @click="openModal"
>
    {{ $tc('sw-settings-country.general.actions.newSnippet') }}
</sw-context-menu-item>

<sw-context-menu-item
    :disabled="isMaxLines"
    @click="addNewLineAt('above')"
>
    {{ $tc('sw-settings-country.general.actions.createBefore') }}
</sw-context-menu-item>

<sw-context-menu-item
```

### Example 5
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
        <sw-context-menu-item
            variant="danger"
            :disabled="isMinLines"
            @click="onDelete"
        >
            {{ $tc('global.default.delete') }}
        </sw-context-menu-item>
    </sw-context-button>
</div>
{% endblock %}

```
