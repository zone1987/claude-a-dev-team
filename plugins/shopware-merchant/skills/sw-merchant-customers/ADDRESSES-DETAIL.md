# Shopware 6 – Customer addresses: full reference

> Source: https://docs.shopware.com/de/shopware-6-de/kunden/uebersicht (Adressen tab)  
> Documented version: 6.7.0.0+

---

## Contents

- [1. Managing Adressen (Addresses) in the admin](#1-managing-adressen-addresses-in-the-admin)
- [2. Edit mode – addresses](#2-edit-mode-addresses)
- [3. Creating a new customer – pre-filling an address](#3-creating-a-new-customer-pre-filling-an-address)
- [4. Addresses in the storefront (customer view)](#4-addresses-in-the-storefront-customer-view)
- [5. Address fields](#5-address-fields)

## 1. Managing Adressen (Addresses) in the admin

### Access

`Kunden` (Customers) → select customer → **"Adressen"** tab

![Addresses tab in the admin](../../assets/kunden-uebersicht-adressen.png)

*(Screenshot from sw-merchant-customers/assets/kunden-uebersicht-adressen.png)*

### Elements

| No. | Element | Function |
|-----|---------|----------|
| (1) | **Standard-Lieferadresse** (Default shipping address) | Green marker; click to change |
| (2) | **Standard-Rechnungsadresse** (Default billing address) | Green marker; click to change |
| (3) | **Suche** (Search) | Filter addresses by text |
| (4) | **Neue Adresse hinzufügen** (Add new address) | Opens the creation form |
| (5) | **Context menu (⋮)** | Bearbeiten (Edit) · Duplizieren (Duplicate) · Löschen (Delete) |

### Actions in detail

#### Adding a new address

1. Click the **"Neue Adresse hinzufügen (4)"** button
2. Fill in the form (mandatory fields: first name, last name, street, postcode, city, country)
3. Save

#### Editing an address

1. Open the address's context menu **(⋮)**
2. Choose **"Bearbeiten"**
3. Make the changes and save

#### Duplicating an address

1. Open the address's context menu **(⋮)**
2. Choose **"Duplizieren"**
3. The copy appears in the list → adjust it if needed

#### Deleting an address

1. Open the address's context menu **(⋮)**
2. Choose **"Löschen"**
3. Confirm in the dialog

> Default shipping and default billing addresses cannot be deleted as long as they are marked as default.

#### Changing the default address

1. Open the context menu **(⋮)** of the desired address
2. Choose **"Als Standard-Lieferadresse setzen"** (Set as default shipping address) or **"Als Standard-Rechnungsadresse setzen"** (Set as default billing address)
3. The previous default marker is removed automatically

---

## 2. Edit mode – addresses

In the customer's **edit mode** ("Bearbeiten" button in the detail view), the **default shipping and default billing address** can likewise be changed directly.

---

## 3. Creating a new customer – pre-filling an address

When creating a new customer, a first address can be entered directly in the **"Adressen"** area.  
It is automatically set as the default shipping and default billing address.

---

## 4. Addresses in the storefront (customer view)

Customers manage addresses themselves under:  
`Mein Konto` (My account) → **"Adressen"**

Available actions:
- Add a new address
- Edit existing addresses
- Delete addresses
- Define default addresses

---

## 5. Address fields

By default, the following fields are recorded:

| Field | Mandatory |
|------|---------|
| Salutation | No |
| First name | Yes |
| Last name | Yes |
| Company | No |
| Street + house number | Yes |
| Address addition | No |
| Postcode | Yes |
| City | Yes |
| Country | Yes |
| State/region | Depends on country |
| Phone number | No |

> The mandatory fields can be adjusted via the Shopware settings.
