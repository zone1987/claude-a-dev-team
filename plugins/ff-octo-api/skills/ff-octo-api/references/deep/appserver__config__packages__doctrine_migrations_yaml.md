# Doctrine Migrations Konfiguration (appserver/config/packages/doctrine_migrations.yaml)

**Absolute Pfad:** `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/config/packages/doctrine_migrations.yaml`

## Zweck

YAML-Konfigurationsdatei des Symfony Doctrine Migrations Bundle. Definiert Pfade und Verhalten für Datenbank-Migrationen, die Schema-Änderungen (Tabellenerstellung, Spaltenänderungen, Indizes) versioniert und reproduzierbar umsetzen. Im ResubmissionAppServer relevant für Verwaltung von Shops, Sessions und Tourismus-Ticketing-Daten.

## Struktur & Konfigurationsschlüssel

```yaml
doctrine_migrations:
    migrations_paths:
        'DoctrineMigrations': '%kernel.project_dir%/migrations'
    enable_profiler: false
```

### Attribute

| Schlüssel | Typ | Wert | Bedeutung |
|-----------|-----|------|----------|
| `doctrine_migrations` | Objekt | - | Wurzelkonfiguration für Doctrine Migrations Bundle |
| `migrations_paths` | Objekt | - | Mapping von Namespace zu Verzeichnis |
| `'DoctrineMigrations'` | String | `'%kernel.project_dir%/migrations'` | Namespace für Migrations-Klassen (z.B. `DoctrineMigrations\Version20251211103914`). Zeigt auf `migrations/` Verzeichnis. Absichtlich unterschiedlich von `App\Migrations` (Kommentar: "should NOT be autoloaded"). |
| `enable_profiler` | Boolean | `false` | Profiler für Migrations-Debugging **deaktiviert**. Performance-Optimization für Produktion. |

## Migrations-Verzeichnis

**Pfad:** `%kernel.project_dir%/migrations/` → `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/migrations/`

Enthält versionierte Migration-Klassen:
- `Version20251211103914.php` – Beispiel: erstellt `shop` Tabelle (shop_id, shop_url, shop_secret, shop_client_id, shop_client_secret, shop_active)
- `.gitignore` – Migrations sind versionskontrolliert

Jede Migration erbt von `Doctrine\Migrations\AbstractMigration` und implementiert:
- `getDescription(): string` – Beschreibung der Änderung
- `up(Schema $schema): void` – Schema-Änderungen (Deployment)
- `down(Schema $schema): void` – Rollback-Logik

## Integration mit Doctrine DBAL/ORM

**Verwandte Konfiguration:** `config/packages/doctrine.yaml`

- **DBAL:** Datenbankverbindung via `DATABASE_URL` (PostgreSQL/MySQL)
- **ORM:** Entity-Mapping (`src/Entity/`) mit Attribute-basierter Konfiguration
- Migrations arbeiten auf DBAL-Ebene (direkte SQL), unabhängig von Entity-Definitionen

## Profiler & Debugging

- `enable_profiler: false` – Migrations-Profiling ausgeschaltet
  - Spart Memory/CPU beim `bin/console doctrine:migrations:migrate`
  - Im Debug-Modus (`kernel.debug = true`) würde dies Queries in der Symfony Profiler-Toolbar anzeigen
  - Für Produktion/CI richtig konfiguriert

## Aufrufe & Nutzung

CLI-Befehle (Symfony Console):
- `bin/console doctrine:migrations:migrate` – Alle ausstehenden Migrationen ausführen (nutzt diese Config)
- `bin/console doctrine:migrations:migrate --dry-run` – Vorschau ohne Ausführung
- `bin/console doctrine:migrations:rollback` – Letzte Migration rückgängig machen
- `bin/console doctrine:migrations:status` – Status aller Migrationen anzeigen

## Besonderheiten & Fallstricke

1. **Namespace-Trennung:** `'DoctrineMigrations'` (nicht `'App\Migrations'`)
   - Verhindert Autoloading durch PSR-4 Autoloader
   - Migrationen sind explizit gemanagt, nicht Teil der autogeladenen Applikation
   - Reduziert Bootzeit von `bin/console` commands

2. **Keine Autogeneration in Production:**
   - Profiler deaktiviert (`false`) für Laufzeit-Effizienz
   - Migrationen sollten **vor Deployment** generiert werden via `bin/console make:migration`
   - Nicht zur Laufzeit vom Webserver ausgeführt

3. **Shop-Tabelle als erste Migration:**
   - Resubmission AppServer verwaltet Shops (`shop` Tabelle mit IDs, URLs, Secrets)
   - Baseline-Migration Version20251211103914 – kritisch für Mehrmandat-Setup

4. **Kernel.project_dir Placeholder:**
   - `%kernel.project_dir%` wird zur Laufzeit durch Symfony Container aufgelöst
   - Ermöglicht Umzug des Projekts ohne Konfiguration-Änderung

## Abhängigkeiten & Bezüge

- **doctrine_migrations.yaml** ← **doctrine.yaml** (Database Connection)
- **doctrine_migrations.yaml** → **migrations/** (Versionierte SQL-Skripte)
- **Doctrine Migrations Bundle** (`vendor/doctrine/doctrine-migrations-bundle/`)
- **Symfony Console** (`bin/console` Befehle)
- Relevant für: ResubmissionAppServer Datenbankinitialisierung, Shop-Setup

## Zusammenfassung

Minimale, aber kritische Konfiguration für reproduzierbare Datenbankänderungen im ResubmissionAppServer. Namespace-Isolation und deaktivierter Profiler sind Production-best-practices. Migrationen werden manuell via CLI generiert und vor Deployment ausgeführt.
