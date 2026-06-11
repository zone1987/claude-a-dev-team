# Shopware Framework-Konzepte (weitere) — Vollständige Doku

Quellen: `concepts/framework/flow-concept.md`, `http_cache.md`, `elasticsearch.md`, `migrations.md`,
`storefront-components.md`, `system-check.md`

---

## Flow Builder (flow-concept.md)

### Konzept

Shopware-Automatisierungslösung für Shop-Betreiber — ohne Programmierkenntnisse.

**Komponenten:**

| Begriff | Beschreibung |
|---|---|
| **Flow** | Automatisierungsprozess; definiert Trigger → Conditions → Actions |
| **Trigger** | Event aus Storefront oder Anwendung (z.B. `checkout.order.place`) |
| **Condition** | Business-Rule; bestimmt ob Action ausgeführt wird |
| **Action** | Aufgabe die bei Trigger/Bedingungserfüllung ausgeführt wird |
| **Flow Template** | Vorgefertigter Flow (Bibliothek); via App oder Plugin; nicht modifizierbar |

Priorität: Bei mehreren Flows mit gleichem Trigger entscheidet Priorität über Ausführungsreihenfolge.
Spezielle Action "Stop flow" beendet weitere Aktionen in der Flow-Sequenz.

### Evaluation Sequence

```
FlowDispatcher::dispatch()
→ FlowExecutor::execute()
→ FlowExecutor::sequenceRuleMatches()? → Action ausführen
→ StopFlowAction::handleFlow()
```

**Beispiel: Bestellung aufgeben**
```
User → CartOrderRoute::Order() → dispatch [checkout.order.place]
→ FlowDispatcher → FlowExecutor → executeAction → StopFlowAction
```

### Storer-Konzept

Jeder Flow kann Daten speichern und für Actions bereitstellen.

- Storer-Klassen: `ProductStorer`, `OrderStorer`, `MailStorer` etc. → extends `FlowStorer`
- Methoden: `store()` und `restore()`
- Aufgerufen bei Flow-Erstellung (`StorableFlow`) im `FlowFactory`
- `restore()` kann direkt oder lazy laden

**Persistenz**: Standard: Flow-Daten werden **nicht** in DB persistiert (gleicher Request-Zyklus).
Ausnahme: Bei verzögerten Flows werden Daten persistiert für späteren Abruf.

---

## HTTP Cache (http_cache.md)

### Konzept

Reverse-Proxy-Cache zwischen Benutzer und Web-Applikation.
Caching spart Applikations-Last durch Wiederverwendung gecachter Responses.

### Aktivierung

```php
#[Route(path: '/detail/{productId}', defaults: ['_httpCache' => true])]
public function index(SalesChannelContext $context, Request $request): Response
```

Nur `GET`-Requests werden als cacheable betrachtet.

### Cache Key (sw-cache-hash Cookie)

- Enthält Hash aller cache-relevanter Informationen (logged-in Status, Steuer-Status, Währung, gematchte Regeln)
- Wird gesetzt sobald Anwendungszustand von Standard abweicht (nicht eingeloggt, Standard-Währung, leerer Cart)
- **Wichtig**: Reverse Proxies (Fastly, Varnish) oder Symfony Cache nutzen `cache-hash` als Teil des Cache Keys
- Ermöglicht differenzierte Cache-Einträge für gleichen Request mit verschiedenem Anwendungszustand

### Deprecated Cookies (werden in 6.8.0.0 entfernt)

- `sw-currency` — Währungs-Info bereits in `sw-cache-hash`
- `sw-states` — States bereits in `sw-cache-hash`

### Cache Invalidierung

- Responses werden mit Tags versehen (alle während Request generierten Cache-Tags)
- HTTP-Cache-Invalidierung einer Storefront-Route = Invalidierung der zugehörigen Store-API-Routen
- **Listen-Routen** (Produktlisting, Suche, Kategorie-Listings) sind **nicht** entity-spezifisch getaggt
  → verlassen sich auf TTL; keine direkte Invalidierung bei Einzelentität-Änderungen
  (zu kostspieliges Tracking über alle möglichen Listings)

