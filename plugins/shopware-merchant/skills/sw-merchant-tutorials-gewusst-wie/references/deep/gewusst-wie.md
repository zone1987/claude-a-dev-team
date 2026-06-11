# Shopware 6 — Tutorials: Gewusst-wie (vollständige Referenz)

---

## 1. Änderungen am Template vornehmen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/aenderungen-am-template-vornehmen

> Anpassungen am Theme sollten niemals direkt im Standard-Theme erfolgen, sondern immer in einem abgeleiteten Theme.

**Theme erstellen:**
```bash
php bin/console theme:create
```

**Datei ableiten:**
```twig
{% sw_extends '@Storefront/storefront/ordner1/ordner2/datei.html.twig' %}
```
Ableitungspfad: `/custom/plugins/DeinTheme/src/Resources/views/storefront/`

**Nützliche Twig-Funktionen:**

| Funktion | Verwendung |
|----------|-----------|
| `{{ dump() }}` | Alle verfügbaren Variablen anzeigen |
| `{% block name_des_blocks %}` | Block einbinden |
| `{{ parent() }}` | Elternblock-Inhalt übernehmen |
| `{{ 'TextbausteinName'\|trans }}` | Textbaustein einbinden |

**Zusatzfelder in der Storefront ausgeben:**
- Kategorien: `{{ page.footer.navigation.active.translated.customFields.name }}`
- Produkte: `{{ page.product.translated.customFields.name }}`
- Kunden: `{{ context.customer.customFields.name }}`

**Dokumenten-Templates:**
- Basisdatei: `/vendor/shopware/core/Framework/Resources/views/documents/base.html.twig`
- Ableitungspfad: `/custom/plugins/DeinTheme/src/Resources/views/documents/`

**Cache leeren:** `php bin/console cache:clear` oder Admin-Interface

---

## 2. Eigenes Formular anlegen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/eigene-formulare-anlegen  
**Voraussetzung:** CMS Erweiterungen (Shopware Evolve Plan)

**Schritt 1:** Inhalte > Erlebniswelten > Erlebniswelt öffnen  
**Schritt 2:** Plus-Symbol (+) > "Formular" per Drag & Drop einfügen  
**Schritt 3 — Formulareinstellungen:**
- Name (intern), Überschrift, Bestätigungstext
- Empfänger-Adresse, E-Mail-Template
- Optional als Vorlage speichern

**Schritt 4 — Feldtypen:**

| Typ | Konfiguration |
|-----|---------------|
| Textfeld / E-Mail | Mit Platzhalter |
| Nummernfeld | Min/Max/Schritte |
| Checkbox | Pflichtfeld möglich |
| Dropdown | Benutzerdefinierte Optionen |
| Textfläche | Mehrzeilig |

Für jedes Feld: Name, Titel, Typ, Breite, Pflichtfeld-Status, Fehlermeldung.

**Schritt 5:** Formular einer Kategorie oder Shop-Seite zuweisen.

---

## 3. Einrichtung des Footers und Servicemenüs

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/einrichtung-des-footers  
**Ab Version:** 6.4.0.0

### Teil 1: Informationsseiten im Footer

**Kategoriestruktur anlegen (Kataloge > Kategorien):**
- Hauptkategorie anlegen (muss aktiv sein)
- Subkategorien via Kontextmenü ("...") > "Neue Subkategorie"
- Jeder Menüpunkt = eigene Kategorie

**Erlebniswelten anlegen und zuweisen:**
- Layout-Typ: "Shopseiten"
- Vorlagen vorhanden für: Impressum, Datenschutz, AGB
- Zuweisung via Kategorie > "Layout (1)"

**Navigation dem Verkaufskanal zuweisen:**
- Verkaufskanäle > Grundeinstellungen
- "Einsprungpunkt für die Footer-Navigation"
- "Einsprungpunkt für die Service-Navigation"
- Hotline anpassen via Textbausteine: `footer.serviceHotlineHeadline`, `footer.serviceHotline`

### Teil 2: Links zu Informationsseiten

**Shopseiten erstellen:** Inhalte > Erlebniswelten (Typ: Shopseiten)

**Shopseiten zuweisen:** Einstellungen > Stammdaten > Shopseiten

| Seite | Verwendung |
|-------|-----------|
| Versandkosten | Produktdetailseiten |
| Datenschutz | Registrierungsformular |
| AGB + Widerruf | Checkout |

