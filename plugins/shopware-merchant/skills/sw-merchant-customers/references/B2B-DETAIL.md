# Shopware 6 – B2B / company accounts: Complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/kunden/uebersicht (Unternehmen tab)  
> Documented version: 6.5.6.0+  
> Prerequisite: **Shopware Evolve Plan**

---

## Contents

- [1. Overview](#1-overview)
- [2. Employee management](#2-employee-management)
- [3. Role management](#3-role-management)
- [4. Frontend view (Storefront)](#4-frontend-view-storefront)
- [5. B2B features at a glance (Evolve Plan)](#5-b2b-features-at-a-glance-evolve-plan)
- [6. Version matrix](#6-version-matrix)

## 1. Overview

The **"Unternehmen" (Companies) tab** in the customer detail view enables complete B2B management of a company account directly in the admin. Features:

- **Mitarbeiterverwaltung** (Employee management): Multiple users per company
- **Rollenverwaltung** (Role management): Define permissions for employees

---

## 2. Employee management

![Employee management](assets/b2b-mitarbeitermanagement.png)

### Inviting an employee

1. `Kunden` (Customers) → company customer detail view → tab **"Unternehmen"**
2. Click the **"Konto hinzufügen (1)"** (Add account) button
3. Fill in the form:

| Field | Required | Description |
|------|---------|-------------|
| Vorname (First name) | Yes | First name of the employee |
| Nachname (Last name) | Yes | Last name of the employee |
| E-Mail (Email) | Yes | Login email address for the employee |
| Rolle (Role) | No | Optional role assignment |

4. Send the invitation → the employee receives an email with an activation link

### Invitation details

| Parameter | Value |
|-----------|------|
| **Gültigkeitsdauer** (Validity period) | **2 hours** |
| **Status nach Versand** (Status after sending) | Shown in the employee list |
| **Neu einladen** (Invite again) | Possible if the link has expired |

### Deactivating an employee

1. Open the context menu (⋮) of the employee
2. Choose **"Deaktivieren"** (Deactivate)
3. The employee can no longer log in (the account is retained)

### Employee status overview

| Status | Meaning |
|--------|-----------|
| Ausstehend (Pending) | Invitation sent, not yet accepted |
| Aktiv (Active) | The employee has activated the account |
| Inaktiv (Inactive) | Deactivated by the admin |

---

## 3. Role management

![New role](assets/b2b-new-rolle.png)

### Creating a role

1. Tab **"Unternehmen"** → **"Rollen"** (Roles) area
2. Click the **"Rolle hinzufügen (2)"** (Add role) button
3. Fill in the form:

| Field | Required | Description |
|------|---------|-------------|
| Name (1) | Yes | Label of the role (e.g. "Einkäufer" (Buyer), "Manager") |
| Standard-Rolle (2) (Default role) | No | Assign this role automatically to new employees |
| Berechtigungen (3) (Permissions) | No | Configure access rights |

### Available permissions

| Permission | Description |
|-------------|-------------|
| **Mitarbeiterverwaltung** | Invite, edit and deactivate employees |
| **Rollenverwaltung** | Create, edit and assign roles |
| **Bestellungen** (Orders) | View and manage orders |

---

## 4. Frontend view (Storefront)

![B2B frontend](assets/b2b-frontend.png)

Employees of a company account can also use the B2B management **directly in the storefront**:

**Access:** `Konto-Icon (1)` (Account icon) in the storefront header

Available areas (identical to the admin):
- **Mitarbeiterverwaltung (2)**: Invite and manage employees
- **Rollenverwaltung (3)**: Create roles and grant permissions

The configuration is completely identical to the admin interface.

---

## 5. B2B features at a glance (Evolve Plan)

Further B2B functions that are activated via customer groups:

| Feature | Configuration | Description |
|---------|--------------|-------------|
| **Schnellbestellungen** (Quick orders) | Customer detail view → activate option | CSV upload + product number search |
| **Angebotsmanagement** (Quote management) | Kundengruppe (Customer group) → B2B options | Create/accept quotes |
| **Bestellgenehmigung** (Order approval) | Kundengruppe → B2B options | Approve orders before execution |

---

## 6. Version matrix

| Feature | Minimum version | Plan |
|---------|---------------|------|
| Unternehmen tab (basic) | 6.5.6.0 | Evolve |
| Mitarbeiterverwaltung | 6.5.6.0 | Evolve |
| Rollenverwaltung | 6.5.6.0 | Evolve |
| Schnellbestellungen | 6.5.4.0 | Evolve |
| Angebotsmanagement | 6.5.6.0 | Evolve |
