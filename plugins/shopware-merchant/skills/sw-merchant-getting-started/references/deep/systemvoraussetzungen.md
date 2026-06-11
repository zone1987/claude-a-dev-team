# Systemvoraussetzungen Shopware 6

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/systemvoraussetzungen  
**Detaillierte Technik-Doku**: https://developer.shopware.com/docs/guides/installation/system-requirements.html

## Überblick

Vor der Installation von Shopware 6 müssen Server-Voraussetzungen erfüllt sein.
Die folgende Übersicht gilt für **Shopware 6.7.x** (aktuell).

---

## Unterstützte Betriebssysteme

- Nur **Unix-basierte Systeme** werden unterstützt:
  - Linux (64-bit Distributionen)
  - macOS 13 oder neuer
  - Windows 10/11 Pro mit WSL 2 oder Docker Desktop

---

## Software-Anforderungen

### PHP
| Shopware Version | Minimale PHP-Version | Empfohlene PHP-Version |
|---|---|---|
| 6.7.x | PHP 8.2 | PHP 8.3 |
| 6.6.x | PHP 8.1 | PHP 8.2 |
| 6.5.x | PHP 8.1 | PHP 8.2 |
| 6.4.x | PHP 7.4 | PHP 8.1 |

**PHP-Extensions (Pflicht)**:
- `curl`, `dom`, `fileinfo`, `gd`, `iconv`, `intl`, `json`
- `libxml`, `mbstring`, `pdo`, `pdo_mysql`, `openssl`
- `simplexml`, `xml`, `zip`, `zlib`

### Datenbank
| System | Mindestversion | Empfohlen |
|---|---|---|
| MySQL | 8.0 | 8.0+ |
| MariaDB | 10.11 | 10.11+ |
| Percona | 8.0 | 8.0+ |

### Webserver
- **Nginx** (empfohlen) ab 1.20
- **Apache** ab 2.4 (mit mod_rewrite)
- Shopware benötigt: `public/` als Document Root

### Node.js (für Theme-Entwicklung)
- Node.js 20+ (für Frontend-Kompilierung)
- Nur relevant für Theme- und Plugin-Entwicklung

---

## Hardware-Empfehlungen

| Komponente | Minimum | Empfohlen |
|---|---|---|
| CPU | 2 Kerne | 4+ Kerne |
| RAM | 4 GB | 8-16 GB |
| Disk | 10 GB frei | 20+ GB SSD |
| Netzwerk | Stabile Verbindung | — |

---

## Shopware Cloud vs. Self-Hosted

| Aspekt | Shopware Cloud | Self-Hosted |
|---|---|---|
| Server-Setup | Nicht nötig | Eigenverantwortlich |
| Systemvoraussetzungen | Automatisch erfüllt | Manuell einzurichten |
| Updates | Automatisch | Manuell oder automatisiert |
| Anpassbarkeit | Eingeschränkt | Vollständig |

---

## Installation

### Über den Shopware Installer
1. Shopware herunterladen: https://www.shopware.com/de/download/
2. ZIP entpacken auf dem Server
3. Verzeichnis-Berechtigungen setzen (write für `var/`, `public/`, `config/`)
4. Browser: `https://meinshop.de/public/recovery/install/` aufrufen
5. System-Check → Lizenz → Datenbank → Import → Shop-Konfiguration

### Über Composer (Entwickler)
```bash
composer create-project shopware/production:^6.7 meinshop
cd meinshop
php bin/console system:setup
php bin/console system:install --create-database
php bin/console user:create --admin admin
```

---

## Weiterführende Links

- Vollständige Entwickler-Systemanforderungen: https://developer.shopware.com/docs/guides/installation/system-requirements.html
- Docker-Setup-Guide: https://developer.shopware.com/docs/guides/installation/docker.html
- Hosting-Partner: https://www.shopware.com/de/hosting/
