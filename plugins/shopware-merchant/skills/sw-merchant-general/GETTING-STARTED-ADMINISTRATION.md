# Administration im Überblick

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/administration-ueberblick

## Überblick

Die Shopware-6-Administration ist das zentrale Backend für die Verwaltung des Online-Shops.
Sie nutzt ein zentrales Anzeige-Format (kein separates Fenstermanagement) und kann in
**mehreren Browser-Tabs parallel** geöffnet werden.

---

## Zugang

- **URL-Schema**: `https://www.meinshop.de/admin`
- **Login**: E-Mail/Benutzername + Passwort
- **Passwort vergessen**: Über den Login-Screen, Bestätigungs-E-Mail an hinterlegte Adresse

---

## Hauptbereiche der Oberfläche

### 1. Linke Navigationsleiste

Die primäre Navigation verläuft links und enthält:

| Bereich | Beschreibung |
|---|---|
| **Dashboard** | Startseite nach Login, Statistik-Übersicht |
| **Bestellungen** | Bestellverwaltung, Retouren |
| **Kunden** | Kundenstammdaten, Gruppen |
| **Katalog** | Produkte, Kategorien, Eigenschaften, Medien |
| **Content** | Erlebniswelten (Shopping Experiences / CMS) |
| **Marketing** | Promotionen, Gutscheine, Newsletter |
| **Verkaufskanäle** | Storefront, Headless, Social, POS |
| **Erweiterungen** | Store, Meine Erweiterungen |
| **Einstellungen** | System, Zahlungen, Versand, Steuern, Benutzer |

- Oben in der Leiste: **Shopware-Versionsnummer** sichtbar
- Unten in der Leiste: **Profil-Einstellungen** (Name, Sprache, Passwort)
- **Navigation minimieren**: Klick auf Pfeil-Icon → nur Icons werden angezeigt (mehr Platz)

---

### 2. Obere Leiste (Top Bar)

| Element | Funktion |
|---|---|
| **Suchleiste (Mitte)** | Suche über Produkte, Kategorien, Kunden, Bestellungen, Medien |
| **Glocken-Icon** | Benachrichtigungen: System-Updates, Plugin-Updates, Hinweise |

---

### 3. Hauptbereich (Content Area)

- Zeigt den Inhalt des aktuell gewählten Menüpunkts
- **Mehrere Tabs**: Browser-Tabs können unabhängig voneinander verschiedene Admin-Seiten anzeigen
- Keine Desktop-Fenster-Metapher – alle Aktionen im gleichen Tab

---

## Tastenkürzel

| Kürzel | Funktion |
|---|---|
| `Strg/Cmd + F` | Schnellsuche öffnen |
| `#` in Suche tippen | Modul-Filterauswahl öffnen |

Vollständige Übersicht: **Profil > Tastenkürzel**

---

## Mehrsprachigkeit der Administration

- Sprache wechseln: Profil (links unten) > Sprache auswählen
- Verfügbare Sprachen: Abhängig vom installierten Sprachpaket
- Standard: Deutsch und Englisch

---

## Interaktiver Lernpfad

Im **Community Hub** (https://hub.shopware.com) gibt es einen interaktiven Lernpfad,
um die Administration praktisch kennenzulernen:
- Schritt-für-Schritt-Anleitungen
- Sandbox-Übungen
- Networking mit anderen Shopware-Nutzern

---

## Hinweis: Berechtigungen

Nicht alle Menüpunkte sind für jeden Benutzer sichtbar. Das hängt von der
**Benutzerrolle** ab (konfigurierbar unter Einstellungen > System > Benutzer & Rechte).

- Administrator: Vollzugriff
- Benutzerdefinierte Rollen: Eingeschränkte Sichtbarkeit/Bearbeitung
