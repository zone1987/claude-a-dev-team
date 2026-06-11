---
name: ff-octo-api
description: >
  Shopware 6.7 Plugin "FfOctoApi" — Ventrata OCTO API für Tourismus-Ticketing (GoldenTours, GoCity, RheinKurier, Demo).
  Nutze diesen Skill bei: "OctoApi", "OCTO", "Ventrata", "FfOctoApi", "GoldenTours", "GoCity", "RheinKurier",
  "ff_octo_product", "Ticket-Booking", "Availability-Check", "Booking-Reservation" — auch bei kleinen Bugfixes,
  Features oder Code-Reviews. Auch bei Fragen zu konkreten Tickets/Pässen/Touren von GoldenTours/GoCity
  (z.B. "Was kostet der London Explorer Pass?") — dann Ticket-ID aus den Referenzdateien nachschlagen und
  gezielten API-Request ausführen. Auch bei der dazugehörigen Shopware-App "FfResubmission" und dem
  "ResubmissionAppServer": "Wiedervorlage", "Resubmission", "Offline-Produkt", "RheinKurier-Produkt anlegen",
  "AppServer", "Iframe-Modul", "customProductTemplate", "manifest.xml" (siehe references/appserver-integration.md).
  Nutze context7 für aktuelle Shopware-6.7-/Symfony-Doku.
---

# FfOctoApi — Shopware 6.7 OCTO API Plugin

## Zweck

Das Plugin **FfOctoApi** (Composer: `ff/octo-api`, Version 1.0.26) integriert die **Ventrata OCTO API** (Open Connectivity for Tourism & Experiences) in Shopware 6.7. Es ermöglicht:

- Import von Tourismus-Produkten (Touren, Erlebnisse, City-Pässe) aus der OCTO API
- Automatische Preissynchronisation mit Währungsumrechnung (GBP → EUR) und Provisionsabzug
- Vollständigen Buchungs-Lebenszyklus (Reservierung → Bestätigung → Stornierung)
- Admin-UI für Produktzuweisung, Variantenerstellung und Medienimport
- Storefront-Verfügbarkeitsprüfung, Session-basierte Cart-Integration und automatische Buchungsbestätigung nach Zahlung

## Technische Voraussetzungen

