# Shopware 6 — Tutorials: EU-Regelungen (vollständige Referenz)

---

## 1. DSGVO (Datenschutz-Grundverordnung)

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/dsgvo  
**Gültig ab:** 25. Mai 2018

### Welche personenbezogenen Daten werden verarbeitet?

| Kategorie | Daten |
|-----------|-------|
| Kundendaten | Adresse, Geburtsdatum, Firmenname |
| Bestellungen | Lieferadresse, Bestellsumme, Warenkorb, IP-Adresse, Referrer |
| Newsletter | Registrierungsdaten |
| Formulare | Anrede, Name, E-Mail, Telefon |
| Bewertungen | Mit Kundenkonto verknüpfte Produktbewertungen |
| Admin | Mitarbeiterdaten mit E-Mail |
| API | Über autorisierte Schnittstellen abrufbare Daten |

### IP-Adressen werden gespeichert in

- `order_customer` (je Bestellung)
- `customer` (letzte Bestellung)
- `log_entry` (Backend-Aktivitäten)
- `version_commit_data` (aktuelle Nutzungsdaten)

### Verschlüsselung

HTTPS-Protokoll mit SSL-Zertifikat für sichere Datenübertragung erforderlich.

### Cookies (Browser-Speicherung)

- Session-Cookies (Warenkorb, Login-Status)
- CSRF-Cookies (Schutzfunktion)
- Timezone-Cookies (Zeitzonenkalibrierung)

Shopware speichert stets nur IDs im Browser des Kunden.

### Datenschutzerklärung einbinden

- Vorkonfigurierte Erlebniswelt "Datenschutz" nutzen
- Unter Einstellungen > Shop > Stammdaten anpassen
- In Checkout und Formularen verlinken

### Cookie Consent Manager

- Shopware bietet integrierten Cookie Consent Manager
- Plugins können eigene Cookies registrieren
- Link für spätere Änderungen: `/cookie/offcanvas`
- Einstellungen: Einstellungen > Allgemein > Stammdaten (Alles-akzeptieren-Button)
- Texte anpassen: Einstellungen > Regional > Textbausteine (Suche "Cookie")

### Daten strukturiert ausgeben (Export)

Import/Export-Funktion für CSV/XML-Export personenbezogener Daten.

### Daten löschen

Über Admin-Kundenmodul durchführbar (automatische Verknüpfungsentfernung).

**Warenkörbe:** Standard-Löschung nach 120 Tagen, konfigurierbar via `shopware.yaml`.

### FAQ

- Kein separates DSGVO-Plugin geplant — Updates werden bei Notwendigkeit bereitgestellt
- Registrierung referenziert Datenschutz via Textbaustein `general.privacyNotice`
- Formulare enthalten automatische Datenschutz-Checkbox
- Drittanbieter-Erweiterungen (PayPal, ERP, Newsletter) können eigene Datenflüsse initiieren

---

## 2. One-Stop-Shop-Verfahren (EU-OSS)

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/one-stop-shop  
**Ab Version:** 6.4.1.0  
**Gültig ab:** 1. Juli 2021

### Definition

EU-OSS ist ein elektronisches Portal, über das Händler und Unternehmen ihre Mehrwertsteuerverpflichtung innerhalb der EU zentral erfüllen können, anstatt sich in jedem Land einzeln zu registrieren.

### Schwellenwert

**10.000 € EU-weit (einheitlich).** Händler, die diesen Betrag überschreiten, sollten sich beim zuständigen OSS-Portal registrieren.

### Shopware-Konfiguration

- Steuersätze weiterhin über das Steuern-Modul konfigurieren
- Anzeige des Lieferlandes neben dem Preis erforderlich
- Kunden müssen Lieferland transparent auswählen können (mit entsprechenden Preisen)

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/eu-regelungen — Stand: 2026-06*
