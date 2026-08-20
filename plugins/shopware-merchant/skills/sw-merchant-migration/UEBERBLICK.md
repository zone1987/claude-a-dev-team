# Migration zu Shopware 6 — Überblick

**Quelle**: https://docs.shopware.com/de/migration-de

## Was bedeutet Migration in Shopware?

Migration bedeutet **Neuanfang auf grüner Wiese** — ein komplett neuer Shop wird aufgebaut und Daten
aus dem bestehenden System werden übertragen. Es ist kein automatisches Upgrade des alten Systems,
sondern ein paralleler Aufbau mit anschließendem Datentransfer.

Shopware 6 enthält einen **Migrationsassistenten** (Erweiterung), der Daten aus dem Quellsystem
(Shopware 5, Shopware 6, Magento) in den neuen Shop überträgt: Kunden, Bestellungen, Produkte u.v.m.

---

## Unterstützte Quellsysteme

### Shopware 5 → Shopware 6
Die vollständigste Migration. Alle typischen Shop-Daten übertragbar.
- Plugin: `SwagMigrationConnector` im SW5-Shop
- Plugin: `SwagMigrationAssistent` im SW6-Shop (ab v16.0.0)
- Unterseite: `docs.shopware.com/de/migration-de/shopware5`

### Shopware 6 → Shopware 6
Umzug zwischen zwei SW6-Instanzen (z.B. Self-hosted → Cloud, Server-Wechsel, Staging → Live).
- **Bedingung:** Quell- und Zielsystem müssen **identische Shopware-Version** haben.
- Unterseite: `docs.shopware.com/de/migration-de/shopware6`

### Magento → Shopware 6
Migration von Magento zu Shopware 6 mit Magento-Wörterbuch (Begriff-Mapping).
- Unterseite: `docs.shopware.com/de/migration-de/magento`

---

## Drei Migrationsphasen

### Phase 1: Vorbereitungsphase
- **Was kann/wird migriert?** — Datenliste prüfen
- **Systemvoraussetzungen prüfen** — Server-Kompatibilität
- **Migrationsumgebung erstellen** — Lizenz, Plan buchen (bei Shopware Professional)
- **Shopware 6 installieren** — neue Instanz aufsetzen

### Phase 2: Migrationsphase
- **Migrationsprozess** — Erweiterungen installieren, Verbindung herstellen, Daten transferieren
- **Upgrade Guide** — manuelle Nacharbeiten nach der Migration
- **Fehlerbehebung** — Probleme im Migrationsprozess lösen

### Phase 3: Abschlussphase
- **Livegang** — Shopware Account, Domain-Routing, Verkaufskanäle umstellen

---

## Was wird migriert? (Shopware 5 → 6, Überblick)

Vollständige Liste: `references/deep/was-wird-migriert.md`

Typisch übertragbare Daten:
- Produkte (inkl. Varianten, Eigenschaften)
- Kategorien
- Kunden und Kundenadressen
- Bestellungen und Bestellpositionen
- Medien (Bilder etc.)
- Hersteller
- Steuerregeln

---

## Systemvoraussetzungen

Vor der Migration prüfen:
1. Server erfüllt SW6-Anforderungen (→ developer.shopware.com/docs/guides/installation/)
2. Für SW5: **SwagMigrationAssistent** im SW5-Shop installieren
   - Zugriff: Backend > Fragezeichen-Symbol > "Shopware 6 Update-Check"
   - Tab "Voraussetzungen": zeigt erfüllte/nicht erfüllte Serveranforderungen
   - Tab "Plugins": zeigt welche Plugins für SW6 verfügbar sind

---

## Migrationsumgebung / Lizenz

Für **Shopware Professional**-Nutzer: Informationsseite über Planwechsel und Unterschiede zwischen Editionen.
Für **Partner**: Wildcard-Umgebungen verfügbar (Partnerbereich der Doku).

---

## Installation Shopware 6

Vollständige Installationsanleitung in der Entwicklerdokumentation:
`https://developer.shopware.com/docs/guides/installation/`
(inkl. Docker-Installation, technische Voraussetzungen, weitere Hinweise)

---

*Quelle: https://docs.shopware.com/de/migration-de | https://docs.shopware.com/de/migration-de/shopware5 | https://docs.shopware.com/de/migration-de/shopware6*
