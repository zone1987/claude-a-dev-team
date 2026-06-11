# Shopware 6 – E-Mail-Templates & Mailer (vollständige Referenz)

Quellen:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/e-mail-templates
- https://docs.shopware.com/de/shopware-6-de/einstellungen/mailer

---

## E-Mail-Templates

**Pfad:** Einstellungen > Inhalte > E-Mail-Templates

Templates für automatisch versendete Mails (Registrierung, Bestellbestätigung usw.) sowie zentrale Header/Footer.  
Zuweisung erfolgt über den **Flow Builder**.

---

### Editor-Struktur

| Bereich | Beschreibung |
|---|---|
| **1. Sprache** | Sprachauswahl (nur aktivierte Sprachen) |
| **2. Informationen** | Typ (vordefinierte Funktion), Beschreibung |
| **3. Optionen** | Betreff, Absendername |
| **4. Anhänge** | Dateiuploads (pro Sprache separat) |
| **5. Mail-Text** | HTML-Version + Plaintext-Version |
| **6. Tools (rechts)** | Papierflugzeug: Test-Mail; `</>`: Variablen-Library; Auge: Vorschau; Bild: Mediathek |

---

### Vordefinierte Templates (Auswahl)

| Template | Zweck |
|---|---|
| Bestellbestätigung | Bestätigung bei Bestelleingang |
| Kunden-Registrierung | Willkommensmail nach Registrierung |
| Passwort Änderungsanfrage | Recovery-Link zum Zurücksetzen |
| Newsletter Double Opt-In | Bestätigungsmail für Newsletter |
| Eintritt Lieferstatus: Versandt | Benachrichtigung bei Versand |
| Eintritt Zahlungsstatus: Bezahlt | Zahlungsbestätigung |
| Versand digitaler Produkte | Download-Link für digitale Artikel |
| Kontaktformular | Benachrichtigung für Shop-Betreiber |

---

### Header & Footer

**1. Informationen:**
- Name, Beschreibung, Verkaufskanal-Zuordnung

**3. Mail-Header:**
```html
<img src="https://meinshop.de/media/logo.png" alt="Logo" />
```

**4. Mail-Footer:**
HTML und Plaintext für Grußformeln, rechtliche Hinweise usw.

---

## Variablensystem

### Syntax
```twig
{{array.subelement.variable}}
```

Beispiel: `{{order.orderCustomer.firstName}}`

Auto-Completion: `{{` tippen → verfügbare Arrays erscheinen.

---

### Array: customer
Verfügbar in: Kundenregistrierung, Double-Opt-In, Passwort-Recovery

| Variable | Bedeutung |
|---|---|
| `customerNumber` | Kundennummer |
| `firstName` / `lastName` | Vor- und Nachname |
| `email` | E-Mail-Adresse |
| `company` | Unternehmensname |
| `birthday` | Geburtsdatum |
| `defaultPaymentMethod` | Standard-Zahlungsart |
| `defaultBillingAddress` | Rechnungsadresse (street, zipcode, city, country, …) |
| `defaultShippingAddress` | Lieferadresse |
| `salutation.displayName` | Anrede |
| `salutation.letterName` | Formale Briefanrede |

---

### Array: customerRecovery
Verfügbar in: Passwort Änderungsanfrage

| Variable | Unterelemente |
|---|---|
| `customer` | firstName, lastName, email, company, title |

---

### Array: userRecovery
Verfügbar in: Benutzer Passwort Wiederherstellung (Admin-Konten)

| Variable | Unterelemente |
|---|---|
| `user` | firstName, lastName, email, username, aclRoles |

---

### Array: newsletterRecipient
Verfügbar in: Newsletter-Registrierung, Double-Opt-In

| Variable | Bedeutung |
|---|---|
| `firstName` / `lastName` | Namen |
| `email` | Newsletter-E-Mail |
| `city` / `zipCode` / `street` | Adressdaten |

---

### Array: contactFormData
Verfügbar in: Kontaktformular

