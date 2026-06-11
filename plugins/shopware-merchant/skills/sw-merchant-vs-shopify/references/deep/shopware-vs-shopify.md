# Shopware vs. Shopify – Vollständiger Plattformvergleich

## 1. Architektur & Hosting

### Shopware
- **Open Source** (Community Edition kostenfrei, kommerziell: Rise, Evolve, Beyond)
- Deployment-Optionen: Self-hosted (eigener Server), PaaS (z. B. Platform.sh, Uberspace), Shopware PaaS, Shopware SaaS
- Vollständige Kontrolle über Serverstandort (AWS, Google Cloud, Azure oder On-Premise)
- API-first-Architektur: REST- und GraphQL-Storefront-API, Admin-API
- Headless-Betrieb nativ unterstützt (entkoppeltes Frontend möglich)

### Shopify
- Reines SaaS-Modell – kein eigenes Hosting möglich
- Datenspeicherung ausschließlich in Shopify-eigener Cloud-Infrastruktur
- Serverstandort nicht selbst wählbar (relevant für DSGVO)
- Headless über Storefront API möglich, aber eingeschränkter als Shopware
- Liquid-Templating als Standard-Customization-Ebene

**Fazit Architektur:** Shopware gibt deutlich mehr Kontrolle über Infrastruktur, Datenhaltung und technischen Stack. Shopify punktet mit sofortiger Betriebsbereitschaft ohne DevOps-Aufwand.

---

## 2. Kostenmodell & TCO (Total Cost of Ownership)

### Shopware

| Edition | Lizenzkosten | Zielgruppe |
|---|---|---|
| Community Edition | Kostenlos | Technisch versierte KMU, Agenturen |
| Rise | GMV-basiert | Wachsende Shops |
| Evolve | GMV-basiert | Mid-Market |
| Beyond | GMV-basiert | Enterprise |

- **Keine Transaktionsgebühren** auf Umsätze bei Drittanbieter-Zahlungsmethoden
- Hostingkosten trägt der Betreiber selbst (Vorteil: Flexibilität; Nachteil: Verantwortung)
- Erweiterungen: teils kostenfrei (Community), teils kostenpflichtig

### Shopify

| Plan | Monatspreis (ca.) | Transaktionsgebühren (ext. Zahler) |
|---|---|---|
| Basic | ab 29 €/Monat | 2,0 % |
| Shopify | ab 79 €/Monat | 1,0 % |
| Advanced | ab 299 €/Monat | 0,5 % |
| Plus | ab 2.300 €/Monat | 0,15 % |

- Transaktionsgebühren entfallen nur bei Nutzung von Shopify Payments (nicht in DE verfügbar)
- Viele essenzielle Funktionen nur über kostenpflichtige Apps realisierbar

**Fazit Kosten:** Bei hohem GMV ist Shopware durch fehlende Transaktionsgebühren deutlich günstiger. Shopify hat niedrige Einstiegshürde, aber steigende Fixkosten und versteckte App-Kosten.

---

## 3. Anpassbarkeit & Erweiterungen

### Shopware
- Vollständiger Quellcodezugriff (PHP/Symfony-Stack)
- Plugin-System mit 3.100+ Erweiterungen im Shopware Store
- Rule Builder: regelbasierte Automatisierungen ohne Code
- Flow Builder: Event-getriggerte Workflows (kommerziell)
- Theme-System: Twig + SCSS, vollständig anpassbar
- Custom Fields, Custom Entities, Extension SDK für Apps

### Shopify
- Liquid-Templating für Theme-Anpassungen
- App Store mit ~8.000+ Apps (viele kostenpflichtig)
- Metafields für zusätzliche Datenpunkte
- Shopify Functions für einfache Backend-Logiken
- Strukturvorgaben durch Shopify-Plattform schwer zu umgehen

**Fazit Anpassbarkeit:** Shopware ermöglicht tiefgreifende technische Anpassungen ohne Limitierungen durch die Plattform. Shopify ist schneller startklar, stößt aber bei komplexen Anforderungen schnell an Grenzen.

---

## 4. B2B-Funktionalität

