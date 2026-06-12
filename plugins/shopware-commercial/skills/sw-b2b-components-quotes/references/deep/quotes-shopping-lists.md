# B2B Quote Management & Shopping Lists — Entwickler-Referenz

## Quote Management

### Konzept

B2B-Partner fuellen den Warenkorb → stellen Angebotsanfrage → Haendler prueft/passt an →
angepasstes Angebot an Partner → Partner akzeptiert/lehnt ab → bei Akzeptanz automatische Bestellung.

### Entitaeten

| Entitaet               | Beschreibung                                             |
|------------------------|----------------------------------------------------------|
| `Quote`                | Hauptentitaet: Status, Preise, Rabatt, Benutzer          |
| `QuoteLineItem`        | Positionen (nur Produkttyp unterstuetzt)                 |
| `QuoteDelivery`        | Lieferinformationen (Versandmethode, Termine)            |
| `QuoteDeliveryPosition`| Lieferpositionen mit Preisen                             |
| `QuoteTransaction`     | Zahlungsinformationen                                    |
| `QuoteComment`         | Kommentare zu einem Angebot                              |
| `QuoteEmployee`        | Verknuepfte Mitarbeiter                                  |
| `QuoteDocument`        | Zugehoerige Dokumente                                    |

Schluessel-Felder Quote:
`id`, `version_id`, `state_id`, `customer_id`, `order_id`, `quote_number`,
`price` (JSON), `shipping_costs` (JSON), `discount` (JSON), `amount_total`, `amount_net`

### Konvertierung: Warenkorb → Angebot

```php
// Shopware\Commercial\B2B\QuoteManagement\Domain\CartToQuote\CartToQuoteConverter

public function convertToQuote(Cart $cart, SalesChannelContext $context, ?OrderConversionContext $orderContext = null): Quote
{
    $order = $this->orderConverter->convertToOrder($cart, $context, $orderContext);
    $quote = $order; // Quote erbt Struktur der Order
    // Anreicherung der Quote-Daten und Line-Items
    return $quote;
}
```

### Konvertierung: Angebot → Warenkorb (Bestellung)

```php
// Shopware\Commercial\B2B\QuoteManagement\Domain\QuoteToCart\QuoteToCartConverter

public function convertToCart(QuoteEntity $quote, SalesChannelContext $context): Cart
{
    $cart = new Cart(Uuid::randomHex());
    $cart->setPrice($quote->getPrice());
    $lineItems = QuoteLineItemTransformer::transformToLineItems($quote->getLineItems());
    $cart->setLineItems($lineItems);
    // Weitere Anreicherung
    return $cart;
}
```

---

## Shopping Lists

### Konzept

Einkaufslisten fuer B2B-Kunden. Produkte koennen schnell in den Warenkorb uebertragen werden.
Preise werden NICHT gespeichert — sie werden bei jedem Laden neu berechnet.

### Datenbankschema

```sql
b2b_components_shopping_list:
  id, customer_id (FK), employee_id (FK), sales_channel_id (FK),
  name, active, custom_fields

b2b_components_shopping_list_line_item:
  id, b2b_components_shopping_list_id (FK), product_id (FK), quantity
```

### Store API Endpoints

```http
POST /store-api/shopping-list                   # Neue Liste erstellen
POST /store-api/shopping-list/{id}/duplicate    # Liste duplizieren
GET  /store-api/shopping-list/{id}              # Einzelne Liste laden
GET  /store-api/shopping-lists                  # Alle Listen laden
DELETE /store-api/shopping-lists                # Listen loeschen (ids: array)
GET  /store-api/shopping-list/{id}/summary      # Zusammenfassung mit Preisen
```

### Preisberechnung

`ShoppingListSubscriber` hoert auf:
- `SHOPPING_LIST_LOADED` → `adminLoadedForSpecificCustomer()`
- `SALES_CHANNEL_SHOPPING_LIST_LOADED` → `salesChannelLoaded()`
- `SALES_CHANNEL_SHOPPING_LIST_LINE_ITEM_LOADED` → `salesChannelLineItemLoaded()`

`ShoppingListPriceCalculator::calculate()` laedt Produkte und berechnet Preise dynamisch
pro SalesChannel und Customer-Context.

**Wichtig:** Im Admin muessen alle Shopping-Lists denselben Kunden haben, sonst kein Preis.
Deaktivierte Produkte werden in Listen gespeichert, aber nicht in die Preisberechnung einbezogen.
