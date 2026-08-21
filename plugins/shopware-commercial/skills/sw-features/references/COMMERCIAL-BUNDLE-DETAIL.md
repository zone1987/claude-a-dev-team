# Shopware Commercial plugin — bundle structure

## Contents

- [Plugin layout](#plugin-layout)
- [Determining bundle names](#determining-bundle-names)
- [Enabling bundles selectively](#enabling-bundles-selectively)
- [Licensing](#licensing)
- [CommercialBundle extension classes](#commercialbundle-extension-classes)
- [Per-customer feature toggles (CustomerSpecificFeatureService)](#per-customer-feature-toggles-customerspecificfeatureservice)
- [Using a plugin without the Commercial plugin (optional dependency)](#using-a-plugin-without-the-commercial-plugin-optional-dependency)
- [Merchant perspective](#merchant-perspective)

## Plugin layout

The Commercial plugin is structured as a group of nested sub-bundles.
Every function (e.g. Advanced Search, Subscriptions, B2B Components) is a self-contained bundle
inside the Commercial plugin.

```
SwagCommercial (root bundle)
├── AdvancedSearch
├── B2BComponents
├── Subscriptions
├── CustomPricing
└── ... (further sub-bundles)
```

## Determining bundle names

```bash
./bin/console debug:container --parameter kernel.bundles --format=json
```

Lists all registered bundles including all Commercial sub-bundles.

## Enabling bundles selectively

Since Shopware 6.6.10.0 an environment variable controls
which Commercial bundles are active:

```bash
# Enable only certain bundles
SHOPWARE_COMMERCIAL_ENABLED_BUNDLES=CustomPricing,Subscription
```

Bundles that are not listed get disabled, even if the Commercial plugin is installed.
Useful for deployments where only a subset of the purchased features is needed.

## Licensing

### Loading the license automatically

On installation the plugin tries to load the license key via the logged-in
Shopware account. If that fails, the plugin is installed but all
features are disabled.

### Updating the license manually

```bash
bin/console commercial:license:update
```

Loads the license key from the Shopware account again.

### Checking the license status

```bash
bin/console commercial:license:info
```

Shows:
- Current license key (set/not set)
- Expiry date of the license
- Enabled features

## CommercialBundle extension classes

Sub-bundles inherit from the base bundle class of the Commercial plugin:

```php
class CommercialB2BBundle extends CommercialBundle
{
    public function getTemplatePriority(): int
    {
        return parent::getTemplatePriority() + 1;
    }

    public function build(ContainerBuilder $container): void
    {
        parent::build($container);
        // Own DI container configuration
    }
}
```

## Per-customer feature toggles (CustomerSpecificFeatureService)

The Commercial plugin offers a system for customer-specific feature unlocks,
primarily in the context of B2B Components:

### PHP usage

```php
class MyService
{
    public function __construct(
        private readonly CustomerSpecificFeatureService $featureService
    ) {}

    public function doAction(CustomerEntity $customer, Context $context): void
    {
        if (!$this->featureService->isAllowed($customer, 'my_feature', $context)) {
            throw new AccessDeniedException();
        }
        // ...
    }
}
```

### Twig usage

```twig
{% if customerHasFeature('shopping_lists') %}
    <a href="{{ path('frontend.b2b.shopping-list.index') }}">Shopping Lists</a>
{% endif %}
```

### Available feature identifiers

| Feature key             | Component             |
|-------------------------|-----------------------|
| `employee_management`   | Employee Management   |
| `quote_management`      | Quote Management      |
| `shopping_lists`        | Shopping Lists        |
| `individual_pricing`    | Individual Pricing    |
| `order_approval`        | Order Approval        |
| `budget_management`     | Budget Management     |
| `organization`          | Organization Units    |

## Using a plugin without the Commercial plugin (optional dependency)

If your own plugin makes the Commercial plugin an optional dependency:

```php
// plugin base class
public function build(ContainerBuilder $container): void
{
    parent::build($container);

    if (!class_exists(CommercialBundle::class)) {
        return; // Commercial not installed, do nothing
    }

    // Load Commercial-specific services
    $loader = new XmlFileLoader($container, new FileLocator($this->getPath() . '/Resources/config'));
    $loader->load('services_commercial.xml');
}
```

## Merchant perspective

For Shopware merchants (plans, which features are contained in which plan):
cross-reference to the `shopware-merchant` skill.
Activation and license management: `sw-commercial-overview`.
