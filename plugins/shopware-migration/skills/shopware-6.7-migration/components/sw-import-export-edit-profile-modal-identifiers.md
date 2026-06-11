# sw-import-export-edit-profile-modal-identifiers

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeIdentifier` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `languageRepository` | |
| `currencyRepository` | |
| `customFieldSetRepository` | |
| `languageCriteria` | |
| `currencyCriteria` | |
| `customFieldSetCriteria` | |
| `identifierColumns` | |
| `identifiers` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
            <sw-import-export-edit-profile-modal-identifiers
                :profile="profile"
            />
            {% endblock %}
            {% endblock %}
        </template>

        <template v-if="active === 'fieldIndicators'">
            <p class="sw-import-export-edit-profile-modal__text">
                {{ $tc('sw-import-export.profile.csvDescriptionBlock') }}
            </p>
        </template>
    </template>
</sw-tabs>
{% endblock %}
```
