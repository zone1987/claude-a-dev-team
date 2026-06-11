# Shopware 6 – Produktvergleich: Vollständige Dokumentation

> Quelle: https://docs.shopware.com/de/shopware-6-de/Produktvergleich
> Version: 6.4.0.0+

---

## 1. Überblick

Der Verkaufskanal **Produktvergleich** ermöglicht Produktexporte zu Preisportalen und Marktplätzen. Neue Kanäle lassen sich für beliebige Portale (auch individuelle Marktplätze) anlegen.

Das System nutzt:
- Twig-Templates für die Exportstruktur
- Caching oder regelmäßige Neuerstellung für aktuelle Daten
- Dynamische Produktgruppen für die Produktauswahl

---

## 2. Grundeinstellungen

### 2.1 Allgemein

- **Name** des Produktvergleiches vergeben
- **Vorlage** wählen: Vorkonfigurierte Templates für bekannte Preisportale verfügbar → automatische Vorkonfiguration für das jeweilige Portal

### 2.2 Storefront-Verkaufskanal

Folgende Parameter konfigurieren:

| Nr. | Parameter | Beschreibung |
|---|---|---|
| 1 | **Verkaufskanal** | Zugehöriger Storefront-Kanal |
| 2 | **Storefront-Domain** | Domain des Kanals (für URL-Generierung) |
| 3 | **Währung** | Exportwährung |
| 4 | **Sprache** | Exportsprache |
| 5 | **Kundengruppe** | Basis für Preisberechnung |

### 2.3 Produktexport

| Nr. | Parameter | Optionen | Hinweis |
|---|---|---|---|
| 1 | **Dateiname** | Text | Frei wählbar |
| 2 | **Encoding** | UTF-8 / ISO-8859-1 | Beim Preisportal erfragen |
| 3 | **Dateiformat** | CSV / XML | Beim Preisportal erfragen |
| 4 | **Produktvarianten** | Ein/Aus | Ob Varianten separat exportiert werden |
| 5 | **Generierungsintervall** | Zeit in Minuten | Aktualisierungszyklus |
| 6 | **Scheduler** | Checkbox | Erfordert `bin/console scheduled-task:run` |
| 7 | **Dynamische Produktgruppe** | Dropdown | Welche Produkte exportiert werden |

### 2.4 API-Zugang

Im API-Zugang-Bereich:
- API-Zugangs-ID generieren
- **Export-URL** wird angezeigt → direkt in das Preisportal eintragen

**Fehlerbehandlung:** Wenn Export-URL Fehler zurückliefert:
- Dynamische Produktgruppen prüfen
- Bedingungen ergänzen: "Verkaufspreis > 0" und "Preis > 0"

### 2.5 Status

| Option | Wirkung |
|---|---|
| **Deaktivieren** | Produktvergleich temporär deaktivieren |
| **Wartungsmodus** | Zugang nur für IP-Whitelist |

---

## 3. Template

Das Template bestimmt den Aufbau der Exportdatei.

### 3.1 Struktur

| Abschnitt | Verwendung |
|---|---|
| **Kopfzeile** | Einmalig am Anfang (CSV: Spaltenbezeichnungen; XML: öffnende Tags, Header) |
| **Produktzeile** | Wird per Schleife auf jeden Artikel angewendet |
| **Fußzeile** | Nur bei XML: schließende Tags |

**Buttons:**
- **Template testen**: Syntaxüberprüfung
- **Vorschau generieren**: Export-Datei ansehen

**Warnung:** Berechnungen im Template verlangsamen die Generierung.

### 3.2 Twig-Grundlagen

#### If-Abfrage

```twig
{% if product.active %}
  "{{ product.productNumber }}",{#- -#}
{% endif %}
```

#### Elseif und Else

```twig
{% if product.availableStock > 20 %}
  Inhalt 1
{% elseif product.availableStock > 10 %}
  Inhalt 2
{% else %}
  Inhalt 3
{% endif %}
```

#### Set-Befehl (Variablenzuweisung)

```twig
{% set price = product.calculatedPrice %}
"{{ price.unitPrice }}",{#- -#}
```

### 3.3 Variablen-Referenz

#### Konfigurationsvariablen

| Variable | Beschreibung |
|---|---|
| `productExport.salesChannelDomain.url` | URL zum Verkaufskanal |
| `context.salesChannel.name` | Name des Verkaufskanals |

#### Exporteinstellungen-Variablen

| Variable | Beschreibung |
|---|---|
| `productExport.fileName` | Name der Exportdatei |
| `productExport.accessKey` | API-Zugangsschlüssel |
| `productExport.encoding` | Encoding (UTF-8/ISO) |
| `productExport.fileFormat` | Dateiformat (CSV/XML) |
| `productExport.includeVariants` | Ob Varianten exportiert werden |
| `productExport.salesChannel.*` | Daten zum Sales Channel |
| `productExport.salesChannelDomain.*` | Daten zur Domain |

