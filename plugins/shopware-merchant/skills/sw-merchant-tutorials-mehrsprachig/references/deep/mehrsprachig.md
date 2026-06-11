# Shopware 6 — Tutorials: Mehrsprachige Shops (vollständige Referenz)

---

## Allgemeines Vorgehen für nicht-standardsprachige Shops

Für alle Sprach-Setups gilt folgender Grundansatz:

1. **Shopware installieren** und Standardsprache wählen
2. **Sprachpaket installieren** (First Run Wizard oder Einstellungen > Plugins)
3. **Admin-Sprache anpassen** (Benutzerprofil > Sprache der Benutzeroberfläche)
4. **Verkaufskanal konfigurieren:**
   - Länder, Währungen, Sprachen hinzufügen
   - Domains mit Sprachzuordnung
5. **Steuern konfigurieren** (landesspezifische Sätze)
6. **Inhalte übersetzen** (Kategorien, Produkte, Eigenschaften)

Grau dargestellte Felder = geerbt/nicht übersetzt.  
HTTP und HTTPS müssen identische Einstellungen haben.

---

## 1. Schweizer Shop (Deutsch + Französisch)

**Quelle:** https://docs.shopware.com/de/shopware-6/tutorials-und-faq/shop-in-einer-nicht-standardsprache-einrichten/schweiz  
**Shopware:** 6.2.0 – 6.3.5.3

### Konfiguration

**Installationssprache:** Deutsch (empfohlen)

**Sprachpaket:** Französisch-Paket über First Run Wizard installieren.

**Verkaufskanal:**
- Länder: Schweiz + Deutschland
- Standardland: Schweiz
- Währung: Schweizer Franken (CHF) als Standard
- Sprachen: Deutsch + Französisch

**Domains:**
- Domain 1: Hauptdomain mit CHF-Währung
- Domain 2: z. B. `store.ch/_fr` für Französisch (Sprache + Textbaustein-Set korrekt zuordnen)

**Steuern:** Einstellungen > Steuern > Schweizer Satz: Standard 7,7 %

**Inhalt übersetzen:** Kategorien, Produkte, Eigenschaften in beide Sprachen übersetzen.

---

## 2. Englischer UK-Shop

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shop-einrichten-in-einer-nicht-standard-sprache/englisch

### Konfiguration

**Installationssprache:** English

**Standardwährung:** GBP (empfohlen)

**Steuern:** Einstellungen > Steuern > UK-Satz: **20 %** Standard-MwSt.

**Verkaufskanal:**
- Länder hinzufügen; Standardland wählen
- Mehrere Währungen möglich (Standardwährung festlegen)
- Sprache: Englisch + ggf. weitere

**Domains:** HTTP und HTTPS mit gleichen Einstellungen anlegen.

**Inhalte:**
- Footer-Navigation als Kategoriestruktur
- Shopping Experiences für Shop-Seiten (Impressum, Datenschutz, T&Cs)
- Produkte, Kategorien, Eigenschaften in Englisch übersetzen (Sprachauswahl oben rechts)

---

## 3. Niederländischer Shop

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shop-einrichten-in-einer-nicht-standard-sprache/niederlaendisch

### Konfiguration

**Installationssprache:** Nederlands

**Steuern:** Einstellungen > Steuern > Niederländischer Satz: **21 %**

**Storefront:**
- Länder, Währungen, Sprachen im Verkaufskanal konfigurieren
- Subdomain-Struktur für mehrsprachige Shops empfohlen

**Produkteigenschaften übersetzen:** Kontextmenü > Sprache wechseln

---

## 4. Irischer Shop (auf Deutsch)

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shop-einrichten-in-einer-nicht-standard-sprache/irisch

Einrichtung analog zu anderen Länder-Shops:
- Steuern für Irland konfigurieren (IR-MwSt. 23 % Standard)
- Sprachpaket falls nötig installieren
- Verkaufskanal mit irischen Domains/Ländern konfigurieren

---

## 5. Polnischer Shop

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shop-einrichten-in-einer-nicht-standard-sprache/polnisch

Einrichtung analog:
- Polnisches Sprachpaket installieren
- Steuern für Polen konfigurieren (PL-MwSt. 23 % Standard)
- PLN als Währung konfigurieren

---

## 6. Shop in Fremdsprache / Bilingual einrichten

**Allgemeine Ressource:** https://docs.shopware.com/de/shopware-6-de/tutorials-and-faq/setting-up-the-Store-in-a-non-default-language/foreign

Für mehrsprachige Länder (bilingual):
- https://docs.shopware.com/de/shopware-6/tutorials-und-faq/shop-einrichten-in-einer-nicht-standard-sprache/bilingual

Prinzip: Für jede Sprache eine eigene Domain anlegen, der jeweiligen Sprache + Textbaustein-Set zuordnen.

---

## 7. USA-Verkauf (Kurzreferenz)

*(Ausführlich in: sw-merchant-tutorials-gewusst-wie)*

**Kernpunkte:**
- Kundengruppe mit Netto-Preisanzeige
- Sprache: `en-US` anlegen
- Steuern: US-States mit Sales-Tax-Sätzen
- Textbaustein `checkout.summaryTax` → "Sales tax"

---

## 8. Versand nach Großbritannien (Kurzreferenz)

*(Ausführlich in: sw-merchant-tutorials-gewusst-wie)*

**Kernpunkte:**
- Waren bis £135: zollfrei
- Zolldokument CN22 (≤ 2 kg) oder CN23 (> 2 kg)
- EORI-Nummer ab 01.01.2021 erforderlich
- Allgemeine Beschreibungen wie "Ersatzteile" sind ungültig

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shops-in-anderen-sprachen — Stand: 2026-06*
