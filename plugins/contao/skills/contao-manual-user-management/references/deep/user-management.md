# Contao 5.x — Benutzerverwaltung

Quellen:
- https://docs.contao.org/5.x/manual/de/benutzerverwaltung/
- https://docs.contao.org/5.x/manual/de/benutzerverwaltung/benutzer/
- https://docs.contao.org/5.x/manual/de/benutzerverwaltung/mitglieder/

---

## Übersicht

Die Benutzerverwaltung ist eine eigene Kategorie in der Backend-Navigation mit vier Modulen:

| Modul | Zweck |
|-------|-------|
| **Benutzer** | Backend-Benutzer (Redakteure, Administratoren) |
| **Benutzergruppen** | Berechtigungspakete für Backend-Benutzer |
| **Mitglieder** | Frontend-Benutzer (Besucher mit Login) |
| **Mitgliedergruppen** | Zugriffsgruppen für Frontend-Mitglieder |

---

## 1. Backend-Benutzer

### Unterschied Benutzer vs. Administratoren

| Merkmal | Normale Benutzer | Administratoren |
|---------|-----------------|-----------------|
| Zugriffsrechte | Nur explizit freigegebene Module | Voller Zugriff auf alles |
| Konfiguration | Über Benutzergruppen | Keine Einschränkungen |
| Standardrechte | Keine (muss alles freischalten) | Alle |

**Wichtig**: Normale Benutzer haben standardmäßig **überhaupt keine Rechte**. Alles muss explizit durch Administratoren freigeschaltet werden.

### Benutzergruppen

Benutzergruppen sind Sammlungen von Berechtigungen. Einzelne Benutzer erben die Berechtigungen ihrer Gruppen.

**Konfigurierbare Bereiche in Benutzergruppen:**

#### Backend-Module freischalten

| Bereich | Konfiguration |
|---------|--------------|
| Backend-Module | Welche Menüpunkte sichtbar sind |
| Inhaltselemente | Welche Element-Typen verwendet werden dürfen |
| Formularfelder | Welche Feldtypen im Formulargenerator nutzbar sind |
| Pagemounts | Auf welche Seiten/Seitenbäume Zugriff besteht |
| Filemounts | Auf welche Ordner in der Dateiverwaltung Zugriff besteht |
| Bildgrößen | Welche Bildgrößen im Editor wählbar sind |
| Mitgliedergruppen | Welche Frontend-Gruppen zugewiesen werden dürfen |

#### Spezielle Rechte

| Bereich | Beschreibung |
|---------|-------------|
| FAQ | Kategorien freischalten |
| Archive | Nachrichtenarchive, Kalender, Newsletter-Kanäle |
| Events | Kalender-Zugriff |
| Newsletter | Verteilerlisten verwalten |

#### Felder-Rechte pro Modul

Für jedes freigeschaltete Modul kann festgelegt werden, welche **einzelnen Eingabefelder** bearbeitet werden dürfen. Felder ohne Berechtigung erscheinen gesperrt oder gar nicht.

### Freischalten an zwei Stellen

Benutzerrechte müssen an **zwei Orten** konfiguriert werden:
1. In der **Benutzerverwaltung**: Module, Pagemounts, Feldrechte
2. In der **Seitenstruktur**: Zugriffsrechte pro Seite (welche Gruppe darf Artikel bearbeiten)

### Benutzerkonten — Konfigurierbare Einstellungen

| Einstellung | Beschreibung |
|-------------|-------------|
| Benutzername | Eindeutiger Loginname |
| E-Mail-Adresse | Kontakt und Benachrichtigungen |
| Backend-Sprache | Sprache der Backend-Oberfläche |
| UI-Optionen | Theme (Hell/Dunkel), Shortcuts |
| Gruppen | Zugehörigkeit zu Benutzergruppen |
| Administrator | Vollzugriff ohne Gruppeneinschränkungen |
| Zwei-Faktor-Authentifizierung | TOTP (Google Authenticator, etc.) |
| Aktivierung | Zeitgesteuert aktivieren/deaktivieren |

