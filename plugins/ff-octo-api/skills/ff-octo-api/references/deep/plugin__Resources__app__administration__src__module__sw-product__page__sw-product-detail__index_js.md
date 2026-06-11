# sw-product-detail Override (`src/Resources/app/administration/src/module/sw-product/page/sw-product-detail/index.js`)

## Zweck
Override der Shopware-Produktdetail-Page: fügt einen „API-Produkt"-Mode-Tab hinzu, erweitert die Produkt-Criteria um `ffOctoProduct` und reagiert auf Reload-Events.

## Typ
- Component-Override (Vue, `$super`-Pattern).

## Computed
- `getModeSettingGeneralTab()` — ergänzt Eintrag `api_product` (Label `sw-product.detailBase.cardTitleApiProduct`).
- `productCriteria()` — `addAssociation('ffOctoProduct')`.

## Methoden
- `createdComponent()` — registriert `reload-product-detail`→`loadAll` (EventBus), pusht `api_product` in `store.modeSettings`, ruft `$super`.
- `beforeDestroy()` — entfernt den EventBus-Listener.

## Bezüge
`component/sw-product-api-product-form/*` (emittiert `reload-product-detail`), `view/sw-product-detail-base/*`.
