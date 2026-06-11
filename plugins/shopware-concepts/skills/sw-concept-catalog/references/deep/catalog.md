# Shopware Produktkatalog — Vollständige Konzept-Doku

Quellen: `concepts/commerce/catalog/index.md`, `products.md`, `categories.md`, `sales-channels.md`

---

## Produkte (concepts/commerce/catalog/products.md)

Produkte sind verkäufliche Entitäten (physisch und digital) im Shop.

### Produktstruktur

- **Produktdetails** — allgemeine Informationen (Titel, ID, Hersteller, Preis, etc.)
- **Produkteigenschaften** — Property Groups und Options; in Tabelle auf Produktdetailseite, Listings, Filterung
- **Kategorien** — hierarchischer Baum; Produkt kann in mehreren Kategorien sein
- **Verpackungsmaße** — Gewicht (kg), Dimensionen (mm); ab 6.7.1.0 konfigurierbare Anzeigeeinheiten

### Datenbankstruktur (ERD-Kernrelationen)

- `Product` 1:M `ProductCategory` M:1 `Category`
- `Product` 1:M `ProductOption` M:1 `PropertyGroupOption` M:1 `PropertyGroup`

### Produktvarianten

- **Selbst-referenzierendes Entity** — Parent-Child-Beziehung (`parent_id`)
- Varianten erben Felder und Associations vom Parent (DAL-Vererbungsmechanismus)
- Kategorien ohne eigene Zuweisung → Eltern-Produkt wird verwendet

### Properties vs. Options — wichtiger Unterschied!

| | Properties | Options |
|---|---|---|
| **Bedeutung** | Fakten über das Produkt | Variantenbestimmende Merkmale |
| **Beispiele** | Produktserie, Waschanleitung, Herkunftsland | Größe, Farbe, Behältervolumen |
| **Variantenbildend?** | Nein | **Ja** |
| **DB-Relation** | product → property_group_option | product → property_group_option |

Beide nutzen dieselbe Datenbankrelation, aber nur **Options** konstituieren Varianten.

### Configurator

Bei Laden eines Variantenprodukts über Store API liefert Shopware ein **Configurator-Objekt**
mit allen Property Groups und den entsprechenden Varianten. Storefront und Composable Frontends
nutzen dieses Objekt für die Variantenauswahl-UI.

---

## Kategorien (concepts/commerce/catalog/categories.md)

Kategorien organisieren Produkte, steuern Storefront-Navigation und definieren SEO-relevante URLs.
Der gesamte Katalog lebt in **einem Kategoriebaum**; jeder Sales Channel wählt Einstiegspunkte.

### Category-Modell

- `parentId`, `path`, `level` — für Breadcrumbs, Vererbung, effizientes Traversieren
- **Flags**: `active`, `visible`, `hideInNavigation` — steuern Rendering unabhängig
- **Typen**:
  - `page` — reguläre Kategorie (Listing oder Landing Page)
  - `folder` — Strukturierungselement; wird nicht als Seite gerendert
  - `link` — Redirect zu externer URL oder internem Link

### Entity-Assoziationen

```
CATEGORY ←→ CATEGORY_TRANSLATION (Übersetzungen)
CATEGORY → CMS_PAGE (Layout-Referenz, vererbbar)
CATEGORY → PRODUCT_STREAM (dynamische Produktzuweisung)
CATEGORY ←→ PRODUCT (explizite Produkt-Links via product_category)
SALES_CHANNEL → CATEGORY (navigation/footer/service Einstiegspunkte)
CATEGORY → SEO_URL (generierte URLs per Category + Sales Channel)
```

### Sales Channel Navigation

Jeder Sales Channel definiert `navigation`, `footer`, `service`-Einstiegskategorien.
Storefront baut Menüs aus den Kind-Kategorien dieser Einstiegspunkte.

Store-API-Endpunkte:
- `GET /store-api/navigation/{activeId}/{rootId}` — hierarchische Menüs
- `GET /store-api/category/{navigationId}` — Kategorie-Details inkl. CMS-Layout-Daten

Navigation-Responses sind gecacht. Cache-Anpassung via `NavigationRouteCacheKeyEvent` und `NavigationRouteCacheTagsEvent`.

### Produktzuweisungen

1. **Explizite Zuweisung** — direkte Links in `product_category` (und `product_category_tree`)
2. **Dynamic Product Groups** — gespeicherte Filter als `product_stream` auf Kategorie (Runtime-Auswertung)

