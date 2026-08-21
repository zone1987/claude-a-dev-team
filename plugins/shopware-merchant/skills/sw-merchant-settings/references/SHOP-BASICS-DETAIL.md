# Shopware 6 – basic shop settings – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/shop

---

## Contents

- [Stammdaten](#stammdaten)
- [Adressen](#adressen)
- [Anreden](#anreden)
- [Kundengruppen](#kundengruppen)
- [Nummernkreise](#nummernkreise)
- [Anmeldung & Registrierung](#anmeldung--registrierung)
- [Warenkorb](#warenkorb)
- [Produkte (product listing settings)](#produkte-product-listing-settings)
- [Newsletter configuration](#newsletter-configuration)
- [Tags](#tags)
- [Maßeinheiten & Maßeinheitensystem](#maßeinheiten--maßeinheitensystem)
- [Dokumente](#dokumente)
- [Wesentliche Merkmale](#wesentliche-merkmale)
- [Zusatzfelder (Custom Fields)](#zusatzfelder-custom-fields)

## Stammdaten

**Path:** Einstellungen (Settings) > Shop > Stammdaten (Master data)  
**Configurable:** globally or per sales channel

### 1. Shop information
| Field | Description |
|---|---|
| Shopname (Shop name) | Public title of the shop in the frontend |
| Shopbetreiber-E-Mail (Shop owner email) | Contact email of the shop operator |
| Meta-Author | Author name for meta tags (SEO) |
| Familienfreundlicher Shop (Family-friendly shop) | Marks the shop as suitable for minors |
| Shopbetreiber-Adresse (Shop owner address) | Business address for the imprint and invoices |
| IBAN / BIC / Kontoinhaber (Account holder) | Bank details for the checkout and invoices |

### 2. Shop pages
Links static content layouts to legally required pages:
- Terms and conditions, right of withdrawal, shipping and payment methods
- Privacy policy, imprint, 404 error page
- Maintenance page, contact page, withdrawal form page, newsletter page

### 3. Law and data protection
| Option | Description |
|---|---|
| Cookie-Banner | Activates the default cookie notice |
| "Alle akzeptieren" (Accept all) button | Optional quick-accept button in the cookie banner |
| Contact form mandatory fields | First name, last name, phone number can be made mandatory |
| Withdrawal button in the footer | Optionally display "Vertrag widerrufen" (Withdraw from contract) |

### 4. robots.txt rules
- Allow/disallow directives for search engine crawlers
- Domain-specific configuration is possible

### 5. CAPTCHA options
| Variant | Description |
|---|---|
| Honeypot | Invisible field for bot detection |
| Einfaches Captcha (Simple captcha) | Image with a distorted letter/number combination |
| Google reCAPTCHA v2 | "I am not a robot" checkbox (with an optional image puzzle) |
| Google reCAPTCHA v3 | Automatic verification via a score (0–1) |
| Friendly Captcha | Blockchain-based, GDPR-compliant (paid) |

### 6. Meta robots tag
Default robots meta tag for the entire shop (index/noindex etc.)

---

## Adressen

**Path:** Einstellungen > Shop > Adressen (Addresses)  
**Note:** from Shopware 6.6.x display options were adjusted and partly removed.

- Configuration: postcode before or after the city name
- Configurable per sales channel
- Affects the address display in the storefront customer account
- Valid for versions 6.1.0–6.5.8.x

---

## Anreden

**Path:** Einstellungen > Customer > Anreden (Salutations)

- Salutations are preconfigured by default with formal letter versions
- **Technischer Name** (Technical name): mandatory field (used among other things at order completion)
- Two fallback salutations with the technical names `not_specified` and `undefined`

### Actions
| Action | Description |
|---|---|
| Create a new salutation | Name, technical name, formal letter version |
| Edit a salutation | Via the context menu |
| Delete a salutation | Via the context menu |

---

## Kundengruppen

**Path:** Einstellungen > Kundengruppen (Customer groups)

> **Critical:** The "Standard-Kundengruppe" (Default customer group) has a fixed UUID and cannot be deleted. If deleted, the frontend can no longer be reached.

### Fields when creating
| Field | Description |
|---|---|
| Name | Label of the customer group |
| Steuerdarstellung (Tax display) | Gross or net price display for this group |
| Eigenes Registrierungsformular (Own registration form) | Can optionally be activated |

### Customer group registration
- Form configuration: title, introductory text, SEO meta description
- Option: registration form for companies (company, department, VAT ID)
- The technical URL is generated after saving
- Must be assigned to at least one sales channel

### B2B components (Commercial, from plan Evolve)
- Employee management, quick orders, quote management, order approval

### Workflow
1. The customer registers via the customer group's own form
2. The admin accepts or rejects in the customer details
3. The customer receives an email notification

---

## Nummernkreise

**Path:** Einstellungen > Allgemein (General) > Nummernkreise (Number ranges)

Creates unique series of character/number combinations for orders, customers and documents.

### Fields
| Field | Description |
|---|---|
| Name / Beschreibung (Description) | Identification in the administration |
| Präfix (Prefix) | Character string before the number |
| Startnummer (Start number) | Starting number of the range |
| Suffix | Character string after the number |
| Erweitert (Advanced) | Pattern-based number assignment (e.g. `Order{n}-{date}`) |
| Aktuelle Nummer (Current number) | Last assigned number (read-only) |
| Vorschau (Preview) | Example output |
| Zuweisung (Assignment) | Purpose + sales channel binding |

### Available number range types
- Orders, invoices, credit notes, cancellation invoices, cancellations
- Delivery notes, returns, partial cancellations
- Customers, products
- Subscription numbers (Abonnements feature)
- Quotes, Quote, Pending Order (B2B)

---

## Anmeldung & Registrierung

**Path:** Einstellungen > Kunde (Customer) > Anmeldung & Registrierung (Login & registration)

### Password settings
| Option | Description |
|---|---|
| Passwort-Mindestlänge (Minimum password length) | Minimum number of characters |
| Passwort zweimal eingeben (Enter password twice) | Confirmation by repetition |

### Account type options
- Default: choose between a customer account or a guest order
- Show a choice between business and private account

### Data protection & data
- Store customer IP addresses in plain text (or anonymise them)
- Data protection checkbox as a mandatory field

### Personal data (display / mandatory field)
- Salutation, title, phone number, birthday
- Enter the email address twice

### Double opt-in
- Can be activated separately for registrations and guest orders
- Confirmation URL is configurable
- The double opt-in domain can be adjusted

### Address fields
- Additional address line 1 & 2 configurable
- The order of city, postcode, federal state can be chosen

### Other options
- Clear the cart on logout
- Allow customers to delete their own account
- Time until guest accounts expire (in seconds)
- Password recovery URL

---

## Warenkorb

**Path:** Einstellungen > Allgemein > Warenkorb (Cart)

### Cart configuration
| Option | Description |
|---|---|
| Maximale Auswahlmenge (Maximum selectable quantity) | Number of products in the quantity dropdown (can be overridden per product) |
| Lieferzeit anzeigen (Show delivery time) | Delivery time in the cart taken from the item |
| Stornierungen erlauben (Allow cancellations) | Customers may cancel orders in their account |
| Payment-Token Gültigkeit (Payment token validity) | Time limit in minutes for completing payment (default: 60 min) |
| API Rate Limiting | Max. products per minute via the API (brute force protection) |
| Summenspalte anzeigen (Show totals column) | Show/hide the totals column in the cart |
| Steuerspalte im Checkout (Tax column in the checkout) | Show VAT instead of the unit price |

### Order completion
| Option | Description |
|---|---|
| Kommentarfeld (Comment field) | Activates customer remarks when ordering |
| Gastkunden-Logout (Guest customer logout) | Automatic logout after order completion |

### AI-generated order completion message (from plan Rise)
| Field | Description |
|---|---|
| Tonfall (Tone) | Neutral, animated or humorous |
| Zeichenzahl (Character count) | Guide value for the text length |
| Verfügbarkeitsregel (Availability rule) | Rule Builder integration for restricting the target group |
| Vorschau (Preview) | Test with selected products |

### Wish list
- Can be activated: heart icon next to the account menu for a product wish list

---

## Produkte (product listing settings)

**Path:** Einstellungen > Allgemein > Produkte (Products)

### Default sales channel
Automatic assignment of newly created products to the configured sales channels.

### Product area (global or per sales channel)
| Option | Description |
|---|---|
| Kaufen-Button in Listings (Buy button in listings) | Show an add-to-cart or a details button |
| Videos in Produkt-Listings (Videos in product listings) | Video playback as the product cover |
| Produkte nach Abverkauf ausblenden (Hide products when sold out) | Stock 0 → not visible |
| Variantenoptionen in Suchvorschlägen (Variant options in search suggestions) | Details about variants in search suggestions |
| Bewertungen anzeigen (Show reviews) | Average star ratings in the listing |
| Anzahl Bewertungen pro Seite (Number of reviews per page) | Pagination setting for reviews |
| Filteroptionen ohne Ergebnisse deaktivieren (Disable filter options without results) | Disables filters without hits |
| Produkte als neu markieren (Mark products as new) | Number of days after creation |
| Anzahl Produkte pro Seite (Number of products per page) | Default pagination |
| Standard-Sortierung (Default sorting) | Predefined sorting for categories |
| Standard-Sortierung Suchergebnisse (Default sorting for search results) | Predefined sorting for search results |

### Managing sorting options
Create custom sorting options:
- Name + technical name (unique)
- Activation status
- Sorting criterion (date, stock, product name, etc.)
- Sorting direction (ascending/descending)
- Priorität (Priority) (frontend order)

---

## Newsletter configuration

**Path:** Einstellungen > Shop > Newsletter

> Shopware has no native newsletter dispatch function. Interfaces for external tools are provided instead.

### Double opt-in configuration
| Field | Description |
|---|---|
| Verkaufskanal (Sales channel) | Specific or global |
| Anmelde-URL (Registration URL) | URL for the confirmation link |
| Double Opt-In | Activation switch |
| Double Opt-In für registrierte Kunden (for registered customers) | Separate option |
| Double Opt-In Domain | Custom domain or sales channel domain |

### Email recipients
Internal emails for template delivery; customers only receive templates if no internal recipients are configured.

### Creating a newsletter form
1. Erlebniswelten (Shopping Experiences) > new layout (shop page, "Volle Breite" (Full width))
2. Add a form block via drag and drop
3. Set the form type to "Newsletter"
4. Link it as a category in the service menu

---

## Tags

**Path:** Einstellungen > Allgemein > Tags

Tags are keywords for products, categories, media, customers, orders, shipping methods, newsletter recipients, landing pages and rules.

### Functions
- Search and filter by duplicates, unused tags, entities
- Create a tag (name + assignments to entities)
- Usable in the Rule Builder as a filter condition

### Application examples
- Highlight products for Google Shopping
- Trigger Flow Builder automations with tags
- Filter dynamic product groups by tag

---

## Maßeinheiten & Maßeinheitensystem

### Product units
**Path:** Einstellungen > Allgemein > Produkteinheiten (Product units)

- Create your own units (e.g. bottles, pairs)
- The short form is not displayed in the frontend by default
- Integration via Twig: `{{ product.unit.shortCode }}`
- Usable in product feeds (Google Shopping)

### Unit system
**Path:** Einstellungen > Allgemein > Maßeinheitensystem (Unit system)  
**Available from:** 6.7.1.0

| Setting | Options |
|---|---|
| Einheitensystem (Unit system) | Metric or Anglo-American |
| Längeneinheit (Length unit) | Millimetres, centimetres, metres |
| Gewichtseinheit (Weight unit) | Grams, kilograms |

Affects how product dimensions are presented in the sales channels.

---

## Dokumente

**Path:** Einstellungen > Handel (Commerce) > Dokumente (Documents)

### Default document types
- Invoice, delivery note, credit note, cancellation invoice

### Main configuration areas
| Area | Settings |
|---|---|
| Zuweisung (Assignment) | Document type (only changeable for your own templates) |
| Einstellungen (Settings) | Name, logo, file name prefix/suffix, page orientation (portrait/landscape), format (A4), line items per page, PDF and/or HTML, header/footer, page numbering |
| Bestellpositionen (Order line items) | Display, numbering |
| Preisanzeige (Price display) | VAT, unit price, total price |
| Frontend-Sichtbarkeit (Frontend visibility) | Visible in the "Mein Konto" (My account) area |
| Lieferadresse (Delivery address) | Show if it differs (invoice only) |
| Geschäftseinstellungen (Business settings) | Address, name, email, phone, website, tax number, tax office, VAT ID, IBAN/BIC, place of jurisdiction, commercial register, place of performance, managing director, payment due date |

---

## Wesentliche Merkmale

**Path:** Einstellungen > Shop > Wesentliche Merkmale (Essential characteristics)  
**Available from:** 6.3.1

Allows product-relevant information (base price, manufacturer number, EAN, properties) to be displayed in the checkout.

### Workflow
1. Create a template: name, description, add fields (base price calculation, properties, product information)
2. Adjust the order using the arrow keys
3. Assign the template in the product (tab "Wesentliche Merkmale")
4. Displayed in the checkout when: a template is assigned AND the data is maintained on the product

---

## Zusatzfelder (Custom Fields)

**Path:** Einstellungen > System > Zusatzfelder (Custom fields)

### Creating sets
- Technical name (unique, cannot be changed after creation)
- Position (numeric, a higher number = further back)
- Label (translatable)
- Assign program areas (products, categories, customers, …)

> Tip: no TWIG special characters (hyphens, hash signs) in the technical name – this can break exports.

### Field types
| Type | Description |
|---|---|
| Auswahl (Selection) | One or several predefined options |
| Objektauswahl (Object selection) | Reference to existing data (products, countries, …) |
| Textfeld (Text field) | Single-line text |
| Datei (Medium) (File/media) | Media file attachment |
| Zahl (Number) | Numeric (integer or decimal, with min/max/step) |
| Datum/Zeit (Date/time) | Date selection |
| Checkbox | Boolean |
| Aktiv/Inaktiv Schalter (Active/inactive switch) | Backend boolean (0/1) |
| Text Editor | Rich text editor |
| Farbauswahl (Colour picker) | HEX colour picker |

### Storefront API note
If "Über Store-API änderbar" (Changeable via Store API) is active: the field is publicly accessible. No sensitive data!

### Shopping Experiences integration
Text block in the Shopping Experiences editor → data mapping → select the custom field → save.

### Use in email templates
Syntax: `{{customer.customFields.FeldName}}`
