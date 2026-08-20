# sw-cms-toolbar

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| tools | — | |
| language-switch | — | |
| actions | — | |
| sidebar | — | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
<sw-cms-toolbar>
    {% block sw_cms_detail_toolbar_language_switch %}
    <template #language-switch>
        <sw-language-switch
            :disabled="isLoading || page.locked || undefined"
            :allow-edit="acl.can('cms.editor')"
            :save-changes-function="saveOnLanguageChange"
            :abort-change-function="abortOnLanguageChange"
            @on-change="onChangeLanguage"
        />
    </template>
    {% endblock %}

    {% block sw_cms_detail_toolbar_title %}
    <template #title>
```