---

## 4. Erstellung der robots.txt

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/erstellung-der-robots-txt

**Ab Version 6.7.1.0:** Robots.txt-Regeln pro Domain direkt im Admin konfigurierbar (Einstellungen > Allgemein > Stammdaten).

**Für ältere Versionen:** Datei manuell im `/public`-Verzeichnis anlegen.

**Beispielkonfiguration:**
```
User-agent: *
Allow: /
Disallow: */?
Disallow: */account/
Disallow: */checkout/
Disallow: */widgets/
Disallow: */navigation/
Disallow: */bundles/
Disallow: */impressum$
Disallow: */datenschutz$
Disallow: */agb$
Sitemap: https://DEINE_DOMAIN/sitemap.xml
```

**Test:** Google Search Console > robots.txt-Tester

**Mehrere Domains (.htaccess):**
```
RewriteRule ^robots\.txt$ robots/%{HTTP_HOST}.txt [NS]
```
**NGINX:**
```
rewrite ^/robots\.txt$ /robots/$host.txt
```
Dateien im `/public/robots/`-Verzeichnis ablegen.

---

## 5. Go-Live-Checkliste

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/Vorgehensweise-fuer-den-Go-Live  
**Ab Version:** 6.1.0.0

| Schritt | Aktion |
|---------|--------|
| 1. Links prüfen | Manuelle Links in Kategorien und Produktbeschreibungen anpassen |
| 2. Demodaten entfernen | Kategorien, Hersteller, Produkte, Eigenschaften (Deinstallation entfernt NICHT automatisch) |
| 3. Versandarten prüfen | Testmethoden entfernen, korrekte Zuweisung in Verkaufskanälen |
| 4. Sandbox deaktivieren | Zahlungsanbieter auf Produktion umstellen (z. B. PayPal: Einstellungen > Plugins > PayPal) |
| 5. Bestellprozess testen | Vollständige Testbestellung inkl. Zahlungsarten und Versand |
| 6. E-Mail-Templates prüfen | Logo, Produktinfos, Kundenvariablen, Bankdaten, Mailer-Einstellungen |
| 7. Nummernkreise | Neuen Nummernkreis für den Verkaufskanal anlegen (Einstellungen > Shop > Nummernkreise); nach Go-Live NICHT mehr ändern |
| 8. Shopware Account | Domain auf Zieldomain umstellen (account.shopware.com > Shop-Domain umbenennen — einmalig!); Verwendungstyp auf "Produktivumgebung" |
| 9. Lizenzdomain im Admin | Einstellungen > System > Shopware Account > Lizenzierungshost anpassen |
| 10. Domains der Verkaufskanäle | In jedem Kanal > Allgemein > Domains aktualisieren |
| 11. Hoster konfigurieren | Hauptdomain auf Shopware-Verzeichnis routen |

---

## 6. Nachträgliche Änderung des MwSt.-Satzes

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/nachtraegliche-aenderung-des-mwst-satzes  
**Ab Version:** 6.5.7.3

### Steuersatz in Einstellungen anpassen

Einstellungen > Shop > Steuer — länderspezifische Steuersätze mit Gültigkeitsdatum.

**Wichtig:** Keine Auswirkung auf hinterlegte Produktpreise — nur der Steueranteil im Warenkorb wird neu berechnet.

### Produktpreise per Import/Export anpassen

1. Produkte mit Standard-Profil exportieren
2. Netto-Preis mit Formel berechnen: `=Brutto/(1+(MwSt-Satz/100))`
3. Angepasste CSV wieder hochladen

### Produktpreise über Rabatte anpassen (Steuersenkung)

**Beispiel: 19 % → 16 %**
- Neuer Rabatt unter Marketing > Rabatte & Aktionen
- Nutzung gesamt + pro Kunde: 0 (unbegrenzt)
- Produktregel: "Positionen mit Steuersatz 19 % UND Rechnungsland Deutschland"
- Rabattwert: **2,52 %** (nicht 3 %, da 119 → 116 %)

**Beispiel: 7 % → 5 %**
- Produktregel: "Positionen mit Steuersatz 7 %"
- Rabattwert: **1,87 %**

### Steuersatz bei bestehenden Bestellungen ändern

1. Bestellung öffnen > Bearbeiten
2. Steuersatz per Doppelklick editieren
3. Speichern

---

