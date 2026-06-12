# Supplier-Vergleich

## Übersicht

| Eigenschaft | GoldenTours | GoCity | RheinKurier |
|------------|------------|--------|-------------|
| Typ | Online | Online | **OFFLINE** |
| API | Ventrata OCTO | GoCity OCTO | Shopware App |
| Identifier | `goldentours` | `gocity` | `rheinkurier` |
| Produkte | 278 (London) | 49 (25 Städte) | Via App |
| Unit-Typen | 8 | 2 | JSON-basiert |
| Reservierungen | Ja | Ja | Nein |
| Stornierungen | Ja | Ja | Nein |
| Delivery-Formate | 6 | 2 | — |
| Availability-Typ | START_TIME, OPENING_HOURS | FREESALE | — |
| Booking-Status | PENDING | ON_HOLD | — |
| Datum-Format | Y-m-d H:i:s | Y-m-d | — |

## Code-Stellen die supplier-spezifisch reagieren

| Datei | Verhalten |
|-------|----------|
| `AbstractOctoApiClient::request()` | Returns `[]` wenn OFFLINE |
| `AvailbilityController::getAvailability()` | Berechnet Offline-Preis aus `pricingFrom` |
| `AvailbilityController::availabilityCalendar()` | Returns `[]` für Offline |
| `CartController::addLineItems()` | Keine Reservierung für Offline |
| `BookingService::bookingReservation()` | Returns `[]` wenn Offline |
| `CheckoutService::confirmTicket()` | Überspringt API-Call |
| `CheckoutService::cancelOrder()` | Überspringt API-Call |
| `OrderSubscriber::onAccountOrderPageLoadedEvent()` | Kein Cancellable-Check |
| `OctoApiPriceUpdaterHandler::run()` | Überspringt RheinKurier |
| `OctoApiWarmCacheHandler::run()` | Überspringt Offline-Clients |
| `OctoProductController::listProducts()` | Filtert GoCity-Produkte ohne 'LON'-Prefix |
| `GoCityClient::getCachedSupplier()` | Ruft `/supplier` statt `/supplier/{id}` auf |

## Datenstruktur-Unterschiede

### GoldenTours hat (GoCity nicht)
- title, country, location, address, Koordinaten, Google Place ID
- Descriptions (short/long), Highlights, Alerts
- Inclusions/Exclusions, Booking/Privacy Terms
- FAQs, Redemption/Usage Instructions
- Cover Image, Banner, Video URL, Gallery (3-10 Bilder)
- Brand und Destination Objekte, Categories, Operator, Tags
- Option-Level: Start/End Dates, Cutoff, Duration, Meeting Points, Itinerary
- Unit-Level: Lokalisierte Titel, accompaniedByRatio

### GoCity hat
- Nur Basis-ID/Name/Locale Info
- optionType immer "PASS"
- cancellationCutoff immer 365 Tage
- 2 Produkttypen: Explorer Pass (CHOICE) und All-Inclusive Pass (DAY)

### RheinKurier
- Keine API-Daten
- Preise nur aus gespeichertem `pricingFrom`
- Keine Reservierungen, Bestätigungen oder Stornierungen
