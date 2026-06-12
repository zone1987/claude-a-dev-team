# Contao 5.x – Drittanbieter-Erweiterungen

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).

---

## 1. Animated Timeline (`pdir/animated-timeline-bundle`)

**Hersteller:** pdir GmbH

**Beschreibung:** jQuery-Erweiterung für Contao 4 zur Darstellung von Inhalten in einer dynamischen Timeline mit Einblend-Animationen.

**Hauptfeatures:**
- Horizontale und vertikale Timeline-Orientierungen
- Responsive Design: Horizontal auf Desktop, vertikal auf Mobilgeräten
- Einblendanimationen (Fade-In)

**Dokumentation:** https://docs.pdir.de/#/animated-timeline/index

---

## 2. EasyThemes (`terminal42/contao-easy_themes`)

**Hersteller:** terminal42 gmbh

**Beschreibung:** Direktzugriff auf Stylesheets, Module, Seitenlayouts und Bildgrößen mit weniger Klicks – besonders nützlich bei mehreren Themes.

**Installation und Aktivierung:**
1. Backend → Benutzerverwaltung → Benutzer bearbeiten
2. Im letzten Abschnitt: "EasyTheme aktivieren" ankreuzen

**Konfiguration — Aktive Module:**
- Theme bearbeiten
- Stylesheets
- Frontend-Module
- Seitenlayouts
- Bildgrößen

**Hinweis:** Der interne CSS-Editor ist veraltet und wird in einer zukünftigen Contao-Version entfernt.

**Anzeigemodi:**
| Modus | Beschreibung |
|-------|-------------|
| Kontextmenü | Erscheint beim Rechtsklick auf Themes |
| Mouseover | Erscheint beim Überfahren der Themes |
| DOM-Inject | Wird direkt unterhalb der Themes angezeigt |
| Backend-Modul | Erstellt zusätzliches Backend-Modul (optionale Referenzgruppe) |

---

## 3. Isotope eCommerce (`isotope/isotope-core`)

**Hersteller:** terminal42 gmbh

**Beschreibung:** Kostenlose eCommerce-Lösung für das Contao CMS.

**Eigenes Benutzerhandbuch:** https://docs.isotopeecommerce.org/manual/de/

---

## 4. Maklermodul für Immobilienmakler (`pdir/maklermodul-bundle`)

**Hersteller:** pdir GmbH (kostenpflichtig)

**Beschreibung:** Spezialisiertes Modul für Immobilienmakler zur Verwaltung von Objektlisten und Kundeninteraktionen in Contao.

**Projekt-Website:** https://maklermodul.de
**Dokumentation:** https://docs.pdir.de/#/maklermodul/index

---

## 5. Merger² (`contao-community-alliance/merger2`)

**Hersteller:** Contao Community Alliance (CCA)

**Beschreibung:** Frontend-Modul für bedingungsbasierte Inhaltsanzeige und -zusammenführung. Unterstützt Artikel, Seiten und andere Frontend-Module.

**Hauptanwendungsfälle:**
- **Inhaltskonsolidierung:** Sprachspezifische Module bedingt anzeigen (z.B. nach Browser-Sprache) — reduziert Layout-Varianten
- **Bedingte Anzeige:** Module/Artikel nur bei bestimmten Kriterien zeigen (Seitentiefe, Mobilansicht, Browser-Sprache)
- **Artikelvererbung:** Automatische Weitergabe von Artikeln von Elternseiten an Kindseiten im Seitenbaum

**Detaillierte Konfiguration:** https://github.com/contao-community-alliance/merger2/wiki

---

## 6. MetaModels

**Hersteller:** MetaModels Team

**Beschreibung:** Erweiterung für strukturierte Dateneingabe und -ausgabe in verschiedenen Formaten. Keine Programmierkenntnisse erforderlich.

**Anwendungsfelder:**
- Produktkataloge
- Veranstaltungen
- Menü- und Speisepläne
- Adressen- und Mitarbeiterverzeichnisse
- Immobilienlisten
- Bildgalerien
- Mehrsprachige Inhaltsverwaltung

**Features:**
- Listen- und Detailansicht
- Filterungen, Sortierungen, Paginierungen
- Mehrsprachige Unterstützung

**Paket:** https://packagist.org/packages/metamodels/
**Handbuch:** https://metamodels.readthedocs.io/de/latest/

---

