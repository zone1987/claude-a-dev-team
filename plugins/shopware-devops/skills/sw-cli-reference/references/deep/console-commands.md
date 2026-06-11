# Shopware 6 — bin/console Befehlsreferenz

> Quelle: `resources/references/core-reference/commands-reference.md`

```bash
bin/console [command] [parameter]
```

---

## General

| Befehl | Beschreibung |
|:-------|:-------------|
| `about` | Zeigt Projektinformationen |
| `completion` | Gibt das Shell-Completion-Skript aus |
| `help` | Zeigt Hilfe zu einem Befehl |
| `list` | Listet alle Befehle auf |

---

## Administration

| Befehl | Beschreibung |
|:-------|:-------------|
| `administration:delete-extension-local-public-files` | Löscht alle lokalen öffentlichen Dateien einer Extension (nach `assets:install` ausführen) |
| `administration:delete-files-after-build` | Löscht unnötige Administration-Dateien nach dem Build |

---

## App

| Befehl | Beschreibung |
|:-------|:-------------|
| `app:activate` | Aktiviert die App im Ordner mit dem angegebenen Namen |
| `app:create` | Erstellt ein App-Skeleton |
| `app:deactivate` | Deaktiviert die App |
| `app:install` | Installiert die App |
| `app:list` | Listet alle Apps auf |
| `app:refresh` | `[app:update]` Aktualisiert installierte Apps |
| `app:uninstall` | Deinstalliert die App |
| `app:url-change:resolve` | Löst App-URL-Änderungen auf |
| `app:validate` | Prüft Manifests auf Fehler |

---

## Assets

| Befehl | Beschreibung |
|:-------|:-------------|
| `assets:install` | Installiert Bundle-Web-Assets im öffentlichen Verzeichnis |

---

## Bundle

| Befehl | Beschreibung |
|:-------|:-------------|
| `bundle:dump` | `[administration:dump:plugins|administration:dump:bundles]` Erstellt JSON-Datei mit Bundle-Konfiguration |

---

## Cache

| Befehl | Beschreibung |
|:-------|:-------------|
| `cache:clear` | Leert den Cache |
| `cache:clear:all` | Leert alle Caches/Pools, invalidiert Tags, entfernt alte Kernel-Cache-Verzeichnisse |
| `cache:clear:delayed` | Invalidiert verzögerte Cache-Keys/Tags |
| `cache:clear:http` | Leert nur den HTTP-Cache |
| `cache:pool:clear` | Leert Cache-Pools |
| `cache:pool:delete` | Löscht ein Item aus einem Cache-Pool |
| `cache:pool:invalidate-tags` | Invalidiert Cache-Tags für alle oder bestimmte Pools |
| `cache:pool:list` | Listet verfügbare Cache-Pools auf |
| `cache:pool:prune` | Bereinigt Cache-Pools |
| `cache:warmup` | Wärmt einen leeren Cache auf |
| `cache:watch:delayed` | Überwacht verzögerte Cache-Keys/Tags |

---

## Cart

| Befehl | Beschreibung |
|:-------|:-------------|
| `cart:migrate` | Migriert Warenkörbe von Redis zur Datenbank |

---

## Changelog

| Befehl | Beschreibung |
|:-------|:-------------|
| `changelog:change` | Gibt alle Änderungen einer spezifischen / unveröffentlichten Version aus |
| `changelog:check` | Validiert Changelog-Datei(en) im `changelog/_unreleased`-Ordner |
| `changelog:create` | Erstellt eine Changelog-Markdown-Datei in `/changelog/_unreleased` |
| `changelog:release` | Erstellt oder aktualisiert das finale Changelog für ein neues Release |

---

## Config

| Befehl | Beschreibung |
|:-------|:-------------|
| `config:dump-reference` | Gibt die Standardkonfiguration für eine Extension aus |

---

## Customer

| Befehl | Beschreibung |
|:-------|:-------------|
| `customer:delete-unused-guests` | Löscht nicht genutzte Gastkunden |

---

## DAL

| Befehl | Beschreibung |
|:-------|:-------------|
| `dal:create:entities` | Erstellt Entity-Klassen |
| `dal:create:hydrators` | Erstellt Hydrator-Klassen |
| `dal:migration:create` | Erstellt Migration für das Entity-Schema |
| `dal:create:schema` | Erstellt das Datenbankschema |
| `dal:refresh:index` | Aktualisiert den Index für ein Entity |
| `dal:validate` | Validiert DAL-Definitionen |

---

## Database

