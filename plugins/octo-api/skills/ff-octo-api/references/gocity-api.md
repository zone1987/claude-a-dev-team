# GoCity OCTO API Dokumentation

> **Offizielle Dokumentation:** https://leisurepassgroup.github.io/trade-api-docs/octo/
> **Produktdaten (komprimiert):** [api/ids/gocity.json](api/ids/gocity.json) (344 KB, 49 Produkte)

## Übersicht

GoCity (ehemals Leisure Pass Group) betreibt eine eigene OCTO-kompatible API für City-Pässe. Im Gegensatz zu Ventrata wird hier eine separate API-Instanz verwendet.

## Basis-URLs

| Umgebung | URL |
|---|---|
| **Staging** | `https://api.staging.gocity.tech/octo/` |
| **Produktion** | `https://api.gocity.com/octo/` |

**Hinweis:** Das Plugin verwendet aktuell die **Staging-URL** (`api.staging.gocity.tech`), konfiguriert in `GoCityClient.php`.

## Authentifizierung

Identisch zu Ventrata: `Authorization: Bearer {token}`

## Unterschiede zu Ventrata

| Aspekt | Ventrata | GoCity |
|---|---|---|
| Basis-URL | `api.ventrata.com/octo/` | `api.staging.gocity.tech/octo/` |
| Buchungsstatus (neu) | `PENDING` | `ON_HOLD` |
| Booking Update (PATCH) | Unterstützt | Nicht dokumentiert |
| Booking Extend | Unterstützt | Nicht dokumentiert |
| Capabilities | 24 | Eingeschränkt (nur `octo/pricing` bestätigt) |
| Unit-Typen | ADULT, CHILD, SENIOR, FAMILY, GROUP, OTHER | ADULT, CHILD (+ VIP in Doku) |
| Webhooks | Vollständig | Nicht dokumentiert |
| Preismodell | Standard | PUBLIC vs. RESTRICTED (`priceDistributionModel`) |
| Datumsformat (Availability) | `Y-m-d H:i:s` | `Y-m-d` (im Plugin speziell behandelt!) |
| Supplier-Endpoint | `GET /suppliers/{id}` | `GET /supplier` (ohne ID) |

### Im Plugin behandelte GoCity-Besonderheiten

1. **Datumsformat:** In `AvailbilityController::getAvailability()` wird für GoCity das Format `Y-m-d` statt `Y-m-d H:i:s` verwendet:
   ```php
   if ($identifier === GoCityClient::IDENTIFIER) {
       $dateFormat = 'Y-m-d';
   }
   ```

2. **Supplier-Endpoint:** `GoCityClient` überschreibt `getCachedSupplier()` und ruft `GET /supplier` ohne ID auf (statt `/suppliers/{id}`).

## GoCity-Produkte

### Produktstruktur

GoCity-Produkte haben weniger Felder als GoldenTours-Produkte. Keine Beschreibungen, Bilder, Tags, Koordinaten etc.:

```json
{
  "id": "UUID",
  "internalName": "London Explorer Pass",
  "reference": "LON Go C Df",
  "locale": "en",
  "timeZone": "Europe/London",
  "allowFreesale": true,
  "instantConfirmation": true,
  "instantDelivery": true,
  "availabilityRequired": true,
  "availabilityType": "OPENING_HOURS",
  "deliveryFormats": ["HTML_URL", "PDF_URL"],
  "deliveryMethods": ["TICKET", "VOUCHER"],
  "redemptionMethod": "DIGITAL",
  "defaultCurrency": "GBP",
  "availableCurrencies": ["GBP"],
  "pricingPer": "UNIT",
  "brand": "Go City",
  "durationType": "CHOICE | DAY",
  "variant": "Default",
  "destinationId": "UUID",
  "destinationName": "London",
  "options": [...]
}
```

### Produkt-Typen

GoCity bietet zwei Haupttypen:

1. **Explorer Pass** (durationType: `CHOICE`) – Kunde wählt X Attraktionen (3-Choice, 4-Choice, ...)
2. **All-Inclusive Pass** (durationType: `DAY`) – Zugang zu allen Attraktionen für X Tage (1-Day, 2-Day, ...)

### Alle 49 GoCity-Produkte

#### Europa (20 Produkte)

| Stadt | Produkt | Währung | Optionen |
|---|---|---|---|
| Amsterdam | Explorer Pass | EUR | 3/4/5/6/7-Choice |
| Amsterdam | All-Inclusive Pass | EUR | 1/2/3/4/5-Day |
| Barcelona | Explorer Pass | EUR | 3/4/5/6/7-Choice |
| Barcelona | All-Inclusive Pass | EUR | 2/3/5-Day |
| Dublin | Explorer Pass | EUR | 3/4/5/6/7-Choice |
| Dublin | All-Inclusive Pass | EUR | 1/2/3/5-Day |
| Gothenburg | All-Inclusive Pass | SEK | 1/2/3-Day |
| London | Explorer Pass | GBP | 2/3/4/5/6/7-Choice |
| London | The London Pass Plus | GBP | 1/2/3/4/5/6/7/10-Day |
| Madrid | Explorer Pass | EUR | 3/4/5/6/7-Choice |
| Madrid | All-Inclusive Pass | EUR | 1/2/3/5-Day |
| Paris | Explorer Pass | EUR | 3/4/5/6/7-Choice |
| Paris | The Paris Pass Plus | EUR | 2/4/6-Day |
| Paris | The Paris Pass | EUR | 2/4/6-Day |
| Prague | All-Inclusive Pass | EUR | 1/2/3-Day |
| Rome | Explorer Pass | EUR | 3/4/5/6/7-Choice |
| Rome | The Rome & Vatican Pass | EUR | 1 Option |
| Stockholm | All-Inclusive Pass | SEK | 1/2/3/5-Day |

