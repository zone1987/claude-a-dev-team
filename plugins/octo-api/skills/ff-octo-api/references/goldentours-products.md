# GoldenTours Produktdaten

> **Produktdaten (komprimiert):** [api/ids/goldentours.json](api/ids/goldentours.json) (6.2 MB, 278 Produkte)
> **Ventrata API Docs:** https://docs.ventrata.com/

## Übersicht

GoldenTours ist der größte Supplier im System mit **278 Produkten**, die alle von London aus operieren. Die Daten kommen über die Ventrata OCTO API (`https://api.ventrata.com/octo/`).

## Produkt-Kategorien (Tags)

| Tag | Beschreibung |
|---|---|
| Afternoon Tea | Nachmittagstee-Bus-Touren |
| Attractions | Einzelne Attraktionen und Eintrittskarten |
| Christmas Lights | Weihnachtsbeleuchtungs-Touren (saisonal) |
| Coach Tours | Bustouren und Tagesausflüge |
| Golden Pass | All-In-One Sightseeing-Ticket |
| London by Night | Abend-/Nachttouren |
| Open Top Bus Tours | Hop-on Hop-off Sightseeing |
| Open Top Packages | Bus-Tour-Pakete mit Attraktionen |
| Private | Privattouren (Black Cab, Walking) |
| Rail Tours | Zugausflüge |
| Seasonal Tours | Saisonale Touren (Weihnachten, Silvester) |
| WB Studio Tour | Harry Potter Warner Bros. Studio |
| WB Studio Tour - Transport only | Nur Transport zur WB Studio |
| WB Studio Tour Packages | Studio-Tour-Pakete |
| Walking Tours | Geführte Spaziergänge |

## Produkt-Struktur (Ventrata/GoldenTours)

GoldenTours-Produkte haben deutlich mehr Felder als GoCity-Produkte:

### Zusätzliche Felder (die GoCity nicht hat)

| Feld | Typ | Beschreibung |
|---|---|---|
| `title` | string | Lokalisierter Produktname |
| `country` | string | ISO-Code (z.B. "GB") |
| `location` | string | Stadt (z.B. "London") |
| `address` | string | Vollständige Adresse |
| `latitude` / `longitude` | number | Koordinaten |
| `googlePlaceId` | string | Google Maps Place ID |
| `subtitle` | string | Kurzbeschreibung |
| `tagline` | string | Marketing-Slogan |
| `keywords` | array | SEO-Keywords |
| `shortDescription` | string | Kurze Beschreibung |
| `description` | string (HTML) | Ausführliche Beschreibung |
| `highlights` | array | Highlights als Aufzählung |
| `alert` | string | Aktuelle Hinweise |
| `inclusions` | array | Was ist enthalten |
| `exclusions` | array | Was ist nicht enthalten |
| `bookingTerms` | string | Buchungsbedingungen |
| `privacyTerms` | string (HTML) | Datenschutz |
| `redemptionInstructions` | string | Einlöseanweisungen |
| `usageInstructions` | string | Nutzungshinweise |
| `cancellationPolicy` | string | Stornierungsbedingungen |
| `faqs` | array | FAQ (Frage-Antwort-Paare) |
| `coverImageUrl` | string | Titelbild-URL (Cloudinary CDN) |
| `bannerImageUrl` | string | Banner-URL |
| `videoUrl` | string | Video-URL |
| `galleryImages` | array | Bildergalerie (3-10 Bilder) |
| `brand` | object | Branding (Logo, Farben, Kontakt) |
| `destination` | object | Zielort-Details |
| `categories` | array | Kategorien |
| `operator` | object | Betreiber (z.B. "Merlin Entertainments") |
| `tags` | array | Kategorie-Tags |

### Options-Zusatzfelder (nur GoldenTours)

| Feld | Typ | Beschreibung |
|---|---|---|
| `availabilityLocalDateStart` | date | Frühestes Buchungsdatum |
| `availabilityLocalDateEnd` | date | Spätestes Buchungsdatum |
| `availabilityCutoff` | string | Buchungsschluss vor Start |
| `availabilityNotice` | string | Vorlaufzeit-Hinweis |
| `title` | string | Lokalisierter Option-Name |
| `subtitle` | string | Option-Untertitel |
| `language` | string | Sprache der Option |
| `shortDescription` | string | Kurzbeschreibung |
| `duration` | string | Dauer-Beschreibung |
| `durationAmount` / `durationUnit` | int/string | Dauer in Einheiten |
| `coverImageUrl` | string | Option-spezifisches Bild |
| `meetingPoint` | string | Treffpunkt-Beschreibung |
| `meetingPointCoordinates` | array | Treffpunkt-Koordinaten |
| `meetingPointLatitude` / `meetingPointLongitude` | number | Treffpunkt Lat/Lon |
| `meetingPointDirections` | string | Anfahrtsbeschreibung |
| `itinerary` | string | Reiseroute |
| `fromPoint` / `toPoint` | string | Start-/Endpunkt |

### Unit-Zusatzfelder (nur GoldenTours)

| Feld | Typ | Beschreibung |
|---|---|---|
| `title` | string | Lokalisierter Name (z.B. "Erwachsene") |
| `titlePlural` | string | Plural (z.B. "Erwachsene") |
| `subtitle` | string | Altersbeschreibung (z.B. "18+ Jahre") |
| `accompaniedByRatio` | int | Begleitverhältnis |
| `accompaniedByRatioDenominator` | int | Nenner des Begleitverhältnisses |
| `notAccompaniedBy` | array | Nicht-erlaubte Begleitung |

