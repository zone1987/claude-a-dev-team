# Booking-Workflow (5 Phasen)

## Übersicht

```
Phase 1: Produktdetailseite laden
  → ProductDetailSubscriber fügt ffOctoProduct-Assoziation hinzu
  → Twig-Templates erkennen OCTO-Produkt und rendern Konfigurator

Phase 2: Verfügbarkeitsprüfung
  → User wählt Datum → DateSelectPlugin → POST /octo-api/availability/check
  → Server validiert, ruft API, gibt gerenderten HTML-Block zurück

Phase 3: In den Warenkorb
  → POST /checkout/line-item/add (Priority 100!)
  → CartController lädt Session-Daten, erstellt Reservierung via API
  → Line-Item mit reservationUuid im Payload

Phase 4: Preisberechnung im Cart
  → OctoCartCollector::process() bei jeder Cart-Neuberechnung
  → Liest Units aus Session, berechnet Preis: Σ(unit.price.retail × quantity)
  → Überschreibt Shopware-Preisberechnung komplett

Phase 5: Bestätigung nach Zahlung
  → OrderSubscriber auf state_machine.order_transaction.state_changed → paid
  → CheckoutService::confirmOrder() → POST /bookings/{uuid}/confirm pro Line-Item
```

---

## Phase 1: Produktdetailseite

### ProductDetailSubscriber

**Datei:** `src/Subscriber/ProductDetailSubscriber.php`
**Event:** `ProductPageCriteriaEvent`

```php
public function onProductPageCriteria(ProductPageCriteriaEvent $event): void
{
    $event->getCriteria()
        ->addAssociation('ffOctoProduct')
        ->addAssociation('options.group.options');
}
```

### Template-Erkennung

```twig
{# buy-widget.html.twig #}
{% set octoProduct = product.getExtension('ffOctoProduct') %}
{% set isOctoProduct = product.extensions.foreignKeys.ffOctoProductId != null %}
```

Wenn `isOctoProduct`: Standard-Preis, Tax und Buy-Form werden ausgeblendet, stattdessen `configurator.html.twig` eingebunden.

### FfBuyBoxPlugin-Initialisierung

```twig
{# configurator.html.twig #}
<div data-ff-buy-box='{{ {
    apiProduct: { identifier: ..., uuid: ..., product: ... },
    product: { id: ..., ... },
    selector: { wrapper: ".product-detail-configurator-details-wrapper" },
    routes: {
        checkAvailability: path("frontend.octo-api.availability.check"),
        getItem: path("frontend.octo-api.session.get-item"),
        setItem: path("frontend.octo-api.session.set"),
        removeItem: path("frontend.octo-api.session.remove-item")
    }
}|json_encode }}'>
```

### Default-Variante

Die erste Option eines API-Produkts mit `default: true` erzeugt eine "unsichtbare" Default-Variante (CSS-Klasse `is-default-variant` → `visually-hidden`).

---

## Phase 2: Verfügbarkeitsprüfung

### Frontend-Flow

1. User wählt Datum in `DateSelectPlugin` (Flatpickr)
2. DateSelectPlugin emittiert `octo-date-changed` Event
3. `FfBuyBoxPlugin._onDateChanged()` wird aufgerufen
4. `FfBuyBoxPlugin._loadAvailability()` sendet POST

### API-Request

```
POST /octo-api/availability/check
{
    "identifier": "goldentours",
    "productId": "shopware-product-id",
    "productUuid": "api-product-uuid",
    "product": { ... },          // API-Produktdaten
    "localDateStart": "2025-03-15T00:00:00.000Z",
    "localDateEnd": "2025-03-15T23:59:59.000Z",
    "units": [{"id": "unit-uuid", "quantity": 2}]
}
```

### AvailbilityController::checkAvailability()

**Datei:** `src/Controller/AvailbilityController.php`
**Route:** `POST /octo-api/availability/check` (StorefrontRouteScope, XmlHttpRequest)

1. **Validierung** via `AvailabilityCheckConstraintCollection`
2. **Session laden:** `octo-product-session-{productId}` für gespeicherte Units
3. **Units mergen:** Request-Units mit Session-Units zusammenführen
4. **OptionId bestimmen:** Aus Session oder API-Produkt (erste Option)
5. **API-Aufruf:**
   - Online: `client->getAvailability(productId, optionId, startDate, endDate, units)`
   - Offline (RheinKurier): Fake-Availability aus `pricingFrom` generieren
   - GoCity: `Y-m-d` Datumsformat verwenden
6. **Preise konvertieren:** retail-Preis → EUR Umrechnung
7. **Session schreiben:** Beide Session-Keys aktualisieren
8. **HTML rendern:** `octo-configurator.html.twig` mit Availability-Daten
9. **Response:** HTML-String (wird via `ElementReplaceHelper` im DOM ersetzt)

