# Custom Fields

## Overview

Custom fields extend existing entities with additional data without creating new database tables. They are stored as JSON in the entity's `custom_fields` column.

## Creating Custom Field Sets (in Plugin Lifecycle)

```php
use Shopware\Core\Framework\Plugin;
use Shopware\Core\Framework\Plugin\Context\InstallContext;
use Shopware\Core\System\CustomField\CustomFieldTypes;

class FfContentPlus extends Plugin
{
    public function install(InstallContext $installContext): void
    {
        $customFieldSetRepository = $this->container->get('custom_field_set.repository');

        $customFieldSetRepository->create([
            [
                'name' => 'ff_content_plus_product',
                'config' => [
                    'label' => [
                        'en-GB' => 'Content Plus',
                        'de-DE' => 'Content Plus',
                    ],
                ],
                'customFields' => [
                    [
                        'name' => 'ff_content_plus_badge_text',
                        'type' => CustomFieldTypes::TEXT,
                        'config' => [
                            'label' => [
                                'en-GB' => 'Badge Text',
                                'de-DE' => 'Badge Text',
                            ],
                            'placeholder' => [
                                'en-GB' => 'e.g. NEW',
                                'de-DE' => 'z.B. NEU',
                            ],
                            'componentName' => 'sw-field',
                            'customFieldType' => 'text',
                            'customFieldPosition' => 1,
                        ],
                    ],
                    [
                        'name' => 'ff_content_plus_highlight',
                        'type' => CustomFieldTypes::BOOL,
                        'config' => [
                            'label' => [
                                'en-GB' => 'Highlight Product',
                                'de-DE' => 'Produkt hervorheben',
                            ],
                            'componentName' => 'sw-field',
                            'customFieldType' => 'checkbox',
                            'customFieldPosition' => 2,
                        ],
                    ],
                    [
                        'name' => 'ff_content_plus_priority',
                        'type' => CustomFieldTypes::INT,
                        'config' => [
                            'label' => [
                                'en-GB' => 'Priority',
                                'de-DE' => 'Priorität',
                            ],
                            'componentName' => 'sw-field',
                            'customFieldType' => 'number',
                            'numberType' => 'int',
                            'customFieldPosition' => 3,
                        ],
                    ],
                ],
                'relations' => [
                    [
                        'entityName' => 'product',
                    ],
                ],
            ],
        ], $installContext->getContext());
    }

    public function uninstall(UninstallContext $uninstallContext): void
    {
        if ($uninstallContext->keepUserData()) {
            return;
        }

        // Delete custom field set
        $customFieldSetRepository = $this->container->get('custom_field_set.repository');
        $criteria = new Criteria();
        $criteria->addFilter(new EqualsFilter('name', 'ff_content_plus_product'));

        $ids = $customFieldSetRepository->searchIds($criteria, $uninstallContext->getContext());
        if ($ids->getTotal() > 0) {
            $customFieldSetRepository->delete(
                array_map(fn ($id) => ['id' => $id], $ids->getIds()),
                $uninstallContext->getContext()
            );
        }
    }
}
```

## Available Custom Field Types

| Type Constant | Description |
|---------------|-------------|
| `CustomFieldTypes::TEXT` | Single-line text |
| `CustomFieldTypes::HTML` | HTML editor |
| `CustomFieldTypes::INT` | Integer |
| `CustomFieldTypes::FLOAT` | Decimal |
| `CustomFieldTypes::BOOL` | Boolean/checkbox |
| `CustomFieldTypes::DATETIME` | Date and time |
| `CustomFieldTypes::SELECT` | Single select |
| `CustomFieldTypes::JSON` | JSON data |
| `CustomFieldTypes::COLORPICKER` | Color picker |
| `CustomFieldTypes::MEDIA` | Media selection |
| `CustomFieldTypes::PRICE` | Price field |
| `CustomFieldTypes::ENTITY` | Entity select |

## Reading Custom Fields

```php
// From entity
$product = $this->productRepository->search($criteria, $context)->first();
$badgeText = $product->getCustomFields()['ff_content_plus_badge_text'] ?? null;

// From DAL with filter
$criteria = new Criteria();
$criteria->addFilter(
    new EqualsFilter('customFields.ff_content_plus_highlight', true)
);
```

## Writing Custom Fields

```php
$this->productRepository->update([
    [
        'id' => $productId,
        'customFields' => [
            'ff_content_plus_badge_text' => 'SALE',
            'ff_content_plus_highlight' => true,
        ],
    ],
], $context);
```

## Custom Fields in Twig (Storefront)

```twig
{% if page.product.customFields.ff_content_plus_badge_text %}
    <span class="badge">{{ page.product.translated.customFields.ff_content_plus_badge_text }}</span>
{% endif %}
```

## Entity Relations

Custom field sets can be linked to multiple entities:

```php
'relations' => [
    ['entityName' => 'product'],
    ['entityName' => 'category'],
    ['entityName' => 'customer'],
    ['entityName' => 'order'],
    ['entityName' => 'media'],
],
```

## Naming Convention

Custom field names: `{vendor_prefix}_{plugin_snake}_{field_name}`

Examples:
- `ff_content_plus_badge_text`
- `ff_content_plus_highlight`
- `adt_product_export_external_id`
