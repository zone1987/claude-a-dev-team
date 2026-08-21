# sw-mail-template-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `getListColumns` | |
| `onChangeLanguage` | |
| `onDuplicate` | |
| `updateRecords` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateRepository` | |
| `skeletonItemAmount` | |
| `showListing` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-mail-template/page/sw-mail-template-index/sw-mail-template-index.html.twig`
```twig
                <sw-mail-template-list
                    ref="mailTemplateList"
                    :search-term="term"
                />

                <sw-mail-header-footer-list
                    ref="mailHeaderFooterList"
                    :search-term="term"
                />
            </template>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
```

### Example 2
Source: `sw-mail-template/view/sw-mail-template-view-templates/sw-mail-template-view-templates.html.twig`
```twig
<sw-mail-template-list ref="mailTemplateList" />
```
