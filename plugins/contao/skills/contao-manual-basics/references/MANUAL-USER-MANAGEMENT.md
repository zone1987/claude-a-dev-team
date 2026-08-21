# Contao 5.x — Benutzerverwaltung (User Management)

Sources:
- https://docs.contao.org/5.x/manual/en/user-management/
- https://docs.contao.org/5.x/manual/en/user-management/users/
- https://docs.contao.org/5.x/manual/en/user-management/members/

---

## Contents

- [Overview](#overview)
- [1. Backend users](#1-backend-users)
- [2. Frontend members](#2-frontend-members)
- [3. Practical tips](#3-practical-tips)

## Overview

The Benutzerverwaltung (User Management) is its own category in the backend navigation with four modules:

| Module | Purpose |
|-------|-------|
| **Benutzer** (Users) | Backend users (editors, administrators) |
| **Benutzergruppen** (User groups) | Permission packages for backend users |
| **Mitglieder** (Members) | Frontend users (visitors with a login) |
| **Mitgliedergruppen** (Member groups) | Access groups for frontend members |

---

## 1. Backend users

### Difference between users and administrators

| Characteristic | Normal users | Administrators |
|---------|-----------------|-----------------|
| Access rights | Only explicitly granted modules | Full access to everything |
| Configuration | Via Benutzergruppen | No restrictions |
| Default rights | None (everything must be granted) | All |

**Important**: normal users have **no rights at all** by default. Everything must be granted explicitly by administrators.

### Benutzergruppen (User groups)

Benutzergruppen are collections of permissions. Individual users inherit the permissions of their groups.

**Configurable areas in Benutzergruppen:**

#### Granting backend modules

| Area | Configuration |
|---------|--------------|
| Backend modules | Which menu items are visible |
| Content elements | Which element types may be used |
| Form fields | Which field types can be used in the Formulargenerator (Form Generator) |
| Pagemounts | Which pages/page trees can be accessed |
| Filemounts | Which folders in the Dateiverwaltung (File Management) can be accessed |
| Image sizes | Which image sizes can be selected in the editor |
| Mitgliedergruppen | Which frontend groups may be assigned |

#### Special rights

| Area | Description |
|---------|-------------|
| FAQ | Grant categories |
| Archives | News archives, calendars, newsletter channels |
| Events | Calendar access |
| Newsletter | Manage distribution lists |

#### Field rights per module

For every granted module it can be defined which **individual input fields** may be edited. Fields without permission appear locked or not at all.

### Granting in two places

User rights must be configured in **two places**:
1. In the **Benutzerverwaltung**: modules, pagemounts, field rights
2. In the **Seitenstruktur** (Page Structure): access rights per page (which group may edit articles)

### User accounts — configurable settings

| Setting | Description |
|-------------|-------------|
| Benutzername (User name) | Unique login name |
| E-Mail-Adresse (E-mail address) | Contact and notifications |
| Backend-Sprache (Backend language) | Language of the backend interface |
| UI options | Theme (light/dark), shortcuts |
| Gruppen (Groups) | Membership of Benutzergruppen |
| Administrator | Full access without group restrictions |
| Two-factor authentication | TOTP (Google Authenticator, etc.) |
| Activation | Activate/deactivate on a schedule |

### Two-factor authentication (2FA)

Users can enable 2FA via their profile:
1. Click **"Sicherheit"** (Security) in the user menu
2. Scan the QR code with a TOTP app (e.g. Google Authenticator, Aegis)
3. Confirm the code
4. From now on a TOTP code is required at login

Administrators can make 2FA **mandatory** for all users.

---

## 2. Frontend members

Frontend Mitglieder (members) are visitors who can log in on the frontend. This function is **optional** — only needed if protected areas exist.

### Mitgliedergruppen (Member groups)

Members are organised into groups. Groups control:
- Access to **protected pages**
- Redirect after login (if enabled in the login module)
- Scheduled activation/deactivation

### Member data management

#### Personal data
- First name, last name
- Date of birth
- Gender

#### Address data
- Company
- Street, postcode, town
- State, country

#### Contact data
- Phone, mobile, fax
- E-mail address *(must be unique)*
- Website
- Language (for multilingual projects)

#### Login data
- User name *(must be unique)*
- Password (stored encrypted)

#### Further settings
- **Home-Verzeichnis** (Home directory): optional personal file directory
- **Mitgliedergruppen**: group membership
- **Abonnements** (Subscriptions): newsletter management
- **Kontoeinstellungen** (Account settings): activation/deactivation, can be scheduled

### Setting up protected areas

**Step by step:**

1. Create a **Mitgliedergruppe** (Benutzerverwaltung → Mitgliedergruppen)
2. Create a **Mitglied** and assign the group
3. **Protect the page** in the Seitenstruktur:
   - Edit the page → enable access protection
   - Select the permitted Mitgliedergruppen
4. Create a **login module** and embed it in the Seitenlayout (Page layout):
   - Layout → Module → New → type: "Login-Formular" (Login form)
   - Configure the redirect after login
5. Create **error pages**:
   - Type "401 Nicht authentifiziert" (401 Not authenticated) for visitors who are not logged in
   - Type "403 Zugriff verweigert" (403 Access denied) for logged-in visitors without rights

### Password reset for frontend members

Members can reset their password via a **password-forgotten module**:
- Module type: "Passwort vergessen" (Forgot password)
- Link by e-mail with a token (double opt-in)

---

## 3. Practical tips

### Administrator password forgotten

If no admin access is possible:
1. Set the `admin` value to `1` directly in the database table `tl_user`, or
2. Reset all admin flags and create a new admin in the Contao install tool:
   - URL: `https://example.com/contao/install`

Via CLI:
```bash
php vendor/bin/contao-console contao:user:create --admin
```

### Resetting a user password

```bash
php vendor/bin/contao-console contao:user:password benutzername
```

### Listing all users

```bash
php vendor/bin/contao-console contao:user:list
php vendor/bin/contao-console contao:user:list --admins
```
