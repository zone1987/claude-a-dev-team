# Shopware 6 – CMS-Erweiterungen: Vollständige Dokumentation

**Quelle:** https://docs.shopware.com/de/shopware-6-de/erweiterungen/cms-erweiterungen  
**Version:** ab 1.0.1; aktuelle Version 2.2.0+

---

## Screenshots

| Datei | Inhalt |
|---|---|
| `../../assets/quickview.png` | Quickview im Listing |
| `../../assets/scroll-navigation-sektion.png` | Scroll-Navigation Sektions-Einstellung |
| `../../assets/scroll-navigation-frontend.png` | Scroll-Navigation im Storefront |
| `../../assets/block-sichtbarkeit.png` | Block-Sichtbarkeit per Rule Builder |
| `../../assets/custom-form-erstellen.png` | Custom Form erstellen |
| `../../assets/custom-form-optionen.png` | Custom Form Optionen |
| `../../assets/custom-form-felder.png` | Custom Form Felder und Gruppen |

---

## Übersicht

Die **CMS-Erweiterungen** sind eine offizielle Shopware-Erweiterung, die als Teil
von **Shopware Evolve** (und höheren Plänen) verfügbar ist.

Sie erweitern die Erlebniswelten um folgende Kernfunktionen:
1. Quickview (Produktvorschau im Listing)
2. Suchergebnisse-Quickview
3. Scroll-Navigation (Anker-Punkte)
4. Block-Sichtbarkeit per Rule Builder
5. Custom Forms (benutzerdefinierte Formulare)

---

## Installation

### Voraussetzungen
- Shopware Evolve Plan oder höher auf der Shop-Domain
- Shopware Account in der Admin hinterlegt

### Schritte
1. Admin > **Erweiterungen > Meine Erweiterungen**
2. Extension „CMS-Erweiterungen" suchen
3. „Installieren" → „Aktivieren"
4. Shop-Konfiguration ggf. anpassen

---

## Feature 1: Quickview

### Funktion
Ermöglicht die Produktvorschau direkt im Listing, ohne die Kategorie-Seite zu verlassen.
Nutzer klicken auf ein Produkt und erhalten sofort einen modalen Vorschau-Dialog.

### Verfügbare Blöcke
Quickview funktioniert mit folgenden Erlebniswelt-Blöcken:
- **Drei Spalten Produkte-Boxen**
- **Produkt-Slider**
- **Cross-Selling**

### Aktivierung
Nach Installation der Extension ist Quickview automatisch für unterstützte Blöcke aktiv.

### Konfiguration
- Extension-Einstellungen öffnen (in Erweiterungen > CMS-Erweiterungen > Konfiguration)
- Quickview de-/aktivieren

---

## Feature 2: Suchergebnisse-Quickview

### Funktion
Erweitert die Quickview-Funktionalität auf die **Suchergebnisseite**.

Nutzer können Produktdetails direkt in der Suche einsehen ohne zur Produktdetailseite
navigieren zu müssen.

### Aktivierung
In der Extension-Konfiguration unter:
- CMS-Erweiterungen > Konfiguration > „Quickview auf Suchergebnisseite aktivieren"

---

## Feature 3: Scroll-Navigation

### Funktion
Erstellt eine **Anker-Punkt-Navigation** innerhalb einer Erlebniswelten-Seite.
Besonders nützlich für lange Landingpages mit mehreren Sektionen.

### Darstellung im Storefront

**Desktop:**
- Navigation erscheint als vertikales Menü auf der **linken Seite**
- Scrollt mit dem Nutzer mit (sticky)
- Aktiver Abschnitt wird hervorgehoben

**Mobil:**
- Navigation erscheint als Buttons unten rechts
- Aufklappbares Menü

### URL-Parameter
Sektionen können direkt über URL-Anker angesprungen werden:
```
https://meinshop.de/landingpage/#sektionsname
```
Beispiel: `/#lorem%20ipsum`

### Einrichtung
1. Erlebniswelt-Layout öffnen
2. Sektion anklicken → Sektions-Einstellungen
3. Sektionsname vergeben (wird als Anker verwendet)
4. Scroll-Navigation ist automatisch aktiv wenn Extension installiert

