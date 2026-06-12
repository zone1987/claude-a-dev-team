# OCTO — Content Capability (`octo/content`)

## Capability-Identifier

```
octo/content
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/content
Content-Type: application/json
```

---

## Überblick

Erweitert die Schemas von Supplier, Destination, Category, Product, Option, Unit, Item,
Availability und Booking mit umfangreichen Inhaltsfeldern (Bilder, Beschreibungen, FAQs,
Reiserouten, Schriftarten, Tarife, Punkte).

Bei kombinierter Nutzung mit `octo/cart` werden auch Order-Antworten erweitert.

---

## Hilfs-Objekte (Helper Objects)

```typescript
interface Notice {
  id: string;
  title: string;
  shortDescription: string;
  coverImageUrl: string;
}

interface TourGroup {
  id: string;
  internalName: string;
  title: string;
  shortDescription: string;
  icon: string;
}

interface Fare {
  id: string;
  internalName: string;
  title: string;
  shortDescription: string;
  fareGroup: FareGroup;
}

interface FareGroup {
  id: string;
  internalName: string;
  title: string;
  shortDescription: string;
}

interface Point {
  id: string;
  internalName: string;
  title: string;
  shortDescription: string;
  pointGroup: PointGroup;
}

interface PointGroup {
  id: string;
  internalName: string;
  title: string;
  shortDescription: string;
}

interface Font {
  id: string;
  name: string;
  normalTtfUrl: string;
  boldTtfUrl: string;
  italicTtfUrl: string;
  boldItalicTtfUrl: string;
}
```

---

## Itinerary-Schema

Auf Products und Options als Array:

```typescript
interface ItineraryItem {
  name: string;
  type: ItineraryType;  // "START" | "POI" | "EVENT" | "END"
  description: string;
  address: string;
  travelTime: string;   // ISO 8601 Duration, z.B. "PT30M"
  duration: string;     // ISO 8601 Duration
}
```

---

## Schema-Erweiterungen nach Ressource

### Product (`GET /products`, `GET /products/{productId}`)

Alle Standard-Produkt-Felder plus:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `title` | string | Anzeigename |
| `shortDescription` | string | Kurzbeschreibung |
| `description` | string | Vollständige Beschreibung (Markdown) |
| `highlights` | string[] | Aufzählung von Highlights |
| `inclusions` | string[] | Was ist enthalten |
| `exclusions` | string[] | Was ist nicht enthalten |
| `bookingTerms` | string | Buchungsbedingungen (Markdown) |
| `redemptionInstructions` | string | Einlöseanweisungen |
| `cancellationPolicy` | string | Stornierungsbedingungen |
| `destination` | Destination | Zielort-Objekt |
| `categories` | Category[] | Kategorien |
| `faqs` | Faq[] | Häufige Fragen |
| `coverImageUrl` | string (URL) | Titelbild |
| `bannerImageUrl` | string (URL) | Bannerbild |
| `videoUrl` | string (URL) | Video (YouTube/Vimeo) |
| `galleryImages` | Media[] | Bildergalerie |
| `bannerImages` | Media[] | Bannerbilder |
| `notices` | Notice[] | Hinweise |
| `tourGroups` | TourGroup[] | Tourgruppen |
| `fonts` | Font[] | Schriftarten für PDF/Ticket |

### Option

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `title` | string | Anzeigename |
| `shortDescription` | string | Kurzbeschreibung |
| `coverImageUrl` | string (URL) | Optionsbild |
| `itinerary` | ItineraryItem[] | Reiseroute |
| `fares` | Fare[] | Tarife |
| `points` | Point[] | Punkte/Haltestellen |

### Unit

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `title` | string | Anzeigename (z.B. "Erwachsene") |
| `shortDescription` | string | Kurzbeschreibung |

### Extra (kombiniert mit `octo/extras`)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `title` | string | Extra-Bezeichnung |
| `shortDescription` | string | Kurzbeschreibung |
| `coverImageUrl` | string (URL) | Bild des Extras |
| `duration` | string | ISO 8601 Duration |
| `durationAmount` | number | Numerischer Betrag der Duration |
| `durationUnit` | string | Zeiteinheit (HOUR, MINUTE, …) |

