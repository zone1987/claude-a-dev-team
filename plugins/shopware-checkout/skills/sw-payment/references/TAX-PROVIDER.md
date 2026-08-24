# Shopware 6 — tax providers

Tax rules differ by country, and in the US by state, county and even city — so most shops delegate
sales tax to a third-party service. Since **6.5.0.0** a plugin can integrate one by extending
`Shopware\Core\Checkout\Cart\TaxProvider\AbstractTaxProvider`, which is called during checkout to
supply new tax rates.

## Contents

- [The provider](#the-provider)
- [Registration](#registration)
- [Persisting it: migration](#persisting-it-migration)
- [Persisting it: repository](#persisting-it-repository)

## The provider

Extend `AbstractTaxProvider` and implement `provide`. A real integration calls a service from here —
the guide's example imports `TaxJar\Client`. Translations for the provider name live in
`TaxProviderTranslationDefinition`.

```php
// <plugin root>/src/Checkout/Cart/Tax/TaxProvider.php
public function provide(Cart $cart): TaxProviderResult
{
    $lineItemTaxes = [];

    foreach ($cart->getLineItems() as $lineItem) {
        $taxRate = 50;
        $price = $lineItem->getPrice()->getTotalPrice();
        $tax = $price * $taxRate / 100;

        // Shopware identifies the line item by uniqueIdentifier, which also works
        // inside nested line item structures
        $lineItemTaxes[$lineItem->getUniqueIdentifier()] = new CalculatedTaxCollection([
            new CalculatedTax($tax, $taxRate, $price),
        ]);
    }

    return new TaxProviderResult(
        $lineItemTaxes,
        // $deliveryTaxes,
        // $cartPriceTaxes
    );
}
```

`TaxProviderResult` takes three collections:

| Argument | Keyed by | Notes |
|---|---|---|
| `$lineItemTaxes` | the line item's `uniqueIdentifier` | works through nested line items |
| `$deliveryTaxes` | the delivery position's id | optional; iterate `$cart->getDeliveries()` and each delivery's `getPositions()` |
| `$cartPriceTaxes` | — | the tax sums for the whole cart |

**`cartPriceTaxes` is worth passing when a provider returns them.** A real tax service usually
computes the totals itself, and handing them over is what makes the checkout show its figures.
Omitted, Shopware calculates the sums itself.

## Registration

Tag the service `shopware.tax.provider`:

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(TaxProvider::class)
        ->tag('shopware.tax.provider');
};
```

## Persisting it: migration

Registering the service is not enough — the provider has to exist in the database. Either through a
migration or through the entity repository.

```php
// <plugin root>/src/Migration/MigrationTaxProvider.php
namespace SwagTaxProviders\Migration;

use Shopware\Core\Framework\Migration\MigrationStep;
use Shopware\Core\System\TaxProvider\Aggregate\TaxProviderTranslation\TaxProviderTranslationDefinition;

class MigrationTaxProvider extends MigrationStep
{
public function getCreationTimestamp(): int
{
    return 1668677456;
}

$ruleId = $connection->fetchOne(
    'SELECT `id` FROM `rule` WHERE `name` = :name',
    ['name' => 'Always valid (Default)']
);

$connection->insert(TaxProviderDefinition::ENTITY_NAME, [
    'id' => Uuid::randomBytes(),
    'identifier' => Swag\BasicExample\Checkout\Cart\Tax\TaxProvider::class,
    'active' => true,
    'priority' => 1,
    'availability_rule_id' => $ruleId,
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);
```

## Persisting it: repository

The plugin's `install` lifecycle method is a good place for it. **Create the availability rule
yourself rather than depending on one being present** — the guide is explicit that specific rules
cannot be relied on.

```php
// <plugin root>/src/BasicExample.php
$ruleRepo = $this->container->get('rule.repository');

$ruleRepo->create([[
    'name' => 'Cart > 0',
    'priority' => 0,
    'conditions' => [[
        'type' => 'cart.cartAmount',
        'operator' => '>=',
        'value' => 0,
    ]],
]], $installContext->getContext());

$criteria = new Criteria();
$criteria->addFilter(new EqualsFilter('name', 'Cart > 0'));
$ruleId = $ruleRepo->searchIds($criteria, $installContext->getContext())->firstId();

$taxRepo = $this->container->get('tax_provider.repository');
$taxRepo->create([[
    'id' => Uuid::randomHex(),
    'identifier' => Swag\BasicExample\Checkout\Cart\Tax\TaxProvider::class,
    'priority' => 1,
    'active' => false,   // switch it on from the activate lifecycle method
    'availabilityRuleId' => $ruleId,
]], $installContext->getContext());
```

Add `uninstall` to remove the providers, and `activate`/`deactivate` to switch them — the same
pattern as a payment method, except a tax provider may be deleted.

The provider then appears in the administration under **Settings > Tax**, where its active state,
priority and availability rule can be changed by hand.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/tax-provider.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/tax-provider.html),
Shopware 6.7, retrieved 2026-08-21.
