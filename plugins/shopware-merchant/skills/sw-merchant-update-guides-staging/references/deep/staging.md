# Shopware 6 — Staging & Testumgebung: Vollständige Referenz

## Begriffe und Unterschiede

### Staging-Umgebung
Eine vollständig separate, nicht-produktive Kopie des Live-Shops mit:
- **Eigenem Hosting** (separater Server oder Container)
- **Eigener Domain** (z.B. staging.meinshop.de)
- **Eigener Datenbank** (Klon der Live-DB)
- **Eigenem Redis-Instanz** (getrennt von Live!)
- **Eigenem Elasticsearch/OpenSearch-Index-Präfix**
- **Eigener .env-Konfiguration**

### Staging-Modus (seit Shopware 6.6.1.0)
Ein Shopware-Mechanismus aktiviert via `bin/console system:setup:staging`, der:
- App-Verbindungen zur Produktion trennt
- E-Mail-Versand deaktiviert
- URLs zur Staging-Domain umschreibt
- Banner in Admin und Storefront anzeigt

> **Kritisch:** `system:setup:staging` dupliziert KEINE Datenbank und KEINE Dateien — das muss separat erledigt werden.

---

## 4-Schritte-Prozess: Staging-Instanz einrichten

### Schritt 1: Separate Installation einrichten

**Empfohlen:** Aus dem Git-Repository in die neue Umgebung deployen.

```bash
# Neue Domain/Subdomain einrichten
# z.B.: staging.meinshop.de

# .env anpassen
APP_URL=https://staging.meinshop.de
APP_ENV=prod
APP_SECRET=<neues-geheimes-secret>
```

> **Lizenz-Hinweis:** In der Shopware Account Lizenz weiterhin die **Live-Domain** verwenden, um Lizenzprobleme zu vermeiden. Shopware toleriert Staging-Instanzen unter anderen Domains.

### Schritt 2: Datenbank klonen

#### Option A: shopware-cli (empfohlen)

```bash
# Standard-Dump (ohne Cart-Daten, "clean")
shopware-cli project dump \
  --clean \
  --host localhost \
  --username db_user \
  --password db_pass \
  --output shop.sql \
  shopware_datenbankname

# Dump mit anonymisierten Kundendaten (DSGVO-konform)
shopware-cli project dump \
  --clean \
  --anonymize \
  --host localhost \
  --username db_user \
  --password db_pass \
  --output shop-anon.sql \
  shopware_datenbankname
```

**Was --anonymize anonymisiert:**
- Kundennamen → zufällige Namen
- E-Mail-Adressen → example.com-Adressen
- Telefonnummern → zufällige Nummern
- Adressen → generische Adressen

#### Option B: mysqldump (klassisch)

```bash
# Vollständiger Dump
mysqldump -u user -p --single-transaction shopware_db > backup.sql

# Dump ohne Session/Log-Tabellen (schneller)
mysqldump -u user -p --single-transaction \
  --ignore-table=shopware_db.messenger_messages \
  --ignore-table=shopware_db.dead_message \
  shopware_db > backup.sql
```

> **Warnung:** `mysqldump` und `mysql` müssen dieselbe Hauptversion und denselben Anbieter (MySQL/MariaDB) haben.

#### Dump auf Staging-Datenbank einspielen

```bash
# Staging-Datenbank vorbereiten
mysql -u staging_user -p -e "CREATE DATABASE IF NOT EXISTS staging_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Dump einspielen
mysql -u staging_user -p staging_db < shop-anon.sql

# Mit Fortschrittsanzeige (pv muss installiert sein)
pv shop-anon.sql | mysql -u staging_user -p staging_db
```

### Schritt 3: Staging konfigurieren

#### .env für Staging anpassen

```bash
# Staging .env (config/packages/.env oder .env.local)
APP_URL=https://staging.meinshop.de
DATABASE_URL=mysql://staging_user:password@localhost:3306/staging_db

# Redis (GETRENNT von Live!)
REDIS_URL=redis://localhost:6380

# Elasticsearch/OpenSearch (GETRENNT von Live!)
SHOPWARE_ES_INDEX_PREFIX=staging_
SHOPWARE_ES_HOSTS=localhost:9200

# Oder Elasticsearch komplett deaktivieren für Staging
SHOPWARE_ES_ENABLED=0
```

> **KRITISCH:** Redis und Elasticsearch NIEMALS zwischen Live und Staging teilen. Unterschiedliche Daten → Datenverlust und Inkonsistenzen.

#### staging.yaml Konfiguration

Datei erstellen: `config/packages/staging.yaml`

```yaml
shopware:
    staging:
        mailing:
            disable_delivery: true      # Keine Mails an echte Kunden!
        storefront:
            show_banner: true           # Staging-Banner in Storefront
        administration:
            show_banner: true           # Staging-Banner in Admin
        sales_channel:
            domain_rewrite: []          # URL-Umschreibung konfigurieren
        elasticsearch:
            check_for_existence: true   # Prüft ob ES-Index bereits existiert
```

#### URL-Umschreibung (drei Methoden)

