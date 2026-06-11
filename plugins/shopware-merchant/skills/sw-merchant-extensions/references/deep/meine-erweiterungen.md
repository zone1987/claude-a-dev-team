# Meine Erweiterungen – Verwaltungszentrum

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen  
**Pfad im Admin**: Erweiterungen > Meine Erweiterungen

## Überblick

Der Bereich **Erweiterungen** ist das zentrale Verwaltungszentrum für alle installierten
und verfügbaren Erweiterungen in Shopware 6. Er ermöglicht das Erweitern des
Standard-Funktionsumfangs durch Apps, Plugins und Themes.

---

## Navigationsstruktur

```
Erweiterungen
├── Store          → Shopware Erweiterungsmarktplatz (browsen & kaufen)
└── Meine Erweiterungen
    ├── Apps-Tab   → Installierte Apps
    ├── Plugins-Tab → Installierte Plugins
    └── Themes-Tab  → Installierte Themes
```

---

## Erweiterung installieren

### Aus dem Shopware Store (Online)
1. **Erweiterungen > Store** öffnen
2. Erweiterung suchen (z. B. "PayPal", "Klarna")
3. **Hinzufügen** oder **Kaufen** klicken
4. Shopware Account muss verknüpft sein (Tab: Shopware Account)
5. Nach dem Kauf erscheint die Erweiterung unter **Meine Erweiterungen**
6. **Installieren** klicken → **Aktivieren** klicken

### Manuell (ZIP-Upload)
1. **Erweiterungen > Meine Erweiterungen** öffnen
2. **Erweiterung hochladen** (ZIP-Datei)
3. Installieren + Aktivieren

### Per Composer (Entwickler-Weg)
```bash
composer require shopware/[extension-name]
php bin/console plugin:refresh
php bin/console plugin:install --activate [PluginName]
```

---

## Erweiterung aktivieren / deaktivieren

| Aktion | Vorgehen | Effekt |
|---|---|---|
| Aktivieren | Toggle-Schalter → ON | Erweiterung läuft; Shop-Cache wird geleert |
| Deaktivieren | Toggle-Schalter → OFF | Erweiterung bleibt installiert, aber inaktiv |
| Deinstallieren | Drei-Punkte-Menü > Deinstallieren | Entfernt Code; Daten optional löschen |

> **Hinweis**: Bei Aktivierung/Deaktivierung wird der Shop-Cache automatisch geleert.
> Bei großen Shops kann das kurze Ladezeiten verursachen.

---

## Erweiterung konfigurieren

Nach der Aktivierung kann eine Erweiterung konfiguriert werden:

1. **Drei-Punkte-Menü** (⋮) neben der Erweiterung → **Konfigurieren**
2. Oder direkt über: **Einstellungen > Erweiterungen > [Erweiterungsname]**

---

## Erweiterung aktualisieren

- Im Bereich **Meine Erweiterungen** erscheint ein **Update-Badge** bei neuen Versionen
- Glocken-Icon (oben rechts im Admin): Benachrichtigt über verfügbare Updates
- Update durchführen: **Aktualisieren** klicken → Kompatibilitätscheck erfolgt automatisch

---

## Shopware Account Tab

Im Bereich **Meine Erweiterungen** gibt es einen **Shopware Account Tab**:
- Shopware Account mit dem Shop verknüpfen
- Lizenzinformationen prüfen
- Fehlerbehebung bei Lizenzproblemen

---

## Lizenzen verwalten

| Lizenztyp | Beschreibung |
|---|---|
| Kostenlose Lizenz | Keine Kosten; Installation nach Account-Verknüpfung |
| Monatliche Miete | Monatliche Abbuchung; Kündigung jederzeit möglich |
| Kauf (Einmalig) | Einmalzahlung; alle zukünftigen Updates inklusive |
| Testlizenz | Zeitlich begrenzt (meist 14–30 Tage) |

Lizenzen verwalten: https://account.shopware.com > Lizenzen

---

## Pläne und Erweiterungen

Einige Erweiterungen sind **Teil eines Plans** (Rise, Evolve, Beyond) und werden über
die **Shopware Commercial Extension** freigeschaltet:

- **Shopware Rise**: Custom Products, Social Shopping, Immersive Elements, AI Copilot
- **Shopware Evolve**: + Advanced Search, CMS-Erweiterungen, Dynamic Access, B2B, Publisher
- **Shopware Beyond**: + Digital Sales Rooms, Kundenspezifische Preise, Multi-Inventory

→ Details: `shopware-commercial.md`

---

## Häufige Probleme

| Problem | Lösung |
|---|---|
| "Keine Verbindung zum Store" | Shopware Account verknüpfen; Firewall prüfen |
| Erweiterung wird nach Update inaktiv | Kompatibilität prüfen; ggf. neuere Version abwarten |
| Lizenz nicht gefunden | Domain im Shopware Account korrekt hinterlegt? |
| Cache-Fehler nach Aktivierung | `php bin/console cache:clear` ausführen |
