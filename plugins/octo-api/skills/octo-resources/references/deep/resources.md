# OCTO — Resources Capability (`octo/resources`)

## Capability-Identifier

```
octo/resources
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/resources
Content-Type: application/json
```

---

## Überblick

Ressourcen werden jeder Buchung zugewiesen und bestimmen die Verfügbarkeit für
ressourcenbasierte Produkte (Fahrzeuge, Zimmer, Sitzpläne etc.). Die Capability
ist optional — ohne explizite Zuweisung werden Ressourcen automatisch vergeben.

---

## API-Endpunkte

### GET /availability/resources

Ressourcen nach `resourceGroupId` für eine `availabilityId` abrufen.

```http
GET https://api.ventrata.com/octo/availability/resources?availabilityId={id}
Authorization: Bearer {api_key}
Octo-Capabilities: octo/resources
```

**Query-Parameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `availabilityId` | string (UUID) | **ja** | Verfügbarkeits-ID |

**Response:** `200 ResourceGroup[]`

---

### POST /availability/resources

Ressourcen-Zuweisungen einreichen.

```http
POST https://api.ventrata.com/octo/availability/resources
Authorization: Bearer {api_key}
Octo-Capabilities: octo/resources
Content-Type: application/json
```

**Request-Body:** Gleiche Felder wie GET-Query-Parameter

**Response:** `200 ResourceGroup[]`

---

## Schema-Erweiterungen

### Availability-Objekt

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `hasResources` | boolean | Availability hat Ressourcen |

> Nur auf `/availability`-Antworten, **nicht** auf `/availability/calendar`.

### AvailabilityBatchRow-Objekt

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `hasResources` | boolean | Batch-Row hat Ressourcen |

### AvailabilityResourcesRequest-Objekt

```typescript
interface AvailabilityResourcesRequest {
  availabilityId: string;
  resourceAllocations: Array<{
    resourceId: string;
  }>;
  // Mit octo/pickups:
  pickupPointId?: string;
  dropoffPointId?: string;
}
```

### Booking-Objekt (Response)

```typescript
interface ResourceAllocation {
  resourceGroupId: string;
  resourceGroup: {
    title: string;
  };
  resourceId: string;
  resource: {
    title: string;
  };
  seatIds: string[];
  seats: Array<{
    row: string;
    column: string;
  }>;
  paxCount: number;  // Server-seitig berechnet, im Request ignoriert
}
```

### BookingWriteRequest-Objekt

```typescript
interface BookingResourceRequest {
  resourceAllocations: Array<{
    resourceId: string;
    // seatIds und paxCount werden ignoriert → server-seitig vergeben
  }>;
}
```

### PackageAvailability-Objekt

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `hasResources` | boolean | Package-Availability hat Ressourcen |

---

## ResourceGroup-Antwort-Schema

```typescript
interface ResourceGroup {
  id: string;      // resourceGroupId
  title: string;
  resources: Array<{
    id: string;    // resourceId
    title: string;
    available: boolean;
    seats?: Array<{
      id: string;
      row: string;
      column: string;
      available: boolean;
    }>;
  }>;
}
```

---

## Unterstützte Endpunkte (Buchungen)

| Endpunkt | Methode | Aktion |
|----------|---------|--------|
| `/bookings` | POST | Buchung mit Ressourcen anlegen |
| `/bookings/{uuid}` | PATCH | Ressourcen aktualisieren |
| `/bookings/{uuid}/confirm` | POST | Mit Ressourcen bestätigen |
| `/bookings/{uuid}` | GET | Buchung mit Ressourcen abrufen |
| `/bookings` | GET | Buchungsliste mit Ressourcen |
| `/bookings/{uuid}/cancel` | POST | Stornierung (Ressourcen freigegeben) |
| `/bookings/{uuid}/extend` | POST | Verlängerung |

---

## Verhaltensregeln

1. **Felder im Request ignoriert**: `paxCount` und `seatIds` in `resourceAllocations` werden
   server-seitig berechnet; im Request übergeben = no-op
2. **Nicht-leere Zuweisung**: Wenn `resourceAllocations` vorhanden und nicht leer →
   nicht enthaltene Zuweisungen werden entfernt
3. **Leere Zuweisung**: `resourceAllocations: []` senden = no-op (keine Änderung)
4. **Vollständigkeit**: Jede Buchung muss aus jeder erforderlichen Ressourcengruppe
   genug Ressourcen zuweisen

---

## Vollständiges Beispiel

### Request: Verfügbare Ressourcen für eine Availability abrufen

```bash
curl -X GET "https://api.ventrata.com/octo/availability/resources?availabilityId=availability_xyz789" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/resources"
```

### Response

```json
[
  {
    "id": "resource_group_bus",
    "title": "Busse",
    "resources": [
      {
        "id": "resource_bus_01",
        "title": "Bus 01 (Mercedes Sprinter)",
        "available": true
      },
      {
        "id": "resource_bus_02",
        "title": "Bus 02 (VW Crafter)",
        "available": false
      }
    ]
  },
  {
    "id": "resource_group_seats",
    "title": "Sitzplätze Bus 01",
    "resources": [
      {
        "id": "resource_seat_group_01",
        "title": "Alle Sitzplätze",
        "available": true,
        "seats": [
          { "id": "seat_1A", "row": "1", "column": "A", "available": true },
          { "id": "seat_1B", "row": "1", "column": "B", "available": true },
          { "id": "seat_2A", "row": "2", "column": "A", "available": false }
        ]
      }
    ]
  }
]
```

### Request: Buchung mit Ressourcen-Zuweisung

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/resources" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "resourceAllocations": [
      { "resourceId": "resource_bus_01" }
    ]
  }'
```

### Response

```json
{
  "uuid": "booking_111222",
  "status": "ON_HOLD",
  "resourceAllocations": [
    {
      "resourceGroupId": "resource_group_bus",
      "resourceGroup": { "title": "Busse" },
      "resourceId": "resource_bus_01",
      "resource": { "title": "Bus 01 (Mercedes Sprinter)" },
      "seatIds": ["seat_1A", "seat_1B"],
      "seats": [
        { "row": "1", "column": "A" },
        { "row": "1", "column": "B" }
      ],
      "paxCount": 2
    }
  ]
}
```

### Request: Availability mit hasResources

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/resources" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [{ "id": "unit_adult", "quantity": 2 }]
  }'
```

```json
[
  {
    "id": "availability_xyz789",
    "localDateTimeStart": "2025-07-01T10:00:00+02:00",
    "available": true,
    "status": "AVAILABLE",
    "hasResources": true
  }
]
```

---

*Quelle: https://docs.ventrata.com/capabilities/resources*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
