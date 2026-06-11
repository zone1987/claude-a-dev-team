# Shopware 6 — Update Guides: Vollständige Referenz (Überblick)

## Kapitelstruktur der offiziellen Dokumentation

Die offiziellen Update Guides unter `docs.shopware.com/de/shopware-6-de/update-guides` umfassen:

| Seite | Inhalt |
|---|---|
| Shopware aktualisieren / updaten | Allgemeine Anleitung (alle Methoden) |
| Update Guide 6.4 zu 6.5 | Major-Update-Anleitung |
| Update Guide Shopware 6.6 | Neuerungen & Anforderungen für 6.6 |
| Update Guide 6.5 zu 6.6 | Major-Update-Anleitung |
| Update Guide Shopware 6.7 | Neuerungen & Anforderungen für 6.7 |

---

## Systemanforderungen je Version

### Shopware 6.7 (aktuell)
| Komponente | Anforderung |
|---|---|
| PHP | 8.2, 8.3 oder 8.4 |
| Node.js | 20 oder höher |
| MySQL | 8.0.17+ (nicht 8.0.20, 8.0.21) |
| MariaDB | 10.11+ (nicht 10.11.5 & 11.0.3) |
| Redis | 7.0+ (optional) |
| OpenSearch/Elasticsearch | 1.0+ / 7.8+ (optional) |

### Shopware 6.6
| Komponente | Anforderung |
|---|---|
| PHP | 8.2+ |
| Node.js | 20 |
| MariaDB | 10.11+ |
| Redis | 7.0 (optional) |
| MySQL | 8.0+ |

### Shopware 6.5 (für Update von 6.4)
| Komponente | Anforderung |
|---|---|
| PHP | 8.1+ |
| Node.js | 18 |
| Git | erforderlich |

### Hardware (Empfehlungen)
| Komponente | Minimum | Empfehlung |
|---|---|---|
| CPU | Dual-Core | Quad-Core oder höher |
| RAM | 8 GB | 16 GB |
| Disk | 10 GB frei | 20 GB frei |

---

## Update-Prozess: Schritt-für-Schritt (Überblick)

### Phase 1: Vorbereitung

**1.1 Testumgebung einrichten**
- Separaten Server oder Subdomain aufsetzen
- Produktive Datenbank klonen (anonymisiert)
- Update erst auf Testumgebung durchführen

**1.2 Backup erstellen (PFLICHT)**
- Shopware erstellt kein automatisches Backup
- Datenbank-Dump via `mysqldump` oder Hosting-Panel
- Alle Dateien sichern (var/, public/media/, config/)
- Backup-Speicherort: extern (anderer Server/Cloud)

**1.3 Erweiterungen prüfen**

Drei Kompatibilitäts-Status im Admin:
1. **Bereits kompatibel** — installierte Version läuft mit neuer Shopware-Version
2. **Mit der neuen Shopware Version kompatibel** — Update der Extension nach Shop-Update möglich
3. **Nicht kompatibel** — keine Nachfolgeversion; Extension muss vor Update deaktiviert/gelöscht werden

Kompatibilität prüfen über:
- Shopware Store (store.shopware.com)
- Admin-Panel: Einstellungen > System > Shopware-Update
- Shopware Account: Bereich "Lizenzen"

### Phase 2: Update durchführen

→ Methode wählen: Admin-Panel, Browser-Installer oder Composer+CLI

### Phase 3: Nachbereitung
- Erweiterungen aktualisieren (Store oder Composer)
- Erweiterungen reaktivieren
- Theme neu kompilieren (bei CLI: `bin/console theme:compile`)
- Storefront testen
- Cache leeren: `bin/console cache:clear`

---

## Wichtige Warnhinweise

> **KRITISCH:** Beim Major-Update (6.4→6.5 oder 6.5→6.6) MÜSSEN ALLE Erweiterungen deaktiviert werden — auch kompatible. Das Theme muss auf den Standard-Theme gesetzt werden.

> **WICHTIG:** Composer-Update ist stabiler als Admin-Update (keine PHP-Timeouts bei großen Shops).

> **HINWEIS:** Inkompatible Erweiterungen können das Update abbrechen oder den Shop blockieren.

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/update-guides*
