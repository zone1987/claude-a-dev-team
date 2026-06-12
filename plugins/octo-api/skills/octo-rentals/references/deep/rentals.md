# OCTO — Rentals Capability (`octo/rentals`)

## Capability-Identifier

```
octo/rentals
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/rentals
Content-Type: application/json
```

---

## Überblick

Fügt Dauerauswahl für Mietprodukte hinzu und gibt Miet-Metadaten auf Product, Option
und Booking-Antworten aus. Beispiele: Fahrradverleih, Kayak-Verleih, Audioguide-Ausleihe.

---

## Schema-Erweiterungen am Product

Endpunkte: `GET /products`, `GET /products/{productId}`

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `isRental` | boolean | Produkt ist ein Mietprodukt |

---

## Schema-Erweiterungen am Option

```typescript
interface RentalDuration {
  id: string;           // z.B. "rental_duration_2h"
  title: string;        // Anzeigename, z.B. "2 Stunden"
  duration: string;     // ISO 8601 Duration, z.B. "PT2H"
  durationAmount: number; // Numerischer Betrag (z.B. 2)
  durationUnit: RentalDurationUnit;
}

type RentalDurationUnit = "HOUR" | "MINUTE" | "DAY" | "WEEK";

// Im Option-Objekt:
interface RentalOption {
  rentalDurations: RentalDuration[];
}
```

---

## Schema-Erweiterungen an Availability

Endpunkte: `POST /availability`, `POST /availability/calendar`,
`POST /availability/batch`, `POST /availability/calendar/batch`

### Request-Erweiterung

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `rentalDurationId` | string | nein | ID der gewählten Mietdauer |

> Die gewählte Dauer wird auf Availability und Preisberechnung angewendet.
> Keine neuen Felder in der Availability-Response.

---

## Schema-Erweiterungen am Booking

### Write-Request

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `rentalDurationId` | string | nein | Gewählte Mietdauer-ID |

### Response

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `rentalDurationId` | string | Gewählte Dauer-ID |
| `rentalDuration` | RentalDurationDetail | Vollständige Dauer-Metadaten |

```typescript
interface RentalDurationDetail {
  id: string;
  duration: string;           // ISO 8601 Duration
  durationAmount: number;     // Numerischer Wert
  durationUnit: RentalDurationUnit;
  title: string;
  description: string;
}
```

---

## Unterstützte Endpunkte

| Endpunkt | Methode | Funktion |
|----------|---------|----------|
| `/products` | GET | Produktliste mit isRental |
| `/products/{productId}` | GET | Einzelprodukt mit rentalDurations |
| `/availability` | POST | Availability mit rentalDurationId |
| `/availability/calendar` | POST | Kalender-Availability mit rentalDurationId |
| `/availability/batch` | POST | Batch-Availability |
| `/availability/calendar/batch` | POST | Batch-Kalender-Availability |
| `/bookings` | POST | Buchung mit rentalDurationId |
| `/bookings/{uuid}` | PATCH | Buchung aktualisieren |
| `/bookings/{uuid}/confirm` | POST | Bestätigen |
| `/bookings` | GET | Buchungsliste |
| `/bookings/{uuid}` | GET | Einzelbuchung |
| `/bookings/{uuid}/cancel` | POST | Stornierung |
| `/bookings/{uuid}/extend` | POST | Verlängerung |

---

## Wichtige Einschränkung

Immer IDs aus `option.rentalDurations[]` verwenden. Nicht unterstützte Duration-Units
geben `INVALID_RENTAL_DURATION_ID` zurück.

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `INVALID_RENTAL_DURATION_ID` | 400 | `rentalDurationId` ist ungültig oder nicht verfügbar |

---

## Vollständiges Beispiel

### Response: Product mit Miet-Dauern

```bash
curl -X GET "https://api.ventrata.com/octo/products/product_bike_rental" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/rentals"
```

```json
{
  "id": "product_bike_rental",
  "internalName": "fahrradverleih-berlin",
  "isRental": true,
  "options": [
    {
      "id": "option_city_bike",
      "internalName": "city-bike",
      "rentalDurations": [
        {
          "id": "rental_duration_1h",
          "title": "1 Stunde",
          "duration": "PT1H",
          "durationAmount": 1,
          "durationUnit": "HOUR"
        },
        {
          "id": "rental_duration_2h",
          "title": "2 Stunden",
          "duration": "PT2H",
          "durationAmount": 2,
          "durationUnit": "HOUR"
        },
        {
          "id": "rental_duration_4h",
          "title": "4 Stunden (Halbtag)",
          "duration": "PT4H",
          "durationAmount": 4,
          "durationUnit": "HOUR"
        },
        {
          "id": "rental_duration_1d",
          "title": "1 Tag",
          "duration": "P1D",
          "durationAmount": 1,
          "durationUnit": "DAY"
        }
      ]
    }
  ]
}
```

### Request: Availability mit Mietdauer

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/rentals, octo/pricing" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_bike_rental",
    "optionId": "option_city_bike",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [{ "id": "unit_bike", "quantity": 1 }],
    "rentalDurationId": "rental_duration_4h"
  }'
```

### Response

```json
[
  {
    "id": "availability_rental_xyz",
    "localDateTimeStart": "2025-07-01T09:00:00+02:00",
    "localDateTimeEnd": "2025-07-01T09:00:00+02:00",
    "allDay": false,
    "available": true,
    "status": "AVAILABLE",
    "vacancies": 15
  }
]
```

### Request: Buchung mit Mietdauer

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/rentals" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_bike_rental",
    "optionId": "option_city_bike",
    "availabilityId": "availability_rental_xyz",
    "units": [{ "id": "unit_bike", "quantity": 1 }],
    "rentalDurationId": "rental_duration_4h"
  }'
```

### Response

```json
{
  "uuid": "booking_rental_001",
  "status": "ON_HOLD",
  "productId": "product_bike_rental",
  "optionId": "option_city_bike",
  "rentalDurationId": "rental_duration_4h",
  "rentalDuration": {
    "id": "rental_duration_4h",
    "duration": "PT4H",
    "durationAmount": 4,
    "durationUnit": "HOUR",
    "title": "4 Stunden (Halbtag)",
    "description": "Genießen Sie 4 Stunden mit unserem City-Bike"
  }
}
```

---

*Quelle: https://docs.ventrata.com/capabilities/rentals*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
