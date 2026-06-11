# Shopware 6 – Benutzer & Rechte (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/System/benutzer

---

## Überblick

**Pfad:** Einstellungen > System > Benutzer & Rechte  
**Verfügbar ab:** 6.4.5.0

Verwaltung von Administratoren und deren Zugriffsrechten in Shopware 6.

---

## 1. Benutzerverwaltung

### Benutzerübersicht
- Alle erstellten Administratoren mit Namen, Rollen, E-Mail-Adressen
- Bearbeitung und Löschung via Kontextmenü
- „Neuer Benutzer"-Button

### Felder beim Anlegen eines Benutzers

| Feld | Beschreibung |
|---|---|
| Vorname / Nachname | Identifikation |
| E-Mail-Adresse | Für Passwort-Zurücksetzen erforderlich |
| Benutzername | Login-Anmeldedaten |
| Passwort | Admin-Zugang (im Profil änderbar) |
| Sprache der Benutzeroberfläche | Wählbare Sprache (im Profil änderbar) |
| Jobtitel | Interne Berufsbezeichnung |
| Profilbild | Zur Unterscheidung in Benutzerlisten |
| Administrator-Status | Vollständige Rechte (selbst nicht zuweisbar) |
| Zeitzone | Für einheitliche Zeitangaben |
| Rollen | Zuweisung vordefinierter Rollen (nur wenn nicht Admin) |

---

## 2. Rollenverwaltung

### Rollenübersicht
- Alle Rollen mit Name und Beschreibung
- Bearbeitung/Löschung via Kontextmenü
- „Neue Rolle"-Button

### Felder
- **Name:** Aussagekräftige Bezeichnung
- **Beschreibung:** Kurze Rollencharakterisierung

---

## 3. Berechtigungssystem

### Hierarchie der Hauptberechtigungen

| Berechtigung | Beschreibung |
|---|---|
| **Ansehen** | Nur Sichtbarkeit, keine Änderungen |
| **Bearbeiten** | Bestehende Konfigurationen ändern |
| **Erstellen** | Neue Entitäten hinzufügen |
| **Löschen** | Entitäten entfernen (auto. mit Ansehen-Recht) |
| **Alle** | Vollzugriff auf den Bereich |

**Vererbungshierarchie:** Löschen → Ansehen; Erstellen → Bearbeiten → Ansehen

---

## 4. Zusätzliche Berechtigungen (Allgemein)

| Berechtigung | Umfang |
|---|---|
| Grundlegende Einstellungen | Einstellungen > Shop (Adressen, Login/Reg., Produkte, SEO, Sitemap, Stammdaten, Warenkorb) + System (Mailer, Shopware-Account) |
| Update starten | Shopware-Updates suchen und installieren |
| Erweiterungen verwalten | Installation, Deinstallation, Aktivierung, Deaktivierung |
| Erweiterung hochladen | ZIP-Datei-Upload in Meine Erweiterungen |
| Ereignis-Logs | Zugriff auf Shopware- und Systemlogs |
| Cache leeren | Caches & Indizes verwalten |
| Import/Export | Datenimport/-export, Profil-Management |
| Shopware Store | Store-Zugriff |
| Eigenes Profil ändern | Persönliche Profileinstellungen |
| Gutschriften erstellen | Gutscheinpositionen im Bestellungsmodul |
| Apps | Gesamter Erweiterungsbereich |

---

## 5. Detaillierte Privilegien

Für Ausnahmefälle (z.B. Erweiterungen ohne korrektes ACL):
- Technische Namen aller Berechtigungen
- Granulare Lesen/Schreiben/Erstellen/Löschen-Rechte pro Funktion
- Grau hinterlegte Checkboxen = bereits im Tab „Allgemein" vergeben

### Fehlerbehandlung
Fehlermeldungen zeigen fehlende Berechtigungen (z.B. `order`, `order_customer`, `order_delivery` — Bearbeiten-Recht) für manuelle Nachkonfiguration.

---

## 6. Konfiguration der Admin-Suche

Pro Benutzer konfigurierbar:
- Selektive Bereichsfreigabe für Suchergebnisse
- Beispiel: Promotions-Bereich aktiviert → Suche nach Rabatt-Codes möglich