- **PHP:** >= 8.3
- **Shopware:** 6.7.x (Conflict mit < 6.7 oder >= 6.8)
- **Symfony:** 7.x (via Shopware)
- **Dependency:** `symfony/uid` ^7.3
- **Namespace:** `FfOctoApi\`

## Plugin-Lokalisierung

Das Plugin heißt **immer** `FfOctoApi`. Es kann an verschiedenen Orten liegen:
- Typisch: `custom/static-plugins/FfOctoApi/`
- Alternativ: `custom/plugins/FfOctoApi/`
- Composer: Als Paket `ff/octo-api`

Suche nach dem Plugin mit: `find . -name "FfOctoApi.php" -path "*/FfOctoApi/*"` oder `grep -r "FfOctoApi" composer.json`

## Architektur-Übersicht

```
FfOctoApi/
├── src/
│   ├── FfOctoApi.php                    # Plugin-Hauptklasse
│   ├── Client/Octo/                     # Supplier-spezifische Clients
│   │   ├── GoldenToursClient.php        # London-Touren (Ventrata)
│   │   ├── GoCityClient.php             # City-Pässe (GoCity Staging)
│   │   ├── RheinKurierClient.php        # OFFLINE — Shopware-App-basiert
│   │   └── DemoClient.php               # Test-Client (Ventrata)
│   ├── Core/Api/Octo/                   # API-Client-Infrastruktur
│   │   ├── AbstractOctoApiClient.php    # Basis: HTTP, Auth, Caching, Headers
│   │   ├── OctoApiClient.php            # OCTO-Methoden (Products, Availability, Bookings)
│   │   ├── CachedOctoApiClient.php      # PSR-6 Cache-Decorator
│   │   ├── OctoApiClientRegistry.php    # Tagged-Iterator-Registry aller Clients
│   │   ├── OctoApiClientInterface.php   # Client-Interface
│   │   ├── CachedOctoApiClientInterface.php
│   │   └── OctoErrorResponse.php        # API-Fehler-Wrapper
│   ├── Controller/                      # API-Routen (Admin + Storefront)
│   │   ├── OctoProductController.php    # GET/POST /api/octo/products
│   │   ├── PropertyController.php       # POST /api/property-group/create
│   │   ├── VariantController.php        # POST /api/product-variants/create
│   │   ├── MediaController.php          # POST /api/product-media/assign
│   │   ├── PriceController.php          # POST /api/product-price/update
│   │   ├── AvailbilityController.php    # POST /octo-api/availability/*
│   │   ├── SessionController.php        # POST /octo-api/session/*
│   │   ├── CartController.php           # POST /checkout/line-item/add (Priority 100!)
│   │   └── NotificationController.php   # POST /notification/notify
│   ├── Service/                         # Business-Logic
│   │   ├── PriceService.php             # Preisberechnung & Währungsumrechnung
│   │   ├── PropertyService.php          # Property-Group-Erstellung aus API-Optionen
│   │   ├── MediaService.php             # Medien-Download & -Zuweisung
│   │   ├── SessionService.php           # Session-Datenverwaltung
│   │   ├── BookingService.php           # Buchungsreservierung mit Validierung
│   │   ├── ValidationService.php        # Constraint-basierte Validierung
│   │   ├── StateService.php             # Order-State-Machine-Übergänge
│   │   ├── CheckoutService.php          # Buchungsbestätigung/-stornierung
│   │   └── ScheduledTask/               # Geplante Aufgaben (alle 3h)
│   │       ├── OctoApiWarmCacheTask.php
│   │       ├── OctoApiWarmCacheHandler.php
│   │       ├── OctoApiPriceUpdaterTask.php
│   │       └── OctoApiPriceUpdaterHandler.php
│   ├── Subscriber/                      # Event-Listener
│   │   ├── OrderSubscriber.php          # Bestätigung/Stornierung bei Zahlungsstatus
│   │   ├── ProductSaveSubscriber.php    # Preis-Update bei Produkt-Speicherung
│   │   ├── ProductDetailSubscriber.php  # Criteria-Erweiterung für PDP
│   │   └── ProductDeleteSubscriber.php  # Orphan-Cleanup
│   ├── Core/Content/OctoProduct/        # Custom Entity
│   │   ├── OctoProductDefinition.php    # Entity: ff_octo_product
│   │   ├── OctoProductEntity.php        # uuid, identifier, product (JSON)
│   │   └── OctoProductCollection.php
│   ├── Extension/Content/Product/       # Shopware Product-Extension
│   │   └── ProductExtension.php         # ff_octo_product_id FK + ffOctoProduct Relation
│   ├── Constraint/                      # Validierung
│   │   ├── ConstraintCollectionRegistry.php
│   │   ├── ValidationResponse.php
│   │   ├── Availability/
│   │   │   ├── AvailabilityCheckConstraintCollection.php
│   │   │   └── AvailabilityCalendarConstraintCollection.php
│   │   └── Booking/
│   │       └── ReservationConstraintCollection.php
│   ├── Enum/ConstraintCollectionEnum.php
│   ├── Constant/OctoErrorCode.php
│   ├── Helper/ClassHelper.php
│   ├── Struct/MediaFile.php
│   ├── Twig/TwigFilters.php            # json_decode Filter + ff_octo_listing_price Function
│   ├── Command/
│   │   ├── LogTestCommand.php           # ff:log:test
│   │   └── PropertyGroupCleanupCommand.php  # ff:property-group:cleanup (DDEV only)
│   ├── Migration/
│   │   ├── Migration1755686022CreateOctoProductTable.php
│   │   ├── Migration1757686022CreateProductExtension.php
│   │   └── Migration1768988700AddOctoProductIdentifierIndex.php
│   └── Resources/
│       ├── config/                      # DI, Routen, Plugin-Config
│       ├── app/storefront/src/          # JS-Plugins, Services, SCSS
│       ├── app/administration/src/      # Admin-Komponenten
│       ├── views/storefront/            # Twig-Templates
│       └── snippet/                     # DE/EN Übersetzungen
└── docs/                                # Ausführliche Dokumentation
```

## Design-Patterns

### Registry Pattern
- **`OctoApiClientRegistry`** — Verwaltet alle OCTO-Clients via Tagged Iterator (`octo.api.client`)
- **`ConstraintCollectionRegistry`** — Verwaltet Validierungs-Constraints (`octo.validation.constraint-collection`)

### Client-Vererbungshierarchie
```
OctoApiClientInterface
  └── AbstractOctoApiClient        (HTTP, Auth, Headers, Config)
      └── OctoApiClient            (OCTO API Methoden)
          └── CachedOctoApiClient  (PSR-6 Caching Decorator)
              ├── GoldenToursClient
              ├── GoCityClient
              ├── RheinKurierClient (OFFLINE = true)
              └── DemoClient
