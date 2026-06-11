# Shopware 6 – SEO-Einstellungen & Sitemap (vollständige Referenz)

Quellen:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/seo
- https://docs.shopware.com/de/shopware-6-de/einstellungen/sitemap

---

## SEO-URL-Templates

**Pfad:** Einstellungen > Shop > SEO-Einstellungen

### Verkaufskanal-Auswahl
Konfigurationen können global für alle Kanäle oder kanalspezifisch erfolgen.

---

### Produktdetailseite
Twig-Syntax für URL-Templates: `{{ product.name }}`

**Verfügbare Variablen:**
| Variable | Bedeutung |
|---|---|
| `{{ product.productNumber }}` | Bestellnummer |
| `{{ product.name }}` | Produktname |
| `{{ product.ean }}` | EAN-Code |
| `{{ product.manufacturer.name }}` | Herstellername |
| `{% for part in product.categories.sortByPosition().first.breadcrumb %}` | Kategorie-Breadcrumb |

**Besonderheiten:**
- Mehrstufige Variablen erfordern manuelle Vervollständigung
- Längenbeschränkung: `{{ product.translated.name[:50] }}`
- Bedingte Logik: IF-Abfragen möglich
- Validierungsindikator: Grünes Häkchen = korrekt, Rotes X = Fehler

**Twig-Filter (Pipe-Operator):**
```twig
{{ product.translated.name|lower }}
```

---

### Landingpage
| Variable | Bedeutung |
|---|---|
| `{{landingPage.name}}` | Name der Landingpage |
| `{{landingPage.metaTitle}}` | Meta-Titel |
| `{{landingPage.url}}` | URL |
| `{{landingPage.active}}` | Aktivstatus |

> Voraussetzung: Mindestens eine Landingpage muss vorhanden sein.

---

### Kategorieseite
| Variable | Bedeutung |
|---|---|
| `{{ category.seoBreadcrumb }}` | Breadcrumb-Pfad |
| `{{ category.translated.name }}` | Übersetzter Kategoriename |
| `{{ category.translated.metaTitle }}` | Übersetzter Meta-Titel |
| `{{ category.parentId }}` | Übergeordnete Kategorie |

**Beispiel mit Filter:**
```twig
{% for part in category.seoBreadcrumb %}{{ part|lower }}{% endfor %}
```

---

## Weiterleitung (HTTP 301)

Option: Automatische Weiterleitungen bei URL-Änderungen aktivieren (statt nur Canonical Links).

---

## SEO-Index neu aufbauen

Nach Template-Änderungen ist ein Neuaufbau erforderlich:
```bash
php bin/console dal:refresh:index
```

---

## Kanonische URLs

- Kennzeichnen die bevorzugte Seite bei duplizierten Inhalten für Suchmaschinen
- Können unterschiedliche Domains verwenden
- Kleinere Variationen (Sortierung, Filter) werden ignoriert

---

## Sitemap

**Pfad:** Einstellungen > Shop > Sitemap  
**Verfügbar ab:** 6.1.0

### Grundprinzip
Shopware erstellt eine maschinell lesbare `sitemap.xml` für Suchmaschinen.  
Abrufbar unter: `https://mydomain.com/sitemap.xml`

Die Datei wird bei großen Shops automatisch aufgeteilt (Index + Teilsitemaps).

### Konfigurierbare Optionen
- Refresh-Time für die Sitemap
- Refresh-Strategie

### Drei Refresh-Strategien

| Strategie | Beschreibung |
|---|---|
| **Geplant** | Automatische Generierung per Scheduled Task |
| **Live** | Neue Sitemap bei fehlendem oder abgelaufenem Cache |
| **Manuell** | Automatisch deaktiviert; manuelle Generierung per CLI |

**Manueller Befehl:**
```bash
php bin/console sitemap:generate
```
> Muss nach jeder URL-Änderung erneut ausgeführt werden.

### Hinweise
- Shopware kann nicht garantieren, dass jede URL indiziert wird
- Für Custom-URLs: Developer-Dokumentation consulten
