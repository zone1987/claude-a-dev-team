# Shopware 6 – Währungen, Sprachen & Länder (vollständige Referenz)

Quellen:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/waehrungen
- https://docs.shopware.com/de/shopware-6-de/einstellungen/sprachen
- https://docs.shopware.com/de/shopware-6-de/einstellungen/laender

---

## Währungen

**Pfad:** Einstellungen > Shop > Währungen

### Übersicht
- Alle konfigurierten Währungen anzeigen
- Kontextmenü: Bearbeiten oder Entfernen
- Faktor basiert auf der obersten Systemwährung (sollte unverändert bleiben)

### Neue Währung erstellen

#### 1. Einstellungen
| Feld | Beschreibung |
|---|---|
| Name | Bezeichnung (z.B. „Euro") |
| ISO-Code | Gültiger ISO-Währungscode |
| Kurzname | Dreistellige Abkürzung (z.B. „EUR") |
| Symbol | Währungssymbol (z.B. „€") |
| Faktor | Umrechnungsfaktor zur Systemwährung |

#### 2. Preisrundungen
| Feld | Beschreibung |
|---|---|
| Nachkommastellen | Dezimalstellen bei Warenkorb-Berechnungen |
| Rundungsintervall | Rundungslogik festlegen |
| Nettokunden | Rundung auf Nettokunden anwenden |
| Summen | Separate Einstellungen für Gesamtsummen |

#### 3. Länder
Länderspezifische Preisrundungseinstellungen können abweichend konfiguriert werden.

### Bearbeiten & Entfernen
- Bestehende Währungen editierbar
- Sprachvarianten hinzufügbar
- Entfernen nur möglich, wenn Währung keinem Objekt zugewiesen

### Darstellung
Die Formatierung des Währungssymbols hängt von der gewählten Sprache ab:
- Deutsch: „499,99 $"
- Englisch: „US$499.99"

---

## Sprachen

**Pfad:** Einstellungen > Allgemein > Sprachen  
**Verfügbar ab:** 6.7.3.0

> **Kritisch:** Die System-Standardsprache wird bei der Installation gewählt und kann **danach nicht mehr geändert** werden.

### Übersicht
Alle konfigurierten Sprachen mit Name, Lokalisierung, ISO-Code, Aktivstatus.

### Filter-Optionen
| Filter | Beschreibung |
|---|---|
| Nur Root-Sprachen | Hauptsprachen ohne Vererbung |
| Nur abgeleitete Sprachen | Sprachen, die von einer Elternsprache erben |

> Abgeleitete Sprachen erben Kernkomponenten vom Elternteil, erlauben aber spezifische Anpassungen.

### Felder (Erstellen / Bearbeiten)
| Feld | Beschreibung |
|---|---|
| Name | Sprachbezeichnung |
| Aktiv | Im Shop aktivieren/deaktivieren |
| Lokalisierung | Land-/Regionszuweisung |
| ISO-Code | Offizieller Code (z.B. `de-DE`, `en-GB`) |
| Erben von | Elternsprache (max. eine möglich) |

### Sprache anlegen
1. Auf „Sprache anlegen" klicken
2. Felder ausfüllen
3. Speichern → Sprache in Verkaufskanälen verfügbar

---

## Länder

**Pfad:** Einstellungen > Regional > Länder  
**Verfügbar ab:** 6.7.0.0

### Übersicht
Tabelle mit: Ländername, Positionierung, ISO-2-Code, ISO-3-Code, Aktivstatus

### Allgemein-Bereich (beim Anlegen)
| Feld | Beschreibung |
|---|---|
| Name | Länderbezeichnung (in Systemstandard-Sprache) |
| Position | Sortierreihenfolge in der Storefront |
| ISO2 | Zweistelliger ISO-Code (z.B. DE) |
| ISO3 | Dreistelliger ISO-Code (z.B. DEU) |

### Optionen-Bereich (8 Schalter)
| Option | Beschreibung |
|---|---|
| Aktiv | Verfügbarkeit im Shop |
| Versand | Versandoptionen aktivieren/deaktivieren |
| Steuerfrei (B2C) | Steuerbefreiung für Einzelkunden |
| Steuerfrei ab | Wertgrenze für B2C-Steuerbefreiung |
| Währungsabhängige Werte | Mehrwährungsunterstützung |
| Steuerfrei (B2B) | Unternehmenssteuerbefreiung (erfordert gültige USt-ID) |
| USt-ID-Format überprüfen | EU-Validierung der Umsatzsteuer-ID |
| USt-ID Pflichtfeld | Obligatorische USt-ID-Eingabe |
| EU-Mitgliedstaat | Automatisch für EU-Länder; fügt „innergemeinschaftliche Lieferung" hinzu |

### Länder/Regionen (Reiter)
- Bundesländer/Regionen verwalten
- Neue Regionen hinzufügen: Name, ISO-Code, Position
- Inline-Bearbeitung per Doppelklick

### Adress-Verwaltung (Validierung)
| Option | Beschreibung |
|---|---|
| Land/Region Pflichtfeld | Pflichtangabe im Adressformular |
| Postleitzahl Pflichtfeld | Pflichtangabe |
| Postleitzahl validieren | Format-Validierung aktivieren |
| Erweiterte Validierungsregeln | RegEx-Format (z.B. `^\d{5}$` für 5 Ziffern) |

**Beispiele:**
- `^\d{5}$` → exakt 5 Ziffern (Deutschland)
- `^(\d{4})\s*([A-Z]{2})$` → Format „1234 AB" (Niederlande)

### Adressformat
- Länderspezifische Adressformatierung konfigurierbar (z.B. USA: Hausnummer vor Straße)
- Live-Vorschau zur Validierung verfügbar
