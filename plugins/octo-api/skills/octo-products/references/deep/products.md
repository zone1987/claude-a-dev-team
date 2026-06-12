# OCTO API — Vollständiges Product / Option / Unit Schema

## Basis-URL

```
https://api.ventrata.com/octo
```

---

## Endpunkte

### GET /products/

Gibt die Liste aller Produkte des Suppliers zurück.

```http
GET https://api.ventrata.com/octo/products/
Authorization: Bearer {api_key}
Octo-Capabilities: octo/pricing,octo/content
Accept-Language: de
```

**Response:** `200 Array<Product>`

**Fehler (400):**
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

---

### GET /products/{id}

Gibt ein einzelnes Produkt zurück.

```http
GET https://api.ventrata.com/octo/products/{productId}
Authorization: Bearer {api_key}
Octo-Capabilities: octo/pricing,octo/content
```

**Path-Parameter:** `id` — Die Produkt-ID

**Response:** `200 Product`

**Fehler (400):**
- `ErrorInvalidProductId`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

---

## Product-Schema

```typescript
type Product = {
  // --- Pflichtfelder (immer vorhanden) ---
  id: string;                        // Eindeutiger Identifier für das Produkt
  internalName: string;              // Interner Name (für Supplier-seitig)
  reference: string | null;          // Optionaler interner Referenzcode
  locale: string;                    // Primäre Sprache (IETF BCP 47, z.B. "en-US")
  timeZone?: string;                 // IANA Zeitzone (z.B. "America/New_York")
  allowFreesale: boolean;            // false = availabilityId für Buchung nötig
  instantConfirmation: boolean;      // Sofortige Ticket-Lieferung nach Bestätigung
  instantDelivery: boolean;          // Reseller kann sofortige Lieferung erwarten
  availabilityRequired: boolean;     // availabilityId für Buchung erforderlich
  availabilityType: AvailabilityType; // START_TIME | OPENING_HOURS
  deliveryFormats: DeliveryFormat[]; // QRCODE, CODE128, AZTECCODE, PDF_URL, PKPASS_URL
  deliveryMethods: DeliveryMethod[]; // TICKET | VOUCHER
  redemptionMethod: RedemptionMethod; // DIGITAL | MANIFEST | PRINT
  options: Option[];                 // Mind. eine Option (Pflicht)

  // --- Pricing-Felder (nur mit octo/pricing Capability) ---
  defaultCurrency?: string;          // Standard-Währung (ISO 4217)
  availableCurrencies?: string[];    // Alle akzeptierten Währungen
  pricingPer?: PricingPer;           // BOOKING | UNIT

  // --- Content-Felder (nur mit octo/content Capability) ---
  title?: string;                    // Öffentlicher, kundenorientierter Produktname
  shortDescription?: string | null;  // Kurze Beschreibung
  description?: string | null;       // Ausführliche Beschreibung
  features?: Feature[];              // Merkmale (Inklusionen, Exklusionen, Highlights, etc.)
  faqs?: Faq[];                      // Häufig gestellte Fragen
  media?: Media[];                   // Bilder, Videos
  locations?: Location[];            // Geografische Standorte
  categoryLabels?: CategoryLabel[];  // Kategorie-Labels
  durationMinutesFrom?: number;      // Min. Dauer in Minuten
  durationMinutesTo?: number | null; // Max. Dauer (null = exakte Dauer)
  commentary?: Commentary[];         // Kommentar-Optionen
};
```

### AvailabilityType Enum

```typescript
enum AvailabilityType {
  START_TIME = 'START_TIME',       // Feste Abfahrtszeiten (z.B. Walking Tour)
  OPENING_HOURS = 'OPENING_HOURS', // Öffnungszeiten (z.B. Museumsticket)
}
```

### DeliveryFormat Enum

```typescript
enum DeliveryFormat {
  PDF_URL = 'PDF_URL',         // Link zu PDF mit vollständigen Ticket-Details
  QRCODE = 'QRCODE',           // QR-Code für Scan-Einlass
  CODE128 = 'CODE128',         // Linearer Barcode (Handel/Ticketing)
  PKPASS_URL = 'PKPASS_URL',   // Apple Wallet / Passbook URL
  AZTECCODE = 'AZTECCODE',     // 2D-Barcode (kompakt, Transport/Events)
}
```

### DeliveryMethod Enum

```typescript
enum DeliveryMethod {
  VOUCHER = 'VOUCHER', // Ein Dokument für die gesamte Buchung
  TICKET = 'TICKET',   // Einzeldokument pro Unit Item
}
```

### RedemptionMethod Enum

