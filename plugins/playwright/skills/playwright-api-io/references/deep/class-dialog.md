# Playwright — class: Dialog

> **Manifest:** 6 Methoden, 0 Properties, 0 Events.
> Repraesentiert Browser-Dialoge (alert, confirm, prompt, beforeunload).
> Instanzen werden ueber das `page.on('dialog')`-Event erhalten.

---

## Uebersicht

`Dialog` kapselt native Browser-Dialoge. Ohne einen registrierten
`dialog`-Handler werden Dialoge automatisch abgewiesen (Chromium/WebKit)
bzw. koennen die Seite blockieren. Der Handler muss `accept()` oder
`dismiss()` aufrufen, sonst haengt die Seite.

```javascript
page.on('dialog', async dialog => {
  console.log(dialog.type(), dialog.message());
  await dialog.accept();
});
```

---

## Methoden

### dialog.accept(promptText?)

Akzeptiert den Dialog. Bei `prompt`-Dialogen kann optional ein Text-Wert
uebergeben werden.

**Signatur:**
```typescript
dialog.accept(promptText?: string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `promptText` | `string` | nein | `""` | Text, der in ein Prompt-Eingabefeld eingetragen wird. Bei `alert`, `confirm`, `beforeunload` ohne Effekt. |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
page.on('dialog', async dialog => {
  if (dialog.type() === 'prompt') {
    await dialog.accept('Mein Name');
  } else {
    await dialog.accept();
  }
});
```

---

### dialog.dismiss()

Verwirft den Dialog (entspricht "Abbrechen" / "OK nicht gewaehlt").

**Signatur:**
```typescript
dialog.dismiss(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
page.on('dialog', async dialog => {
  await dialog.dismiss();
});
```

---

### dialog.message()

Gibt den im Dialog angezeigten Text zurueck.

**Signatur:**
```typescript
dialog.message(): string
```

**Parameter:** Keine

**Rueckgabe:** `string` — der Nachrichtentext des Dialogs

**Beispiel:**
```javascript
page.on('dialog', dialog => {
  console.log('Dialog-Text:', dialog.message());
});
```

---

### dialog.defaultValue()

Gibt den vorausgefuellten Wert eines `prompt`-Dialogs zurueck.
Fuer alle anderen Dialog-Typen wird `""` zurueckgegeben.

**Signatur:**
```typescript
dialog.defaultValue(): string
```

**Parameter:** Keine

**Rueckgabe:** `string` — vorausgefuellter Prompt-Wert oder leerer String

**Beispiel:**
```javascript
page.on('dialog', async dialog => {
  console.log('Default:', dialog.defaultValue()); // z.B. "Max Mustermann"
  await dialog.accept(dialog.defaultValue());
});
```

---

### dialog.type()

Gibt den Typ des Dialogs zurueck.

**Signatur:**
```typescript
dialog.type(): string
```

**Parameter:** Keine

**Rueckgabe:** `'alert' | 'beforeunload' | 'confirm' | 'prompt'`

| Wert | Beschreibung |
|------|--------------|
| `'alert'` | `window.alert()` — nur OK-Button |
| `'confirm'` | `window.confirm()` — OK und Abbrechen |
| `'prompt'` | `window.prompt()` — Texteingabe |
| `'beforeunload'` | `beforeunload`-Event-Dialog — Verlassen bestaetigen |

**Beispiel:**
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
      await dialog.accept('Antwort');
      break;
  }
});
```

---

### dialog.page()

Gibt die Seite zurueck, die den Dialog ausgeloest hat.

**Signatur:**
```typescript
dialog.page(): Page | null
```

**Parameter:** Keine

**Rueckgabe:** `Page | null` — die ausloesende Seite, oder `null` wenn nicht bestimmbar

**Beispiel:**
```javascript
page.on('dialog', dialog => {
  const origin = dialog.page();
  if (origin) {
    console.log('Dialog von:', origin.url());
  }
});
```

---

## Wichtige Hinweise

- **Automatisches Abweisen:** Ohne Handler werden Dialoge automatisch
  abgewiesen. Dies kann dazu fuehren, dass `confirm()` `false` zurueckgibt
  und Seiten-Logik entsprechend verzweigt.
- **Blockierung:** Der Handler muss zwingend `accept()` oder `dismiss()`
  aufrufen — sonst wartet der Browser ewig.
- **Async-Handler:** Der Event-Handler kann `async` sein; Playwright wartet
  auf die Aufloesung.

---

## Properties

Keine offentlichen Properties.

## Events

Keine eigenen Events auf dem Dialog-Objekt. Dialog-Instanzen werden ueber
`page.on('dialog')` empfangen.

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 6      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `type()` und `message()` lesen den Dialog aus; `accept()`/`dismiss()`
beenden ihn. `defaultValue()` ist nur fuer Prompts relevant. `page()` hilft
in Multi-Page-Szenarien beim Zuordnen des Dialogs zur Quelle.

---

*Quelle: https://playwright.dev/docs/api/class-dialog*
