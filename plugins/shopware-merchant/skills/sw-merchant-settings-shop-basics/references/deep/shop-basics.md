# Shopware 6 – Shop-Grundeinstellungen (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/shop

---

## Stammdaten

**Pfad:** Einstellungen > Shop > Stammdaten  
**Konfigurierbar:** Global oder pro Verkaufskanal

### 1. Shop-Informationen
| Feld | Beschreibung |
|---|---|
| Shopname | Öffentlicher Titel des Shops im Frontend |
| Shopbetreiber-E-Mail | Kontakt-E-Mail des Shop-Betreibers |
| Meta-Author | Autorenname für Meta-Tags (SEO) |
| Familienfreundlicher Shop | Markierung als jugendfreundlich |
| Shopbetreiber-Adresse | Geschäftsadresse für Impressum und Rechnungen |
| IBAN / BIC / Kontoinhaber | Bankdaten für Checkout und Rechnungen |

### 2. Shopseiten
Verknüpfung von statischen Inhaltslayouts mit rechtlichen Pflichtseiten:
- AGB, Widerrufsbelehrung, Versand- und Zahlungsarten
- Datenschutz, Impressum, 404-Fehlerseite
- Wartungsseite, Kontaktseite, Widerrufsantragsseite, Newsletter-Seite

### 3. Recht und Datenschutz
| Option | Beschreibung |
|---|---|
| Cookie-Banner | Standard-Cookie-Hinweis aktivieren |
| „Alle akzeptieren"-Button | Optionaler Schnellakzeptanz-Button im Cookie-Banner |
| Kontaktformular-Pflichtfelder | Vorname, Nachname, Telefonnummer als Pflicht konfigurierbar |
| Widerrufs-Button im Footer | „Vertrag widerrufen" optional anzeigen |

### 4. robots.txt-Regeln
- Allow/Disallow-Anweisungen für Suchmaschinen-Crawler
- Domainspezifische Konfiguration möglich

### 5. CAPTCHA-Optionen
| Variante | Beschreibung |
|---|---|
| Honeypot | Unsichtbares Feld zur Bot-Erkennung |
| Einfaches Captcha | Grafik mit verzerrter Buchstaben-/Zahlenkombination |
| Google reCAPTCHA v2 | „Ich bin kein Roboter"-Checkbox (mit optionalem Bilderrätsel) |
| Google reCAPTCHA v3 | Automatische Verifikation per Score (0–1) |
| Friendly Captcha | Blockchain-basiert, DSGVO-konform (kostenpflichtig) |

### 6. Meta-Robots-Tag
Standard-Robots-Meta-Tag für den gesamten Shop (Index/Noindex usw.)

---

## Adressen

**Pfad:** Einstellungen > Shop > Adressen  
**Hinweis:** Ab Shopware 6.6.x wurden Anzeigeoptionen angepasst und teils entfernt.

- Konfiguration: Postleitzahl vor oder nach dem Ortsnamen
- Pro Verkaufskanal konfigurierbar
- Beeinflusst Adressanzeige im Kundenkonto der Storefront
- Gültig für Versionen 6.1.0–6.5.8.x

---

## Anreden

**Pfad:** Einstellungen > Customer > Anreden

- Standardmäßig vorkonfigurierte Anreden mit formalen Brief-Versionen
- **Technischer Name:** Pflichtfeld (wird u.a. beim Bestellabschluss verwendet)
- Zwei Fallback-Anreden mit techn. Namen `not_specified` und `undefined`

### Aktionen
| Aktion | Beschreibung |
|---|---|
| Neue Anrede anlegen | Name, techn. Name, formale Briefversion |
| Anrede bearbeiten | Via Kontextmenü |
| Anrede löschen | Via Kontextmenü |

---

## Kundengruppen

**Pfad:** Einstellungen > Kundengruppen

> **Kritisch:** Die „Standard-Kundengruppe" hat eine feste UUID und kann nicht gelöscht werden. Beim Löschen ist das Frontend nicht mehr aufrufbar.

### Felder beim Anlegen
| Feld | Beschreibung |
|---|---|
| Name | Bezeichnung der Kundengruppe |
| Steuerdarstellung | Brutto- oder Nettopreisanzeige für diese Gruppe |
| Eigenes Registrierungsformular | Optional aktivierbar |

