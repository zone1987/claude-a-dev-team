# CheckoutService (`src/Service/CheckoutService.php`)

## Zweck
Bestätigt bzw. storniert OCTO-Buchungen für eine Bestellung: ruft (online) die OCTO-`bookingConfirm`/`bookingCancellation`-API, schreibt einen ausführlichen Audit-Trail in den internen Order-Kommentar und markiert bei Fehlschlag die Order zur **Wiedervorlage** (`resubmission_active`). **Hotspot.** `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `class CheckoutService`

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$lineItemStates` | array | Sammelt pro LineItem den Confirm-Audit-Eintrag. |

## Konstruktor / DI
`EntityRepository $orderRepository`, `$productRepository`, `$customerRepository`, `OctoLoggerInterface $logger`, `OctoApiClientRegistry $clientRegistry`.

## Methoden
### `confirmOrder(orderId, Context): void`
- Lädt Order (`getOrder`) + Produkte; pro LineItem: `reservationUuid` aus Payload, Produkt (Parent bei Variante), `ffOctoProduct`-Extension.
- Ruft `confirmTicket(...)` (auch offline → nur Audit, kein API-Call).
- **Bei `!confirmed`:** Order-Custom-Fields `resubmission_active=true` + `resubmission_date` (Format `Y-m-d H:i:s.v`) setzen → Wiedervorlage (gelesen vom ResubmissionAppServer).
- Wenn ALLE LineItems bestätigt: `addInternalComments` schreibt den Audit-Trail.

### `private getOrder(orderId, Context): ?OrderEntity`
Criteria mit `customFields`, `stateMachineState`, `lineItems.product`, `primaryOrderDelivery.shippingOrderAddress.country`.

### `private getCustomerById(customerId, Context): ?CustomerEntity`
Mit `language.locale`.

### `private confirmTicket(octoProduct, order, context, lineItem, reservationUuid): bool`
- Baut Audit-`lineItemState` (`confirmed`, Label, ggf. `localDate`).
- **Nur online + reservationUuid≠'':** `bookingConfirm(uuid, fullName, email, [localeCode], countryIso, false, orderNumber)`. Bei `OctoErrorResponse` → State = Fehlercode (z.B. `ALREADY_CONFIRMED`), ggf. Message.
- Units je Typ → `lineItemUnits`; optionLabel; pusht in `$lineItemStates`. Gibt `true` zurück (Exception → error + `false`).

### `private getProducts(lineItems, Context): ProductCollection|EntityCollection`
Lädt referenzierte Produkte + Parents mit `ffOctoProduct`.

### `addInternalComments(order, comments, Context): void` (public)
Baut formatierten internen Kommentar (LINE-ITEM STATE CHANGED, ID/PRODUCT/DATE OF USE/OPTION/STATE/MESSAGE/CANCELLED_AT/REFUND/REASON/UNITS), hängt an bestehenden an, Upsert.

### `cancelOrder(orderId, Context): void` (public)
Lädt Order nur wenn State `cancelled`. Pro LineItem Audit (`CANCELED`, refund FULL). **Online + reservationUuid:** `bookingCancellation(uuid)`; übernimmt `response['cancellation']` falls vorhanden. `addInternalComments`.

## Besonderheiten / Fallstricke
- **Cross-Repo:** `resubmission_active`/`resubmission_date` sind die vom `FfResubmission`-Manifest definierten Order-Custom-Fields; der ResubmissionAppServer listet/bearbeitet sie. Namen müssen synchron bleiben (`../appserver-integration.md`).
- **Offline (RheinKurier):** kein `bookingConfirm`/`bookingCancellation`, aber Audit-Eintrag wird trotzdem geschrieben.
- `ALREADY_CONFIRMED` (siehe `OctoErrorCode`) wird als State im Audit vermerkt, nicht als harter Fehler — Resubmission greift nur bei echtem Fehlschlag (`confirmTicket` → false via Exception).
- Aufgerufen vom `OrderSubscriber` (Payment-Confirm → `confirmOrder`; Cancel → `cancelOrder`).

## Bezüge
`OrderSubscriber`, `OctoApiClient::bookingConfirm/bookingCancellation`, `OctoErrorResponse`, `Constant/OctoErrorCode.php`, `../booking-flow.md`, `../appserver-integration.md`.
