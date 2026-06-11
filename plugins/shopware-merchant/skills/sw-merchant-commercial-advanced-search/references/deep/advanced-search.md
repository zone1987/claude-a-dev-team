# Shopware Advanced Search 2.0 – Vollständige Dokumentation

## Überblick

**Advanced Search 2.0** ist die professionelle Suchlösung von Shopware 6, basierend auf OpenSearch-Infrastruktur.

**Verfügbarkeit:** Evolve-Plan und höher
**Mindestversion:** Shopware 6.5.6.0
**Voraussetzungen:**
- OpenSearch-Infrastruktur
- Shopware Commercial Extension
- Evolve-Plan oder höher

**Pfad im Admin:** Einstellungen → Allgemein → Suche

---

## Such-Verhalten konfigurieren

### Suchmodus

| Modus | Verhalten |
|---|---|
| AND-Suche | Ergebnisse müssen ALLE Suchbegriffe enthalten |
| OR-Suche | Ergebnisse müssen mindestens EINEN Begriff enthalten |

### Mindestsuchwortlänge

Pro Verkaufskanal konfigurierbar – Suchen mit weniger Zeichen werden ignoriert.

### Sonderzeichen in Produktnummern

Sonderzeichen können über die YAML-Konfiguration beibehalten werden:

```yaml
# config/packages/shopware.yaml
shopware:
  search:
    preserved_chars: ['-', '_', '.']
```

---

## Durchsuchbare Inhalte

Festlegbar, welche Felder in Suchergebnissen erscheinen:

### Produkte
- Name, Beschreibung, Produktnummer
- EAN, Hersteller-Nummer
- Benutzerdefinierte Felder

### Kategorien
- Name, Beschreibung
- Kategorie-Tags

### Hersteller
- Name

### Ranking / Gewichtung

Jedes Suchfeld erhält eine Punktzahl (Score). Höhere Werte = höhere Sichtbarkeit in Suchergebnissen.

**Beispiel:**
- Produktname: 1000 Punkte
- Produktnummer: 500 Punkte
- Beschreibung: 100 Punkte

---

## Suchergebnis-Anzeige

Separate Konfiguration für:

| Bereich | Einstellung |
|---|---|
| Schnellsuche (Dropdown) | Max. Ergebnisanzahl |
| Volltextsuche (Ergebnisseite) | Max. Ergebnisanzahl |

---

## Boostings

Boostings erhöhen die Sichtbarkeit bestimmter Produkte in Suchergebnissen.

**Erstellung:**
1. Einstellungen → Suche → Boostings → Neues Boosting
2. Name und Priorität festlegen
3. Produktauswahl über dynamische Produktgruppe oder Custom-Regel
4. Gültigkeitszeitraum (optional für saisonale Relevanz)
5. Zuweisung zu Verkaufskanälen

**Anwendungsfälle:**
- Saison-Produkte temporär hervorheben
- Neue Kollektionen priorisieren
- Margenstarke Produkte bevorzugen

---

## Actions (Suchterm-Umleitungen)

Actions leiten Kunden von bestimmten Suchbegriffen zu definierten Zielen um.

**Konfiguration:**
1. Einstellungen → Suche → Actions → Neue Action
2. Suchbegriff/e definieren
3. Ziel festlegen: Produkt, Kategorie oder URL

**Anwendungsfälle:**
- Markennamen auf Kategorie leiten
- Tippfehler abfangen und korrekt weiterleiten
- Saisonale Aktionsseiten bei bestimmten Suchen anzeigen

---

## Synonyme

Synonyme sorgen dafür, dass verwandte Begriffe dieselben Ergebnisse liefern.

### Äquivalenz-Synonyme
Alle Begriffe sind vollständig austauschbar:
- „Sofa" ↔ „Couch" ↔ „Sessel"

### Explizite Zuordnung
Spezifische Begriffe werden auf breitere Kategorien gemappt:
- „iPhone" → „Smartphone", „Handy", „Mobiltelefon"
- Suche nach „iPhone" zeigt alle Smartphones, aber nicht umgekehrt

---

## AI Copilot Integration (Rise+)

Mit dem AI Copilot (Rise-Plan) wird die Suche um KI-Funktionen erweitert:

### Kontextbasierte Suche
- Kunden beschreiben ihr Produkt in natürlicher Sprache
- KI interpretiert Kundenabsicht unter Berücksichtigung des Shop-Kontexts
- Max. 100 Zeichen Eingabe
- Im Storefront: Icon neben dem Suchfeld mit Beispielvorschlägen

### Bildbasierte Suche
- Kunden laden ein Bild hoch
- System findet visuell ähnliche Produkte im Sortiment

---

## Storefront-Integration

Die Advanced Search aktiviert sich automatisch für alle konfigurierten Verkaufskanäle. Keine weiteren Storefront-Anpassungen nötig.

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/advancedsearch-2-0 (Stand: 2026-06)*
