# sw-card-filter

> Filter card with integrated search functionality.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| placeholder | `any` | `''` | no |  |
| delay | `any` | `500` | no |  |
| initialSearchTerm | `any` | `''` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| filter | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-card-filter-term-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasFilter` | |
| `hasFilterClass` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-card-filter
    ref="itemFilter"
    :placeholder="$tc('sw-settings-search.generalTab.textPlaceholderTermsFilter')"
    @sw-card-filter-term-change="onSearchTermChange"
/>
{% endblock %}

{% block sw_settings_search_excluded_search_terms_actions %}
<div class="sw-settings-search-excluded-search-terms-group-actions">
    {% block sw_settings_search_excluded_search_terms_add_button %}
    <mt-button
        class="sw-settings-search-excluded-search-terms__insert-button"
        ghost
        size="small"
        :disabled="!acl.can('product_search_config.creator')"
```

### Example 2
Source: `sw-settings-tax/component/sw-tax-rule-card/sw-tax-rule-card.html.twig`
```twig
<sw-card-filter
    :placeholder="$tc('sw-settings-tax.taxRuleCard.searchBarPlaceholder')"
    @sw-card-filter-term-change="onSearchTermChange"
>
    <template #filter>
        {% block sw_tax_rule_card_header_create_rule_button %}
        <mt-button
            v-tooltip.bottom="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('tax.editor'),
                showOnDisabledElements: true
            }"
            class="sw-tax-rule-grid-button"
            size="small"
            :disabled="!acl.can('tax.editor') || undefined"
```

### Example 3
Source: `sw-promotion-v2/component/promotion-codes/sw-promotion-v2-individual-codes-behavior/sw-promotion-v2-individual-codes-behavior.html.twig`
```twig
<sw-card-filter
    :placeholder="$tc('sw-promotion-v2.detail.base.codes.individual.searchPlaceholder')"
    @sw-card-filter-term-change="onSearchTermChange"
>
    <template #filter>

        {% block sw_promotion_v2_individual_codes_behavior_toolbar_filter_add_codes %}
        <mt-button
            class="sw-promotion-v2-individual-codes-behavior__add-codes-action"
            ghost
            size="small"
            :disabled="!acl.can('promotion.editor')"
            variant="secondary"
            @click="onOpenAddCodesModal"
        >
```

### Example 4
Source: `sw-settings-rule/component/sw-settings-rule-add-assignment-listing/sw-settings-rule-add-assignment-listing.html.twig`
```twig
    <sw-card-filter
        :placeholder="$tc('global.sw-simple-search-field.defaultPlaceholder')"
        @sw-card-filter-term-change="doSearch"
    />
    {% endblock %}
</template>

{% block sw_settings_rule_add_assignment_listing_grid %}
<sw-data-grid
    class="sw-settings-rule-add-assignment-listing__grid"
    :is-loading="loading"
    :data-source="items"
    :columns="entityContext.addContext.gridColumns"
    :is-record-selectable="isNotAssigned"
    :show-actions="false"
```

### Example 5
Source: `sw-settings-rule/component/sw-settings-rule-category-tree/sw-settings-rule-category-tree.html.twig`
```twig
<sw-card-filter @sw-card-filter-term-change="searchTreeItems" />
```