```

### Online vs. Offline Clients
Ein zentrales Konzept: Clients mit `OFFLINE = true` (RheinKurier) machen **keine** API-Calls. In jedem Code-Pfad, der API-Aufrufe macht, muss geprüft werden:
```php
if ($client->isOffline()) {
    return []; // oder: Preis aus pricingFrom berechnen
}
```

**Betroffene Stellen:** `AbstractOctoApiClient::request()`, `AvailbilityController`, `CartController`, `BookingService`, `CheckoutService`, `OrderSubscriber`, `OctoApiWarmCacheHandler`, `OctoApiPriceUpdaterHandler`

> **RheinKurier ≠ rein manuell.** Die RheinKurier-Produkte werden NICHT von Hand als Shopware-Produkt
> gepflegt, sondern über den separaten **ResubmissionAppServer** (Shopware App, eigenes Repo) angelegt.
> Dieser schreibt per Admin-API ein `product` mit `ffOctoProduct`-Association (`identifier='rheinkurier'`,
> `reference='GTP2'`) in die `ff_octo_product`-Entity und ruft zur Variantenerzeugung sogar den
> FfOctoApi-`VariantController` (`/api/product-variants/create`) auf. `OFFLINE = true` heißt nur:
> zur Laufzeit kein OCTO-API-Call. Details: `references/appserver-integration.md`.

### Deterministische UUID-Generierung
Das Plugin nutzt `Symfony\Component\Uid\Uuid::fromStringToHex()` um reproduzierbare IDs zu erzeugen:
```php
// Property Group ID
Uuid::fromStringToHex("{apiProductId}-property-group")

// Property Group Option ID
Uuid::fromStringToHex("{apiProductId}-{optionReference}-{identifier}-property-group-option")

