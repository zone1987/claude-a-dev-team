# Shopware CMS / Shopping Experiences — Vollständige Konzept-Doku

Quellen: `concepts/commerce/content/index.md`, `shopping-experiences-cms.md`, `cookie-consent-management.md`

---

## Content-Überblick (index.md)

Shopware 6 hat ein integriertes CMS-System namens **Shopping Experiences** basierend auf Layouts.
Tool: **Page Builder** im Admin-Panel.

Zusätzlich: **Cookie Consent Management** für DSGVO-Konformität.

---

## Shopping Experiences / CMS (shopping-experiences-cms.md)

### Struktur

Hierarchische Struktur: **Page → Section(en) → Block(s) → Slot(s) → Element**

#### Page

Wrapper mit `type`:
- `page` — standard CMS-Seite (Shop-Seiten, Kategorieseiten)
- `landingpage` — Landing-Page-Layouts
- `product_list` — Produkt-Listing/Kategorie-Layouts
- `product_detail` — Produktdetailseiten-Layouts

#### Section

Horizontaler Container. `type`:
- `sidebar` — Zwei-Spalten-Layout (Sidebar + Content)
- `fullwidth` — Einzelne volle Spalte

#### Block

Einheit, die üblicherweise eine ganze Zeile überspannt. Block-Kategorien:
`text`, `image`, `video`, `text-image`, `commerce`, `sidebar`, `form`, `html`, `favorite`, `app`

Jeder Block enthält null bis mehrere Slots. Ein Slot hat einen Namen und ist Container für genau ein Element.

Beispiel Block-JSON:
```json
{
    "type": "text-hero",
    "slots": [{
        "type": "text",
        "slot": "content",
        "config": {
            "content": { "source": "static", "value": "Hello World" }
        }
    }]
}
```

#### Slot

Benannter Container für genau ein Element.
- `source: "static"` — statischer Wert
- `source: "mapped"` — zur Laufzeit dynamisch aufgelöst (z.B. `category.description`)

#### Elements (Primitive)

Built-in Element-Typen:
`text`, `html`, `form`, `image`, `image-slider`, `video`, `youtube-video`, `vimeo-video`,
`product-listing`, `product-box`, `product-slider`, `product-name`, `manufacturer-logo`,
`buy-box`, `cross-selling`, `product-description-reviews`, `category-navigation`

Eigene Element-Typen via `CmsElementResolverInterface` registrieren.

### Hydration dynamischer Inhalte

Während CMS-Struktur statisch ist, kann Inhalt dynamisch und kontext-bewusst sein.
Beispiel: Gleicher Layout für mehrere Kategorieseiten — Produktlisting, Header-Bild, Beschreibung
werden je nach Kategorie-Konfiguration geladen.

**Resolving-Prozess** (Orchestrator: `SalesChannelCmsPageLoader::load()`):

1. `CmsPageLoaderCriteriaEvent` dispatchen (Kriterien anpassbar)
2. CMS-Layout laden (Sections, Blocks, Slots, Background Media)
3. Nach `position` sortieren
4. Resolver-Kontext aufbauen (Request + SalesChannelContext + optionale Entity)
5. Slot-Konfiguration der Entity überschreiben (z.B. kategorie-spezifische Anpassungen)
6. Slot-Daten auflösen via `CmsSlotsDataResolver`:
   - **Collect**: jeder Element-Resolver's `collect()` erstellt `CriteriaCollection`
   - **Optimize**: einfache ID-Kriterien mergen, komplexe Suchen separieren (min. DB-Queries)
   - **Fetch**: optimierte Kriterien gegen DAL ausführen
   - **Enrich**: `enrich()` füllt Slot mit geholten Daten
7. `CmsPageLoadedEvent` dispatchen (Post-Processing möglich)
8. Cache-Tags sammeln (Produkt-IDs etc. für HTTP-Cache-Invalidierung)
9. Vollständige Page-Daten zurückgeben

### Erweiterbarkeit

**Custom Element Resolver** via `CmsElementResolverInterface`:
- `getType()` — Element-Typ-Identifier
- `collect()` — CriteriaCollection aufbauen
- `enrich()` — Slot mit Daten befüllen

**Event-basierte Extensions** (ab 6.6.7):
- `CmsSlotsDataResolveExtension`
- `CmsSlotsDataCollectExtension`
- `CmsSlotsDataEnrichExtension`

