# Shopware 6 – Social Shopping: Vollständige Dokumentation

> Quelle: https://docs.shopware.com/de/shopware-6-de/erweiterungen/social-shopping
> Version: 3.1.0+

---

## 1. Überblick

Social Shopping ermöglicht die Anbindung von Social-Media-Plattformen als Verkaufskanäle via XML-Feed-Export. Die Extension ist **Bestandteil ab dem Plan Shopware Rise**.

**Installation:**
- Erweiterungen > Meine Erweiterungen
- Extension herunterladen (verfügbar wenn Rise-Plan für Domain registriert ist)

**Wichtig:** Vor Deaktivierung des Social-Shopping-Plugins müssen alle Social-Shopping-Kanäle gelöscht werden.

**Admin-Spalten:**
In den Admin-Bereichen Kunden und Bestellungen wird eine "Einstieg"-Spalte hinzugefügt, um die Quelle (welcher Social-Shopping-Kanal) zu zeigen.

---

## 2. Facebook

### 2.1 Konfiguration – Allgemein

| Nr. | Feld | Beschreibung |
|---|---|---|
| 1 | **Sprachauswahl** | Konfiguration pro Sprache; Hauptsprache wird vererbt |
| 7 | **Name** | Bezeichnung des Kanals |
| 8 | **Aktiv** | Feed-Generierung aktivieren/deaktivieren |
| 9 | **Storefront Verkaufskanal** | Auswahl der zugehörigen Storefront |
| 10 | **Storefront Verkaufskanal-Domain** | Domain-Auswahl bei mehreren Domains |
| 11 | **Währung** | Produktdarstellung in dieser Währung |
| 12 | **Dynamische Produktgruppe** | Welche Produkte in den Feed aufgenommen werden |

### 2.2 Weitere Einstellungen

| Nr. | Feld | Beschreibung |
|---|---|---|
| 1 | **Varianten als eigene Produkte importieren** | Einzelne Varianten oder als Sammelprodukt exportieren |
| 2 | **Generierungsintervall** | "Live" = Echtzeitgenerierung; oder geplanter Zeitpunkt |
| 3 | **Per Scheduler generieren** | Automatisierung via Message Queue |
| 4 | **Standard Google-Produktkategorie-ID** | Numerische Kategorie-ID (von Google definiert) |
| 5 | **Zeitpunkt der letzten Generierung** | Letzter Aktualisierungsstempel |

### 2.3 Statistiken

Zeigt Metriken zu:
- Bestellungen (aus diesem Kanal)
- Kunden (Neuregistrierungen)
- Umsatz

Mit Zeitraum-Filter (z.B. letzte 24 Stunden, letzte 7 Tage).

**Voraussetzung:** Ohne die Referral-Code-Variable im Template können Statistiken nicht berechnet werden.

### 2.4 Unveröffentlichte Produkte validieren

- **Produkte validieren** Button: Prüft alle Feed-Produkte auf Gültigkeit
- **Ergebnis der Validierung**: Listet ungültige Produkte mit konkreten Fehlermeldungen

### 2.5 Integration

**Export-URL:** Diese URL trägt man in Facebook ein für den automatischen Feed-Abruf.

### 2.6 Template

Das Template steuert den Aufbau der XML-Exportdatei:
- **Kopfzeile** (einmalig, XML-Header)
- **Produktzeile** (pro Produkt, in Schleife)
- **Fußzeile** (XML-Abschluss)

**Funktionen:**
- **Template testen** (1): Syntaxprüfung
- **Vorschau generieren** (2): Export-Datei ansehen
- **Variablen** (3): Verfügbare Datenfelder mit Kopier-Funktion

**Referral-Code für Statistiken:**

```twig
{{ socialShoppingSalesChannel.salesChannelId }}
```

Vollständiger Tracking-Link im Template:

```twig
<g:link>{{ seoUrl('frontend.detail.page', {'productId': product.id}) }}?referralCode={{ socialShoppingSalesChannel.salesChannelId }}</g:link>
```

---

## 3. Instagram

### 3.1 Konfiguration

Identische Konfigurationsstruktur wie Facebook:
- Name, Aktiv, Storefront-Kanal, Domain, Währung, Produktgruppe
- Varianten-Handling, Generierungsintervall, Scheduler
- Google-Produktkategorie-ID, Generierungsstempel

### 3.2 Template-Referral-Code

```twig
{{ socialShoppingSalesChannel.salesChannelId }}
```

SEO-URL-Integration:

```twig
<g:link>{{ seoUrl('frontend.detail.page', {'productId': product.id}) }}?referralCode={{ socialShoppingSalesChannel.salesChannelId }}</g:link>
```

---

## 4. Google Shopping

### 4.1 Besonderheit: Domain-Verifizierung

Google Shopping erfordert eine Domain-Verifizierung via HTML-Tag im `public`-Verzeichnis des Shopware-Projekts.

### 4.2 Konfiguration

Gleiche Grundeinstellungen wie Facebook/Instagram mit XML-Feed für Google Shopping.

### 4.3 Tracking-Link für Statistiken

```twig
<link>{{ seoUrl('frontend.detail.page', {'productId': product.id}) }}?referralCode={{ socialShoppingSalesChannel.salesChannelId }}</link>
```

---

## 5. Pinterest

### 5.1 Unterschied zu anderen Plattformen

Pinterest arbeitet **nicht mit Export-Feeds**, sondern nutzt Meta-Daten (Rich Pins), über die Pinterest die benötigten Informationen direkt von den Produktseiten abruft.

### 5.2 Konfiguration

| Nr. | Feld | Beschreibung |
|---|---|---|
| 5 | **Name** | Kanalbezeichnung |
| 6 | **Aktiv** | Aktivierungsschalter |
| 7 | **Storefront Verkaufskanal** | Zugehörige Storefront |
| 8 | **Storefront Verkaufskanal-Domain** | Domain-Auswahl |
| 9 | **Währung** | Währungseinstellung |

### 5.3 Validierung

Im Tab Integration: Button öffnet Pinterest Rich Pins Validator zur Überprüfung der korrekten Meta-Daten-Implementierung.

---

## 6. Templates anpassen

Alle Feed-Templates (außer Pinterest) basieren auf **Twig**-Syntax und können individuell angepasst werden.

Standardtemplates werden mit Shopware ausgeliefert.

**Community-Ressourcen:**
- Code-Snippets für häufige Erweiterungen: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/gewusst-wie/produktvergleich-code-snippets
- Interaktiver Lernpfad: https://hub.shopware.com/learn/unit/user-sales-channels

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/erweiterungen/social-shopping
