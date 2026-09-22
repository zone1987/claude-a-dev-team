---
name: sw-cart-processor
description: Scaffolds a Shopware 6 cart collector and cart processor (cart calculation), including the PHP service registration.
argument-hint: <Name> [--plugin <PluginName>] [--with-collector]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-cart-processor

Creates a cart processor, optionally with a collector. Skills: `sw-cart`.

## Steps

1. Name and target plugin; with `--with-collector`, a collector as well.
2. `src/Core/Checkout/Cart/<Name>Processor.php` implementing `CartProcessorInterface::process`,
   and where asked for `<Name>Collector.php` implementing `CartDataCollectorInterface::collect`.
3. Register it in `src/Resources/config/services/cart.php` — **PHP, not XML**, explicitly
   and without autowiring:

   ```php
   $services->set(MyProcessor::class)
       ->args([service('Shopware\Core\Checkout\Cart\Price\QuantityPriceCalculator')])
       // Without autoconfigure this tag is not inferred; the processor would be
       // registered as a service nothing ever calls.
       ->tag('shopware.cart.processor', ['priority' => 5000]);
   ```

   XML service definitions are `@deprecated tag:v6.8.0`.
   → `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`

4. Work on `$toCalculate`, take prices from the calculator services, and let the collector
   load its data in one batch rather than per line item.

Validation and blockers belong in a validator instead, discounts in a promotion — both in
the `sw-cart` skill.

## Before it counts as done

`composer gate` green, unit tests for the arithmetic, and the cart behaviour proved
end-to-end. → `shopware-testing` → `sw-testing-standard`
