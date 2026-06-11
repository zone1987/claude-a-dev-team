# Doctrine ORM-Konfiguration (ResubmissionAppServer) (/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/config/packages/doctrine.yaml)

## Zweck

Zentrale Konfigurationsdatei für Doctrine ORM/DBAL im Symfony-basierten **ResubmissionAppServer** (Ticketing-Backend für OCTO-API-Integration). Definiert:
- Datenbankverbindung (PostgreSQL über `DATABASE_URL` Umgebungsvariable)
- Entity-Mapping (Quellverzeichnis `src/Entity`, Namespace `App\Entity`)
- ORM-Verhalten (Lazy Loading, Proxy-Generierung, XML-Validierung)
- Umgebungsspezifische Optimierungen (Test-DB-Suffix, Prod-Cache-Pooling)

**Kategorie:** Konfiguration (YAML)  
**Kontext:** AppServer-Backend (keine Shopware-direkte Abhängigkeit; eigenständiges Ticketing-System)

---

## Struktur & Konfigurationsschlüssel

### doctrine.dbal (Database Abstraction Layer)

**`url`** 
- Wert: `'%env(resolve:DATABASE_URL)%'`
- Typ: Umgebungsvariable (env resolver)
- Bedeutung: Datenbank-Verbindungsstring aus `.env` oder deployment env
- Erwartet: PostgreSQL DSN (z.B. `postgres://user:pass@host:5432/dbname`)
- Fallstricke: `resolve:` ist erforderlich für Umgebungsvariablen mit Sonderzeichen

**`profiling_collect_backtrace`**
- Wert: `'%kernel.debug%'` (boolean, nur im Debug-Modus aktiv)
- Bedeutung: Aktiviert Stack-Traces für DBAL-Profiler (Symfony Debug Toolbar)
- Seiteneffekt: Performance-Overhead; nur dev/test aktivieren

**`use_savepoints`**
- Wert: `true`
- Bedeutung: Ermöglicht verschachtelte Transaktionen via Savepoints (PostgreSQL)
- Use-Case: Nested try-catch bei Ticket-Reservierungen, Preis-Validierungen

**`server_version`** (auskommentiert)
- Default: Wird aus `DATABASE_URL` abgeleitet
- Alternative: Explizit angeben (z.B. `'16'` für PostgreSQL 16)
- Seiteneffekt: Doctrine generiert DB-spezifische SQL-Dialekte

---

### doctrine.orm (Object-Relational Mapping)

**`auto_generate_proxy_classes`**
- Wert: `true` (außer prod: `false`)
- Bedeutung: Generiert Proxy-Klassen für Lazy-Loading zur Laufzeit
- Fallstricke: In Prod muss `proxy_dir` beschreibbar sein oder Caching vorab generiert

**`enable_lazy_ghost_objects`**
- Wert: `true`
- Bedeutung: Verwendet "Ghost Objects" (Doctrine 2.13+) für effizienteres Lazy-Loading
- Impact: Reduziert Memory-Footprint bei großen Entity-Graphen (z.B. Ticket + LineItems + Pricing)

**`report_fields_where_declared`**
- Wert: `true`
- Bedeutung: Validation meldet Fehler in der Zeile, wo Property deklariert ist (nicht in Trait/Base)
- Zweck: Bessere Fehlerausgaben beim XML-Mapping

**`validate_xml_mapping`**
- Wert: `true`
- Bedeutung: Validiert Doctrine-XML-Mapping-Dateien beim Start
- Fallstricke: Typos in `orm:` Tags werden früh erkannt, können aber Startup verlangsamen

**`naming_strategy`**
- Wert: `doctrine.orm.naming_strategy.underscore_number_aware`
- Bedeutung: Konvertiert camelCase Properties zu snake_case Spalten
  - Beispiel: `lineItemId` → `line_item_id`
- Standard Symfony-Konvention für Legacy-Datenbanken

**`identity_generation_preferences`**
- Wert: 
  ```yaml
  Doctrine\DBAL\Platforms\PostgreSQLPlatform: identity
  ```