// Unique Line-Item ID (identisch in 3 Klassen!)
$unitString = implode('__', array_map(fn($u) => "{$u['id']}_q{$u['quantity']}", $units));
Uuid::fromStringToHex($productId . $unitString)
```

### Cart Collector Pattern
`OctoCartCollector` implementiert `CartProcessorInterface` + `CartCollectorInterface` mit Priority **6000** und überschreibt die Shopware-Preisberechnung für OCTO-Produkte komplett.

### Rekursionsschutz
`ProductSaveSubscriber` setzt eine Context-Extension `octo_price_update` um Endlosschleifen bei Preis-Updates zu verhindern.

## Supplier-Übersicht

| Supplier | Identifier | API | Produkte | Status |
|----------|-----------|-----|----------|--------|
| GoldenTours | `goldentours` | Ventrata (`api.ventrata.com/octo/`) | 278 (London) | Online |
| GoCity | `gocity` | GoCity Staging (`api.staging.gocity.tech/octo/`) | 49 (25 Städte) | Online |
| RheinKurier | `rheinkurier` | — | via Shopware App | **OFFLINE** |
| Demo | `demo` | Ventrata | Test-Produkte | Online |

## Konfiguration

### Plugin-Config (`FfOctoApi.config.*`)
| Key | Typ | Default | Beschreibung |
|-----|-----|---------|-------------|
| `expirationTime` | Select | 10800 | Cache-TTL in Sekunden (0/3600/7200/10800) |
| `bookingReservationTime` | Select | 30 | Reservierungsdauer in Minuten (5-60) |
| `goldentoursApiKey` | Password | — | GoldenTours API Key |
| `gocityApiKey` | Password | — | GoCity API Key |
| `demoApiKey` | Password | — | Demo API Key |
| `provisionValue` | Float | 10 | Provision in % (vom Netto abgezogen) |
| `testingEnvironment` | Bool | true | `Octo-Env: test` Header senden |

### Environment Variables (haben Vorrang vor Config)
- `OCTO_API_KEY_GOLDEN_TOURS`
- `OCTO_API_KEY_GO_CITY`
- `OCTO_API_KEY_DEMO`

### Custom Fields
- `rk_product_provision_value` — Produkt-spezifische Provision (überschreibt globale)

## OCTO API Requests (STRENG REGLEMENTIERT!)

### Sicherheitsregeln — PFLICHT!

1. **NUR die in diesem Abschnitt definierten Requests dürfen ausgeführt werden.** Keine Abwandlungen, keine eigenen Requests, keine zusätzlichen Endpunkte.
2. **Jeder Request MUSS exakt so ausgeführt werden wie hier dokumentiert** — gleiche Header, gleiche Reihenfolge, gleiche Werte.
3. **Der Header `Octo-Env: test` ist IMMER Pflicht.** Es darf NIEMALS ein Request ohne diesen Header oder mit `Octo-Env: live` ausgeführt werden.
4. **Keine eigenständigen API-Calls erfinden.** Wenn ein benötigter Request hier nicht aufgeführt ist, frage den User.

### Verfügbare Requests

#### Products auflisten — GoldenTours

```bash
curl -s -X GET "https://api.ventrata.com/octo/products" \
  -H "Authorization: Bearer $OCTO_API_KEY_GOLDEN_TOURS" \
  -H "Octo-Capabilities: octo/pricing, octo/content" \
  -H "Accept-Language: de-DE, en-GB" \
  -H "Octo-Available-Languages: de, en" \
  -H "Content-Type: application/json" \
  -H "Octo-Env: test" | jq .
```

#### Products auflisten — GoCity

```bash
curl -s -X GET "https://api.staging.gocity.tech/octo/products" \
  -H "Authorization: Bearer $OCTO_API_KEY_GO_CITY" \
  -H "Octo-Capabilities: octo/pricing, octo/content" \
  -H "Accept-Language: de-DE, en-GB" \
  -H "Octo-Available-Languages: de, en" \
  -H "Content-Type: application/json" \
  -H "Octo-Env: test" | jq .
```

#### Einzelnes Ticket abfragen — GoldenTours

Nutze diesen Request wenn Informationen zu einem bestimmten Ticket benötigt werden, statt alle Produkte zu laden. Die `<TICKET-ID>` ist die UUID des Produkts (siehe `references/api/ids/goldentours.json`).

```bash
curl -s -X GET "https://api.ventrata.com/octo/products/<TICKET-ID>" \
  -H "Authorization: Bearer $OCTO_API_KEY_GOLDEN_TOURS" \
  -H "Octo-Capabilities: octo/pricing, octo/content" \
  -H "Accept-Language: de-DE, en-GB" \
  -H "Octo-Available-Languages: de, en" \
  -H "Content-Type: application/json" \
  -H "Octo-Env: test" | jq .
```

#### Einzelnes Ticket abfragen — GoCity

Nutze diesen Request wenn Informationen zu einem bestimmten Ticket benötigt werden, statt alle Produkte zu laden. Die `<TICKET-ID>` ist die UUID des Produkts (siehe `references/api/ids/gocity.json`).

```bash
curl -s -X GET "https://api.staging.gocity.tech/octo/products/<TICKET-ID>" \
  -H "Authorization: Bearer $OCTO_API_KEY_GO_CITY" \
  -H "Octo-Capabilities: octo/pricing, octo/content" \
  -H "Accept-Language: de-DE, en-GB" \
  -H "Octo-Available-Languages: de, en" \
  -H "Content-Type: application/json" \
  -H "Octo-Env: test" | jq .
