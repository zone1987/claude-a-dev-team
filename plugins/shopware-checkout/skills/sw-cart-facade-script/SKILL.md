---
name: sw-cart-facade-script
description: >
  Warenkorb per App-Script manipulieren in Shopware 6: Cart-Facade (services.cart) im cart-Hook, Items/Preise/Rabatte
  hinzufügen ohne PHP-Processor. Trigger: "Cart Facade", "cart script", "App Script warenkorb", "services.cart",
  "cart hook", "discount per script", "warenkorb script manipulieren". Shopware 6.7.
---

# Shopware 6 — Cart-Facade (App-Script)

Apps (und Plugins via Script) manipulieren den Warenkorb über die **Cart-Facade** im `cart`-Script-Hook — ohne eigenen
PHP-Processor.

```twig
{# Resources/scripts/cart/my-cart.twig #}
{% set products = services.cart.products.get('...') %}
{% do services.cart.discount('ff-promo', 'percentage', 10, 'FF Rabatt') %}
{% do services.cart.products.add(productId) %}
```

Facade-Services u.a. `products`, `items`, `discount`, `surcharge`, `price`, `errors`. Läuft im sandboxed Script-Kontext
(`shopware-framework` → `sw-app-script`). Für komplexe/performancekritische Logik in einem PHP-Processor (`sw-cart-processor`).
Ideal für App-basierte Promotions/Gebühren ohne eigenen App-Server.
