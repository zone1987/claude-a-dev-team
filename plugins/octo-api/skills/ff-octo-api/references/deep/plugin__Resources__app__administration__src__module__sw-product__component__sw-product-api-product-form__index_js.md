# sw-product-api-product-form (`src/Resources/app/administration/src/module/sw-product/component/sw-product-api-product-form/index.js`)

## Zweck
Vue-Komponente in der Produktdetail-Admin, über die ein Shopware-Produkt einem OCTO-API-Produkt zugewiesen wird. Lädt verfügbare API-Produkte (gefiltert nach Supplier), legt bei „Apply" die `ff_octo_product`-Entity an und erzeugt Property-Group, Varianten, Medien und Preise.

## Typ
- Vue-Komponente (`template`, `inject`, `mixins` placeholder/notification).

## Injects
`repositoryFactory`, `octoProductApiService`, `propertyApiService`, `variantApiService`, `productMediaApiService`, `productPriceApiService`, `numberRangeService`.

## Props
- `allowEdit` (Bool, default true), `showSettingsApiProduct` (Bool, default true).

## Data
`octoProduct`, `apiProducts`, `apiSuppliers`, `selectedApiProduct`, `selectedApiSuppliers`, `isApiProductLoading`.

## Computed (Auswahl)
- `product`/`parentProduct` (Store `swProductDetail`), `isLoading`, `octoProductRepository` (`ff_octo_product`), `filteredApiProducts` (nach Supplier), `isApplyButtonDisabled`.

## Methoden (Apply-Flow)
- `loadApiProducts()` — `octoProductApiService.getProducts()`, baut Supplier-Liste (Labels `sw-product.apiProductForm.supplier.{identifier}`), `loadCurrentApiProduct()`.
- `loadCurrentApiProduct()` — lädt bei gesetzter `ffOctoProductId` das Detail-API-Produkt.
- `applyApiProductSettings(selectedApiProductId)` — `preSave(...)` → parallel `createProductMedia()` + `createProductVariants()` → dann `updatePrices()` → `reloadProduct()` + Success-Notification.
- `preSave(id)` — lädt API-Produkt, legt `ff_octo_product`-Entity an (id/uuid/identifier/product), setzt Name/Description/inaktiv/Preis 0/Produktnummer/Stock, speichert Produkt.
- `createProductVariants()` — `propertyApiService.createPropertyGroup(...)` → `variantApiService.createProductVariants(...)`.
- `createProductMedia()` — `productMediaApiService.assignProductMedia(...)`.
- `updatePrices()` — `productPriceApiService.updateProductPrices(octoProduct.product, product.id, identifier)`.
- Setter: `setName/setDescription/setInactive/setPrice/setProductNumber/setStock`.
- `reloadProduct()` — EventBus `reload-product-detail`.

## Besonderheiten / Fallstricke
- Neue Produkte werden **inaktiv** mit Preis 0 angelegt (erst nach Preis-Update sinnvoll aktivieren).
- Der Apply-Flow ruft genau die Plugin-Endpunkte (Property/Variant/Media/Price), die auch der AppServer (für RheinKurier) per Admin-API anspricht.
- Supplier-Labels über Snippets `sw-product.apiProductForm.supplier.*`.

## Bezüge
`core/service/api/*`, `Controller/{OctoProduct,Property,Variant,Media,Price}Controller.php`, `sw-product-api-product-form.html.twig`, `sw-product-api-product-form.scss`.
