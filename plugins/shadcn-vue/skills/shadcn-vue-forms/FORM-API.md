# Form — API

vee-validate API: https://vee-validate.logaretm.com/v4/api/
Zod API: https://zod.dev

## Anatomie

```vue
<template>
  <Form>
    <FormField v-slot="{ componentField }" name="fieldName">
      <FormItem>
        <FormLabel />
        <FormControl>
          <!-- Input-Komponente oder natives input -->
        </FormControl>
        <FormDescription />
        <FormMessage />
      </FormItem>
    </FormField>
  </Form>
</template>
```

## Sub-Komponenten

| Komponente | Herkunft | Beschreibung |
|---|---|---|
| `Form` | vee-validate (re-export) | Form-Root mit Validierungsschema |
| `FormField` | vee-validate `Field` (re-export) | Scoped-Slot fuer Feldkontext |
| `FormFieldArray` | vee-validate `FieldArray` (re-export) | Fuer Arrays von Feldern |
| `FormItem` | shadcn-vue | Behaelter, stellt eindeutige ID via Injection bereit |
| `FormLabel` | shadcn-vue | Label, verbindet sich automatisch mit FormItem-ID |
| `FormControl` | shadcn-vue | Slot-Wrapper, setzt ARIA-Attribute automatisch |
| `FormDescription` | shadcn-vue | Hilfetext (aria-describedby) |
| `FormMessage` | shadcn-vue | Fehlermeldung (vee-validate ErrorMessage) |

## FormField — Scoped Slot Props

| Prop | Beschreibung |
|---|---|
| `componentField` | v-bind-Objekt fuer shadcn-Komponenten (modelValue + onChange) |
| `field` | Objekt fuer native Inputs (value + onInput + onBlur) |
| `value` | Aktueller Feldwert |
| `handleChange` | Change-Handler-Funktion |
| `meta` | Feldzustand (valid, dirty, touched) |
| `errors` | Fehlerliste |

## useFormField — Composable

Gibt IDs und Feldstatus fuer eigene Komponenten zurueck:

```ts
const {
  id,              // Einzel-ID
  name,            // Feldname
  formItemId,      // `${id}-form-item`
  formDescriptionId, // `${id}-form-item-description`
  formMessageId,   // `${id}-form-item-message`
  error,           // errorMessage aus vee-validate
  valid,           // computed boolean
  isDirty,         // computed boolean
  isTouched,       // computed boolean
} = useFormField()
```

Muss innerhalb von `<FormField>` (vee-validate `FieldContextKey`) und `<FormItem>` (FORM_ITEM_INJECTION_KEY) verwendet werden.

## FormControl

Nutzt reka-ui `<Slot>` um ARIA-Attribute auf das erste Kind-Element anzuwenden:
- `id`: automatisch gesetzt
- `aria-describedby`: FormDescription-ID (+ FormMessage-ID wenn Fehler vorhanden)
- `aria-invalid`: true wenn Fehler vorhanden

## Checkbox-Sonderfall

Fuer Checkbox/Switch/Radio: `type="checkbox"` in FormField setzen, Wert ueber `value` + `handleChange` binden:

```vue
<FormField v-slot="{ value, handleChange }" type="checkbox" name="accepts">
  <FormItem>
    <FormControl>
      <Checkbox :checked="value" @update:checked="handleChange" />
    </FormControl>
    <FormMessage />
  </FormItem>
</FormField>
```