### Kundengruppen-Registrierung
- Formularkonfiguration: Titel, Einführungstext, SEO-Meta-Beschreibung
- Option: Registrierungsformular für Unternehmen (Firma, Abteilung, USt-ID)
- Technische URL wird nach dem Speichern generiert
- Muss mindestens einem Verkaufskanal zugewiesen sein

### B2B-Komponenten (Commercial, ab Plan Evolve)
- Mitarbeiterverwaltung, Schnellbestellungen, Angebotsmanagement, Bestellgenehmigung

### Workflow
1. Kunde registriert sich über eigenes Kundengruppen-Formular
2. Admin akzeptiert oder lehnt in den Kundendetails ab
3. Kunde erhält E-Mail-Benachrichtigung

---

## Nummernkreise

**Pfad:** Einstellungen > Allgemein > Nummernkreise

Erstellt eindeutige Serien von Zeichen-/Zahlenkombinationen für Bestellungen, Kunden und Belege.

### Felder
| Feld | Beschreibung |
|---|---|
| Name / Beschreibung | Identifikation in der Administration |
| Präfix | Zeichenkette vor der Nummer |
| Startnummer | Beginnnummer des Kreises |
| Suffix | Zeichenkette nach der Nummer |
| Erweitert | Pattern-basierte Nummernzuweisung (z.B. `Order{n}-{date}`) |
| Aktuelle Nummer | Zuletzt vergebene Nummer (Read-only) |
| Vorschau | Beispiel-Ausgabe |
| Zuweisung | Zweck + Verkaufskanal-Bindung |

### Verfügbare Nummernkreistypen
- Bestellungen, Rechnungen, Gutschriften, Stornorechnungen, Stornos
- Lieferscheine, Retouren, Teilstornierungen
- Kunden, Produkte
- Abo-Nummern (Abonnements-Feature)
- Angebote, Quote, Pending Order (B2B)

---

## Anmeldung & Registrierung

**Pfad:** Einstellungen > Kunde > Anmeldung & Registrierung

### Passwort-Einstellungen
| Option | Beschreibung |
|---|---|
| Passwort-Mindestlänge | Mindestanzahl Zeichen |
| Passwort zweimal eingeben | Bestätigung durch Wiederholung |

### Kontotyp-Optionen
- Standard: Kundenkonto oder Gastbestellung auswählen
- Auswahl zwischen Geschäfts- und Kundenkonto anzeigen

### Datenschutz & Daten
- Kunden-IP-Adressen in Klartext speichern (oder anonymisieren)
- Datenschutz-Checkbox als Pflichtfeld

### Persönliche Daten (anzeigen / Pflichtfeld)
- Anrede, Titel, Telefonnummer, Geburtstag
- E-Mail zweimal eingeben

### Double-Opt-In
- Für Registrierungen und Gast-Bestellungen separat aktivierbar
- Bestätigungs-URL konfigurierbar
- Double-Opt-In-Domain anpassbar

### Adressfelder
- Adresszusatzzeile 1 & 2 konfigurierbar
- Reihenfolge von Stadt, PLZ, Bundesland wählbar

### Sonstige Optionen
- Warenkorb bei Abmeldung löschen
- Kundenlöschung durch Kunden erlauben
- Zeit bis Gastkonten ablaufen (in Sekunden)
- Passwort-Wiederherstellungs-URL

---

## Warenkorb

**Pfad:** Einstellungen > Allgemein > Warenkorb

### Warenkorb-Konfiguration
| Option | Beschreibung |
|---|---|
| Maximale Auswahlmenge | Produktanzahl im Mengen-Dropdown (überschreibbar per Produkt) |
| Lieferzeit anzeigen | Lieferzeit im Warenkorb aus dem Artikel |
| Stornierungen erlauben | Kunden dürfen Bestellungen im Account stornieren |
| Payment-Token Gültigkeit | Zeitlimit in Minuten für Zahlungsabschluss (Standard: 60 min) |
| API Rate Limiting | Max. Produkte/Minute via API (Brute-Force-Schutz) |
| Summenspalte anzeigen | Summenspalte im Warenkorb ein-/ausblenden |
| Steuerspalte im Checkout | MwSt. statt Stückpreis anzeigen |