```typescript
enum RedemptionMethod {
  DIGITAL = 'DIGITAL',   // Digitales oder gedrucktes Ticket vorzeigen
  MANIFEST = 'MANIFEST', // Name/Referenz gegen Manifest prüfen (kein Ticket nötig)
  PRINT = 'PRINT',       // Physisches gedrucktes Ticket zwingend erforderlich
}
```

### PricingPer Enum

```typescript
enum PricingPer {
  BOOKING = 'BOOKING', // Preis pro Buchung (z.B. Privatcharterprodukte)
  UNIT = 'UNIT',       // Preis pro Unit (Standard)
}
```

---

## Option-Schema

```typescript
type Option = {
  // --- Pflichtfelder ---
  id: string;                           // Eindeutiger Identifier
  default: boolean;                     // true = erste Auswahl in Customer-Interfaces
  internalName: string;                 // Interner Name (Supplier-seitig)
  reference: string | null;             // Optionaler interner Referenzcode
  availabilityLocalStartTimes: string[]; // Alle möglichen Startzeiten (z.B. ["09:00","14:00"])
  cancellationCutoff: string;           // Textbeschreibung der Stornierungsrichtlinie
  cancellationCutoffAmount: number;     // Numerischer Cutoff-Wert
  cancellationCutoffUnit: DurationUnit; // minute | hour | day
  requiredContactFields: ContactField[]; // Pflichtfelder für Lead-Traveler
  restrictions: OptionRestrictions;     // Min/Max Units
  units: Unit[];                        // Ticket-Typen

  // --- Pricing-Felder (nur mit octo/pricing) ---
  pricingFrom?: Pricing[];
  pricing?: Pricing[];

  // --- Content-Felder (nur mit octo/content) ---
  title?: string;
  shortDescription?: string | null;
  description?: string | null;
  features?: Feature[];
  faqs?: Faq[];
  media?: Media[];
  locations?: Location[];
  categoryLabels?: CategoryLabel[];
  durationMinutesFrom?: number;
  durationMinutesTo?: number | null;
  commentary?: Commentary[];
};

type OptionRestrictions = {
  minUnits: number | null; // Min. Anzahl Units pro Buchung (null = kein Minimum)
  maxUnits: number | null; // Max. Anzahl Units pro Buchung (null = kein Maximum)
};
```

### DurationUnit Enum (für cancellationCutoffUnit)

```typescript
enum DurationUnit {
  MINUTE = 'minute',
  HOUR = 'hour',
  DAY = 'day',
}
```

---

## Unit-Schema

```typescript
type Unit = {
  // --- Pflichtfelder ---
  id: string;                           // Eindeutiger Identifier (im Scope der Option)
  internalName: string;                 // Interner Name (nicht für Kunden sichtbar)
  reference: string | null;             // Optionaler interner Referenzcode
  type: UnitType;                       // ADULT, YOUTH, CHILD, INFANT, FAMILY, SENIOR, STUDENT, MILITARY, OTHER
  restrictions: UnitRestrictions;       // Alter, Anzahl, Höhe, Gewicht, etc.
  requiredContactFields: ContactField[]; // Pflicht-Kontaktfelder pro Ticket

  // --- Pricing-Felder (nur mit octo/pricing) ---
  pricingFrom?: Pricing[];
  pricing?: Pricing[];

  // --- Content-Felder (nur mit octo/content) ---
  title?: string | null;           // Öffentlicher Name (z.B. "Erwachsener")
  shortDescription?: string;       // Kurze Beschreibung
  features?: Feature[];            // Merkmale
};
```

### UnitType Enum

```typescript
enum UnitType {
  ADULT = 'ADULT',
  YOUTH = 'YOUTH',
  CHILD = 'CHILD',
  INFANT = 'INFANT',
  FAMILY = 'FAMILY',
  SENIOR = 'SENIOR',
  STUDENT = 'STUDENT',
  MILITARY = 'MILITARY',
  OTHER = 'OTHER',
  // TRAVELLER kann als Ersatz für ADULT, CHILD, INFANT, YOUTH, STUDENT, MILITARY, SENIOR verwendet werden
}
```

### UnitRestrictions-Schema

```typescript
type UnitRestrictions = {
  minAge: number;               // Mindestalter für den Kauf
  maxAge: number;               // Maximalalter für den Kauf
  idRequired: boolean;          // Ausweis erforderlich (z.B. Studentenausweis)
  minQuantity: number | null;   // Min. Anzahl pro Buchung (null = kein Minimum)
  maxQuantity: number | null;   // Max. Anzahl pro Buchung (null = unbegrenzt)
  paxCount: number;             // Anzahl Personen pro Unit (z.B. 1 Familienticket = 4)
  accompaniedBy: string[];      // Unit-IDs, die mitgebucht werden müssen
  minHeight?: number;           // Mindestgröße (z.B. Vergnügungspark-Fahrten)
  maxHeight?: number;           // Maximalgröße
  heightUnit?: string;          // "cm" oder "in"
  minWeight?: number;           // Mindestgewicht
  maxWeight?: number;           // Maximalgewicht
  weightUnit?: string;          // "kg" oder "lb"
};
```

