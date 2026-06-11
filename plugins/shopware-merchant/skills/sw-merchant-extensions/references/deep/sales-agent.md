# Sales Agent – Außendienst-Frontend-App

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/sales-agent  
**Plan**: Shopware Evolve (oder höher)  
**Verfügbar ab**: Shopware 6.5.0.0  
**Typ**: Separate Frontend-Anwendung (kein Admin-Plugin)

## Überblick

Der **Sales Agent** ist ein Benutzerverwaltungssystem für Vertriebsteams:
- Außendienstmitarbeiter bekommen eigene Zugänge
- Können zugewiesene Kunden und deren Bestellhistorie einsehen
- Können Bestellungen im Namen von Kunden aufgeben
- Angebots-/Quoten-System für individuelle Preisverhandlungen

> "Bei dem Sales Agent handelt es sich **nicht** um eine Erweiterung, die im Shopware Admin
> installiert oder per Klick aktiviert werden kann, sondern um eine **separate Frontend-App**."

---

## Technische Besonderheit

Der Sales Agent wird als **Quellcode über ein GitLab-Repository** bereitgestellt:
- Agenturen und Entwickler können die App anpassen und integrieren
- Deployment durch technisches Team notwendig
- Verbindung zum Shopware-Backend über API

---

## Administration (Shopware Admin)

### Zugang
**Einstellungen > System > Sales Agent**

### Sales-User-Konten erstellen
1. "Neuen Sales Agent anlegen" klicken
2. Name, E-Mail-Adresse eingeben
3. Kunden zuweisen (Mehrfachauswahl)
4. Speichern → automatische **Einladungs-E-Mail** mit Link zur Passwort-Einrichtung

### Kunden zuweisen
- Einem Sales Agent können beliebig viele Kunden zugewiesen werden
- Ein Kunde kann mehreren Sales Agents zugeordnet sein
- Zuweisung jederzeit änderbar

---

## Sales Agent Frontend-App

### Dashboard-Funktionen

| Funktion | Beschreibung |
|---|---|
| Kundenliste | Alle zugewiesenen Kunden im Überblick |
| Bestellhistorie | Bestellungen pro Kunde einsehen |
| Neue Bestellung | Im Namen des Kunden bestellen |
| Angebotserstellung | Angebote mit individuellen Preisen erstellen |
| Angebotsverwaltung | Status verfolgen, Angebote versenden |

### Neue Bestellung im Namen eines Kunden
1. Kunden in der Liste auswählen
2. "Neue Bestellung" klicken
3. Produkte auswählen und konfigurieren
4. Menge und optionale Anpassungen
5. Bestellen

---

## Angebotssystem

### Angebot erstellen
1. Kunden auswählen
2. "Neues Angebot" erstellen
3. Produkte hinzufügen
4. **Individuelle Preise** und **Rabatte** festlegen
5. Ablaufdatum setzen
6. **Dokument auto-generieren** oder manuelles Dokument hochladen
7. Angebot an Kunden senden (E-Mail mit Angebotslink)

### Angebots-Workflow
```
Sales Agent erstellt Angebot
  → Kunde erhält E-Mail mit Angebotslink
  → Kunde öffnet Angebot im Storefront
  → Kunde akzeptiert → Bestellung wird erzeugt
  → Oder: Kunde lehnt ab → Sales Agent informiert
```

---

## Persönliche Einstellungen (Sales Agent Portal)

Sales Agent können selbst ändern:
- Anzeigesprache
- Zeitzone
- Vorname / Nachname
- Telefonnummer
- Passwort

**Nicht änderbar durch Sales Agent**:
- E-Mail-Adresse (nur Admin)
- Kundenzuweisungen (nur Admin)

---

## Anwendungsfälle

- B2B-Außendienst: Vertriebsmitarbeiter vor Ort bestellen für Kunden
- Key Account Management: Dedizierte Betreuer für Großkunden
- Telefonverkauf: Sales-Mitarbeiter nehmen Bestellungen telefonisch auf
- Angebotsprozesse: Preisverhandlungen mit nachverfolgbaren Angeboten
