# Shopware 6 – Verkaufskanal anlegen: Vollständige Dokumentation

> Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
> Version: 6.7.7.0+

---

## 1. Verkaufskanal anlegen – Einstieg

Das **+** Symbol neben **Verkaufskanäle** im Hauptmenü öffnet den Typ-Auswahl-Dialog.

![Verkaufskanal anlegen Dialog](../../sw-merchant-sales-channels/assets/kanal-hinzufuegen-dialog.png)

---

## 2. Verfügbare Kanal-Typen

### 2.1 Storefront (HTML)

Vollständiger Online-Shop mit:
- Sichtbarem Frontend für Kunden
- Theme-Zuweisung und Theme-Konfiguration
- Navigationsstruktur (Haupt-, Footer- und Service-Navigation)
- Vollständigem Checkout-Prozess
- Google-Analytics-Integration

**Verwendung:** Klassischer B2C/B2B Online-Shop

### 2.2 Headless-Verkaufskanal

- Keine eigene Storefront / kein Frontend
- Reine API-Schnittstelle (Store API / Sales Channel API)
- Wird von Shopware vorinstalliert (Default-Headless-Kanal)

**WICHTIG:** Der vorinstallierte Headless-Kanal darf niemals gelöscht werden. Zahlreiche Erweiterungen (z.B. B2B-Suite, Apps) nutzen diesen Kanal intern. Statt Löschen: andere Kanäle als Favoriten markieren, sodass der Headless-Kanal aus der Sidebar ausgeblendet wird.

**Verwendung:** Mobile Apps, PWA, externe Systeme via API

### 2.3 Produktvergleich

- Generiert Export-Feeds (XML oder CSV) für Preisportale und Marktplätze
- Template-basiert mit Twig-Syntax
- Konfigurierbare Generierungsintervalle (live oder geplant)
- Unterstützung für Twig-Variablen (Produkt, Preise, SEO-URLs etc.)

**Verwendung:** billiger.de, Idealo, Google Shopping, eigene Marktplätze

### 2.4 Social Shopping (ab Shopware Rise)

Vier Plattformen werden unterstützt:
- **Facebook** – XML-Feed + Tracking per Referral-Code
- **Instagram** – XML-Feed (identisch zu Facebook)
- **Google Shopping** – XML-Feed + Domain-Verifizierung erforderlich
- **Pinterest** – Kein Feed; nutzt Meta-Daten (Rich Pins)

**Voraussetzung:** Shopware Rise (oder höher) Plan

### 2.5 Agentic Commerce Product Feed (ab 6.7.10.0)

- JSONL-Feed für KI-Plattformen (z.B. ChatGPT Marketplace)
- OpenAI-Template vorkonfiguriert
- Affiliate- und Kampagnen-Code für Tracking
- **Hinweis:** ChatGPT Marketplace-Registrierung aktuell nur in den USA verfügbar

---

## 3. Grundkonfiguration nach Anlage

Nach Wahl des Typs öffnet sich der Konfigurationsbereich. Pflichtkonfiguration:

1. **Name** (intern, für Admin-Sidebar)
2. **Sprache(n)** und Standard-Sprache
3. **Währung(en)** und Standard-Währung
4. **Domain(s)** hinterlegen

Weitere Details → Skill `sw-merchant-sales-channels-config`

---

## 5. Kanal löschen

- Löschen ist **unwiderruflich**
- Headless-Kanal: **niemals löschen**
- Alternative: Als Nicht-Favorit markieren → wird aus Sidebar ausgeblendet

![Verkaufskanal löschen Button](../../sw-merchant-sales-channels/assets/loeschen.png)

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