### ContactField Enum

```typescript
enum ContactField {
  FIRST_NAME = 'firstName',
  LAST_NAME = 'lastName',
  EMAIL_ADDRESS = 'emailAddress',
  PHONE_NUMBER = 'phoneNumber',
  COUNTRY = 'country',
  NOTES = 'notes',
  LOCALES = 'locales',
  ALLOW_MARKETING = 'allowMarketing',
  POSTAL_CODE = 'postalCode',
}
```

---

## Pricing-Schema (mit octo/pricing Capability)

```typescript
type Pricing = {
  original: number;          // Marketingpreis (Strike-Through-Preis)
  retail: number;            // Empfohlener Verkaufspreis (inkl. Steuern und Gebühren)
  net: number | null;        // Großhandelspreis für Reseller
  currency: string;          // ISO 4217 Währungscode (z.B. "USD", "EUR")
  currencyPrecision: number; // Dezimalstellen (z.B. 2 für USD, 0 für JPY)
  includedTaxes: Tax[];      // Im Preis enthaltene Steuern
};

// Preis-Umrechnung:
// actualPrice = price / Math.pow(10, currencyPrecision)
// Beispiel: USD: 4500 / 10^2 = 45.00 USD
// Beispiel: JPY: 4500 / 10^0 = 4500 JPY

type Tax = {
  name: string;         // Steuerbezeichnung (z.B. "VAT", "City Tax")
  retail: number;       // Steueranteil am Einzelhandelspreis
  original: number;     // Steueranteil am Originalpreis
  net: number | null;   // Steueranteil am Nettopreis
};

type PricingUnit = Pricing & {
  unitId: string;       // Unit-ID zu der dieser Preis gehört
};
```

---

## Content-Schema-Typen (mit octo/content Capability)

### Feature-Schema

```typescript
type Feature = {
  shortDescription: string | null;
  type: FeatureType;
};

enum FeatureType {
  INCLUSION = 'INCLUSION',                       // Was ist inbegriffen
  EXCLUSION = 'EXCLUSION',                       // Was ist NICHT inbegriffen
  HIGHLIGHT = 'HIGHLIGHT',                       // Verkaufsargumente/Alleinstellungsmerkmale
  PREBOOKING_INFORMATION = 'PREBOOKING_INFORMATION', // Infos vor der Buchung
  PREARRIVAL_INFORMATION = 'PREARRIVAL_INFORMATION', // Infos vor der Ankunft
  REDEMPTION_INSTRUCTION = 'REDEMPTION_INSTRUCTION', // Einlöseanweisungen
  ACCESSIBILITY_INFORMATION = 'ACCESSIBILITY_INFORMATION', // Barrierefreiheit
  ADDITIONAL_INFORMATION = 'ADDITIONAL_INFORMATION', // Sonstige Zusatzinfos
  BOOKING_TERM = 'BOOKING_TERM',                 // Buchungsbedingungen
  CANCELLATION_TERM = 'CANCELLATION_TERM',       // Stornierungsbedingungen
}
```

### FAQ-Schema

```typescript
type Faq = {
  question: string; // Die Frage
  answer: string;   // Die Antwort
};
```

### Media-Schema

```typescript
type Media = {
  src: string;               // Stabile, öffentlich zugängliche URL
  type: MediaType;           // image/jpeg, image/png, video/mp4, etc.
  rel: MediaRel;             // LOGO | COVER | GALLERY
  title: string | null;
  caption: string | null;
  copyright: string | null;
};

enum MediaType {
  IMAGE_JPEG = 'image/jpeg',
  IMAGE_PNG = 'image/png',
  VIDEO_MP4 = 'video/mp4',
  VIDEO_AVI = 'video/avi',
  EXTERNAL_YOUTUBE = 'external/youtube',
  EXTERNAL_VIMEO = 'external/vimeo',
}

enum MediaRel {
  LOGO = 'LOGO',
  COVER = 'COVER',
  GALLERY = 'GALLERY',
}
```

### Location-Schema

