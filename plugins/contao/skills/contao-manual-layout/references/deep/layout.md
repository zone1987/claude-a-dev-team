# Contao 5.x – Layout: Theme-Manager, Module & Templates

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).

---

## 1. Theme-Manager

### Themes verwalten

Ein Theme fasst alle designrelevanten Elemente einer Webseite zusammen.

**Bestandteile eines Themes:**
- Das Theme selbst
- Stylesheets
- Frontend-Module
- Seitenlayouts
- Bildgrößen
- Dateien (Upload-Verzeichnis)
- Angepasste Templates (optional)

Hinweis: Stylesheets, Module, Layouts und Bildgrößen liegen in der Datenbank. Dateien und Templates liegen in Unterverzeichnissen.

**Konfigurationsfelder:**

| Feld | Beschreibung |
|------|-------------|
| **Theme-Titel** | Name in Backend-Übersicht und Export-Dateiname |
| **Autor** | Name des Theme-Designers |
| **Ordner** | Zugehörige Ordner aus dem Upload-Verzeichnis |
| **Bildschirmfoto** | Screenshot für die Theme-Übersicht |
| **Templates-Ordner** | Unterordner mit angepassten Templates |

**Export:** `.cto`-Datei (ZIP-Archiv) mit `theme.xml`, `files/` und `templates/`.

**Import:** Prüft fehlende Felder in Tabellen, nicht vorhandene Layoutbereiche und bereits existierende Templates. Nach dem Import muss das Theme durch Zuweisung eines Seitenlayouts zu einer Seite aktiviert werden.

**Sicherheitswarnung:** Nur Themes von vertrauenswürdigen Herstellern installieren.

---

### Stylesheets verwalten

Der interne CSS-Editor ist **veraltet** und wird in einer zukünftigen Contao-Version entfernt. Bestehende Stylesheets exportieren und als externe Stylesheets in Seitenlayouts einbinden.

**Medientypen:**
- `all`, `screen`, `print`, `handheld`, `projection`, `aural`, `braille`, `embossed`, `tty`, `tv`
- Relevanteste für Webseiten: `screen` und `print`

**Bedingungskommentare:** Internet Explorer-spezifische Direktiven (`if IE`, `if lt IE 6`, `if gte IE 6`).

**Formatdefinitions-Reihenfolge:** Wichtig! Spätere Definitionen überschreiben frühere. Neuordnung per Drag-and-Drop.

**Import/Export:** CSS-Dateien importieren oder exportieren über Navigationssymbole.

---

### Seitenlayouts verwalten

Das Seitenlayout strukturiert die Webseite und teilt sie in Layoutbereiche für Frontend-Module ein.

**Kopf-/Fußzeile:**
- Konfigurierbare Zeilenhöhen
- Typisch: Firmenlogo oben, Copyright unten

**Spaltenkonfiguration:**
- Bis zu drei Spalten (links, Haupt, rechts)
- Anpassbare Breiten für linke und rechte Spalte
- Hauptspalte passt sich automatisch an

**Eigene Layoutbereiche:**
Fünf Standard-Bereiche plus benutzerdefinierte Bereiche. Positionen: `top`, `before`, `main`, `after`, `bottom`, `manual`.

**CSS-Framework-Komponenten:**
- Layout-Builder (für Seitengenerator erforderlich)
- Responsives Layout
- 12-Spalten-Grid
- CSS-Reset
- Formularunterstützung
- Icon-Ressourcen

**Stylesheets:**
- Interne und externe CSS-Dateien
- SCSS- und LESS-Unterstützung (Achtung: interne Bibliothek unterstützt ggf. nicht alle modernen Dart-Sass-Features)
- Konfigurierbare Ladereihenfolge
- Optionale Komprimierung

**Webfonts:** Google Fonts-Integration; manuelle Einbindung empfohlen.

**JavaScript-Templates:**
| Template | Funktion |
|----------|---------|
| `js_autofocus` | Fokus-Navigation bei Formularfehlern |
| `js_highlight` | Syntax-Highlighter |
| `js_nocookie` | CSRF-Schutz-Benachrichtigung |
| `js_slider` | Content-Slider-Funktionalität (Legacy) |
| `js_accordion` | Akkordeon (Legacy) |

**jQuery und MooTools:** Optional ladenbar. Quelle: lokal, CDN oder CDN mit Fallback.

**Analytics:** Google Analytics und Matomo (Piwik) über Template.

**Bildgrößen:** Lightbox-Dimensionen mit responsiven Pixeldichten (1x, 1.5x, 2x).