### Shopware (nativ)
- Kundengruppen und individuelle Preislisten
- Angebotswesen (kommerziell)
- Bestelllisten / Schnellbestellung
- Digital Sales Rooms für kollaborativen B2B-Verkauf (kommerziell)
- Custom Pricing (kommerziell)
- Netto-Preisdarstellung pro Kundengruppe
- B2B-Komponenten: Freigabe-Workflows, Mitarbeiterverwaltung pro Unternehmen

### Shopify
- B2B-Features seit Shopify Plus (teuerster Plan)
- Separate B2B-Storefront nur über Plus verfügbar
- Individuelle Preislisten: Über Apps oder Plus-Feature
- Kein natives Angebotswesen

**Fazit B2B:** Shopware hat klar die Nase vorn. B2B-Funktionen sind tief integriert und ab kommerziellen Tarifen verfügbar. Shopify benötigt für gleichwertige B2B-Funktionalität den teuren Plus-Plan oder externe Apps.

---

## 5. Internationalisierung & Omnichannel

### Shopware
- Beliebig viele Sales Channels (unterschiedliche Sprachen, Währungen, Preislisten)
- Mehrsprachigkeit nativ im Core
- POS-Integration via API
- Marktplatz-Anbindung (Amazon, eBay) über Extensions
- Omnichannel-Strategie nativ unterstützt

### Shopify
- Shopify Markets für mehrere Märkte (Sprache + Währung)
- Maximale Flexibilität durch App-Ökosystem
- POS (Shopify POS) als eigenständiges Produkt
- Marktplatz-Anbindung über Apps

**Fazit Internationalisierung:** Shopware bietet mehr native Flexibilität. Shopify Markets ist solide, aber weniger konfigurierbar für komplexe Multi-Market-Setups.

---

## 6. API-first & Headless

### Shopware
- Storefront API (GraphQL) für Headless-Setups
- Admin API (REST) für Backend-Integration
- Composable-Commerce-Ansatz: Frontend vollständig entkoppelbar
- Native Integration in Vue.js Frontends (Shopware Frontends)
- Event-System für reaktive Architekturen

### Shopify
- Storefront API (GraphQL) vorhanden
- Hydrogen-Framework (React-basiert) für Headless
- Sinnvoller Headless-Einstieg, aber stärker an Shopify-Ökosystem gebunden

**Fazit Headless:** Beide Plattformen unterstützen Headless, Shopware mit offenerem Ökosystem. Shopify mit Hydrogen liefert einen fertigen React-Stack.

---

## 7. SEO & Performance

### Shopware
- Volle Kontrolle über URL-Struktur, Canonical-Tags, Sitemap
- Server-seitiges Rendering (SSR) im Standard-Storefront
- HTTP-Cache, Redis, Varnish-Unterstützung konfigurierbar
- Performance abhängig von Hosting-Konfiguration (Chance und Risiko)
- SEO-Grundlagen: Meta-Tags, Breadcrumbs, strukturierte Daten via Extensions

### Shopify
- SEO-Grundfunktionen im Core vorhanden
- Automatisches CDN und Bildoptimierung durch Shopify-Infrastruktur
- Sehr stabile Performance durch Shopify-Hosting
- Eingeschränkte Kontrolle über technische SEO-Parameter (z. B. URL-Struktur festgelegt)

**Fazit SEO/Performance:** Shopify liefert out-of-the-box stabiles Hosting und CDN. Shopware ermöglicht bei richtiger Konfiguration überlegene Performance, erfordert aber technisches Know-how.

---

## 8. Datenschutz & DSGVO

### Shopware
- Serverstandort vollständig selbst wählbar (EU-Hosting problemlos)
- Keine erzwungene Datenübertragung an Dritte
- DSGVO-Anforderungen technisch leichter vollständig erfüllbar
- Shopware GmbH mit Sitz in Schöppingen (Deutschland)

### Shopify
- Datenspeicherung in Shopify-Cloud (USA/Kanada)
- Standardmäßig Drittland-Datentransfer
- DSGVO-Compliance nur eingeschränkt selbst steuerbar
- Data Processing Agreement mit Shopify möglich, aber keine EU-Only-Option