```

### Umgebungsvariablen

Die API-Keys werden über Umgebungsvariablen bereitgestellt:
- `OCTO_API_KEY_GOLDEN_TOURS` — GoldenTours API Key
- `OCTO_API_KEY_GO_CITY` — GoCity API Key

## Workflow: Ticket-Abfrage beantworten

Wenn der User eine Frage zu einem bestimmten Ticket, Pass, Tour oder Attraktion von **GoldenTours** oder **GoCity** stellt, folge diesem Ablauf:

### Schritt 1: Ticket-ID nachschlagen

Lies die entsprechende ID-Datei und suche den passenden Eintrag per Name (Fuzzy-Match auf den Suchbegriff des Users):

- **GoldenTours:** `references/api/ids/goldentours.json`
- **GoCity:** `references/api/ids/gocity.json`

Falls der User keinen Supplier nennt, durchsuche **beide** Dateien. Falls mehrere Treffer möglich sind, zeige dem User die Kandidaten und frage welches gemeint ist.

### Schritt 2: Einzelnes Ticket per API abfragen

Führe einen gezielten Request mit der gefundenen `<TICKET-ID>` aus (siehe "Einzelnes Ticket abfragen" oben). **Niemals alle Produkte laden** wenn nur ein einzelnes Ticket gefragt ist.

### Schritt 3: Response auswerten und Frage beantworten

Analysiere den API-Response und beantworte die Frage des Users. Typische Fragen und wo die Antworten im Response liegen:

| Frage | Response-Feld |
|-------|--------------|
| Preis / Was kostet...? | `options[].units[].pricingFrom[]` (retailPrice, originalPrice) |
| Optionen / Varianten | `options[]` (id, internalName, availabilityType) |
| Beschreibung / Was ist...? | `description`, `shortDescription`, `content.*.description` |
| Verfügbare Einheiten (Erwachsene, Kinder...) | `options[].units[]` (internalName, type, pricingFrom) |
| Öffnungszeiten / Wann? | `availabilityType`, `options[].availabilityLocalStartTimes` |
| Stornierungsbedingungen | `options[].cancellationCutoff`, `options[].cancellationCutoffAmount` |
| Bilder | `content.*.images[]`, `options[].content.*.images[]` |
| Treffpunkt / Wo? | `content.*.meetingPoint`, `content.*.location` |
| Dauer | `options[].durationAmount`, `options[].durationUnit` |
| Enthaltene Leistungen | `content.*.inclusions`, `content.*.exclusions` |
| Highlights | `content.*.highlights` |

### Beispiel-Ablauf

User fragt: *"Was kostet der Dubai Explorer Pass?"*

1. **Suche in** `gocity.json` → Treffer: `{"name": "Dubai Explorer Pass", "id": "ae508b91-8017-3476-be44-b652f1c0fe19"}`
2. **API-Request:**
   ```bash
   curl -s -X GET "https://api.staging.gocity.tech/octo/products/ae508b91-8017-3476-be44-b652f1c0fe19" \
     -H "Authorization: Bearer $OCTO_API_KEY_GO_CITY" \
     -H "Octo-Capabilities: octo/pricing, octo/content" \
     -H "Accept-Language: de-DE, en-GB" \
     -H "Octo-Available-Languages: de, en" \
     -H "Content-Type: application/json" \
     -H "Octo-Env: test" | jq .
   ```
3. **Auswertung:** Preise aus `options[].units[].pricingFrom[]` extrahieren und dem User aufbereitet präsentieren.

## Referenz-Dateien

Für detaillierte Implementierungsdetails lies die entsprechenden Referenzdateien:

| Thema | Datei | Wann lesen |
|-------|-------|-----------|
| Architektur & Design Patterns | `references/architecture.md` | Bei Architektur-Fragen, Verzeichnisstruktur |
| API-Client-Architektur & Methoden | `references/api-clients.md` | Bei Client-Änderungen, neuen Suppliern, API-Calls |
| Booking-Workflow (5 Phasen) | `references/booking-flow.md` | Bei Buchungs-/Checkout-Änderungen |
| Preisberechnung (statisch + dynamisch) | `references/price-calculation.md` | Bei Preis-/Währungs-/Provisions-Anpassungen |
| Session-Management & Keys | `references/session-management.md` | Bei Session-/Cart-Problemen |
| Controller & Routen | `references/controllers-routes.md` | Bei neuen/geänderten API-Endpunkten |
| Database-Entities & Schema | `references/database-entities.md` | Bei Migrationen, Entity-Änderungen |
| Storefront-JavaScript | `references/storefront-javascript.md` | Bei Frontend-Plugin-Änderungen |
| Twig-Templates | `references/twig-templates.md` | Bei Template-Anpassungen |
| Admin-Komponenten | `references/administration.md` | Bei Admin-UI-Änderungen |
| Scheduled Tasks & Subscribers | `references/scheduled-tasks-subscribers.md` | Bei Event-/Task-Anpassungen |
| Ventrata OCTO API Referenz | `references/ventrata-octo-api.md` | Bei API-Fragen, neuen Capabilities |
| GoCity API & Produkte | `references/gocity-api.md` | Bei GoCity-spezifischem Code, Datum-Format |
| GoldenTours Produktdaten | `references/goldentours-products.md` | Bei GoldenTours-Produkten, Feldern, Preisen |
| Supplier-Vergleich | `references/supplier-comparison.md` | Bei supplier-spezifischem Code |
| Konfiguration & Services | `references/configuration-services.md` | Bei Config-/DI-Änderungen |
| GoldenTours Produkt-IDs | `references/api/ids/goldentours.json` | Schnellreferenz: Name → ID aller GoldenTours-Attraktionen |
| GoCity Produkt-IDs | `references/api/ids/gocity.json` | Schnellreferenz: Name → ID aller GoCity-Attraktionen |
| ResubmissionAppServer-Integration | `references/appserver-integration.md` | Bei RheinKurier-Produktanlage, Wiedervorlagen, AppServer ↔ `ff_octo_product`, Cross-Repo-Vertrag (`VariantController`) |
| **Deep Reference (Per-Datei)** | `references/deep/_index.md` | Vollständige methodengenaue Doku JEDER Quelldatei (220 Dateien: Plugin + Tests + AppServer + Manifest). Nachschlagen, wenn exakte Signatur/Methode/Route/Fallstrick einer konkreten Datei gebraucht wird. |

## Wichtige Konventionen

### PHP-Code
- Alle Services sind `readonly` deklariert
- Konstruktoren nutzen **Property Promotion** (`private readonly ...`)
- Routen nutzen **PHP Attributes** (`#[Route(...)]`)
- Logging auf Channel `octo` (Datei: `var/log/octo-{env}.log`)
- PSR-12 Coding Standard, Psalm Level 4, Rector für Shopware 6.7

