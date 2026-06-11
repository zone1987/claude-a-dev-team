# Shopware Sales Agent – Vollständige Dokumentation

## Überblick

Der Sales Agent ist eine separate Frontend-App (keine Admin-Erweiterung), die Außendienstmitarbeitern ermöglicht, B2B-Kunden zu verwalten und Angebote zu erstellen.

**Verfügbarkeit:** Evolve-Plan und höher
**Mindestversion:** Shopware 6.5.0.0
**Typ:** Separate Frontend-App (kein Admin-Plugin)
**Voraussetzung:** Shopware Commercial Extension

---

## Admin: Benutzer und Berechtigungen

**Pfad im Admin:** Einstellungen → System → Sales Agent – Benutzer & Berechtigungen

### Sales Representative anlegen

| Feld | Beschreibung |
|---|---|
| Vorname / Nachname | Vollständiger Name |
| E-Mail | Für Login und Kommunikation |
| Sprache | Interface-Sprache der App |
| Admin-Rechte | Volle Verwaltungsrechte in der Sales Agent App |
| Aktiv/Inaktiv | Zugang aktivieren oder sperren |
| Löschen | Konto dauerhaft entfernen |

Nach der Erstellung erhält der Mitarbeiter automatisch eine Einladungs-E-Mail mit Setup-Anweisungen.

**Screenshot Übersicht:** `../../assets/sales-agent-overview.png`
**Screenshot Neuer Benutzer:** `../../assets/sales-agent-neuer-benutzer.png`

### Kunden zuweisen

- **Einzelzuweisung**: Kunden-Übersicht → Einzelkunde → Sales Agent zuweisen
- **Massenzuweisung**: Mehrere Kunden markieren → Sales Agent zuweisen

**Wichtig:** Nur Administratoren können Kunden einem Vertriebsmitarbeiter zuweisen oder Zuordnungen ändern.

---

## Sales Agent App: Benutzeroberfläche

### Persönliche Einstellungen
Nach dem ersten Login können Mitarbeiter konfigurieren:
- Sprache (Interface)
- Zeitzone
- Name (Anzeigename)
- Telefonnummer
- Passwort ändern

### Kundenverwaltung
- Liste aller zugewiesenen Kunden
- Kundendaten einsehen
- Bestellhistorie des Kunden einsehen
- Direkt in Kundenkonto wechseln

### Bestellungen erstellen
Sales Agents können im Namen von Kunden Bestellungen aufgeben:
1. Kunden auswählen
2. In Kundenkonto wechseln
3. Produkte in den Warenkorb legen
4. Checkout im Namen des Kunden abschließen

---

## Angebotsverwaltung (Quote Management)

**Screenshot Angebotsliste:** *(Bild nicht verfügbar – S3-Zugriff verweigert)*

### Angebot erstellen

#### Tab: Allgemein
| Feld | Beschreibung |
|---|---|
| Kunde | Kundenauswahl aus zugewiesenen Kunden |
| Verkaufskanal | Verkaufskanal für das Angebot |
| Gültig bis | Ablaufdatum des Angebots |
| Persönliche Nachricht | Individueller Text für den Kunden |

#### Tab: Positionen
| Funktion | Beschreibung |
|---|---|
| Produkte hinzufügen | Suche nach Produktname oder -nummer |
| Standardpreis | Regulärer Listenpreis |
| Sonderpreis | Individuell verhandelter Preis |
| Menge | Bestellmenge je Position |

#### Tab: Rabatte
| Option | Beschreibung |
|---|---|
| Absoluter Rabatt | Fixer Betrag (z.B. -50 €) |
| Prozentualer Rabatt | Relativer Abzug (z.B. -10%) |

#### Tab: Dokumente
| Option | Beschreibung |
|---|---|
| Auto-generiertes PDF | System erstellt Angebots-PDF |
| Benutzerdefiniertes Dokument | Eigenes Dokument hochladen und anhängen |

### Angebot versenden
1. Angebot fertigstellen
2. Per E-Mail an Kunden senden
3. Kunde kann Angebot annehmen oder ablehnen
4. Bei Annahme: Direkte Umwandlung in Bestellung

---

## Integration mit B2B Components

Sales Agent ergänzt die B2B Components:
- Angebote die über den Sales Agent erstellt werden, erscheinen auch in der Admin-Ansicht unter Bestellungen → Angebote
- Genehmigungsregeln des Kunden gelten auch für Sales Agent-Bestellungen
- Kundengruppenpreise werden im Sales Agent angewendet

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/erweiterungen/sales-agent (Stand: 2026-06)*
