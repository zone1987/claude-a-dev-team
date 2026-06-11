# Shopware AI Copilot – Vollständige Dokumentation

## Überblick

Der **Shopware AI Copilot** ist ein KI-Assistent, der nativ in Shopware 6 integriert ist. Er nutzt künstliche Intelligenz, um E-Commerce-Abläufe zu vereinfachen.

**Verfügbarkeit:** Rise-Plan und höher (Commercial Extension erforderlich)

---

## Funktionen im Detail

### 1. Content für Erlebniswelten

Der AI Copilot hilft dabei, verschiedene Arten von Textinhalten für Shopping Experiences zu erstellen. Texte können direkt generiert und in mehrere Sprachen übersetzt werden.

**Anwendung:** Im Erlebniswelten-Editor → AI Copilot-Funktion aktivieren → Beschreibung eingeben → Text generieren/übersetzen

### 2. Bild-Keywords

Das System analysiert hochgeladene Produktbilder und vergibt automatisch relevante Schlagwörter. Diese werden für die Suche und Klassifizierung genutzt.

**Pfad:** Produkt bearbeiten → Medienbereich → AI-Keyword-Vorschlag

### 3. Produkteigenschaften

Basierend auf vorhandenen Produktbeschreibungen schlägt die KI passende Produktattribute und -eigenschaften vor. Der Händler übernimmt oder passt diese an.

### 4. Personalisierte Checkout-Nachricht (Post-Purchase Messaging)

Nach dem Checkout erhalten Kunden eine personalisierte, KI-generierte Nachricht. Die KI nutzt dabei den Warenkorbinhalt, um relevante und loyalitätsstärkende Nachrichten zu formulieren.

**Konfiguration:** Flow Builder → Trigger: Bestellung abgeschlossen → Aktion: AI Checkout-Nachricht

### 5. Bewertungszusammenfassung (Review Summaries)

Statt einzelner Bewertungen zu lesen, erhalten Kunden auf der Produktdetailseite eine prägnante KI-Zusammenfassung aller Produktbewertungen.

**Anzeige:** Wird automatisch auf Produktdetailseiten angezeigt (ab konfigurierter Mindestanzahl von Bewertungen)

### 6. Kundenklassifizierung

Das System erstellt automatisch Kundenlabels basierend auf der Kaufhistorie. Diese Labels ermöglichen gezieltes Marketing und Segmentierung.

**Pfad:** Kunden > Kunden-Übersicht → KI-Labels werden automatisch zugeordnet

### 7. Export-Assistent

Händler können Shop-Daten in CSV-Format exportieren, indem sie natürliche Sprachbefehle eingeben. Kein manuelles Konfigurieren der Export-Parameter nötig.

**Beispiel:** „Exportiere alle Produkte aus Kategorie Schuhe mit Preis unter 100 Euro"

### 8. Produktbeschreibungen

Händler geben Kerninformationen zu einem Produkt ein, die KI generiert daraus vollständige, verkaufsoptimierte Produktbeschreibungen. Diese können direkt verwendet oder weiter angepasst werden.

**Pfad:** Produkt bearbeiten → Beschreibungsfeld → AI-Assistent öffnen → Stichworte eingeben → Generieren

### 9. Intelligente Suche (Advanced Search Integration)

Zwei Suchmodi, die mit Advanced Search 2.0 kombiniert werden:

**Kontextbasierte Suche:**
- Kunden beschreiben ihr Produktbedürfnis in natürlicher Sprache
- System interpretiert die Absicht unter Berücksichtigung des Shop-Kontexts
- Maximale Keyword-Länge: 100 Zeichen
- Im Storefront: Icon neben dem Suchfeld mit Beispielvorschlägen

**Bildbasierte Suche:**
- Kunden laden ein Foto hoch
- System findet visuell ähnliche Produkte

**Voraussetzung:** Advanced Search 2.0 (Evolve+) für volle Funktionalität; grundlegende AI-Suche bereits in Rise

### 10. Bildgenerierung

Händler erstellen Produktbilder durch natürlichsprachliche Beschreibungen. Kein Bildbearbeitungsprogramm erforderlich.

**Pfad:** Medienbereich → AI Bild generieren → Beschreibung eingeben → Bild erstellen

---

## Übersetzungsfunktionen

Der AI Copilot kann generierte Inhalte automatisch in alle konfigurierten Shop-Sprachen übersetzen:
- Bewertungsübersetzungen für internationale Kunden
- Produktbeschreibungen in mehrere Sprachen
- Erlebniswelt-Texte übersetzen

---

## Technische Voraussetzungen

- Shopware Commercial Extension aktiv
- Rise-Plan oder höher gebucht
- Für bildbasierte Suche: Advanced Search 2.0 (Evolve+)
- Internetverbindung für KI-API-Aufrufe

---

## Integration mit anderen Features

| Feature | AI Copilot Funktion |
|---|---|
| Erlebniswelten | Content-Erstellung und Übersetzung |
| Flow Builder | Personalisierte Checkout-Nachrichten |
| Advanced Search | Kontextbasierte und bildbasierte Suche |
| Produktverwaltung | Beschreibungen und Eigenschaften |
| Medienbereich | Bildkeywords und Bildgenerierung |
| Kundenmanagement | Kundenklassifizierung und Labels |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/features/shopware-rise/ai-copilot (Stand: 2026-06)*