| Befehl | Beschreibung |
|:-------|:-------------|
| `database:clean-personal-data` | Bereinigt personenbezogene Daten aus der Datenbank |
| `database:create-migration` | Erstellt eine neue Migrationsdatei |
| `database:migrate` | Führt alle Migrationen aus |
| `database:migrate-destructive` | Führt alle destruktiven Migrationen aus |
| `database:refresh-migration` | Aktualisiert den Migrationsstatus |

---

## Debug

| Befehl | Beschreibung |
|:-------|:-------------|
| `debug:autowiring` | Listet Klassen/Interfaces für Autowiring auf |
| `debug:business-events` | Gibt alle Business Events aus |
| `debug:config` | Gibt die aktuelle Konfiguration einer Extension aus |
| `debug:container` | Zeigt aktuelle Services der Anwendung |
| `debug:dotenv` | Listet alle dotenv-Dateien mit Variablen und Werten auf |
| `debug:event-dispatcher` | Zeigt konfigurierte Listener |
| `debug:messenger` | Listet Nachrichten für Message Buses auf |
| `debug:router` | Zeigt aktuelle Routen |
| `debug:scheduler` | Listet Schedules und wiederkehrende Nachrichten auf |
| `debug:serializer` | Zeigt Serialisierungsinformationen für Klassen |
| `debug:translation` | Zeigt Übersetzungsnachrichten-Informationen |
| `debug:twig` | Zeigt Twig-Funktionen, -Filter, -Globals und -Tests |
| `debug:validator` | Zeigt Validierungsconstraints für Klassen |

---

## Dotenv

| Befehl | Beschreibung |
|:-------|:-------------|
| `dotenv:dump` | Kompiliert .env-Dateien zu .env.local.php |

---

## Error

| Befehl | Beschreibung |
|:-------|:-------------|
| `error:dump` | Gibt Fehlerseiten als statische HTML-Dateien aus |

---

## Elasticsearch / OpenSearch (es)

| Befehl | Beschreibung |
|:-------|:-------------|
| `es:admin:index` | Indiziert Elasticsearch für die Admin-Suche |
| `es:admin:mapping:update` | Aktualisiert Elasticsearch-Index-Mapping für Admin |
| `es:admin:reset` | Setzt Admin-Elasticsearch-Indizierung zurück |
| `es:admin:test` | Testet den Admin-Suchindex |
| `es:create:alias` | Erstellt den Elasticsearch-Alias |
| `es:index` | Re-indiziert alle Entities in Elasticsearch |
| `es:index:cleanup` | Bereinigt veraltete Indizes |
| `es:mapping:update` | Aktualisiert Elasticsearch-Index-Mapping |
| `es:reset` | Setzt den Elasticsearch-Index zurück |
| `es:status` | Zeigt den Status des Elasticsearch-Index |
| `es:test:analyzer` | Testet einen Elasticsearch-Analyzer |

---

## Feature Flags

| Befehl | Beschreibung |
|:-------|:-------------|
| `feature:disable` | Deaktiviert Feature-Flags |
| `feature:dump` | `[administration:dump:features]` Erstellt JSON-Datei mit Feature-Config |
| `feature:enable` | Aktiviert Feature-Flags |
| `feature:list` | Listet alle registrierten Features auf |

---

## Framework

| Befehl | Beschreibung |
|:-------|:-------------|
| `framework:demodata` | Generiert Demo-Daten |
| `framework:dump:class:schema` | Gibt das Schema des angegebenen Entities aus |
| `framework:schema` | Gibt die API-Definition als JSON aus |

---

## HTTP

| Befehl | Beschreibung |
|:-------|:-------------|
| `http:cache:warm:up` | Wärmt den HTTP-Cache auf |

---

## Import

| Befehl | Beschreibung |
|:-------|:-------------|
| `import:entity` | Importiert Entities aus einer CSV-Datei |
| `import-export:delete-expired` | Löscht alle abgelaufenen Import/Export-Dateien |

---

## Integration

| Befehl | Beschreibung |
|:-------|:-------------|
| `integration:create` | Erstellt eine Integration und gibt Key und Secret aus |

---

## Lint

| Befehl | Beschreibung |
|:-------|:-------------|
| `lint:container` | Prüft injizierte Service-Argumente gegen Typen |
| `lint:translations` | Validiert Übersetzungsdateien |
| `lint:twig` | Validiert Twig-Templates |
| `lint:xliff` | Validiert XLIFF-Dateien |
| `lint:yaml` | Validiert YAML-Dateien |

---

## Mailer

