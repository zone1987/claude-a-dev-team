# Contao 5.x – Insert-Tags & Simple Tokens

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).

---

## Insert-Tags

Insert-Tags sind Platzhalter der Form `{{keyword}}` oder `{{keyword::parameter}}`, die beim Rendern einer Seite durch ihre Werte ersetzt werden. Sie können überall in Contao verwendet werden.

---

## 1. Link-Tags

| Tag | Beschreibung |
|-----|-------------|
| `{{link::*}}` | HTML-Link; Parameter: Seiten-ID, Alias oder absolute URL |
| `{{link::login}}` | Link zur Login-Seite des aktuellen Frontend-Benutzers |
| `{{link_open::*}}` / `{{link_close}}` | Öffnendes und schließendes Link-Tag |
| `{{link_url::*}}` | Nur die URL |
| `{{link_title::*}}` | Title-Attribut der Seite |
| `{{link_name::*}}` | Name der Seite |
| `{{article::*}}` | Link zu Artikel (ID oder Alias) |
| `{{article_open::*}}` / `{{article_url::*}}` / `{{article_title::*}}` | Artikel-Varianten |
| `{{news::*}}` | Link zu einem News-Eintrag |
| `{{news_open::*}}` / `{{news_url::*}}` / `{{news_title::*}}` / `{{news_feed::*}}` | News-Varianten |
| `{{event::*}}` | Link zu einem Event |
| `{{event_open::*}}` / `{{event_url::*}}` / `{{event_title::*}}` / `{{calendar_feed::*}}` | Event-Varianten |
| `{{faq::*}}` | Link zu einer FAQ-Frage |
| `{{faq_open::*}}` / `{{faq_url::*}}` / `{{faq_title::*}}` | FAQ-Varianten |

### Link-Parameter
- `::absolute` – Ausgabe als absolute URL
- `::blank` – Öffnet in neuem Fenster mit `target="_blank" rel="noreferrer noopener"`

---

## 2. Mitglieder-Eigenschaften

Greifen auf Felder der `tl_member`-Tabelle des eingeloggten Frontend-Benutzers zu.

| Tag | Beschreibung |
|-----|-------------|
| `{{user::*}}` | Beliebiges Feld aus `tl_member` |
| `{{user::firstname}}` | Vorname |
| `{{user::lastname}}` | Nachname |
| `{{user::company}}` | Firma |
| `{{user::phone}}` / `{{user::mobile}}` / `{{user::fax}}` | Telefonnummern |
| `{{user::email}}` | E-Mail-Adresse |
| `{{user::website}}` | Website-URL |
| `{{user::street}}` | Straße |
| `{{user::postal}}` | PLZ |
| `{{user::city}}` | Stadt |
| `{{user::country}}` | Land |
| `{{user::username}}` | Benutzername |

---

## 3. Seiteneigenschaften

Greifen auf Felder der `tl_page`-Tabelle der aktuellen Seite zu.

| Tag | Beschreibung |
|-----|-------------|
| `{{page::*}}` | Beliebiges Feld aus `tl_page` |
| `{{page::id}}` | Aktuelle Seiten-ID |
| `{{page::alias}}` | Aktueller Seiten-Alias |
| `{{page::title}}` | Seitenname |
| `{{page::pageTitle}}` | Seitentitel |
| `{{page::description}}` | Seitenbeschreibung |
| `{{page::language}}` | Seitensprache |
| `{{page::parentAlias}}` / `{{page::parentTitle}}` / `{{page::parentPageTitle}}` | Übergeordnete Seite |
| `{{page::mainAlias}}` / `{{page::mainTitle}}` / `{{page::mainPageTitle}}` | Hauptübergeordnete Seite |
| `{{page::rootTitle}}` / `{{page::rootPageTitle}}` | Webseitenname und -titel |

---

## 4. Umgebungsvariablen

