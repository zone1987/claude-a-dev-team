# OCTO — Packages Capability (`octo/packages`)

## Capability-Identifier

```
octo/packages
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/packages
Content-Type: application/json
```

---

## Überblick

Ermöglicht Paketprodukte mit auswählbaren Sub-Produkten ("Includes"). Das Paket-Produkt
fasst mehrere Einzel-Erlebnisse zusammen; die Includes können fest oder optional sein.

---

## Schema-Erweiterungen am Product

Endpunkte: `GET /products`, `GET /products/{productId}`

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `isPackage` | boolean | Produkt ist ein Paket |
| `isPackagePass` | boolean | Paket-Pass-Indikator |
| `packageProduct` | boolean | Paket-Produkt-Flag (redundant zu isPackage) |

---

## Schema-Erweiterungen am Option

```typescript
interface PackageInclude {
  id: string;           // UUID der Include-Gruppe
  title: string;        // Anzeigename der Gruppe
  description: string;  // Beschreibung
  includes: Array<{
    id: string;         // UUID des Include-Items
    productId: string;  // Referenziertes Produkt
    optionId: string;   // Referenzierte Option
    required: boolean;  // Pflichteinschluss
  }>;
}

// Im Option-Objekt:
interface PackageOption {
  packageIncludes: PackageInclude[];
}
```

---

## Schema-Erweiterungen an Availability

Endpunkte: `POST /availability` (nicht `/availability/calendar`)

```typescript
interface PackageAvailability {
  id: string;
  localDateTimeStart: string;    // ISO 8601
  localDateTimeEnd: string;      // ISO 8601
  allDay: boolean;
  available: boolean;
  status: "AVAILABLE" | "SOLD_OUT" | "LIMITED" | "CLOSED";
  statusMessage: string;
  utcCutoffAt: string;           // ISO 8601
  openingHours: Array<{
    from: string;                // "HH:MM"
    to: string;                  // "HH:MM"
  }>;
  packageIncludeId: string;      // Referenz zur Include-Gruppe
}

// Im Availability-Objekt:
interface AvailabilityWithPackages {
  packageAvailabilities: PackageAvailability[];
}
```

> Hinweis: `/availability/calendar` enthält **keine** `packageAvailabilities`.

---

## Schema-Erweiterungen am Booking

### Request-Felder

```typescript
// Variante 1: Includes als packageBookings beim Anlegen
interface PackageBookingWriteRequest {
  packageBookings: Array<{
    productId: string;
    optionId: string;
    availabilityId: string;
    units: Array<{ id: string; quantity: number }>;
    packageIncludeId: string;
  }>;
}

// Variante 2: Include-Buchung direkt mit packageUuid
interface IncludeBookingWriteRequest {
  productId: string;      // Include-Produkt
  optionId: string;
  availabilityId: string;
  units: Array<{ id: string; quantity: number }>;
  packageUuid: string;    // UUID der Parent-Package-Buchung
  packageIncludeId: string;
}
```

### Response-Felder

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `packageUuid` | string (UUID) | UUID der Parent-Package-Buchung |
| `packageIncludeId` | string | Include-Identifier |
| `packageUnitItemUuid` | string (UUID) | Unit-Item innerhalb des Pakets |
| `packageBookings` | Booking[] | Child-Include-Buchungen |

### BookingUnitItem-Erweiterung

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `packageIncludeId` | string | Include-Identifier |
| `packageUnitItemUuid` | string (UUID) | Unit-Item-Referenz |

---

## Unterstützte Endpunkte

| Endpunkt | Methode | Funktion |
|----------|---------|----------|
| `/products` | GET | Produktliste mit Package-Feldern |
| `/products/{productId}` | GET | Einzelprodukt mit Package-Feldern |
| `/availability` | POST | Verfügbarkeit mit packageAvailabilities |
| `/availability/calendar` | POST | Kalender (ohne packageAvailabilities) |
| `/bookings` | POST | Paket-Buchung anlegen |
| `/bookings/{uuid}` | PATCH | Paket-Buchung aktualisieren |
| `/bookings/{uuid}/confirm` | POST | Paket-Buchung bestätigen |
| `/bookings` | GET | Buchungen abrufen |
| `/bookings/{uuid}/cancel` | POST | Stornierung |
| `/bookings/{uuid}/extend` | POST | Verlängerung |

---

## Einschränkungen

- Include-Buchungen berücksichtigen `updatable` und `cancellable`-Flags
- Child-Buchungen mit versteckten Includes oder abweichendem Stornierungsstatus werden
  nicht serialisiert
- `/availability/calendar` schließt verschachtelte `packageAvailabilities` aus

---

## Vollständiges Beispiel

### Request: Paket-Availability abfragen

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/packages" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_package_001",
    "optionId": "option_package_default",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [{ "id": "unit_adult", "quantity": 2 }]
  }'
```

### Response

```json
[
  {
    "id": "availability_pkg_xyz",
    "localDateTimeStart": "2025-07-01T09:00:00+02:00",
    "localDateTimeEnd": "2025-07-01T17:00:00+02:00",
    "allDay": false,
    "available": true,
    "status": "AVAILABLE",
    "packageAvailabilities": [
      {
        "id": "avail_include_001",
        "localDateTimeStart": "2025-07-01T09:00:00+02:00",
        "localDateTimeEnd": "2025-07-01T11:00:00+02:00",
        "allDay": false,
        "available": true,
        "status": "AVAILABLE",
        "statusMessage": "Verfügbar",
        "utcCutoffAt": "2025-06-30T22:00:00Z",
        "openingHours": [],
        "packageIncludeId": "include_grp_001"
      },
      {
        "id": "avail_include_002",
        "localDateTimeStart": "2025-07-01T13:00:00+02:00",
        "localDateTimeEnd": "2025-07-01T15:00:00+02:00",
        "allDay": false,
        "available": true,
        "status": "AVAILABLE",
        "statusMessage": "Verfügbar",
        "utcCutoffAt": "2025-06-30T22:00:00Z",
        "openingHours": [],
        "packageIncludeId": "include_grp_002"
      }
    ]
  }
]
```

### Request: Paket-Buchung mit Includes anlegen

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/packages" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_package_001",
    "optionId": "option_package_default",
    "availabilityId": "availability_pkg_xyz",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "packageBookings": [
      {
        "productId": "product_include_a",
        "optionId": "option_include_a",
        "availabilityId": "avail_include_001",
        "units": [{ "id": "unit_adult", "quantity": 2 }],
        "packageIncludeId": "include_grp_001"
      },
      {
        "productId": "product_include_b",
        "optionId": "option_include_b",
        "availabilityId": "avail_include_002",
        "units": [{ "id": "unit_adult", "quantity": 2 }],
        "packageIncludeId": "include_grp_002"
      }
    ]
  }'
```

### Response

```json
{
  "uuid": "booking_pkg_main_001",
  "status": "ON_HOLD",
  "productId": "product_package_001",
  "optionId": "option_package_default",
  "packageBookings": [
    {
      "uuid": "booking_include_a_001",
      "status": "ON_HOLD",
      "packageUuid": "booking_pkg_main_001",
      "packageIncludeId": "include_grp_001"
    },
    {
      "uuid": "booking_include_b_001",
      "status": "ON_HOLD",
      "packageUuid": "booking_pkg_main_001",
      "packageIncludeId": "include_grp_002"
    }
  ]
}
```

---

*Quelle: https://docs.ventrata.com/capabilities/packages*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