**RSS/Atom-Feeds:** Verknüpfung mit News- und Kalender-Feeds im `<head>`.

**Statisches Layout:** Konvertiert Liquid Layout in feste Breite (links/rechts/zentriert).

**Experten-Einstellungen:**
- Benutzerdefinierte Seitentemplates
- Markup-Komprimierung
- Viewport-Tag-Anpassung
- Title-Tag-Überschreibung
- Body-Klassen und -Events
- Zusätzliche `<head>`-Tags

---

## 2. Modulverwaltung

Module werden innerhalb von Themes erstellt und in Seitenlayouts eingebunden. Sie generieren HTML-Code für die Frontend-Ausgabe.

**Zugriffsschutz:** Einschränkung auf Mitgliedergruppen; Option "Nur Gästen anzeigen" in Experten-Einstellungen.

---

### 2.1 Navigationsmodule

#### Navigationsmenü
Hierarchische Navigation aus allen veröffentlichten, nicht versteckten Seiten.

| Einstellung | Beschreibung |
|-------------|-------------|
| **Startlevel** | Einstiegspunkt (z.B. Level 2 für Untermenüs) |
| **Stoplevel** | Maximale Verschachtelungstiefe |
| **Harter Grenzwert** | Keine Elemente jenseits des Stoplevels |
| **Geschützte Seiten anzeigen** | Eingeloggt-beschränkte Seiten einbeziehen |
| **Versteckte Seiten anzeigen** | Aus Navigation ausgeblendete Seiten einbeziehen |
| **Referenzseite** | Eigener Startpunkt statt Wurzel |
| **Navigationstemplate** | Template-Auswahl |

Template: `mod_navigation`

#### Individuelle Navigation
Menü aus frei wählbaren Seiten (ohne Hierarchie-Abhängigkeit).
Template: `mod_customnav`

#### Navigationspfad (Breadcrumb)
Zeigt den Pfad zur aktuellen Seite.
Template: `mod_breadcrumb`

#### Quicknavigation (Dropdown)
Dropdown-Menü zum direkten Seitensprung.
- Custom Label, Stoplevel, harter Grenzwert, Referenzseite
- Template: `mod_quicknav`

#### Quicklink
Dropdown aus frei wählbaren Seiten.
Template: `mod_quicklink`

#### Buchnavigation
Vor-/zurück-/aufwärts-Navigation durch Seiten ("Blättern").
Template: `mod_booknav`

#### Artikelnavigation
Vor-/zurück-Navigation durch Artikel einer Seite.
- **Erstes Element laden**: Ersten Artikel automatisch laden
- Template: `mod_articlenav`

#### HTML-Sitemap
Übersicht aller veröffentlichten, nicht versteckten Seiten.
Template: `mod_sitemap`

**HTML-Ausgabe:** Alle Navigationsmodule nutzen `<!-- indexer::stop -->` und `<!-- indexer::continue -->` Kommentare sowie schema.org-Markup.

---

### 2.2 Benutzermodule

#### Login-Formular
Authentifizierung für registrierte Mitglieder.
- Auto-Login, Passwort-Reset-Seite (ab 5.3), Weiterleitungsseite
- Option: Zur zuletzt besuchten Seite weiterleiten
- Template: `ce_login`

#### Personendaten
Mitglieder können persönliche Daten bearbeiten.
- Editierbare Felder konfigurierbar
- Newsletter-Abonnement (wenn Erweiterung aktiv)
- Templates: `member_default` (linear) oder `member_grouped` (Fieldsets)

#### Registrierung
Neuanmeldung für Besucher.
- Pflichtfelder, Mitgliedergruppen, Home-Verzeichnis, Spam-Schutz
- E-Mail-basierte Aktivierung (24-Stunden-Link)
- Platzhalter: `##firstname##`, `##domain##`, `##link##`
- Templates: `member_default`, `member_grouped`

#### Passwort ändern
Für eingeloggte Mitglieder. Altes Passwort wird verifiziert.
Template: `ce_changePassword`

#### Passwort vergessen
Wiederherstellung via E-Mail. Spam-Schutz, Bestätigungsseite, E-Mail-Template.
Template: `ce_lostPassword`

#### Konto schließen
Konto deaktivieren oder dauerhaft löschen, optional Home-Verzeichnis entfernen.
Template: `ce_closeAccount`

#### Zwei-Faktor-Authentifizierung
TOTP/2FA-Setup mit QR-Code für Authenticator-Apps, Backup-Key-Anzeige.
Template: `ce_two_factor`

---

### 2.3 Website-Suche

#### Suchmodul

