# Shopware 6 – Caches & Indizes (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/caches-indizes

---

## Überblick

**Pfad:** Einstellungen > System > Caches & Indizes  
**Nur für Self-Hosted** (nicht für SaaS-Umgebungen)  
**Verfügbar ab:** 6.2.0

---

## Konfigurationsübersicht (Dashboard)

Das Dashboard zeigt drei Hauptinformationen:

| Information | Beschreibung |
|---|---|
| Umgebung | Zeigt ob der Shop im „Production"-Modus läuft |
| HTTP-Cache | Status der HTTP-Cache-Aktivierung |
| Cache-Adapter | Welcher Adapter verwendet wird |

### Konfiguration via .env
```env
# HTTP-Cache aktivieren (1) oder deaktivieren (0)
SHOPWARE_HTTP_CACHE_ENABLED=1
```

---

## Admin-Aktionen

### Cache aktualisieren
Löscht zwischengespeicherte Daten für kürzlich geänderte Inhalte (z.B. Theme-, Produktanpassungen).

### Cache löschen
Entfernt den **gesamten Cache** ohne anschließendes Aufwärmen.
```bash
php bin/console cache:clear
```

### Indizes aktualisieren
Aktualisiert Kategorie-, Produkt- und SEO-URL-Indizes:
```bash
php bin/console dal:refresh:index
```

---

## Indexer-Übersicht

| Indexer | Funktion |
|---|---|
| `category.indexer` | Kategorieindex mit Subkategorien, Baum, Breadcrumb, SEO-URLs |
| `customer.indexer` | Suchindex für Kundeneinträge |
| `landing_page.indexer` | Index für Landingpages mit SEO-URLs |
| `media.indexer` | Mediendateien und -ordner mit Vererbung |
| `payment_method.indexer` | Zahlungsarten-Index |
| `product.indexer` | Umfassender Produktindex: Vererbung, Lagerbestand, Varianten, Kategoriezuweisungen, Preise, Bewertungen, Streams, SEO-URLs |
| `product_stream.indexer` | Dynamische Produktgruppen |
| `promotion.indexer` | Rabatte & Aktionen mit Ausschlüssen und Verwendung |
| `rule.indexer` | Rule-Builder-Regeln und Bedingungen |
| `sales_channel.indexer` | Verkaufskanäle |
| `flow.indexer` | Workflow-Flows |
| `newsletter_recipient.indexer` | Newsletter-Empfänger |

### Selektive Indexaktualisierung
- Indexer aus Dropdown auswählen
- Methode: „Nur Auswahl aktualisieren" oder „Alle außer Auswahl"

---

## Cache automatisiert leeren

Shopware 6 leert den Cache **nicht automatisch**. Empfehlung:

```bash
php bin/console cache:clear
php bin/console cache:warmup
```

**Best Practice:** Via Cronjob täglich während geringen Traffics (z.B. nachts) ausführen.

---

## Manuelle Cache-Löschung (Fallback)

Falls CLI-Befehl fehlschlägt:
```bash
rm -rf /path/to/shopware/var/cache/*
```

---

## Hintergrundwissen

| Begriff | Bedeutung |
|---|---|
| **Cache** | Beschleunigt Anfragen durch gespeicherte Daten |
| **Index** | Listen von Daten im Textformat für schnelle Suchalgorithmen |
