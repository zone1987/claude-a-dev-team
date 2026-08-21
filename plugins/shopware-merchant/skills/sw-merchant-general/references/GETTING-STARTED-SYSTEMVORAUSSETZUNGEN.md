# System requirements Shopware 6

**Source**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/systemvoraussetzungen  
**Detailed technical documentation**: https://developer.shopware.com/docs/guides/installation/system-requirements.html

## Contents

- [Overview](#overview)
- [Supported operating systems](#supported-operating-systems)
- [Software requirements](#software-requirements)
- [Hardware recommendations](#hardware-recommendations)
- [Shopware Cloud vs. self-hosted](#shopware-cloud-vs-self-hosted)
- [Installation](#installation)
- [Further links](#further-links)

## Overview

Server prerequisites have to be met before installing Shopware 6.
The following overview applies to **Shopware 6.7.x** (current).

---

## Supported operating systems

- Only **Unix-based systems** are supported:
  - Linux (64-bit distributions)
  - macOS 13 or newer
  - Windows 10/11 Pro with WSL 2 or Docker Desktop

---

## Software requirements

### PHP
| Shopware version | Minimum PHP version | Recommended PHP version |
|---|---|---|
| 6.7.x | PHP 8.2 | PHP 8.3 |
| 6.6.x | PHP 8.1 | PHP 8.2 |
| 6.5.x | PHP 8.1 | PHP 8.2 |
| 6.4.x | PHP 7.4 | PHP 8.1 |

**PHP extensions (mandatory)**:
- `curl`, `dom`, `fileinfo`, `gd`, `iconv`, `intl`, `json`
- `libxml`, `mbstring`, `pdo`, `pdo_mysql`, `openssl`
- `simplexml`, `xml`, `zip`, `zlib`

### Database
| System | Minimum version | Recommended |
|---|---|---|
| MySQL | 8.0 | 8.0+ |
| MariaDB | 10.11 | 10.11+ |
| Percona | 8.0 | 8.0+ |

### Web server
- **Nginx** (recommended) from 1.20
- **Apache** from 2.4 (with mod_rewrite)
- Shopware requires: `public/` as the document root

### Node.js (for theme development)
- Node.js 20+ (for frontend compilation)
- Only relevant for theme and plugin development

---

## Hardware recommendations

| Component | Minimum | Recommended |
|---|---|---|
| CPU | 2 cores | 4+ cores |
| RAM | 4 GB | 8-16 GB |
| Disk | 10 GB free | 20+ GB SSD |
| Network | Stable connection | — |

---

## Shopware Cloud vs. self-hosted

| Aspect | Shopware Cloud | Self-hosted |
|---|---|---|
| Server setup | Not needed | Your own responsibility |
| System requirements | Automatically met | To be set up manually |
| Updates | Automatic | Manual or automated |
| Customisability | Restricted | Complete |

---

## Installation

### Via the Shopware installer
1. Download Shopware: https://www.shopware.com/de/download/
2. Extract the ZIP on the server
3. Set directory permissions (write for `var/`, `public/`, `config/`)
4. Browser: open `https://meinshop.de/public/recovery/install/`
5. System check → licence → database → import → shop configuration

### Via Composer (developers)
```bash
composer create-project shopware/production:^6.7 meinshop
cd meinshop
php bin/console system:setup
php bin/console system:install --create-database
php bin/console user:create --admin admin
```

---

## Further links

- Full developer system requirements: https://developer.shopware.com/docs/guides/installation/system-requirements.html
- Docker setup guide: https://developer.shopware.com/docs/guides/installation/docker.html
- Hosting partners: https://www.shopware.com/de/hosting/
