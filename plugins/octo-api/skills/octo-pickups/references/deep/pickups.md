# OCTO — Pickups Capability (`octo/pickups`)

## Capability-Identifier

```
octo/pickups
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/pickups
Content-Type: application/json
```

---

## Überblick

Fügt Abholungs- und Rückgabe-Konfiguration zu Produkt-Optionen hinzu, zeitgesteuerte
Abholpunkte zu Availability-Antworten und Auswahlfelder auf Buchungsobjekten.

---

## Schema-Erweiterungen am Option-Objekt

Endpunkte: `GET /products`, `GET /products/{productId}`

```typescript
interface PickupPoint {
  id: string;
  name: string;
  directions: string;
  address: string;
  coordinates: {
    latitude: number;
    longitude: number;
  };
  placeId: string;
  addressComponents: {
    street: string;
    streetNumber: string;
    city: string;
    state: string;
    country: string;
    postalCode: string;
  };
}

interface OptionPickup {
  pickupAvailable: boolean;     // Abholung verfügbar
  pickupRequired: boolean;      // Abholung obligatorisch
  pickupPoints: PickupPoint[];  // Verfügbare Abholpunkte
  dropoffAvailable: boolean;    // Rückgabe verfügbar
  dropoffRequired: boolean;     // Rückgabe obligatorisch
  dropoffPoints: PickupPoint[]; // Verfügbare Rückgabepunkte
}
```

---

## Schema-Erweiterungen an Availability

Endpunkte: `POST /availability`, `POST /availability/batch`

Wie Option, aber mit zeitlichen Daten:

```typescript
interface TimedPickupPoint extends PickupPoint {
  localDateTime: string;    // Startzeit ISO 8601 (nullable)
  localDateTimeTo: string;  // Endzeitfenster ISO 8601 (nullable)
}

interface AvailabilityPickup {
  pickupAvailable: boolean;
  pickupRequired: boolean;
  pickupPoints: TimedPickupPoint[];
  dropoffAvailable: boolean;
  dropoffRequired: boolean;
  dropoffPoints: TimedPickupPoint[];
}
```

---

## Schema-Erweiterungen am AvailabilityResourcesRequest

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `pickupPointId` | string (UUID) | Gewählter Abholpunkt |
| `dropoffPointId` | string (UUID) | Gewählter Rückgabepunkt |

---

## Schema-Erweiterungen am BookingWriteRequest

Endpunkte: `POST /bookings`, `PATCH /bookings/{uuid}`

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `pickupRequested` | boolean | nein | Abholung anfordern |
| `pickupPointId` | string (UUID) | nein | ID des Abholpunkts |
| `pickupHotel` | string | nein | Hotelname (löst Geocoding aus wenn kein Match) |
| `pickupAddress` | string | nein | Adresse für genaueres Geocoding |
| `pickupHotelRoom` | string | nein | Zimmernummer |
| `pickupNotes` | string | nein | Sonderanweisungen |
| `dropoffRequested` | boolean | nein | Rückgabe anfordern |
| `dropoffPointId` | string (UUID) | nein | ID des Rückgabepunkts |
| `dropoffHotel` | string | nein | Hotelname für Rückgabe |
| `dropoffAddress` | string | nein | Adresse für Rückgabe-Geocoding |
| `dropoffNotes` | string | nein | Sonderanweisungen für Rückgabe |

**Prioritätsregel:** Wenn `pickupPointId` und `pickupHotel` beide übergeben → `pickupPointId` hat Vorrang.

---

## Schema-Erweiterungen an der Booking-Response

Alle BookingWriteRequest-Felder plus:

```typescript
interface BookingPickupResponse {
  pickupPoint: {
    id: string;
    name: string;
    localDateTime: string;    // ISO 8601 Abholzeit
    localDateTimeTo: string;  // ISO 8601 Endzeitfenster (nullable)
  } | null;
  pickupDispatch: {
    id: string;
    vehicle: string;
    driver: string;
    guide: string;
    area: string;
    notes: string;
  } | null;
  dropoffPoint: {
    id: string;
    name: string;
    localDateTime: string;
    localDateTimeTo: string;
  } | null;
  dropoffDispatch: {
    id: string;
    vehicle: string;
    driver: string;
    guide: string;
    area: string;
    notes: string;
  } | null;
}
```

