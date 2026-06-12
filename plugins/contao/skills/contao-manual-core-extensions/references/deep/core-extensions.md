# Contao 5.x – Core-Erweiterungen

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).
Paket: Bestandteil der "Vollständigen Installation".

---

## 1. News/Blog-Erweiterung (`contao/news-bundle`)

News-Einträge können im Backend verwaltet und mit Frontend-Modulen ausgegeben werden. Beiträge können mit Inhaltselementen beliebig strukturiert werden.

### 1.1 Nachrichtenarchive

Archive organisieren News-Einträge nach Themen oder Sprachen.

**Titel und Weiterleitung:**
- **Titel**: Backend-Anzeige
- **Weiterleitungsseite**: Ziel für "Weiterlesen"-Links (sollte Nachrichtenleser-Modul enthalten)

**Zugriffsschutz:** Archiv schützen, erlaubte Mitgliedergruppen.

**Kommentare:**
| Einstellung | Beschreibung |
|-------------|-------------|
| Kommentare aktivieren | Aktivierungsschalter |
| Benachrichtigung an | Systemadmin, Artikelautor oder beide |
| Sortierreihenfolge | Aufsteigend (älteste zuerst) oder absteigend |
| Kommentare pro Seite | Pagination-Limit |
| Moderieren | Freigabe vor Veröffentlichung |
| BBCode erlauben | [b], [i], [u], [img], [code], [color], [quote], [url], [email] |
| Login zum Kommentieren benötigt | Nur für registrierte Mitglieder |
| Spam-Schutz deaktivieren | Für authentifizierte Nutzer |

**RSS-Feeds:** RSS 2.0, Atom oder JSON. Konfiguration über "News-Feed"-Seitentyp.

### 1.2 Nachrichtenbeiträge

Einstellungen:

| Feld | Beschreibung |
|------|-------------|
| **Titel** | Artikelüberschrift |
| **Beitrag hervorheben** | Hervorgehobener Status (über Archive hinweg) |
| **Nachrichtenalias** | URL-Referenz |
| **Autor** | Änderbar |
| **Datum/Uhrzeit** | Veröffentlichungsdatum |

**Weiterleitungsziel:**
- Standard (Archiv-Standardseite)
- Seite / Artikel / Individuelle URL
- Link-Text, Kanonische URL (ab 5.3), neues Fenster

**Metadaten:**
- Meta-Titel, Robots-Tag (index/follow/noindex/nofollow), Meta-Beschreibung (150–300 Zeichen)
- Google-Suchergebnis-Vorschau

**Inhalt:**
- Unterüberschrift, Teasertext
- Bild mit Ausrichtung (oben/unten/links/rechts), Skalierungsmodi, Lightbox, Alt-Text, Link
- Anlagen (Dateien für RSS-Export und Download)

**Experten-Einstellungen:**
- CSS-Klasse
- Kommentare deaktivieren
- Suchindexierer (ab 5.6): Standard / Immer indizieren / Niemals indizieren

**Veröffentlichung:** Manuell, Anzeigen ab, Anzeigen bis.

### 1.3 Frontend-Module

#### Nachrichtenliste
Zeigt Beiträge aus einem oder mehreren Archiven.

| Einstellung | Beschreibung |
|-------------|-------------|
| Nachrichtenarchive | Quell-Archive |
| Nachrichtenleser | Automatisch wechseln bei Beitrags-Auswahl |
| Anzahl an Elementen | Limit |
| Hervorgehobene Beiträge | Alle / Nur hervorgehobene / Hervorgehobene überspringen / Hervorgehobene zuerst |
| Sortierreihenfolge | Datum auf-/absteigend, Überschrift auf-/absteigend, Zufällig |
| Elemente überspringen | Offset |
| Elemente pro Seite | Paginierung |

**Templates:**
- `news_full` – Vollständiger Artikel (für Nachrichtenleser empfohlen)
- `news_latest` – Metadaten, Bild, Überschrift, Teaser, "Weiterlesen"
- `news_short` – Metadaten, Überschrift, Teaser, "Weiterlesen"
- `news_simple` – Datum und Überschrift

#### Nachrichtenleser
Zeigt einzelne Beiträge via URL-Alias (Permalink).
Beispiel: `www.example.com/nachricht/form-folgt-funktion.html`
Gibt HTTP 404 zurück, wenn kein Artikel gefunden.

| Einstellung | Beschreibung |
|-------------|-------------|
| Nachrichtenarchive | Zu durchsuchende Archive |
| Aktuelle URL für kanonische Links | Ab Contao 5.3 |
| Übersichtsseite | Seite für "Zurück zur Übersicht"-Link |