---

## Feature 4: Block-Sichtbarkeit per Rule Builder

### Funktion
Einzelne CMS-Blöcke können basierend auf **Rule Builder-Regeln** konditionell
ein- oder ausgeblendet werden.

### Anwendungsfälle
- Blöcke nur für eingeloggte Kunden anzeigen
- Blöcke nur für bestimmte Kundengruppen
- Blöcke nur in bestimmten Zeiträumen (z.B. Aktionszeitraum)
- Blöcke nach Bestellhistorie / Umsatz steuern
- Geographische Steuerung (Land/Region)

### Verwendung
1. Erlebniswelt-Layout öffnen
2. Block anklicken → Block-Einstellungen in rechter Sidebar
3. Bereich „Sichtbarkeit" → Regel zuweisen
4. Aus vorhandenen Rules auswählen oder neue erstellen
5. Speichern

### Rule Builder
Rules werden in **Einstellungen > Rule Builder** (oder Marketing > Rule Builder) definiert.
Hier können komplexe Bedingungen mit AND/OR-Verknüpfungen erstellt werden.

---

## Feature 5: Custom Forms (Benutzerdefinierte Formulare)

### Funktion
Ermöglicht die Erstellung von **individuellen Formularen** mit eigenen Feldern,
Feldgruppen und E-Mail-Vorlagen – weit über das Standard-Kontaktformular hinaus.

### Einsatzbereiche
- Bewerbungsformulare
- Produktanfragen mit spezifischen Feldern
- Veranstaltungsanmeldungen
- Rückrufanfragen
- Kundenumfragen

### Verfügbare Feldtypen
- Textfeld (einzeilig)
- Textarea (mehrzeilig)
- E-Mail-Feld
- Telefonnummer
- Zahl
- Datum/Uhrzeit
- Auswahlliste (Dropdown)
- Checkbox
- Radio-Buttons
- Datei-Upload

### Formular erstellen

1. Erweiterungen > CMS-Erweiterungen > Tab „Formulare"
2. „Neues Formular erstellen"
3. **Allgemeine Einstellungen:**
   - Formularname
   - Empfänger-E-Mail(s)
   - E-Mail-Vorlage für Bestätigungs-E-Mail
   - E-Mail-Vorlage für Benachrichtigung
4. **Felder hinzufügen:**
   - Feldtyp wählen
   - Label/Bezeichnung eingeben
   - Pflichtfeld (ja/nein)
   - Validierungsregeln setzen
5. **Feldgruppen** (optional): Felder logisch gruppieren
6. Speichern

### Formular in Erlebniswelt einbinden

1. Erlebniswelt-Layout öffnen
2. Block-Kategorie „Formulare" in der Sidebar öffnen
3. „Custom Form"-Block per Drag & Drop einfügen
4. Block anklicken → Formular aus Liste auswählen
5. Speichern

### E-Mail-Vorlagen für Custom Forms

Separate Vorlagen für:
- **Kundenbestätigung**: E-Mail an Absender nach Formular-Einreichung
- **Shop-Benachrichtigung**: E-Mail an Shop-Betreiber mit Formularinhalt

Vorlagen können unter Einstellungen > E-Mail-Vorlagen angepasst werden.

---

## Changelog (Versionshistorie)

| Version | Änderungen |
|---|---|
| 2.2.0+ | Aktuelle Version |
| 2.0.0 | Custom Forms Feature |
| 1.5.0 | Block-Sichtbarkeit per Rule Builder |
| 1.3.0 | Suchergebnisse-Quickview |
| 1.1.0 | Scroll-Navigation |
| 1.0.1 | Initiale Version (Quickview) |

---

## Verwandte Dokumentation

- Erlebniswelten: `sw-merchant-content-shopping-experiences`
- Rule Builder: `sw-merchant-marketing` (Marketing-Bereich)
- Standard-Kontaktformular: Erlebniswelten > Block „Formular"
- Shopware Evolve: https://www.shopware.com/de/preise/
