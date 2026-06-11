# AvailbilityController (`src/Controller/AvailbilityController.php`)

## Zweck
Storefront-Controller für die **Verfügbarkeitsprüfung** von OCTO-Produkten. Verarbeitet AJAX-Requests aus dem Buy-Widget: prüft Verfügbarkeit + berechnet Preise/Units, persistiert den Auswahl-State in der Session und liefert gerenderte Twig-Block-Fragmente (Units/Preis/Availability-State) zurück. Behandelt online (OCTO-API) und offline (RheinKurier, lokale Berechnung). Eine der fehleranfälligsten Dateien (Session-Unit-Merge, viele Edge-Cases). (Dateiname enthält Tippfehler „Availbility".)

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class AvailbilityController extends StorefrontController`
- Klassen-Route-Scope: `StorefrontRouteScope` (`#[Route(defaults: [..._ROUTE_SCOPE => [StorefrontRouteScope::ID]])]`).
- `/** @noinspection ALL */` am Dateianfang.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$logger` | `OctoLoggerInterface` | Logging (Channel `octo`). |
| `$clientRegistry` | `OctoApiClientRegistry` | Supplier-Client-Auflösung + Offline-Check. |
| `$priceService` | `PriceService` | Währungsumrechnung, Lowest-Price. |
| `$propertyService` | `PropertyService` | (injiziert; im aktuellen Code nicht direkt verwendet). |
| `$sessionService` | `SessionService` | Session-Items lesen/schreiben. |
| `$validationService` | `ValidationService` | Request-Validierung. |
| `$calendarService` | `CalendarService` | Offline-Kalender. |

## Routen / öffentliche Methoden
### `checkAvailability(Request): Response`
- **Route:** `POST /octo-api/availability/check`, name `frontend.octo-api.availability.check`, `XmlHttpRequest=true`, `_httpCache=false`.
- **Ablauf:** validiert gegen `AVAILABILITY_CHECK`; bei Fehler 400 mit Messages (geloggt als warning). Lädt Session-Daten + API-Produkt (Fallback: `product.extensions.ffOctoProduct.product`).
- **Session-Unit-Merge (kritisch, Z. 88–123):** Nur wenn `units` GAR NICHT im Request ist (`$request->get('units') !== null` → false), werden Session-Units herangezogen; explizit gesendete (auch leere) Units sind maßgeblich (verhindert Zurückspringen einer Menge nach Minus→0).
- Ermittelt Option (`getOption`), Availability (`getAvailability`), Preis (`getTotalPrice`), Units (`getUnits`).
- Setzt `product['available']=false` wenn keine Units/Availability. Reichert Units mit Preis/Type an, persistiert Unit- und Octo-Produkt-Session-Items.
- **Begleit-Logik:** Units vom Typ `CHILD`/`INFANT` ohne eigene `accompaniedBy`-Restriktion bekommen alle Nicht-Begleit-Units als Begleiter zugewiesen.
- **Preis-Fallback:** wenn `price.retail == 0` → Lowest-Price + `listingPriceFrom=true`; wenn keine Units → `price.retail = product.calculatedPrice.unitPrice`.
- Rendert 3 Twig-Blöcke via `renderBlockView` aus `configurator.html.twig`: `buy_widget_configurator_detail__units_inner`, `__price_inner`, `__availability_state_inner`.
- Bei Offline-Client wird `capacity` auf `null` gesetzt.
- **Rückgabe:** JSON mit `units`, `product`, `status`, `available`, `capacity`, `widgets` (DOM-Selektor → HTML). Bei Exception 400 + Log.

### `availabilityCalendar(Request): Response`
- **Route:** `POST /octo-api/availability/calendar`, name `frontend.octo-api.availability.calendar`, `XmlHttpRequest=true`, `_httpCache=true`.
- Validiert gegen `AVAILABILITY_CALENDAR`. Berechnet Monatsanfang/-ende aus `date`.
- Offline: `calendarService->getCalendar(...)`. Online: `client->getCachedAvailabilityCalendar(...)`. Gibt JSON-Kalender zurück. Wirft `DateMalformedStringException`.

## Private Methoden (Auswahl)
- `setOctoProductSessionItem(...)`: speichert unter `getUniqueLineItemId(productId, units)` JSON {units, availability, localDate, localTime}.
- `setUnitSessionItem(...)`: speichert unter `octo-product-session-{productId}` JSON {optionId, units(>0), localDate, localTime}.
- `getSessionData(...)`: liest `octo-product-session-{productId}`; bei Fehler `[]` + warning.
- `getOption(apiProduct, product, request)`: matcht die gewählte Shopware-Option per Namensvergleich (`title`/`internalName` vs. `translated.name`).
- `getTotalPrice(availability)`: Default-Pricing (0/EUR) wenn leer, dann `priceService->getConvertedExchangePrice`.
- `getUnits(...)`: baut Units aus `apiProduct.options[].units`, setzt Preise aus `availability.unitPricing`, überträgt gewählte Quantities, normalisiert Felder (restrictions, price, pricingFrom).
- `getApiProduct(request)`: `client->getCachedProduct(productUuid)`.
- `getAvailability(request, option)`: **Offline** → berechnet Preis lokal aus `option.units[].pricingFrom[0]` × quantity, baut synthetisches Availability-Objekt (`available=true`). **Online** → setzt Capabilities `['ventrata/resources','octo/pricing']`, `client->getAvailability(...)[0]`.
- `getUniqueLineItemId(referenceId, units): string`: filtert `quantity>0`, baut `id_qQty`-String, `Uuid::fromStringToHex(referenceId.unitString)`.

## Besonderheiten / Fallstricke
- **Duplikat:** `getUniqueLineItemId` existiert auch in `CartController` — dort jedoch **ohne** den `quantity>0`-Filter. Bei Änderungen beide angleichen (sonst weichen die Session-Keys ab!).
- `Octo-Env: test` Pflicht bei Online-Calls.
- Session-Merge-Logik ist die häufigste Bug-Quelle (Mengen-Sprünge).

## Bezüge
`OctoApiClientRegistry`, `PriceService`, `CalendarService`, `SessionService`, `ValidationService`, `configurator.html.twig`, `../session-management.md`.
