# Contao 5.x – Formulargenerator (Form Generator)

Complete reference from the Contao 5.x manual (German).

---

## Contents

- [1. Configuring forms](#1-configuring-forms)
- [2. Form fields](#2-form-fields)
- [3. Creating a search form (tutorial)](#3-creating-a-search-form-tutorial)

## 1. Configuring forms

The Formulargenerator (Form Generator) is located in the backend under **Inhalte** (Content). Forms can send data by e-mail or store it in the database. Validation is performed automatically based on predefined rules.

### Title and redirect

| Setting | Description |
|-------------|-------------|
| **Titel** (Title) | Visible in the backend only |
| **Formular-Alias** (Form alias) | Unique reference as an alternative to the numeric form ID |
| **Weiterleitungsseite** (Redirect page) | Target page after submission (confirmation page) |

### Form configuration

| Option | Description |
|--------|-------------|
| **HTML-Tags erlauben** (Allow HTML tags) | Allows HTML input in fields with configurable tags |
| **Per Ajax senden** (Send via Ajax) | No redirect; confirmation message; uses Simple Tokens (as of Contao 5.1) |

### Sending form data (e-mail)

Data is sent by e-mail to one or more recipients. File fields are automatically attached.

| Setting | Description |
|-------------|-------------|
| **Per E-Mail versenden** (Send via e-mail) | Enables e-mail dispatch |
| **Empfänger-Adresse** (Recipient address) | Comma-separated list of e-mail addresses |
| **Betreff** (Subject) | E-mail subject line |
| **Datenformat** (Data format) | Raw data, XML, CSV, CSV (Excel) or e-mail format |
| **Leere Felder auslassen** (Skip empty fields) | Send only fields that were filled in |

**Data formats:**
| Format | Details |
|--------|---------|
| Raw data | Unprocessed field contents one below the other |
| XML file | XML attachment with the form data |
| CSV file | CSV with the form data |
| CSV file (Excel) | CSV in Microsoft Excel format |
| E-mail | Formatted like a manual message; processes `name`, `email`, `subject`, `message` |

**Special field names:**
| Field name | Effect |
|----------|-----------|
| `email` | Is used as the reply-to address |
| `name` | Name for the reply-to address |
| `firstname` + `lastname` | Name for the reply-to (without a `name` field) |
| `cc` | This e-mail address receives a copy |

**SMTP recommendation:** without a custom SMTP server, dispatch happens via Sendmail, which can cause problems. Using the e-mail transport protocol (SMTP) is recommended.

### Storing form data (database)

| Setting | Description |
|-------------|-------------|
| **Eingaben speichern** (Store submissions) | Enables database storage |
| **Zieltabelle** (Target table) | Previously created table with identically named columns |

**Important:** field names must match the database columns exactly. Special characters such as hyphens can cause problems.

### Expert settings

| Option | Description |
|--------|-------------|
| **Übertragungsmethode** (Transmission method) | POST (default) or GET |
| **HTML5-Validierung deaktivieren** (Disable HTML5 validation) | Adds the `novalidate` attribute |
| **CSS-ID/-Klasse** (CSS ID/class) | Targeted CSS formatting |
| **Formular-ID** (Form ID) | Identifies the form for frontend modules |

---

## 2. Form fields

All fields require at least a **Feldname** (Field name) and **Feldbezeichnung** (Field label). All support CSS classes, keyboard shortcuts and a tab index.

### Erklärung (Explanation)
Rich text block for information. Generates a wrapper div with the class `widget-explanation`.

### HTML-Code
Custom HTML content without enclosing markup.

### Fieldset Anfang/Ende (Fieldset start/end)
Logical grouping of controls. Semantic `<fieldset>` element with `<legend>`.

### Textfeld (Text field)
Single-line input field.

**Validation rules:**
- Numeric, alphabetic, alphanumeric
- Date/time formats
- Phone number, e-mail validation
- URL (relative and absolute)
- Custom regex

**Additional options:**
- Placeholder text
- Help text (as of Contao 5.6)
- Min./max. input length
- Default value

### Passwortfeld (Password field)
Two-field system (password + confirmation), masked input.

### Textarea
Multi-line field. Configurable rows and columns. Identical validation to the Textfeld.

### Select-Menü (Select menu / dropdown)
- Multiple selection optional
- Configurable list size with scrolling
- JavaScript-based option editor with grouping capability
- CSS class `multiselect` when multiple selection is enabled

### Radio-Button-Menü (Radio button menu)
Single selection from several options.

### Checkbox-Menü (Checkbox menu)
Multiple selection without restriction. A hidden input field prevents an empty array being transmitted.

### Datei-Upload (File upload)
- File type whitelist (comma-separated extensions)
- File size limit (default: 2 MB)
- Image dimension check (width/height)
- Storage location configuration
- Home directory option for logged-in members
- Duplicate handling with numeric suffixes

### Range-Slider
- Minimum and maximum value
- Step size
- Default value

### Verstecktes Feld (Hidden field)
Invisible field for transmitting data without user interaction.

### Sicherheitsfrage (Security question / CAPTCHA)
- "Honeypot" technique with hidden bait fields
- Automatic spambot detection
- Mathematical fallback task in case of false positives
- Protection against data loss guaranteed

### Absendefeld (Submit field)
Button for submitting the form.
- **Textschaltfläche** (Text button, default)
- **Bildschaltfläche** (Image button) with image selection

---

## 3. Creating a search form (tutorial)

A custom search form can be created with the Formulargenerator and embedded in the header.

**Steps:**
1. Create a new form; Übertragungsmethode: **GET**; Weiterleitungsseite: the search page
2. Add a Textfeld; Feldname: `keywords`; optionally mark it as a mandatory field
3. Optional: Radio-Button-Menü; Feldname: `query_type`; option values: `and` and `or`
4. Add an Absendefeld
5. Embed the form as a frontend module in the Seitenlayout (e.g. the header)

---

Sources:
- https://docs.contao.org/5.x/manual/en/form-generator/
- https://docs.contao.org/5.x/manual/en/form-generator/forms/
- https://docs.contao.org/5.x/manual/en/form-generator/form-fields/
- https://docs.contao.org/5.x/manual/en/form-generator/create-a-search-form/