### JavaScript (Storefront)
- Plugins registriert via `PluginManager.register()` in `main.js`
- Einziger registrierter Plugin: `FfBuyBox` auf `[data-ff-buy-box]`
- Child-Plugins: DateSelect, TimeSelect, QuantitySelect, BuyBtn
- Event-Kommunikation über `document.$emitter`
- Loading-States via `StateService` mit Proxy-Pattern

### JavaScript (Administration)
- 5 API-Services registriert auf `Shopware.Service()`
- Vue-Komponente `sw-product-api-product-form` für Produktzuweisung
- Component-Overrides für `sw-product-detail` und `sw-product-detail-base`

### Twig
- OCTO-Erkennung: `product.extensions.foreignKeys.ffOctoProductId != null`
- Session-Zugriff: `app.request.session.get('octo-product-session-' ~ product.id)|json_decode`
- Custom Filter: `{{ jsonString|json_decode }}`
- Translations: `OctoApi.*` Namespace

## Workflow: Neuen Supplier hinzufügen

1. **Client-Klasse** erstellen in `src/Client/Octo/` — `CachedOctoApiClient` erweitern
2. **Konstanten** definieren: `IDENTIFIER`, `SUPPLIER_ID`, `DESTINATION_ID`, `BASE_URL`, `COLOR`, `API_KEY_CONFIG_KEY`, `API_ENV_KEY`
3. **Service registrieren** in `clients.xml` mit Tag `octo.api.client`
4. **API-Key-Config** hinzufügen in `config.xml`
5. **Snippets** für Admin-Supplier-Namen ergänzen
6. Bei **OFFLINE**: Alle Offline-Checks in betroffenen Klassen implementieren

