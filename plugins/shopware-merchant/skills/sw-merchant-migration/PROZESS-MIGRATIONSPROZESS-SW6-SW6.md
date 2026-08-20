# Migrationsprozess: Shopware 6 → Shopware 6

**Quelle**: https://docs.shopware.com/de/migration-de/shopware6-Migrationsprozess

---

## Anwendungsfälle

- Umzug in die Shopware Cloud (SaaS)
- Server-Wechsel / Hosting-Wechsel
- Staging-Instanz → Live-Instanz übertragen

---

## Kritische Voraussetzung

> ⚠️ **Quell- und Zielsystem müssen dieselbe Shopware-Version verwenden.**
> Eine Migration zwischen unterschiedlichen Versionen ist **nicht möglich**.

---

## Unterschiede zu SW5→SW6

- **Kein SwagMigrationConnector** im Quellshop nötig (kein separater Connector)
- Im Quellshop muss ebenfalls der **SwagMigrationAssistent** installiert und aktiv sein
- Verbindungstyp ist **ausschließlich API** (kein Local-Modus)
- Profil: **„Shopware 6"** im Assistenten wählen

---

## Schritt 1: Erweiterungen installieren

### Im Quellshop (SW6)
- **SwagMigrationAssistent** installieren und aktivieren

### Im Zielshop (SW6)
- **SwagMigrationAssistent** installieren und aktivieren
- Ab Version **16.0.0** des Assistenten

---

## Schritt 2: Integration im Quellshop anlegen

**Pfad:** Einstellungen > System > Integrationen > Integration anlegen

| Feld | Beschreibung |
|---|---|
| **Name** | z.B. „Migration" |
| **Administrator** | Checkbox aktivieren (Pflicht!) |
| **Zugangs-ID** | Automatisch generiert — zwischenspeichern! |
| **Sicherheitsschlüssel** | Automatisch generiert — zwischenspeichern! |

Speichern mit: **„Integration speichern"**

---

## Schritt 3: Verbindung im Zielshop herstellen

**Pfad:** Einstellungen > Erweiterungen > Migrations-Assistent

1. **„Initiale Verbindung anlegen"** anklicken
2. Profil: **„Shopware 6"** wählen
3. **„Fortfahren"**
4. Verbindung konfigurieren:

| Feld | Inhalt |
|---|---|
| **Name** | Eindeutiger Verbindungsname |
| **Profil** | Shopware 6 |
| **Schnittstelle** | API (einzige Option) |
| **Zugangs-ID** | Aus Schritt 2 |
| **Sicherheitsschlüssel** | Aus Schritt 2 |
| **Shopdomain** | URL des Quellshops |

> ⚠️ Keine Bindestriche im Verbindungsnamen!

---

## Schritt 4–6: Daten prüfen, Migration starten, Livegang

Der weitere Ablauf entspricht der SW5→SW6-Migration:
→ Detaildoku: `references/deep/migrationsprozess-sw5-sw6.md`

---

*Quelle: https://docs.shopware.com/de/migration-de/shopware6 | https://docs.shopware.com/de/migration-de/shopware6-Migrationsprozess*