## 7. Partner- und Kampagnenmarketing (Affiliate-Codes)

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/Partnermarketing  
**Ab Version:** 6.1.3.0

### URL-Syntax

```
# Partner-URL
http://www.meineshopurl.de/?affiliateCode=MeinAffiliateCode

# Kampagnen-URL
http://www.meineshopurl.de/?campaignCode=MeinCampaignCode

# Kombiniert
http://www.meineshopurl.de/?affiliateCode=MeinAffiliateCode&campaignCode=MeinCampaignCode
```

**Kein Cookie erforderlich** — Codes werden direkt in der Datenbank hinterlegt.

Der Code wird der Bestellung zugewiesen, auch wenn der Kunde bereits registriert ist.

### Codes auswerten

In Kundenübersicht und Bestellungenübersicht: Spalten "Affiliate-Code" und "Kampagnen-Code" einblenden und filtern.

---

## 8. Produkte in die USA verkaufen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/produkte-in-die-usa-verkaufen  
**Ab Version:** 6.4.7.0

**Schritt 1 — Neue Kundengruppe (Netto-Anzeige):**
Einstellungen > Kundengruppen > Gruppe mit Netto-Preisanzeige anlegen.

**Schritt 2 — Sprache:**
Einstellungen > Shop > Sprache > "English, United States" mit Locale `en-US` und ISO-Code `en-US`.

**Schritt 3 — Verkaufskanal:**
- Kundengruppe: US-Gruppe
- Sprache: amerikanisches Englisch

**Schritt 4 — Steuern:**
Einstellungen > Steuern > Standard-Satz > Land: USA > "Individual States" > Bundesstaaten und Steuersätze eintragen.

**Schritt 5 — Textbaustein anpassen:**
Textbaustein `checkout.summaryTax` von "MwSt." auf "Sales tax" ändern (neues Textbaustein-Set anlegen).

---

## 9. Sendungsverfolgung

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/sendungsverfolgung  
**Ab Version:** 6.4.8.0

### Tracking-Link in E-Mail-Template (Text)

Navigation: Einstellungen > E-Mail-Templates > "Eintritt Lieferstatus: Versandt"

```twig
{% for delivery in order.deliveries %}
{% for trackingCode in delivery.trackingCodes %}
https://www.dhl.de/de/privatkunden/pakete-empfangen/verfolgen.html?piececode={{ trackingCode }}
{% endfor %}
{% endfor %}
```

### Tracking-Link in E-Mail-Template (HTML)

```html
{% for delivery in order.deliveries %}
{% for trackingCode in delivery.trackingCodes %}
Sendungsverfolgung: <a href="https://www.dhl.de/de/privatkunden/pakete-empfangen/verfolgen.html?piececode={{ trackingCode }}">{{ trackingCode }}</a><br>
{% endfor %}
{% endfor %}
```

### Tracking-URL in Versandart hinterlegen

Einstellungen > Shop > Versandart > Basis-URL eintragen:
`https://www.dhl.de/de/privatkunden/pakete-empfangen/verfolgen.html?piececode=`

### Sendungsnummer in Bestelldetails

Bestellung öffnen > Bearbeiten > Sendungsnummer(n) eingeben → erscheint im Kundenbereich unter "Bestellungen".

---

## 10. Shopware Erweiterungen — Lizenzen und Subscriptions FAQ

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shopware-erweiterungen-lizenzen-faq

### Lizenzen FAQ

| Frage | Antwort |
|-------|---------|
| Erweiterungs-Warnung im Admin | Nicht lizenzierte Erweiterungen müssen komplett gelöscht werden |
| Lizenz richtig löschen | Deinstallieren + Löschen in Meine Erweiterungen; ggf. manuell aus DB/Dateisystem; Miete auf account.shopware.com kündigen |

### Subscriptions FAQ

| Frage | Antwort |
|-------|---------|
| Was ist eine Subscription? | Sichert Update-Versorgung (Features, Sicherheits-Patches) |
| Auswirkungen ohne Subscription | Keine direkten Ausfälle, aber keine Updates mehr |
| Subscription verlängern | Nicht mehr möglich — Wechsel zu Mietmodell empfohlen |
| Lizenzverstoß | Mietlizenz wird bereitgestellt, keine Strafgebühr |

**Kontakt:** store@shopware.com

---

## 11. Tipps zur Bedienung des Admin

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/tippszurbedienungdesadmin  
**Ab Version:** 6.0.0

### Multi-Tab-Nutzung

