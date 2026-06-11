# sw-product Modul-Registrierung (`src/Resources/app/administration/src/module/sw-product/index.js`)

## Zweck
Registriert die OCTO-Admin-Komponente und überschreibt zwei Shopware-Produkt-Komponenten.

## Inhalt
- `Shopware.Component.register('sw-product-api-product-form', …)` — neue Komponente.
- `Shopware.Component.override('sw-product-detail', …)` — Page-Override.
- `Shopware.Component.override('sw-product-detail-base', …)` — View-Override (Template).

## Bezüge
`component/sw-product-api-product-form/*`, `page/sw-product-detail/index.js`, `view/sw-product-detail-base/index.js`.
