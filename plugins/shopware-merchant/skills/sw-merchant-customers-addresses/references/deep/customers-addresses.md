# Shopware 6 – Kundenadressen: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/kunden/uebersicht (Tab Adressen)  
> Dokumentierte Version: 6.7.0.0+

---

## 1. Adressen im Admin verwalten

### Zugriff

`Kunden` → Kunden auswählen → Tab **„Adressen"**

![Adressen Tab Admin](../../assets/kunden-uebersicht-adressen.png)

*(Screenshot aus sw-merchant-customers/assets/kunden-uebersicht-adressen.png)*

### Elemente

| Nr. | Element | Funktion |
|-----|---------|----------|
| (1) | **Standard-Lieferadresse** | Grüne Markierung; klicken zum Ändern |
| (2) | **Standard-Rechnungsadresse** | Grüne Markierung; klicken zum Ändern |
| (3) | **Suche** | Adressen nach Text filtern |
| (4) | **Neue Adresse hinzufügen** | Formular zum Anlegen öffnen |
| (5) | **Kontextmenü (⋮)** | Bearbeiten · Duplizieren · Löschen |

### Aktionen im Detail

#### Neue Adresse hinzufügen

1. Button **„Neue Adresse hinzufügen (4)"** klicken
2. Formular ausfüllen (Pflichtfelder: Vorname, Nachname, Straße, PLZ, Stadt, Land)
3. Speichern

#### Adresse bearbeiten

1. Kontextmenü **(⋮)** der Adresse öffnen
2. **„Bearbeiten"** wählen
3. Änderungen vornehmen und speichern

#### Adresse duplizieren

1. Kontextmenü **(⋮)** der Adresse öffnen
2. **„Duplizieren"** wählen
3. Kopie erscheint in der Liste → ggf. anpassen

#### Adresse löschen

1. Kontextmenü **(⋮)** der Adresse öffnen
2. **„Löschen"** wählen
3. Bestätigung im Dialog

> Standard-Liefer- und Standard-Rechnungsadressen können nicht gelöscht werden, solange sie als Standard markiert sind.

#### Standard-Adresse ändern

1. Kontextmenü **(⋮)** der gewünschten Adresse öffnen
2. **„Als Standard-Lieferadresse setzen"** oder **„Als Standard-Rechnungsadresse setzen"** wählen
3. Alte Standard-Markierung wird automatisch entfernt

---

## 2. Bearbeitungsmodus – Adressen

Im **Bearbeitungsmodus** des Kunden (Button „Bearbeiten" in der Detailansicht) kann ebenfalls die **Standard-Liefer- und Standard-Rechnungsadresse** direkt geändert werden.

---

## 3. Neuen Kunden anlegen – Adresse vorbelegen

Beim Anlegen eines neuen Kunden kann im Bereich **„Adressen"** direkt eine erste Adresse hinterlegt werden.  
Diese wird automatisch als Standard-Liefer- und Standard-Rechnungsadresse gesetzt.

---

## 4. Adressen im Storefront (Kundensicht)

Kunden verwalten Adressen selbst unter:  
`Mein Konto` → **„Adressen"**

Verfügbare Aktionen:
- Neue Adresse hinzufügen
- Bestehende Adressen bearbeiten
- Adressen löschen
- Standard-Adressen festlegen

---

## 5. Adressfelder

Standardmäßig werden folgende Felder erfasst:

| Feld | Pflicht |
|------|---------|
| Anrede | Nein |
| Vorname | Ja |
| Nachname | Ja |
| Firma | Nein |
| Straße + Hausnummer | Ja |
| Adresszusatz | Nein |
| PLZ | Ja |
| Stadt | Ja |
| Land | Ja |
| Bundesland/Region | Je nach Land |
| Telefonnummer | Nein |

> Die Pflichtfelder können über die Shopware-Einstellungen angepasst werden.
