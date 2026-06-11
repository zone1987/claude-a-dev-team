---
name: sw-merchant-sales-channels-product-comparison
description: >
  Shopware Produktvergleich Verkaufskanal, Preisportal Feed, Produktexport XML CSV,
  Twig Template Produktexport, Produktfeed Google Shopping Idealo billiger.de,
  Vergleichsportal anbinden, Export-URL Produktvergleich, Produktvariablen Template,
  Produktexport Scheduler, Produktexport Fehlerbehebung
---

# Shopware 6 – Produktvergleich (Export-Feeds)

XML/CSV-Feeds für Preisportale und Marktplätze konfigurieren.

## Kernfunktionen

- Vorkonfigurierte Templates für bekannte Portale
- Eigene Templates mit Twig möglich
- Scheduler für automatische Neuberechnung
- Dynamische Produktgruppen für Produktauswahl
- Variablen für alle Produktdaten, Preise, SEO-URLs

## Template-Typen

| Abschnitt | Beschreibung |
|---|---|
| **Kopfzeile** | XML/CSV-Header (einmalig) |
| **Produktzeile** | Twig-Schleife pro Produkt |
| **Fußzeile** | XML-Abschluss (nur XML) |

## Häufige Twig-Variablen

- `product.translated.name` – Produktname
- `product.calculatedPrice.unitPrice` – Preis
- `product.cover.media.url` – Produktbild
- `seoUrl('frontend.detail.page', {'productId': product.id})` – URL

## Quelle

https://docs.shopware.com/de/shopware-6-de/Produktvergleich