Shopware unterstützt mehrere Browser-Tabs. Bei Abmeldung: automatische Abmeldung in allen Tabs.

### Tastenkürzel

**Übersicht aufrufen:** Shift + ?

| Aktion | Shortcut |
|--------|----------|
| Suchfeld aktivieren | `f` |
| Speichern | `alt+s` (Win/Linux) / `ctrl+s` (Mac) |
| Aktion abbrechen | `Esc` |
| Cache leeren | `alt+c` / `ctrl+c` |
| Neues Produkt | `A + P` |
| Neue Kategorie | `A + C` |
| Neuer Kunde | `A + U` |
| Neuer Hersteller | `A + M` |
| Dashboard | `G + H` |
| Produkte | `G + P` |
| Bestellungen | `G + O` |
| Einstellungen | `G + S` |

---

## 12. Testumgebung anlegen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/testumgebung-anlegen

### Option 1: Nebenverzeichnis des Liveshops

1. Neuen Ordner anlegen (z. B. "testshop")
2. Alle Dateien inkl. `.env` und `.htaccess` kopieren
3. Subdomain erstellen und auf Ordner routen

**Leere Datenbank anlegen (phpMyAdmin / Adminer / CLI):**
```sql
CREATE DATABASE IF NOT EXISTS NameDeinerDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**`.env` anpassen:**
```
DATABASE_URL=mysql://user:passwort@localhost:3306/testshop
APP_URL=http://deinshop.de/testshop/public
```
*Ab Shopware 6.5: In `.env.local` statt `.env`.*

**Live-Datenbank kopieren (CLI):**
```bash
# Export
mysqldump -u Benutzername -p NameDerDatenbank > Dateiname.sql
# Import
mysql -u Benutzername -p NameDerDatenbank < NameDesExports.sql
```

**Verkaufskanal-Domain anpassen:** Admin > Verkaufskanal > URL für Testumgebung eintragen.

**Bei erstem Admin-Aufruf:** "Deine Shop-Domain hat sich geändert" → "Installiere Deine Apps neu" wählen.

### Option 2: Lokale Testumgebung

`/etc/hosts`-Eintrag:
```
192.168.0.123    mein-shop.de
```
Achtung: Liveshop ist vom selben Rechner dann nicht mehr erreichbar.

### Option 3: Staging-Modus (ab 6.6.1.0)

Integrierter Staging-Modus in der Developer Documentation beschrieben.

---

## 13. Übersetzungen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/Uebersetzungen  
**Ab Version:** 6.0.0

### Textbausteine (System-Texte)

Einstellungen > Shop > Textbausteine — jede Sprache hat ein eigenes Set.

Für neue Sprachen (z. B. Niederländisch): Set duplizieren und übersetzen. Alternativ: Sprachpaket aus dem Plugin Store.

### Individuelle Texte (Produkte, Kategorien etc.)

Einstellungen > Shop > Sprachen > Neue Sprache anlegen.

**Übersetzungsprozess:**
1. Produktübersicht öffnen
2. Originalsprache einstellen
3. Produkt bearbeiten
4. Sprache auf Zielsprache wechseln
5. Felder übersetzen (grau = geerbt, noch nicht übersetzt)

---

## 14. Wie gestalte ich meinen Shop

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/wie-gestalte-ich-meinen-shop  
**Ab Version:** 6.4.7.0

**Layout erstellen:** Inhalte > Erlebniswelten > Neues Layout > Layouttyp wählen > Elemente via Drag & Drop

**Layout zuweisen:** Kataloge > Kategorien > Layout-Reiter

**Layouts duplizieren:** Inhalte > Erlebniswelten > Layout wählen > "Duplizieren"

---

## 15. Zahlungsarten für mehrere Länder

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/zahlungsarten-fuer-verschiedene-laender  
**Ab Version:** 6.4.7.0

**Rechtlicher Hinweis:** EU-Geoblocking-Verordnung beachten — rechtliche Beratung empfohlen.

**Schritt 1 — Regel erstellen:**

Beispiel: Nur für UK
- Name: "Invoice only for UK" | Priorität: 1
- Bedingung: `Rechnungsland | Ist eine von | Vereinigtes Königreich`

Beispiel: Für alle außer UK
- Name: "All except UK" | Priorität: 10
- Bedingung: `Rechnungsland | Ist keine von | Vereinigtes Königreich`

**Schritt 2 — Regel zuweisen:**
Zahlungsart > Verfügbarkeitsregel > erstellte Regel auswählen.

---

## 16. Versand nach Großbritannien aus der EU

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-and-faq/versand-nach-GB

### Steuerliche Behandlung

| Szenario | Regelung |
|----------|----------|
| EU → UK Direktlieferung | Ausfuhrlieferung, steuerfrei |
| UK Waren bis £135 | Keine Zollgebühren, keine Einfuhrumsatzsteuer |
| UK Waren über £135 | MwSt. bei Einfuhr fällig |
| UK Marketplace bis £135 | Marktplatz-Simulation, keine UK-Registrierungspflicht |

### Zolldokumente

| Dokument | Verwendung |
|----------|-----------|
| CN22 | Pakete bis 2 kg / € 425 |
| CN23 + CP71 | Pakete 2–20 kg / € 425+ |

**Pflichtangaben in CN22/CN23:**
- Detaillierte Artikelbeschreibung (keine allgemeinen Begriffe!)
- Nettogewicht, Artikelwert mit Währung
- HS-Tarifnummer (6-stellig)
- Ursprungsland
- Datum und Unterschrift

**EORI-Nummer:** Ab 1. Januar 2021 für EU-UK-Warenverkehr erforderlich (beginnt mit "GB").

---

## 17. Lagerbewegung deaktivieren

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/gewusst-wie/lagerbewegung-deaktivieren  
**Ab Version:** 6.5.4.0

Wenn ein externes Lager-/WMS-System die Bestandsverwaltung übernimmt, kann Shopware die interne Berechnung deaktivieren.

**Konfiguration** (`/config/packages/shopware.yaml`):

```yaml
shopware:
  stock:
    enable_stock_management: false
