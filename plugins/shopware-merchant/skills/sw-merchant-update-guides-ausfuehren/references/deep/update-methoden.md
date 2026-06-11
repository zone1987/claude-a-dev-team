# Shopware 6 — Update-Methoden: Vollständige Referenz

## Überblick der drei Update-Methoden

| Methode | Verfügbar seit | Timeout-Risiko | Technisches Know-how |
|---|---|---|---|
| Admin-Panel (GUI) | 6.0 | Möglich bei großen Shops | Niedrig |
| Browser-Installer (PHP-Datei) | 6.0 | Gering | Niedrig (FTP) |
| Composer + CLI | 6.3.0 | Kein | Mittel–Hoch |

---

## Methode 1: Admin-Panel (Schritt-für-Schritt)

**Navigationspfad:** Einstellungen > System > Shopware-Update

### Schritt 1: Systemvoraussetzungen prüfen
Das Admin-Panel führt einen Systemcheck durch:
- **Grüne Indikatoren** = Voraussetzung erfüllt
- **Rote Indikatoren** = Problem; muss behoben werden bevor Update möglich

Typische rote Indikatoren:
- PHP-Version zu alt
- fehlende PHP-Extensions
- Dateirechte-Probleme (var/, public/)
- Datenbankverbindung fehlerhaft

### Schritt 2: Erweiterungs-Kompatibilität

Admin zeigt alle installierten Erweiterungen mit Status:

| Status | Bedeutung | Aktion |
|---|---|---|
| Bereits kompatibel | Läuft direkt mit neuer SW-Version | Nichts tun |
| Mit neuer SW-Version | Update der Extension nach SW-Update möglich | Extension nach Update updaten |
| Nicht kompatibel | Keine kompatible Version verfügbar | Deaktivieren/löschen VOR Update |

### Schritt 3: Backup-Bestätigung

Häkchen setzen: "Ja, ich habe meine Daten gesichert"
→ Erst dann wird "Installieren" aktiv

### Schritt 4: Deaktivierungsoptionen

| Option | Wann nutzen |
|---|---|
| Alle Erweiterungen deaktivieren | Empfohlen bei Major-Updates; sicherste Methode |
| Inkompatible deaktivieren | Nur für Minor-Updates mit bekannten kompatiblen Extensions |
| Ich bin mir der Gefahren bewusst | Nur wenn alle Extensions definitiv kompatibel; riskant |

### Schritt 5: Update durchführen

Nach Auswahl und Bestätigung startet der Update-Prozess. Grüne Häkchen auf der linken Seite zeigen den Fortschritt.

---

## Methode 2: Browser-Installer

**Geeignet für:** Shared Hosting ohne SSH/Shell-Zugang

### Schritt-für-Schritt

1. **PHP-Datei herunterladen**
   - URL: im Shopware Changelog-Downloadbereich (Version > Download)
   - Dateiname: `shopware-installer.phar.php`

2. **Datei hochladen via FTP**
   - Zielverzeichnis: `public/` (Web-Root des Shops)
   - **WICHTIG: Binären Übertragungsmodus verwenden!**
     - FileZilla: Übertragung → Übertragungstyp → Binär
     - Falsche Übertragung (ASCII) korrumpiert die PHP-Datei

3. **Installer im Browser aufrufen**
   ```
   https://www.meine-shop-domain.de/shopware-installer.phar.php
   ```

4. **Automatischer Ablauf**
   - Installer erkennt bestehende Installation → Update-Modus
   - Zeigt Fortschrittsscreens
   - Abschluss: Erfolgsmeldung

### Logik des Installers

| Zustand public/ | Modus |
|---|---|
| Leer (keine Installation) | Neuinstallation |
| Bestehende Shopware-Installation | Update |

---

## Methode 3: Composer + CLI (vollständige Referenz)

**Verfügbar seit:** Shopware 6.3.0

**Vorteile:**
- Keine PHP-Timeouts
- Reproduzierbar (Git, CI/CD)
- Vollständige Kontrolle über Versionen
- Empfohlen von Shopware für professionelle Umgebungen

### Vollständige Befehlssequenz (Produktionsserver)

```bash
# ===== VORBEREITUNG =====

# 1. Kompatibilitäts-Check (benötigt shopware-cli)
shopware-cli project upgrade-check

# 2. Wartungsmodus für alle Sales Channels aktivieren
bin/console sales-channel:maintenance:enable --all

# 3. Update vorbereiten (Datenbank-Locks, Pre-Migration-Checks)
bin/console system:update:prepare

# ===== VERSION ANPASSEN (lokal, nicht auf Server) =====

# 4. composer.json bearbeiten — Zielversion setzen
# Beispiel: Update auf Shopware 6.7.0.0
# {
#   "require": {
#     "shopware/core": "6.7.0.0",
#     "shopware/administration": "6.7.0.0",
#     "shopware/storefront": "6.7.0.0",
#     "shopware/elasticsearch": "6.7.0.0"  // nur wenn genutzt
#   }
# }

# ===== DEPENDENCIES AKTUALISIEREN =====

# 5. Composer Update (--no-scripts verhindert vorzeitige Ausführung)
composer update --no-scripts

# 6. Symfony Flex Recipes aktualisieren
#    (aktualisiert config/packages/*.yaml, .env.dist, etc.)
composer recipes:update

# ===== CODE DEPLOYEN =====

# 7. Geänderte Dateien committen und deployen
git add composer.json composer.lock
git commit -m "Update Shopware to 6.7.0.0"
# Deploy via eigenen Deploy-Prozess

# ===== DATENBANKMIGRATIONEN =====

# 8. Datenbankmigrationen ausführen
bin/console system:update:finish

# ===== NACHBEREITUNG =====

# 9. Theme kompilieren
bin/console theme:compile

# 10. Cache leeren
bin/console cache:clear

# 11. Optionale Indizes neu aufbauen (bei Elasticsearch/OpenSearch)
bin/console es:index

# 12. Wartungsmodus deaktivieren
bin/console sales-channel:maintenance:disable --all
```

