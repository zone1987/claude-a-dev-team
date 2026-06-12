# Contao 5.x – Artikelverwaltung & Inhaltselemente

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).

---

## 1. Artikelverwaltung

Artikel verknüpfen Inhalte mit Seiten und Layoutbereichen. Jede Seite kann beliebig viele Artikel enthalten, die im zugeordneten Layoutbereich der Reihe nach ausgegeben werden.

### Kerneinstellungen eines Artikels

| Feld | Beschreibung |
|------|-------------|
| **Artikel-Alias** | Eindeutige Referenz; ermöglicht Direktaufruf via URL `seite/articles/alias.html` |
| **Teasertext** | Kurzfassung für Übersichtsseiten |
| **Teaser CSS-ID/Klasse** | Individuelle Stilisierung des Teasers |
| **Teaser anzeigen** | Wird automatisch aktiviert, wenn mehrere Artikel je Bereich existieren |
| **Syndikation** | Print-Funktion, Facebook- und Twitter-Sharing |
| **Individuelles Template** | Überschreibt das Standard-Template `mod_article` |

### Zugriffsschutz

- **Schutz aktivieren** – nur sichtbar für angemeldete Mitglieder
- **Erlaubte Mitgliedergruppen** – Gruppenauswahl
- **Nur Gästen anzeigen** (Experten-Einstellungen) – wird ausgeblendet, sobald ein Mitglied eingeloggt ist

### Veröffentlichung

- Manueller Schalter
- **Anzeigen ab / Anzeigen bis** – zeitgesteuerte Aktivierung/Deaktivierung

---

## 2. Inhaltselemente – Übersicht

Contao bietet sieben Kategorien von Inhaltselementen. Ab Contao 5.3 unterstützen drei Elemente **verschachtelte Inhaltselemente** (Akkordeon, Elementgruppe, Content Slider).

---

## 3. Text-Elemente

### Überschrift
- **Text** + Hierarchie (h1–h6)
- Template: `content_element/headline`

### Text
- Rich-Text-Editor (TinyMCE)
- Optionales Bild mit Ausrichtung (oben, unten, linksbündig, rechtsbündig)
- Bildgrößen-Modi: Exaktes Format, Proportional, An Rahmen anpassen
- Template: `content_element/text`

### HTML
- Beliebiger HTML-Code (nur erlaubte Tags)
- Kein umschließendes Markup

### Ungefiltertes HTML *(ab Contao 5.3)*
- Keinerlei Tag-Beschränkung (Vorsicht!)
- Template: `content_element/unfilteredHtml`

### Aufzählung (geordnet/ungeordnet)
- Listentyp wählbar
- CSV-Import möglich
- Template: `content_element/list`

### Tabelle
- Kopf-/Fußzeile, Zeilenkopf, Sortierbarkeit
- CSV-Import
- Template: `content_element/table`

### Code
Syntax-Highlighting für: Apache, Bash, C#, C++, CSS, Diff, HTML, HTTP, Ini, JSON, Java, JavaScript, Markdown, Nginx, Perl, PHP, PowerShell, Python, Ruby, SCSS, SQL, Twig, YAML, XML.
Ausgabe: `<div class="content-code"><pre><code>…</code></pre></div>`

### Markdown
- Quelle: Text oder Datei
- Erweiterter Syntax (Tabellen, Fußnoten)
- Template: `content_element/markdown`

### Beschreibungsliste *(ab Contao 5.3)*
- Schlüssel-Wert-Paare (`<dl>/<dt>/<dd>`)
- Template: `content_element/descriptionList`

---

## 4. Link-Elemente

### Hyperlink
Erzeugt einen Link zu einer externen URL oder E-Mail-Adresse.

