# sw-import-export-edit-profile-import-settings

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `handleCreateEntities` | |
| `handleUpdateEntities` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
    <sw-import-export-edit-profile-import-settings
        v-if="profile.type !== 'export'"
        :profile="profile"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
<sw-import-export-edit-profile-import-settings :profile="profile" />
```