### Bestellabschluss
| Option | Beschreibung |
|---|---|
| Kommentarfeld | Kundenbemerkungen bei Bestellung aktivieren |
| Gastkunden-Logout | Automatisches Abmelden nach Bestellabschluss |

### AI-generierte Bestellabschluss-Nachricht (ab Plan Rise)
| Feld | Beschreibung |
|---|---|
| Tonfall | Neutral, Angeregt oder Humorvoll |
| Zeichenzahl | Richtwert für Textlänge |
| Verfügbarkeitsregel | Rule-Builder-Integration zur Zielgruppen-Einschränkung |
| Vorschau | Test mit ausgewählten Produkten |

### Merkzettel
- Aktivierbar: Herzchen-Icon neben Account-Menü für Produktmerkliste

---

## Produkte (Produktlisteneinstellungen)

**Pfad:** Einstellungen > Allgemein > Produkte

### Standard-Verkaufskanal
Automatische Zuweisung neu erstellter Produkte zu konfigurierten Verkaufskanälen.

### Produkt-Bereich (global oder pro Verkaufskanal)
| Option | Beschreibung |
|---|---|
| Kaufen-Button in Listings | Add-to-Cart oder Details-Button anzeigen |
| Videos in Produkt-Listings | Videowiedergabe als Produktcover |
| Produkte nach Abverkauf ausblenden | Lagerbestand 0 → nicht sichtbar |
| Variantenoptionen in Suchvorschlägen | Details zu Varianten in Suchvorschlägen |
| Bewertungen anzeigen | Durchschnittliche Sternbewertungen im Listing |
| Anzahl Bewertungen pro Seite | Paginierungseinstellung für Bewertungen |
| Filteroptionen ohne Ergebnisse deaktivieren | Filter ohne Treffer deaktivieren |
| Produkte als neu markieren | Anzahl Tage nach Erstellung |
| Anzahl Produkte pro Seite | Standard-Paginierung |
| Standard-Sortierung | Vordefinierte Sortierung für Kategorien |
| Standard-Sortierung Suchergebnisse | Vordefinierte Sortierung für Suchergebnisse |

### Sortier-Optionen verwalten
Benutzerdefinierte Sortieroptionen anlegen:
- Name + technischer Name (eindeutig)
- Aktivierungsstatus
- Sortierkriterium (Datum, Bestand, Produktname, usw.)
- Sortierrichtung (aufsteigend/absteigend)
- Priorität (Frontend-Reihenfolge)

---

## Newsletter-Konfiguration

**Pfad:** Einstellungen > Shop > Newsletter

> Shopware hat keine native Newsletter-Versandfunktion. Es werden Schnittstellen für externe Tools bereitgestellt.

### Double-Opt-In Konfiguration
| Feld | Beschreibung |
|---|---|
| Verkaufskanal | Spezifisch oder global |
| Anmelde-URL | URL für Bestätigungslink |
| Double Opt-In | Aktivierungsschalter |
| Double Opt-In für registrierte Kunden | Separate Option |
| Double Opt-In Domain | Custom-Domain oder Verkaufskanal-Domain |

### E-Mail-Empfänger
Interne E-Mails für Template-Zustellung; Kunden erhalten Templates nur, wenn keine internen Empfänger konfiguriert sind.

