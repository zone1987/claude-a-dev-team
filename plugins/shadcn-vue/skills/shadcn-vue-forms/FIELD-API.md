# Field — API

## Sub-Komponenten

| Komponente | Element | Beschreibung |
|---|---|---|
| `Field` | `<div role="group">` | Root-Container mit Orientierungsvarianten |
| `FieldGroup` | `<div>` | Gruppiert mehrere Fields (`@container/field-group`) |
| `FieldContent` | `<div>` | Bereich fuer Label + Description bei Checkboxen/Radios |
| `FieldLabel` | `<Label>` | Zugaengliches Label (wraps reka-ui Label) |
| `FieldTitle` | `<div>` | Nicht-label Title-Text (fuer FieldContent) |
| `FieldDescription` | `<p>` | Hilfetext unter dem Eingabefeld |
| `FieldError` | `<div role="alert">` | Fehlermeldung(en), dedupliziert |
| `FieldLegend` | `<legend>` | Legend fuer `<fieldset>` (FieldSet) |
| `FieldSet` | `<fieldset>` | Native fieldset fuer Radio-/Checkbox-Gruppen |
| `FieldSeparator` | `<div>` | Horizontaler Trenner innerhalb einer FieldGroup |

## Field

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `orientation` | `"vertical" \| "horizontal" \| "responsive"` | `"vertical"` | Layout-Richtung |
| `class` | `string` | - | - |

### Daten-Attribute (data-*)

| Attribut | Beschreibung |
|---|---|
| `data-invalid` | Markiert Field als ungueltig (Farbe auf destructive) |
| `data-disabled` | Markiert Field als deaktiviert (opacity-50 auf Label) |

### Orientierungsvarianten

| Variante | Verhalten |
|---|---|
| `vertical` (Standard) | Elemente vertikal gestapelt, volle Breite |
| `horizontal` | Label links (`flex-auto`), Control rechts (`items-center`) |
| `responsive` | Vertikal per Default, horizontal ab `@md` (Container Query) |

Hinweis: `responsive` nutzt `@md/field-group` Container Query — FieldGroup muss vorhanden sein.

## FieldError

| Prop | Typ | Beschreibung |
|---|---|---|
| `errors` | `Array<string \| { message: string \| undefined } \| undefined>` | Fehlermeldungen (Zod, Valibot, ArkType kompatibel) |
| `class` | `string` | - |

Verhalten:
- Kein `errors`-Array: rendert `<slot>` (manueller Inhalt)
- 1 unique Fehler: inline Text
- Mehrere unique Fehler: `<ul>` Liste
- Duplikate werden automatisch gefiltert

## FieldLegend

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | `"legend" \| "label"` | - | `legend`: text-base, `label`: text-sm |
| `class` | `string` | - | - |

## FieldLabel (Choice Card Pattern)

Wenn FieldLabel ein `<Field>` als Kind enthaelt, rendert es als "Choice Card":
- `w-full flex-col rounded-md border`
- `has-data-[state=checked]:bg-primary/5 border-primary` wenn ausgewaehlt

Nutzung: Checkbox/Radio innerhalb eines FieldLabel fuer klickbaren Card-Style.

## FieldSeparator

Optionaler Slot fuer Text-Label in der Mitte der Trennlinie (CSS-Overlay-Technik).

```vue
<FieldSeparator>oder</FieldSeparator>
```