| Befehl | Beschreibung |
|:-------|:-------------|
| `mailer:test` | Testet Mailer-Transporte durch Senden einer Test-Mail |

---

## make:plugin — Plugin-Scaffolding

| Befehl | Beschreibung |
|:-------|:-------------|
| `make:plugin:admin-module` | Generiert ein Administration-Module-Skeleton |
| `make:plugin:command` | Generiert ein Plugin-CLI-Command-Skeleton |
| `make:plugin:composer` | Generiert Composer-Konfiguration für ein Plugin |
| `make:plugin:config` | Generiert ein Plugin-System-Config-Skeleton |
| `make:plugin:custom-fieldset` | Generiert ein Custom Field Set für ein Plugin |
| `make:plugin:entity` | Generiert Entity-Scaffolding für ein Plugin |
| `make:plugin:event-subscriber` | Generiert ein Event-Subscriber-Skeleton |
| `make:plugin:javascript-plugin` | Generiert ein JavaScript-Plugin-Skeleton |
| `make:plugin:plugin-class` | Generiert die Basis-Plugin-Klasse |
| `make:plugin:scheduled-task` | Generiert ein Scheduled-Task-Skeleton |
| `make:plugin:store-api-route` | Generiert ein Store-API-Route-Skeleton |
| `make:plugin:storefront-controller` | Generiert einen Storefront-Controller |
| `make:plugin:tests` | Generiert ein Plugin-Test-Skeleton |

---

## Media

| Befehl | Beschreibung |
|:-------|:-------------|
| `media:delete-local-thumbnails` | Löscht physische Thumbnails wenn Remote-Thumbnails aktiviert |
| `media:delete-unused` | Löscht nie verwendete Mediendateien. Flags: `--dry-run`, `--grace-period-days=N`, `--folder-entity=PRODUCT` |
| `media:generate-media-types` | Generiert Medientypen für alle Media-Entities |
| `media:generate-thumbnails` | Generiert Thumbnails für alle Media-Entities |
| `media:update-path` | Aktualisiert die `path`-Spalte aller Media-Einträge |

---

## Messenger

| Befehl | Beschreibung |
|:-------|:-------------|
| `messenger:consume` | Verarbeitet Nachrichten |
| `messenger:failed:remove` | Entfernt Nachrichten aus dem Fehler-Transport |
| `messenger:failed:retry` | Wiederholt Nachrichten aus dem Fehler-Transport |
| `messenger:failed:show` | Zeigt Nachrichten aus dem Fehler-Transport |
| `messenger:setup-transports` | Bereitet die Infrastruktur für den Transport vor |
| `messenger:stats` | Zeigt die Nachrichtenanzahl für Transporte |
| `messenger:stop-workers` | Stoppt Worker nach der aktuellen Nachricht |

---

## Number Range

| Befehl | Beschreibung |
|:-------|:-------------|
| `number-range:migrate` | Migriert den Increment-Speicher eines Nummernkreises |

---

## Plugin

| Befehl | Beschreibung |
|:-------|:-------------|
| `plugin:activate` | Aktiviert angegebene Plugins |
| `plugin:create` | Erstellt ein Plugin-Skeleton |
| `plugin:deactivate` | Deaktiviert angegebene Plugins |
| `plugin:install` | Installiert angegebene Plugins |
| `plugin:list` | Listet alle Plugins auf |
| `plugin:refresh` | Aktualisiert die Plugin-Liste aus dem Dateisystem |
| `plugin:uninstall` | Deinstalliert angegebene Plugins |
| `plugin:update` | Aktualisiert angegebene Plugins |
| `plugin:update:all` | Installiert alle verfügbaren Plugin-Updates |
| `plugin:zip-import` | Importiert ein Plugin aus einer ZIP-Datei |

---

## Product Export

| Befehl | Beschreibung |
|:-------|:-------------|
| `product-export:generate` | Generiert eine Produktexportdatei |

---

## Router

| Befehl | Beschreibung |
|:-------|:-------------|
| `router:match` | Debuggt Routen durch Simulieren eines Pfad-Matches |

---

## S3

| Befehl | Beschreibung |
|:-------|:-------------|
| `s3:set-visibility` | Setzt alle Dateien im S3-Filesystem auf öffentlich |

---

## Sales Channel

| Befehl | Beschreibung |
|:-------|:-------------|
| `sales-channel:create` | Erstellt einen neuen Sales Channel |
| `sales-channel:create:storefront` | Erstellt einen neuen Storefront-Sales-Channel |
| `sales-channel:list` | Listet alle Sales Channels auf |
| `sales-channel:maintenance:disable` | Deaktiviert den Wartungsmodus |
| `sales-channel:maintenance:enable` | Aktiviert den Wartungsmodus |
| `sales-channel:update:domain` | Aktualisiert eine Sales-Channel-Domain |