---

## Verhaltensregeln

1. **Priorität**: `pickupPointId` > `pickupHotel`; gleiches Prinzip für Dropoff
2. **Hotel-Geocoding**: Unbekannte Hotelnamen lösen automatisches Geocoding aus; neuer Eintrag wird angelegt
3. **Adress-Verbesserung**: `pickupAddress`/`dropoffAddress` verbessert Geocoding-Genauigkeit
4. **Löschen**: `null` senden löscht bestehende Abholwerte
5. **Dropoff-Auflösung**: Custom-Dropoff-Produkte benötigen Endzeiten; haltepunktbasierte Produkte lösen per Haltestelle/Datum auf

---

## Vollständiges Beispiel

### Request: Product mit Pickup-Konfiguration

```bash
curl -X GET "https://api.ventrata.com/octo/products/product_abc123" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pickups"
```

### Response (Option-Auszug)

```json
{
  "id": "option_def456",
  "pickupAvailable": true,
  "pickupRequired": false,
  "pickupPoints": [
    {
      "id": "pickup_point_001",
      "name": "Hotel Adlon Berlin",
      "directions": "Bitte 10 Minuten vor Abfahrt in der Lobby warten",
      "address": "Unter den Linden 77, 10117 Berlin",
      "coordinates": {
        "latitude": 52.5163,
        "longitude": 13.3777
      },
      "placeId": "ChIJBxjuEv9RqEcR8LFXM00gMQ4",
      "addressComponents": {
        "street": "Unter den Linden",
        "streetNumber": "77",
        "city": "Berlin",
        "state": "Berlin",
        "country": "DE",
        "postalCode": "10117"
      }
    }
  ],
  "dropoffAvailable": true,
  "dropoffRequired": false,
  "dropoffPoints": []
}
```

### Request: Availability mit zeitgesteuerten Abholpunkten

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pickups" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [{ "id": "unit_adult", "quantity": 2 }]
  }'
```

### Response (Availability mit Zeiten)

```json
[
  {
    "id": "availability_xyz789",
    "localDateTimeStart": "2025-07-01T10:00:00+02:00",
    "available": true,
    "pickupAvailable": true,
    "pickupRequired": false,
    "pickupPoints": [
      {
        "id": "pickup_point_001",
        "name": "Hotel Adlon Berlin",
        "directions": "10 Minuten vor Abfahrt in der Lobby",
        "localDateTime": "2025-07-01T09:30:00+02:00",
        "localDateTimeTo": "2025-07-01T09:45:00+02:00"
      }
    ],
    "dropoffAvailable": false,
    "dropoffRequired": false,
    "dropoffPoints": []
  }
]
```

### Request: Buchung mit Hotel-Abholung

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pickups" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "pickupRequested": true,
    "pickupHotel": "Hotel Adlon Kempinski",
    "pickupAddress": "Unter den Linden 77, 10117 Berlin",
    "pickupHotelRoom": "302",
    "pickupNotes": "Bitte Telefon anrufen bei Ankunft"
  }'
```

### Response

```json
{
  "uuid": "booking_111222",
  "status": "ON_HOLD",
  "pickupRequested": true,
  "pickupHotel": "Hotel Adlon Kempinski",
  "pickupAddress": "Unter den Linden 77, 10117 Berlin",
  "pickupHotelRoom": "302",
  "pickupNotes": "Bitte Telefon anrufen bei Ankunft",
  "pickupPoint": {
    "id": "pickup_point_001",
    "name": "Hotel Adlon Berlin",
    "localDateTime": "2025-07-01T09:30:00+02:00",
    "localDateTimeTo": "2025-07-01T09:45:00+02:00"
  },
  "pickupDispatch": null,
  "dropoffRequested": false,
  "dropoffPoint": null,
  "dropoffDispatch": null
}
```

---

*Quelle: https://docs.ventrata.com/capabilities/pickups*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