### Newsletter-Formular erstellen
1. Erlebniswelten > neues Layout (Shopseite, „Volle Breite")
2. Formular-Block per Drag-and-Drop hinzufügen
3. Formulartyp auf „Newsletter" setzen
4. Im Service-Menü als Kategorie verlinken

---

## Tags

**Pfad:** Einstellungen > Allgemein > Tags

Tags sind Schlagwörter für Produkte, Kategorien, Medien, Kunden, Bestellungen, Versandarten, Newsletter-Empfänger, Landingpages und Regeln.

### Funktionen
- Suche und Filterung nach Duplikaten, unbenutzten Tags, Entitäten
- Tag erstellen (Name + Zuweisungen zu Entitäten)
- Im Rule Builder als Filterbedingung verwendbar

### Anwendungsbeispiele
- Produkte für Google Shopping hervorheben
- Flow-Builder-Automatisierungen mit Tags anstoßen
- Dynamische Produktgruppen per Tag filtern

---

## Maßeinheiten & Maßeinheitensystem

### Produkteinheiten
**Pfad:** Einstellungen > Allgemein > Produkteinheiten

- Eigene Einheiten anlegen (z.B. Flaschen, Paare)
- Kurzform wird standardmäßig nicht im Frontend angezeigt
- Integration via Twig: `{{ product.unit.shortCode }}`
- Verwendbar in Produkt-Feeds (Google Shopping)

### Maßeinheitensystem
**Pfad:** Einstellungen > Allgemein > Maßeinheitensystem  
**Verfügbar ab:** 6.7.1.0

| Einstellung | Optionen |
|---|---|
| Einheitensystem | Metrisch oder Angloamerikanisch |
| Längeneinheit | Millimeter, Zentimeter, Meter |
| Gewichtseinheit | Gramm, Kilogramm |

Beeinflusst Darstellung von Produktmaßen in Verkaufskanälen.

---

## Dokumente

**Pfad:** Einstellungen > Handel > Dokumente

### Standard-Dokumenttypen
- Rechnung, Lieferschein, Gutschrift, Stornorechnung

### Hauptkonfigurationsbereiche
| Bereich | Einstellungen |
|---|---|
| Zuweisung | Dokumententyp (nur bei eigenen Vorlagen änderbar) |
| Einstellungen | Name, Logo, Dateinamenpräfix/-suffix, Seitenausrichtung (Portrait/Landscape), Format (A4), Positionen/Seite, PDF und/oder HTML, Kopf-/Fußzeile, Seitennummerierung |
| Bestellpositionen | Anzeige, Nummerierung |
| Preisanzeige | MwSt., Einzelpreis, Gesamtpreis |
| Frontend-Sichtbarkeit | Im „Mein Konto"-Bereich sichtbar |
| Lieferadresse | Bei Abweichung anzeigen (nur Rechnung) |
| Geschäftseinstellungen | Adresse, Name, E-Mail, Telefon, Website, Steuernummer, Finanzamt, USt-ID, IBAN/BIC, Gerichtsstand, Handelsregister, Erfüllungsort, Geschäftsführer, Zahlungsfälligkeit |

---

## Wesentliche Merkmale

**Pfad:** Einstellungen > Shop > Wesentliche Merkmale  
**Verfügbar ab:** 6.3.1

Ermöglicht die Anzeige produktrelevanter Infos (Grundpreis, Herstellernummer, EAN, Eigenschaften) im Checkout.

### Workflow
1. Template erstellen: Name, Beschreibung, Felder hinzufügen (Grundpreisberechnung, Eigenschaften, Produktinfos)
2. Reihenfolge per Pfeiltasten anpassen
3. Template im Produkt zuweisen (Reiter „Wesentliche Merkmale")
4. Anzeige im Checkout wenn: Template zugewiesen UND Daten beim Produkt gepflegt

---

## Zusatzfelder (Custom Fields)

**Pfad:** Einstellungen > System > Zusatzfelder

### Sets erstellen
- Technischer Name (eindeutig, unveränderbar nach Erstellung)
- Position (numerisch, höhere Zahl = weiter hinten)
- Label (übersetzbar)
- Programmbereiche zuweisen (Produkte, Kategorien, Kunden, …)

> Tipp: Keine TWIG-Sonderzeichen (Bindestriche, Rauten) im technischen Namen – kann Exporte brechen.

### Feldtypen
| Typ | Beschreibung |
|---|---|
| Auswahl | Einzelne oder mehrere vordef. Optionen |
| Objektauswahl | Verweis auf bestehende Daten (Produkte, Länder, …) |
| Textfeld | Einzeiliger Text |
| Datei (Medium) | Mediendatei-Anhang |
| Zahl | Numerisch (Integer oder Dezimal, mit Min/Max/Step) |
| Datum/Zeit | Datumsauswahl |
| Checkbox | Boolean |
| Aktiv/Inaktiv Schalter | Backend-Boolean (0/1) |
| Text Editor | Rich-Text-Editor |
| Farbauswahl | HEX-Farbpicker |

### Storefront API-Hinweis
Wenn „Über Store-API änderbar" aktiv: Feld ist öffentlich zugänglich. Keine sensiblen Daten!

### Erlebniswelten-Integration
Text-Block im Experience-World-Editor → Daten-Mapping → Zusatzfeld auswählen → speichern.

### Verwendung in E-Mail-Templates
Syntax: `{{customer.customFields.FeldName}}`