### Headless-Fähigkeit / Separation of Content and Presentation

CMS ist **kanalunabhängig**:
- Browser: Shopware Storefront → HTML
- SPA / Headless Frontend: API → JSON interpretieren
- Native App: Nur relevante Blöcke anzeigen
- Smart Speaker: Nur `voice`-Typ-Elemente vorlesen

**Wichtig für Headless**: Admin-Preview zeigt nur wie Storefront es darstellt — bei stark abweichenden
Headless-Frontends ist die Preview nur begrenzt repräsentativ.

---

## Cookie Consent Management (cookie-consent-management.md)

### Überblick

DSGVO-unterstützendes Cookie-Consent-System. Verfügbar ab 6.7.3.0 für Store-API-Endpunkt und
Hash-Mechanismus.

### Systemkomponenten

1. **Cookie Provider Service** — sammelt alle Cookie-Definitionen (Core, Plugins, Apps)
2. **Store API Endpoint** (`GET /store-api/cookie/groups`) — exponiert Cookie-Konfiguration + Hash
3. **Storefront Component** — verwaltet Consent-UI und User-Präferenzen
4. **Configuration Hash** — trackt Änderungen für Re-Consent

### Cookie-Flow

```
User → Storefront → StoreAPI → CookieProvider
                             ↓ Cookie groups + hash
Storefront vergleicht gespeicherten Hash (pro Sprache)
→ Hash geändert: Consent-Banner anzeigen
→ Hash identisch: gespeicherte Präferenzen anwenden
User trifft Auswahl → Präferenzen + Hash speichern (mit Sprach-ID)
```

### Cookie-Kategorien (DSGVO-konform)

| Kategorie | Snippet-Key | Beispiele |
|---|---|---|
| Technisch erforderlich | `cookie.groupRequired` | Session, Warenkorb, Security Token |
| Komfortfunktionen | `cookie.groupComfortFeatures` | YouTube, Social Media, Chat |
| Marketing | `cookie.groupMarketing` | Facebook Pixel, Google Ads, Affiliate |
| Statistik/Tracking | `cookie.groupStatistical` | Google Analytics, Hotjar, A/B Testing |

Technisch erforderliche Cookies können **nicht** deaktiviert werden.

### Hash-Mechanismus

- Hash berechnet aus allen Cookie-Konfigurationen (Name, Beschreibung, Ablaufzeit)
- Gespeichert als Cookie `cookie-config-hash`: `{"<sprach-id>": "<hash>"}` 
- Bei Besuch: aktueller Hash vs. gespeicherter Hash für aktuelle Sprache vergleichen
- Unterschied → alle nicht-essentiellen Cookies entfernen → Re-Consent

**Hash ändert sich bei**: neue Cookies (Plugins/Apps), modifizierte/entfernte Cookies, geänderte Cookie-Gruppen

**Warum Sprach-ID im Hash?** — Für Multi-Sprach-Shops auf derselben Domain (verschiedene Domains
sind durch Browser-Cookie-Scoping bereits getrennt).

### Cookie-Lifetime-Tracking

| Cookie | Zweck | Lebensdauer |
|---|---|---|
| `cookie-preference` | Gespeicherte Consent-Entscheidungen | 30 Tage |
| `cookie-config-hash` | Konfigurationsänderungs-Tracking pro Sprache | 30 Tage |

**Geschützte Cookies** (niemals entfernt): `session-*`, `timezone`

### Store API Endpoint (ab 6.7.3.0)

`GET /store-api/cookie/groups`

Liefert: Cookie-Gruppen, Konfiguration, Hash, Sprach-ID.
Ermöglicht Headless-Implementierungen, Custom Frontends und Third-Party-Integrationen.

### Erweiterbarkeit

- **Plugins**: Event Listener zum Hinzufügen eigener Cookies
- **Apps**: Cookies in `manifest.xml` definieren
- **JavaScript**: Events für Consent-Änderungen (`reacting-to-cookie-consent-changes`)

### DSGVO-Features

- Opt-in by default (keine vorausgefüllten Checkboxen)
- Granulare Kontrolle (einzelne Kategorien accept/reject)
- Re-Consent bei Konfigurationsänderungen
- Klare Cookie-Beschreibungen
- Einfaches Widerrufen (Präferenzen jederzeit änderbar)
- Konfigurationsänderungs-Tracking via Hash
