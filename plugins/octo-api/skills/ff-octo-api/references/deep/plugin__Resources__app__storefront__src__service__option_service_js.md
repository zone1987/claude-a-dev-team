# OptionService (Storefront) (`src/Resources/app/storefront/src/service/option.service.js`)

## Zweck
Ermittelt die aktuell gewählte OCTO-Options-UUID anhand des Shopware-Varianten-Switch-Selects (Mapping Variantenname → API-Option). Aktualisiert sich bei Variantenwechsel.

## Typ
- `export default class OptionSevice` (Klassenname-Tippfehler „Sevice")

## Felder
- `#_variantSwitchSelector` = `form[data-variant-switch] select`, `#_variantSelector`, `#_selectedOptionUuid`, `#_apiProduct`.

## Methoden
- `constructor(element, apiProduct)` — findet das Variant-Switch-Select im Parent, ermittelt initiale Option-UUID, registriert `change`-Listener.
- `#_onOptionChanged(event)` — aktualisiert UUID.
- `#_getSelectedOptionUuid(selectField)` — matcht den gewählten Options-Text gegen `apiProduct.product.options[].title/internalName` (Whitespace bereinigt), gibt `option.id`.
- `get selectedOptionUuid` — aktuelle UUID.

## Besonderheiten / Fallstricke
- Matching per **Name** (nicht ID) → bei abweichenden Whitespaces/Übersetzungen fragil.

## Bezüge
`buy-box.plugin.js` (übergibt `selectedOptionUuid` an `date-select`), Twig-Variantenselector.
