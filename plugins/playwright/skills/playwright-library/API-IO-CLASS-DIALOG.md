# Playwright — class: Dialog

> **Manifest:** 6 methods, 0 properties, 0 events.
> Represents browser dialogs (alert, confirm, prompt, beforeunload).
> Instances are obtained via the `page.on('dialog')` event.

---

## Contents

- [Overview](#overview)
- [Methods](#methods)
- [Important notes](#important-notes)
- [Properties](#properties)
- [Events](#events)
- [Manifest](#manifest)

## Overview

`Dialog` encapsulates native browser dialogs. Without a registered
`dialog` handler, dialogs are dismissed automatically (Chromium/WebKit)
or may block the page. The handler must call `accept()` or
`dismiss()`, otherwise the page hangs.

```javascript
page.on('dialog', async dialog => {
  console.log(dialog.type(), dialog.message());
  await dialog.accept();
});
```

---

## Methods

### dialog.accept(promptText?)

Accepts the dialog. For `prompt` dialogs a text value can optionally
be passed.

**Signature:**
```typescript
dialog.accept(promptText?: string): Promise<void>
```

**Parameters:**

| Name | Type | Required | Default | Description |
|------|-----|---------|---------|--------------|
| `promptText` | `string` | no | `""` | Text that is entered into a prompt input field. Has no effect for `alert`, `confirm`, `beforeunload`. |

**Returns:** `Promise<void>`

**Example:**
```javascript
page.on('dialog', async dialog => {
  if (dialog.type() === 'prompt') {
    await dialog.accept('My name');
  } else {
    await dialog.accept();
  }
});
```

---

### dialog.dismiss()

Dismisses the dialog (equivalent to "Cancel" / "OK not chosen").

**Signature:**
```typescript
dialog.dismiss(): Promise<void>
```

**Parameters:** None

**Returns:** `Promise<void>`

**Example:**
```javascript
page.on('dialog', async dialog => {
  await dialog.dismiss();
});
```

---

### dialog.message()

Returns the text displayed in the dialog.

**Signature:**
```typescript
dialog.message(): string
```

**Parameters:** None

**Returns:** `string` — the message text of the dialog

**Example:**
```javascript
page.on('dialog', dialog => {
  console.log('Dialog text:', dialog.message());
});
```

---

### dialog.defaultValue()

Returns the pre-filled value of a `prompt` dialog.
For all other dialog types `""` is returned.

**Signature:**
```typescript
dialog.defaultValue(): string
```

**Parameters:** None

**Returns:** `string` — pre-filled prompt value or empty string

**Example:**
```javascript
page.on('dialog', async dialog => {
  console.log('Default:', dialog.defaultValue()); // e.g. "John Doe"
  await dialog.accept(dialog.defaultValue());
});
```

---

### dialog.type()

Returns the type of the dialog.

**Signature:**
```typescript
dialog.type(): string
```

**Parameters:** None

**Returns:** `'alert' | 'beforeunload' | 'confirm' | 'prompt'`

| Value | Description |
|------|--------------|
| `'alert'` | `window.alert()` — OK button only |
| `'confirm'` | `window.confirm()` — OK and Cancel |
| `'prompt'` | `window.prompt()` — text input |
| `'beforeunload'` | `beforeunload` event dialog — confirm leaving |

**Example:**
```javascript
page.on('dialog', async dialog => {
  switch (dialog.type()) {
    case 'alert':
      await dialog.accept();
      break;
    case 'confirm':
      await dialog.dismiss();
      break;
    case 'prompt':
      await dialog.accept('Answer');
      break;
  }
});
```

---

### dialog.page()

Returns the page that triggered the dialog.

**Signature:**
```typescript
dialog.page(): Page | null
```

**Parameters:** None

**Returns:** `Page | null` — the triggering page, or `null` if it cannot be determined

**Example:**
```javascript
page.on('dialog', dialog => {
  const origin = dialog.page();
  if (origin) {
    console.log('Dialog from:', origin.url());
  }
});
```

---

## Important notes

- **Automatic dismissal:** Without a handler, dialogs are dismissed
  automatically. This can cause `confirm()` to return `false`
  and page logic to branch accordingly.
- **Blocking:** The handler must always call `accept()` or `dismiss()`
  — otherwise the browser waits forever.
- **Async handlers:** The event handler may be `async`; Playwright waits
  for it to resolve.

---

## Properties

No public properties.

## Events

No own events on the Dialog object. Dialog instances are received via
`page.on('dialog')`.

---

## Manifest

| Category | Count |
|-----------|--------|
| Methods  | 6      |
| Properties | 0     |
| Events    | 0      |

**Conclusion:** `type()` and `message()` read the dialog out; `accept()`/`dismiss()`
close it. `defaultValue()` is only relevant for prompts. `page()` helps
in multi-page scenarios to map the dialog to its source.

---

*Source: https://playwright.dev/docs/api/class-dialog*
