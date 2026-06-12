# OCTO API — Vollständige Fehlercode-Referenz

## Fehler-Response-Format

Alle Fehler-Responses der OCTO API verwenden folgende Struktur:

```typescript
type BaseError = {
  error: string;         // Fehlercode-Identifier (z.B. "INVALID_PRODUCT_ID")
  errorMessage: string;  // Lesbare Fehlermeldung (übersetzt via Accept-Language)
};
```

Einige Fehlercodes haben zusätzliche Felder (kontextspezifische Informationen):

```typescript
// Mit zusätzlichem Feld productId:
type ErrorInvalidProductId = BaseError & {
  productId: string;
};

// Mit zusätzlichem Feld optionId:
type ErrorInvalidOptionId = BaseError & {
  optionId: string;
};

// Mit zusätzlichem Feld unitId:
type ErrorInvalidUnitId = BaseError & {
  unitId: string;
};

// Mit zusätzlichem Feld availabilityId:
type ErrorInvalidAvailabilityId = BaseError & {
  availabilityId: string;
};

// Mit zusätzlichem Feld uuid:
type ErrorInvalidBookingUuid = BaseError & {
  uuid: string;
};
```

---

## HTTP-Statuscodes

| HTTP-Status | Bedeutung |
|------------|-----------|
| `200 OK` | Anfrage erfolgreich |
| `400 Bad Request` | Ungültige Anfrage |

---

## Vollständige Fehlercode-Liste

| Fehlercode | Beschreibung | Zusatzfelder |
|-----------|-------------|-------------|
| `INVALID_PRODUCT_ID` | Fehlende oder ungültige `productId` in der Anfrage | `productId` |
| `INVALID_OPTION_ID` | Fehlende oder ungültige `optionId` in der Anfrage | `optionId` |
| `INVALID_UNIT_ID` | Fehlende oder ungültige `unitId` in der Anfrage | `unitId` |
| `INVALID_AVAILABILITY_ID` | Fehlende oder ungültige `availabilityId` in der Anfrage | `availabilityId` |
| `INVALID_BOOKING_UUID` | Fehlende oder ungültige Buchungs-UUID, oder bei Bestätigung: Buchung ist möglicherweise bereits abgelaufen | `uuid` |
| `BAD_REQUEST` | Request-Body ist nicht korrekt formatiert, hat fehlende Pflichtfelder oder enthält falsche Datentypen | — |
| `UNPROCESSABLE_ENTITY` | Request-Body ist technisch korrekt, kann aber aus anderen Gründen nicht verarbeitet werden | — |
| `INTERNAL_SERVER_ERROR` | Backend-Server ist ausgefallen oder es gibt einen Netzwerkausfall | — |
| `UNAUTHORIZED` | Der API-Key wurde nicht im `Authorization`-Header gesendet | — |
| `FORBIDDEN` | Der API-Key ist ungültig oder widerrufen, oder fehlender Zugriff auf Endpunkt/Ressource | — |

---

## Fehler-Response-Beispiele

### INVALID_PRODUCT_ID

```json
{
  "error": "INVALID_PRODUCT_ID",
  "errorMessage": "The Product ID was invalid or missing",
  "productId": "123"
}
```

### INVALID_OPTION_ID

```json
{
  "error": "INVALID_OPTION_ID",
  "errorMessage": "The Option ID was invalid or missing",
  "optionId": "321"
}
```

### INVALID_UNIT_ID

```json
{
  "error": "INVALID_UNIT_ID",
  "errorMessage": "The Unit ID was invalid or missing",
  "unitId": "senior"
}
```

### INVALID_AVAILABILITY_ID

```json
{
  "error": "INVALID_AVAILABILIY_ID",
  "errorMessage": "The Availability ID was invalid or missing",
  "availabilityId": "2020-01-01T10:30+08:00"
}
```

### UNAUTHORIZED

```json
{
  "error": "UNAUTHORIZED",
  "errorMessage": "No authorization header was provided"
}
```

### FORBIDDEN

```json
{
  "error": "FORBIDDEN",
  "errorMessage": "The API key was invalid or revoked"
}
```

### BAD_REQUEST

```json
{
  "error": "BAD_REQUEST",
  "errorMessage": "The request body is not formatted correctly"
}
```

---

## Fehler pro Endpunkt

### POST /availability/ und POST /availability/calendar

Mögliche Fehler (400):
- `ErrorInvalidProductId`
- `ErrorInvalidOptionId`
- `ErrorBadRequest`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

### POST /bookings/ (Reservation)

Mögliche Fehler (400):
- `ErrorInvalidProductId`
- `ErrorInvalidOptionId`
- `ErrorInvalidUnitId`
- `ErrorInvalidAvailabilityId`
- `ErrorUnprocessableEntity`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

### POST /bookings/{uuid}/confirm

Mögliche Fehler (400):
- `ErrorInvalidProductId`
- `ErrorInvalidOptionId`
- `ErrorInvalidUnitId`
- `ErrorInvalidAvailabilityId`
- `ErrorInvalidBookingUuid`
- `ErrorUnprocessableEntity`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

### POST /bookings/{uuid}/cancel

Mögliche Fehler (400):
- `ErrorInvalidBookingUuid`
- `ErrorUnprocessableEntity`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

### GET /bookings/ und GET /bookings/{uuid}

Mögliche Fehler (400):
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`
- (GET /{uuid} auch: `ErrorInvalidBookingUuid`)

### GET /products/ und GET /products/{id}

Mögliche Fehler (400):
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`
- (GET /{id} auch: `ErrorInvalidProductId`)

---

## Fehlerübersetzung

Fehlermeldungen im Feld `errorMessage` werden automatisch übersetzt, wenn der `Accept-Language`-Header gesetzt ist. Beispiel:

```http
Accept-Language: de
```

Gibt dann deutschen Text in `errorMessage` zurück.

---

**Quelle:** https://docs.ventrata.com/getting-started/errors