## 7. News Facebook Sync (`inspiredminds/contao-news-facebook`)

**Hersteller:** INSPIRED MINDS (kostenpflichtig, ab v9.0)

**Beschreibung:** Automatische Synchronisierung zwischen Facebook-Seiten/-Gruppen und Contao-Newsarchiven. Import von Facebook-Posts als Nachrichtenbeiträge und Veröffentlichung von Contao-News auf Facebook.

### Installation

`composer.json` anpassen:
```json
{
  "repositories": [
    {
      "type": "composer",
      "url": "https://<USERNAME>:<TOKEN>@packeton.inspiredminds.at"
    }
  ],
  "require": {
    "inspiredminds/contao-news-facebook": "^9.0"
  }
}
```

### Facebook-App erstellen (optional)

1. developers.facebook.com → App erstellen
2. Anwendungsfall: "Other", Typ: "Business"
3. "Facebook Login for Business" hinzufügen
4. Redirect-URI: `https://example.org/_facebook/callback`

### App-Credentials konfigurieren (optional, falls keine integrierte App)

`config/config.yaml`:
```yaml
contao_news_facebook:
    app_id: '%env(FACEBOOK_APP_ID)%'
    app_secret: '%env(FACEBOOK_APP_SECRET)%'
```

`.env.local`:
```
FACEBOOK_APP_ID=123456789123456
FACEBOOK_APP_SECRET=abc123...
```

### Newsarchiv konfigurieren

1. Nachrichtenarchiv öffnen
2. "Facebook-Sync" aktivieren
3. Numerische Facebook-Seiten-ID eingeben
4. "Seitenbeiträge abrufen" aktivieren (optional: Datumsgrenzen)
5. "Facebook verbinden" für Token-Autorisierung
6. Bilder-Download-Ordner konfigurieren (Standard: `files/facebook_images`)

### Zusätzliche Systemeinstellungen
- **OpenGraph-Metatags deaktivieren**: Verhindert automatische `og:image`-Tags bei geteilten Artikeln
- **Als Fotos posten**: Erneut aktivieren, wenn Artikel mit Teaser-Bild als Foto gepostet werden sollen

**Headline-Länge konfigurieren:**
```yaml
contao_news_facebook:
    headline_length: 64
```

### Verwendung

- **Facebook-Posts abrufen**: Stündlich via Contao-Cronjob
- **Nach Facebook veröffentlichen**: Wenn "Auf Facebook-Seite posten" im Artikel aktiviert; minutlich geprüft
- **Manuell synchronisieren**: Button in globalen Operationen der Nachrichtenarchive

### Hooks

**`processFacebookPost`:** Anpasst Konvertierung von Facebook-Posts zu Contao-Beiträgen.

**`changeFacebookMessage`:** Ändert den Nachrichtentext vor dem Facebook-Post.

```php
#[AsHook('changeFacebookMessage')]
class ChangeFacebookMessageListener
{
    public function __invoke(string $message, $news, $archive): string
    {
        if ($news->addImage && $news->fbPostAsPhoto) {
            $message .= "\n\n".$this->generator->generate($news, [], 1);
        }
        return $message;
    }
}
```

### Template-Daten

Templates erhalten zusätzliche Variablen:
- `fbData` – Originaldaten des Facebook-Posts
- `fbPostId` – Zugehörige Facebook-Post-ID
- `fromFb` – Boolean: Facebook-Herkunft

---

## 8. Weitere erwähnte Erweiterungen

**News Sync** (`inspiredminds/contao-news-sync`): Kostenpflichtige Erweiterung zur Synchronisierung von Nachrichtenartikeln zwischen Contao-Installationen.

**Social Feed**: Zeigt Feeds von Facebook und Instagram an.

---

Quellen:
- https://docs.contao.org/5.x/manual/de/erweiterungen/
- https://docs.contao.org/5.x/manual/de/erweiterungen/animated-timeline/
- https://docs.contao.org/5.x/manual/de/erweiterungen/contao-easy_themes/
- https://docs.contao.org/5.x/manual/de/erweiterungen/isotope-core/
- https://docs.contao.org/5.x/manual/de/erweiterungen/maklermodul/
- https://docs.contao.org/5.x/manual/de/erweiterungen/merger2/
- https://docs.contao.org/5.x/manual/de/erweiterungen/metamodels/
- https://docs.contao.org/5.x/manual/de/erweiterungen/news-facebook-sync/