```

Danach: Cache leeren. Bestandswerte bleiben gespeichert, werden aber nicht mehr automatisch angepasst.

---

## 18. Cookie Consent Manager — FAQ

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/gewusst-wie/cookie-consent-manager-faq  
**Ab Version:** 6.7.0.0

| Frage | Antwort |
|-------|---------|
| Einstellungen im Admin? | Einstellungen > Allgemein > Stammdaten |
| Alles-akzeptieren-Button? | Einstellungen > Allgemein > Stammdaten aktivieren |
| Cookie-Einstellungen für Kunden änderbar machen? | Kategorie anlegen: Typ Link, Ziel `/cookie/offcanvas`, Protokoll deaktivieren |
| Texte anpassen? | Einstellungen > Regional > Textbausteine > Suche "Cookie" |

---

## 19. Shopware Video-Guide: Upload und Nutzung

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shopware-video-guide  
**Ab Version:** 6.7.8.0

### Unterstützte Videoformate

- `video/mp4` (.mp4)
- `video/ogg` (.ogv, .ogg)
- `video/webm` (.webm)

Formate wie `.mov` oder `.avi` können Warnungen auslösen und möglicherweise nicht abspielen.

### Upload-Limits

Abhängig von Servereinstellungen (`upload_max_filesize`, `post_max_size`). URL-Upload-Limit: `shopware.media.url_upload_max_size`.

### Verwendung

| Bereich | Pfad |
|---------|------|
| Upload | Inhalte > Medien > Drag & Drop |
| Coverbild | Video auswählen > "Coverbild festlegen" |
| In Produktgalerie | Kataloge > Produkte > Medien-Bereich |
| In CMS-Seiten | Inhalte > Erlebniswelten > Medienelement > Video wählen |

### Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| "Nicht unterstütztes Format" | In MP4/OGG/WebM konvertieren |
| "Payload too large" | Serverlimits erhöhen oder URL-Upload nutzen |
| Transport-/Timeout-Fehler | Stabile Verbindung, Dateigröße reduzieren |
| Cover-Auswahl fehlgeschlagen | Gültiges Bildformat verwenden |

---

## 20. Code Snippets für Produktvergleiche

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/gewusst-wie/produktvergleich-code-snippets  
**Ab Version:** 6.4.0.0

Twig-Snippets für Produktvergleichs-Templates:
- Listenpreise exportieren (wenn `sale_price` vorhanden)
- Zusätzliche Bildlinks in Schleife
- Versandkosten-Segment
- Grundpreisangaben (`purchaseUnit`, `referenceUnit`)
- Varianteneigenschaften in Schleife

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/gewusst-wie — Stand: 2026-06*
