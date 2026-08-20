# sw-cms-create

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `assignToEntity` | |
| `onWizardComplete` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pageHasSections` | |
| `categoryRepository` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-create/sw-cms-create.html.twig`
```twig
<sw-cms-create-wizard
    :page="page"
    @on-section-select="onAddSection($event, 0)"
    @wizard-complete="onWizardComplete"
/>
{% endblock %}

```
