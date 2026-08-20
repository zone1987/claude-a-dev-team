# Shopware SaaS — Einstieg & Ersteinrichtung

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/einstieg-in-shopware-saas

---

## Admin-Zugang

**URL-Format:** `https://[shopdomain]/admin`  
**Beispiel:** `https://meinshop.shopware.store/admin`

---

## Checkliste: Erste Schritte

### 1. Kategorien und Produkte anlegen

**Kategorien:**
- Neue Hauptkategorie: **Produkte** (unter „home")
- Footer-Kategorie: **Footer Menü** (für Rechtstexte)
- Kontextmenü-Optionen: „Neue Kategorie davor", „Neue Kategorie danach", „Neue Subkategorie"

**Produkte erstellen:**
- Pfad: **Kataloge > Produkte > „Neue Produkte hinzufügen"**
- Erforderliche Felder ausfüllen, dann speichern

### 2. Branding / Theme

- **Pfad:** Themes
- **Standard-Theme duplizieren:** Themes > Shopware default theme > „..." > „Duplikat erstellen"
- Eigenes Duplikat bearbeiten — bleibt nach Updates unverändert
- **Erlebniswelten:** Inhalte > Erlebniswelten (für Landingpages, Shop- und Kategorieseiten)

### 3. Gesetzliche Bestimmungen (Pflicht!)

- Impressum unter „Legal" im Kategorienbaum anlegen
- Alle Layouts unter „Rechtliches" und „Informationen" anpassen
- Speichern: Oben rechts auf **„Speichern"** klicken

### 4. Versand- und Zahlungsarten

- **Versand:** Einstellungen > Shop > Versand
- **Zahlungsarten:** Standard = Nachnahme, Vorkasse, Rechnung
- Direktlink: Checkliste > „Lege Versand- und Zahlungsarten fest"

---

## Weitere erste Schritte

### Unternehmensinformationen
- **Pfad:** Einstellungen > Unternehmen
- **Felder:** Umsatzsteuer-ID, Kontaktinformationen
- **Hinweis:** Bei Shopware-Account-Verknüpfung sind manche Daten gebunden (nicht direkt änderbar)

### Produkte importieren
- **Pfad:** Einstellungen > Shop > Import/Export
- Artikel und weitere Inhalte importierbar

### Mehrere Sprachen
- **Pfad:** Einstellungen > Shop > Sprachen
- Standard: Englisch vorinstalliert
- Länder / Währungen: Erfordert höheren Plan (Rise, Evolve oder Beyond)

### Dokumente erstellen
- **Pfad:** Einstellungen > Shop > Dokumente
- Standardvorlagen: Lieferschein, Rechnung, Gutschrift, Stornorechnung
- Bestellung → Drei-Punkte-Menü → „Anzeigen" → „Neu erstellen" → Dokumenttyp wählen

---

## Systemeinstellungen

### Wartungsmodus
- **Aktivierung:** Verkaufskanal wählen > Status > Wartungsmodus
- **IP-Whitelist:** Eigene IP eintragen, um Shop trotz Wartungsmodus anzusehen
- **Voraussetzung:** Plan muss bereits gebucht sein

### Storefront im Baumodus anzeigen
- Admin-Login im selben Browser setzt automatisch ein Cookie
- Shop für Admin sichtbar, für Besucher weiterhin „In Bearbeitung"-Seite
- **Einschränkung:** Private/Inkognito-Fenster erlauben keinen Admin-Login

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/einstieg-in-shopware-saas*
