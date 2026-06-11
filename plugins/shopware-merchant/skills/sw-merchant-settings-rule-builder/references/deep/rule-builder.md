# Shopware 6 – Rule Builder (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/regeln

---

## Überblick

**Pfad:** Einstellungen > Automatisierung > Rule Builder

Ermöglicht die Definition von Regeln zur Individualisierung verschiedener Shop-Features ohne Programmierung.

---

## Allgemeine Informationen einer Regel

| Feld | Beschreibung |
|---|---|
| Name | Eindeutige Regelbezeichnung |
| Beschreibung | Optionale Funktionserläuterung |
| Priorität | Anwendungsreihenfolge (höherer Wert = früher ausgewertet) |
| Typ | Optional zur Einschränkung von Zuweisungsmöglichkeiten |
| Tags | Organisationsmerkmale für Suche und Filterung |

---

## Bedingungssystem

### Kernkomponenten
| Komponente | Beschreibung |
|---|---|
| Bedingung | Parameter zum Abfragen (z.B. Lieferland) |
| Operator | Vergleichsmethode (z.B. Ist, Ist nicht) |
| Eingabewert | Vergleichskriterium (z.B. Deutschland) |
| UND-Verknüpfung | Alle Bedingungen müssen erfüllt sein |
| ODER-Verknüpfung | Mindestens eine Bedingung muss erfüllt sein |
| Unterbedingungen | Werden automatisch bei Verknüpfungswechsel angelegt |

### Regeln anlegen
1. Einstellungen > Automatisierung > Rule Builder
2. „Regel erstellen"
3. Allgemeine Informationen ausfüllen
4. Mindestens eine Bedingung mit Operator wählen
5. Eingabewert angeben
6. Speichern

---

## Operatoren

| Operator | Funktion |
|---|---|
| Mind. eine | Mindestens ein Wert trifft zu |
| Alle | Alle Werte treffen zu |
| Gleich | Exakte Übereinstimmung |
| Ungleich | Keine Übereinstimmung |
| Ist eine von | Übereinstimmung mit einer von mehreren Optionen |
| Ist keine von | Keine Übereinstimmung mit einer der Optionen |
| Größer | Wert größer als Eingabe |
| Größer gleich | Wert ≥ Eingabe |
| Kleiner | Wert kleiner als Eingabe |
| Kleiner gleich | Wert ≤ Eingabe |

---

## Bedingungskategorien

### Allgemein
- Ausgelöst durch Admin-API
- Datumsbereich, Immer zutreffend
- Sprache, Steuerdarstellung, Verkaufskanal, Währung
- Wochentag, Zeitraum

### Bestellungen
- Affiliate-Code, Bestellstatus
- Bestellung mit Dokument / gesendetem Dokument
- Bestellung mit Tag / Zusatzfeld
- Kampagnen-Code, Lieferstatus, Zahlungsstatus
- Vom Administrator erstellt

### Kunde
- Affiliate-Code, Angemeldeter Kunde
- Angefragte Kundengruppe
- Anzahl abgeschlossener Bestellungen, Gesamtwert
- Firmenkunde, Gastbesteller
- Kundenanrede, Kundenalter, Geburtstag
- Kundengruppe, Kundennummer
- Lieferadresse: Bundesland, Land, PLZ, Stadt, Straße
- Rechnungsadresse: Bundesland, Land, PLZ, Stadt, Straße
- Zeit seit erster/letzter Anmeldung
- Zeit seit letzter Bestellung
- Ist aktiv, Newsletter-Empfänger
- Mit abweichender Lieferadresse
- Standard-Zahlungsart, Tag, Zusatzfeld

### Positionen im Warenkorb
- Anzahl unterschiedlicher Positionen
- Position als „neu" markiert / im Abverkauf
- In dynamischer Produktgruppe / Kategorie
- Hervorgehoben / versandkostenfrei
- Durchschnittsbewertung
- Breite, Einkaufspreis, Erscheinungsdatum, Gewicht, Höhe
- Hersteller, Lagerbestand, Länge, Steuersatz
- Prozentuales Preis/Streichpreis-Verhältnis
- Streichpreis, Tag, Varianten-/Eigenschaftsausprägung
- Verfügbarer Bestand, Volumen, Zusatzfeld
- Positionsanzahl, Stückpreis, Zwischensumme
- Summe aller Einkaufspreise

### Warenkorb
- Gesamtanzahl aller Produkte (mit optionalem Filter)
- Gesamtanzahl unterschiedlicher Produkte (mit optionalem Filter)
- Gesamtgewicht, Gesamtsumme, Gesamtvolumen
- Summe, Versandkosten
- Verwendete Versandart, Zahlungsart

### Marketing & Rabattaktionen
- Anzahl der Rabatte
- Rabattaktion, Rabattaktionen mit Aktionscodetyp
- Zwischensumme aller Rabatte

---

## Bedingungen mit optionalem Filter

| Bedingung | Filtermöglichkeit |
|---|---|
| Zwischensumme aller Positionen | Nach Kategorie |
| Gesamtanzahl aller Produkte | Nach Tags |
| Gesamtanzahl unterschiedlicher Produkte | Nach Streichpreis-Status |

---

## Zuweisungen (Reiter)

| Bereich | Verwendung |
|---|---|
| Zahlungsmethoden | Verfügbarkeitsregel |
| Versandmethoden | Verfügbarkeitsregel |
| Versandkosten | Berechnungsregel |
| Promotionen | Verfügbarkeit |
| Rabatte | Berechnungsregel |
| Erweiterte Preisgestaltung | Preisregeln |
| Flow-Definition | Flow Builder |
| Sichtbarkeit | Dynamic Access |

---

## Vorschaumodus (ab Plan Rise)

- Validiert Bedingungen in Echtzeit anhand ausgewählter Bestellungen
- Simulierbare Zeitpunkte
- Kein Einfluss auf Echtdaten

---

## Regeln teilen (ab v6.7.1.0 + Rise Plan)

### Download
Kontextmenü → **Download** → JSON-Export mit allen Bedingungen und Operatoren

### Upload
Einstellungen > Automatisierung > Rule Builder → **Regel hochladen** → Datei wählen → Upload

Bei fehlenden Referenzen (Kunden, Kundengruppen, Verkaufskanäle) erfolgt automatische Neuzuweisung.

---

## Regeln löschen

Via Kontextmenü → **Löschen**

> **Einschränkung:** Zugewiesene Regeln können nicht gelöscht werden.

---

## Lernressourcen

- Interaktiver Lernpfad: https://hub.shopware.com/learn/unit/user-rule-builder
