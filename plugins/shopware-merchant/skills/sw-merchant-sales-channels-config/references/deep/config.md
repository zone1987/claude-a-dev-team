# Shopware 6 – Verkaufskanal: Konfiguration (vollständig)

> Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
> Version: 6.7.7.0+

---

## 1. Grundeinstellungen

![Grundeinstellungen Übersicht](../../sw-merchant-sales-channels/assets/grundeinstellungen.png)

| Nr. | Feld | Funktion |
|---|---|---|
| 1 | **Name** | Interner Name des Verkaufskanals (erscheint in Admin-Sidebar) |
| 2 | **Als Favorit markieren** | Kanal in der Admin-Sidebar anzeigen |
| 3 | **Einstiegspunkt Haupt-Navigation** | Startkategorie für Hauptmenü; Kategorien eine Ebene darunter werden als Hauptnavigation angezeigt |
| 4 | **Hauptnavigations-Ebenen** | Anzahl der sichtbaren Navigationsebenen unterhalb der Startebene |
| 5 | **Einstiegspunkt Footer-Navigation** | Startkategorie für Footer; Ebene darunter = Überschriften, nächste Ebene = anklickbare Links |
| 6 | **Einstiegspunkt Footer-Service-Navigation** | Kategorie für Service-Navigation (standardmäßig unten rechts) |
| 7 | **Kundengruppe** | Standard-Kundengruppe für neue und nicht eingeloggte Besucher |
| 8 | **Länder** | Verfügbare Lieferländer + Standard-Land |
| 9 | **Sprachen** | Verfügbare Sprachen + Standard-Sprache |
| 10 | **Standard-Maßeinheiten** | Einheitensystem, Längen- und Gewichtseinheit |

---

## 2. Zahlung und Versand

![Zahlung und Versand](../../sw-merchant-sales-channels/assets/zahlung-versand.png)

| Nr. | Feld | Konfiguriert unter |
|---|---|---|
| 1 | **Zahlungsarten** | Einstellungen > Zahlungsarten; eine Standard-Zahlungsart erforderlich |
| 2 | **Versandarten** | Einstellungen > Versand; eine Standard-Versandart erforderlich |
| 3 | **Währungen** | Einstellungen > Währungen; Standard-Währung erforderlich |
| 4 | **Steuerberechnung** | Methode der Steuerberechnung festlegen |

---

## 3. Hreflang

Das Hreflang-Metatag ist relevant, wenn es mehrere Sprachversionen des Shops gibt. Es ordnet Inhalte eindeutig Sprachen zu und verhindert, dass Google mehrsprachige Versionen als Duplicate Content einstuft.

![Hreflang Einstellung](../../sw-merchant-sales-channels/assets/hreflang.png)

**Aktivierung:**
- Nach Aktivierung werden alle konfigurierten Domains im Dropdown angezeigt
- Die Standard-Domain dient als Fallback für alle Sprachen

---

## 4. Status und Wartungsmodus

![Status Einstellung](../../sw-merchant-sales-channels/assets/status.png)

| Option | Wirkung |
|---|---|
| **Kanal deaktivieren** | Kanal vorübergehend für Besucher und API nicht erreichbar |
| **Wartungsmodus** | Frontend zeigt nur Wartungsseiten-Layout |
| **IP-Whitelist** | Bestimmte IP-Adressen erhalten Zugriff trotz Wartungsmodus |

**Proxy-Server Hinweis:**
Bei Betrieb hinter einem Proxy muss dessen IP als "Trusted Proxy" eingetragen werden:

```env
TRUSTED_PROXIES=IP_des_Proxys
```

Alternativ via PHP-Einstellungen gemäß Symfony-Dokumentation:
https://symfony.com/doc/current/deployment/proxies.html#solution-settrustedproxies

---

## 5. Theme-Zuweisung (Reiter "Theme")

![Theme-Reiter](../../sw-merchant-sales-channels/assets/theme-reiter.png)

- Zeigt das aktuell zugeordnete Theme mit Vorschaubild
- Klick auf Vorschau oder "Theme ändern" → Auswahl installierter Themes
- "Themes bearbeiten" → weiterleitung zur Theme-Konfiguration

**Hinweis:** Theme-Zuweisung nur bei Storefront-Kanälen (HTML) verfügbar.

---

## 6. Analyse – Google Analytics (Reiter "Analyse")

![Analyse Konfiguration](../../sw-merchant-sales-channels/assets/analyse-konfiguration.png)

### Konfigurationsfelder

| Nr. | Feld | Beschreibung |
|---|---|---|
| 1 | **Tracking-ID** | Aus Google Analytics: Verwaltung > Tracking-Informationen > Tracking-Code |
| 2 | **Google Analytics aktivieren** | Aktivierungsschalter für den Tracking-Code |
| 3 | **Bestellungen verfolgen** | Kaufabschlüsse in Analysen berücksichtigen |
| 4 | **IP-Anonymisierung** | Letzte zwei Zifferngruppen der Kunden-IP werden genullt (z.B. 94.31.0.0). In der EU gesetzlich empfohlen. |
| 5 | **Offcanvas-Warenkorb tracken** | `view_cart`-Event auch beim Öffnen des Offcanvas-Warenkorbs auslösen (nicht nur auf Warenkorbseite). Erhöht Warenkorb-Ansichten in Berichten. |

### Standard-Events

- add-to-cart.event.js
- add-to-cart-by-number.event.js
- begin-checkout.event.js
- begin-checkout-on-cart.event.js
- checkout-progress.event.js
- login.event.js
- purchase.event.js
- remove-from-cart.event.js
- search-ajax.event.js
- sign-up.event.js
- view-item.event.js
- view-item-list.event.js
- view-search-results.js

### Google Tag Manager

Analytics wird via Google Tag Manager implementiert. Benutzerdefinierte Events oder Skripte sind nicht direkt möglich – erfordern Erweiterungen aus dem Shopware Store.

### Erweiterte E-Commerce-Daten (gtag.js)

- Impressionsdaten
- Produktdaten
- Angebotsdaten
- Aktionsdaten

Referenz: https://developers.google.com/analytics/devguides/collection/ga4/validate-ecommerce?hl=de

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
