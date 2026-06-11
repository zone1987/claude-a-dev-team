# sw-product-detail-base Override (`src/Resources/app/administration/src/module/sw-product/view/sw-product-detail-base/index.js`)

## Zweck
Override der Produktdetail-Base-View; bindet nur das überschriebene Twig-Template ein (das die `sw-product-api-product-form`-Karte einfügt).

## Inhalt
- `import template from './sw-product-detail-base.html.twig'; export default { template };`

## Bezüge
`sw-product-detail-base.html.twig` (Template-Override), `component/sw-product-api-product-form/*`.
