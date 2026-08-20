# Internationalisierung

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/internationalisierung

## Überblick

Shopware 6 unterstützt den internationalen Verkauf über Mehrsprachigkeit, Multi-Währung
und länderspezifische Zahlungs- und Versandoptionen. Dieser Artikel beschreibt die
strukturierte Vorgehensweise für die internationale Einrichtung.

---

## Vorüberlegungen vor der Einrichtung

Vor der Implementierung sollten folgende Fragen geklärt sein:

| Frage | Relevanz |
|---|---|
| Welche Zahlarten werden im Ausland bevorzugt? | Zahlungsmethoden pro Land konfigurieren |
| Welche Steuerregeln gelten? | Länderspezifische Steuersätze einrichten |
| Werden mehrere Währungen benötigt? | Währungen anlegen und Wechselkurse konfigurieren |
| Sind Übersetzungen vorhanden? | Produkttexte, E-Mail-Templates, Kategorienamen übersetzen |
| Welche Versandoptionen gibt es international? | Versandarten + Lieferländer definieren |

---

## Implementierungsschritte (empfohlene Reihenfolge)

### Schritt 1: Sprache einrichten
- Pfad: **Einstellungen > Sprachen**
- Neue Sprache hinzufügen (über Sprachpaket-Erweiterung)
- Standard: Deutsch und Englisch bereits verfügbar
- Weitere Sprachen: Sprachpaket installieren → `../../../sw-merchant-extensions/references/deep/sprachpaket.md`

### Schritt 2: Länder aktivieren
- Pfad: **Einstellungen > Länder & Gebiete**
- Gewünschte Länder für Kundenregistrierung aktivieren (Häkchen)
- Ohne Aktivierung können Kunden aus diesem Land sich nicht registrieren

### Schritt 3: Währungen konfigurieren
- Pfad: **Einstellungen > Währungen**
- Neue Währung anlegen (z. B. GBP, USD, CHF)
- Wechselkurse manuell eintragen oder automatisch abrufen (über Erweiterung)
- Rundungsregeln pro Währung konfigurierbar

### Schritt 4: Steuersätze einrichten
- Pfad: **Einstellungen > Steuern**
- Länderspezifische Steuersätze anlegen
- Beispiel: DE 19%, AT 20%, FR 20%, UK 0% (nach Brexit)
- Steuerregeln können an Kundengruppen und Länder geknüpft werden

### Schritt 5: Zahlungsmethoden konfigurieren
- Pfad: **Einstellungen > Zahlungen**
- Pro Zahlungsmethode: Verfügbarkeit nach Land einschränken (Rule Builder)
- Beispiel: SEPA nur für SEPA-Länder, lokale Zahlarten für spezifische Märkte

### Schritt 6: Versandmethoden definieren
- Pfad: **Einstellungen > Versand**
- Versandregeln (Rule Builder): Welche Versandarten in welche Länder?
- Internationale Versandkosten separat konfigurieren

### Schritt 7: Verkaufskanäle einrichten
- Option A: **Ein Verkaufskanal mit Mehrsprachigkeit** (Sprachauswahl im Storefront)
- Option B: **Separate Verkaufskanäle pro Land** (eigene Domain, eigene Konfiguration)
- Für Option B: Eigene Domains pro Land empfohlen (z. B. `shop.de`, `shop.co.uk`)

---

## Übersetzungen verwalten

Shopware verwendet ein **Vererbungsmodell** für Übersetzungen:
- Felder ohne Übersetzung **erben** von der Standardsprache
- Übersetzungen müssen in der jeweiligen Sprachansicht gepflegt werden

Übersetzbare Bereiche:

| Bereich | Pfad |
|---|---|
| Produktbeschreibungen | Katalog > Produkte > [Produkt] > Sprache wählen |
| E-Mail-Templates | Einstellungen > E-Mail-Templates |
| Kategorienamen | Katalog > Kategorien > [Kategorie] > Sprache wählen |
| Erlebniswelten (CMS) | Content > Erlebniswelten |
| Eigenschaften & Optionen | Katalog > Eigenschaften |

---

## Testphase vor Go-Live

- Alle Übersetzungen auf Vollständigkeit prüfen
- Zahlungs- und Versandregeln für jede Zielregion testen (Testbestellung)
- Steuerberechnung im Checkout verifizieren
- Währungsdarstellung in der Storefront prüfen

---

## Shopware Cloud vs. Self-Hosted

Bei **Shopware Cloud** sind einige Einstellungen (z. B. Domain-Management) über das
Cloud-Dashboard zu konfigurieren; das Admin-Interface bleibt gleich.
