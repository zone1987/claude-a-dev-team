# sw-entity-tag-select

> Tag-based multi-select for entity associations.

## Methods

| Method | Description |
|--------|-------------|
| `resetActiveItem` | |
| `search` | |
| `addItem` | |
| `createNewTag` | |
| `checkTagExists` | |
| `filterSearchGeneratedTags` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
    <sw-entity-tag-select
        v-if="category && !isLoading"
        v-model:entity-collection="category.tags"
        class="sw-category-detail-base__tags"
        :label="$tc('sw-category.base.general.labelCategoryTags')"
        :placeholder="$tc('sw-category.base.general.labelCategoryTagsPlaceholder')"
        :disabled="!acl.can('category.editor')"
    />
    {% endblock %}

    {% block sw_category_detail_information_type %}
    <div class="sw-category-detail-base__type-container">

        {% block sw_category_detail_information_type_select %}
        <sw-single-select
```

### Example 2
Source: `sw-category/view/sw-landing-page-detail-base/sw-landing-page-detail-base.html.twig`
```twig
    <sw-entity-tag-select
        v-if="landingPage && !isLoading"
        v-model:entity-collection="landingPage.tags"
        class="sw-landing-page-detail-base__tags"
        :label="$tc('sw-landing-page.base.general.labelTags')"
        :placeholder="$tc('sw-landing-page.base.general.labelTagsPlaceholder')"
        :disabled="!acl.can('landing_page.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_landing_page_detail_base_seo %}
<mt-card
    position-identifier="sw-landing-page-detail-seo"
```

### Example 3
Source: `sw-media/component/sidebar/sw-media-tag/sw-media-tag.html.twig`
```twig
            <sw-entity-tag-select
                v-model:entity-collection="media.tags"
                :disabled="disabled"
                @update:entity-collection="handleChange"
            />
        </template>
        {% endblock %}
    </sw-media-collapse>
</div>
{% endblock %}

```

### Example 4
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
    <sw-entity-tag-select
        v-if="!isLoading"
        v-model:entity-collection="shippingMethod.tags"
        :disabled="!acl.can('shipping.editor') || undefined"
        :placeholder="$tc('sw-product.categoryForm.placeholderTags')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_settings_shipping_detail_top_ruleshippingPriceStore %}
<mt-card
    position-identifier="sw-settings-shipping-detail-condition-container"
    class="sw-settings-shipping-detail__condition_container"
    :title="$tc('sw-settings-shipping.detail.topRule')"
```

### Example 5
Source: `sw-settings-rule/view/sw-settings-rule-detail-base/sw-settings-rule-detail-base.html.twig`
```twig
            <sw-entity-tag-select
                v-if="rule"
                v-model:entity-collection="rule.tags"
                name="sw-field--rule-tags"
                class="sw-settings-rule-detail__tags-field"
                :label="$tc('global.sw-tag-field.title')"
                :disabled="!acl.can('rule.editor') || undefined"
                :placeholder="$tc('sw-settings-rule.detail.placeholderTags')"
            />
            {% endblock %}
        </div>
    </template>
    <sw-loader v-else />
</mt-card>
{% endblock %}
```
