# Shopware 6 — Cart Facade (App Script)

Apps (and plugins via script) manipulate the cart through the **cart facade** in the `cart` script hook — without a
PHP processor of their own.

```twig
{# Resources/scripts/cart/my-cart.twig #}
{% set products = services.cart.products.get('...') %}
{% do services.cart.discount('ff-promo', 'percentage', 10, 'FF Rabatt') %}
{% do services.cart.products.add(productId) %}
```

Facade services include `products`, `items`, `discount`, `surcharge`, `price`, `errors`. Runs in the sandboxed script
context (`shopware-framework` → `sw-app-script`). Put complex or performance-critical logic in a PHP processor (`sw-cart-processor`).
Ideal for app-based promotions/fees without an app server of your own.