```typescript
type Location = {
  title: string | null;
  shortDescription: string | null;
  types: LocationType[];
  minutesTo: number | null;    // Reisezeit zur nächsten Location in Minuten
  minutesAt: number | null;    // Aufenthaltsdauer in Minuten
  place: Place;
};

enum LocationType {
  START = 'START',
  ITINERARY_ITEM = 'ITINERARY_ITEM',
  POINT_OF_INTEREST = 'POINT_OF_INTEREST',
  ADMISSION_INCLUDED = 'ADMISSION_INCLUDED',
  END = 'END',
  REDEMPTION = 'REDEMPTION',
}

type Place = {
  latitude: number;
  longitude: number;
  postalAddress: PostalAddress;
  identifiers: Identifiers; // googlePlaceId, applePlaceId, tripadvisorLocationId, etc.
  sameAs: string[];         // URLs zu Web-Seiten oder Social-Media-Profilen
};

type PostalAddress = {
  streetAddress: string | null;
  addressLocality: string | null;  // Stadt
  addressRegion: string | null;    // Bundesland/Provinz
  postalCode: string | null;
  addressCountry: string | null;
  postOfficeBoxNumber: string | null;
};

type Identifiers = {
  googlePlaceId: string | null;
  applePlaceId: string | null;
  tripadvisorLocationId: string | null;
  yelpPlaceId: string | null;
  facebookPlaceId: string | null;
  foursquarePlaceId: string | null;
  baiduPlaceId: string | null;
  amapPlaceId: string | null;
};
```

### Commentary-Schema

```typescript
type Commentary = {
  format: CommentaryFormat; // Kommentarformat
  language: string;         // IETF BCP 47 Sprachcode
};

enum CommentaryFormat {
  IN_PERSON = 'IN_PERSON',       // Live-Kommentar durch Guide
  RECORDED_AUDIO = 'RECORDED_AUDIO', // Voraufgezeichnetes Audio
  WRITTEN = 'WRITTEN',           // Schriftliches Material
  OTHER = 'OTHER',               // Andere Formate
}
```

### CategoryLabel Enum

```typescript
enum CategoryLabel {
  MULTI_DAY = 'multi-day',
  CITY_CARDS = 'city-cards',
  ADULTS_ONLY = 'adults-only',
  ANIMALS = 'animals',
  AUDIO_GUIDE = 'audio-guide',
  BEACHES = 'beaches',
  BIKE_TOURS = 'bike-tours',
  BOAT_TOURS = 'boat-tours',
  CLASSES = 'classes',
  DAY_TRIPS = 'day-trips',
  FAMILY_FRIENDLY = 'family-friendly',
  FAST_TRACK = 'fast-track',
  FOOD = 'food',
  GUIDED_TOURS = 'guided-tours',
  HISTORY = 'history',
  HOP_ON_HOP_OFF = 'hop-on-hop-off',
  LITERATURE = 'literature',
  LIVE_MUSIC = 'live-music',
  MUSEUMS = 'museums',
  NIGHTLIFE = 'nightlife',
  OUTDOORS = 'outdoors',
  PRIVATE_TOURS = 'private-tours',
  ROMANTIC = 'romantic',
  RECURRING_EVENTS = 'recurring-events',
  SELF_GUIDED = 'self-guided',
  SMALL_GROUP_TOURS = 'small-group-tours',
  SPORTS = 'sports',
  THEME_PARKS = 'theme-parks',
  WALKING_TOURS = 'walking-tours',
  WHEELCHAIR_ACCESSIBLE = 'wheelchair-accessible',
  ACCOMMODATION_INCLUDED = 'accommodation-included',
  TRIP_DIFFICULTY_EASY = 'trip-difficulty-easy',
  TRIP_DIFFICULTY_MEDIUM = 'trip-difficulty-medium',
  TRIP_DIFFICULTY_HARD = 'trip-difficulty-hard',
}
```

---

## Supplier-Schema

```typescript
type Supplier = {
  id: string;
  name: string;
  endpoint: string;      // Basis-URL (ohne abschließenden Slash)
  contact: SupplierContact;
  shortDescription?: string | null; // nur mit octo/content
  media?: Media[];                  // nur mit octo/content
};

type SupplierContact = {
  website: string | null;
  email: string | null;
  telephone: string | null; // E.164-Format
  address: string | null;
};
```

### GET /supplier/

```http
GET https://api.ventrata.com/octo/supplier/
Authorization: Bearer {api_key}
Octo-Capabilities: octo/content
```

**Response:** `200 Supplier`

---

## Praktische Hinweise

1. **Self-Service Mapping:** Ventrata bietet eine Mapping-Capability (`octo/mappings`), die den Aufwand der Produktzuordnung erheblich reduziert
2. **Importstrategie:** Entweder bestehende Produktdatenbank mappen oder Produktliste direkt importieren
3. **Features werden wiederholt:** Features und FAQs sind absichtlich auf Product- UND Option-Ebene vorhanden; Reseller müssen beide Ebenen für die Kundenanzeige kombinieren
4. **Media werden wiederholt:** Medien sind auf Product- und Option-Ebene; Reseller sollten beide Ebenen zusammenführen

---

**Quellen:**
- https://docs.ventrata.com/octo-core/products
- https://github.com/octotravel/octo-types (TypeScript-Typdefinitionen)
