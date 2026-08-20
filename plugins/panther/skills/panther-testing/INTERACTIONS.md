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

- [INTERACTIONS-DETAIL.md](INTERACTIONS-DETAIL.md) — Vollstandige Form/Field/Mouse/Keyboard-Signaturen, Drag & Drop, alle WebDriverKeys-Konstanten, Beispiele
