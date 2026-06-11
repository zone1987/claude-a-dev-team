# CartController (`src/Controller/CartController.php`)

## Zweck
Überschreibt die Shopware-Standardroute `frontend.checkout.line-item.add` (Priority **100**), um OCTO-Produkte mit Session-State (gewählte Units, Availability, Datum/Zeit) korrekt in den Warenkorb zu legen — inkl. Buchungsreservierung (online) und Payload-Anreicherung (Besuchsdatum, Reservierung, Labels). Standard-Produkte werden weiterhin normal verarbeitet.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class CartController extends StorefrontController`, `declare(strict_types=1)`
- Klassen-Route-Scope: `StorefrontRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$lineItemFactoryRegistry` | `LineItemFactoryRegistry` | Erzeugt LineItems. |
| `$cartService` | `CartService` | Fügt Items dem Cart hinzu. |
| `$bookingService` | `BookingService` | OCTO-Reservierung (online). |
| `$clientRegistry` | `OctoApiClientRegistry` | Offline-Check je Identifier. |
| `$systemConfigService` | `SystemConfigService` | Liest `bookingReservationTime`. |
| `$productRepository` | `EntityRepository` | Lädt Produkte inkl. Assoziationen. |
| `$logger` | `OctoLoggerInterface` | Logging. |

## Routen / öffentliche Methoden
### `addLineItems(Cart, RequestDataBag, Request, SalesChannelContext): Response`
- **Route:** `POST /checkout/line-item/add`, name `frontend.checkout.line-item.add`, `XmlHttpRequest=true`, **`priority: 100`** (überschreibt Core).
- Umhüllt von `Profiler::trace('cart::add-line-item', …)`.
- Liest `lineItems` aus dem DataBag (sonst `RoutingException::missingRequestParameter`).
- Lädt Produkte gebündelt (`getProductsByDataBag`), holt Session.
- **Pro LineItem:**
  - `referencedId`, Produkt + Parent, Session-Item `octo-product-session-{referencedId}`.
  - **Standard-Produkt** (keine `ffOctoProduct`-Extension ODER kein Session-Item): normales LineItem via Factory, weiter.
  - **OCTO-Produkt:** baut LineItem mit `id = Uuid::randomHex()`, Payload aus Session-Item + `taxRate`, `isOctoProduct=true`, `parentId`, `label{variant,parent}`.
  - Setzt Payload `isDefaultVariant` (erste Option `default`), `identifier`, `localTimeStart`.
  - **Besuchsdatum:** formatiert `localDate`/`localDateStart` via `IntlDateFormatter` mit explizitem Pattern `dd.MM.yyyy` (SHORT liefert sonst 2-stelliges Jahr) → Payload `visitingDate`.
  - **Reservierung (wenn `availability` vorhanden):** Offline-Check; bei online `bookingService->bookingReservation(...)` mit `SymfonyUuid::v4()`; fehlt `utcExpiresAt`, wird es aus `bookingReservationTime` berechnet (Format `AvailabilityCheckConstraintCollection::DATE_FORMAT`). Setzt Payload `reservationUuid`, `offlineClient`, `reservation`. Fängt `ValidationFailedException|DateMalformedStringException` (Log).
  - `CartException` mit Code `CART_INVALID_LINE_ITEM_QUANTITY_CODE` → Flash + ActionResponse; sonst rethrow.
- Fügt alle Items via `cartService->add` hinzu, Erfolgs-/Fehler-Flash (`traceErrors`).
- `ProductNotFoundException|RoutingException` → Fehler-Flash.
- **Rückgabe:** `createActionResponse($request)`.

## Private Methoden
- `getReservationUnits(currentSessionItem)`: expandiert Units mit `quantity>0` zu je `quantity` Einzel-Einträgen `['unitId'=>…]`.
- `traceErrors(cart)`: filtert Erfolgs-Promotions raus, fügt persistente Fehler als Flash hinzu, gibt `true` bei Fehlern.
- `filterSuccessErrorMessages(cart)`: wandelt `PromotionCartAddedInformationError` in Erfolgs-Flash.
- `getSessionItem(session, name)`: `@json_decode` des Session-Werts; `null` + warning bei Fehlen.
- `getSession(request)`: wirft `LogicException`, wenn Sessions deaktiviert.
- `getProductsByDataBag(lineItems, context)`: lädt referenzierte Produkte + deren Parents, mit Assoziationen `ffOctoProduct`, `cover.media`, `properties.options`, `tax.rules`.
- `getUniqueLineItemId(referenceId, units)`: `id_qQty`-String + `Uuid::fromStringToHex`. **Ohne** `quantity>0`-Filter (Abweichung zu `AvailbilityController`!).
- `getBookingReservationTime(context)`: liest `FfOctoApi.config.bookingReservationTime` (SalesChannel-spezifisch), Default `'30'`.

## Besonderheiten / Fallstricke
- **Priority 100** überschreibt die Core-Route — bei Shopware-Updates auf Signatur-Kompatibilität achten.
- **`getUniqueLineItemId`-Duplikat & Filter-Abweichung:** `AvailbilityController` filtert vorab `quantity>0`, hier NICHT. Solange die übergebenen Units bereits nur >0 enthalten, ergibt sich derselbe Hash — Vorsicht bei Änderungen.
- Offline-Produkte überspringen die echte Reservierung.

## Bezüge
`BookingService`, `OctoApiClientRegistry`, `OctoProductEntity`, `AvailabilityCheckConstraintCollection`, `Core/Checkout/Cart/OctoCartCollector.php`, `../session-management.md`, `../booking-flow.md`.
