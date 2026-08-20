# Shopware 6 – System info, logs & other system settings (complete reference)

Sources:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/logging
- https://docs.shopware.com/de/shopware-6-de/einstellungen/System/shopwareaccount
- https://docs.shopware.com/de/shopware-6-de/einstellungen/system/daten-teilen
- https://docs.shopware.com/de/shopware-6-de/einstellungen/Business-Events

---

## Contents

- [Ereignis-Logs](#ereignis-logs)
- [Shopware Account Verknüpfung](#shopware-account-verknüpfung)
- [Datenschutzeinstellungen (Daten teilen)](#datenschutzeinstellungen-daten-teilen)
- [Business-Events (Legacy)](#business-events-legacy)
- [Suche (Einstellungen > Shop > Suche)](#suche-einstellungen-shop-suche)

## Ereignis-Logs

**Path:** Einstellungen (Settings) > System > Ereignis-Logs (Event logs)  
**Self-hosted only**

As of version 6.5 the entries have been minimised. For extended logging configuration (e.g. mail logs) consult the developer documentation.

### Controls
- `...` icon: hide columns
- Three-bar icon: show columns, toggle compact mode
- Central search bar: search the log

### Columns
| Spalte (Column) | Inhalt (Content) |
|---|---|
| Nachricht (Message) | Originating area (e.g. Checkout, Mail) |
| Priorität (Priority) | Importance level with numeric value |
| Inhalt | Message text (clickable for details) |

### Priority levels

| Stufe (Level) | Wert (Value) | Bedeutung (Meaning) |
|---|---|---|
| Debug | 100 | Function debugging |
| Info | 200 | Basic system information |
| Error | 300 | Error message to be checked |
| Critical | 400 | Critical error, immediate review required |

### Detail view
A modal window shows different information depending on the entry type.
- Mail logs: several view modes
- Debug entries: source-code format only

---

## Shopware Account Verknüpfung

**Path:** Einstellungen > System > Shopware Account  
**Available from:** 6.3.5.0  
**Self-hosted only**

Connects the Shopware installation with the personal Shopware Account to access purchased extensions and subscriptions.

### Configuration fields

| Feld (Field) | Beschreibung (Description) |
|---|---|
| Lizenzierungshost (Licensing host) | Host domain (must match the domain registered in the account exactly, including `www.` if needed) |
| Verifikationsprüfsumme (Verification checksum) | Optional; required if the domain is not yet verified; shown at the domain entry in the account |

---

## Datenschutzeinstellungen (Daten teilen)

**Path:** Einstellungen > System > Datenschutzeinstellungen (Data protection settings)

Transparent and GDPR-compliant data management for analysis and Shopware improvements.

### Two data categories

| Kategorie (Category) | Beschreibung |
|---|---|
| **Shop-Daten (anonym)** (Shop data, anonymous) | Orders, diagnostics, general shop information; fully anonymised |
| **Nutzungsdaten** (Usage data) | Personal behavioural data in the administration (clicks, navigation, features) |

### Configuration
- **Shop-Daten:** Einstellungen > System > Datenschutzeinstellungen (toggle)
- **Nutzungsdaten:** own profile > Datenschutzeinstellungen (toggle)

### Modal after login
Options:
- "Alles ablehnen" (Reject all) — no sharing
- "Alles akzeptieren" (Accept all) — both types enabled
- "Auswahl speichern" (Save selection) — individual configuration

### FAQ note
Shop data: no personal data. Usage data: recording of admin actions.

---

## Business-Events (Legacy)

**Path:** Einstellungen > Shop > Business-Events  
**Available from:** 6.3.3.0  
**Note:** Replaced by the **Flow Builder** as of v6.4.8.0.

### Table columns

| Spalte | Inhalt |
|---|---|
| Event | Technical name + understandable description |
| Titel (Title) | Individually assigned name |
| Verkaufskanal (Sales channel) | Assigned channels (empty = all) |
| Regeln (Rules) | Conditions from the Rule Builder |
| E-Mail-Template (Mail template) | Template used |
| Aktiv (Active) | Status |

### Creating a business event

| Feld | Beschreibung |
|---|---|
| Titel | Custom name |
| Aktiv | Enable/disable |
| Event | Event to be automated |
| E-Mail-Template | Template used for sending |
| Verkaufskanal | Optionally channel-specific |
| Regeln | Rule Builder conditions |

### Mail recipients
Store internal mail addresses. Customers only receive templates if **no** internal recipients are configured.

---

## Suche (Einstellungen > Shop > Suche)

**Available from:** 6.4.0.0

### Special characters in product numbers
Configurable in `config/packages/shopware.yaml`:
```yaml
shopware:
  search:
    product:
      search_ranking:
        special_chars: ['-', '_', '+', '.', '@', '/']
```

### Allgemein (General) – search behaviour
| Option | Beschreibung |
|---|---|
| UND-Modus (AND mode) | Only results containing all search terms |
| ODER-Modus (OR mode) | Results containing at least one term |
| Minimale Suchbegriffslänge (Minimum search term length) | Default: 2 characters |
| Maximale Länge (Maximum length) | 255 characters |

### Searchable content (configurable per field)
- Suchbar (Searchable): on/off
- Ranking Punktzahl (Ranking score): weighting
- Suchbegriffe trennen (Split search terms): splitting at special characters

**Default searchable content:**
Category name, category custom fields, own search terms, product description, product EAN, manufacturer name, manufacturer number, manufacturer custom fields, product meta description, product meta title, product name, property value, product number, property name, product tag

### Search index
- "Such-Index neu erstellen" (Rebuild search index) button
- Shows the time of the last update
- Progress indicator while rebuilding

### Advanced Search (from plan Evolve / Commercial)
Requires Elasticsearch or OpenSearch.

| Option | Beschreibung |
|---|---|
| Advanced Search aktivieren (Enable Advanced Search) | Per sales channel |
| Trefferanzahl (Number of hits) | For preview search and result page |
| Echtzeit-Suche (Real-time search) | With test function (without frontend access) |

### AI Copilot (from plan Rise)
- **Context-based search:** natural-language input, sales channel description (max. 100 characters), 3 example instructions per language
- **Image-based search:** PNG/JPEG upload or camera photo (up to 3 similar products)
