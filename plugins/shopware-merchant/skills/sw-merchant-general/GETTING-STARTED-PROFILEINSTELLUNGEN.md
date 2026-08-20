# Profileinstellungen

**Quelle**: https://docs.shopware.com/de/shopware-6-de/einstellungen/Profileinstellungen  
**Gilt ab**: Shopware 6.4.8.0

## Überblick

Die Profileinstellungen ermöglichen jedem Admin-Benutzer die **persönliche Konfiguration** der
eigenen Darstellung und Präferenzen in der Administration.

**Zugang**: Links unten in der Administration → Profilbild/Name klicken

---

## Profilbereich

### Persönliche Informationen
| Feld | Beschreibung | Änderbar hier? |
|---|---|---|
| Vorname | Anzeigename in der Administration | Nein¹ |
| Nachname | Anzeigename in der Administration | Nein¹ |
| Benutzername | Login-Name | Nein¹ |
| E-Mail-Adresse | Login & Benachrichtigungen | Ja |
| Profilbild | Eigenes Bild hochladen (JPG, PNG) | Ja |
| Sprache der Administration | Deutsch, Englisch, weitere bei installierten Sprachpaketen | Ja |

> ¹ Kernprofilinformationen (Name, Benutzername) nur änderbar unter:
> **Einstellungen > System > Benutzer & Rechte > Benutzer [Name] bearbeiten**

---

## Passwort ändern

1. Im Profilbereich zu **Passwort** navigieren
2. Aktuelles Passwort eingeben
3. Neues Passwort eingeben (2× zur Bestätigung)
4. Speichern

---

## Sucheinstellungen (Search Settings)

Jeder Benutzer kann individuell konfigurieren, **welche Entitäten** die Administrations-Suche
indexieren und durchsuchen soll:

- **Alle auswählen** – Alle verfügbaren Entitäten aktivieren
- **Alle abwählen** – Alle Entitäten deaktivieren
- **Standard wiederherstellen** – Zurück auf Shopware-Default

### Durchsuchbare Entitäten (Standard)
- Produkte
- Bestellungen
- Kunden
- Kategorien
- Medien
- Hersteller
- Eigenschaften

---

## Tastenkürzel-Übersicht

Im Profil gibt es eine Sektion **Tastenkürzel** mit allen verfügbaren Shortcuts:

| Kürzel | Aktion |
|---|---|
| `Strg/Cmd + F` | Schnellsuche öffnen |
| `#` in Suche | Modul-Filter öffnen |
| `Strg/Cmd + S` | Speichern (in Formularen) |
| `Esc` | Modal / Überlagerung schließen |

---

## Sprache der Administration

- **Wechsel**: Profil > Sprache > Auswahl → Seite neu laden
- **Wichtig**: Ändert nur die **Administrationssprache**, nicht die Storefront-Sprache
- Für neue Sprachen: Sprachpaket-Erweiterung installieren
  → Siehe `../../../sw-merchant-extensions/references/deep/sprachpaket.md`