#### Nordamerika (28 Produkte)

| Stadt | Produkt | Währung | Optionen |
|---|---|---|---|
| Boston | Explorer/All-Inclusive | USD | 2-5 Choice / 1-3 Day |
| Cancun | All-Inclusive Pass | USD | 1-5 Day |
| Chicago | Explorer/All-Inclusive | USD | 2-7 Choice / 1-5 Day |
| Las Vegas | Explorer/All-Inclusive | USD | 2-7 Choice / 1-5 Day |
| Los Angeles | All-Inclusive Plus/Standard | USD | 1-5 Day |
| Miami | Explorer/All-Inclusive | USD | 2-5 Choice / 1-3 Day |
| New Orleans | All-Inclusive Pass | USD | 1-3 Day |
| New York | Explorer Pass | USD | 2-10 Choice |
| New York | The New York Pass | USD | 1-10 Day |
| New York | Pass Essentials | USD | 1 Option |
| Oahu | Explorer/All-Inclusive | USD | 2-7 Choice / 1-7 Day |
| Orlando | Explorer/All-Inclusive | USD | 2-5 Choice / 2-5 Day |
| Philadelphia | Explorer/All-Inclusive | USD | 2-7 Choice / 1-3 Day |
| San Antonio | Explorer Pass | USD | 2-5 Choice |
| San Diego | Explorer/All-Inclusive/Essentials | USD | diverse |
| San Francisco | Explorer/All-Inclusive | USD | 2-5 Choice / 1-3 Day |

#### Naher Osten (3 Produkte)

| Stadt | Produkt | Währung | Optionen |
|---|---|---|---|
| Dubai | Explorer Pass | USD | 3/4/5/6/7-Choice |
| Dubai | All-Inclusive Pass | USD | 1/2/3/4/5-Day |
| Dubai | Highlights Pass | USD | 3/4/5-Choice |

### Option-Struktur (GoCity)

```json
{
  "id": "UUID",
  "default": false,
  "internalName": "London Explorer Pass 2-Choice",
  "reference": "LON Go 2C Df Ps",
  "optionType": "PASS",
  "availabilityLocalStartTimes": [],
  "cancellationCutoff": "365 days",
  "cancellationCutoffAmount": -365,
  "cancellationCutoffUnit": "day",
  "requiredContactFields": ["emailAddress"],
  "restrictions": { "minUnits": 0, "maxUnits": 50 },
  "units": [...],
  "durationValue": 2
}
```

**Besonderheiten:**
- `optionType` ist immer `PASS`
- `availabilityLocalStartTimes` ist immer leer (OPENING_HOURS, kein fester Startzeitpunkt)
- `cancellationCutoff` ist immer 365 Tage (1 Jahr Stornierungsfrist)
- `durationValue` gibt die Anzahl der Tage/Choices an

### Unit-Struktur (GoCity)

```json
{
  "id": "UUID",
  "internalName": "London Explorer Pass 2-Choice Adult",
  "reference": "Ad",
  "type": "ADULT",
  "requiredContactFields": [],
  "restrictions": {
    "minAge": 13,
    "maxAge": 99,
    "idRequired": false,
    "minQuantity": 0,
    "maxQuantity": 50,
    "paxCount": 1,
    "accompaniedBy": []
  },
  "pricingFrom": [
    { "original": 5400, "retail": 5400, "net": 4320, "currency": "GBP", "currencyPrecision": 2 }
  ],
  "pricing": [
    { "original": 5400, "retail": 5400, "net": 4320, "currency": "GBP", "currencyPrecision": 2 }
  ]
}
```

**Immer nur 2 Unit-Typen:**
- `ADULT` (minAge: 13, maxAge: 99)
- `CHILD` (minAge: 3, maxAge: 12)

### Preis-Übersicht (GoCity)

| Währung | Verwendung | Preisspanne (Retail) |
|---|---|---|
| EUR | Europa (Amsterdam, Barcelona, Dublin, Madrid, Paris, Prague, Rome) | 29.00 – 179.00 EUR |
| GBP | London | 54.00 – 99.00 GBP |
| USD | Nordamerika, Dubai | 49.00 – 339.00 USD |
| SEK | Gothenburg, Stockholm | 449.00 – 899.00 SEK |

### GoCity Buchungsablauf (OCTO)

```
1. GET /octo/products         → Alle Pässe laden
2. POST /octo/availability    → Verfügbarkeit prüfen (Freesale, immer verfügbar)
3. POST /octo/bookings        → Reservierung (Status: ON_HOLD)
4. POST /octo/bookings/{id}/confirm → Bestätigung mit Kundendaten
5. POST /octo/bookings/{id}/cancel  → Stornierung (wenn cancellable=true)
```

### GoCity Kontaktdaten

Bei Bestätigung (`/confirm`) wird ein `OctoContact`-Objekt übergeben:
```json
{
  "fullName": "string",
  "firstName": "string",
  "lastName": "string",
  "emailAddress": "string (pflicht)",
  "phoneNumber": "string",
  "locales": ["de-DE"],
  "postalCode": "string",
  "country": "de",
  "notes": "string"
}
```
