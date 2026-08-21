# B2B Quote Management & Shopping Lists — Developer reference

## Quote Management

### Concept

B2B partners fill the cart → submit a quote request → the merchant reviews/adjusts it →
adjusted quote goes to the partner → the partner accepts/declines → on acceptance an order is created automatically.

### Entities

| Entity                 | Description                                              |
|------------------------|----------------------------------------------------------|
| `Quote`                | Main entity: state, prices, discount, users              |
| `QuoteLineItem`        | Line items (only the product type is supported)          |
| `QuoteDelivery`        | Delivery information (shipping method, dates)            |
| `QuoteDeliveryPosition`| Delivery positions with prices                           |
| `QuoteTransaction`     | Payment information                                      |
| `QuoteComment`         | Comments on a quote                                      |
| `QuoteEmployee`        | Linked employees                                         |
| `QuoteDocument`        | Associated documents                                     |

Key fields of Quote:
`id`, `version_id`, `state_id`, `customer_id`, `order_id`, `quote_number`,
`price` (JSON), `shipping_costs` (JSON), `discount` (JSON), `amount_total`, `amount_net`

### Conversion: cart → quote

```php
// Shopware\Commercial\B2B\QuoteManagement\Domain\CartToQuote\CartToQuoteConverter

public function convertToQuote(Cart $cart, SalesChannelContext $context, ?OrderConversionContext $orderContext = null): Quote
{
    $order = $this->orderConverter->convertToOrder($cart, $context, $orderContext);
    $quote = $order; // Quote inherits the structure of the order
    // Enrichment of the quote data and line items
    return $quote;
}
```

### Conversion: quote → cart (order)

```php
// Shopware\Commercial\B2B\QuoteManagement\Domain\QuoteToCart\QuoteToCartConverter

public function convertToCart(QuoteEntity $quote, SalesChannelContext $context): Cart
{
    $cart = new Cart(Uuid::randomHex());
    $cart->setPrice($quote->getPrice());
    $lineItems = QuoteLineItemTransformer::transformToLineItems($quote->getLineItems());
    $cart->setLineItems($lineItems);
    // Further enrichment
    return $cart;
}
```

---

## Shopping Lists

### Concept

Shopping lists for B2B customers. Products can be transferred into the cart quickly.
Prices are NOT stored — they are recalculated on every load.

### Database schema

```sql
b2b_components_shopping_list:
  id, customer_id (FK), employee_id (FK), sales_channel_id (FK),
  name, active, custom_fields

b2b_components_shopping_list_line_item:
  id, b2b_components_shopping_list_id (FK), product_id (FK), quantity
```

### Store API endpoints

```http
POST /store-api/shopping-list                   # Create a new list
POST /store-api/shopping-list/{id}/duplicate    # Duplicate a list
GET  /store-api/shopping-list/{id}              # Load a single list
GET  /store-api/shopping-lists                  # Load all lists
DELETE /store-api/shopping-lists                # Delete lists (ids: array)
GET  /store-api/shopping-list/{id}/summary      # Summary with prices
```

### Price calculation

`ShoppingListSubscriber` listens to:
- `SHOPPING_LIST_LOADED` → `adminLoadedForSpecificCustomer()`
- `SALES_CHANNEL_SHOPPING_LIST_LOADED` → `salesChannelLoaded()`
- `SALES_CHANNEL_SHOPPING_LIST_LINE_ITEM_LOADED` → `salesChannelLineItemLoaded()`

`ShoppingListPriceCalculator::calculate()` loads the products and calculates prices dynamically
per sales channel and customer context.

**Important:** in the admin all shopping lists must belong to the same customer, otherwise no price.
Deactivated products are stored in lists but are not included in the price calculation.
