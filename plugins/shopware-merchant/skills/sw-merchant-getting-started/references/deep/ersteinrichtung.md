# Ersteinrichtungs-Assistent (First-Run Wizard)

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/ersteinrichtungs-assistent

## Überblick

Der Ersteinrichtungs-Assistent (First-Run Wizard) startet **automatisch nach der ersten Installation**
von Shopware 6. Er führt durch die grundlegende Shop-Konfiguration in mehreren Schritten.

Der Assistent kann jederzeit erneut aufgerufen werden:
> **Einstellungen > System > Ersteinrichtungs-Assistent**

---

## Schritte des Assistenten

### 1. Dataimport (Demo-Daten)
- **Option A: Demo-Daten laden** – Produkte, Kategorien, Hersteller für Testzwecke importieren
- **Option B: Überspringen** – Mit leerem Shop beginnen

> Empfehlung: Demo-Daten für erste Tests laden; vor dem echten Betrieb wieder entfernen.

---

### 2. Standardwerte
- Konfiguration: Welche Verkaufskanäle werden **automatisch mit neu erstellten Produkten** verknüpft?
- Erleichtert das Inventarmanagement über mehrere Storefronts hinweg

---

### 3. Mailer-Einstellungen
- SMTP-Konfiguration für ausgehende E-Mails (Bestellbestätigungen, Passwort-Reset etc.)
- **Kann später konfiguriert werden** (überspringen möglich)
- Pfad zum Nachkonfigurieren: Einstellungen > System > Mailer

---

### 4. PayPal-Integration
- PayPal-API-Zugangsdaten eingeben
- Optional: PayPal als Standard-Zahlungsmethode für alle Verkaufskanäle setzen
- Kann auch später unter **Erweiterungen > Meine Erweiterungen > PayPal** konfiguriert werden

---

### 5. Erweiterungen
- Empfohlene Erweiterungen nach Region und Kategorie durchsuchen
- Direkte Installation im Assistenten möglich
- Voraussetzung: Shopware Account muss verknüpft sein (Schritt 6)

---

### 6. Shopware Account verknüpfen
- Account mit der Shop-Instanz verbinden
- Ermöglicht Zugriff auf gekaufte Erweiterungen und Lizenzen
- **Domain-Verifizierung** für Shop-Betrieb notwendig

---

### 7. Shopware Store-Verbindung
- Direktzugriff auf Shopware Store-Erweiterungen und -Dienste aus dem Admin heraus aktivieren
- Voraussetzung für die Anzeige des Store-Bereichs im Admin

---

## Nach dem Assistenten: Empfohlene erste Schritte

1. **Grundeinstellungen prüfen**: Einstellungen > Grundeinstellungen (Shop-Name, Adresse, Kontakt)
2. **Verkaufskanal konfigurieren**: Verkaufskanäle > Storefront
3. **Erste Kategorie anlegen**: Katalog > Kategorien
4. **Erstes Produkt erstellen**: Katalog > Produkte > Produkt anlegen
5. **Zahlungsmethoden aktivieren**: Einstellungen > Zahlungen
6. **Versandmethoden einrichten**: Einstellungen > Versand
7. **Steuerregeln konfigurieren**: Einstellungen > Steuern

---

## Tipps

- Der Assistent ist **idempotent** – erneutes Durchlaufen überschreibt keine vorhandenen Daten
- Schritte können einzeln übersprungen und später nachgeholt werden
- Nach dem Assistenten: Dashboard zeigt erste Statistiken