#### Nachrichtenarchiv
Listet alle Beiträge eines Zeitraums (Tag/Monat/Jahr).
- Archivformat: Tag, Monat oder Jahr
- "Kein Zeitraum ausgewählt": Modul ausblenden / Aktuellen Zeitraum anzeigen / Alle anzeigen

#### Nachrichtenarchiv-Menü
Navigationsmenü nach Tag/Monat/Jahr.
- Beitragsanzahl anzeigen, Sortierreihenfolge, Weiterleitungsseite

**Achtung:** Nur ein Lesermodul pro Seite erlaubt. Nachrichtenlisten nicht in Seitenlayouts einbauen (Auto-Switch vermeiden).

---

## 2. Kalender-Erweiterung (`contao/calendar-bundle`)

Verwaltet vergangene und zukünftige Veranstaltungen. Unterstützt Wiederholungstermine.

### 2.1 Terminarchive

**Kommentare:** Identische Konfiguration wie bei News-Archiven.

**RSS-Feeds:**
| Einstellung | Beschreibung |
|-------------|-------------|
| Format | RSS 2.0 oder Atom |
| Exporttyp | Teaser-Text oder vollständige Einträge |
| Max. Beiträge | Typisch 25 |
| Basis-URL | Für Multi-Domain-Setups |

### 2.2 Termine

| Feld | Beschreibung |
|------|-------------|
| **Titel** | Veranstaltungsname |
| **Zeit hinzufügen** | Aktiviert Zeitangaben |
| **Start-/Endzeit** | Optional (ohne Ende: offenes Ende) |
| **Start-/Enddatum** | Mehrtägige Events |
| **Veranstaltungsort** | Name und Adresse |
| **Teasertext** | Kurzfassung für Listen |

**Wiederholungen:**
- Aktivierbar; Intervall: Tag(e), Woche(n), Monat(e), Jahr(e)
- Wiederholungsanzahl; automatisch ausblenden nach N Wiederholungen

**Metadaten und Anlagen:** Analog zu News-Beiträgen.

### 2.3 Frontend-Module

#### Kalender
- Standard-Kalender (`cal_default`) – groß, klickbare Ereignisse
- Mini-Kalender (`cal_mini`) – kompakt mit Tageslinks
- Verkürzte Darstellung für Mehrtages-Events
- Hervorgehobene Events: Alle / Nur hervorgehobene / Hervorgehobene überspringen
- Weiterleitungsseite für Mini-Kalender

#### Eventleser
Zeigt einzelne Events via Permalink.
Beispiel: `www.example.com/event/european-design-awards.html`

**Event-Templates:**
- `event_full` – Vollständig (für Leser empfohlen)
- `event_list` – Titel, Datum/Uhrzeit, Eventtext
- `event_teaser` – Titel, Datum/Uhrzeit, Teaser, "Weiterlesen"
- `event_upcoming` – Datum und Titel

#### Eventliste
Listen nach Zeitraum; Anzeigeformat:
- Eventliste (Zeitraum), Zukünftige Events (Vorschau), Vergangene Events (Rückblick)

#### Eventliste-Menü
Navigation nach Tag/Monat/Jahr. Soll die gleichen Kalender verwenden wie die Eventliste.

---

## 3. FAQ-Erweiterung (`contao/faq-bundle`)

Verwaltet häufig gestellte Fragen in Kategorien.

### 3.1 FAQ-Kategorien

**Einstellungen:**
- **Titel** (Backend)
- **Überschrift** (Frontend)
- **Weiterleitungsseite** (sollte FAQ-Leser-Modul enthalten)
- **Kommentare**: Identische Konfiguration wie News

### 3.2 Fragen

| Feld | Beschreibung |
|------|-------------|
| **Frage** | Fragestellung |
| **FAQ-Alias** | URL-Referenz |
| **Autor** | Änderbar |
| **Antwort** | Rich-Text-Editor |
| **Bild** | Optional, mit Skalierungsmodi und Ausrichtung |
| **Anlagen** | Dateien für Download |

**Metadaten:** Meta-Titel, Robots-Tag, Meta-Beschreibung, Google-Vorschau.

### 3.3 Frontend-Module

#### FAQ-Liste
Zeigt Fragen aus einer oder mehreren Kategorien als Liste mit Links.
```html
<div class="mod_faqlist block">
  <ul><li><a href="…">…</a></li></ul>
</div>
```

#### FAQ-Leser
Zeigt die Antwort auf eine bestimmte Frage via Permalink.
Beispiel: `example.com/frage/kann-ich-eigene-php-skripte-verwenden.html`
Gibt HTTP 404 zurück, wenn nicht gefunden.