### Booking / BookingWriteRequest / Gift / Order

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `termsAccepted` | boolean | Nutzungsbedingungen akzeptiert |

> Bei Orders (`octo/cart`) überschreibt das `termsAccepted` auf Root-Ebene die Werte auf Booking-Ebene.

---

## Erweiterte Endpunkte

**Read (Product-Daten):**
- `GET /products`
- `GET /products/{productId}`

**Write (Booking-Felder):**
- `POST /bookings`
- `PATCH /bookings/{uuid}`
- `POST /bookings/{uuid}/confirm`

**Write (Order-Felder, benötigt `octo/cart`):**
- `POST /orders`
- `PATCH /orders/{orderId}`
- `PATCH /orders/{orderId}/preview`
- `POST /orders/{orderId}/confirm`

---

## Vollständiges Beispiel

### Request: Product mit Content abrufen

```bash
curl -X GET "https://api.ventrata.com/octo/products/product_abc123" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/content"
```

### Response (Auszug)

```json
{
  "id": "product_abc123",
  "internalName": "city-tour-berlin",
  "title": "Berlin Stadtrundfahrt",
  "shortDescription": "Entdecken Sie die Hauptstadt in 2 Stunden.",
  "description": "# Berlin Stadtrundfahrt\n\nEine unvergessliche Tour...",
  "highlights": [
    "Brandenburger Tor",
    "Reichstag",
    "Checkpoint Charlie"
  ],
  "inclusions": ["Audioguide", "Eintritt Reichstag"],
  "exclusions": ["Mittagessen", "Transfers"],
  "coverImageUrl": "https://cdn.ventrata.com/products/abc123/cover.jpg",
  "galleryImages": [
    {
      "id": "media_001",
      "url": "https://cdn.ventrata.com/products/abc123/gallery1.jpg",
      "title": "Brandenburger Tor",
      "type": "JPEG"
    }
  ],
  "faqs": [
    {
      "question": "Ist der Tour barrierefrei?",
      "answer": "Ja, alle Fahrzeuge sind mit Rollstuhlrampen ausgestattet."
    }
  ],
  "destination": {
    "id": "dest_berlin",
    "name": "Berlin",
    "country": "DE",
    "latitude": 52.52,
    "longitude": 13.405
  },
  "notices": [
    {
      "id": "notice_001",
      "title": "Baustelle am Brandenburger Tor",
      "shortDescription": "Vom 01.-15. Juli eingeschränkte Zufahrt.",
      "coverImageUrl": null
    }
  ],
  "options": [
    {
      "id": "option_def456",
      "title": "Standard Tour",
      "shortDescription": "2h klassische Stadtführung",
      "coverImageUrl": "https://cdn.ventrata.com/options/def456/cover.jpg",
      "itinerary": [
        {
          "name": "Startpunkt Hauptbahnhof",
          "type": "START",
          "description": "Treffpunkt am Eingang Nord",
          "address": "Europaplatz 1, 10557 Berlin",
          "travelTime": "PT0M",
          "duration": "PT5M"
        },
        {
          "name": "Brandenburger Tor",
          "type": "POI",
          "description": "Wahrzeichen Berlins",
          "address": "Pariser Platz, 10117 Berlin",
          "travelTime": "PT15M",
          "duration": "PT20M"
        },
        {
          "name": "Endpunkt",
          "type": "END",
          "description": "Rückkehr zum Startpunkt",
          "address": "Europaplatz 1, 10557 Berlin",
          "travelTime": "PT15M",
          "duration": "PT0M"
        }
      ]
    }
  ]
}
```

### Request: Buchung mit termsAccepted

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/content" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "termsAccepted": true
  }'
```

---

## TypeScript-Typen (octo-types, MIT)

```typescript
// Aus @octotravel/octo-types
type ItineraryType = "START" | "POI" | "EVENT" | "END";

interface Media {
  id: string;
  url: string;
  title: string;
  type: "JPEG" | "PNG" | "MP4" | "YOUTUBE" | "VIMEO";
}

// CapabilityId enum: OCTO_CONTENT = "octo/content"
```

---

*Quelle: https://docs.ventrata.com/capabilities/content*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