## Verfügbarkeitstypen

| Typ | Beschreibung | Beispiel |
|---|---|---|
| `START_TIME` | Kunde wählt feste Startzeit | Die meisten Touren und Attraktionen |
| `OPENING_HOURS` | Kunde wählt Zeitfenster innerhalb Öffnungszeiten | Museen, Hop-on Hop-off |

## Unit-Typen

GoldenTours verwendet **8 verschiedene Unit-Typen** (vs. 2 bei GoCity):

| Typ | Beschreibung | Typisches Alter |
|---|---|---|
| `ADULT` | Erwachsener | 18+ (variiert) |
| `CHILD` | Kind | 3-17 (variiert) |
| `YOUTH` | Jugendlicher | 12-17 (variiert) |
| `SENIOR` | Senior | 65+ |
| `INFANT` | Kleinkind | 0-2/3 |
| `FAMILY` | Familie (Gruppenpreis) | - |
| `STUDENT` | Student | - |
| `OTHER` | Sonstiges (mit eigenem Titel) | - |

## Preise

### Währungen
Alle Produkte bieten Preise in **EUR und GBP** (Dual-Currency):

```json
"pricingFrom": [
  { "original": 3500, "retail": 3500, "net": 3220, "currency": "EUR", "currencyPrecision": 2 },
  { "original": 3000, "retail": 3000, "net": 2760, "currency": "GBP", "currencyPrecision": 2 }
]
```

### Preisspannen (GBP)

| Kategorie | Preisspanne | Beispiele |
|---|---|---|
| Günstige Attraktionen | £4 – £20 | Wellington Arch, HMS Belfast |
| Standard-Attraktionen | £8 – £35 | London Eye, Museen, Walking Tours |
| Tagestouren | £40 – £120 | Stonehenge, Windsor, Bath |
| Premium-Touren | £100 – £250 | Luxury Tours, Multi-Stop Tours |
| Privattouren | £200 – £1.600 | Black Cab Tours, Private Paris Tour |

### Preisstruktur im Plugin

Das Plugin verwendet bevorzugt den **GBP-Preis** und konvertiert ihn nach EUR:
```php
// PriceService.php
$gbpPriceIndex = array_search('GBP', array_column($pricings, 'currency'));
$pricing = $gbpPriceIndex !== false ? $pricings[$gbpPriceIndex] : $pricings[0];
```

## Delivery-Formate

| Format | Beschreibung |
|---|---|
| `QRCODE` | QR-Code direkt |
| `PNG_URL` | QR-Code als Bild-URL |
| `PKPASS_URL` | Apple Wallet |
| `GOOGLE_WALLET_URL` | Google Wallet |
| `PDF_URL` | PDF-Ticket |
| `AZTECCODE` | Aztec-Barcode (selten) |

## Stornierungsbedingungen

Variieren pro Produkt/Option:
- `0 hours` – Bis kurz vor Beginn stornierbar
- `24 hours` – 24 Stunden vorher
- `48 hours` / `2 days` – 2 Tage vorher
- `7 days` – 1 Woche vorher

## Lokalisierung

GoldenTours-Produkte werden mit `locale: "de"` (Deutsch) ausgeliefert, aber mit gemischt deutsch/englischen Inhalten:
- Produktnamen teilweise deutsch (z.B. "Hop-on-Hop-off-Sightseeing-Tour durch London")
- Optionen und Units meist englisch
- Unit-Titel lokalisiert (z.B. "Erwachsene" statt "Adult", "18+ Jahre")
- Das `language`-Feld auf Option-Ebene ist meist `"en"`

## Bilder

Alle Bilder werden über Cloudinary CDN gehostet:
```
https://cdn.ventrata.com/image/...
```

Bildformate:
- `coverImageUrl` – Hauptbild (pro Produkt und pro Option)
- `galleryImages` – Array mit 3-10 Bildern, jeweils mit `url`, `title`, `caption`
- `bannerImageUrl` – Banner-Bild

## Settlement-Methoden

| Methode | Beschreibung |
|---|---|
| `DIRECT` | Direkte Abrechnung |
| `VOUCHER` | Gutschein-basiert |
| `WHOLESALE` | Großhandels-Abrechnung |

## Bekannte Produktbeispiele

### Hop-on Hop-off Bus Tours
- Mehrere Varianten (24h, 48h, 72h)
- Verschiedene Combo-Pakete (+ London Eye, + Tower, + Westminster Abbey, + Madame Tussauds)
- Optionen: Peak/Off-Peak/Standard mit unterschiedlichen Preisen und Zeiten

### Harry Potter Warner Bros. Studio
- Studio Tour mit Rücktransport
- Nur Transport
- Studio Tour + Hop-on Hop-off Combo

### Privattouren (Black Cab)
- Sightseeing, Harry Potter, Rock'n'Roll, Night Tour, Beatles
- Alle mit Hotel Pickup
- Höchste Preiskategorie

### Tagesausflüge
- Stonehenge, Bath, Windsor, Oxford, Cambridge
- Verschiedene Kombinationen
- Mit/ohne Lunch
- Luxus-Varianten
