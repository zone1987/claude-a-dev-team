# Shopware Rule Builder (Commercial Features) – Vollständige Dokumentation

## Überblick

Der Rule Builder ermöglicht Händlern, Bedingungsregeln zu erstellen, die verschiedene Shop-Einstellungen und Features personalisieren.

**Pfad im Admin:** Einstellungen → Automatisierung → Rule Builder

**Verfügbarkeit nach Plan:**

| Feature | Plan |
|---|---|
| Rule Builder (Basis) | Community Edition |
| Regelvorschau (Preview) | Rise+ |
| Regeln teilen (Export/Import) | Rise+ (ab 6.7.1.0) |

---

## Grundaufbau einer Regel

### Allgemeine Informationen
| Feld | Beschreibung |
|---|---|
| Name | Interne Bezeichnung |
| Beschreibung | Erläuterung des Regelzwecks |
| Priorität | Höhere Werte werden zuerst ausgeführt |
| Typ | Klassifikation der Regel |
| Tags | Organisationshilfe |

### Bedingungsstruktur

Jede Bedingung besteht aus:
1. **Bedingungsparameter**: Was wird verglichen? (z.B. Warenkorb-Gesamt, Kundengruppe)
2. **Operator**: Vergleichstyp (=, ≠, >, <, ≥, ≤, „einer von", „alle")
3. **Eingabewert**: Vergleichswert

### Logikverknüpfung

| Operator | Verhalten |
|---|---|
| AND | ALLE Bedingungen müssen erfüllt sein |
| OR | MINDESTENS EINE Bedingung muss erfüllt sein |

**Verschachtelung:** AND- und OR-Gruppen können beliebig verschachtelt werden.

---

## Verfügbare Bedingungen (80+)

### Allgemein
- Sprache
- Währung
- Datum/Uhrzeit (Zeiträume, Wochentage)
- Verkaufskanal

### Bestellungen
- Bestellstatus
- Bestelldokumente (Rechnung vorhanden etc.)
- Bestelltags

### Kunden
- Kundengruppe
- Rechnungsadresse (Land, PLZ, Bundesland)
- Lieferadresse (Land, PLZ, Bundesland)
- Kundenalter
- Kaufhistorie (Gesamtumsatz, Anzahl Bestellungen)
- Ist eingeloggt

### Warenkorb / Positionen
- Warenkorb-Gesamtpreis
- Artikel in bestimmter Kategorie
- Artikelattribute (Eigenschaft, Merkmal)
- Artikelabmessungen (Gewicht, Höhe, Breite)
- Artikel-Tags

### Rabatte & Marketing
- Aktionscode vorhanden
- Affiliatecode vorhanden

### Zahlungs- und Versandmethoden
- Ausgewählte Zahlungsmethode
- Ausgewählte Versandmethode

---

## Operatoren

| Operator | Anwendung |
|---|---|
| Ist gleich (=) | Exakter Wert |
| Ist ungleich (≠) | Alles außer diesem Wert |
| Ist größer als (>) | Numerische Vergleiche |
| Ist kleiner als (<) | Numerische Vergleiche |
| Ist größer oder gleich (≥) | Numerische Vergleiche |
| Ist kleiner oder gleich (≤) | Numerische Vergleiche |
| Einer von | Mehrere erlaubte Werte |
| Alle | Mehrere Pflicht-Werte |

---

## Commercial Feature: Regelvorschau (Rise+)

Die Vorschaufunktion testet Regeln in Echtzeit gegen echte Bestellungen.

### Verwendung
1. Regel erstellen oder öffnen
2. Button „Vorschau" klicken
3. Bestehende Bestellung auswählen
4. System zeigt: TRUE oder FALSE je Bedingung

### Nutzen
- Fehlerdiagnose vor dem Live-Schalten
- Verständnis komplexer Regelketten
- Test von saisonalen oder zeitabhängigen Regeln

---

## Commercial Feature: Regeln teilen (Rise+, ab 6.7.1.0)

Regeln können zwischen Shopware-Instanzen exportiert und importiert werden.

### Export
1. Regel öffnen
2. „Regel exportieren" → JSON-Datei wird heruntergeladen

### Import
1. Neuer Regel-Import
2. JSON-Datei hochladen
3. Bei fehlenden Referenzen (z.B. Kundengruppen): Neuzuordnung im Dialog
4. Regel ist aktiv und bereit zur Verwendung

### Anwendungsfälle
- Regelsets zwischen Entwicklungs- und Produktionssystem synchronisieren
- Regelvorlagen für Agenturen und Shops
- Backup und Versionierung von Regelkonfigurationen

---

## Regelverwendung (Assignment Tab)

Der Tab **„Verwendung"** in jeder Regel zeigt, wo sie eingesetzt wird:
- Zahlungsmethoden
- Versandmethoden
- Promotionen / Aktionen
- Flow Builder (Bedingungen)
- Advanced Search (Boostings)
- Abonnement-Pläne

Dies ermöglicht Impact-Analyse vor Regeländerungen.

---

## Praxisbeispiele

### Beispiel 1: Kostenloser Versand ab Bestellwert
- **Bedingung:** Warenkorb-Gesamt ≥ 50 €
- **Verwendung:** Versandmethode „Kostenlos" → Verfügbarkeitsregel

### Beispiel 2: B2B-Kundengruppe Netto-Preise
- **Bedingung:** Kundengruppe = „Geschäftskunden"
- **Verwendung:** Preisanzeige netto

### Beispiel 3: Weihnachtsrabatt (zeitbasiert)
- **Bedingung:** Datum zwischen 01.12. und 26.12.
- **Verwendung:** Aktionscode automatisch anwenden

### Beispiel 4: Großbestellungs-Rabatt (mit Staffel)
- **Bedingung:** Warenkorb-Gesamt ≥ 500 €
- **Verwendung:** Promotion 5% Rabatt

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/regeln (Stand: 2026-06)*