**Fazit DSGVO:** Für datensensibler aufgestellte Unternehmen und öffentliche Auftraggeber ist Shopware klar vorzuziehen.

---

## 9. Support & Community

### Shopware
- Offizielle Dokumentation (docs.shopware.com)
- Community Forum + Slack
- Shopware-Partner-Netzwerk: 1.600+ Partner weltweit
- Direkter Hersteller-Support (kommerziell)
- Gartner Magic Quadrant 2025: Visionary-Status

### Shopify
- Umfangreiche Dokumentation und Hilfe-Center
- 24/7-Support (Chat/E-Mail)
- Sehr große Community und App-Ökosystem
- Shopify Experts Marketplace für Agenturen

**Fazit Support:** Shopify punktet mit 24/7-Sofort-Support. Shopware hat starkes deutschsprachiges Partner-Netzwerk und besseren Enterprise-Support.

---

## 10. Zielgruppen

| Zielgruppe | Empfehlung |
|---|---|
| Schneller Einstieg, wenig Technik | Shopify |
| DSGVO-sensibler Betrieb, EU-Hosting | Shopware |
| B2B-Handel | Shopware |
| Enterprise mit komplexen Anforderungen | Shopware |
| Internationaler Multi-Market-Betrieb | Shopware (mehr Flexibilität) |
| Kleiner B2C-Shop, Einsteiger | Shopify |
| Headless-Commerce-Projekt | Beide (je nach Stack-Präferenz) |
| DACH-Markt mit Fokus auf Anpassbarkeit | Shopware |

---

## 11. Migrationspfad Shopify → Shopware

### Offizielle Ressource
Shopware stellt unter `/de/migration/zu-shopware/` Informationen zur Migration bereit.

### Typischer Migrationsprozess

1. **Analyse & Vorbereitung**
   - Produktkatalog exportieren (CSV/API)
   - Kundendaten und Bestellhistorie sichern
   - Erweiterungen/Apps auf Shopware-Äquivalente prüfen
   - Theme/Design: Neuumsetzung erforderlich (kein Liquid → Twig)

2. **Datenmigration**
   - Shopware Migration Assistant (Plugin) für automatisierten Import
   - Produkte, Kategorien, Kunden, Bestellungen, Medien
   - URL-Weiterleitungen planen (SEO-Schutz)

3. **Technische Einrichtung**
   - Hosting aufsetzen (Self-hosted oder PaaS)
   - Shopware installieren und konfigurieren
   - Zahlungsanbieter integrieren (kein Transaktionsgebühren-Lock-in)
   - Sales Channels und Sprachen anlegen

4. **Theme & Frontend**
   - Shopware Storefront (Twig) oder Headless-Lösung
   - Kein direktes Liquid-zu-Twig-Konverter vorhanden
   - Shopware-zertifizierte Agenturen empfehlenswert

5. **Go-Live**
   - DNS-Umstellung
   - 301-Weiterleitungen aktiv
   - SEO-Monitoring nach Launch

### Herausforderungen der Migration
- Theme muss neu entwickelt werden (kein 1:1-Export)
- App-Äquivalente prüfen (nicht alle Shopify-Apps haben Shopware-Pendants)
- Initiale Hosting-Infrastruktur muss aufgebaut werden
- Technisches Know-how oder Agentur-Support empfohlen

### Vorteile nach Migration
- Keine monatlichen Fixkosten und Transaktionsgebühren ab bestimmtem GMV
- Vollständige Datenkontrolle und EU-Hosting
- Native B2B-Funktionen ohne Aufpreis (ab kommerziellem Tarif)
- Unbegrenzte Anpassungsmöglichkeiten am Quellcode

---

## Kennzahlen Shopware (Stand 2025)

- 25 Mrd. € Plattform-GMV
- 3.100+ Erweiterungen im Store
- 1.600+ Partner weltweit
- Gartner Magic Quadrant 2025: Visionary

---

## Quellen

- Shopware-Vergleichsseite: https://www.shopware.com/de/shopware-vs-shopify/ (abgerufen 2026-06-11)
- Allgemeines Plattformwissen: Shopware-Dokumentation, Shopify-Pricing-Seite, öffentliche Gartner-Reports
