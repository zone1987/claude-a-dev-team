# sw-mail-header-footer-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onEdit` | |
| `getList` | |
| `getListColumns` | |
| `getSalesChannelsString` | |
| `onDuplicate` | |
| `checkCanBeDeleted` | |
| `onDelete` | |
| `getMailHeaderFooterCriteria` | |
| `onMultipleDelete` | |
| `showDeleteErrorNotification` | |
| `updateRecords` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mailHeaderFooterRepository` | |
| `skeletonItemAmount` | |
| `showListing` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-mail-template/page/sw-mail-template-index/sw-mail-template-index.html.twig`
```twig
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
{% endblock %}

```

### Example 2
Source: `sw-mail-template/view/sw-mail-template-view-header-footer/sw-mail-template-view-header-footer.html.twig`
```twig
<sw-mail-header-footer-list ref="mailHeaderFooterList" />
```