### Zwei-Faktor-Authentifizierung (2FA)

Benutzer können 2FA über ihr Profil aktivieren:
1. Im Benutzermenü auf **„Sicherheit"** klicken
2. QR-Code mit TOTP-App scannen (z.B. Google Authenticator, Aegis)
3. Code bestätigen
4. Ab sofort ist beim Login ein TOTP-Code erforderlich

Administratoren können 2FA für alle Benutzer **verpflichtend** machen.

---

## 2. Frontend-Mitglieder

Frontend-Mitglieder sind Besucher, die sich im Frontend anmelden können. Diese Funktion ist **optional** — nur nötig, wenn geschützte Bereiche existieren.

### Mitgliedergruppen

Mitglieder werden in Gruppen organisiert. Gruppen steuern:
- Zugriff auf **geschützte Seiten**
- Weiterleitung nach Login (wenn im Login-Modul aktiviert)
- Zeitgesteuerte Aktivierung/Deaktivierung

### Mitglieder-Datenverwaltung

#### Personendaten
- Vorname, Nachname
- Geburtsdatum
- Geschlecht

#### Adressdaten
- Firma
- Straße, PLZ, Ort
- Staat, Land

#### Kontaktdaten
- Telefon, Handy, Fax
- E-Mail-Adresse *(muss eindeutig sein)*
- Webseite
- Sprache (für mehrsprachige Projekte)

#### Zugangsdaten
- Benutzername *(muss eindeutig sein)*
- Passwort (verschlüsselt gespeichert)

#### Weitere Einstellungen
- **Home-Verzeichnis**: Optionales persönliches Dateiverzeichnis
- **Mitgliedergruppen**: Gruppenzugehörigkeit
- **Abonnements**: Newsletter-Verwaltung
- **Kontoeinstellungen**: Aktivierung/Deaktivierung, zeitgesteuert möglich

### Geschützte Bereiche einrichten

**Schritt-für-Schritt:**

1. **Mitgliedergruppe** anlegen (Benutzerverwaltung → Mitgliedergruppen)
2. **Mitglied** anlegen und Gruppe zuweisen
3. **Seite schützen** in der Seitenstruktur:
   - Seite bearbeiten → Zugriffsschutz aktivieren
   - Erlaubte Mitgliedergruppen auswählen
4. **Login-Modul** erstellen und in Seitenlayout einbinden:
   - Layout → Module → Neu → Typ: „Login-Formular"
   - Weiterleitung nach Login konfigurieren
5. **Fehlerseiten** anlegen:
   - Typ „401 Nicht authentifiziert" für nicht eingeloggte Besucher
   - Typ „403 Zugriff verweigert" für eingeloggte Besucher ohne Rechte

### Passwort-Reset für Frontend-Mitglieder

Mitglieder können ihr Passwort über ein **Passwort-Vergessen-Modul** zurücksetzen:
- Modul-Typ: „Passwort vergessen"
- Link per E-Mail mit Token (Double-Opt-In)

---

## 3. Praxis-Tipps

### Administrator-Passwort vergessen

Falls kein Admin-Zugang möglich ist:
1. Direkt in der Datenbanktabelle `tl_user` den `admin`-Wert auf `1` setzen, oder
2. Alle Admin-Flags zurücksetzen und im Contao Install-Tool neuen Admin anlegen:
   - URL: `https://example.com/contao/install`

Via CLI:
```bash
php vendor/bin/contao-console contao:user:create --admin
```

### Benutzer-Passwort zurücksetzen

```bash
php vendor/bin/contao-console contao:user:password benutzername
```

### Alle Benutzer auflisten

```bash
php vendor/bin/contao-console contao:user:list
php vendor/bin/contao-console contao:user:list --admins
```
