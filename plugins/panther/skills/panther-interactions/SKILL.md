---
name: panther-interactions
description: >
  Browser-Interaktionen in Symfony Panther: Klicken (click/clickLink), Formulare einreichen
  (submitForm/submit), Form-Objekt vollstandig (set/get/disableValidation, alle FormField-Typen:
  ChoiceFormField mit select/tick/untick/addChoice, FileFormField mit upload, InputFormField
  mit setValue, TextareaFormField), Mouse-API (clickTo/doubleClickTo/mouseMoveTo/
  contextClickTo), Keyboard-API (sendKeys/WebDriverKeys-Konstanten), Drag & Drop,
  File-Upload, JavaScript-basierte Interaktionen via executeScript.
  Browser interactions: form manipulation, Mouse API, Keyboard API, drag & drop, file upload.
  Trigger: "panther formular ausfüllen", "panther form fill", "panther click", "panther submit",
  "panther mouse", "panther keyboard", "panther drag drop", "panther file upload",
  "choiceformfield select", "formfield tick untick", "panther sendkeys", "panther interaktion",
  "panther form field", "panther input", "panther select option", "panther checkbox".
---

# Panther — Browser-Interaktionen

```php
$crawler = $client->request('GET', '/checkout');
$form = $crawler->selectButton('Bestellen')->form();
$form['email']->setValue('user@example.com');
$form['country']->select('DE');
$form['terms']->tick();
$client->submit($form);
```

## Form-Feld-Typen

| Klasse               | Methoden                                      |
|----------------------|-----------------------------------------------|
| `InputFormField`     | `setValue($val)`, `getValue()`                |
| `TextareaFormField`  | `setValue($val)`, `getValue()`                |
| `ChoiceFormField`    | `select($val)`, `tick()`, `untick()`, `getValue()`, `isDisabled()`, `addChoice($val, $select?)` |
| `FileFormField`      | `upload($path)`, `getValue()`                 |

## Mouse & Keyboard

```php
$mouse = $client->getMouse();
$mouse->clickTo('[data-x]', 10, 20);      // linksklick
$mouse->doubleClickTo('button');           // doppelklick
$mouse->contextClickTo('img');            // rechtsklick
$mouse->mouseMoveTo('#target');           // hover

$kb = $client->getKeyboard();
$kb->sendKeys(\Facebook\WebDriver\WebDriverKeys::ENTER);
```

## Vertiefung

- [references/deep/interactions.md](references/deep/interactions.md) — Vollstandige Form/Field/Mouse/Keyboard-Signaturen, Drag & Drop, alle WebDriverKeys-Konstanten, Beispiele
