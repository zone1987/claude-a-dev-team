# Shopware 6 – Order overview: complete reference

## Contents

- [Bestellliste (Order list)](#bestellliste-order-list)
- [Filter options](#filter-options)
- [List menu](#list-menu)
- [Bulk actions (Mehrfachänderung)](#bulk-actions-mehrfachänderung)
- [State overviews](#state-overviews)
- [Source](#source)

## Bestellliste (Order list)

The order overview is reachable under **Bestellungen** (Orders) in the administration.

![Order overview](../../assets/bestellungen-uebersicht.png)

### Elements of the list view

| Element | Description |
|---|---|
| "Bestellung anlegen" (Create order) button | Create a new manual order |
| Column dropdown | Control the visibility of individual table columns |
| Compact mode | Space-saving view of the list rows |
| Column sorting | Clicking a column heading sorts ascending/descending |
| Filter area | 15+ filter criteria, combinable |

---

## Filter options

![Filter](../../assets/bestellungen-filter.png)

The following filter criteria are available (they can be combined):

| Filter | Values / note |
|---|---|
| Affiliate-Code (Affiliate code) | Free text |
| Kampagnen-Code (Campaign code) | Free text |
| Dokumente (Documents) | With / without attachment |
| Bestelldatum (Order date) | Date range (from–to) |
| Bestellstatus (Order state) | Offen (Open), In Bearbeitung (In progress), Abgeschlossen (Completed), Storniert (Cancelled), Abgelehnt (Rejected), Ausstehende Freigabe (Pending approval) |
| Zahlungsstatus (Payment state) | 12 variants: Bezahlt (Paid), Offen, Erstattet (Refunded), Teilweise bezahlt (Partially paid), Teilweise erstattet (Partially refunded), Genehmigt (Authorised), Erinnerung zugeschickt (Reminded), Beauftragt (In progress/ordered), Fehlgeschlagen (Failed), Storniert, In Bearbeitung, Widerrufen (Chargeback) |
| Lieferstatus (Delivery state) | Geliefert (Shipped), Teilweise geliefert (Partially shipped), Offen, Teilretoure (Partial return), Retoure (Return), Storniert |
| Zahlungsart (Payment method) | Choose from the configured payment methods |
| Versandart (Shipping method) | Choose from the configured shipping methods |
| Verkaufskanal (Sales channel) | All active sales channels |
| Rechnungsland (Billing country) | Country list |
| Lieferland (Shipping country) | Country list |
| Kundengruppe (Customer group) | All customer groups that have been created |
| Tags | Order tags that have been assigned |
| Produkte (Products) | Search by the products contained |

---

## List menu

![List menu](../../assets/bestellungen-menue.png)

Via the action menu (three dots) on each row or via checkbox selection, single actions are available: open, edit or delete the order.

---

## Bulk actions (Mehrfachänderung)

![Bulk edit](../../assets/mehrfachaenderung.png)

### Selection

- Select individual orders via checkbox
- Select all visible orders via the header checkbox
- Selection across pages is possible
- **Maximum: 1,000 orders per batch**
- A selection counter is displayed
- Deselect option for selections spanning multiple pages

### Available bulk operations

#### State changes

Simultaneous change of:
- Zahlungsstatus
- Lieferstatus
- Bestellstatus

Options:
- E-mail notification to the customer (toggle)
- Send a document along (if e-mail is active)
- **"Bereits versendete Dokumente überspringen" (Skip already sent documents)**: prevents sending documents twice

> **Note:** State transitions are subject to validation rules – incompatible transitions across several orders are intercepted.

#### Creating documents in batches

| Document | Particularity |
|---|---|
| Rechnung (Invoice) | Date is mandatory; numbers are assigned automatically |
| Stornorechnung (Cancellation invoice) | Automatically references the preceding invoice number |
| Lieferschein (Delivery note) | Date + comment optional |
| Gutschrift (Credit note) | Only if credit note line items exist in the order |

- Collective PDF download is possible (the orders are merged into a single PDF)
- Duplicate check: documents that already exist are skipped

#### Controlling flow execution

Toggle **"Flows auslösen" (Trigger flows)**: prevents automation rules from being executed twice during bulk operations.

---

## State overviews

The following state diagrams show the permitted transitions:

### Bestellstatus transitions
Offen → In Bearbeitung → Abgeschlossen or Storniert

### Zahlungsstatus transitions
Offen → Bezahlt / Fehlgeschlagen / Erstattet (depending on the payment method)

### Lieferstatus transitions
Offen → Geliefert → Retoure / Teilretoure

> **Cancellation**: Only when the **Bestellstatus** is set to "Storniert" are reserved stock levels released again. Setting only the payment or delivery state to "Storniert" is not sufficient.

---

## Source
https://docs.shopware.com/de/shopware-6-de/bestellungen/uebersicht