### Session-Keys (werden in Phase 2 geschrieben)

**Key 1:** `octo-product-session-{shopwareProductId}`
```json
{
    "optionId": "api-option-uuid",
    "units": [
        {"id": "unit-id", "type": "ADULT", "quantity": 2, "price": {"retail": 2500}},
        {"id": "unit-id", "type": "CHILD", "quantity": 1, "price": {"retail": 1500}}
    ],
    "localDateStart": "2025-03-15T00:00:00.000Z"
}
```

**Key 2:** `{uniqueLineItemId}` (deterministische UUID)
```json
{
    "units": [...],           // Wie oben, plus restrictions, accompaniedBy
    "availability": {
        "id": "availability-uuid",  // Für Reservierung!
        "status": "AVAILABLE",
        "capacity": 50
    },
    "localTimeStart": "09:00"
}
```

### Availability-Kalender

```
POST /octo-api/availability/calendar
{
    "identifier": "goldentours",
    "productId": "api-product-id",
    "optionId": "api-option-id",
    "date": "2025-03-01T00:00:00.000Z",
    "units": [{"id": "unit-id", "quantity": 1}]
}
```

Wird von `DateSelectPlugin._loadCalendarAvailability()` beim Monatswechsel aufgerufen. Deaktiviert Tage wo `statusCode !== 'AVAILABLE'`.

---

## Phase 3: In den Warenkorb

### CartController::addLineItems()

**Datei:** `src/Controller/CartController.php`
**Route:** `POST /checkout/line-item/add` (StorefrontRouteScope, **Priority 100** — überschreibt Shopware!)

#### Ablauf:

1. **Produkte laden** mit Assoziationen: parent, ffOctoProduct, media, properties, tax
2. **Für jedes Line-Item:**
   - Prüfe ob OCTO-Produkt (`ffOctoProductId` vorhanden)
   - Wenn nicht: normales Shopware-Produkt → Standard-Handling

3. **Session-Daten lesen:**
   ```php
   $productSessionKey = 'octo-product-session-' . $referencedId;
   $sessionItem = $this->getSessionItem($session, $productSessionKey);
   // Enthält: optionId, units, localDateStart
   ```

4. **Unique Line-Item ID berechnen:**
   ```php
   $uniqueLineItemId = $this->getUniqueLineItemId($referencedId, $currentSessionItem['units']);
   // = Uuid::fromStringToHex($referencedId . implode('__', array_map(fn($u) => "{$u['id']}_q{$u['quantity']}", $units)))
   ```

5. **Zweite Session lesen** (mit uniqueLineItemId als Key):
   ```php
   $octoSessionItem = $this->getSessionItem($session, $uniqueLineItemId);
   // Enthält: units, availability (mit ID!), localTimeStart
   ```

6. **Reservierung erstellen** (wenn availability vorhanden und Client online):
   ```php
   $reservation = $this->bookingService->bookingReservation(
       identifier: $identifier,
       uuid: Uuid::v4()->toRfc4122(),
       expirationMinutes: (int) $this->getBookingReservationTime($context),
       productId: $octoProduct->getProduct()['id'],
       optionId: $sessionItem['optionId'],
       availabilityId: $octoSessionItem['availability']['id'],
       unitItems: $this->getReservationUnits($octoSessionItem)
   );
   ```

7. **Line-Item-Payload setzen:**
   ```php
   $lineItem->setPayloadValue('isOctoProduct', true);
   $lineItem->setPayloadValue('reservationUuid', $reservation['uuid'] ?? null);
   $lineItem->setPayloadValue('reservation', $reservation);
   $lineItem->setPayloadValue('taxRate', $product->getTax()->getTaxRate());
   $lineItem->setPayloadValue('visitingDate', $sessionItem['localDateStart']);
   $lineItem->setPayloadValue('units', $octoSessionItem['units']);
   $lineItem->setPayloadValue('identifier', $identifier);
   ```

8. **Line-Item in Cart** mit `$uniqueLineItemId` als ID

### getReservationUnits()

```php
private function getReservationUnits(array $currentSessionItem): array
// Konvertiert Session-Units zu Booking-UnitItems:
// Für jede Unit mit quantity > 0: erstelle {unitId, quantity}-Einträge
// Dabei wird jede Unit einzeln aufgelistet (1 Eintrag pro unitId pro Quantity)
```

---

## Phase 4: Preisberechnung im Cart

### OctoCartCollector::process()

**Datei:** `src/Core/Checkout/Cart/OctoCartCollector.php`
**Tags:** `shopware.cart.processor` + `shopware.cart.collector` (Priority **6000**)