## Workflow: Neuen API-Endpunkt hinzufügen

1. **Controller** in `src/Controller/` erstellen oder erweitern
2. **Route-Attribute** definieren: `#[Route(path: '...', name: '...', methods: ['POST'], defaults: ['_routeScope' => ['storefront'|'api']])]`
3. **Controller in** `controllers.xml` registrieren (mit Dependencies)
4. **Constraint Collection** erstellen wenn Validierung nötig (Tag: `octo.validation.constraint-collection`)
5. Bei Storefront-Routen: `XmlHttpRequest` und `_httpCache` Defaults beachten

## Code-Qualität

```bash
# Alle Quality-Checks
composer quality-gate     # psalm + ecs + phpcs
composer all-checks       # psalm + ecs + phpcs + rector

# Einzeln
composer psalm            # Statische Analyse (Level 4)
composer ecs              # Easy Coding Standard
composer phpcs            # PHP CodeSniffer (PSR-12)
composer rector           # Code-Modernisierung (Shopware 6.7)
```

## Skill aktuell halten (PFLICHT!)

Wenn du Anpassungen am FfOctoApi-Plugin vornimmst, aktualisiere **immer** auch die entsprechenden Skill-Referenzdateien unter `~/.claude/skills/ff-octo-api/references/`. Der Skill muss jederzeit den aktuellen Stand des Plugins widerspiegeln.

### Was aktualisiert werden muss:

- **Neue Klasse/Service/Controller hinzugefügt:** Aktualisiere die passende Referenzdatei (z.B. `controllers-routes.md`, `api-clients.md`) und `architecture.md`
- **Neue Route:** Aktualisiere `controllers-routes.md`
- **Neuer Subscriber/Event:** Aktualisiere `scheduled-tasks-subscribers.md`
- **Neuer Supplier/Client:** Aktualisiere `api-clients.md`, `supplier-comparison.md`, `architecture.md`
- **Migration/Entity-Änderung:** Aktualisiere `database-entities.md`
- **Twig-Template-Änderung:** Aktualisiere `twig-templates.md`
- **JavaScript-Plugin-Änderung:** Aktualisiere `storefront-javascript.md`
- **Admin-Komponente geändert:** Aktualisiere `administration.md`
- **Preis-/Buchungslogik geändert:** Aktualisiere `price-calculation.md` und/oder `booking-flow.md`
- **Konfiguration geändert:** Aktualisiere `configuration-services.md`
- **Session-Keys geändert:** Aktualisiere `session-management.md`

### Wie aktualisieren:

1. Nimm die Änderung am Plugin vor
2. Identifiziere die betroffene(n) Referenzdatei(en)
3. Aktualisiere exakte Methodensignaturen, Parameter, Routen, Events etc.
4. Bei neuen Dateien/Klassen: Füge sie auch in `architecture.md` ein
5. Bei grundlegend neuer Funktionalität: Erstelle ggf. eine neue Referenzdatei und füge sie in die Tabelle oben ein

## Context7-Nutzung

Nutze context7 für aktuelle Dokumentation zu:
- **Shopware 6.7**: Entity-Definitionen, Cart-Processing, Scheduled Tasks, Admin-Komponenten
- **Symfony 7.x**: Routing-Attribute, Validator-Constraints, HTTP-Client, Cache
- **Ventrata OCTO API**: Endpoint-Referenz, Capabilities, Booking-Status

```
# Beispiel context7-Queries:
- "shopware entity definition custom entity"
- "shopware cart processor interface"  
- "shopware scheduled task handler"
- "symfony validator constraint collection"
- "symfony http client options"
```