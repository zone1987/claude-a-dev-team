# Contao Hooks – Formulare

Hooks für den Formular-Generator: Felder laden, validieren, Daten verarbeiten und speichern.

---

## `compileFormFields`

**Zweck:** Wird ausgelöst, wenn die Felder eines Formulars zusammengestellt werden. Erlaubt Modifikation der Feldliste vor dem Rendern.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$fields` | Array von `\Contao\FormFieldModel`-Instanzen |
| 2 | `string` | `$formId` | Formular-Alias mit Präfix `auto_` |
| 3 | `\Contao\Form` | `$form` | Die Formular-Instanz |

**Rückgabe:** `array` – Das (ggf. modifizierte) Array von `FormFieldModel`-Instanzen.

**Zeitpunkt:** Während der Formular-Feld-Zusammenstellung beim Rendern.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Form;

#[AsHook('compileFormFields')]
class CompileFormFieldsListener
{
    public function __invoke(array $fields, string $formId, Form $form): array
    {
        // Felder dynamisch hinzufügen, entfernen oder modifizieren
        return $fields;
    }
}
```

---

## `loadFormField`

**Zweck:** Wird ausgelöst, wenn ein Formularfeld geladen wird. Erlaubt dynamische Modifikation von Widgets.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\Widget` | `$widget` | Die aktuelle Frontend-Widget-Instanz |
| 2 | `string` | `$formId` | Formular-Alias mit Präfix `auto_` |
| 3 | `array` | `$formData` | Formular-Konfiguration aus `tl_form` |
| 4 | `\Contao\Form` | `$form` | Die Formular-Instanz |

**Rückgabe:** `\Contao\Widget` – Die (ggf. modifizierte) Widget-Instanz.

**Zeitpunkt:** Beim Laden eines Formularfelds aus dem Formular-Generator.

```php
#[AsHook('loadFormField')]
class LoadFormFieldListener
{
    public function __invoke(Widget $widget, string $formId, array $formData, Form $form): Widget
    {
        if ('myForm' === $form->formID) {
            $widget->class .= ' myclass';
        }
        return $widget;
    }
}
```

---

## `prepareFormData`

**Zweck:** Wird nach der Formularübermittlung, aber **vor** der Verarbeitung ausgelöst. Ermöglicht Modifikation oder Erweiterung der Formulardaten, z.B. Hinzufügen von Dateianhängen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array&` | `$submittedData` | Benutzer-Eingaben (als Referenz) |
| 2 | `array` | `$labels` | Feld-Labels des Formulars |
| 3 | `array` | `$fields` | Formularfelder als `\Contao\Widget`-Instanzen |
| 4 | `\Contao\Form` | `$form` | Die Formular-Instanz |
| 5 | `array&` | `$files` | Dateien-Array (Contao 5.2+, als Referenz) |

**Rückgabe:** `void`

**Zeitpunkt:** Nach Übermittlung, vor weiterer Verarbeitung (E-Mail, Datenbankpersistenz etc.).

```php
#[AsHook('prepareFormData')]
class PrepareFormDataListener
{
    public function __invoke(
        array &$submittedData,
        array $labels,
        array $fields,
        Form $form,
        array &$files
    ): void {
        // Dateianhang programmatisch hinzufügen
        $files[] = [
            'name'     => 'MyFile.txt',
            'tmp_name' => '/path/to/MyFile.txt',
            'type'     => 'text/plain',
        ];
        // Zusätzliche Felder berechnen
        $submittedData['computed_deadline'] = strtotime('+1 hour');
    }
}
```

---

## `processFormData`

**Zweck:** Wird ausgelöst, nachdem ein Formular übermittelt wurde. Für eigene Verarbeitungslogik nach dem Standardablauf.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$submittedData` | Übermittelte Formulardaten |
| 2 | `array` | `$formData` | Formular-Konfiguration aus `tl_form` |
| 3 | `array\|null` | `$files` | Informationen über hochgeladene Dateien |
| 4 | `array` | `$labels` | Feld-Labels des Formulars |
| 5 | `\Contao\Form` | `$form` | Die Formular-Instanz |

**Rückgabe:** `void`

**Zeitpunkt:** Nach der vollständigen Formularverarbeitung.

```php
#[AsHook('processFormData')]
class ProcessFormDataListener
{
    public function __invoke(array $submittedData, array $formData, array|null $files, array $labels, Form $form): void
    {
        // z.B. Daten an externe API weiterleiten
    }
}
```

---

## `storeFormData`

**Zweck:** Wird ausgelöst, **bevor** übermittelte Formulardaten in der Datenbank gespeichert werden. Erlaubt Modifikation der zu speichernden Daten.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$data` | Datensatz, der gespeichert wird |
| 2 | `\Contao\Form` | `$form` | Die Formular-Instanz |

**Rückgabe:** `array` – Das (ggf. modifizierte) Datensatz-Array.

**Zeitpunkt:** Direkt vor dem Schreiben in die Datenbanktabelle.

```php
#[AsHook('storeFormData')]
class StoreFormDataListener
{
    public function __invoke(array $data, Form $form): array
    {
        // Aktuellen Frontend-Benutzer zuordnen
        $data['member'] = 0;
        $user = $this->tokenStorage->getToken()?->getUser();
        if ($user instanceof FrontendUser) {
            $data['member'] = $user->id;
        }
        return $data;
    }
}
```

---

## `validateFormField`

**Zweck:** Wird ausgelöst, wenn ein Formularfeld übermittelt wird. Ermöglicht benutzerdefinierte Validierungslogik.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\Widget` | `$widget` | Das aktuelle Frontend-Widget |
| 2 | `string` | `$formId` | Formular-Alias mit Präfix `auto_` |
| 3 | `array` | `$formData` | Formular-Konfiguration aus `tl_form` |
| 4 | `\Contao\Form` | `$form` | Die Formular-Instanz |

**Rückgabe:** `\Contao\Widget` – Die (ggf. modifizierte) Widget-Instanz.

**Zeitpunkt:** Während der Widget-Validierung bei Formularübermittlung.

```php
#[AsHook('validateFormField')]
class ValidateFormFieldListener
{
    public function __invoke(Widget $widget, string $formId, array $formData, Form $form): Widget
    {
        if ('myform' === $form->formID && 'mywidget' === $widget->name) {
            if ($widget->value === 'verbotenerWert') {
                $widget->addError('Dieser Wert ist nicht erlaubt.');
            }
        }
        return $widget;
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
