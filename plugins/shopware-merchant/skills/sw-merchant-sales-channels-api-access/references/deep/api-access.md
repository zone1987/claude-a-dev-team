# Shopware 6 – Verkaufskanal: API-Zugang (vollständig)

> Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
> Version: 6.7.7.0+

---

## 1. API-Zugangs-ID generieren

![API-Zugang](../../sw-merchant-sales-channels/assets/api-zugang.png)

Im Abschnitt **API-Zugang** jedes Verkaufskanals kann ein API-Schlüssel generiert werden.

**Zugang:** Verkaufskanal öffnen > Abschnitt "API-Zugang"

**Aktion:** Button "API-Zugangs-ID generieren" klicken

---

## 2. Funktionsweise

### Was ist der Access Key?

Der API-Zugangsschlüssel (Access Key) authentifiziert Anfragen an die **Sales Channel API** (auch Store API genannt). Er ermöglicht externen Systemen den Zugriff auf kanal-spezifische Daten:

- Produktlisten und Produktdetails
- Kategoriestruktur
- Preise (für Kundengruppe des Kanals)
- Warenkorb-Operationen
- Checkout-Prozess
- Kundenregistrierung und Login

### Verwendung im API-Request

Der Access Key wird im HTTP-Header übergeben:

```http
GET /store-api/product
sw-access-key: SWSCXXXXXXXXXX
```

### Kanal-Kontext

Jeder Access Key ist genau einem Verkaufskanal zugeordnet. Alle API-Anfragen mit diesem Key laufen im Kontext des entsprechenden Kanals:
- Kanalspezifische Preise
- Kanalspezifische Sprachen
- Kanalspezifische Produktzuordnungen

---

## 3. Anwendungsfälle

| Anwendungsfall | Beschreibung |
|---|---|
| **Progressive Web App (PWA)** | Headless Frontend kommuniziert über Store API mit Shopware |
| **Mobile App (iOS/Android)** | Native App nutzt Store API für Shop-Funktionen |
| **Externe Warenwirtschaft** | ERP/WMS-System fragt Bestellungen ab |
| **Produktvergleich-Feed** | Automatischer Export via API |
| **Headless B2B-Portal** | Separater Kanal mit eigenem Access Key für B2B-Kunden |

---

## 4. Sicherheitshinweise

- **Access Key sofort nach Generierung sichern** – er wird nur einmal angezeigt
- Bei Verlust: neuen Key generieren (alter Key wird automatisch ungültig)
- Bei Kompromittierung (öffentlicher Commit, Leak): sofort neuen Key generieren
- Access Key ist kein Admin-API-Schlüssel – er ermöglicht nur Zugriff auf öffentliche Shop-Daten des jeweiligen Kanals

---

## 5. Produktvergleich: Export-URL

Für Produktvergleich-Kanäle wird neben dem Access Key auch eine **Export-URL** angezeigt:

```
https://www.shop.de/sales-channel-api/v3/product-export/{access-key}/{filename}
```

Diese URL kann direkt in Preisportale eingetragen werden für automatischen Feed-Abruf.

**Fehlerbehandlung bei Export:**
- Wenn die Export-URL Fehler liefert: Dynamische Produktgruppen prüfen
- Fehlende Preise: Bedingung "Verkaufspreis > 0" in die Produktgruppe aufnehmen

---

## 6. Weitere Dokumentation

- Developer-Dokumentation Sales Channel API: https://developers.shopware.com/docs/concepts/api/store-api
- API-Zugang für Produktvergleich → Skill `sw-merchant-sales-channels-product-comparison`

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