Wird bei **jeder** Cart-Neuberechnung aufgerufen.

```php
public function process(
    CartDataCollection $data,
    Cart $original,
    Cart $toCalculate,
    SalesChannelContext $context,
    CartBehavior $behavior
): void
```

#### Ablauf:

1. **Filtere** Product-Typ Line-Items
2. **Für jedes Item mit** `isOctoProduct === true`:
   - Label anpassen (bei Default-Variante: Parent-Name verwenden)
   - Session-Daten laden mit `uniqueLineItemId`
   - **Preis berechnen:**
     ```php
     $price = 0;
     foreach ($units as $unit) {
         $price += $unit['price']['retail'] * $unit['quantity'];
     }
     ```
   - `QuantityPriceDefinition` erstellen mit Tax-Rate aus Payload
   - `CalculatedPrice` setzen → **überschreibt Shopware-Preisberechnung komplett**

### Unique Line-Item ID (identisch in 3 Klassen!)

Die gleiche Berechnung existiert in:
- `AvailbilityController`
- `CartController`
- `OctoCartCollector`

```php
private function getUniqueLineItemId(string $referenceId, array $units): string
{
    $unitString = implode('__', array_map(
        fn ($unit) => $unit['id'] . '_q' . $unit['quantity'],
        $units
    ));
    return Uuid::fromStringToHex($referenceId . $unitString);
}
```

**KRITISCH:** Die Reihenfolge der Units muss beim Schreiben und Lesen identisch sein!

---

## Phase 5: Bestätigung nach Zahlung

### OrderSubscriber

**Datei:** `src/Subscriber/OrderSubscriber.php`

**Event:** `state_machine.order_transaction.state_changed`
**Methode:** `onStateMachineStateTransactionChanged()`

```php
// Nur bei Transition zu "paid"
if ($event->getTransitionSide() === StateMachineStateChangeEvent::STATE_MACHINE_TRANSITION_SIDE_ENTER
    && $event->getStateName() === OrderTransactionStates::STATE_PAID) {
    $this->checkoutService->confirmOrder($orderId, $event->getContext());
}
```

### CheckoutService::confirmOrder()

**Datei:** `src/Service/CheckoutService.php`

1. **Order laden** mit LineItems, Produkte, Customer
2. **Für jedes Line-Item mit** `reservationUuid`:
   ```php
   $this->confirmTicket(
       lineItem: $lineItem,
       product: $product,
       customer: $customer,
       context: $context
   );
   ```
3. **confirmTicket():**
   ```php
   $response = $client->bookingConfirm(
       uuid: $lineItem->getPayloadValue('reservationUuid'),
       fullName: $customer->getFirstName() . ' ' . $customer->getLastName(),
       emailAddress: $customer->getEmail(),
       locales: ['de-DE'],
       country: 'de'
   );
   ```
4. **Bei Fehler:** Setzt Custom Fields:
   - `resubmission_active: true`
   - `resubmission_date: {datum + 3 Tage}`
5. **Interne Kommentare** zur Order hinzufügen (pro Line-Item)

---

## Stornierung

### Trigger 1: Kunde storniert im Account

**Event:** `CancelOrderRouteRequestEvent`
**Methode:** `OrderSubscriber::onCancelOrderRouteRequestEvent()`

```php
$this->checkoutService->cancelOrder($orderId, $event->getContext());
```

### Trigger 2: Admin storniert

**Event:** `state_machine.order.state_changed`
**Methode:** `OrderSubscriber::onStateMachineStateChanged()`

```php
if ($event->getStateName() === OrderStates::STATE_CANCELLED) {
    $this->checkoutService->cancelOrder($orderId, $event->getContext());
}
```

### CheckoutService::cancelOrder()

1. Order laden
2. Prüfe Order-Status = cancelled
3. **Für jedes Line-Item mit** `reservationUuid`:
   ```php
   if (!$client->isOffline()) {
       $response = $client->bookingCancellation($lineItem->getPayloadValue('reservationUuid'));
   }
   ```
4. Interne Kommentare hinzufügen

### Stornierbarkeits-Prüfung

**Event:** `AccountOrderPageLoadedEvent`
**Methode:** `OrderSubscriber::onAccountOrderPageLoadedEvent()`

Prüft für jedes Line-Item via API ob Buchung stornierbar ist:
```php
$booking = $client->getBooking($reservationUuid);
$lineItem->setPayloadValue('cancellable', $booking['cancellable'] ?? false);
```

Im Template `order-item.html.twig` wird der Cancel-Button nur angezeigt wenn mindestens ein Line-Item `cancellable: true` hat.