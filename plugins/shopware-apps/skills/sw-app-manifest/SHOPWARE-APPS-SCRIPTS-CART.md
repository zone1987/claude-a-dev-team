---
title: Cart Manipulation Scripts
impact: MEDIUM
impactDescription: Cart scripts enable discounts, surcharges, and line item manipulation
tags: scripts, cart, discount, line-item, price, manipulation
---

## Cart Manipulation Scripts

Cart scripts execute whenever the cart is calculated. Place them in `Resources/scripts/cart/`.

### Adding Products

```twig
{# Add a product by ID #}
{% do services.cart.products.add(productId) %}

{# Add with specific quantity #}
{% do services.cart.products.add(productId, 3) %}
```

### Percentage Discount

```twig
{% if services.cart.items.count > 3 %}
    {% do services.cart.discount('my-discount', 'percentage', 10, 'Bulk Discount 10%') %}
{% endif %}
```

### Absolute Discount

```twig
{% set price = services.cart.price.create({
    'default': { 'gross': 5.0, 'net': 4.20 },
    'EUR': { 'gross': 5.0, 'net': 4.20 }
}) %}

{% do services.cart.discount('abs-discount', 'absolute', price, 'Fixed €5 off') %}
```

### Surcharge

```twig
{% set surchargePrice = services.cart.price.create({
    'default': { 'gross': 3.99, 'net': 3.35 }
}) %}

{% do services.cart.surcharge('handling-fee', 'absolute', surchargePrice, 'Handling Fee') %}
```

### Idempotency (Prevent Duplicate Application)

**Incorrect (discount added every calculation):**

```twig
{% do services.cart.discount('my-discount', 'percentage', 10, 'Discount') %}
```

**Correct (check before adding):**

```twig
{% if not services.cart.has('my-discount') %}
    {% do services.cart.discount('my-discount', 'percentage', 10, 'Discount') %}
{% endif %}
```

**Alternative: Use custom cart states:**

```twig
{% if not services.cart.states.has('my-vendor-discount-applied') %}
    {% do services.cart.discount('my-discount', 'percentage', 10, 'Discount') %}
    {% do services.cart.states.add('my-vendor-discount-applied') %}
{% endif %}
```

### Configuration-Based Pricing

```twig
{% set discountPercent = services.config.app('discountPercent') %}
{% if discountPercent %}
    {% do services.cart.discount('config-discount', 'percentage', discountPercent, 'Configured Discount') %}
{% endif %}
```

### Recalculation

After adding products, call `calculate()` to update totals:

```twig
{% do services.cart.products.add(productId) %}
{% do services.cart.calculate() %}
{# Note: previous variable references to cart items are invalidated after calculate() #}
```
