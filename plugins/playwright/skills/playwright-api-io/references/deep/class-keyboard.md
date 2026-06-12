# Playwright — class: Keyboard

> **Manifest:** 5 Methoden, 0 Properties, 0 Events.
> Bietet vollstandige Tastatursteuerung uber keydown/keyup/press/type/insertText.
> Modifier-Kombinationen wie `Control+A` werden nativ unterstuetzt.
> Zugriff: `page.keyboard`.

---

## Uebersicht

`Keyboard` steuert die virtuelle Tastatur des Browsers. Alle Koordinaten arbeiten
im Kontext des aktiven Fokus-Elements. Die Instanz ist ueber `page.keyboard`
erreichbar und nicht direkt instanziierbar.

---

## Methoden

### keyboard.down(key)

Sendet ein `keydown`-Event fuer den angegebenen Key.

**Signatur:**
```typescript
keyboard.down(key: string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `key` | `string` | ja | — | Key-Name oder einzelnes Zeichen, z.B. `"ArrowLeft"`, `"a"`, `"F5"` |

**Unterstuetzte Keys (Auswahl):**
F1–F12, Digit0–Digit9, KeyA–KeyZ, Backquote, Minus, Equal, Backslash,
Backspace, Tab, Delete, Escape, ArrowLeft, ArrowRight, ArrowUp, ArrowDown,
End, Enter, Home, Insert, PageDown, PageUp, Space,
Shift, Control, Alt, Meta, ShiftLeft, ControlOrMeta

`ControlOrMeta` loest sich automatisch zu `Control` (Windows/Linux) oder
`Meta` (macOS) auf.

**Rueckgabe:** `Promise<void>`

**Hinweise:**
- Modifier-Keys (Shift, Control usw.) beeinflussen den Zeichencase
  nachfolgender `type()`-Aufrufe.
- Wiederholtes `down()` ohne zwischengeschaltetes `up()` setzt `repeat: true`.

**Beispiel:**
```javascript
// Shift druecken, dann Buchstabe A tippen (Grossbuchstabe), dann Shift loslassen
await page.keyboard.down('Shift');
await page.keyboard.press('KeyA');
await page.keyboard.up('Shift');
```

---

### keyboard.up(key)

Sendet ein `keyup`-Event fuer den angegebenen Key.

**Signatur:**
```typescript
keyboard.up(key: string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `key` | `string` | ja | — | Key-Name oder Zeichen; gleiche Werte wie bei `down()` |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.keyboard.up('Shift');
```

---

### keyboard.press(key, options?)

Kombination aus `down()` und `up()`. Sendet keydown, wartet optional, sendet keyup.

**Signatur:**
```typescript
keyboard.press(key: string, options?: {
  delay?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `key` | `string` | ja | — | Key-Name oder Zeichen. Shortcuts wie `"Control+o"`, `"Shift+T"`, `"ControlOrMeta+A"` moeglich |
| `options.delay` | `number` | nein | `0` | Millisekunden zwischen keydown und keyup |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
// Einzelne Taste
await page.keyboard.press('ArrowLeft');

// Shortcut
await page.keyboard.press('Control+a');

// Mit Verzoegerung
await page.keyboard.press('Enter', { delay: 50 });
```

---

### keyboard.type(text, options?)

Sendet fuer jedes Zeichen des Strings `keydown`, `keypress`/`input` und `keyup`.

**Signatur:**
```typescript
keyboard.type(text: string, options?: {
  delay?: number;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `text` | `string` | ja | — | Text, der Zeichen fuer Zeichen eingetippt wird |
| `options.delay` | `number` | nein | `0` | Millisekunden zwischen aufeinanderfolgenden Tastendruecken |

**Rueckgabe:** `Promise<void>`

**Hinweise:**
- Modifier-Keys beeinflussen den Case **nicht** — `type()` ist unabhaengig
  vom aktuellen Shift/Caps-Zustand.
- Fuer Nicht-US-Zeichen (z.B. Umlaute) wird nur das `input`-Event gefeuert,
  kein `keydown`/`keyup`.

**Beispiel:**
```javascript
await page.keyboard.type('Hello, World!');
await page.keyboard.type('Langsam', { delay: 100 });
```

---

### keyboard.insertText(text)

Sendet ausschliesslich ein `input`-Event — kein `keydown`, kein `keypress`,
kein `keyup`.

**Signatur:**
```typescript
keyboard.insertText(text: string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `text` | `string` | ja | — | Text, der direkt als Input-Event eingefuegt wird |

**Rueckgabe:** `Promise<void>`

**Hinweise:**
- Geeignet fuer Zeichen, die keine eigene Key-Entsprechung haben (z.B. Emoji,
  CJK-Zeichen).
- Modifier-Keys haben keinen Effekt.

**Beispiel:**
```javascript
await page.keyboard.insertText('嗨');
await page.keyboard.insertText('🎉');
```

---

## Properties

Keine offentlichen Properties.

## Events

Keine eigenen Events — Keyboard-Interaktionen loesen Events auf den Seiten-
Elementen aus, nicht auf dem Keyboard-Objekt selbst.

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 5      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** Die Klasse deckt die gesamte low-level Tastatureingabe ab. `press()`
und `type()` sind die Allzweck-Methoden; `down()`/`up()` werden benoetigt, wenn
Modifier-Keys waehrend anderer Aktionen gehalten werden sollen. `insertText()`
ist die effizienteste Option fuer reine Text-Eingabe ohne Event-Overhead.

---

*Quelle: https://playwright.dev/docs/api/class-keyboard*
