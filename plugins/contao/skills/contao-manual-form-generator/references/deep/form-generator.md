# Contao 5.x – Formulargenerator

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).

---

## 1. Formulare konfigurieren

Der Formulargenerator befindet sich im Backend unter **Inhalte**. Formulare können Daten per E-Mail versenden oder in der Datenbank speichern. Validierung erfolgt automatisch anhand vorgegebener Regeln.

### Titel und Weiterleitung

| Einstellung | Beschreibung |
|-------------|-------------|
| **Titel** | Nur im Backend sichtbar |
| **Formular-Alias** | Eindeutige Referenz als Alternative zur numerischen Formular-ID |
| **Weiterleitungsseite** | Zielseite nach Absendung (Bestätigungsseite) |

### Formular-Konfiguration

| Option | Beschreibung |
|--------|-------------|
| **HTML-Tags erlauben** | Erlaubt HTML-Eingaben in Feldern mit konfigurierbaren Tags |
| **Per Ajax senden** | Kein Redirect; Bestätigungsmeldung; nutzt Simple Tokens (ab Contao 5.1) |

### Formulardaten versenden (E-Mail)

Daten werden per E-Mail an einen oder mehrere Empfänger gesendet. Dateifelder werden automatisch als Anhang beigefügt.

| Einstellung | Beschreibung |
|-------------|-------------|
| **Per E-Mail versenden** | Aktiviert E-Mail-Versand |
| **Empfänger-Adresse** | Kommagetrennte Liste von E-Mail-Adressen |
| **Betreff** | E-Mail-Betreffzeile |
| **Datenformat** | Rohdaten, XML, CSV, CSV (Excel) oder E-Mail-Format |
| **Leere Felder auslassen** | Nur ausgefüllte Felder senden |

**Datenformate:**
| Format | Details |
|--------|---------|
| Rohdaten | Unbearbeitete Feldinhalte untereinander |
| XML-Datei | XML-Anhang mit Formulardaten |
| CSV-Datei | CSV mit Formulardaten |
| CSV-Datei (Excel) | CSV im Microsoft-Excel-Format |
| E-Mail | Formatiert wie manuelle Nachricht; verarbeitet `name`, `email`, `subject`, `message` |

**Spezielle Feldnamen:**
| Feldname | Auswirkung |
|----------|-----------|
| `email` | Wird als Reply-To-Adresse verwendet |
| `name` | Name für Reply-To-Adresse |
| `firstname` + `lastname` | Name für Reply-To (ohne `name`-Feld) |
| `cc` | E-Mail-Adresse erhält Kopie |

**Empfehlung SMTP:** Ohne benutzerdefinierten SMTP-Server erfolgt der Versand über Sendmail, was zu Problemen führen kann. Nutzung des E-Mail-Transportprotokolls (SMTP) wird empfohlen.

### Formulardaten speichern (Datenbank)

| Einstellung | Beschreibung |
|-------------|-------------|
| **Eingaben speichern** | Aktiviert Datenbankspeicherung |
| **Zieltabelle** | Vorher erstellte Tabelle mit gleichnamigen Spalten |

**Wichtig:** Feldnamen müssen exakt mit Datenbankspalten übereinstimmen. Sonderzeichen wie Bindestriche können Probleme verursachen.

### Experten-Einstellungen

| Option | Beschreibung |
|--------|-------------|
| **Übertragungsmethode** | POST (Standard) oder GET |
| **HTML5-Validierung deaktivieren** | Fügt `novalidate`-Attribut hinzu |
| **CSS-ID/-Klasse** | Gezielte CSS-Formatierung |
| **Formular-ID** | Identifiziert das Formular für Frontend-Module |

---

## 2. Formularfelder

Alle Felder benötigen mindestens **Feldname** und **Feldbezeichnung**. Alle unterstützen CSS-Klassen, Tastaturkürzel und Tab-Index.

### Erklärung
Rich-Text-Block zur Information. Erzeugt Wrapper-Div mit Klasse `widget-explanation`.

### HTML-Code
Benutzerdefinierter HTML-Inhalt ohne umschließendes Markup.

### Fieldset Anfang/Ende
Logische Gruppierung von Steuerelementen. Semantisches `<fieldset>`-Element mit `<legend>`.

### Textfeld
Einzeiliges Eingabefeld.

**Validierungsregeln:**
- Numerisch, alphabetisch, alphanumerisch
- Datum/Uhrzeit-Formate
- Telefonnummer, E-Mail-Validierung
- URL (relativ und absolut)
- Benutzerdefinierte Regex

**Zusätzliche Optionen:**
- Platzhalter-Text
- Hilfetext (ab Contao 5.6)
- Min./Max-Eingabelänge
- Standardwert

### Passwortfeld
Zwei-Felder-System (Passwort + Bestätigung), maskierte Eingabe.

### Textarea
Mehrzeiliges Feld. Konfigurierbare Reihen und Spalten. Identische Validierung wie Textfeld.

### Select-Menü (Dropdown)
- Mehrfachauswahl optional
- Konfigurierbare Listengröße mit Scroll
- JavaScript-gestützter Optionseditor mit Gruppierungsmöglichkeit
- CSS-Klasse `multiselect` bei aktivierter Mehrfachauswahl

### Radio-Button-Menü
Einzelauswahl aus mehreren Optionen.

### Checkbox-Menü
Mehrfachauswahl ohne Beschränkung. Verstecktes Eingabefeld verhindert leere Array-Übertragung.

### Datei-Upload
- Dateityp-Whitelist (kommagetrennte Endungen)
- Dateigröße-Limit (Standard: 2 MB)
- Bild-Dimensionsprüfung (Breite/Höhe)
- Speicherort-Konfiguration
- Home-Verzeichnis-Option für eingeloggte Mitglieder
- Duplikat-Handling mit numerischen Suffixen

### Range-Slider
- Minimalwert und Maximalwert
- Schrittgröße
- Standardwert

### Verstecktes Feld
Unsichtbares Feld für Datenübertragung ohne Benutzerinteraktion.

### Sicherheitsfrage (CAPTCHA)
- "Honeypot"-Technik mit versteckten Köder-Feldern
- Automatische Spambot-Erkennung
- Mathematische Fallback-Aufgabe bei Fehlalarmen
- Datenverlust-Sicherheit garantiert

### Absendefeld
Schaltfläche zum Formularversand.
- **Textschaltfläche** (Standard)
- **Bildschaltfläche** mit Bildauswahl

---

## 3. Suchformular erstellen (Tutorial)

Ein benutzerdefiniertes Suchformular kann mit dem Formulargenerator erstellt und in der Kopfzeile eingebunden werden.

**Schritte:**
1. Neues Formular erstellen; Übertragungsmethode: **GET**; Weiterleitungsseite: die Suchseite
2. Textfeld hinzufügen; Feldname: `keywords`; optional als Pflichtfeld markieren
3. Optional: Radio-Button-Menü; Feldname: `query_type`; Optionswerte: `and` und `or`
4. Absendefeld hinzufügen
5. Formular als Frontend-Modul in das Seitenlayout (z.B. Kopfzeile) einbinden

---

Quellen:
- https://docs.contao.org/5.x/manual/de/formulargenerator/
- https://docs.contao.org/5.x/manual/de/formulargenerator/formulare/
- https://docs.contao.org/5.x/manual/de/formulargenerator/formularfelder/
- https://docs.contao.org/5.x/manual/de/formulargenerator/ein-suchformular-erstellen/