**Begründung**: Eine Entität kann in vielen verschiedenen Listings erscheinen (verschiedene Filter, Sortierung,
Pagination). Strikte Konsistenz ist nicht garantierbar; kleine Stale-Zeit wird für Stabilität akzeptiert.

**Invalidierungs-Logging** (ab 6.7.7.0, disabled by default):
```yaml
shopware:
  cache:
    invalidation:
      tag_invalidation_log_enabled: false
```

### HTTP Cache Workflow (ab 6.8.0.0 / 6.7.6.0 mit CACHE_REWORK Flag)

`CacheResponseSubscriber` bei Response-Generierung:
1. `sw-language-id` + `sw-currency-id` Header anwenden; Vary-Header erweitern
2. Early Exits prüfen (HTTP Cache aktiviert?)
3. `sw-context-hash` berechnen (Cart, Customer, Rules, etc.)
4. Cacheability prüfen (GET + `_httpCache` Attribut)
5. Context-Hash validieren (Client vs. Server); mismatch → no-cache
6. Caching Policy anwenden → `Cache-Control` Headers setzen

---

## Elasticsearch (elasticsearch.md)

### Konzept

NoSQL-Datenbank mit Fokus auf Suchfähigkeiten. Shopware nutzt ES für verbesserte Produkt- und
Kategorie-Suche.

### Aktivierung

ES wird nur in explizit definierten Suchen genutzt.
Standard: `ProductSearchRoute`, `ProductListingRoute`, `ProductSuggestRoute`.

```php
$context->addState(Context::STATE_ELASTICSEARCH_AWARE);
$repository->search($criteria, $context);
```

**Fallback**: Bei ES-Fehler → MySQL-Datenlast. Deaktivierbar: `SHOPWARE_ES_THROW_EXCEPTION=1`

### Kernkomponenten

| Klasse | Aufgabe |
|---|---|
| `ElasticsearchDefinition` | Definiert Felder + Aggregationen pro Entity für ES |
| `ElasticsearchEntitySearcher` | Dekoriert EntitySearcher → mappt auf ES-Struktur; gibt IdSearchResult zurück |
| `ElasticsearchEntityAggregator` | Wie Searcher, aber für Aggregationen |
| `CriteriaParser` | Übersetzt Criteria in ES-Notation |
| `ProductSearchBuilder` | Spezifischer Search Builder für Produktsuche |
| `ProductUpdater` | Subscribt auf `ProductIndexerEvent`; triggert Re-Indexierung |

### CLI-Befehle

```bash
es:index          # Alle konfigurierten Entities neu indexieren
es:reset          # Alle aktiven Indizes zurücksetzen und Queue leeren (nur bei Korruption)
es:status         # Status aller aktuellen Indizes
es:create:alias   # Index-Alias aktualisieren (macht neuen Index aktiv)
es:index:cleanup  # Veraltete ES-Indizes löschen
es:test:analyzer  # ES-Analyzer auf Indizes testen
```

---

## Migrations (migrations.md)

### Konzept

PHP-Klassen mit Datenbank-Schema-Änderungen. Können vorwärts/rückwärts ausgeführt werden.

### Plugin-Migrations

- Platzierung: `Migration/`-Verzeichnis im Plugin-Source-Root
- Dateiname-Konvention: spezifisches Muster (via Shopware Console-Command generieren)
- Shopware erkennt Plugin-Migrations automatisch

### Methoden

| Methode | Typ | Beschreibung |
|---|---|---|
| `update()` | Non-destructive | Nur umkehrbare Änderungen (neue Tabellen, Columns hinzufügen) |
| `updateDestructive()` | Destructive | Unwiderrufliche Änderungen (Tabellen/Columns droppen) |

---

## Storefront Components (ab 6.7.11.0) (storefront-components.md)

### Konzept

Neues Component-System basierend auf **Symfony UX Twig Components**.
Bringt moderne, framework-ähnliche Entwicklungserfahrung in den Storefront.

### Anonymous Components (einfachste Form)

Einzelne Twig-Template-Datei definiert die Komponente.

```
MyExtension/src/Resources/views/components/Button/Primary.html.twig
→ Komponenten-Name: MyExtension:Button:Primary
```

