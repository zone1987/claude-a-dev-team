# Contao Hooks – Forms

Hooks for the form generator: loading fields, validating, processing and storing data.

---

## Contents

- [`compileFormFields`](#compileformfields)
- [`loadFormField`](#loadformfield)
- [`prepareFormData`](#prepareformdata)
- [`processFormData`](#processformdata)
- [`storeFormData`](#storeformdata)
- [`validateFormField`](#validateformfield)

## `compileFormFields`

**Purpose:** Triggered when the fields of a form are compiled. Allows modifying the field list before rendering.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$fields` | Array of `\Contao\FormFieldModel` instances |
| 2 | `string` | `$formId` | Form alias with the prefix `auto_` |
| 3 | `\Contao\Form` | `$form` | The form instance |

**Returns:** `array` – The (possibly modified) array of `FormFieldModel` instances.

**Timing:** While the form fields are compiled during rendering.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Form;

#[AsHook('compileFormFields')]
class CompileFormFieldsListener
{
    public function __invoke(array $fields, string $formId, Form $form): array
    {
        // Add, remove or modify fields dynamically
        return $fields;
    }
}
```

---

## `loadFormField`

**Purpose:** Triggered when a form field is loaded. Allows dynamic modification of widgets.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\Widget` | `$widget` | The current front end widget instance |
| 2 | `string` | `$formId` | Form alias with the prefix `auto_` |
| 3 | `array` | `$formData` | Form configuration from `tl_form` |
| 4 | `\Contao\Form` | `$form` | The form instance |

**Returns:** `\Contao\Widget` – The (possibly modified) widget instance.

**Timing:** When a form field is loaded from the form generator.

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

**Purpose:** Triggered after the form has been submitted, but **before** it is processed. Allows modifying or extending the form data, for example by adding file attachments.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array&` | `$submittedData` | User input (by reference) |
| 2 | `array` | `$labels` | Field labels of the form |
| 3 | `array` | `$fields` | Form fields as `\Contao\Widget` instances |
| 4 | `\Contao\Form` | `$form` | The form instance |
| 5 | `array&` | `$files` | Files array (Contao 5.2+, by reference) |

**Returns:** `void`

**Timing:** After submission, before further processing (e-mail, database persistence etc.).

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
        // Add a file attachment programmatically
        $files[] = [
            'name'     => 'MyFile.txt',
            'tmp_name' => '/path/to/MyFile.txt',
            'type'     => 'text/plain',
        ];
        // Compute additional fields
        $submittedData['computed_deadline'] = strtotime('+1 hour');
    }
}
```

---

## `processFormData`

**Purpose:** Triggered after a form has been submitted. For your own processing logic after the standard flow.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$submittedData` | Submitted form data |
| 2 | `array` | `$formData` | Form configuration from `tl_form` |
| 3 | `array\|null` | `$files` | Information about uploaded files |
| 4 | `array` | `$labels` | Field labels of the form |
| 5 | `\Contao\Form` | `$form` | The form instance |

**Returns:** `void`

**Timing:** After the form has been processed completely.

```php
#[AsHook('processFormData')]
class ProcessFormDataListener
{
    public function __invoke(array $submittedData, array $formData, array|null $files, array $labels, Form $form): void
    {
        // e.g. forward the data to an external API
    }
}
```

---

## `storeFormData`

**Purpose:** Triggered **before** submitted form data is written to the database. Allows modifying the data that is about to be stored.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$data` | The record that is stored |
| 2 | `\Contao\Form` | `$form` | The form instance |

**Returns:** `array` – The (possibly modified) record array.

**Timing:** Immediately before the write to the database table.

```php
#[AsHook('storeFormData')]
class StoreFormDataListener
{
    public function __invoke(array $data, Form $form): array
    {
        // Assign the current front end member
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

**Purpose:** Triggered when a form field is submitted. Allows custom validation logic.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\Widget` | `$widget` | The current front end widget |
| 2 | `string` | `$formId` | Form alias with the prefix `auto_` |
| 3 | `array` | `$formData` | Form configuration from `tl_form` |
| 4 | `\Contao\Form` | `$form` | The form instance |

**Returns:** `\Contao\Widget` – The (possibly modified) widget instance.

**Timing:** During widget validation on form submission.

```php
#[AsHook('validateFormField')]
class ValidateFormFieldListener
{
    public function __invoke(Widget $widget, string $formId, array $formData, Form $form): Widget
    {
        if ('myform' === $form->formID && 'mywidget' === $widget->name) {
            if ($widget->value === 'forbiddenValue') {
                $widget->addError('This value is not allowed.');
            }
        }
        return $widget;
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