Beide Zuweisungstypen werden für Kategorie-Listings zusammengeführt.
Listing-Kriterien: `ProductListingRoute` → erweiterbar via `ProductListingCriteriaEvent`.

### CMS-Layout-Integration

- Kategorien können CMS-Layout referenzieren (`cmsPageId`)
- **Vererbung**: fehlt `cmsPageId` → Parent-Layout wird verwendet
- Kategorie-spezifische Slot-Konfiguration wird zur Laufzeit gemergt
- `folder`-Kategorien ignorieren Layouts; `link`-Kategorien redirecten sofort

### SEO-Felder

- `metaTitle`, `metaDescription`, `keywords`, `seoUrl`, `noIndex`, `noFollow`
- URL-Templates konfigurierbar unter *Einstellungen → SEO*
- Rebuild beim Ändern von Kategorien oder via SEO-Indexer

### Extensibility-Events

- `NavigationLoadedEvent` — Navigation-Baum geladen; anreichern/anpassen
- `CategoryIndexerEvent` — De-normalisierte Daten oder externe Such-Indizes synchronisieren
- `ProductListingCriteriaEvent` — Listing-Filter, Sorting, Aggregationen anpassen
- `SeoUrlUpdateEvent` — auf SEO-URL-Regenerierung reagieren

---

## Sales Channels (concepts/commerce/catalog/sales-channels.md)

Sales Channels definieren, wie der Katalog einer konkreten Zielgruppe exponiert wird.
Ein Shopware-Instanz kann mehrere "Stores" bedienen ohne Daten zu duplizieren.

### Was ein Sales Channel steuert

- **Channel-Typ**: Storefront, Headless Store API, Product Feed, custom
- **Audience Defaults**: Sprache, Währung, Land, Steuerberechnungsmodus, Kundengruppe, Standard-Zahlung/Versand
- **Navigation Roots**: `navigation`, `footer`, `service` Einstiegskategorien
- **Presentation**: Home-CMS-Page (`homeCmsPageId`) + Theme-Konfiguration
- **Availability**: erlaubte Domains, Zahlungs-/Versandmethoden, Sprachen, Währungen, Länder, Produktsichtbarkeit

### Kernmodell

```
SALES_CHANNEL → SALES_CHANNEL_DOMAIN (URLs + Sprache + Währung + Snippet-Set)
SALES_CHANNEL → CATEGORY (navigation/footer/service roots)
SALES_CHANNEL → CMS_PAGE (Home-Page)
SALES_CHANNEL ←→ PRODUCT (via product_visibility)
SALES_CHANNEL ←→ PAYMENT_METHOD / SHIPPING_METHOD / CURRENCY / LANGUAGE (Mappings)
```

- `sales_channel`: Defaults, Navigation Roots, Home CMS Page, Access Key, Maintenance-Flags, hreflang
- `sales_channel_domain`: URL + Sprache + Währung + Snippet Set — Matching über Host/Pfad

### Domains und Lokalisierung

Beispiel-Konfiguration:
```
https://example.com/     → en-GB, GBP
https://de.example.com   → de-DE, EUR
https://example.es/      → es-ES, EUR
```

**Empfehlung**: Subdomains (z.B. `de.example.com`) statt Sub-Pfade (z.B. `example.com/de`),
da Sub-Pfade bei gleicher Domain zu Cookie-Konflikten zwischen Channels führen.

`hreflangActive` und `hreflangDefaultDomainId` steuern hreflang-Links.

### Produkt-Sichtbarkeit

Produkte benötigen eine `product_visibility`-Zeile pro Sales Channel.
Visibility-Level bestimmt: durchsuchbar und/oder direkt erreichbar.
`main_category` — SEO-freundliche URL pro Produkt und Sales Channel.

### Context-Erstellung

Eingehende Requests → Sales Channel via Access Key oder Domain-Matching auflösen.
`SalesChannelContextService` baut `SalesChannelContext` mit:
- Defaults (Sprache, Währung, Zahlung, Versand)
- Token, Customer, regelbasierte Preise, Berechtigungen

Relevante Store-API-Routen:
- `GET /store-api/context` — aktuellen Kontext lesen/wechseln
- `GET /store-api/navigation/{activeId}/{rootId}`
- `GET /store-api/category/{navigationId}`

### Extension Points

- `SalesChannelContextCreatedEvent` — Kontext aufgebaut; anreichern oder Session persistieren
- `SalesChannelContextSwitchEvent` — bei Wechsel von Währung, Sprache, Zahlung, Versand, Adresse
- `SalesChannelContextRestoredEvent` — gespeicherter Context-Token wiederhergestellt