`index.html.twig` → Verzeichnisname als Komponenten-Name.

**Properties definieren:**
```twig
{% props label = 'Click here!', size = 'md' %}
<button class="my-button size-{{ size }}">{{ label }}</button>
```

**Verwendung:**
```twig
<twig:MyExtension:Button:Primary label="Buy now!" size="lg" />
```

### PHP-backed Components (nur Plugins)

PHP-Klasse neben Template, für fortgeschrittene Logik.
Muss als Service mit `autoconfigure: true` registriert werden.

```php
#[AsTwigComponent()]
class Primary
{
    public string $label = 'Click me!';
    public string $size = 'md';
}
```

### Component SCSS

SCSS-Datei mit gleichem Namen → automatisch ins Component-Build eingebunden.
Kein PHP-Theme-Compiler — separater Vite-Buildprozess.

**Theme-Variablen**: Als CSS Custom Properties verfügbar (nicht als SCSS-Variablen):
```css
.btn-primary { background: var(--sw-color-brand-primary); }
```

### JavaScript Component System

Nachfolger des JS-Plugin-Systems. Wichtige Unterschiede:

1. **Automatische Initialisierung** — via `data-component` Attribut; MutationObserver für DOM-Änderungen
2. **Keine manuelle Registrierung** — ES Module Loading via generiertem Import-Map
3. **Event-System statt Overrides** — `window.Shopware.emit/on/intercept`
4. **TypeScript Support**

**Grundstruktur:**
```javascript
export default class ButtonPrimary extends ShopwareComponent {
    static options = { label: 'Click me!', size: 'md' };
    init() { /* Initialisierung */ }
    destroy() { /* Cleanup */ }
}
```

**Event Interception** (für Datomanipulation vor Versand):
```javascript
window.Shopware.intercept('BuyButton:PreSubmit', (data) => {
    data.formData.append('foo', 'bar');
    return data;
});
```

### Build-Prozess

```bash
# Vollständiger Storefront-Build
composer build:js:storefront

# Nur Components
composer npm:storefront run build:components
```

Build-Artefakte müssen mit Extension mitgeliefert werden (kein Runtime-Kompilieren).

### Dev-Server

```bash
composer storefront:dev-server
```
Vite-basiert; Live-Reload, kein Proxy nötig; normale Storefront-URL nutzen.

---

## System Checks (system-check.md)

### Konzept

Überprüfungen um sicherzustellen, dass Shopware-Installation normal funktioniert.
Jeder Check verifiziert einen spezifischen Aspekt der Funktionalität.

### Check-Typen

| Typ | Beschreibung |
|---|---|
| **Readiness Checks** | Vor System-Bereitschaft für Traffic ausgeführt |
| **Health Checks** | Periodisch für System-Gesundheit; manuell oder durch Monitoring |
| **Long-running Checks** | Subset der Health Checks; können lange dauern; immer im Hintergrund |

### Kategorien

| Kategorie | Beschreibung |
|---|---|
| `SYSTEM` | Backbone-Funktionalität (z.B. Datenbankverbindung) |
| `FEATURE` | Spezifische Feature-Funktionalität (z.B. Payment-System) |
| `EXTERNAL` | Externe Services (z.B. SMTP-Server erreichbar) |
| `AUXILIARY` | Hilfsdienste (z.B. Background-Tasks laufen) |

### Status-Werte

`OK` → `SKIPPED` → `UNKNOWN` → `WARNING` → `ERROR` → `FAILURE`

- `SKIPPED`: Kriterien für Check nicht erfüllt (z.B. nicht anwendbar in aktuellem Environment)
- `ERROR`: Laufzeitfehler; Teile könnten noch funktionieren
- `FAILURE`: Unwiederherstellbarer Fehler

### Execution Context

| Kontext | Beschreibung |
|---|---|
| `WEB` | Im Web-Environment |
| `CLI` | In Kommandozeilen-Umgebung |
| `PRE_ROLLOUT` | Vor System-Rollout |
| `RECURRENT` | Als Scheduled Task |

Immutable Environments: Runtime-Konfigurationsprüfung nach Deployment nicht nötig,
aber vor Rollout essentiell.