---

## Scheduled Task

| Befehl | Beschreibung | Version |
|:-------|:-------------|:--------|
| `scheduled-task:deactivate` | Deaktiviert einen Scheduled Task | 6.7.2.0 |
| `scheduled-task:register` | Registriert alle Scheduled Tasks | |
| `scheduled-task:run` | Führt Scheduled Tasks aus | |
| `scheduled-task:run-single` | Führt einen einzelnen Scheduled Task aus | 6.5.5.0 |
| `scheduled-task:list` | Listet alle Scheduled Tasks auf | 6.5.5.0 |
| `scheduled-task:schedule` | Schedulet einen Scheduled Task | 6.7.2.0 |

---

## Secrets

| Befehl | Beschreibung |
|:-------|:-------------|
| `secrets:decrypt-to-local` | Entschlüsselt alle Secrets in den lokalen Vault |
| `secrets:encrypt-from-local` | Verschlüsselt lokale Secrets in den Vault |
| `secrets:generate-keys` | Generiert neue Verschlüsselungsschlüssel |
| `secrets:list` | Listet alle Secrets auf |
| `secrets:remove` | Entfernt ein Secret aus dem Vault |
| `secrets:reveal` | Zeigt den Wert eines Secrets |
| `secrets:set` | Setzt ein Secret im Vault |

---

## Server

| Befehl | Beschreibung |
|:-------|:-------------|
| `server:dump` | Startet einen Dump-Server (sammelt und zeigt Dumps) |
| `server:log` | Startet einen Log-Server (zeigt Logs in Echtzeit) |

---

## Services

| Befehl | Beschreibung |
|:-------|:-------------|
| `services:install` | Installiert alle Services |

---

## Sitemap

| Befehl | Beschreibung |
|:-------|:-------------|
| `sitemap:generate` | Generiert Sitemaps für einen oder alle aktiven Shops |

---

## Snippets

| Befehl | Beschreibung |
|:-------|:-------------|
| `snippets:validate` | Validiert Snippets |

---

## State Machine

| Befehl | Beschreibung |
|:-------|:-------------|
| `state-machine:dump` | Gibt eine State Machine als Graphviz-Datei aus |

---

## Store

| Befehl | Beschreibung |
|:-------|:-------------|
| `store:download` | Lädt ein Plugin aus dem Store herunter |
| `store:login` | Login im Store |

---

## System

| Befehl | Beschreibung |
|:-------|:-------------|
| `system:check` | Prüft die System-Health der Shopware-Applikation |
| `system:config:get` | Liest einen Config-Wert |
| `system:config:set` | Setzt einen Config-Wert |
| `system:configure-shop` | Konfiguriert den Shop |
| `system:generate-app-secret` | Generiert ein neues App-Secret |
| `system:install` | Installiert das Shopware-6-System |
| `system:is-installed` | Prüft ob das System installiert ist (Exit-Code 0 = installiert) |
| `system:setup` | Startet die System-Einrichtung |
| `system:setup:staging` | Installiert Shopware 6 im Staging-Modus |
| `system:update:finish` | Schließt den Update-Prozess ab |
| `system:update:prepare` | Bereitet den Update-Prozess vor |

---

## Theme

| Befehl | Beschreibung |
|:-------|:-------------|
| `theme:change` | Ändert das aktive Theme für einen Sales Channel |
| `theme:compile` | Kompiliert das Theme |
| `theme:create` | Erstellt ein Theme-Skeleton |
| `theme:dump` | Gibt die Theme-Konfiguration aus |
| `theme:prepare-icons` | Bereitet Theme-Icons vor |
| `theme:refresh` | Aktualisiert die Theme-Konfiguration |

---

## Translation

| Befehl | Beschreibung |
|:-------|:-------------|
| `translation:extract` | Extrahiert fehlende Übersetzungskeys aus dem Code |
| `translation:install` | Lädt und installiert Übersetzungen von GitHub |
| `translation:pull` | Lädt Übersetzungen von einem Provider |
| `translation:push` | Pusht Übersetzungen zu einem Provider |

---

## User

| Befehl | Beschreibung |
|:-------|:-------------|
| `user:change-password` | Ändert das Passwort eines Benutzers |
| `user:create` | Erstellt einen neuen Benutzer |
| `user:list` | Listet aktuelle Benutzer auf |