| Feld | Beschreibung |
|------|-------------|
| **Link-Adresse** | URL inkl. Protokoll (http://, mailto:, tel:) |
| **In neuem Fenster öffnen** | Öffnet Link in neuem Tab |
| **Link-Text** | Angezeigter Text statt der URL |
| **Den Link einbetten** | Bettet Link in umgebenden Text ein (`%s` als Platzhalter) |
| **Link-Titel** | `title`-Attribut |
| **Lightbox** | `data-lightbox`-Attribut für Lightbox-Kontrolle |
| **Bild als Link** | Ersetzt Text durch Bild-Link |

Template: `content_element/hyperlink`

### Top-Link
Springt an den Seitenanfang. Link-Text: Standard "Nach oben".
Template: `content_element/toplink`

---

## 5. Datei-Elemente

### Download
Einzelne Datei zum Herunterladen oder im Browser anzeigen.

| Feld | Beschreibung |
|------|-------------|
| **Quelldatei** | Dateiauswahl |
| **Im Browser anzeigen** | Kein Download-Dialog |
| **Link überschreiben** | Eigener Link-Text und -Titel |
| **Vorschaubilder** | Zeigt Vorschau-Thumbnails; Anzahl konfigurierbar |

Template: `content_element/download`

### Downloads
Mehrere Dateien / Ordner. Zusätzlich:
- **Sortieren nach**: Benutzerdefiniert, Dateiname (auf-/absteigend), Datum, Zufällig
- **Dateien ohne Metadaten ignorieren**
- **Home-Verzeichnis verwenden** (bei eingeloggten Mitgliedern)

Template: `content_elements/downloads`

---

## 6. Media-Elemente

### Bild
| Feld | Beschreibung |
|------|-------------|
| **Quelldatei** | Bild-Auswahl |
| **Bildgröße** | Dimensionen |
| **Lightbox/Neues Fenster** | Öffnet Originalgröße beim Klick |
| **Metadaten überschreiben** | Individuelle Alt-/Titel-Daten |
| **Bildlink-URL** | Klickbares Bild (deaktiviert Lightbox) |
| **Bildunterschrift** | Beschriftungstext |

Ausgabe: `<figure>`-Element mit optionalem `<figcaption>`

### Galerie
| Feld | Beschreibung |
|------|-------------|
| **Quelldateien** | Ordner oder einzelne Bilder |
| **Home-Verzeichnis** | Bei eingeloggten Mitgliedern |
| **Sortieren nach** | Benutzerdefiniert, Dateiname, Datum, Zufällig |
| **Vorschaubilder pro Reihe** | Spaltenanzahl |
| **Elemente pro Seite** | Paginierung |
| **Lightbox** | Vollbild-Ansicht |

### Video/Audio
| Einstellung | Optionen |
|-------------|---------|
| **Autoplay** | Ja/Nein |
| **Steuerelemente** | Anzeigen/Ausblenden |
| **Loop** | Ja/Nein |
| **Inline** | Kein Vollbild |
| **Vorladestufe** | Auto, Metadaten, Keine |
| **Untertitel** | Optionaler Track |
| **Start-/Stoppzeit** | In Sekunden |
| **Vorschaubild** | Ersetzt erstes Frame |

Template: `content_element/player`

### Vimeo
- **Vimeo-ID**, Autoplay, Loop, Profil-/Titel-/Autor-Ausblenden
- Steuerfarben (Hex), Startzeit
- **Splash-Screen**: Erst bei Klick laden (Datenschutz)

Template: `content_element/vimeo`

### YouTube
- **YouTube-ID**, umfangreiche Player-Optionen
- **youtube-nocookie.com**-Domain (Datenschutz)
- Verwandte Videos aus gleichem Kanal
- **Splash-Screen**: Lazy-Load mit eigenem Bild

Template: `content_element/youtube`

---

## 7. Verschiedenes (verschachtelte Elemente, ab Contao 5.3)

### Akkordeon
Mehrere auf-/zuklappbare Abschnitte. Nur ein Abschnitt gleichzeitig offen.

| Einstellung | Beschreibung |
|-------------|-------------|
| **Alle Abschnitte schließen** | Verhindert, dass erster Abschnitt automatisch öffnet |

Template: `content_element/accordion`
HTML: `<div class="content-accordion">` mit `handorgel__header`-Buttons und `handorgel__content`-Regionen (ARIA).

### Elementgruppe
Gruppiert mehrere Inhaltselemente zu einem Kindelement — nützlich innerhalb von Sliders oder Akkordeons.
Template: `content_element/element_group`

### Content Slider
Slideshow aus verschiedenen Inhaltselementen via Swiper.

| Einstellung | Beschreibung |
|-------------|-------------|
| **Slide-Intervall** | Millisekunden (0 = deaktiviert) |
| **Übergangsgeschwindigkeit** | Millisekunden |
| **Slide-Versatz** | Startposition (ab 0) |
| **Kontinuierlich** | Loop |

Template: `content_element/swiper`

---

## 8. Include-Elemente

| Element | Beschreibung |
|---------|-------------|
| **Artikel** | Bindet anderen Artikel ein (nur Inhaltselemente, kein Header) |
| **Inhaltselement** | Bindet bestehendes Element als Alias ein |
| **Formular** | Fügt ein Formular aus dem Formulargenerator ein |
| **Modul** | Bindet ein Frontend-Modul ein |
| **Kommentare** | Ermöglicht Besucherkommentare; Einstellungen: Moderation, BBCode, Login-Pflicht, Spam-Schutz |
| **Individuelles Template** | Template mit eigenen Schlüssel/Wert-Paaren |
| **Artikelteaser** | Zeigt Teasertext eines anderen Artikels mit "Weiterlesen"-Link |

---

## 9. Legacy-Elemente (Wrapper-System, vor Contao 5.3)

### Akkordeon (Legacy)
Verwendet `js_accordion`-Template im Seitenlayout.

| Modus | Funktion |
|-------|---------|
| Einzelelement | Einzelner Abschnitt mit Text und optionalem Bild |
| Umschlag Anfang | Eröffnet Akkordeon-Bereich |
| Umschlag Ende | Schließt Akkordeon-Bereich |

- Einstellungen: Bereichsüberschrift (HTML erlaubt), CSS-Format, Klassen für Toggler und Akkordeon
- Templates: `ce_accordionSingle`, `ce_accordionStart`

### Slider (Legacy)
Verwendet `js_slider`-Template im Seitenlayout.

| Modus | Funktion |
|-------|---------|
| Umschlag Anfang | Eröffnet Slider |
| Umschlag Ende | Schließt Slider |

- Einstellungen: Slide-Intervall, Übergangsgeschwindigkeit, Slide-Versatz, Kontinuierlich
- Template: `ce_sliderStart`

---

## 10. Gemeinsame Einstellungen aller Inhaltselemente

- **Template überschreiben**: Individuelles Template wählbar
- **Zugriffsschutz**: Einschränkung auf Mitgliedergruppen
- **CSS-ID/-Klasse**: In den Experten-Einstellungen
- **Nur Gästen anzeigen**: Sichtbar nur für nicht-eingeloggte Besucher

---

Quellen:
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/artikel/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/text-elemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/media-elemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/link-elemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/datei-elemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/include-elemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/legacy-elemente/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/inhaltselemente/verschiedenes/