| Tag | Beschreibung |
|-----|-------------|
| `{{env::host}}` | Aktueller Hostname (z.B. example.com) |
| `{{env::url}}` | Hostname mit Protokoll (z.B. https://www.example.com) |
| `{{env::path}}` | Basis-URL mit Pfad zum Contao-Verzeichnis |
| `{{env::request}}` | Aktueller Request-String (z.B. news/items/welcome.html) |
| `{{env::ip}}` | IP-Adresse des Besuchers |
| `{{env::referer}}` | URL der zuvor besuchten Seite |
| `{{env::files_url}}` | Statische URL für das Upload-Verzeichnis |
| `{{env::assets_url}}` | Statische URL für das Assets-Verzeichnis |

---

## 5. Include-Tags

| Tag | Beschreibung |
|-----|-------------|
| `{{insert_article::*}}` | Artikel per ID oder Alias einbinden |
| `{{insert_content::*}}` | Inhaltselement per ID einbinden |
| `{{insert_module::*}}` | Modul per ID einbinden |
| `{{insert_form::*}}` | Formular per ID einbinden |
| `{{article_teaser::*}}` | Teaser-Text eines Artikels |
| `{{news_teaser::*}}` | Teaser eines News-Eintrags |
| `{{event_teaser::*}}` | Teaser eines Events |
| `{{file::*}}` | Einbinden von .php- oder .html5-Dateien aus templates/; UUID-Referenz möglich |

---

## 6. Diverses

| Tag | Beschreibung |
|-----|-------------|
| `{{fragment::*}}` | Wird als ESI-Fragment gerendert |
| `{{date}}` | Aktuelles Datum (globales Format) |
| `{{date::*}}` | Datum mit eigenem Format (PHP-Datumsfunktion) |
| `{{format_date::*::*}}` | UNIX-Timestamp oder standardisiertes Datum formatieren |
| `{{convert_date::*::*::*}}` | Datum von einem in ein anderes Format umwandeln |
| `{{last_update}}` / `{{last_update::*}}` | Letzter Aktualisierungs-Timestamp |
| `{{email::*}}` | Kodierter E-Mail-Link |
| `{{email_open::*}}` / `{{email_close}}` | Kodierter E-Mail-Link-Teile |
| `{{email_url::*}}` | Nur kodierte E-Mail-Adresse |
| `{{form_session_data::*}}` | Zugiff auf übermittelte Formularfeldwerte |
| `{{lang::*}}...{{lang}}` | Fremdsprachigen Text auszeichnen |
| `{{abbr::*}}...{{abbr}}` | Abkürzungen auszeichnen |
| `{{acronym::*}}...{{acronym}}` | Akronyme auszeichnen |
| `{{iflng::*}}` | Inhalt nur für bestimmte Sprache(n) anzeigen |
| `{{ifnlng::*}}` | Inhalt für andere Sprachen als die angegebene anzeigen |
| `{{image::*}}` | Bildvorschau mit Breite, Höhe, Alt, Klasse, Rel, Modus |
| `{{picture::*}}` | Responsives `<picture>`-Element mit Größenkonfiguration |
| `{{figure::*}}` | `<figure>`-Element mit `<picture>` und `<figcaption>` |
| `{{label::*}}` | Übersetzung aus Sprachdateien |
| `{{trans::*::*::*}}` | Symfony-Übersetzungssystem |
| `{{version}}` | Aktuelle Contao-Version |
| `{{toggle_view}}` | Wechselt zwischen Mobil- und Desktop-Layout |
| `{{br}}` | HTML-Zeilenumbruch `<br>` |
| `{{asset::*::*}}` | CSS/JavaScript-Pfade aus Packages einbinden |
| `{{empty}}` | Leerer String |

---

## 7. Verschachtelte Insert-Tags

Tags, die IDs oder Aliases ausgeben, können verschachtelt werden:

```
{{link::{{page::id}}::absolute}}   → Link zur aktuellen Seite (absolut)
{{link_url::{{page::id}}}}#anker  → Relativer Link mit Anker
```

**Achtung:** Endlosschleifen vermeiden (z.B. `{{insert_article::{{page::alias}}}}`) — Seitenabsturz möglich.

---

## 8. Insert-Tag-Flags

Flags verarbeiten die Tag-Ausgabe weiter. Mehrere Flags kombinierbar:

```
{{ua::browser|uncached}}
{{page::title|standardize|strtoupper}}
```

| Flag | Beschreibung |
|------|-------------|
| `refresh` | Ausgabe bei jedem Request neu generieren |
| `attr` | Sonderzeichen als HTML-Entities (für Attribute) |
| `urlattr` | Wie `attr`, zusätzlich Doppelpunkte URL-kodieren (verhindert `javascript:`-Protokolle) |
| `addslashes` | Backslash vor bestimmten Zeichen |
| `standardize` | Ausgabe standardisieren (z.B. Seiten-Aliases) |
| `ampersand` | & in Entities umwandeln |
| `specialchars` | Sonderzeichen in Entities umwandeln |
| `nl2br` | HTML-Zeilenumbrüche vor Zeilenenden einfügen |
| `strtolower` | Kleinbuchstaben |
| `utf8_strtolower` | Unicode-bewusste Kleinbuchstaben |
| `strtoupper` | Großbuchstaben |
| `utf8_strtoupper` | Unicode-bewusste Großbuchstaben |
| `ucfirst` | Ersten Buchstaben großschreiben |
| `lcfirst` | Ersten Buchstaben kleinschreiben |
| `ucwords` | Ersten Buchstaben jedes Worts großschreiben |
| `trim` | Leerzeichen an beiden Enden entfernen |
| `ltrim` | Leerzeichen am Anfang entfernen |
| `rtrim` | Leerzeichen am Ende entfernen |
| `utf8_romanize` | In römische Zeichen umwandeln |
| `encodeEmail` | E-Mail-Adressen kodieren |
| `number_format` | Zahl formatieren (keine Dezimalstellen) |
| `currency_format` | Währung formatieren (zwei Dezimalstellen) |
| `readable_size` | In lesbares Format umwandeln |
| `urlencode` | URL-kodieren |
| `rawurlencode` | RFC 3986-Kodierung |
| `flatten` | Array in kommagetrennte Schlüssel:Wert-Liste |

---

## 9. Basis-Entities

Spezielle Syntax für HTML-Entities (wenn per DCA `basicEntities` aktiviert):

| Syntax | Entity | Zweck |
|--------|--------|-------|
| `[&]` | `&amp;` | Ampersand |
| `[lt]` | `&lt;` | Kleiner-als |
| `[gt]` | `&gt;` | Größer-als |
| `[nbsp]` | `&nbsp;` | Geschütztes Leerzeichen |
| `[-]` | `&shy;` | Weiches Trennzeichen |
| `[zwsp]` | `&ZeroWidthSpace;` | Nullbreites Leerzeichen |
| `[lsqb]` | `&lsqb;` | Öffnende eckige Klammer |
| `[rsqb]` | `&rsqb;` | Schließende eckige Klammer |
| `[{]` / `[}]` | `{{` / `}}` | Insert-Tag-Syntax im Frontend anzeigen |

---

## Simple Tokens

Simple Tokens sind Platzhalter ähnlich wie Insert-Tags, aber der Einsatzbereich wird von der jeweiligen Funktion (Entwickler) festgelegt. Ab Contao 4.10 basieren sie auf der Symfony Expression Language.

### Syntax

- **Ausgabe:** `##tokenname##`
- **Bedingung:** `{if tokenname=="wert"}…{endif}` (keine Hashes in Bedingungen, geschweifte Klammern stattdessen)

### Verfügbare Standard-Tokens

| Token | Beschreibung | Modul |
|-------|-------------|-------|
| `##tstamp##` | Aktueller Timestamp | Allgemein |
| `##flang##` | Aktuelle Sprache | Allgemein |
| `##domain##` | Aktueller Domain | Newsletter |
| `##link##` | Newsletter-Link | Newsletter |
| `##channels##` | Abonnierte Kanäle | Newsletter |

### Einsatzbereiche

- Benutzerregistrierungs- und Passwortwiederherstellungs-Module
- Newsletter-Verwaltung (Leser, Abonnements, Kündigungen)
- Erweiterungen: Notification Center, Isotope eCommerce, Leads, MetaModels
- Insert-Tag-Platzhalter

### Praktische Anwendung

Dynamische Dateinamen: `datei_von_##tstamp##.pdf`
Dateipfade: `files/data/##form_broschuere##.pdf`

### Bedingungsoperatoren

| Operator | Funktion |
|----------|---------|
| `==` / `!=` | Gleichheitsvergleich |
| `===` / `!==` | Strikter Typvergleich |
| `<` / `>` / `<=` / `>=` | Vergleichsoperatoren |
| `&&` / `\|\|` | Logisches UND/ODER (ab 4.10) |
| `in` / `not in` | Array-Operationen (ab 4.10) |
| `contains` / `starts with` / `ends with` | String-Vergleich (ab 4.10) |
| `matches` | Regex-Muster (ab 4.10) |

---

Quellen:
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/insert-tags/
- https://docs.contao.org/5.x/manual/de/artikelverwaltung/simple-tokens/
