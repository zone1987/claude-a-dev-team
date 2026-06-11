# sw-card-section

> Section divider within a sw-card with configurable appearance.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| divider | `any` | `''` | no | Valid: `top`, `right`, `bottom`, `left` |
| secondary | `any` | `false` | no |  |
| slim | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cardSectionClasses` | |

## Examples

### Example 1
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-card-section divider="bottom">
    {% block sw_customer_card_metadata_container %}
    <sw-container>
        {% block sw_customer_card_metadata %}
        <div class="sw-review-detail__metadata">
            {% block sw_customer_card_metadata_customer_name %}
            {% block sw_custsomer_card_metadata_customer_name_label %}

            <div class="sw-review-detail__metadata-review-headline">
                <div>
                    <div class="sw-review-detail__metadata-review-title">
                        {{ review.title }}
                    </div>

                    <p class="sw-review-detail__metadata-review-content">
```

### Example 2
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-card-section
    class="sw-review-detail__base-info-section"
    secondary
    slim
>
    <slot name="default">
        <sw-container
            class="sw-review-base-info"
            columns="repeat(auto-fit, minmax(250px, 1fr))"
            gap="0px 15px"
        >
            <div class="sw-review-base-info-columns">
                {% block sw_customer_base_metadata_created_at %}
                <sw-description-list>
                    {% block sw_customer_base_metadata_created_at_label %}
```

### Example 3
Source: `sw-settings-tax/component/sw-tax-rule-card/sw-tax-rule-card.html.twig`
```twig
<sw-card-section
    divider="bottom"
    secondary
    slim
>
    {% block sw_tax_rule_card_header_filter %}
    <sw-card-filter
        :placeholder="$tc('sw-settings-tax.taxRuleCard.searchBarPlaceholder')"
        @sw-card-filter-term-change="onSearchTermChange"
    >
        <template #filter>
            {% block sw_tax_rule_card_header_create_rule_button %}
            <mt-button
                v-tooltip.bottom="{
                    message: $tc('sw-privileges.tooltip.warning'),
```

### Example 4
Source: `sw-product/component/sw-product-properties/sw-product-properties.html.twig`
```twig
<sw-card-section
    secondary
    divider="bottom"
>
    <sw-container
        columns="1fr auto"
        gap="0 15px"
    >
        {% block sw_product_properties_filled_state_header_form_control %}
        <sw-simple-search-field
            v-model:value="searchTerm"
            variant="form"
            size="small"
            :placeholder="$tc('sw-product.properties.placeholderSearchAddedProperties')"
            :disabled="isPropertiesLoading || undefined"
```

### Example 5
Source: `sw-customer/component/sw-customer-default-addresses/sw-customer-default-addresses.html.twig`
```twig
<sw-card-section
    v-if="customer.defaultShippingAddress.id"
    divider="right"
>
    {% block sw_customer_default_addresses_shipping_postal %}
    <sw-address
        :address="customer.defaultShippingAddress"
        :headline="$tc('sw-customer.detailBase.titleDefaultShippingAddress')"
        :show-edit-button="customerEditMode"
        :edit-link="defaultShippingAddressLink"
        :formatting-address="formattingShippingAddress"
    />
    {% endblock %}
</sw-card-section>
```