| Einstellung | Funktion |
|-------------|---------|
| **Standard-Abfragetyp** | UND oder ODER |
| **Ungenaue Suche** | Platzhalter-ähnliche Ergebnisse |
| **Kontext-Spannweite** | Zeichenanzahl um gefundene Begriffe |
| **Minimale Suchwort-Länge** | Mindestzeichenzahl (0 = deaktiviert) |
| **Elemente pro Seite** | Paginierung |
| **Suchformular-Layout** | Einfach oder erweitert (mit UND/ODER-Optionen) |
| **Weiterleitungsseite** | Ziel nach Formularabsendung |
| **Referenzseite** | Einschränkung auf Seitenbereich |

**Suchsyntax:**
- `"web design"` – Phrasensuche (exakte Reihenfolge)
- `web*` – Platzhalter-Suche
- `+web` – Begriff erzwingen
- `-web` – Begriff ausschließen

**Indexierungssteuerung:**
```html
<!-- indexer::stop -->
[Inhalt wird nicht indiziert]
<!-- indexer::continue -->
```

**Geschützte Seiten indexieren** (in `config/config.yaml`):
```yaml
contao:
  search:
    index_protected: true
```

---

### 2.4 Anwendungsmodule

#### Formular
Bindet ein Formular aus dem Formulargenerator ein.
Einstellung: **Formular** — Auswahl des einzufügenden Formulars.

#### Auflistung
Listet Datenbankdatensätze auf — sortierbar, filterbar, durchsuchbar.

| Einstellung | Beschreibung |
|-------------|-------------|
| **Tabelle** | Datenbankquelle |
| **Felder** | Kommagetrennte Feldliste |
| **Bedingung** | SQL-Filter oder Insert-Tags |
| **Durchsuchbare Felder** | Erzeugt Suchformular |
| **Sortieren nach** | Standard-Sortierung |
| **Elemente pro Seite** | Paginierung |
| **Felder der Detailseite** | Detail-Ansicht aktivieren |

---

### 2.5 Verschiedenes

#### Artikelliste
Zeigt alle Artikel einer ausgewählten Spalte.
- Überspringen von Elementen, Spaltenwahl, Referenzseite
- Template: `mod_articlelist`

#### Zufallsbild
Zufälliges Bild aus Ordner/Auswahl.
- Skalierungsmodi, Lightbox, Bildunterschrift
- Template: `mod_randomImage`

#### Eigener HTML-Code
Beliebiger HTML-Code (Backend-Sicherheitsregeln).
Template: `mod_html`

#### RSS-Reader
Abonniert und zeigt RSS-Feeds.
- Feed-URLs, Gesamtbeiträge, Elemente pro Seite, Cache-Dauer
- Templates: `rss_default` (Header + Posts) oder `rss_items_only`

#### Startpunktabhängige Module
Wählt unterschiedliche Module je Startpunkt — verhindert mehrere Layout-Varianten.

#### Individuelles Template
Template mit eigenen Schlüssel/Wert-Paaren.
Template: `mod_template`

---

## 3. Templates

Templates steuern die HTML-Ausgabe von Modulen, Inhaltselementen, Formularen und anderen Komponenten. Im Backend unter Layout > Templates können sie ohne Update-Risiko angepasst werden.

**Typen:** PHP-Templates und Twig-Templates.

**Wichtig:** Für CSS-Anpassungen ist ein Template-Override oft nicht nötig — CSS-ID und -Klasse können direkt in den Experten-Einstellungen gesetzt werden.

---

Quellen:
- https://docs.contao.org/5.x/manual/de/layout/
- https://docs.contao.org/5.x/manual/de/layout/theme-manager/
- https://docs.contao.org/5.x/manual/de/layout/theme-manager/themes-verwalten/
- https://docs.contao.org/5.x/manual/de/layout/theme-manager/stylesheets-verwalten/
- https://docs.contao.org/5.x/manual/de/layout/theme-manager/seitenlayouts-verwalten/
- https://docs.contao.org/5.x/manual/de/layout/modulverwaltung/
- https://docs.contao.org/5.x/manual/de/layout/modulverwaltung/navigationsmodule/
- https://docs.contao.org/5.x/manual/de/layout/modulverwaltung/benutzermodule/
- https://docs.contao.org/5.x/manual/de/layout/modulverwaltung/website-suche/
- https://docs.contao.org/5.x/manual/de/layout/modulverwaltung/anwendungen/
- https://docs.contao.org/5.x/manual/de/layout/modulverwaltung/verschiedenes/
- https://docs.contao.org/5.x/manual/de/layout/templates/