| Variable | Bedeutung |
|---|---|
| `firstName` / `lastName` | Absenderdaten |
| `email` | Kontakt-E-Mail |
| `phone` | Telefonnummer |
| `subject` / `comment` | Nachrichteninhalt |

---

### Array: order
Verfügbar in: Bestellungs- und lieferbezogene Mails

| Variable | Unterelemente | Zweck |
|---|---|---|
| `orderNumber` | — | Bestellnummer |
| `orderDateTime` | — | Zeitstempel |
| `price` | netPrice, totalPrice, taxStatus | Preisdetails |
| `shippingTotal` | — | Versandkosten |
| `orderCustomer` | (siehe customer) | Käuferdaten |
| `currency` | isoCode, symbol, shortName | Währungsinfo |
| `addresses[0]` | firstName, lastName, street, zipcode, city, country, vatID, … | Adressen |
| `deliveries[0]` | shippingOrderAddress, shippingMethod, trackingCodes | Versanddetails |
| `transactions.first` | paymentMethod, stateMachineState | Zahlungsinfo |
| `lineItems[0]` | quantity, unitPrice, totalPrice, label, payload.productNumber | Bestellpositionen |
| `stateMachineState` | name | Aktueller Bestellstatus |

---

### Array: salesChannel
Verfügbar in: Alle Standard-Templates

| Variable | Unterelemente | Zweck |
|---|---|---|
| `name` | — | Verkaufskanal-Name |
| `domains.0` | url | Domain-URL |

---

## Praktische Beispiele

### Zahlungsart-spezifischer Inhalt
```twig
{% for transactions in order.transactions %}
{% if transactions.paymentMethodId == "ID-aus-der-URL" %}
  Bitte überweise {{ order.price.totalPrice }} EUR
  auf IBAN: DEXX XX
  Referenz: {{ order.orderNumber }}
{% endif %}
{% endfor %}
```

> Die Zahlungsart-ID ist in der URL beim Bearbeiten der Zahlungsart zu finden.

### Zusatzfeld verwenden
```twig
{{customer.customFields.FeldName}}
```

---

## Mailer-Konfiguration

**Pfad:** Einstellungen > System > Mailer  
**Nur für Self-Hosted** (nicht für SaaS)

---

### 1. Lokaler E-Mail-Agent (sendmail)
| Option | Beschreibung |
|---|---|
| Versandmodus | Synchron (-bs) oder Asynchron (-t) — Synchron empfohlen |
| Versand deaktivieren | Kompletten E-Mail-Versand deaktivieren |

---

### 2. SMTP-Server (Basic Auth)
| Feld | Beschreibung |
|---|---|
| Host | SMTP-Server-Adresse |
| Port | Standard 25; AOL/Gmail: 587 |
| Benutzername / Passwort | Login-Daten (oft E-Mail-Adresse) |
| Verschlüsselung | SSL, TLS oder unverschlüsselt |
| Absender-Adresse | Fallback-Adresse |
| Empfänger-Adresse | Test-Adresse (erhält Kopie aller Mails) |
| Versand deaktivieren | Kompletter Schalter |

---

### 3. SMTP-Server mit OAuth 2 (z.B. Office 365)
| Feld | Beschreibung |
|---|---|
| OAuth URL | Token-Abruf-URL |
| OAuth Scope | Bereichsdefinition |
| Client ID | Anwendungs-ID |
| Client Secret | Authentifizierungstoken |

---

### Provider-Verbindungsdaten

| Provider | Server | Port | Verschlüsselung |
|---|---|---|---|
| 1und1/IONOS | smtp.ionos.de | 465 | SSL |
| Google Mail | smtp.gmail.com | 465 | SSL |
| HostEurope | variabel | 25/587/465 | variabel |
| Timme Hosting | — | 465 oder 587 | SSL/TLS |

---

### Konfiguration via .env
```env
MAILER_DSN=smtp://Benutzername:Password@mailserveradresse:port
```

Vollständige Dokumentation: https://symfony.com/doc/current/mailer.html
