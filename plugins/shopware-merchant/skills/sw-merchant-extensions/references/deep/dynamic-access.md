# Dynamic Access – Regelbasierte Inhaltszugangskontrolle

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/dynamicaccess  
**Plan**: Shopware Evolve (oder höher)  
**Verfügbar ab**: Shopware 6.4.6.0 (Rule Builder Integration)

## Überblick

**Dynamic Access** ermöglicht es, Shop-Inhalte (Kategorien, Produkte, Varianten) auf Basis
von Rule-Builder-Regeln **bedingt anzuzeigen oder zu verbergen**. Inhalte erscheinen im
Storefront nur, wenn eine der definierten Regeln zutrifft.

---

## Anwendungsbereiche

### 1. Kategorien ausblenden

**Konfiguration**:
1. **Katalog > Kategorien** → Kategorie öffnen
2. Tab **Allgemein** → Abschnitt "Sichtbarkeit"
3. Unter "Dynamic Access Rules" → Regeln hinzufügen

**Verhalten**:
- Kategorie wird im Storefront nur angezeigt, wenn **mindestens eine** der Regeln zutrifft
- Keine Regeln gesetzt = Kategorie immer sichtbar (Standard)

> **Hinweis**: Versteckte Kategorien verbergen die enthaltenen Produkte **nicht automatisch**.
> Produkte können über die Suche noch gefunden werden – daher auch auf Produktebene Regeln setzen.

### 2. Produkte ausblenden

**Konfiguration**:
1. **Katalog > Produkte** → Produkt öffnen
2. Tab **Allgemein** → Abschnitt "Sichtbarkeit"
3. Unter "Dynamic Access Rules" → Regeln hinzufügen

**Verhalten**:
- Produkt wird nur angezeigt, wenn mindestens eine Regel zutrifft
- Unsichtbare Produkte sind auch **nicht suchbar**

### 3. Varianten ausblenden

**Konfiguration**: Auf Variantenebene (innerhalb des Produkts, Tab Varianten)

**Besonderheit**: Varianten werden nicht direkt ausgeblendet. Stattdessen:
- Variante ist auf der Produktdetailseite **nicht wählbar** (ausgegraut)
- Das Produkt selbst bleibt sichtbar

---

## Regeln erstellen (Rule Builder)

### Typische Regeln für Dynamic Access

| Regel | Anwendungsfall |
|---|---|
| Kundengruppe = "B2B" | Nur für B2B-Kunden sichtbar |
| Kunde ist eingeloggt | Nur für registrierte Kunden |
| Land = "DE" | Nur in Deutschland sichtbar |
| Datum zwischen [Start] und [Ende] | Saisonale Produkte |
| Warenkorb enthält Produkt X | Cross-Selling-Logik |

Regeln erstellen: **Einstellungen > Regeln > Neue Regel**

---

## Wichtige Hinweise & Fallstricke

### Produkte in versteckten Kategorien
- Wenn eine Kategorie per Dynamic Access versteckt wird, bleiben die Produkte
  darin über die **Suche** auffindbar
- **Lösung**: Gleiche Regeln auch auf Produktebene anwenden (oder Bulk-Assignment)

### Sich gegenseitig ausschließende Regeln
- Regeln sollten nicht so konfiguriert sein, dass der Inhalt **nie** angezeigt wird
- Beispiel: Regel A = "Land DE" UND Regel B = "Land FR" mit AND-Verknüpfung → niemals sichtbar
- Verwende OR-Verknüpfung oder prüfe die Regellogik

### Warenkorb mit verstecktem Produkt
- Wenn ein Produkt in den Warenkorb gelegt wurde und danach per Dynamic Access
  ausgeblendet wird, **blockiert es den Checkout**
- Der Kunde muss das Produkt aus dem Warenkorb entfernen

---

## Bulk-Zuweisung per Import/Export

Für große Kataloge: Regeln über den **Import/Export-Bereich** in Massen zuweisen:
1. **Einstellungen > Import/Export** öffnen
2. Produkt-Export durchführen (CSV)
3. Dynamic-Access-Spalten in der CSV ausfüllen
4. Importieren

---

## Abgrenzung zu anderen Zugangsmechanismen

| Mechanismus | Beschreibung |
|---|---|
| Dynamic Access | Regelbasierte Sichtbarkeit (Plan: Evolve+) |
| Kundengruppen-Sichtbarkeit | Standard: Produkte/Kategorien für Kundengruppen konfigurieren |
| Shopware Login Required | Shop komplett hinter Login sperren (Einstellungen > Benutzer & Rechte) |