#### Produktvariablen (nur in Produktzeile)

| Variable | Beschreibung |
|---|---|
| `product.active` | Aktiv-Status |
| `product.productNumber` | Produktnummer |
| `product.translated.name` | Produktname |
| `seoUrl('frontend.detail.page', {'productId': product.id})` | SEO-URL des Produkts |
| `product.translated.description` | Produktbeschreibung |
| `product.deliveryTime` | Lieferzeit-Objekt |
| `product.restockTime` | Wiederauffüllzeiten (Tage) |
| `product.minPurchase` | Mindestabnahme |
| `product.maxPurchase` | Maximalabnahme |
| `product.availableStock` | Verfügbarer Lagerbestand |
| `product.stock` | Gesamter Lagerbestand |
| `product.manufacturerNumber` | Herstellernummer |
| `product.ean` | EAN-Code |
| `product.manufacturer.translated.name` | Hersteller |
| `product.cover.media.url` | Hauptbild-URL |
| `product.calculatedPrice.unitPrice` | Einzelpreis (Brutto) |
| `product.calculatedPrice.listPrice.price` | Streichpreis (Brutto) |
| `product.categories.first.getBreadCrumb` | Kategorie-Pfad |
| `product.available` | Verfügbarkeit (Boolean) |
| `product.isCloseout` | Abverkauf (Boolean) |
| `product.shippingFree` | Kostenloser Versand (Boolean) |
| `product.markAsTopseller` | Topseller-Markierung (Boolean) |
| `product.weight` | Gewicht |
| `product.width` | Breite |
| `product.height` | Höhe |
| `product.length` | Länge |
| `product.releaseDate` | Verkaufsstart |
| `product.keywords` | Schlüsselwörter |
| `product.metaDescription` | Meta-Beschreibung |
| `product.metaTitle` | Meta-Titel |
| `product.packUnit` | Verpackungseinheit |
| `product.tax.taxRate` | Mehrwertsteuersatz |

### 3.4 Zusatzfelder in Templates

**Produkt-Zusatzfeld:**

```twig
{{ product.translated.customFields.technischer_name_des_zusatzfeldes }}
```

**Mit Bedingung (Fehler vermeiden wenn Feld nicht gesetzt):**

```twig
{% if product.translated.customFields.technischer_name_des_zusatzfeldes is defined %}
  {{ product.translated.customFields.technischer_name_des_zusatzfeldes }}
{% endif %}
```

**Hersteller-Zusatzfeld:**

```twig
{{ product.manufacturer.translated.customFields.technischer_name_des_zusatzfeldes }}
```

### 3.5 Eigenschaften ausgeben

**Alle Eigenschaften eines Produkts:**

```twig
{% for properties in product.properties %}
  {{ properties.name }}
{% endfor %}
```

**Spezifische Eigenschaftsgruppe (z.B. "Größe"):**

```twig
{% for properties in product.properties %}
  {% if properties.group.name == "Größe" %}
    {{ properties.name }}
  {% endif %}
{% endfor %}
```

### 3.6 Mehrere Bilder ausgeben

```twig
{%- if product.media|length > 1 -%}
  "{%- for mediaAssociation in product.media|slice(0, 5) -%}
    {{ mediaAssociation.media.url }}
    {%- if not loop.last -%},{%- endif -%}
  {%- endfor -%}"
{%- endif -%}{#- -#}
```

---

## 4. Fehlerbehebung

### 4.1 Fehlende Inhalte (z.B. kein Produktbild)

Export bricht ab wenn Produktbilder fehlen. Lösung: Bedingungsprüfung im Template.

**Vorher:**
```twig
<g:image_link>{{ product.cover.media.url }}</g:image_link>
```

**Nachher:**
```twig
<g:image_link>
  {% if product.cover.media.url is defined and product.cover.media.url is not null %}
    {{ product.cover.media.url }}
  {% endif %}
</g:image_link>
```

### 4.2 Produkt keiner gültigen Kategorie zugeordnet

**Fehlermeldung:**
```
Impossible to access an attribute ("getBreadCrumb") on a null variable
```

**Korrektur:**
```twig
<g:product_type>
  {% if product.categories.first.getBreadCrumb is defined and product.categories.first.getBreadCrumb is not null %}
    {{ product.categories.first.getBreadCrumb|slice(1)|join(' > ')|raw|escape }}
  {% endif %}
</g:product_type>
```

### 4.3 Leerzeichen/Whitespace entfernen

Bindestrich in Twig-Tags entfernt Whitespace links/rechts:

```twig
{%- for properties in product.properties -%}
  {%- if properties.group.name == "Markenname" -%}
    {{- properties.name -}}
  {%- endif -%}
{%- endfor -%}
```

---

## 5. Hilfreiche Code-Snippets

Vollständige Code-Snippet-Sammlung für häufige Anforderungen:
https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/gewusst-wie/produktvergleich-code-snippets

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/Produktvergleich