#### FAQ-Seite
Zeigt alle Fragen und Antworten aus gewählten Kategorien auf einer einzigen Seite.
```html
<div class="mod_faqpage block">
  <article>
    <h2>FAQ</h2>
    <section><h3>…</h3><div class="ce_text block">…</div></section>
    <p class="toplink"><a href="#top">Nach oben</a></p>
  </article>
</div>
```

---

## 4. Newsletter-Erweiterung (`contao/newsletter-bundle`)

Verwaltet Newsletter und Empfängerlisten. Versand direkt aus dem Backend. Double Opt-In integriert.

### 4.1 Verteiler (Newsletter-Archiv)

**Einstellungen:**
| Feld | Beschreibung |
|------|-------------|
| **Titel** | Backend-Referenz |
| **Weiterleitungsseite** | Ziel für Frontend-Modul-Links |

**E-Mail-Templates (ab 5.3):**
- `mail_default` – HTML 3.2 für breite Kompatibilität
- `mail_responsive` – Modernes responsives Design

Template-Variablen: `$this->charset`, `$this->title`, `$this->body`, `$this->css`

**Absender-Konfiguration:**
- Absender-E-Mail (Pflichtfeld)
- Absendername
- Mailer-Transport (für Multi-Domain-Setups)

### 4.2 Newsletter-Inhalte

| Einstellung | Beschreibung |
|-------------|-------------|
| **Betreff** | E-Mail-Betreffzeile |
| **Newsletter-Alias** | URL-freundlicher Bezeichner |
| **HTML-Inhalt** | Rich-Text mit Preheader-Text (5.3+, 40–130 Zeichen) |
| **Text-Inhalt** | Plaintext-Fallback |
| **Anlagen** | Dateien für Versand |

**Personalisierung mit Simple Tokens:**
```
##firstname## ##lastname##
{if gender=="male"}Herr {elseif gender=="female"}Frau {else}Damen und Herren{endif}
```

**Experten-Einstellungen:**
- Text-Only-Modus
- Externe Bilder (verhindert Einbettung in HTML-Version)

### 4.3 Abonnenten-Verwaltung

- Datensätze enthalten nur E-Mail und Aktivierungsstatus (Datenschutz)
- Double Opt-In: Bestätigungs-E-Mail vor Aktivierung
- Manuelle Aktivierung im Backend möglich
- CSV-Import: Trennzeichen Komma, Semikolon, Tab, Zeilenumbruch

### 4.4 Versandprozess

**Server-Limit-Konfiguration:**
- E-Mails pro Zyklus
- Wartezeit zwischen Zyklen (Sekunden)
- Versatz (Offset) für unterbrochenen Versand

Beispiel: 100 E-Mails/Minute → 10 E-Mails alle 6 Sekunden

**Unterbrochenen Versand fortsetzen:**
1. System-Log prüfen (Kategorie: `NEWSLETTER_X`)
2. Anzahl gesendeter E-Mails notieren
3. Diesen Wert als Offset eingeben

### 4.5 Frontend-Module

#### Abonnieren
- Verteiler auswählen, Verteilermenü ausblenden, Spam-Schutz
- Eigener Text (DSGVO-Hinweise)
- Weiterleitungsseite
- Bestätigungs-E-Mail mit `##channel##`, `##domain##`, `##link##`

#### Kündigen
- Verteiler, Menü ausblenden, Spam-Schutz
- Weiterleitungsseite
- Bestätigungs-E-Mail mit `##channel##`, `##domain##`

#### Newsletterliste
Zeigt alle gesendeten Newsletter (nach Datum sortiert, neueste zuerst).

#### Newsletterleser
Einzelnen Newsletter via Permalink.
Beispiel: `www.example.com/newsletterleser/newsletteralias.html`
Gibt HTTP 404 zurück, wenn nicht gefunden.

---

## 5. Kommentare (Weiterleitung)

Die Kommentarfunktion ist als Include-Inhaltselement eingebunden und nicht als eigene Core-Extension eigenständig. Kommentareinstellungen werden pro Archiv (News, Kalender, FAQ) oder direkt im Inhaltselement "Kommentare" konfiguriert.

Einstellungen: Sortierung, Paginierung, Moderation, BBCode, Login-Pflicht, Spam-Schutz.

---

## 6. Auflistung (Weiterleitung)

Das Auflistungs-Modul befindet sich unter Layout > Modulverwaltung > Anwendungen und ist kein separates Core-Bundle, sondern Teil des Core. Siehe Layout-Referenz für Details.

---

Quellen:
- https://docs.contao.org/5.x/manual/de/core-erweiterungen/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/nachrichten/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/nachrichten/nachrichtenverwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/nachrichten/frontend-module/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/kalender/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/kalender/terminverwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/kalender/frontend-module/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/faq/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/faq/faq-verwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/faq/frontend-module/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/newsletter/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/newsletter/newsletter-verwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/newsletter/frontend-module/