**Methode 1: Direkter Austausch (equal)**
```yaml
shopware:
    staging:
        sales_channel:
            domain_rewrite:
                - type: equal
                  match: https://www.meinshop.de
                  replace: https://staging.meinshop.de
```

**Methode 2: Präfix-Ersetzung (prefix)**
```yaml
shopware:
    staging:
        sales_channel:
            domain_rewrite:
                - type: prefix
                  match: https://www.meinshop.de
                  replace: https://staging.meinshop.de
```

**Methode 3: Regex-Ersetzung (regex)**
```yaml
shopware:
    staging:
        sales_channel:
            domain_rewrite:
                - type: regex
                  match: '/https?:\/\/(\w+)\.(\w+)$/m'
                  replace: 'http://$1-$2.local'
```

### Schritt 4: Staging-Modus aktivieren

```bash
# Interaktiv (Bestätigung erforderlich)
bin/console system:setup:staging

# Nicht-interaktiv (für Scripts/CI)
bin/console system:setup:staging --no-interaction --force
```

**Was der Befehl ausführt:**
1. Löscht alle Apps mit aktiven externen Verbindungen
2. Setzt Instanz-ID zurück (verhindert App-Konflikte mit Live)
3. Deaktiviert E-Mail-Versand
4. Schreibt Sales-Channel-URLs um (aus domain_rewrite-Konfiguration)
5. Verifiziert Elasticsearch-Indizes (auf Existenz prüfen)
6. Aktiviert Staging-Banner in Admin und Storefront

---

## Was der Staging-Modus NICHT tut

| Nicht enthalten | Muss separat erledigt werden |
|---|---|
| Datenbank duplizieren | mysqldump / shopware-cli project dump |
| Dateien kopieren | rsync / Hosting-Tools |
| Live-Umgebung modifizieren | — |
| Hosting einrichten | Hosting-Provider / DevOps |

---

## App-Verwaltung nach Staging-Aktivierung

Der Staging-Befehl **löscht alle Apps** mit externen Verbindungen (Shopware App Server, externe APIs).

Nach Staging-Aktivierung:
```bash
# Apps neu installieren (generiert neue Instanz-IDs)
bin/console app:install <app-name>
# oder über Admin: Erweiterungen > Apps > Installieren
```

Für Plugin-Entwickler: Staging-Event abonnieren
```php
use Shopware\Core\Maintenance\Staging\Event\SetupStagingEvent;

public static function getSubscribedEvents(): array
{
    return [SetupStagingEvent::class => 'onSetupStaging'];
}

public function onSetupStaging(SetupStagingEvent $event): void
{
    // Eigene Staging-Initialisierung
    // z.B. Test-API-Keys setzen, Webhooks deaktivieren
}
```

---

## Staging-Umgebung schützen

Die Staging-Umgebung sollte vor öffentlichem Zugang geschützt werden:

### Apache: Basic Auth
```apache
# .htaccess im Web-Root
AuthType Basic
AuthName "Staging"
AuthUserFile /pfad/zu/.htpasswd
Require valid-user
```

```bash
# .htpasswd erstellen
htpasswd -c /pfad/zu/.htpasswd staging_user
```

### Nginx: Basic Auth
```nginx
server {
    auth_basic "Staging";
    auth_basic_user_file /pfad/zu/.htpasswd;
}
```

### IP-Beschränkung (Apache)
```apache
Order Deny,Allow
Deny from all
Allow from 192.168.1.0/24
Allow from 10.0.0.100
```

### IP-Beschränkung (Nginx)
```nginx
allow 192.168.1.0/24;
allow 10.0.0.100;
deny all;
```

### Cloudflare Access / Azure Application Gateway
- OAuth2-Proxy-Lösung
- Mitarbeiter-Login via SSO
- Keine separate Passwort-Verwaltung nötig

---

## Testumgebung für Updates: Best Practices

### Workflow für Update-Tests

1. **Datenbank-Snapshot erstellen** (Live → Staging)
2. **Dateien synchronisieren** (`rsync` von Live → Staging)
3. **Staging-Modus aktivieren** (`system:setup:staging`)
4. **Update auf Staging durchführen** (Admin oder Composer)
5. **Testen:** Storefront, Admin, Bestellprozess, Extensions
6. **Falls OK:** Update auf Live durchführen
7. **Falls Fehler:** Staging für Debugging nutzen; Live unangetastet

### Checkliste nach Update auf Staging

- [ ] Startseite lädt korrekt
- [ ] Admin-Login funktioniert
- [ ] Produkte werden angezeigt
- [ ] Bestellung aufgeben möglich (Testbestellung)
- [ ] Alle aktivierten Extensions funktionieren
- [ ] Theme wird korrekt dargestellt
- [ ] E-Mails werden NICHT versendet (Staging-Modus aktiv)
- [ ] Keine PHP-Fehler in den Logs (`var/log/`)

---

*Quelle: https://developer.shopware.com/docs/guides/hosting/installation-updates/creating-a-staging-instance.html*
*Ergänzend: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