### Lokale Entwicklungsumgebung (vereinfacht)

```bash
# 1. Version in composer.json anpassen
# 2. Composer Update
composer update --no-scripts

# 3. Symfony Flex Recipes
composer recipes:update

# 4. Commit & Push → Deploy auf Server
git add composer.json composer.lock
git commit -m "Update Shopware to X.X.X.X"
```

### Bekannte Fehler und Lösungen

**Fehler 1: APP_ENV=dev web_profiler-Fehler (Shopware < 6.4.17.0)**
```bash
composer require --dev profiler
```

**Fehler 2: framework:demo-data Faker-Fehler (Shopware < 6.4.17.0)**
```bash
composer require --dev mbezhanov/faker-provider-collection maltyxx/images-generator
```

**Fehler 3: Composer Memory Limit**
```bash
COMPOSER_MEMORY_LIMIT=-1 composer update --no-scripts
```

**Fehler 4: Dependency Konflikt nach Update**
```bash
composer why-not shopware/core 6.7.0.0
# Zeigt welche Pakete inkompatibel sind
```

---

## Troubleshooting: Erweiterungen lassen sich nicht deaktivieren

### Problem
Der Auto-Updater kann inkompatible Extensions nicht deaktivieren → Update schlägt fehl.

### Lösung 1: "Alle Erweiterungen deaktivieren" wählen
Im Admin-Update-Dialog: "Alle Erweiterungen deaktivieren" wählen statt "Inkompatible deaktivieren".

### Lösung 2: Manuelle Deaktivierung im Admin
Admin > Erweiterungen > Meine Erweiterungen → jede Extension einzeln deaktivieren
Dann Update ohne Deaktivierungsoption im Updater starten.

### Lösung 3: SQL-Deaktivierung (bei hartnäckigen Fällen)

```sql
-- Minor-Update: Nur inkompatible deaktivieren
UPDATE plugin SET active = 0 WHERE active = 1 AND name IN (
    'InkompatiblesPlugin1', 'InkompatiblesPlugin2'
);

-- Major-Update (6.4 → 6.5 oder 6.5 → 6.6): ALLE deaktivieren
UPDATE plugin SET active = 0;

-- Nach SQL-Deaktivierung: Theme auf Standard setzen
UPDATE theme SET active = 1 WHERE technical_name = 'Storefront';
UPDATE theme SET active = 0 WHERE technical_name != 'Storefront';
```

> **WICHTIG:** Nach SQL-Deaktivierung im Updater-Dialog KEINE Deaktivierungsoption mehr wählen.

### Lösung 4: shopware-cli
```bash
shopware-cli extension deactivate <extension-technical-name>
```

---

## Wartungsmodus: Vollständige Referenz

### Per CLI (alle Sales Channels)
```bash
# Aktivieren
bin/console sales-channel:maintenance:enable --all

# Deaktivieren
bin/console sales-channel:maintenance:disable --all
```

### Per CLI (einzelner Sales Channel)
```bash
# Sales Channel IDs ermitteln
bin/console debug:container

# Aktivieren für spezifischen Kanal
bin/console sales-channel:maintenance:enable <uuid-des-sales-channels>

# Deaktivieren
bin/console sales-channel:maintenance:disable <uuid-des-sales-channels>
```

### Per Admin-Panel
Admin > Einstellungen > Verkaufskanäle > [Kanal auswählen] > Reiter "Allgemein" > Wartungsmodus

### IP-Ausnahmen für Wartungsmodus
In `config/packages/shopware.yaml`:
```yaml
shopware:
    maintenance:
        ip_whitelist:
            - '192.168.1.100'
            - '10.0.0.0/24'
```

---

## Rollback-Prozess

### Voraussetzung: Backup vorhanden

#### Schritt 1: Wartungsmodus aktivieren (falls nicht bereits aktiv)
```bash
# CLI
bin/console sales-channel:maintenance:enable --all

# oder manuell: .maintenance file im Shop-Root anlegen
touch .maintenance
```

#### Schritt 2: Datenbankbackup einspielen
```bash
# Datenbank löschen und neu einlesen
mysql -u user -p -e "DROP DATABASE shopware; CREATE DATABASE shopware;"
mysql -u user -p shopware < backup-vor-update-DATUM.sql

# Alternativ mit pv (Fortschrittsanzeige):
pv backup-vor-update-DATUM.sql | mysql -u user -p shopware
```

#### Schritt 3: Dateien zurücksetzen

**Via Composer:**
```bash
# composer.json auf alte Version zurücksetzen (aus Git)
git checkout composer.json composer.lock
composer install --no-dev
```

**Via Datei-Backup:**
```bash
# Backup entpacken und überschreiben
tar -xzf shop-backup-vor-update.tar.gz -C /pfad/zum/shop/
```

#### Schritt 4: Cache leeren
```bash
bin/console cache:clear

# Alternativ manuell:
rm -rf var/cache/prod_* var/cache/dev_*
```

#### Schritt 5: Wartungsmodus deaktivieren
```bash
bin/console sales-channel:maintenance:disable --all
# oder:
rm .maintenance
```

#### Schritt 6: Shop testen
- Storefront aufrufen
- Admin-Login prüfen
- Bestellprozess testen

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
*Ergänzend: https://developer.shopware.com/docs/guides/hosting/installation-updates/performing-updates.html*
