# sw-promotion-v2-wizard-description

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Examples

### Example 1
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-wizard-shipping-discount-trigger/sw-promotion-v2-wizard-shipping-discount-trigger.html.twig`
```twig
<sw-promotion-v2-wizard-description>
    {{ $tc('sw-promotion-v2.detail.shipping-discount-trigger.description') }}
</sw-promotion-v2-wizard-description>
```

### Example 2
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-rule-selection/sw-promotion-v2-settings-rule-selection.html.twig`
```twig
<sw-promotion-v2-wizard-description class="sw-promotion-v2-settings-rule-selection__description">
    {{ $tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.description') }}
</sw-promotion-v2-wizard-description>
```

### Example 3
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-wizard-discount-selection/sw-promotion-v2-wizard-discount-selection.html.twig`
```twig
<sw-promotion-v2-wizard-description>
    {{ $tc('sw-promotion-v2.detail.discount-selection.description') }}
</sw-promotion-v2-wizard-description>
```

### Example 4
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-trigger/sw-promotion-v2-settings-trigger.html.twig`
```twig
<sw-promotion-v2-wizard-description
    class="sw-promotion-v2-settings-trigger-settings__description"
>
    {{ $tc('sw-promotion-v2.detail.discounts.wizard.shipping-discount.description') }}
</sw-promotion-v2-wizard-description>
```