- Bedeutung: Nutzt PostgreSQL `IDENTITY` (SERIAL/BIGSERIAL) für Auto-Increment IDs
- Alternative: `sequence` (explizite Sequences), `uuid` (für UUIDs)
- Use-Case: Ticket-IDs, Order-IDs sollen DB-seitig generiert werden

**`auto_mapping`** (global)
- Wert: `true`
- Bedeutung: Doctrine durchsucht automatisch alle Bundles nach Entities
- Abhängigkeiten: Definierte Mappings (siehe unten) werden berücksichtigt

**`mappings`** (Entity-Pfade)

```yaml
App:
  type: attribute
  is_bundle: false
  dir: '%kernel.project_dir%/src/Entity'
  prefix: 'App\Entity'
  alias: App
```

- **type:** `attribute` → Doctrine Attributes (#[ORM\Entity], #[ORM\Column], etc.), nicht XML
- **is_bundle:** `false` → AppServer ist keine Symfony Bundle, eigenständiges App-Projekt
- **dir:** `/src/Entity` → Pfad, in dem Entity-Klassen liegen
- **prefix:** `App\Entity` → Namespace für alle Entities
- **alias:** `App` → Kurzform in DQL (`SELECT a FROM App:Order` statt `App\Entity\Order`)

**`controller_resolver`**
- `auto_mapping: false` → Deaktiviert auto-routing von Entity-IDs in Controller-Argumenten
- Grund: AppServer hat kein HTTP-Routing zu Entities; nur API-Operationen

---

### when@test (Test-Umgebung)

```yaml
when@test:
  doctrine:
    dbal:
      dbname_suffix: '_test%env(default::TEST_TOKEN)%'
```

- **dbname_suffix:** Hängt `_test` oder `_test{TOKEN}` an Datenbanknamen
  - Beispiel: Hauptdatenbank `octo_ticketing` → Test-DB `octo_ticketing_test` oder `octo_ticketing_test_X` (ParaTest-Parallelisierung)
- **Effekt:** Jeder PHPUnit-Prozess nutzt isolierte Datenbank
- **TEST_TOKEN:** Von ParaTest gesetzt für parallele Test-Isolation
- **Fallstricke:** Test-Datenbank muss vor Tests existieren oder via `bin/console doctrine:database:create --env=test`

---

### when@prod (Produktionsumgebung)

```yaml
when@prod:
  doctrine:
    orm:
      auto_generate_proxy_classes: false
      proxy_dir: '%kernel.build_dir%/doctrine/orm/Proxies'
      query_cache_driver:
        type: pool
        pool: doctrine.system_cache_pool
      result_cache_driver:
        type: pool
        pool: doctrine.result_cache_pool

  framework:
    cache:
      pools:
        doctrine.result_cache_pool:
          adapter: cache.app
        doctrine.system_cache_pool:
          adapter: cache.system
```

**ORM-Optimierungen:**
- **auto_generate_proxy_classes: false** → Proxies müssen vorab generiert werden (`bin/console cache:warmup`)
- **proxy_dir:** Speichert Pre-generated Proxies (vermeidet Laufzeit-Codegen)
- **query_cache_driver:** Cached Doctrine Metadata (Spalten, Relationen) pro Entity
  - Pool: `doctrine.system_cache_pool` (Redis/APCu in Prod)
- **result_cache_driver:** Cached Abfrageergebnisse (SELECT-Ergebnisse)
  - Pool: `doctrine.result_cache_pool`
  - Use-Case: Häufig abgerufene Katalog-Daten (Pricing-Tables)

**Cache-Pools:**
- `doctrine.result_cache_pool` → Nutzt `cache.app` (Redis oder File-basiert)
- `doctrine.system_cache_pool` → Nutzt `cache.system` (schneller Cache für Metadaten)

**Seiteneffekte:**
- Verbesserte Performance durch Caching (weniger DB-Metadaten-Queries)
- Erfordert `cache:warmup` beim Deployment
- Cache-Invalidation notwendig bei Entity-Schema-Änderungen

---

## Abhängigkeiten & Bezüge

- **Umgebungsvariablen:** `.env`, `.env.local` (DATABASE_URL)
- **Entity-Klassen:** `/src/Entity/*` (Namespace `App\Entity`)
- **Doctrine Bundles:** `DoctrineBundle` (Symfony Bundle)
- **Cache-Infrastruktur (Prod):** Redis oder APCu (via `framework.cache`)
- **Database:** PostgreSQL (empfohlen; DBAL unterstützt auch MySQL, SQLite)

---

## Besonderheiten & Fallstricke

### 1. **Umgebungsspezifische Konfiguration**
   - Dev/Test: Auto-Proxy-Generierung aktiv → langsamerer Start, aber flexibel
   - Prod: Proxies pre-generated → schneller Start, erfordert `cache:warmup`
   - **Fallstrick:** Vergessenes `cache:warmup` beim Deployment → RuntimeException bei Proxy-Miss

### 2. **Savepoints bei verschachtelten Transaktionen**
   - `use_savepoints: true` ermöglicht `BEGIN; SAVEPOINT sp1; ROLLBACK TO sp1;`
   - Kritisch für Ticket-Reservierungen (äußere TX für Verfügbarkeit, innere für Preisvalidierung)

### 3. **PostgreSQL Identity vs. Sequence**
   - `identity` nutzt SERIAL/BIGSERIAL (einfacher, Standard)
   - Alternative `sequence` für explizite Kontrolle über Sequenz-Namen
   - **Fallstrick:** UUID-Entities brauchen eigene Strategy; hier nicht konfiguriert

### 4. **Test-Isolation via ParaTest**
   - `dbname_suffix` mit `TEST_TOKEN` ermöglicht parallele Tests
   - Jeder Worker bekommt isolierte DB → keine Lock-Konflikte
   - Voraussetzung: Genug PostgreSQL-Connections für Worker-Zahl

### 5. **Cache-Pools in Prod**
   - Query-Cache wichtig für häufig abgerufene Entities (Pricing-Katalog)
   - Result-Cache kann stale Daten verursachen → manuelles Invalidieren bei Änderungen
   - **Fallstrick:** Cache-Adapter nicht konfiguriert → Fallback auf File-Cache (langsam)

### 6. **attribute vs. xml Mapping**
   - Diese Config nutzt `type: attribute` (PHP 8 Attributes)
   - Alternative: XML-Mapping-Dateien (z.B. `config/doctrine/Entity.*.orm.xml`)
   - Beide können vermischt werden; `validate_xml_mapping: true` prüft XML-Syntax

### 7. **Lazy Ghost Objects (Doctrine 2.13+)**
   - Effizientere Darstellung nicht-geladener Properties
   - Fallstrick: Erfordert PHP 8.1+; ältere Versionen ignorieren diese Config

---

## Verwandte Dateien

- `.env` / `.env.local` — Umgebungsvariablen (DATABASE_URL)
- `/src/Entity/*` — Doctrine Entity-Klassen (mit Attributes)
- `config/services.yaml` — Doctrine Service-Definitionen
- `config/packages/cache.yaml` — Cache-Pool-Konfiguration (Prod)
- `bin/console doctrine:*` — Doctrine CLI-Befehle
  - `doctrine:database:create` — Erstellt DB-Schema
  - `doctrine:migrations:*` — Schema-Migrationen
  - `doctrine:cache:warmup` — Prod-Cache vorab generieren

---

## Typische Verwendung im AppServer-Kontext

1. **Entity-Persistierung:** Tickets, Orders, Pricing-Data werden über Doctrine ORM persistiert
2. **Query-Performance:** Result-Cache für häufig abgerufene Katalog-Daten (Prod)
3. **Transaktionale Konsistenz:** Savepoints für verschachtelte Reservierungs-Flows
4. **Test-Isolation:** Separate Test-Datenbanken pro PHPUnit-Worker (ParaTest)

